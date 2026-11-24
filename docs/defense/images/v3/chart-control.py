"""Draw the speed control charts of the defense slides from chart-control-data.csv.

Run from this folder:  python chart-control.py   (needs matplotlib)

Data sources, all recorded on the robot at 0.1 s per sample:
- open loop step (PWM 143) and the run with the initial PSO gains: the files
  step_response_velocity_lazo_abierto.npy and step_response_velocity.npy in
  firmware/pid_config of ros2-indoor-exploration-robot;
- run with the final gains: read from the figure respuesta_escalon_final_mvp.png
  of the same folder. The reading uses the figure's grid lines as the scale and
  was checked on the initial PSO run, where all 202 samples matched the recorded
  data after rounding to the 0.01 m/s resolution of the measurement.

The fitted curve is the right wheel model exactly as the identification simulates it:
Euler steps of 0.1 s with the parameters of the first PSO, fitted to the measured speed
smoothed over 5 samples. Between samples it is drawn with the exponential that passes
through the same points. Its marks (L, tau, Km) are separate overlay files so the slide
can reveal them one click at a time.
Each SVG is drawn at the size it has on the slide, so 11 pt in the file is 11 pt on screen.
"""

import csv
import logging
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
INK, MUTED, GRID, AXIS = "#111827", "#6B7280", "#E5E7EB", "#9CA3AF"
LEFT, RIGHT, MODEL = "#004EAA", "#C2410C", "#654A97"
KM, TAU, L = 0.000890, 0.3485, 0.0692  # right wheel, first PSO
STEP_T, PWM = 1.0, 143

plt.rcParams.update(
    {
        "svg.fonttype": "none",
        "svg.hashsalt": "chart-control",
        "font.family": ["Calibri", "Carlito", "DejaVu Sans"],
        "font.size": 11,
        "axes.edgecolor": AXIS,
        "axes.labelcolor": MUTED,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)
comma = FuncFormatter(lambda v, _: f"{v:.2f}".replace(".", ","))
comma0 = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))


def save(fig, path):
    """Write the SVG with no date and no trailing spaces, so the same data gives the same file."""
    fig.savefig(path, transparent=True, metadata={"Date": None})
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text(
        "\n".join(line.rstrip() for line in lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def load():
    with open(HERE / "chart-control-data.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}


def style(ax, ylabel=None):
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, labelsize=11.5)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11.5)


def step_input(d):
    fig = plt.figure(figsize=(7.60, 1.05))
    ax = fig.add_axes([0.10, 0.20, 0.87, 0.66])
    ax.step(d["t_s"], d["open_loop_pwm"], where="post", color=INK, linewidth=2.4)
    ax.set_xlim(0, 10)
    ax.set_ylim(-12, 175)
    ax.set_yticks([0, 143], ["0", "56 %"])
    ax.set_xticks(range(0, 11, 2))
    ax.tick_params(labelbottom=False)
    ax.text(
        1.25,
        152,
        "pulso fijo de potencia desde t = 1 s",
        fontsize=12.5,
        color=INK,
        va="bottom",
    )
    style(ax, "potencia")
    save(fig, HERE / "chart-control-step-input.svg")
    plt.close(fig)


def step_output(d):
    fig = plt.figure(figsize=(7.60, 2.45))
    ax = fig.add_axes([0.10, 0.20, 0.87, 0.74])
    ax.plot(
        d["t_s"],
        d["open_loop_left_mps"],
        color=LEFT,
        linewidth=2.2,
        marker="o",
        markersize=2.6,
        label="rueda izquierda",
    )
    ax.plot(
        d["t_s"],
        d["open_loop_right_mps"],
        color=RIGHT,
        linewidth=2.2,
        marker="o",
        markersize=2.6,
        label="rueda derecha",
    )
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 0.16)
    ax.set_yticks([0, 0.05, 0.10, 0.13])
    ax.yaxis.set_major_formatter(comma)
    ax.set_xticks(range(0, 11, 2))
    ax.set_xlabel("tiempo (s)", fontsize=11.5)
    style(ax, "velocidad (m/s)")
    ax.text(
        9.9,
        0.142,
        "se estabilizan cerca de 0,13 m/s",
        fontsize=12,
        color=INK,
        ha="right",
    )
    ax.legend(loc="lower right", fontsize=12, frameon=False, ncol=2, handlelength=1.6)
    save(fig, HERE / "chart-control-step-output.svg")
    plt.close(fig)


