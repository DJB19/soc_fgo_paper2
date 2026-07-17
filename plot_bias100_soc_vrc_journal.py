import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

input_file = (
    "results/"
    "paper2_nonlinear_bias100_vrc.csv"
)

df = pd.read_csv(input_file)

time_h = df["time"] / 3600.0

soc_true = df["soc_true"] * 100.0
soc_cc = df["soc_kf"] * 100.0
soc_fgo = df["soc_fgo"] * 100.0

cc_error = soc_cc - soc_true
fgo_error = soc_fgo - soc_true

cc_rmse = np.sqrt(
    np.mean(cc_error ** 2)
)

fgo_rmse = np.sqrt(
    np.mean(fgo_error ** 2)
)

cc_mae = np.mean(
    np.abs(cc_error)
)

fgo_mae = np.mean(
    np.abs(fgo_error)
)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": 10,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8.5,
    "axes.linewidth": 0.8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(7.0, 5.9),
    sharex=True,
    gridspec_kw={
        "height_ratios": [2.05, 1.0],
        "hspace": 0.08
    }
)

# Panel (a): SOC trajectories
ax1.plot(
    time_h,
    soc_true,
    color="black",
    linewidth=2.1,
    label="Reference SOC",
    zorder=4
)

ax1.plot(
    time_h,
    soc_cc,
    color="#0072B2",
    linewidth=1.7,
    linestyle="--",
    label=(
        "Coulomb counting "
        f"(RMSE = {cc_rmse:.2f} pp)"
    )
)

ax1.plot(
    time_h,
    soc_fgo,
    color="#D55E00",
    linewidth=1.7,
    linestyle="-.",
    label=(
        "Nonlinear FGO "
        f"(RMSE = {fgo_rmse:.2f} pp)"
    )
)

ax1.set_ylabel("SOC (%)")
ax1.set_ylim(5, 83)

ax1.yaxis.set_major_locator(
    MultipleLocator(10)
)

ax1.yaxis.set_minor_locator(
    MultipleLocator(5)
)

ax1.legend(
    loc="lower left",
    frameon=True,
    framealpha=0.95,
    edgecolor="0.80"
)

ax1.text(
    0.015,
    0.94,
    "(a)",
    transform=ax1.transAxes,
    fontsize=11,
    fontweight="bold",
    va="top"
)

ax1.text(
    0.985,
    0.94,
    "10% current-sensor bias",
    transform=ax1.transAxes,
    ha="right",
    va="top",
    fontsize=9,
    color="0.25"
)

# Panel (b): estimation errors
ax2.axhline(
    0,
    color="black",
    linewidth=0.8
)

ax2.plot(
    time_h,
    cc_error,
    color="#0072B2",
    linewidth=1.6,
    label="Coulomb counting"
)

ax2.plot(
    time_h,
    fgo_error,
    color="#D55E00",
    linewidth=1.6,
    label="Nonlinear FGO"
)

ax2.fill_between(
    time_h,
    cc_error,
    0,
    color="#0072B2",
    alpha=0.08
)

error_min = min(
    cc_error.min(),
    fgo_error.min()
)

error_max = max(
    cc_error.max(),
    fgo_error.max()
)

error_span = error_max - error_min
padding = max(0.3, 0.10 * error_span)

ax2.set_ylim(
    error_min - padding,
    error_max + padding
)

ax2.set_xlim(
    time_h.iloc[0],
    time_h.iloc[-1]
)

ax2.set_xlabel("Time (h)")
ax2.set_ylabel(
    "SOC error\n"
    "(percentage points)"
)

ax2.xaxis.set_major_locator(
    MultipleLocator(0.5)
)

ax2.xaxis.set_minor_locator(
    MultipleLocator(0.25)
)

ax2.yaxis.set_major_locator(
    MultipleLocator(2)
)

ax2.yaxis.set_minor_locator(
    MultipleLocator(1)
)

ax2.text(
    0.015,
    0.92,
    "(b)",
    transform=ax2.transAxes,
    fontsize=11,
    fontweight="bold",
    va="top"
)

# Inset: magnified FGO error
axins = ax2.inset_axes([0.12, 0.10, 0.37, 0.61])

axins.axhline(
    0,
    color="black",
    linewidth=0.6
)

axins.plot(
    time_h,
    fgo_error,
    color="#D55E00",
    linewidth=1.2
)

fgo_min = fgo_error.min()
fgo_max = fgo_error.max()
fgo_span = fgo_max - fgo_min
fgo_padding = max(
    0.03,
    0.12 * fgo_span
)

axins.set_xlim(
    time_h.iloc[0],
    time_h.iloc[-1]
)

axins.set_ylim(
    fgo_min - fgo_padding,
    fgo_max + fgo_padding
)

axins.set_title(
    "FGO error (magnified)",
    fontsize=7.5,
    pad=2
)

axins.tick_params(
    labelsize=6.5,
    direction="in"
)

axins.grid(
    color="0.90",
    linewidth=0.35
)

for ax in (ax1, ax2):
    ax.grid(
        which="major",
        color="0.85",
        linewidth=0.45
    )

    ax.grid(
        which="minor",
        color="0.91",
        linewidth=0.35,
        linestyle=":"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.tick_params(
        which="both",
        direction="in",
        top=False,
        right=False
    )

fig.align_ylabels([ax1, ax2])

fig.subplots_adjust(
    left=0.14,
    right=0.98,
    top=0.98,
    bottom=0.11
)

png_file = (
    "manuscript/figures/"
    "paper2_bias100_soc_vrc_journal.png"
)

pdf_file = (
    "manuscript/figures/"
    "paper2_bias100_soc_vrc_journal.pdf"
)

fig.savefig(
    png_file,
    dpi=600,
    bbox_inches="tight"
)

fig.savefig(
    pdf_file,
    bbox_inches="tight"
)

print(
    f"CC RMSE  = {cc_rmse:.6f} "
    "percentage points"
)

print(
    f"FGO RMSE = {fgo_rmse:.6f} "
    "percentage points"
)

print(
    f"CC MAE   = {cc_mae:.6f} "
    "percentage points"
)

print(
    f"FGO MAE  = {fgo_mae:.6f} "
    "percentage points"
)

print(
    f"Final CC error  = "
    f"{cc_error.iloc[-1]:.6f} "
    "percentage points"
)

print(
    f"Final FGO error = "
    f"{fgo_error.iloc[-1]:.6f} "
    "percentage points"
)

print("Saved:", png_file)
print("Saved:", pdf_file)

plt.show()
