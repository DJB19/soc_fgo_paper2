#!/usr/bin/env python3
"""Run all five GTSAM bias cases and calculate submission metrics."""

import argparse
import csv
import math
import subprocess
import sys
from pathlib import Path


BIAS_LABELS = ((0.5, "005"), (1.0, "010"), (2.0, "020"), (5.0, "050"), (10.0, "100"))


def metrics(path: Path) -> tuple[float, float, float, float]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    truth = [float(row["soc_true"]) for row in rows]
    cc = [float(row["soc_kf"]) for row in rows]
    fgo = [float(row["soc_fgo"]) for row in rows]

    def pair(values: list[float]) -> tuple[float, float]:
        errors = [estimate - reference for estimate, reference in zip(values, truth)]
        return (
            math.sqrt(sum(error * error for error in errors) / len(errors)),
            sum(abs(error) for error in errors) / len(errors),
        )

    cc_rmse, cc_mae = pair(cc)
    fgo_rmse, fgo_mae = pair(fgo)
    return cc_rmse, fgo_rmse, cc_mae, fgo_mae


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable", type=Path, required=True)
    parser.add_argument(
        "--input-dir", type=Path, default=Path("generated/simulation_inputs")
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("generated/simulation")
    )
    parser.add_argument(
        "--summary", type=Path, default=Path("generated/simulation_metrics.csv")
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        subprocess.run([sys.executable, "scripts/generate_bias_datasets.py"], check=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)

    summary_rows = []
    for bias_percent, code in BIAS_LABELS:
        source = args.input_dir / f"paper2_bias{code}.csv"
        output = args.output_dir / f"simulation_bias{code}.csv"
        subprocess.run([str(args.executable), str(source), str(output)], check=True)
        values = metrics(output)
        summary_rows.append((bias_percent, *values))

    with args.summary.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(("Bias_percent", "CC_RMSE", "FGO_RMSE", "CC_MAE", "FGO_MAE"))
        writer.writerows(summary_rows)
    print(args.summary)


if __name__ == "__main__":
    main()

