import pandas as pd
import numpy as np

files = [
    ("0.5%", "Linear FGO", "results/paper2_linear_bias005.csv"),
    ("0.5%", "Nonlinear FGO", "results/paper2_nonlinear_bias005.csv"),
    ("1.0%", "Linear FGO", "results/paper2_linear_bias010.csv"),
    ("1.0%", "Nonlinear FGO", "results/paper2_nonlinear_bias010.csv"),
    ("2.0%", "Linear FGO", "results/paper2_linear_bias020.csv"),
    ("2.0%", "Nonlinear FGO", "results/paper2_nonlinear_bias020.csv"),
    ("5.0%", "Linear FGO", "results/paper2_linear_bias050.csv"),
    ("5.0%", "Nonlinear FGO", "results/paper2_nonlinear_bias050.csv"),
    ("10.0%", "Linear FGO", "results/paper2_linear_bias100.csv"),
    ("10.0%", "Nonlinear FGO", "results/paper2_nonlinear_bias100.csv"),
]

print("Bias,Method,CC_RMSE,FGO_RMSE,CC_MAE,FGO_MAE")

for bias, method, f in files:
    df = pd.read_csv(f)

    cc_rmse = np.sqrt(np.mean((df["soc_kf"] - df["soc_true"])**2))
    fgo_rmse = np.sqrt(np.mean((df["soc_fgo"] - df["soc_true"])**2))

    cc_mae = np.mean(np.abs(df["soc_kf"] - df["soc_true"]))
    fgo_mae = np.mean(np.abs(df["soc_fgo"] - df["soc_true"]))

    print(f"{bias},{method},{cc_rmse},{fgo_rmse},{cc_mae},{fgo_mae}")
