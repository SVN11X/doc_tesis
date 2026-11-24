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

The FOPDT curve is the right wheel model exactly as the identification simulates it:
Euler steps of 0.1 s with the parameters of the first PSO, which was fitted to the
measured speed smoothed over 5 samples.
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
    ax.tick_params(length=0, labelsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11)


def open_loop(d):
    fig = plt.figure(figsize=(4.30, 2.40))
    ax_u = fig.add_axes([0.16, 0.74, 0.80, 0.18])
    ax_v = fig.add_axes([0.16, 0.18, 0.80, 0.50], sharex=ax_u)
    ax_u.step(d["t_s"], d["open_loop_pwm"], where="post", color=INK, linewidth=2)
    ax_u.set_yticks([0, 143])
    ax_u.set_ylim(-10, 175)
    ax_u.text(
        1.25, 150, "escalón de PWM = 143 de 255", fontsize=11, color=INK, va="bottom"
    )
    style(ax_u, "PWM")
    ax_u.tick_params(labelbottom=False)
    ax_v.plot(
        d["t_s"], d["open_loop_left_mps"], color=LEFT, linewidth=2, label="izquierda"
    )
    ax_v.plot(
        d["t_s"], d["open_loop_right_mps"], color=RIGHT, linewidth=2, label="derecha"
    )
    ax_v.set_ylim(0, 0.15)
    ax_v.set_yticks([0, 0.05, 0.10, 0.15])
    ax_v.yaxis.set_major_formatter(comma)
    ax_v.set_xlim(0, 10)
    ax_v.set_xticks(range(0, 11, 2))
    ax_v.set_xlabel("tiempo (s)", fontsize=11)
    style(ax_v, "velocidad (m/s)")
    ax_v.legend(loc="lower right", fontsize=11, frameon=False, ncol=2, handlelength=1.4)
    save(fig, HERE / "chart-control-open-loop.svg")
    plt.close(fig)


def fopdt(d):
    t = d["t_s"]
    u = d["open_loop_pwm"]
    plateau = KM * PWM
    model = np.zeros_like(t)
    for k in range(1, len(t)):
        model[k] = model[k - 1] + (0.1 / TAU) * (
            KM * u[max(k - int(L / 0.1), 0)] - model[k - 1]
        )
    fig = plt.figure(figsize=(4.55, 2.90))
    ax = fig.add_axes([0.15, 0.16, 0.82, 0.74])
    sel = (t >= 0.6) & (t <= 3.0)
    base = [
        ax.axvline(STEP_T, color=AXIS, linewidth=1.2, linestyle=":"),
        ax.text(STEP_T + 0.03, 0.140, "escalón", fontsize=11, color=MUTED, va="center"),
        ax.plot(
            t[sel], model[sel], color=MODEL, linewidth=2.2, label="modelo identificado"
        )[0],
        ax.plot(
            t[sel],
            d["open_loop_right_mps"][sel],
            "o",
            color=INK,
            markersize=5,
            label="medido, rueda derecha",
        )[0],
    ]
    ax.set_xlim(0.6, 3.0)
    ax.set_ylim(0, 0.15)
    ax.set_yticks([0, 0.05, 0.10, 0.15])
    ax.yaxis.set_major_formatter(comma)
    ax.xaxis.set_major_formatter(comma0)
    ax.set_xlabel("tiempo (s)", fontsize=11)
    style(ax, "velocidad (m/s)")
    leg = ax.legend(
        loc="upper left",
        bbox_to_anchor=(0.0, 1.12),
        fontsize=11,
        frameon=False,
        ncol=2,
        handlelength=1.4,
    )

    y63 = 0.632 * plateau
    t63 = np.interp(y63, model[(t >= 0.9) & (t <= 2)], t[(t >= 0.9) & (t <= 2)])
    arrow = {
        "arrowstyle": "<->",
        "color": MODEL,
        "linewidth": 1.6,
        "shrinkA": 0,
        "shrinkB": 0,
    }
    cotas = [
        ax.annotate("", xy=(2.85, 0), xytext=(2.85, plateau), arrowprops=arrow),
        ax.text(
            2.78,
            0.068,
            "Km = 0,000890\nm/s por PWM\n(meseta 0,127 ÷ 143)",
            fontsize=11,
            color=INK,
            ha="right",
            fontweight="bold",
            linespacing=1.1,
        ),
        ax.plot([0.6, t63], [y63, y63], color=MODEL, linewidth=1.2, linestyle="--")[0],
        ax.plot([t63], [y63], "o", color=MODEL, markersize=6)[0],
        ax.text(0.63, y63 + 0.004, "63 %", fontsize=11, color=INK, fontweight="bold"),
        ax.annotate(
            "τ = 0,35 s:\nqué tan rápido sube",
            xy=(1.12, 0.068),
            xytext=(1.40, 0.042),
            fontsize=11,
            color=INK,
            fontweight="bold",
            linespacing=1.1,
            arrowprops={"arrowstyle": "-", "color": MODEL, "linewidth": 1.2},
        ),
        ax.annotate(
            "",
            xy=(STEP_T, 0.006),
            xytext=(STEP_T + L, 0.006),
            arrowprops={"arrowstyle": "-", "color": MODEL, "linewidth": 3},
        ),
        ax.annotate(
            "L = 0,07 s (menos de 1 muestra)",
            xy=(STEP_T + L / 2, 0.008),
            xytext=(1.20, 0.010),
            fontsize=11,
            color=INK,
            fontweight="bold",
            linespacing=1.1,
            arrowprops={"arrowstyle": "-", "color": MODEL, "linewidth": 1.2},
        ),
    ]
    for a in cotas:
        a.set_visible(False)
    save(fig, HERE / "chart-control-fopdt.svg")
    for a in base + [leg]:
        a.set_visible(False)
    for a in cotas:
        a.set_visible(True)
    ax.axis("off")
    save(fig, HERE / "chart-control-fopdt-cotas.svg")
    plt.close(fig)


