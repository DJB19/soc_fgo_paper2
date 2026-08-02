#!/usr/bin/env python3
"""Regenerate the three submission figures from repository results."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 10, "savefig.dpi": 300})


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


simulation = read_csv(ROOT / "results" / "simulation_metrics.csv")
bias = np.array([float(row["Bias_percent"]) for row in simulation])
cc = np.array([float(row["CC_RMSE"]) for row in simulation])
fgo = np.array([float(row["FGO_RMSE"]) for row in simulation])
fig, ax = plt.subplots(figsize=(6.6, 4.1))
ax.plot(bias, cc, "o-", label="Coulomb counting")
ax.plot(bias, fgo, "s-", label="Nonlinear FGO")
ax.plot(bias, 0.003821 * bias, "--", alpha=0.55)
ax.plot(bias, 0.000309 * bias, "--", alpha=0.55)
ax.set(xlabel="Multiplicative current bias (%)", ylabel="SOC RMSE", xlim=(0, 10.3), ylim=(0, 0.041))
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "figure1_bias_rmse.png")
plt.close(fig)

z = np.linspace(0.0, 1.0, 600)
ocv = 3.0 + 1.2 * z - 0.1 * np.sin(2.0 * np.pi * z)
docv = 1.2 - 0.2 * np.pi * np.cos(2.0 * np.pi * z)
fig, axes = plt.subplots(2, 1, figsize=(6.6, 5.0), sharex=True)
axes[0].plot(z, ocv, color="#222222", lw=2)
axes[0].set_ylabel("OCV (V)")
axes[1].plot(z, docv, color="#6a3d9a", lw=2)
axes[1].set(xlabel="SOC", ylabel="dV_OCV/dz (V per unit SOC)", ylim=(0.45, 1.95))
for axis in axes:
    axis.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "figure2_ocv_sensitivity.png")
plt.close(fig)

trajectory = read_csv(ROOT / "results" / "nasa_bias100_trajectory.csv")
time_h = np.array([float(row["time"]) / 3600.0 for row in trajectory])
reference = np.array([float(row["soc_ref"]) for row in trajectory])
cc_soc = np.array([float(row["soc_cc_unclipped"]) for row in trajectory])
fgo_soc = np.array([float(row["soc_fgo"]) for row in trajectory])
fig, axes = plt.subplots(2, 1, figsize=(6.6, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.55, 1.0]})
axes[0].plot(time_h, 100 * reference, color="#202020", lw=2, label="Reference SOC")
axes[0].plot(time_h, 100 * cc_soc, "--", lw=2, label="Coulomb counting")
axes[0].plot(time_h, 100 * fgo_soc, "-.", lw=2, label="Nonlinear FGO")
axes[0].set_ylabel("SOC (%)")
axes[0].legend()
axes[1].axhline(0, color="#202020", lw=1)
axes[1].plot(time_h, 100 * (cc_soc - reference), "--", lw=2)
axes[1].plot(time_h, 100 * (fgo_soc - reference), "-.", lw=2)
axes[1].set(xlabel="Time (h)", ylabel="Estimation error (pp)")
for axis in axes:
    axis.grid(True, alpha=0.22)
fig.tight_layout()
fig.savefig(OUT / "figure3_nasa_b0005.png")
plt.close(fig)

print(OUT)

