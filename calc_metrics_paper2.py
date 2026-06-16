import pandas as pd
import numpy as np

files = [
    "results/paper2_linear_noise003.csv",
    "results/paper2_nonlinear_noise003.csv"
]

for f in files:
    df = pd.read_csv(f)

    rmse_kf = np.sqrt(np.mean((df["soc_kf"]-df["soc_true"])**2))
    rmse_fgo = np.sqrt(np.mean((df["soc_fgo"]-df["soc_true"])**2))

    mae_kf = np.mean(np.abs(df["soc_kf"]-df["soc_true"]))
    mae_fgo = np.mean(np.abs(df["soc_fgo"]-df["soc_true"]))

    print()
    print(f)
    print("KF RMSE :", rmse_kf)
    print("FGO RMSE:", rmse_fgo)
    print("KF MAE  :", mae_kf)
    print("FGO MAE :", mae_fgo)

