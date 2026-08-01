# Robust Battery State-of-Charge Estimation under Current Sensor Bias Using Nonlinear Factor Graph Optimization

This repository is the submission-aligned code and processed-data release for the article by Lei Zhang and Daisuke Tashima. It contains the nonlinear GTSAM estimator, the controlled simulation dataset, processed NASA B0005 supporting-case data, numerical summaries, and scripts used to reproduce the reported tables and figures.

## Verified headline results

| Test | Coulomb counting RMSE | Nonlinear FGO RMSE |
|---|---:|---:|
| Simulation, 10% current bias | 0.038210 | 0.003092 |
| NASA B0005 supporting case, 10% bias | 0.057197 | 0.010111 |

Across the five simulated bias levels, the origin-constrained propagation coefficients are 0.003821 per 1% bias for Coulomb counting and 0.000309 per 1% bias for nonlinear FGO, a reduction of 91.9%.

## Repository contents

```text
.
├── include/                         # GTSAM custom factors
├── src/main_nonlinear.cpp           # RC-consistent nonlinear FGO estimator
├── scripts/
│   ├── generate_bias_datasets.py    # creates the five biased simulation inputs
│   ├── run_simulation_pipeline.py   # runs the estimator and writes metrics
│   ├── evaluate_nasa_supporting_case.py
│   └── make_figures.py
├── data/
│   ├── simulation/paper2_clean_base.csv
│   └── nasa/                        # processed B0005 cycle and FGO trajectories
├── results/                         # submission-aligned numerical results
└── figures/                         # the three figures used in the manuscript
```

Historical drafts, teacher-review files, Paper 1 outputs, noise-only tests, and invalid intermediate results were deliberately excluded from this release.

## Simulation reproduction

Requirements:

- CMake 3.16 or later
- C++14 compiler
- GTSAM 4.x
- Python 3.9 or later
- Python packages in `requirements.txt` for plotting

From the repository root:

```bash
python scripts/generate_bias_datasets.py
cmake -S . -B build
cmake --build build -j
python scripts/run_simulation_pipeline.py --executable build/soc_fgo_nonlinear
```

The pipeline evaluates 0.5%, 1%, 2%, 5%, and 10% multiplicative current bias. It writes the trajectory files to `generated/simulation/` and the summary to `generated/simulation_metrics.csv`. The historical output column `soc_kf` is retained for compatibility; it is Coulomb counting, not a Kalman-filter estimate.

The model parameters match the manuscript: Q = 3.0 Ah, R0 = 0.05 ohm, R1 = 0.02 ohm, C1 = 2000 F, sigma0 = 1e-4, sigmap = 1e-3, and sigmav = 0.02 V. The RC polarization voltage is reconstructed from the biased current supplied to the estimator.

## NASA B0005 supporting case

Run:

```bash
python scripts/evaluate_nasa_supporting_case.py
```

The script evaluates only the 180 active-discharge samples from 0 to 3346.937 s and leaves Coulomb-counting SOC unclipped so accumulated drift is preserved. It reproduces `results/nasa_metrics.csv` and the 10% trajectory used in Figure 3.

This is a controlled supporting case, not an independent validation: reference SOC and the empirical voltage model were derived from the same first-discharge record. The original NASA MATLAB files are not redistributed here. They are available from the [NASA Ames Prognostics Center of Excellence Data Set Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).

## Figures

```bash
python -m pip install -r requirements.txt
python scripts/make_figures.py
```

The generated figures are written to `generated/figures/`. Checked copies corresponding to the submitted manuscript are included in `figures/`.

## Data notes

- `data/simulation/paper2_clean_base.csv` contains the unbiased, model-generated trajectory.
- Biased simulation inputs preserve the reference SOC and terminal voltage and multiply only current by `(1 + bias)`.
- `data/nasa/nasa_B0005_discharge_cycle_1.csv` is the processed first B0005 discharge cycle.
- `data/nasa/nasa_fgo_bias*.csv` contains processed FGO trajectories used by the supporting-case evaluation.
- Numerical values reported in the article are collected in `results/simulation_metrics.csv` and `results/nasa_metrics.csv`.

## License

Code is released under the MIT License. The processed NASA data remain subject to the terms of the original NASA source.

