"""Draw the explanatory diagrams of the defense slides as SVG files.

Run from this folder:  python diagrams.py   (standard library only)

Every diagram is a schematic drawn by hand for the slides, not data. Files that
end in -layer-N are the same size as their base file, so a slide can stack them
and animate each part on its own. Labels use Calibri, which PowerPoint has and
LibreOffice maps to Carlito.
"""

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent

BLUE = "#004EAA"
GREEN = "#78BF26"
DARK_GREEN = "#3B6E10"
TEAL = "#0E7490"
ORANGE = "#CB6B22"
PURPLE = "#654A97"
RED = "#C2410C"
YELLOW = "#FACC15"
INK = "#111827"
GRAY = "#6B7280"
MID = "#9CA3AF"
LIGHT = "#D1D5DB"
PALE = "#E5E7EB"
PAPER = "#F3F4F6"
FONT = "Calibri, Carlito, Arial, sans-serif"


def svg(width, height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">{"".join(body)}</svg>\n'
    )


def clipped(width, height, body, inset=6):
    return [
        f'<clipPath id="frame"><rect x="{inset}" y="{inset}" width="{width - 2 * inset}" '
        f'height="{height - 2 * inset}" rx="4"/></clipPath>',
        '<g clip-path="url(#frame)">',
        *body,
        "</g>",
    ]


def text(x, y, value, size=13, color=INK, weight="normal", anchor="middle"):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{value}</text>'
    )


def line(x1, y1, x2, y2, color=INK, width=2, dash=None, cap="round", opacity=1):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
        f'stroke-width="{width}" stroke-linecap="{cap}"{dash_attr} opacity="{opacity}"/>'
    )


def rect(x, y, w, h, fill="none", stroke="none", width=0, rx=0, dash=None, opacity=1):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{width}"{dash_attr} opacity="{opacity}"/>'
    )


def circle(cx, cy, r, fill="none", stroke="none", width=0, opacity=1, dash=None):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{width}" opacity="{opacity}"{dash_attr}/>'
    )


def path(d, color=INK, width=2, fill="none", dash=None, opacity=1):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{dash_attr} opacity="{opacity}"/>'
    )


def arrow(x1, y1, x2, y2, color=INK, width=2, head=8, dash=None):
    angle = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - head * math.cos(angle - 0.45), y2 - head * math.sin(angle - 0.45))
    right = (x2 - head * math.cos(angle + 0.45), y2 - head * math.sin(angle + 0.45))
    tip = (
        f'<path d="M{left[0]:.1f},{left[1]:.1f} L{x2:.1f},{y2:.1f} L{right[0]:.1f},{right[1]:.1f} Z" '
        f'fill="{color}" stroke="{color}" stroke-width="1" stroke-linejoin="round"/>'
    )
    return line(x1, y1, x2, y2, color, width, dash) + tip


def cross(cx, cy, size=10, color=RED, width=3.5):
    return line(cx - size, cy - size, cx + size, cy + size, color, width) + line(
        cx - size, cy + size, cx + size, cy - size, color, width
    )


def write(name, content):
    (HERE / name).write_text(content, encoding="utf-8", newline="\n")


def l298n():
    body = [rect(20, 20, 360, 300, fill="#C81E1E", stroke="#8F1414", width=3, rx=12)]
    for x in (34, 366):
        for y in (34, 306):
            body.append(circle(x, y, 7, fill="#F3F4F6", stroke="#8F1414", width=2))
    body.append(rect(110, 40, 180, 120, fill="#1F2937", stroke="#111827", width=2, rx=4))
    for i in range(9):
        x = 122 + i * 19.5
        body.append(rect(x, 46, 9, 108, fill="#374151", stroke="#0B1220", width=1, rx=2))
    body.append(rect(150, 168, 100, 36, fill="#111827", rx=3))
    body.append(text(200, 192, "L298N", 16, "#E5E7EB", "bold"))
    for x0 in (36, 300):
        body.append(rect(x0, 120, 64, 84, fill="#1D4ED8", stroke="#1E3A8A", width=2, rx=4))
        for k in range(2):
            cy = 141 + k * 42
            body.append(circle(x0 + 32, cy, 13, fill="#D1D5DB", stroke="#4B5563", width=2))
            body.append(line(x0 + 23, cy, x0 + 41, cy, "#4B5563", 3))
    body.append(rect(70, 236, 126, 64, fill="#1D4ED8", stroke="#1E3A8A", width=2, rx=4))
    for k in range(3):
        cx = 91 + k * 42
        body.append(circle(cx, 268, 13, fill="#D1D5DB", stroke="#4B5563", width=2))
        body.append(line(cx - 9, 268, cx + 9, 268, "#4B5563", 3))
    body.append(rect(222, 250, 140, 36, fill="#111827", rx=3))
    for k in range(6):
        body.append(rect(230 + k * 22, 260, 12, 16, fill="#FBBF24", rx=1))
    for x in (250, 300):
        body.append(rect(x, 212, 22, 26, fill="#111827", rx=2))
    body.append(circle(330, 228, 6, fill="#F87171", stroke="#7F1D1D", width=1.5))
    body.append(rect(40, 214, 30, 16, fill="#F3F4F6", rx=2))
    return svg(400, 340, body)


