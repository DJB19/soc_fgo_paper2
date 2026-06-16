# Robust SOC Estimation Using Nonlinear Factor Graph Optimization Under Current Sensor Bias

This repository contains the source code, datasets, experimental results, figures, and manuscript draft for a research study on robust battery State-of-Charge (SOC) estimation under current sensor bias using nonlinear Factor Graph Optimization (FGO).

The main purpose of this project is to evaluate whether nonlinear FGO can reduce SOC drift caused by biased current measurements compared with conventional Coulomb Counting (CC).

## Research Background

Accurate SOC estimation is essential for Battery Management Systems (BMSs) in electric vehicles and battery energy storage systems. Coulomb Counting is simple and widely used, but it is highly sensitive to current sensor bias because current measurement errors accumulate over time through integration.

To address this issue, this study applies nonlinear Factor Graph Optimization, which jointly considers:

- current-based SOC transition constraints,
- voltage-based measurement constraints,
- global optimization over the full SOC trajectory.

## Main Contributions

This repository includes:

1. A first-order RC battery model for generating simulation data.
2. Current sensor bias experiments under 0.5%, 1%, 2%, 5%, and 10% bias levels.
3. Comparison between Coulomb Counting, linear FGO, and nonlinear FGO.
4. NASA B0005 real battery dataset validation.
5. SOC estimation error evaluation using RMSE and MAE.
6. Figures and manuscript draft for Paper2.

## Key Results

### Simulation Validation

Using a 12,001-sample simulated battery dataset under random current profiles, the following result was obtained under 10% current sensor bias:

| Method | RMSE |
|---|---:|
| Coulomb Counting | 0.0382 |
| Nonlinear FGO | 0.0067 |

The simulation results show that Coulomb Counting error increases as current bias grows, while nonlinear FGO maintains stable SOC estimation accuracy.

### NASA B0005 Validation

The first discharge cycle of the NASA B0005 lithium-ion battery aging dataset was extracted and converted into CSV format. Artificial current measurement biases of 5% and 10% were introduced.

| Current Bias | CC RMSE | Nonlinear FGO RMSE |
|---:|---:|---:|
| 5% | 0.02585 | 0.01618 |
| 10% | 0.04941 | 0.01618 |

The NASA validation further confirms that nonlinear FGO is more robust than Coulomb Counting under current sensor bias.

## Repository Structure

```text
.
 data/
 results/
 manuscript/
   ├── paper2_draft.md
   └── figures/
 src/
 main.cpp
 main_clean.cpp
 main_nonlinear.cpp
 analysis scripts


