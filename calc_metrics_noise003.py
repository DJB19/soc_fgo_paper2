import csv
import math

files = [
    ("Noise003 Linear Voltage FGO", "results/result_random_linear_voltage_noise003.csv"),
    ("Noise003 Nonlinear Voltage FGO", "results/result_random_nonlinear_voltage_noise003.csv"),
]

print("Method,RMSE_KF,MAE_KF,MAX_KF,RMSE_FGO,MAE_FGO,MAX_FGO")

for name, path in files:
    true_vals = []
    kf_vals = []
    fgo_vals = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            true_vals.append(float(row["soc_true"]))
            kf_vals.append(float(row["soc_kf"]))
            fgo_vals.append(float(row["soc_fgo"]))

    n = len(true_vals)
    err_kf = [abs(t - k) for t, k in zip(true_vals, kf_vals)]
    err_fgo = [abs(t - g) for t, g in zip(true_vals, fgo_vals)]

    rmse_kf = math.sqrt(sum(e * e for e in err_kf) / n)
    mae_kf = sum(err_kf) / n
    max_kf = max(err_kf)

    rmse_fgo = math.sqrt(sum(e * e for e in err_fgo) / n)
    mae_fgo = sum(err_fgo) / n
    max_fgo = max(err_fgo)

    print(f"{name},{rmse_kf:.6f},{mae_kf:.6f},{max_kf:.6f},{rmse_fgo:.6f},{mae_fgo:.6f},{max_fgo:.6f}")
