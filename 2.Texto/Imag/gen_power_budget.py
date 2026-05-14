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
subsystems = ['Raspberry Pi 4\n(5 V)', 'L298N + motores\n(12 V)', 'RPLIDAR A1\n(5 V)', 'Total 5 V', 'Total 12 V']
p_cont     = [7.6,                      7.2,                       2.25,                9.85,       7.2]
p_pico     = [12.5,                     43.2,                       3.0,                15.5,      43.2]
# The "extra" peak above continuous
p_extra    = [p - c for p, c in zip(p_pico, p_cont)]

x = np.arange(len(subsystems))
width = 0.55

# ─── Figure ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
fig.patch.set_facecolor('white')

# Colors
COL_CONT  = '#2980B9'
COL_EXTRA = '#E74C3C'
COL_TOTAL_CONT = '#1A5276'
COL_TOTAL_EXTRA = '#922B21'

colors_cont  = [COL_CONT, COL_CONT, COL_CONT, COL_TOTAL_CONT, COL_TOTAL_CONT]
colors_extra = [COL_EXTRA, COL_EXTRA, COL_EXTRA, COL_TOTAL_EXTRA, COL_TOTAL_EXTRA]

# Stacked bars
bars_cont = ax.bar(x, p_cont, width, label='Potencia continua',
                   color=colors_cont, edgecolor='white', linewidth=0.8, zorder=3)
bars_extra = ax.bar(x, p_extra, width, bottom=p_cont, label='Excedente de pico',
                    color=colors_extra, alpha=0.75, edgecolor='white', linewidth=0.8,
                    zorder=3, hatch='///')

# ─── Value labels ────────────────────────────────────────────────────────────
for i, (c, p, e) in enumerate(zip(p_cont, p_pico, p_extra)):
    # Continuous value (inside bar)
    if c > 3:
        ax.text(i, c/2, f'{c:.1f} W', ha='center', va='center',
                fontsize=8, fontweight='bold', color='white', fontfamily='sans-serif')
    # Peak value (on top)
    ax.text(i, p + 0.8, f'{p:.1f} W', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color='#922B21', fontfamily='sans-serif')

# ─── Separator between individual and totals ─────────────────────────────────
ax.axvline(x=2.7, color='#BDC3C7', lw=1.0, ls='--', zorder=1)
ax.text(1.0, 48.0, 'Por subsistema', ha='center', fontsize=8.5, color='#566573',
        fontfamily='sans-serif', style='italic')
ax.text(3.5, 48.0, 'Totales por riel', ha='center', fontsize=8.5, color='#566573',
        fontfamily='sans-serif', style='italic')

# ─── Axes formatting ─────────────────────────────────────────────────────────
ax.set_xticks(x)
ax.set_xticklabels(subsystems, fontsize=8.5, fontfamily='sans-serif')
ax.set_ylabel('Potencia (W)', fontsize=10, fontfamily='sans-serif', fontweight='bold')
ax.set_ylim(0, 52)
ax.yaxis.grid(True, alpha=0.3, zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ─── Legend ───────────────────────────────────────────────────────────────────

legend_elements = [
    Patch(facecolor=COL_CONT, edgecolor='white', label='Potencia continua'),
    Patch(facecolor=COL_EXTRA, edgecolor='white', alpha=0.75, hatch='///',
          label='Excedente de pico (transitorio)'),
]
ax.legend(handles=legend_elements, loc='upper center', fontsize=8.5,
          framealpha=0.9, edgecolor='#BDC3C7', bbox_to_anchor=(0.35, 1.0))

# ─── Annotation: motors dominate peak ────────────────────────────────────────
ax.annotate('Motores dominan\nel pico (stall)',
            xy=(1, 43.2), xytext=(2.2, 40),
            fontsize=7.5, color='#922B21', fontfamily='sans-serif',
            fontstyle='italic', ha='center',
            arrowprops=dict(arrowstyle='->', color='#922B21', lw=1.0))

ax.annotate('RPi domina el\ncontinuo en 5 V',
            xy=(0, 7.6), xytext=(0.2, 22),
            fontsize=7.5, color=COL_CONT, fontfamily='sans-serif',
            fontstyle='italic', ha='center',
            arrowprops=dict(arrowstyle='->', color=COL_CONT, lw=1.0))

plt.tight_layout(pad=0.8)
fig.savefig(output_path_file,
                dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.1)
print("OK — Gráfico de presupuesto de potencia generado.")
