# Robust Battery State-of-Charge Estimation under Current Sensor Bias Using Nonlinear Factor Graph Optimization

This repository contains the source code, simulation results, manuscript draft, and validation materials for the second paper on battery State-of-Charge (SOC) estimation using nonlinear Factor Graph Optimization (FGO).

## Research Focus

This study focuses specifically on the robustness of SOC estimation under current sensor bias. Unlike general SOC estimation studies that mainly compare estimation accuracy under nominal measurement conditions, this work investigates how biased current measurements cause cumulative SOC drift and how nonlinear FGO can mitigate this drift by incorporating voltage-based measurement constraints.

The main objective is to compare conventional Coulomb Counting (CC) and nonlinear FGO under different levels of artificial current sensor bias.

## Paper Title

**Robust Battery State-of-Charge Estimation under Current Sensor Bias Using Nonlinear Factor Graph Optimization**

## Main Contributions

1. A current-sensor-bias-oriented SOC estimation problem is formulated to analyze the cumulative drift of Coulomb Counting under biased current measurements.

2. A nonlinear FGO-based SOC estimation framework is developed by combining current-based SOC transition constraints and voltage-based measurement constraints.

3. The proposed method is evaluated using both controlled simulation data and preliminary real battery validation based on the NASA B0005 lithium-ion battery aging dataset.

## Simulation Study

A first-order RC battery model was used to generate a 12,001-sample simulation dataset under random current profiles. Artificial current sensor biases of 0.5%, 1%, 2%, 5%, and 10% were introduced into the current measurements.

The simulation results show that the estimation error of Coulomb Counting increases as current sensor bias grows, while nonlinear FGO maintains more stable estimation accuracy through voltage-constrained optimization.

For example, under a 10% current sensor bias in the simulation dataset:

- Coulomb Counting RMSE: 0.0382
- Nonlinear FGO RMSE: 0.0067

## NASA B0005 Preliminary Validation

A preliminary real-data validation was conducted using the first discharge cycle of the NASA B0005 lithium-ion battery aging dataset. Artificial current biases of 5% and 10% were applied to the measured current signal.

The NASA validation results further support the robustness of nonlinear FGO under current sensor bias:

| Current Bias | Coulomb Counting RMSE | Nonlinear FGO RMSE |
|---|---:|---:|
| 5% | 0.02585 | 0.01618 |
| 10% | 0.04941 | 0.01618 |

These results indicate that nonlinear FGO can reduce current-bias-induced SOC drift under realistic voltage and current measurement conditions.

## Repository Structure

```text
.
 data/                         # Simulation and processed validation datasets
 results/                      # Output results from CC and FGO experiments
 src/                          # C++ source code for battery model and FGO experiments
 manuscript/                   # Manuscript draft, figures, and teacher review files
   ├── paper2_draft.md
   ├── paper2_draft_for_teacher.html
   ├── paper2_draft_for_teacher_selfcontained.html
   └── figures/
 CMakeLists.txt
 README.md

eof

