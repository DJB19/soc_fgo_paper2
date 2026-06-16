import pandas as pd
import numpy as np

files = [
    "results/paper2_linear_noise003.csv",
    "results/paper2_nonlinear_noise003.csv",
    "results/paper2_linear_noise005.csv",
    "results/paper2_nonlinear_noise005.csv",
    "results/paper2_linear_noise010.csv",
    "results/paper2_nonlinear_noise010.csv"
]

for f in files:
    print("\n====================")
    print(f)

    df = pd.read_csv(f)

    rmse_cc = np.sqrt(np.mean((df["soc_kf"]-df["soc_true"])**2))
    rmse_fgo = np.sqrt(np.mean((df["soc_fgo"]-df["soc_true"])**2))

    mae_cc = np.mean(np.abs(df["soc_kf"]-df["soc_true"]))
    mae_fgo = np.mean(np.abs(df["soc_fgo"]-df["soc_true"]))

    print("CC RMSE :", rmse_cc)
    print("FGO RMSE:", rmse_fgo)
    print("CC MAE  :", mae_cc)
    print("FGO MAE :", mae_fgo)