def fitted_curve(d):
    """Right wheel model at the samples, and the exponential through those samples."""
    t, u = d["t_s"], d["open_loop_pwm"]
    model = np.zeros_like(t)
    for k in range(1, len(t)):
        model[k] = model[k - 1] + (0.1 / TAU) * (
            KM * u[max(k - int(L / 0.1), 0)] - model[k - 1]
        )
    start = t[np.argmax(model > 0)] - 0.1
    a = 1 - 0.1 / TAU
    tm = np.linspace(0.5, 3.0, 600)
    ym = np.where(tm < start, 0, KM * PWM * (1 - a ** ((tm - start) / 0.1)))
    return tm, ym


def fopdt(d):
    t = d["t_s"]
    plateau = KM * PWM
    tm, ym = fitted_curve(d)
    raw = d["open_loop_right_mps"]
    smooth = np.convolve(np.pad(raw, 2, mode="symmetric"), np.ones(5) / 5, mode="valid")
    fig = plt.figure(figsize=(7.44, 4.15))
    ax = fig.add_axes([0.10, 0.13, 0.87, 0.72])
    sel = (t >= 0.5) & (t <= 3.0)
    base = [
        ax.axvline(STEP_T, color=AXIS, linewidth=1.3, linestyle=":"),
        ax.text(STEP_T + 0.03, 0.150, "escalón", fontsize=12, color=MUTED, va="center"),
        ax.plot(
            t[sel],
            smooth[sel],
            color=AXIS,
            linewidth=2.2,
            label="medido suavizado: lo que ajusta el PSO",
        )[0],
        ax.plot(
            tm, ym, color=MODEL, linewidth=2.6, label="curva ajustada por el 1.er PSO"
        )[0],
        ax.plot(
            t[sel],
            d["open_loop_right_mps"][sel],
            "o",
            color=INK,
            markersize=7,
            label="medido, rueda derecha",
        )[0],
    ]
    ax.set_xlim(0.5, 3.0)
    ax.set_ylim(0, 0.16)
    ax.set_yticks([0, 0.04, 0.08, 0.12])
    ax.yaxis.set_major_formatter(comma)
    ax.xaxis.set_major_formatter(comma0)
    ax.set_xlabel("tiempo (s)", fontsize=12)
    style(ax, "velocidad (m/s)")
    ax.tick_params(labelsize=12)
    leg = ax.legend(
        loc="upper left",
        bbox_to_anchor=(0.0, 1.17),
        fontsize=12,
        frameon=False,
        ncol=2,
        handlelength=1.6,
        columnspacing=1.2,
    )
    box = {
        "boxstyle": "round,pad=0.35",
        "facecolor": "white",
        "edgecolor": MODEL,
        "linewidth": 1.4,
    }
    line = {"arrowstyle": "-", "color": MODEL, "linewidth": 1.4}

    y63 = 0.632 * plateau
    t63 = np.interp(y63, ym, tm)
    marks = {
        "l": [
            ax.axvspan(STEP_T, STEP_T + L, color=MODEL, alpha=0.35, linewidth=0),
            ax.annotate(
                "1 · Retardo (L): despega casi al instante (< 0,1 s)",
                xy=(STEP_T + L / 2, 0.006),
                xytext=(1.22, 0.012),
                fontsize=13,
                color=INK,
                fontweight="bold",
                bbox=box,
                arrowprops=line,
            ),
        ],
        "tau": [
            ax.plot([0.5, t63], [y63, y63], color=MODEL, linewidth=1.6, linestyle="--")[
                0
            ],
            ax.plot([t63], [y63], "o", color=MODEL, markersize=9)[0],
            ax.text(
                0.53,
                y63 + 0.004,
                "63 %",
                fontsize=12.5,
                color=INK,
                fontweight="bold",
            ),
            ax.annotate(
                "2 · Rapidez (τ): acelera en ~0,3 s (tiempo al 63 %)",
                xy=(t63 + 0.01, y63 - 0.002),
                xytext=(1.30, 0.046),
                fontsize=13,
                color=INK,
                fontweight="bold",
                bbox=box,
                arrowprops=line,
                linespacing=1.15,
            ),
        ],
        "km": [
            ax.annotate(
                "",
                xy=(2.88, 0),
                xytext=(2.88, plateau),
                arrowprops={
                    "arrowstyle": "<->",
                    "color": MODEL,
                    "linewidth": 2,
                    "shrinkA": 0,
                    "shrinkB": 0,
                },
            ),
            ax.text(
                2.80,
                0.093,
                "3 · Fuerza / Ganancia (Km):\nvelocidad final ÷ potencia aplicada",
                fontsize=13,
                color=INK,
                fontweight="bold",
                ha="right",
                va="center",
                bbox=box,
                linespacing=1.2,
            ),
        ],
    }
    for group in marks.values():
        for a in group:
            a.set_visible(False)
    save(fig, HERE / "chart-control-fopdt.svg")
    for a in base + [leg]:
        a.set_visible(False)
    ax.axis("off")
    for name, group in marks.items():
        for a in group:
            a.set_visible(True)
        save(fig, HERE / f"chart-control-fopdt-{name}.svg")
        for a in group:
            a.set_visible(False)
    plt.close(fig)


