#!/usr/bin/env python3
"""Reproduce the active-discharge NASA B0005 supporting-case metrics."""

import argparse
import csv
import math
from pathlib import Path


CUTOFF_SECONDS = 3346.937
CASES = ((0.0, "000"), (0.05, "005"), (0.10, "010"))


def score(estimate: list[float], reference: list[float]) -> tuple[float, float]:
    errors = [value - truth for value, truth in zip(estimate, reference)]
    return (
        math.sqrt(sum(error * error for error in errors) / len(errors)),
        sum(abs(error) for error in errors) / len(errors),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/nasa"))
    parser.add_argument("--output-dir", type=Path, default=Path("generated/nasa"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with (args.data_dir / "nasa_B0005_discharge_cycle_1.csv").open(
        newline="", encoding="utf-8"
    ) as stream:
        raw = list(csv.DictReader(stream))
    raw_by_time = {round(float(row["time"]), 3): row for row in raw}

    summary = []
    trajectory_10 = []
    for bias, code in CASES:
        with (args.data_dir / f"nasa_fgo_bias{code}.csv").open(
            newline="", encoding="utf-8"
        ) as stream:
            processed = list(csv.DictReader(stream))
        active = [
            row for row in processed if float(row["time"]) <= CUTOFF_SECONDS + 1e-9
        ]
        reference = [
            float(raw_by_time[round(float(row["time"]), 3)]["soc_ref"])
            for row in active
        ]
        # The reference is normalized Coulomb integration of the original current.
        # Applying multiplicative bias without clipping gives this exact CC trajectory.
        cc = [1.0 + (1.0 + bias) * (truth - 1.0) for truth in reference]
        fgo = [float(row["soc_fgo"]) for row in active]
        cc_rmse, cc_mae = score(cc, reference)
        fgo_rmse, fgo_mae = score(fgo, reference)
        summary.append((100.0 * bias, cc_rmse, fgo_rmse, cc_mae, fgo_mae, len(active)))

        if code == "010":
            trajectory_10 = [
                (row["time"], truth, cc_value, fgo_value)
                for row, truth, cc_value, fgo_value in zip(active, reference, cc, fgo)
            ]

    summary_path = args.output_dir / "nasa_metrics.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("Bias_percent", "CC_RMSE", "FGO_RMSE", "CC_MAE", "FGO_MAE", "samples"))
        writer.writerows(summary)

    trajectory_path = args.output_dir / "nasa_bias100_trajectory.csv"
    with trajectory_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("time", "soc_ref", "soc_cc_unclipped", "soc_fgo"))
        writer.writerows(trajectory_10)

    print(summary_path)
    print(trajectory_path)


if __name__ == "__main__":
    main()

