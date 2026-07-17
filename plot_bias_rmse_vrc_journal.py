import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

summary = pd.read_csv(
    "paper2_vrc_corrected_results.csv"
)

bias = np.concatenate([
    [0.0],
    summary["Bias_percent"].to_numpy()
])

cc_rmse = np.concatenate([
    [6.145202983355383e-7],
    summary["CC_RMSE"].to_numpy()
])

fgo_rmse = np.concatenate([
    [4.704411657431543e-7],
    summary["FGO_RMSE"].to_numpy()
])

# Least-squares slopes constrained through the origin
kappa_cc = np.dot(bias, cc_rmse) / np.dot(bias, bias)
kappa_fgo = np.dot(bias, fgo_rmse) / np.dot(bias, bias)

cc_fit = kappa_cc * bias
fgo_fit = kappa_fgo * bias

suppression = (
    1.0 - kappa_fgo / kappa_cc
) * 100.0

ratio = kappa_cc / kappa_fgo

def r_squared(y, y_fit):
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum(
        (y - np.mean(y)) ** 2
    )
    return 1.0 - ss_res / ss_tot

r2_cc = r_squared(cc_rmse, cc_fit)
r2_fgo = r_squared(fgo_rmse, fgo_fit)

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
    1, 2,
    figsize=(8.3, 3.8),
    gridspec_kw={
        "width_ratios": [2.15, 1.0],
        "wspace": 0.36
    }
)

# Panel (a): RMSE response
ax1.plot(
    bias,
    cc_rmse,
    color="#0072B2",
    marker="o",
    markersize=5.5,
    linewidth=0,
    markerfacecolor="white",
    markeredgewidth=1.4,
    label="Coulomb counting"
)

ax1.plot(
    bias,
    fgo_rmse,
    color="#D55E00",
    marker="s",
    markersize=5.2,
    linewidth=0,
    markerfacecolor="white",
    markeredgewidth=1.4,
    label="Nonlinear FGO"
)

x_fit = np.linspace(0, 10, 300)

ax1.plot(
    x_fit,
    kappa_cc * x_fit,
    color="#0072B2",
    linewidth=1.8,
    linestyle="-"
)

ax1.plot(
    x_fit,
    kappa_fgo * x_fit,
    color="#D55E00",
    linewidth=1.8,
    linestyle="--"
)

ax1.set_xlabel("Current-sensor bias (%)")
ax1.set_ylabel("SOC RMSE")

ax1.set_xlim(-0.15, 10.3)
ax1.set_ylim(-0.0005, 0.041)

ax1.xaxis.set_major_locator(
    MultipleLocator(2)
)

ax1.xaxis.set_minor_locator(
    MultipleLocator(1)
)

ax1.yaxis.set_major_locator(
    MultipleLocator(0.01)
)

ax1.yaxis.set_minor_locator(
    MultipleLocator(0.005)
)

ax1.yaxis.set_major_formatter(
    FormatStrFormatter("%.02f")
)

ax1.legend(
    loc="upper left",
    frameon=True,
    framealpha=0.95,
    edgecolor="0.80"
)

equation_text = (
    rf"$RMSE_{{CC}}={kappa_cc:.6f}b$"
    "\n"
    rf"$RMSE_{{FGO}}={kappa_fgo:.6f}b$"
)

ax1.text(
    0.965,
    0.53,
    equation_text,
    transform=ax1.transAxes,
    ha="right",
    va="top",
    fontsize=8.8,
    color="0.20"
)

ax1.text(
    0.02,
    0.97,
    "(a)",
    transform=ax1.transAxes,
    fontsize=11,
    fontweight="bold",
    va="top"
)

# Panel (b): propagation coefficients
methods = [
    "Coulomb\ncounting",
    "Nonlinear\nFGO"
]

coefficients = [
    kappa_cc,
    kappa_fgo
]

colors = [
    "#0072B2",
    "#D55E00"
]

bars = ax2.bar(
    methods,
    coefficients,
    width=0.62,
    color=colors,
    edgecolor="black",
    linewidth=0.6
)

ax2.set_ylabel(
    "Bias-propagation coefficient\n"
    r"$\kappa$ (SOC RMSE per 1% bias)"
)

ax2.set_ylim(
    0,
    kappa_cc * 1.28
)

for bar, value in zip(
    bars,
    coefficients
):
    ax2.text(
        bar.get_x()
        + bar.get_width() / 2,
        value + kappa_cc * 0.025,
        f"{value:.6f}",
        ha="center",
        va="bottom",
        fontsize=8.5
    )

ax2.text(
    0.50,
    0.82,
    f"{suppression:.1f}% reduction\n"
    f"({ratio:.1f}" + r"$\times$ lower)",
    transform=ax2.transAxes,
    ha="center",
    va="center",
    fontsize=9,
    color="0.20"
)

ax2.text(
    0.04,
    0.97,
    "(b)",
    transform=ax2.transAxes,
    fontsize=11,
    fontweight="bold",
    va="top"
)

for ax in (ax1, ax2):
    ax.grid(
        axis="y",
        which="major",
        color="0.85",
        linewidth=0.45
    )

    ax.grid(
        axis="y",
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

fig.subplots_adjust(
    left=0.10,
    right=0.98,
    top=0.97,
    bottom=0.18
)

png_file = (
    "manuscript/figures/"
    "paper2_bias_rmse_vrc_journal.png"
)

pdf_file = (
    "manuscript/figures/"
    "paper2_bias_rmse_vrc_journal.pdf"
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

print(f"kappa_CC  = {kappa_cc:.9f}")
print(f"kappa_FGO = {kappa_fgo:.9f}")
print(f"Suppression = {suppression:.3f}%")
print(f"Coefficient ratio = {ratio:.3f}")
print(f"R2 CC  = {r2_cc:.9f}")
print(f"R2 FGO = {r2_fgo:.9f}")
print("Saved:", png_file)
print("Saved:", pdf_file)

plt.show()
