"""Generate rehearsal audio for the defense from script-v3.md with a Chilean Spanish neural voice.

Run from docs/defense:  python generar_audio_guion.py
Requires: pip install edge-tts==7.3.1 and internet access.

Writes to audio_guion/:
- one MP3 per main slide (01_portada.mp3 ... 30_gracias.mp3),
- defensa_completa.mp3, all main slides with 1.5 s of silence between them,
- respaldos_respuestas.mp3, the short answers for R1 to R11.

script-v3.md is only read. The pronunciation fixes are applied in memory, so the
script keeps its normal spelling. MP3 files are joined at frame level, so no
ffmpeg is needed.
"""

import argparse
import asyncio
import re
import sys
import unicodedata
from pathlib import Path

import edge_tts

VOICE = "es-CL-LorenzoNeural"
RATE = "-10%"
CLICK_PAUSE_S = 0.6
SLIDE_PAUSE_S = 1.5
TIME_LIMIT_S = 30 * 60
PARALLEL_REQUESTS = 4

SLIDE_RE = re.compile(r"^Lámina (\d+) · (.+?) \((\d+) s\)$")
BACKUP_RE = re.compile(r"^(R\d+) · (.+?) \(lámina \d+\)$")


def split_camel(word):
    return " ".join(re.findall(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|\d+", word))


# Order matters: longer and more specific patterns first.
PRONUNCIATION = [
    (r"(\d) (\d{3})\b", r"\1\2"),
    (r"(?:https?://)?github\.com/\S+", "nuestro repositorio abierto en GitHub"),
    (
        r"repositorio de GitHub,?\s*ros2-indoor-exploration-robot",
        "repositorio abierto en GitHub",
    ),
    (r"ros2-indoor-exploration-robot", "el repositorio del proyecto"),
    (r"\b(\w+)\.py\b", lambda m: "el script " + split_camel(m.group(1))),
    (r"(?<=[A-Za-z])_(?=[A-Za-z])", " "),
    (r"\bLIDAR 2D\b", "láidar dos de"),
    (r"\bLIDAR 3D\b", "láidar tres de"),
    (r"\bRPLidar\b", "erre pe láidar"),
    (r"\bLIDAR\b", "láidar"),
    (r"\bROS 2\b", "Ros dos"),
    (r"\bROS 1\b", "Ros uno"),
    (r"\bROS\b", "Ros"),
    (r"\bRViz2\b", "erre viz dos"),
    (r"\bNav2\b", "Nav dos"),
    (r"\bSLAM\b", "eslam"),
    (r"\bA\*", "A estrella"),
    (r"\bDWB\b", "de doble ve be"),
    (r"\bPSO\b", "pe ese o"),
    (r"\bFOPDT\b", "efe o pe de te"),
    (r"\bPWM\b", "pe doble ve eme"),
    (r"\bPID\b", "pe i de"),
    (r"\bPI\b", "pe i"),
    (r"\bIMU\b", "i eme u"),
    (r"\bURDF\b", "u erre de efe"),
    (r"\bPLA\+", "pe ele a plus"),
    (r"\bKm\b", "ka eme"),
    (r"τ", "tau"),
    (r"\bKp\b", "ka pe"),
    (r"\bKd\b", "ka de"),
    (r"\bKi\b", "ka i"),
    (r"\bKo\b", "ka o"),
    (r"\bL298N\b", "ele doscientos noventa y ocho ene"),
    (r"\bTB6612FNG\b", "te be seis seis uno dos efe ene ge"),
    (r"\bDRV8871\b", "de erre ve ocho ocho siete uno"),
    (r"\bCycloneDDS\b", "Cyclone de de ese"),
    (r"\bANYmal\b", "énimal"),
    (r"\bUTEM\b", "Utem"),
    (r"\bWi-Fi\b", "wifi"),
    (r"\bGPS\b", "ge pe ese"),
    (r"\bCPU\b", "ce pe u"),
    (r"\bMIT\b", "eme i te"),
    (r"\bIP\b", "i pe"),
    (r"\bRTT\b", "erre te te"),
    (r"\bLCM\b", "ele ce eme"),
    (r"\bMPPI\b", "eme pe pe i"),
    (r"\bRRT\b", "erre erre te"),
    (r"\bDC\b", "de ce"),
    (r"\b2D\b", "dos de"),
    (r"\b3D\b", "tres de"),
    (r"\b1\.er\b", "primer"),
    (r"\b2\.º", "segundo"),
    (r"(\d)\s*m/s\b", r"\1 metros por segundo"),
    (r"(\d)\s*m²", r"\1 metros cuadrados"),
    (r"(\d)\s*cm\b", r"\1 centímetros"),
    (r"(\d)\s*ms\b", r"\1 milisegundos"),
    (r"(\d)\s*Hz\b", r"\1 hertz"),
    (r"(\d)\s*%", r"\1 por ciento"),
    (r"(\d)\s*×", r"\1 veces"),
    (r"°", " grados"),
    (r"±", " más menos "),
    (r"≈", "aproximadamente "),
    (r"[«»*`]", ""),
    (r"\s{2,}", " "),
]


def speakable(text):
    """Turn one piece of narration into what the voice should read."""
    text = re.sub(r"\[[^\]]*\]", " ", text)
    for pattern, repl in PRONUNCIATION:
        text = re.sub(pattern, repl, text)
    return text.strip()


def segments(text):
    """Split narration at each [CLIC]; each piece is read and followed by a short pause."""
    return [speakable(part) for part in text.split("[CLIC]")]


def slug(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", ascii_name.lower()).strip("_")


def read_script(path):
    """Return (main slides, backup answers) parsed from the script."""
    lines = path.read_text(encoding="utf-8").splitlines()
    slides, backups = [], []
    section = "main"
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "## Láminas de respaldo":
            section = "skip"
        elif line == "## Respuestas breves":
            section = "backups"
        elif line.startswith("## ") and section == "backups":
            section = "end"
        slide = SLIDE_RE.match(line) if section == "main" else None
        backup = BACKUP_RE.match(line) if section == "backups" else None
        if slide or backup:
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            while i < len(lines) and lines[i].strip():
                body.append(lines[i].strip())
                i += 1
            text = " ".join(body)
            if slide:
                slides.append((int(slide.group(1)), slide.group(2), text))
            else:
                backups.append((backup.group(1), backup.group(2), text))
            continue
        i += 1
    return slides, backups


# MP3 frame handling (MPEG audio layer III)
BITRATE_KBPS = {
    1: [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],
    2: [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],
}
SAMPLE_RATE = {
    3: [44100, 48000, 32000],
    2: [22050, 24000, 16000],
    0: [11025, 12000, 8000],
}


def frames(data):
    """Yield (offset, length, seconds) for each layer III frame, skipping ID3 tags."""
    pos = 0
    if data[:3] == b"ID3":
        size = (data[6] << 21) | (data[7] << 14) | (data[8] << 7) | data[9]
        pos = 10 + size
    while pos + 4 <= len(data):
        if data[pos] != 0xFF or (data[pos + 1] & 0xE0) != 0xE0:
            pos += 1
            continue
        version = (data[pos + 1] >> 3) & 0x3
        layer = (data[pos + 1] >> 1) & 0x3
        br_idx = data[pos + 2] >> 4
        sr_idx = (data[pos + 2] >> 2) & 0x3
        padding = (data[pos + 2] >> 1) & 0x1
        if version == 1 or layer != 1 or br_idx in (0, 15) or sr_idx == 3:
            pos += 1
            continue
        rate = SAMPLE_RATE[version][sr_idx]
        kbps = BITRATE_KBPS[1 if version == 3 else 2][br_idx]
        samples = 1152 if version == 3 else 576
        length = (144 if version == 3 else 72) * kbps * 1000 // rate + padding
        yield pos, length, samples / rate
        pos += length


def frame_bytes(data):
    return b"".join(data[o : o + n] for o, n, _ in frames(data))


def duration(data):
    return sum(s for _, _, s in frames(data))


def silence(like, seconds):
    """Silent frames with the same format as `like`: a valid header followed by zeros."""
    offset, length, frame_s = next(frames(like))
    header = bytearray(like[offset : offset + 4])
    header[2] &= 0xFD
    length -= (like[offset + 2] >> 1) & 0x1
    frame = bytes(header) + bytes(length - 4)
    return frame * max(1, round(seconds / frame_s))


async def synthesize(text, voice, rate, limit):
    async with limit:
        for attempt in range(4):
            try:
                audio = bytearray()
                async for chunk in edge_tts.Communicate(
                    text, voice, rate=rate
                ).stream():
                    if chunk["type"] == "audio":
                        audio += chunk["data"]
                if audio:
                    return frame_bytes(bytes(audio))
                raise RuntimeError("empty audio")
            except Exception as exc:
                if attempt == 3:
                    raise RuntimeError(f"TTS failed for: {text[:60]}...") from exc
                await asyncio.sleep(2 * (attempt + 1))


async def render(parts, voice, rate, limit):
    """parts: list of texts; consecutive non-empty parts are joined with a click pause."""
    audios = await asyncio.gather(
        *(synthesize(p, voice, rate, limit) for p in parts if p)
    )
    out = bytearray()
    for k, audio in enumerate(audios):
        if k:
            out += silence(audio, CLICK_PAUSE_S)
        out += audio
    return bytes(out)


def mmss(seconds):
    s = round(seconds)
    return f"{s // 60:02d}:{s % 60:02d}"


async def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Genera el audio de ensayo de la defensa a partir del guion."
    )
    parser.add_argument("--script", type=Path, default=here / "script-v3.md")
    parser.add_argument("--out", type=Path, default=here / "audio_guion")
    parser.add_argument("--voice", default=VOICE)
    parser.add_argument("--rate", default=RATE)
    args = parser.parse_args()

    slides, backups = read_script(args.script)
    if [n for n, _, _ in slides] != list(range(1, len(slides) + 1)) or not slides:
        sys.exit(f"Se esperaban láminas numeradas desde 1 en {args.script}")
    args.out.mkdir(exist_ok=True)
    limit = asyncio.Semaphore(PARALLEL_REQUESTS)

    rendered = await asyncio.gather(
        *(render(segments(text), args.voice, args.rate, limit) for _, _, text in slides)
    )
    full = bytearray()
    print(f"{'N.º':>3}  {'Archivo':<42} {'Duración':>8}")
    for (n, name, _), audio in zip(slides, rendered):
        path = args.out / f"{n:02d}_{slug(name)}.mp3"
        path.write_bytes(audio)
        print(f"{n:>3}  {path.name:<42} {mmss(duration(audio)):>8}")
        if full:
            full += silence(audio, SLIDE_PAUSE_S)
        full += audio
    (args.out / "defensa_completa.mp3").write_bytes(full)
    total = duration(bytes(full))
    print(f"\nTotal defensa_completa.mp3: {mmss(total)} ({total:.1f} s)")

    answers = await asyncio.gather(
        *(
            render(
                [speakable(f"Respaldo {code[1:]}. {title}."), *segments(text)],
                args.voice,
                args.rate,
                limit,
            )
            for code, title, text in backups
        )
    )
    joined = bytearray()
    for audio in answers:
        if joined:
            joined += silence(audio, SLIDE_PAUSE_S)
        joined += audio
    if joined:
        (args.out / "respaldos_respuestas.mp3").write_bytes(joined)
        print(
            f"Total respaldos_respuestas.mp3 ({len(answers)} respuestas): {mmss(duration(bytes(joined)))}"
        )

    if total >= TIME_LIMIT_S:
        sys.exit("La defensa completa supera los 30 minutos.")
    print("Bajo el límite de 30 minutos.")


if __name__ == "__main__":
    asyncio.run(main())
