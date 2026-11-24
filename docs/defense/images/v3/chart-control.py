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
through the same points.

Each chart is split into layers of the same size with a transparent background, so the
slide can stack them and animate each one on its own: the axes, the curves and the
callouts. The axes show no numbers on purpose; the exact values are in the speaker notes.
Each SVG is drawn at the size it has on the slide, so 11 pt in the file is 11 pt on screen.
"""

import csv
import logging
from pathlib import Path

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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


def save(fig, path):
    """Write the SVG with no date and no trailing spaces, so the same data gives the same file."""
    fig.savefig(path, transparent=True, metadata={"Date": None})
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text(
        "\n".join(line.rstrip() for line in lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def save_layers(fig, base, layers, prefix):
    """Save the base chart, then each layer alone on a blank canvas of the same size."""
    for group in layers.values():
        for a in group:
            a.set_visible(False)
    save(fig, HERE / f"{prefix}.svg")
    for a in base:
        a.set_visible(False)
    for name, group in layers.items():
        for a in group:
            a.set_visible(True)
        save(fig, HERE / f"{prefix}-{name}.svg")
        for a in group:
            a.set_visible(False)


def load():
    with open(HERE / "chart-control-data.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}


def bare_axes(ax, xlabel, ylabel=None):
    """Axes with their lines and titles but without numbers."""
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)


def step(d):
    """Open loop step: both wheels, plus a close-up of the final speed that shows the gap."""
    t = d["t_s"]
    left, right = d["open_loop_left_mps"], d["open_loop_right_mps"]
    fig = plt.figure(figsize=(7.60, 3.52))
    ax = fig.add_axes([0.07, 0.12, 0.90, 0.74])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 0.16)
    bare_axes(ax, "tiempo", "velocidad")
    handles = [
        plt.Line2D([], [], color=LEFT, linewidth=2.6),
        plt.Line2D([], [], color=RIGHT, linewidth=2.6),
    ]
    legend = ax.legend(
        handles,
        ["rueda izquierda", "rueda derecha"],
        loc="upper left",
        bbox_to_anchor=(0.0, 1.17),
        ncol=2,
        fontsize=12.5,
        frameon=False,
        handlelength=1.8,
    )
    base = list(ax.spines.values()) + [
        ax.xaxis.label,
        ax.yaxis.label,
        legend,
        ax.axvline(STEP_T, color=AXIS, linewidth=1.4, linestyle=":"),
        ax.text(STEP_T + 0.12, 0.149, "pulso", fontsize=12.5, color=MUTED),
    ]
    curves = [
        ax.plot(t, left, color=LEFT, linewidth=2.4)[0],
        ax.plot(t, right, color=RIGHT, linewidth=2.4)[0],
    ]

    x0, x1, y0, y1 = 3.0, 9.9, 0.1195, 0.1345
    zoom_box = Rectangle(
        (x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor=INK, linewidth=1.3, linestyle="--"
    )
    ax.add_patch(zoom_box)
    inset = fig.add_axes([0.36, 0.19, 0.59, 0.40])
    inset.set_xlim(x0, x1)
    inset.set_ylim(y0, y1)
    inset.set_xticks([])
    inset.set_yticks([])
    inset.set_facecolor("white")
    for spine in inset.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor(INK)
        spine.set_linewidth(1.3)
    sel = t >= x0
    mean_left, mean_right = left[sel].mean(), right[sel].mean()
    inset.plot(t[sel], left[sel], color=LEFT, linewidth=1.2, alpha=0.35)
    inset.plot(t[sel], right[sel], color=RIGHT, linewidth=1.2, alpha=0.35)
    inset.plot([x0, x1], [mean_left, mean_left], color=LEFT, linewidth=3.2)
    inset.plot([x0, x1], [mean_right, mean_right], color=RIGHT, linewidth=3.2)
    inset.annotate(
        "",
        xy=(9.05, mean_left),
        xytext=(9.05, mean_right),
        arrowprops={
            "arrowstyle": "<->",
            "color": INK,
            "linewidth": 2,
            "shrinkA": 0,
            "shrinkB": 0,
        },
    )
    inset.text(
        8.9,
        (mean_left + mean_right) / 2,
        "brecha",
        fontsize=13.5,
        color=INK,
        fontweight="bold",
        ha="right",
        va="center",
    )
    inset.text(
        x0 + 0.15, y1 - 0.0012, "vista ampliada", fontsize=12, color=MUTED, va="top"
    )
    connectors = [
        ax.plot([x0, 3.25], [y0, 0.0955], color=INK, linewidth=1, linestyle="--")[0],
        ax.plot([x1, 9.75], [y0, 0.0955], color=INK, linewidth=1, linestyle="--")[0],
    ]
    inset.set_visible(False)
    save_layers(
        fig,
        base,
        {"curves": curves, "zoom": [zoom_box, inset] + connectors},
        "chart-control-step-output",
    )
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
    """Measured right wheel and its mathematical twin, with the three traits as callouts."""
    t = d["t_s"]
    plateau = KM * PWM
    tm, ym = fitted_curve(d)
    fig = plt.figure(figsize=(7.44, 4.15))
    ax = fig.add_axes([0.08, 0.10, 0.89, 0.75])
    sel = (t >= 0.5) & (t <= 3.0)
    ax.set_xlim(0.5, 3.0)
    ax.set_ylim(0, 0.16)
    bare_axes(ax, "tiempo", "velocidad")
    handles = [
        plt.Line2D([], [], color=INK, marker="o", linestyle="none", markersize=7),
        plt.Line2D([], [], color=MODEL, linewidth=2.8),
    ]
    legend = ax.legend(
        handles,
        ["medición real", "gemelo matemático"],
        loc="upper left",
        bbox_to_anchor=(0.0, 1.16),
        ncol=2,
        fontsize=12.5,
        frameon=False,
        handlelength=1.8,
        columnspacing=1.6,
    )
    base = list(ax.spines.values()) + [ax.xaxis.label, ax.yaxis.label, legend]
    box = {
        "boxstyle": "round,pad=0.35",
        "facecolor": "white",
        "edgecolor": MODEL,
        "linewidth": 1.4,
    }
    line = {"arrowstyle": "-", "color": MODEL, "linewidth": 1.4}
    y63 = 0.632 * plateau
    t63 = np.interp(y63, ym, tm)
    layers = {
        "measured": [
            ax.plot(t[sel], d["open_loop_right_mps"][sel], "o", color=INK, markersize=7)[0]
        ],
        "model": [ax.plot(tm, ym, color=MODEL, linewidth=2.8)[0]],
        "l": [
            ax.axvspan(STEP_T, STEP_T + L, color=MODEL, alpha=0.35, linewidth=0),
            ax.annotate(
                "Reacción: arranca casi al instante",
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
            ax.plot([t63], [y63], "o", color=MODEL, markersize=10)[0],
            ax.annotate(
                "Rapidez: acelera en un tercio de segundo",
                xy=(t63 + 0.01, y63 - 0.002),
                xytext=(1.30, 0.046),
                fontsize=13,
                color=INK,
                fontweight="bold",
                bbox=box,
                arrowprops=line,
            ),
        ],
        "km": [
            ax.annotate(
                "",
                xy=(2.88, plateau),
                xytext=(2.88, 0),
                arrowprops={
                    "arrowstyle": "-|>",
                    "color": MODEL,
                    "linewidth": 2.2,
                    "shrinkA": 0,
                    "shrinkB": 0,
                },
            ),
            ax.text(
                2.80,
                0.093,
                "Fuerza: cuánta velocidad entrega\ncon la potencia aplicada",
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
    save_layers(fig, base, layers, "chart-control-fopdt")
    plt.close(fig)


def closed_loop(d):
    """Floor runs before (seed from simulation) and after the final tuning, one panel per wheel."""
    t = d["t_s"]
    fig = plt.figure(figsize=(7.60, 3.80))
    axes = [
        fig.add_axes([0.06, 0.14, 0.43, 0.62]),
        fig.add_axes([0.555, 0.14, 0.43, 0.62]),
    ]
    panels = [
        ("Rueda izquierda", "left", LEFT, "antes: se quedaba corta", (3.0, 0.12)),
        ("Rueda derecha", "right", RIGHT, "antes: subía por tramos", (2.8, 0.11)),
    ]
    base, after = [], []
    for ax, (title, key, color, before, before_xy) in zip(axes, panels):
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 0.16)
        ax.set_xticks(range(0, 9, 2))
        ax.set_yticks([])
        ax.tick_params(length=0, labelsize=12)
        ax.set_xlabel("tiempo (s)", fontsize=12)
        base += list(ax.spines.values()) + [ax.xaxis, ax.xaxis.label]
        base += [
            ax.plot(t, d["reference_mps"], color=INK, linewidth=1.4, linestyle=(0, (2, 2)))[0],
            ax.text(1.12, 0.139, "meta", fontsize=12, color=INK, ha="left"),
            ax.plot(t, d[f"initial_pso_{key}_mps"], color=AXIS, linewidth=2.2, linestyle="--")[0],
            ax.annotate(
                before,
                xy=before_xy,
                xytext=(3.4, 0.060),
                fontsize=12.5,
                color=MUTED,
                arrowprops={"arrowstyle": "-", "color": AXIS, "linewidth": 1.3},
            ),
            ax.set_title(title, fontsize=13, color=INK, fontweight="bold", loc="left", pad=5),
        ]
        after.append(ax.plot(t, d[f"final_{key}_mps"], color=color, linewidth=2.8)[0])
    axes[0].set_ylabel("velocidad", fontsize=12)
    base.append(axes[0].yaxis.label)
    handles = [
        plt.Line2D([], [], color=INK, linewidth=1.4, linestyle=(0, (2, 2))),
        plt.Line2D([], [], color=AXIS, linewidth=2.2, linestyle="--"),
        plt.Line2D([], [], color=LEFT, linewidth=2.8),
        plt.Line2D([], [], color=RIGHT, linewidth=2.8),
    ]
    base.append(
        fig.legend(
            handles,
            [
                "velocidad pedida",
                "antes: calibración simulada",
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
    )
    save_layers(fig, base, {"after": after}, "chart-control-closed-loop")
    plt.close(fig)


if __name__ == "__main__":
    data = load()
    step(data)
    fopdt(data)
    closed_loop(data)