def lidar_plane():
    width, height = 560, 250
    floor_y = 222
    plane_y = 112
    base = [
        line(10, floor_y, 550, floor_y, GRAY, 3),
        rect(40, 140, 118, 70, fill="#1F2937", rx=14),
        circle(70, 212, 12, fill=INK),
        circle(134, 214, 7, fill=INK),
        rect(80, 116, 50, 24, fill="#111827", rx=6),
        rect(88, 106, 34, 12, fill="#374151", rx=4),
        rect(500, 40, 34, floor_y - 40, fill=PALE, stroke=MID, width=2),
    ]
    beam = [
        line(122, plane_y, 498, plane_y, GREEN, 3.5),
        circle(498, plane_y, 7, fill=GREEN),
        rect(495, plane_y - 30, 8, 60, fill=GREEN, opacity=0.9, rx=2),
        line(122, plane_y, 380, plane_y - 2, GREEN, 1.4, "5 6", opacity=0.6),
        text(300, plane_y - 14, "plano del láser", 22, DARK_GREEN, "bold"),
    ]
    outside = [
        rect(232, 182, 62, 40, fill="none", stroke=MID, width=2.5, dash="6 5", rx=3),
        text(263, 246, "caja baja", 20, GRAY),
        rect(410, 58, 90, 12, fill="none", stroke=MID, width=2.5, dash="6 5", rx=2),
        text(430, 46, "repisa en altura", 20, GRAY),
    ]
    return (
        svg(width, height, base),
        svg(width, height, beam),
        svg(width, height, outside),
    )


def lidar_surfaces():
    width, height = 560, 170
    body = [
        rect(40, 24, 10, 92, fill="#BFDBFE", stroke="#60A5FA", width=2),
        line(160, 70, 52, 70, MID, 2.5, "6 5"),
        arrow(52, 70, 140, 118, MID, 2.5, 10, "6 5"),
        text(100, 158, "espejo o metal", 20, GRAY),
        rect(296, 24, 8, 92, fill="#E0F2FE", stroke="#7DD3FC", width=2, opacity=0.9),
        arrow(210, 70, 392, 70, MID, 2.5, 10, "6 5"),
        text(300, 158, "vidrio", 20, GRAY),
        rect(462, 24, 72, 92, fill="#111827", rx=4),
        arrow(410, 70, 460, 70, MID, 2.5, 10, "6 5"),
        circle(486, 70, 5, fill=MID, opacity=0.6),
        text(498, 158, "negro mate", 20, GRAY),
    ]
    return svg(width, height, body)


