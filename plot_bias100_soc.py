import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/paper2_nonlinear_bias100.csv")

plt.figure(figsize=(9,5))

plt.plot(df["time"], df["soc_true"], label="True SOC")
plt.plot(df["time"], df["soc_kf"], label="Coulomb Counting")
plt.plot(df["time"], df["soc_fgo"], label="Nonlinear FGO")

plt.xlabel("Time (s)")
plt.ylabel("SOC")
plt.grid(True)
plt.legend()

plt.savefig("paper2_bias100_soc_comparison.png", dpi=300)
plt.show()