def closed_loop(d):
    t = d["t_s"]
    fig = plt.figure(figsize=(6.25, 3.00))
    axes = [
        fig.add_axes([0.10, 0.17, 0.41, 0.58]),
        fig.add_axes([0.57, 0.17, 0.41, 0.58]),
    ]
    panels = [
        ("Rueda izquierda", "left", LEFT, 1.8, "subida 0,8 s"),
        ("Rueda derecha", "right", RIGHT, 2.4, "subida 1,4 s"),
    ]
    for ax, (title, key, color, t_up, rise) in zip(axes, panels):
        ax.plot(t, d["reference_mps"], color=INK, linewidth=1.3, linestyle=(0, (2, 2)))
        ax.plot(
            t, d[f"initial_pso_{key}_mps"], color=AXIS, linewidth=1.8, linestyle="--"
        )
        ax.plot(t, d[f"final_{key}_mps"], color=color, linewidth=2.2)
        ax.annotate(
            "",
            xy=(STEP_T, 0.035),
            xytext=(t_up, 0.035),
            arrowprops={
                "arrowstyle": "<->",
                "color": INK,
                "linewidth": 1.3,
                "shrinkA": 0,
                "shrinkB": 0,
            },
        )
        ax.text(
            t_up + 0.15,
            0.030,
            rise,
            fontsize=11.5,
            color=INK,
            fontweight="bold",
            va="center",
        )
        ax.set_title(
            title, fontsize=12, color=INK, fontweight="bold", loc="left", pad=4
        )
        ax.set_xlim(0, 8)
        ax.set_xticks(range(0, 9, 2))
        ax.set_ylim(0, 0.16)
        ax.set_yticks([0, 0.05, 0.10, 0.13])
        ax.yaxis.set_major_formatter(comma)
        ax.set_xlabel("tiempo (s)", fontsize=11)
        style(ax)
    axes[0].set_ylabel("velocidad (m/s)", fontsize=11)
    axes[0].annotate(
        "antes: se queda\nen 0,12 m/s",
        xy=(3.0, 0.12),
        xytext=(3.4, 0.072),
        fontsize=11,
        color=MUTED,
        arrowprops={"arrowstyle": "-", "color": AXIS, "linewidth": 1.2},
        linespacing=1.1,
    )
    axes[0].text(
        7.9,
        0.006,
        "sin sobreimpulso",
        fontsize=11,
        color=INK,
        fontweight="bold",
        ha="right",
    )
    axes[1].text(
        7.9,
        0.006,
        "error final ≤ 0,002 m/s",
        fontsize=11,
        color=INK,
        fontweight="bold",
        ha="right",
    )
    axes[1].annotate(
        "antes: 0,11 m/s,\nllega a los 6 s",
        xy=(2.6, 0.11),
        xytext=(3.2, 0.072),
        fontsize=11,
        color=MUTED,
        arrowprops={"arrowstyle": "-", "color": AXIS, "linewidth": 1.2},
        linespacing=1.1,
    )
    handles = [
        plt.Line2D([], [], color=INK, linewidth=1.3, linestyle=(0, (2, 2))),
        plt.Line2D([], [], color=AXIS, linewidth=1.8, linestyle="--"),
        plt.Line2D([], [], color=LEFT, linewidth=2.2),
        plt.Line2D([], [], color=RIGHT, linewidth=2.2),
    ]
    fig.legend(
        handles,
        ["referencia 0,13 m/s", "antes: PSO inicial", "después, izq.", "después, der."],
        loc="upper center",
        ncol=2,
        fontsize=11,
        frameon=False,
        handlelength=1.6,
        columnspacing=1.0,
        bbox_to_anchor=(0.54, 1.03),
    )
    save(fig, HERE / "chart-control-closed-loop.svg")
    plt.close(fig)


if __name__ == "__main__":
    data = load()
    open_loop(data)
    fopdt(data)
    closed_loop(data)