def windup():
    width, height = 520, 250
    left, right, top, bottom = 44, 500, 40, 214
    goal_y = 106
    cap_y = 62
    axes = [
        line(left, bottom, right, bottom, GRAY, 2),
        line(left, top, left, bottom, GRAY, 2),
        line(left, goal_y, right, goal_y, DARK_GREEN, 2, "7 5"),
        text(right - 4, goal_y + 22, "velocidad pedida", 15, DARK_GREEN, "bold", "end"),
        line(left, cap_y, right, cap_y, RED, 1.6, "3 4"),
        text(right - 4, cap_y - 8, "tope del motor", 15, RED, anchor="end"),
        text((left + right) / 2, height - 6, "tiempo", 15, GRAY),
    ]

    def curve(points):
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)

    def second_order(t, zeta, omega):
        wd = omega * math.sqrt(1 - zeta ** 2)
        k = zeta / math.sqrt(1 - zeta ** 2)
        return 1 - math.exp(-zeta * omega * t) * (math.cos(wd * t) + k * math.sin(wd * t))

    xs = [left + i * (right - left) / 120 for i in range(121)]
    without = []
    with_guard = []
    for i, x in enumerate(xs):
        t = i / 120
        y_without = bottom - (bottom - goal_y) * second_order(t, 0.22, 16)
        y_guard = bottom - (bottom - goal_y) * second_order(t, 0.9, 14)
        without.append((x, max(y_without, cap_y)))
        with_guard.append((x, y_guard))
    lose = [
        path(curve(without), "#F59E0B", 3),
        line(left + 6, 16, left + 36, 16, "#F59E0B", 4),
        text(left + 44, 21, "sin protección: se pasa y oscila", 15, "#B45309", anchor="start"),
    ]
    win = [
        path(curve(with_guard), BLUE, 3.5),
        line(left + 262, 16, left + 292, 16, BLUE, 4),
        text(left + 300, 21, "con protección: llega limpio", 15, BLUE, "bold", "start"),
    ]
    return svg(width, height, axes), svg(width, height, lose), svg(width, height, win)


def node(cx, cy, r, fill, stroke, label=None, label_color="white"):
    out = [circle(cx, cy, r, fill=fill, stroke=stroke, width=2.5)]
    if label:
        out.append(text(cx, cy + 5, label, 14, label_color, "bold"))
    return out


def ros1():
    width, height = 520, 230
    cx, cy = 260, 115
    ring = [(260 + 165 * math.cos(a), 115 + 85 * math.sin(a)) for a in
            [math.radians(d) for d in (200, 250, 290, 340, 20, 70, 110, 160)]]
    base = []
    for x, y in ring:
        base.append(line(cx, cy, x, y, MID, 2.5))
    for x, y in ring:
        base += node(x, y, 16, "#DBEAFE", BLUE)
    base += node(cx, cy, 30, BLUE, BLUE, "maestro")
    down = [circle(cx, cy, 33, fill="white", opacity=0.75)]
    for x, y in ring:
        down.append(circle(x, y, 18, fill="white", opacity=0.7))
        down.append(line(cx, cy, x, y, "white", 4, opacity=0.8))
    down += cross(cx, cy, 16)
    return svg(width, height, base), svg(width, height, down)


def ros2():
    width, height = 520, 230
    ring = [(260 + 170 * math.cos(a), 115 + 85 * math.sin(a)) for a in
            [math.radians(d) for d in (200, 250, 290, 340, 20, 70, 110, 160)]]
    base = []
    for i, (x1, y1) in enumerate(ring):
        for x2, y2 in ring[i + 1:]:
            base.append(line(x1, y1, x2, y2, LIGHT, 1.4))
    for x, y in ring:
        base += node(x, y, 16, "#DBEAFE", BLUE)
    base += [rect(150, 92, 220, 46, fill="#EEF7E4", stroke=GREEN, width=2, rx=23),
             text(260, 121, "DDS: se descubren solos", 14, DARK_GREEN, "bold")]
    lost = ring[2]
    down = [circle(lost[0], lost[1], 19, fill="white", opacity=0.8)]
    down += cross(lost[0], lost[1], 10)
    for x, y in ring:
        if (x, y) != lost:
            down.append(circle(x, y, 7, fill=GREEN))
    return svg(width, height, base), svg(width, height, down)


def walls(width, height, inset=18):
    return [
        rect(inset, inset, width - 2 * inset, height - 2 * inset, fill="white", stroke=INK, width=5, rx=4),
        line(inset + (width - 2 * inset) * 0.45, inset, inset + (width - 2 * inset) * 0.45,
             inset + (height - 2 * inset) * 0.62, INK, 5),
    ]


def loop_route(width, height, inset=18, drift=0.0, steps=60):
    pts = []
    x0, y0 = inset + 40, height - inset - 34
    w, h = width - 2 * inset - 80, height - 2 * inset - 68
    for i in range(steps + 1):
        t = i / steps
        if t < 0.25:
            x, y = x0 + w * t / 0.25, y0
        elif t < 0.5:
            x, y = x0 + w, y0 - h * (t - 0.25) / 0.25
        elif t < 0.75:
            x, y = x0 + w - w * (t - 0.5) / 0.25, y0 - h
        else:
            x, y = x0, y0 - h + h * (t - 0.75) / 0.25
        x += drift * 60 * t * t
        y -= drift * 26 * t * t
        pts.append((x, y))
    return pts


