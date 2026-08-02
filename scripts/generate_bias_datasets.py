#!/usr/bin/env python3
"""Create current-biased simulation inputs without changing voltage or truth."""

import argparse
import csv
from pathlib import Path


DEFAULT_BIASES = (0.005, 0.01, 0.02, 0.05, 0.10)


def label(bias: float) -> str:
    return f"{round(1000 * bias):03d}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/simulation/paper2_clean_base.csv"),
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("generated/simulation_inputs")
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with args.input.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))

    for bias in DEFAULT_BIASES:
        output = args.output_dir / f"paper2_bias{label(bias)}.csv"
        with output.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(
                stream, fieldnames=("time", "current", "voltage", "soc_true")
            )
            writer.writeheader()
            for row in rows:
                writer.writerow(
                    {
                        "time": row["time"],
                        "current": f"{float(row['current']) * (1.0 + bias):.16g}",
                        "voltage": row["voltage"],
                        "soc_true": row["soc_true"],
                    }
                )
        print(output)


if __name__ == "__main__":
    main()

