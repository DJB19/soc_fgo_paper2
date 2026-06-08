# SOC-FGO-Paper1

Factor Graph Optimization (FGO) Based Battery State-of-Charge Estimation Using GTSAM

## Overview

This repository contains the source code, datasets, and experimental results associated with the paper:

**"Factor Graph Optimization for Battery State-of-Charge Estimation: A Comparative Study with Conventional Approaches"**

The objective of this work is to investigate the applicability of Factor Graph Optimization (FGO) for battery State-of-Charge (SOC) estimation and compare its performance with traditional estimation approaches under different measurement conditions.

---

## Features

* Linear voltage measurement model
* Nonlinear voltage measurement model
* GTSAM-based factor graph optimization
* Noise sensitivity analysis
* Random current profile testing
* Reproducible simulation environment
* Publication-ready figures and evaluation scripts

---

## Repository Structure

```text
.
├── src/
│   └── battery_model.cpp
│
├── data/
│   └── input datasets
│
├── results/
│   ├── SOC estimation results
│   ├── comparison figures
│   └── evaluation metrics
│
├── main.cpp
├── main_clean.cpp
├── main_nonlinear.cpp
│
├── SOCProcessFactor.h
├── SOCVoltageFactor.h
├── SOCVoltageFactorNonlinear.h
│
└── plot_paper1_figures.py
```

## Requirements

* Ubuntu Linux
* CMake >= 3.20
* GTSAM 4.x
* Eigen3
* C++17

---

## Build

```bash
mkdir build
cd build

cmake ..
make -j
```

---

## Run

Linear model:

```bash
./soc_fgo_clean
```

Nonlinear model:

```bash
./soc_fgo_nonlinear
```

---

## Experimental Results

The repository includes:

* SOC estimation trajectories
* Error comparison analysis
* Noise sensitivity evaluation
* Publication-ready PDF and PNG figures

Generated figures:

```text
results/
├── figure1_soc_comparison.pdf
├── figure2_error_comparison.pdf
└── figure3_noise_sensitivity.pdf
```

---

## Reproducibility

All simulation data, source code, plotting scripts, and factor graph implementations are provided to support full reproducibility of the published results.

---

## Future Work

Planned extensions include:

* Real-world battery datasets
* Battery aging (SOH) estimation
* Sliding-window optimization
* Comparison with EKF and UKF
* Public benchmark dataset evaluation

---



## Author

Lei Zhang

Doctoral Researcher

Fukuoka Institute of Technology

Faculty of Engineering

Department of Electrical Engineering

Tashima Laboratory

Japan


---

## License

This repository is released for academic and research purposes.
