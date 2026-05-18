import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from pathlib import Path
import sys

try:
    script_path = Path(__file__).resolve()
except NameError:
    script_path = Path(sys.argv[0]).resolve() if sys.argv and sys.argv[0] else Path.cwd()

parent_folder = script_path.parent
print(parent_folder)
output_file_name = "fig_power_budget.png"
output_path_file = parent_folder / output_file_name

# ─── Data from tab:power_budget_filled ───────────────────────────────────────
# Valores alineados con la tabla del capítulo:
# - Riel 5 V: Raspberry Pi 4 + RPLIDAR A1 + periféricos USB + subtotal de salida.
# - Riel 12 V: L298N + motores + entrada del buck + total visto desde batería.
subsystems = [
    'Raspberry Pi 4\n(5 V)',
    'RPLIDAR A1\n(5 V)',
    'Periféricos USB\n(5 V)',
    'Subtotal 5 V\n(salida buck)',
    'L298N + motores\n(12 V)',
    'Buck DFR0205\n(entrada 12 V)',
    'Total 12 V\n(batería)',
]

p_cont = [7.60, 2.25, 0.25, 10.10, 7.20, 11.88, 19.08]
p_pico = [12.5, 3.0, 0.5, 16.0, 43.2, 18.8, 62.0]
p_extra = [p - c for p, c in zip(p_pico, p_cont)]

x = np.arange(len(subsystems))
width = 0.58

# ─── Figure ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.5, 5.8), dpi=300)
fig.patch.set_facecolor('white')

# Colors
COL_5V_CONT = '#2980B9'
COL_5V_EXTRA = '#E74C3C'
COL_12V_CONT = '#1F618D'
COL_12V_EXTRA = '#C0392B'
COL_TOTAL_CONT = '#154360'
COL_TOTAL_EXTRA = '#922B21'

colors_cont = [
    COL_5V_CONT, COL_5V_CONT, COL_5V_CONT, COL_TOTAL_CONT,
    COL_12V_CONT, COL_12V_CONT, COL_TOTAL_CONT,
]
colors_extra = [
    COL_5V_EXTRA, COL_5V_EXTRA, COL_5V_EXTRA, COL_TOTAL_EXTRA,
    COL_12V_EXTRA, COL_12V_EXTRA, COL_TOTAL_EXTRA,
]

# Stacked bars
ax.bar(x, p_cont, width, label='Potencia continua',
       color=colors_cont, edgecolor='white', linewidth=0.8, zorder=3)
ax.bar(x, p_extra, width, bottom=p_cont, label='Excedente de pico',
       color=colors_extra, alpha=0.75, edgecolor='white', linewidth=0.8,
       zorder=3, hatch='///')

# ─── Value labels ────────────────────────────────────────────────────────────
for i, (c, p) in enumerate(zip(p_cont, p_pico)):
    if c >= 3:
        ax.text(i, c / 2, f'{c:.1f} W', ha='center', va='center',
                fontsize=8, fontweight='bold', color='white', fontfamily='sans-serif')
    elif c > 0:
        ax.text(i, c + 0.8, f'{c:.2f} W', ha='center', va='bottom',
                fontsize=7, color='#566573', fontfamily='sans-serif')

    ax.text(i, p + 1.2, f'{p:.1f} W', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color='#922B21', fontfamily='sans-serif')

# ─── Separator between rails ─────────────────────────────────────────────────
ymax = max(p_pico) * 1.18
ax.axvline(x=3.5, color='#BDC3C7', lw=1.0, ls='--', zorder=1)
ax.text(1.5, ymax * 0.93, 'Riel de 5 V', ha='center', fontsize=8.5,
        color='#566573', fontfamily='sans-serif', style='italic')
ax.text(5.0, ymax * 0.93, 'Riel de 12 V / batería', ha='center', fontsize=8.5,
        color='#566573', fontfamily='sans-serif', style='italic')

# ─── Axes formatting ─────────────────────────────────────────────────────────
ax.set_xticks(x)
ax.set_xticklabels(subsystems, fontsize=8.3, fontfamily='sans-serif')
ax.set_ylabel('Potencia (W)', fontsize=10, fontfamily='sans-serif', fontweight='bold')
ax.set_ylim(0, ymax)
ax.yaxis.grid(True, alpha=0.3, zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ─── Legend ──────────────────────────────────────────────────────────────────
legend_elements = [
    Patch(facecolor=COL_5V_CONT, edgecolor='white', label='Potencia continua'),
    Patch(facecolor=COL_5V_EXTRA, edgecolor='white', alpha=0.75, hatch='///',
          label='Excedente de pico (transitorio)'),
]
ax.legend(handles=legend_elements, loc='upper center', fontsize=8.5,
          framealpha=0.9, edgecolor='#BDC3C7', bbox_to_anchor=(0.35, 1.0))

# ─── Annotations ─────────────────────────────────────────────────────────────
ax.annotate('Motores dominan\nel pico de actuación',
            xy=(4, 43.2), xytext=(5.35, 47),
            fontsize=7.5, color='#922B21', fontfamily='sans-serif',
            fontstyle='italic', ha='center',
            arrowprops=dict(arrowstyle='->', color='#922B21', lw=1.0))

ax.annotate('RPi domina el\ncontinuo en 5 V',
            xy=(0, 7.6), xytext=(0.45, 25),
            fontsize=7.5, color=COL_5V_CONT, fontfamily='sans-serif',
            fontstyle='italic', ha='center',
            arrowprops=dict(arrowstyle='->', color=COL_5V_CONT, lw=1.0))

ax.annotate('Total batería incluye\nmotores + entrada del buck',
            xy=(6, 62.0), xytext=(5.1, 66),
            fontsize=7.5, color='#922B21', fontfamily='sans-serif',
            fontstyle='italic', ha='center',
            arrowprops=dict(arrowstyle='->', color='#922B21', lw=1.0))

plt.tight_layout(pad=0.8)
fig.savefig(output_path_file,
            dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.1)
print("OK — Gráfico de presupuesto de potencia generado.")