def gmapping():
    width, height = 520, 230
    rng = random.Random(7)
    base = walls(width, height)
    route = loop_route(width, height, drift=0.0)
    for k in range(9):
        d = (k - 4) * 0.09
        pts = loop_route(width, height, drift=d)
        base.append(path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), "#93C5FD", 1.6, opacity=0.8))
    end = route[-1]
    for _ in range(90):
        r = rng.gauss(0, 13)
        a = rng.uniform(0, 2 * math.pi)
        base.append(circle(end[0] + r * math.cos(a), end[1] + 22 + r * math.sin(a) * 0.7, 2.6, fill=BLUE, opacity=0.75))
    base.append(text(width / 2, height - 30, "cada punto es una hipótesis con su propio mapa", 16, BLUE, "bold"))
    return svg(width, height, base)


def pose_graph():
    width, height = 520, 230
    base = walls(width, height)
    pts = loop_route(width, height, drift=0.9, steps=12)
    for a, b in zip(pts, pts[1:]):
        base.append(line(a[0], a[1], b[0], b[1], PURPLE, 2.5))
    for x, y in pts:
        base.append(circle(x, y, 6.5, fill="white", stroke=PURPLE, width=2.5))
    closure = [line(pts[-1][0], pts[-1][1], pts[0][0], pts[0][1], GREEN, 4, "8 6"),
               circle(pts[0][0], pts[0][1], 11, stroke=GREEN, width=3),
               text(width / 2, height - 30, "cierre de lazo: «ya estuve aquí» y el mapa se corrige", 16, DARK_GREEN, "bold")]
    return svg(width, height, base), svg(width, height, closure)


def hector():
    width, height = 520, 230
    base = walls(width, height)
    pts = loop_route(width, height, drift=0.55, steps=40)
    base.append(path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), ORANGE, 3))
    for x, y in pts[::5]:
        base.append(path(f"M{x - 10:.1f},{y - 6:.1f} Q{x:.1f},{y - 16:.1f} {x + 10:.1f},{y - 6:.1f}", ORANGE, 1.6, opacity=0.7))
    gap = [circle(pts[0][0], pts[0][1], 9, fill="white", stroke=ORANGE, width=2.5),
           line(pts[-1][0], pts[-1][1], pts[0][0], pts[0][1], RED, 2, "4 5"),
           text(width / 2, height - 30, "barrido contra barrido: el error se acumula", 16, ORANGE, "bold")]
    return svg(width, height, base + gap)


def cartographer():
    width, height = 520, 230
    base = walls(width, height)
    rng = random.Random(3)
    tiles = []
    for i in range(6):
        x = 34 + i * 50 + rng.uniform(-6, 6)
        y = 40 + (i % 2) * 52 + rng.uniform(-6, 6)
        tiles.append(rect(x, y, 96, 84, fill="#E0E7FF", stroke=PURPLE, width=1.8, rx=4, opacity=0.55))
    gauge = [
        path("M392,150 A46,46 0 0,1 484,150", LIGHT, 12),
        path("M392,150 A46,46 0 0,1 476,126", RED, 12),
        line(438, 150, 474, 120, INK, 3.5),
        circle(438, 150, 6, fill=INK),
        text(438, 178, "uso de CPU", 17, INK, "bold"),
    ]
    return svg(width, height, base + tiles + gauge)


def grid_cells(width, height, cols, rows, inset=12):
    cw = (width - 2 * inset) / cols
    ch = (height - 2 * inset) / rows
    return cw, ch, inset