def closed_loop(d):
    t = d["t_s"]
    fig = plt.figure(figsize=(7.60, 3.80))
    axes = [
        fig.add_axes([0.085, 0.14, 0.42, 0.62]),
        fig.add_axes([0.565, 0.14, 0.42, 0.62]),
    ]
    panels = [
        (
            "Rueda izquierda",
            "left",
            LEFT,
            1.8,
            "subida 0,8 s",
            "antes: queda corta\nen 0,12 m/s",
            (3.0, 0.12),
        ),
        (
            "Rueda derecha",
            "right",
            RIGHT,
            2.4,
            "subida 1,4 s",
            "antes: lenta,\nllega a los 6 s",
            (2.6, 0.11),
        ),
    ]
    for ax, (title, key, color, t_up, rise, before, before_xy) in zip(
        axes, panels
    ):
        ax.plot(t, d["reference_mps"], color=INK, linewidth=1.4, linestyle=(0, (2, 2)))
        ax.plot(
            t, d[f"initial_pso_{key}_mps"], color=AXIS, linewidth=2.0, linestyle="--"
        )
        ax.plot(t, d[f"final_{key}_mps"], color=color, linewidth=2.6)
        ax.annotate(
            "",
            xy=(STEP_T, 0.035),
            xytext=(t_up, 0.035),
            arrowprops={
                "arrowstyle": "<->",
                "color": INK,
                "linewidth": 1.5,
                "shrinkA": 0,
                "shrinkB": 0,
            },
        )
        ax.text(
            t_up + 0.15,
            0.035,
            rise,
            fontsize=13,
            color=INK,
            fontweight="bold",
            va="center",
        )
        ax.annotate(
            before,
            xy=before_xy,
            xytext=(3.5, 0.068),
            fontsize=12,
            color=MUTED,
            linespacing=1.1,
            arrowprops={"arrowstyle": "-", "color": AXIS, "linewidth": 1.3},
        )
        ax.set_title(
            title, fontsize=13, color=INK, fontweight="bold", loc="left", pad=5
        )
        ax.set_xlim(0, 8)
        ax.set_xticks(range(0, 9, 2))
        ax.set_ylim(0, 0.16)
        ax.set_yticks([0, 0.05, 0.10, 0.13])
        ax.yaxis.set_major_formatter(comma)
        ax.set_xlabel("tiempo (s)", fontsize=11.5)
        style(ax)
    axes[0].set_ylabel("velocidad (m/s)", fontsize=11.5)
    handles = [
        plt.Line2D([], [], color=INK, linewidth=1.4, linestyle=(0, (2, 2))),
        plt.Line2D([], [], color=AXIS, linewidth=2.0, linestyle="--"),
        plt.Line2D([], [], color=LEFT, linewidth=2.6),
        plt.Line2D([], [], color=RIGHT, linewidth=2.6),
    ]
    fig.legend(
        handles,
        [
            "velocidad pedida: 0,13 m/s",
            "antes: PSO inicial",
            "después, rueda izq.",
            "después, rueda der.",
        ],
        loc="upper center",
        ncol=2,
        fontsize=12,
        frameon=False,
        handlelength=1.8,
        columnspacing=1.4,
        bbox_to_anchor=(0.53, 1.02),
    )
    save(fig, HERE / "chart-control-closed-loop.svg")
    plt.close(fig)


if __name__ == "__main__":
    data = load()
    step_input(data)
    step_output(data)
    fopdt(data)
    closed_loop(data)
