import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

output_dir = "manuscript/figures"
os.makedirs(output_dir, exist_ok=True)

soc = np.linspace(0.0, 1.0, 1001)
soc_percent = 100.0 * soc

ocv = (
    3.0
    + 1.2 * soc
    - 0.1 * np.sin(2.0 * np.pi * soc)
)

docv_dsoc = (
    1.2
    - 0.2 * np.pi * np.cos(2.0 * np.pi * soc)
)

slope_min = docv_dsoc.min()
slope_max = docv_dsoc.max()

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.labelsize": 10,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8.5,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.8,
    "savefig.dpi": 600
})

fig, axes = plt.subplots(
    1,
    2,
    figsize=(7.2, 3.15),
    constrained_layout=True
)

ax1, ax2 = axes

# Panel (a): nonlinear OCV-SOC relationship
ax1.plot(
    soc_percent,
    ocv,
    color="#0072B2",
    linewidth=2.0
)

ax1.set_xlabel("SOC (%)")
ax1.set_ylabel("Open-circuit voltage (V)")
ax1.set_xlim(0, 100)
ax1.xaxis.set_major_locator(MultipleLocator(20))
ax1.yaxis.set_major_locator(MultipleLocator(0.2))
ax1.grid(
    True,
    linestyle="--",
    linewidth=0.55,
    alpha=0.45
)

ax1.text(
    0.03,
    0.95,
    "(a)",
    transform=ax1.transAxes,
    fontsize=10,
    fontweight="bold",
    va="top"
)

# Panel (b): local voltage sensitivity
ax2.plot(
    soc_percent,
    docv_dsoc,
    color="#D55E00",
    linewidth=2.0
)

ax2.fill_between(
    soc_percent,
    0,
    docv_dsoc,
    color="#D55E00",
    alpha=0.10
)

ax2.scatter(
    [0, 50, 100],
    [slope_min, slope_max, slope_min],
    color="#D55E00",
    s=24,
    zorder=3
)

ax2.annotate(
    f"Minimum = {slope_min:.3f}",
    xy=(0, slope_min),
    xytext=(9, slope_min + 0.18),
    arrowprops={
        "arrowstyle": "->",
        "linewidth": 0.8
    },
    fontsize=7.5
)

ax2.annotate(
    f"Maximum = {slope_max:.3f}",
    xy=(50, slope_max),
    xytext=(56, slope_max - 0.20),
    arrowprops={
        "arrowstyle": "->",
        "linewidth": 0.8
    },
    fontsize=7.5
)

ax2.set_xlabel("SOC (%)")
ax2.set_ylabel(r"Local sensitivity $dV_{\mathrm{OCV}}/dSOC$ (V)")
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 2.05)
ax2.xaxis.set_major_locator(MultipleLocator(20))
ax2.yaxis.set_major_locator(MultipleLocator(0.4))
ax2.grid(
    True,
    linestyle="--",
    linewidth=0.55,
    alpha=0.45
)

ax2.text(
    0.03,
    0.95,
    "(b)",
    transform=ax2.transAxes,
    fontsize=10,
    fontweight="bold",
    va="top"
)

png_file = (
    output_dir
    + "/paper2_ocv_sensitivity_journal.png"
)

pdf_file = (
    output_dir
    + "/paper2_ocv_sensitivity_journal.pdf"
)

fig.savefig(
    png_file,
    bbox_inches="tight"
)

fig.savefig(
    pdf_file,
    bbox_inches="tight"
)

plt.close(fig)

print(f"Minimum OCV slope = {slope_min:.6f} V/SOC")
print(f"Maximum OCV slope = {slope_max:.6f} V/SOC")
print(f"Sensitivity ratio = {slope_max / slope_min:.3f}")
print(f"Saved: {png_file}")
print(f"Saved: {pdf_file}")