def astar():
    width, height = 520, 230
    cols, rows = 26, 11
    cw, ch, ins = grid_cells(width, height, cols, rows)
    blocked = {(12, r) for r in range(0, 8)} | {(c, 4) for c in range(17, 23)}
    start, goal = (2, 8), (23, 2)
    body = []
    for c in range(cols):
        for r in range(rows):
            fill = INK if (c, r) in blocked else "white"
            body.append(rect(ins + c * cw, ins + r * ch, cw, ch, fill=fill, stroke=PALE, width=1))
    wave = []
    for c in range(cols):
        for r in range(rows):
            if (c, r) in blocked:
                continue
            g = math.hypot(c - start[0], r - start[1])
            h = math.hypot(c - goal[0], r - goal[1])
            if g + h <= math.hypot(goal[0] - start[0], goal[1] - start[1]) * 1.12:
                shade = max(0.2, 0.8 - g / 30)
                wave.append(rect(ins + c * cw + 1, ins + r * ch + 1, cw - 2, ch - 2, fill="#93C5FD", opacity=shade))
    route_cells = [(c, 8) for c in range(2, 14)] + [(13, r) for r in range(7, 1, -1)]
    route_cells += [(c, 2) for c in range(14, 24)]
    pts = [(ins + (c + 0.5) * cw, ins + (r + 0.5) * ch) for c, r in route_cells]
    route = [path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), "#16A34A", 4)]
    marks = [rect(ins + start[0] * cw + 2, ins + start[1] * ch + 2, cw - 4, ch - 4, fill=RED, rx=2),
             circle(ins + (goal[0] + 0.5) * cw, ins + (goal[1] + 0.5) * ch, 8, fill="white", stroke="#16A34A", width=3)]
    return svg(width, height, body + marks), svg(width, height, wave), svg(width, height, route + marks)


def rrt():
    width, height = 520, 230
    rng = random.Random(11)
    body = [rect(12, 12, width - 24, height - 24, fill="white", stroke=PALE, width=1.5, rx=4),
            rect(250, 12, 26, 150, fill=INK), rect(360, 110, 120, 22, fill=INK)]
    nodes = [(50, 190)]
    parents = [None]
    goal = (470, 50)
    for _ in range(600):
        if math.hypot(nodes[-1][0] - goal[0], nodes[-1][1] - goal[1]) < 22:
            break
        target = goal if rng.random() < 0.12 else (rng.uniform(20, 500), rng.uniform(20, 210))
        j = min(range(len(nodes)), key=lambda k: (nodes[k][0] - target[0]) ** 2 + (nodes[k][1] - target[1]) ** 2)
        x0, y0 = nodes[j]
        dx, dy = target[0] - x0, target[1] - y0
        dist = math.hypot(dx, dy) or 1
        step = min(26, dist)
        x1, y1 = x0 + dx / dist * step, y0 + dy / dist * step
        if 244 < x1 < 282 and y1 < 168 or 354 < x1 < 486 and 104 < y1 < 138:
            continue
        nodes.append((x1, y1))
        parents.append(j)
    tree = []
    for k in range(1, len(nodes)):
        p = nodes[parents[k]]
        tree.append(line(p[0], p[1], nodes[k][0], nodes[k][1], "#A78BFA", 1.6))
        tree.append(circle(nodes[k][0], nodes[k][1], 2.4, fill=PURPLE))
    best = min(range(len(nodes)), key=lambda k: (nodes[k][0] - goal[0]) ** 2 + (nodes[k][1] - goal[1]) ** 2)
    chain = [goal]
    k = best
    while k is not None:
        chain.append(nodes[k])
        k = parents[k]
    route = [path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in chain), "#16A34A", 3.5)]
    marks = [rect(42, 182, 16, 16, fill=RED, rx=2), circle(goal[0], goal[1], 9, fill="white", stroke="#16A34A", width=3)]
    return svg(width, height, body + tree + route + marks)


def robot_marker(x, y, size=14, heading=0.0):
    a = math.radians(heading)
    tip = (x + size * math.cos(a), y + size * math.sin(a))
    return [rect(x - size * 0.7, y - size * 0.7, size * 1.4, size * 1.4, fill=RED, rx=3),
            line(x, y, tip[0], tip[1], "white", 3)]


def dwb():
    width, height = 340, 190
    ox, oy = 50, 150
    obstacle = (150, 118, 40, 40)
    arcs = []
    options = []
    for curv in (-0.012, -0.008, -0.005, -0.002, 0.001, 0.004, 0.007):
        pts = []
        x, y, th = ox, oy, math.radians(-6)
        for _ in range(40):
            x += 4.6 * math.cos(th)
            y += 4.6 * math.sin(th)
            th += curv * 4.6
            pts.append((x, y))
        d = f"M{ox},{oy} " + " ".join(f"L{px:.1f},{py:.1f}" for px, py in pts)
        hit = any(obstacle[0] - 3 < px < obstacle[0] + obstacle[2] + 3 and
                  obstacle[1] - 3 < py < obstacle[1] + obstacle[3] + 3 for px, py in pts)
        arcs.append(path(d, MID if hit else "#FDBA74", 2.2, dash="5 5" if hit else None))
        if not hit:
            options.append((abs(curv), d))
    chosen = min(options)[1]
    body = [rect(6, 6, width - 12, height - 12, fill="white", stroke=PALE, width=1.5, rx=4)]
    body += clipped(width, height, arcs + [rect(*obstacle, fill=INK, rx=4), path(chosen, "#EA580C", 4.5)]
                    + robot_marker(ox, oy, 12, -6))
    return svg(width, height, body)


