import pandas as pd
import numpy as np

input_file = "sensor_data_random_12000s.csv"
df = pd.read_csv(input_file)

np.random.seed(42)

noise_levels = {
    "003": 0.03,
    "005": 0.05,
    "010": 0.10
}

for tag, level in noise_levels.items():
    out = df.copy()

    current_noise = np.random.normal(0, level, len(out))
    voltage_noise = np.random.normal(0, level, len(out))

    out["current"] = out["current"] * (1 + current_noise)
    out["voltage"] = out["voltage"] * (1 + voltage_noise)

    output_file = f"data/paper2_noise{tag}.csv"
    out.to_csv(output_file, index=False)
    print(f"Created {output_file}")

print("Done.")
