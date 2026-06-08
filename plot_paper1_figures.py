import pandas as pd
import matplotlib.pyplot as plt

# Load data
current = pd.read_csv("results/result_case1.csv")
linear = pd.read_csv("results/result_case1_voltage_fgo.csv")
nonlinear = pd.read_csv("results/result_case1_nonlinear_voltage_fgo.csv")

# Figure 1: SOC estimation comparison
plt.figure(figsize=(8, 5))
plt.plot(current["time"], current["soc_true"], label="Reference SOC", linewidth=2)
plt.plot(current["time"], current["soc_fgo"], label="Current-Only FGO", linestyle="--")
plt.plot(linear["time"], linear["soc_fgo"], label="Linear Voltage FGO", linestyle="-.")
plt.plot(nonlinear["time"], nonlinear["soc_fgo"], label="Nonlinear Voltage FGO", linestyle=":")
plt.xlabel("Time (s)")
plt.ylabel("SOC")
plt.title("SOC Estimation Comparison under Constant-Current Conditions")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/figure1_soc_comparison.png", dpi=300)
plt.savefig("results/figure1_soc_comparison.pdf")
plt.close()

# Figure 2: Absolute SOC estimation error
current_error = abs(current["soc_fgo"] - current["soc_true"])
linear_error = abs(linear["soc_fgo"] - linear["soc_true"])
nonlinear_error = abs(nonlinear["soc_fgo"] - nonlinear["soc_true"])

plt.figure(figsize=(8, 5))
plt.plot(current["time"], current_error, label="Current-Only FGO Error", linestyle="--")
plt.plot(linear["time"], linear_error, label="Linear Voltage FGO Error", linestyle="-.")
plt.plot(nonlinear["time"], nonlinear_error, label="Nonlinear Voltage FGO Error", linestyle=":")
plt.xlabel("Time (s)")
plt.ylabel("Absolute SOC Error")
plt.title("SOC Estimation Error under Constant-Current Conditions")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/figure2_error_comparison.png", dpi=300)
plt.savefig("results/figure2_error_comparison.pdf")
plt.close()

# Figure 3: Noise sensitivity
noise = [0.01, 0.03, 0.05, 0.10]
linear_rmse = [0.066174, 0.066339, 0.066565, 0.067395]
nonlinear_rmse = [0.009022, 0.009565, 0.010440, 0.013604]

plt.figure(figsize=(8, 5))
plt.plot(noise, linear_rmse, marker="o", label="Linear Voltage FGO")
plt.plot(noise, nonlinear_rmse, marker="s", label="Nonlinear Voltage FGO")
plt.xlabel("Voltage Noise Level (V)")
plt.ylabel("RMSE")
plt.title("Noise Sensitivity Analysis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/figure3_noise_sensitivity.png", dpi=300)
plt.savefig("results/figure3_noise_sensitivity.pdf")
plt.close()

print("Figures generated successfully:")
print("results/figure1_soc_comparison.png")
print("results/figure2_error_comparison.png")
print("results/figure3_noise_sensitivity.png")