def pure_pursuit():
    width, height = 340, 190
    inner = [path("M40,160 C120,160 140,60 300,50", "#16A34A", 3.5)]
    ox, oy = 60, 150
    lx, ly = 176, 96
    inner.append(circle(ox, oy, 70, stroke=MID, width=1.5, dash="5 5"))
    inner.append(path(f"M{ox},{oy} Q{120},{140} {lx},{ly}", "#EA580C", 3.5))
    inner.append(circle(lx, ly, 8, fill="#EA580C"))
    inner.append(rect(206, 120, 40, 40, fill=INK, rx=4))
    inner += robot_marker(ox, oy, 12, -20)
    body = [rect(6, 6, width - 12, height - 12, fill="white", stroke=PALE, width=1.5, rx=4)]
    return svg(width, height, body + clipped(width, height, inner))


def mppi():
    width, height = 340, 190
    rng = random.Random(5)
    ox, oy = 50, 150
    inner = []
    for _ in range(160):
        x, y, th = ox, oy, math.radians(-30)
        pts = []
        curv0 = rng.gauss(0, 0.007)
        for _ in range(45):
            th += curv0 * 5 + rng.gauss(0, 0.02)
            x += 5 * math.cos(th)
            y += 5 * math.sin(th)
            pts.append((x, y))
        inner.append(path("M" + f"{ox},{oy} " + " ".join(f"L{px:.1f},{py:.1f}" for px, py in pts), PURPLE, 0.8, opacity=0.35))
    inner.append(rect(170, 56, 40, 40, fill=INK, rx=4))
    inner += robot_marker(ox, oy, 12, -30)
    body = [rect(6, 6, width - 12, height - 12, fill="white", stroke=PALE, width=1.5, rx=4)]
    return svg(width, height, body + clipped(width, height, inner))


def occupancy(width, height, cols, rows, known_cols, ins=10):
    cw = (width - 2 * ins) / cols
    ch = (height - 2 * ins) / rows
    cells = []
    for c in range(cols):
        for r in range(rows):
            known = c < known_cols(r)
            wall = known and (r in (0, rows - 1) or c == 0)
            fill = INK if wall else ("white" if known else "#D1D5DB")
            cells.append(rect(ins + c * cw, ins + r * ch, cw, ch, fill=fill, stroke="#E5E7EB", width=0.8))
    return cells, cw, ch


def frontier():
    width, height = 340, 190
    cols, rows = 17, 9

    def known(r):
        return 9 if r in (2, 3, 4, 5, 6) else 7

    cells, cw, ch = occupancy(width, height, cols, rows, known)
    ins = 10
    front = []
    for r in range(1, rows - 1):
        c = known(r)
        front.append(rect(ins + c * cw, ins + r * ch, cw, ch, fill=YELLOW, opacity=0.95))
    body = cells + front + robot_marker(ins + 2.5 * cw, ins + 4.5 * ch, 10)
    body.append(circle(ins + (known(4) + 0.5) * cw, ins + 4.5 * ch, 10, stroke="#16A34A", width=3))
    return svg(width, height, body)


def info_gain():
    width, height = 340, 190
    cols, rows = 17, 9

    def known(r):
        return 9 if r in (2, 3, 4, 5, 6) else 7

    cells, cw, ch = occupancy(width, height, cols, rows, known)
    ins = 10
    body = []
    candidates = [(9.5, 2.5, "0,4"), (9.5, 5.5, "0,7"), (7.5, 1.5, "0,2")]
    for cx, cy, score in candidates:
        x, y = ins + cx * cw, ins + cy * ch
        body.append(path(f"M{x:.1f},{y:.1f} L{x + 90:.1f},{y - 40:.1f} A98,98 0 0,1 {x + 90:.1f},{y + 40:.1f} Z",
                         TEAL, 1.5, fill="#99F6E4", opacity=0.45))
        body.append(circle(x, y, 7, fill=TEAL))
        body.append(text(x - 14, y + 5, score, 13, TEAL, "bold", "end"))
    body += robot_marker(ins + 2.5 * cw, ins + 4.5 * ch, 10)
    return svg(width, height, cells + clipped(width, height, body, inset=10))


