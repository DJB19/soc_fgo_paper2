import pandas as pd
import numpy as np

files = [
    "results/paper2_linear_bias005.csv",
    "results/paper2_nonlinear_bias005.csv"
]

for f in files:
    print("\n====================")
    print(f)

    df = pd.read_csv(f)

    cc_rmse = np.sqrt(np.mean((df["soc_kf"]-df["soc_true"])**2))
    fgo_rmse = np.sqrt(np.mean((df["soc_fgo"]-df["soc_true"])**2))

    cc_mae = np.mean(np.abs(df["soc_kf"]-df["soc_true"]))
    fgo_mae = np.mean(np.abs(df["soc_fgo"]-df["soc_true"]))

    print("CC RMSE :", cc_rmse)
    print("FGO RMSE:", fgo_rmse)
    print("CC MAE  :", cc_mae)
    print("FGO MAE :", fgo_mae)