def active_slam():
    width, height = 340, 190
    cols, rows = 17, 9

    def known(r):
        return 9 if r in (2, 3, 4, 5, 6) else 7

    cells, cw, ch = occupancy(width, height, cols, rows, known)
    ins = 10
    body = list(cells)
    route = (f"M{ins + 2.5 * cw:.1f},{ins + 4.5 * ch:.1f} C{ins + 8 * cw:.1f},{ins + 7.5 * ch:.1f} "
             f"{ins + 9 * cw:.1f},{ins + 1.5 * ch:.1f} {ins + 4 * cw:.1f},{ins + 2 * ch:.1f}")
    body.append(path(route, PURPLE, 3, dash="7 5"))
    for k, (cx, cy, rx) in enumerate([(4.5, 6.2, 26), (8.2, 4.4, 20), (6.0, 2.0, 12)]):
        body.append(f'<ellipse cx="{ins + cx * cw:.1f}" cy="{ins + cy * ch:.1f}" rx="{rx}" ry="{rx * 0.6:.1f}" '
                     f'fill="#E9D5FF" stroke="{PURPLE}" stroke-width="1.6" opacity="0.8"/>')
    body += robot_marker(ins + 2.5 * cw, ins + 4.5 * ch, 10)
    return svg(width, height, body)


def lidar_rays():
    width, height = 200, 200
    body = []
    for k in range(24):
        a = 2 * math.pi * k / 24
        r = 78 if k % 3 else 64
        body.append(line(100, 100, 100 + r * math.cos(a), 100 + r * math.sin(a), GREEN, 2, opacity=0.8))
        body.append(circle(100 + r * math.cos(a), 100 + r * math.sin(a), 4, fill=DARK_GREEN))
    body.append(circle(100, 100, 18, fill=INK))
    body.append(circle(100, 100, 8, fill="#374151"))
    return svg(width, height, body)


def encoder_pulses():
    width, height = 260, 140
    body = [circle(64, 70, 52, fill="#E5E7EB", stroke=GRAY, width=3)]
    for k in range(12):
        a = 2 * math.pi * k / 12
        body.append(rect(64 + 40 * math.cos(a) - 6, 70 + 40 * math.sin(a) - 6, 12, 12, fill=INK, rx=2))
    body.append(circle(64, 70, 12, fill=GRAY))
    wave = "M132,96"
    x = 132
    for _ in range(6):
        wave += f" L{x},44 L{x + 10},44 L{x + 10},96 L{x + 20},96"
        x += 20
    body.append(path(wave, TEAL, 3))
    return svg(width, height, body)


def main():
    write("drawing-l298n.svg", l298n())
    for suffix, content in zip(("base", "layer-1", "layer-2"), lidar_plane()):
        write(f"diagram-lidar-plane-{suffix}.svg", content)
    write("diagram-lidar-surfaces.svg", lidar_surfaces())
    for suffix, content in zip(("base", "layer-1", "layer-2"), windup()):
        write(f"diagram-windup-{suffix}.svg", content)
    for name, func in (("ros1", ros1), ("ros2", ros2), ("pose-graph", pose_graph)):
        base, layer = func()
        write(f"diagram-{name}-base.svg", base)
        write(f"diagram-{name}-layer-1.svg", layer)
    write("diagram-gmapping.svg", gmapping())
    write("diagram-hector.svg", hector())
    write("diagram-cartographer.svg", cartographer())
    for suffix, content in zip(("base", "layer-1", "layer-2"), astar()):
        write(f"diagram-astar-{suffix}.svg", content)
    write("diagram-rrt.svg", rrt())
    write("diagram-dwb.svg", dwb())
    write("diagram-pure-pursuit.svg", pure_pursuit())
    write("diagram-mppi.svg", mppi())
    write("diagram-frontier.svg", frontier())
    write("diagram-info-gain.svg", info_gain())
    write("diagram-active-slam.svg", active_slam())
    write("diagram-lidar-rays.svg", lidar_rays())
    write("diagram-encoder-pulses.svg", encoder_pulses())


if __name__ == "__main__":
    main()
