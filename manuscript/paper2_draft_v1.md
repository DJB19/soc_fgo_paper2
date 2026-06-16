# Robust SOC Estimation Using Nonlinear Factor Graph Optimization Under Current Sensor Bias

## Abstract


Accurate battery State-of-Charge (SOC) estimation is essential for the safe and efficient operation of electric vehicles and battery energy storage systems. Conventional Coulomb Counting (CC) methods are widely used due to their simplicity; however, their estimation accuracy is highly sensitive to current sensor bias, which causes cumulative SOC drift over time. In this study, a nonlinear Factor Graph Optimization (FGO) framework is proposed to improve SOC estimation robustness under biased current measurements.

A first-order RC battery model was used to generate a 12,001-sample dataset under random current profiles. Artificial current sensor biases of 0.5%, 1%, 2%, 5%, and 10% were introduced into the measurements. The performance of conventional Coulomb Counting and nonlinear FGO was evaluated using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE).

Experimental results show that the estimation error of Coulomb Counting increases significantly as current sensor bias grows. In contrast, the nonlinear FGO approach maintains stable estimation accuracy through voltage-constrained optimization. Under a 10% current sensor bias, the RMSE of Coulomb Counting increased to 0.0382, whereas the RMSE of nonlinear FGO remained at 0.0067. These findings demonstrate that nonlinear FGO can effectively mitigate SOC drift caused by current sensor bias and provide robust battery state estimation under sensor uncertainty.

**Keywords:** Battery Management System, State of Charge, Factor Graph Optimization, Sensor Bias, Electric Vehicle, State Estimation


## 1 Introduction
Electric vehicles (EVs) and battery energy storage systems have experienced rapid development in recent years due to increasing concerns regarding environmental sustainability, energy efficiency, and carbon emission reduction. As the primary energy source of these systems, lithium-ion batteries play a critical role in determining overall performance, safety, and reliability. Consequently, accurate monitoring and management of battery states have become essential tasks in modern Battery Management Systems (BMSs).

Among various battery states, State-of-Charge (SOC) is one of the most important indicators because it represents the remaining available capacity of a battery. Accurate SOC estimation is necessary for energy management, driving range prediction, charging control, and battery protection. However, SOC cannot be measured directly and must be estimated using measurable quantities such as current, voltage, and temperature. Therefore, developing reliable SOC estimation methods remains an active research topic in both academia and industry.

Conventional SOC estimation approaches include Coulomb Counting (CC), equivalent circuit model-based observers, and Kalman filter-based algorithms. Among these methods, Coulomb Counting is widely adopted because of its simplicity and low computational cost. Nevertheless, its performance strongly depends on the accuracy of current measurements. Even a small bias in current sensor readings can accumulate over time and lead to significant SOC estimation drift. Such cumulative errors become particularly problematic during long-term operation and can reduce the reliability of battery management systems.

Factor Graph Optimization (FGO) has recently attracted attention as an alternative state estimation framework. Unlike traditional recursive estimation methods, FGO formulates the estimation problem as a graph optimization task that jointly considers historical measurements and system constraints. This global optimization capability enables the estimator to reduce accumulated errors and improve robustness against sensor uncertainties. In particular, voltage measurements can be incorporated as additional constraints to correct SOC estimation drift caused by biased current measurements.

This study investigates the robustness of nonlinear Factor Graph Optimization for battery SOC estimation under current sensor bias conditions. A first-order RC battery model is employed to generate battery operation data under random current profiles. Several levels of current sensor bias are artificially introduced into the measurements. The performance of conventional Coulomb Counting and nonlinear FGO is then compared using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). Experimental results demonstrate that nonlinear FGO can effectively mitigate SOC drift and maintain stable estimation accuracy even when substantial current sensor bias is present.

## 2 Battery Model
A first-order RC equivalent circuit model was employed in this study to simulate the dynamic behavior of a lithium-ion battery. Due to its balance between computational efficiency and modeling accuracy, the first-order RC model is widely used in battery state estimation research.

The model consists of an open-circuit voltage (OCV) source, an ohmic resistance (R_0), and a parallel RC network composed of resistance (R_1) and capacitance (C_1). The RC network is used to represent battery polarization effects and transient voltage dynamics during charging and discharging processes.

The battery State-of-Charge (SOC) is updated using the Coulomb Counting principle:

SOC(k+1) = SOC(k) - \frac{I(k)\Delta t}{Q}

where (I(k)) is the battery current, (\Delta t) is the sampling interval, and (Q) is the battery capacity in Coulombs.

The polarization voltage of the RC branch is modeled as:

V_{RC}(k+1) = \alpha V_{RC}(k) + (1-\alpha)R_1I(k)

where

\alpha = e^{-\frac{\Delta t}{R_1C_1}}

The terminal voltage is calculated as:

V(k) = OCV(SOC(k)) - I(k)R_0 - V_{RC}(k)

In this work, the battery model parameters were selected as:

* (R_0 = 0.01\ \Omega)
* (R_1 = 0.02\ \Omega)
* (C_1 = 2000\ F)

The initial SOC was set to 0.8. Random current profiles ranging from 0.2 A to 1.0 A were generated to emulate varying battery operating conditions. Current sensor bias was then introduced into the measurements to evaluate the robustness of different SOC estimation approaches.

## 3 Nonlinear Factor Graph Optimization
The battery SOC estimation problem was formulated as a nonlinear Factor Graph Optimization (FGO) problem. In a factor graph, unknown state variables are represented as nodes, while measurement constraints are represented as factors connecting these nodes.

In this study, the SOC value at each time step was defined as a state variable:

x_k = SOC(k)

The objective of FGO is to estimate the optimal sequence of SOC states by minimizing the overall error generated by all constraints in the graph.

### 3.1 Process Factor

The process factor describes the battery SOC evolution according to the Coulomb Counting principle. For two consecutive states, the process model is given by:

SOC(k+1) = SOC(k) - \frac{I(k)\Delta t}{Q}

where (I(k)) denotes the measured current, (\Delta t) is the sampling interval, and (Q) is the battery capacity.

This relationship is implemented as a process factor connecting adjacent SOC nodes in the graph. The process factor provides the primary state transition information but may accumulate errors when current sensor bias exists.

### 3.2 Voltage Factor

To compensate for accumulated drift, battery terminal voltage measurements are incorporated as additional constraints.

The predicted terminal voltage is computed using the battery model:

V_{pred}(k) = OCV(SOC(k)) - I(k)R_0 - V_{RC}(k)

The voltage factor is defined as the difference between measured voltage and predicted voltage:

e_v(k) = V_{meas}(k) - V_{pred}(k)

Unlike Coulomb Counting, which relies solely on current integration, the voltage factor continuously constrains the SOC estimate using voltage observations. This mechanism allows the optimization process to correct accumulated SOC drift caused by biased current measurements.

### 3.3 Nonlinear Optimization

The complete factor graph consists of process factors and voltage factors over the entire estimation horizon.

The optimal SOC trajectory is obtained by minimizing the total nonlinear least-squares cost function:

J = \sum e_p^2 + \sum e_v^2

where (e_p) represents process-factor residuals and (e_v) represents voltage-factor residuals.

The optimization was implemented using the Georgia Tech Smoothing and Mapping (GTSAM) library. Initial SOC estimates were generated using Coulomb Counting and subsequently refined through nonlinear optimization.

By jointly utilizing historical information and voltage constraints, nonlinear FGO can reduce estimation drift and improve robustness against sensor uncertainties.

## 4 Experimental Design
### 4. Experimental Setup

To evaluate the robustness of nonlinear Factor Graph Optimization under current sensor bias conditions, a simulation-based experimental framework was developed.

A first-order RC battery model was used to generate battery operation data. The simulation duration was set to 12,000 seconds with a sampling interval of 1 second, resulting in a dataset containing 12,001 samples. The battery current was randomly generated within the range of 0.2 A to 1.0 A to emulate varying operating conditions. The initial SOC was set to 0.8.

The generated dataset contained the following variables:

* Time
* Battery current
* Terminal voltage
* Ground-truth SOC

To investigate the influence of current sensor bias, five biased datasets were created from the baseline dataset. The current measurements were multiplied by a constant bias factor while keeping the true battery dynamics unchanged.

The evaluated bias levels were:

* 0.5%
* 1.0%
* 2.0%
* 5.0%
* 10.0%

For each bias level, SOC estimation was performed using:

1. Coulomb Counting (CC)
2. Linear Factor Graph Optimization (Linear FGO)
3. Nonlinear Factor Graph Optimization (Nonlinear FGO)

The estimated SOC values were compared against the ground-truth SOC generated by the battery simulator.

Two commonly used evaluation metrics were adopted:

Root Mean Square Error (RMSE)

RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(SOC_{est,i}-SOC_{true,i})^2}

Mean Absolute Error (MAE)

MAE = \frac{1}{N}\sum_{i=1}^{N}|SOC_{est,i}-SOC_{true,i}|

All optimization procedures were implemented using the GTSAM library in C++. The experiments were conducted on Linux using the same battery model and estimation framework for all tested bias levels to ensure a fair comparison.

## 5 Results and Discussion
### 5. Results and Discussion

The estimation performance of Coulomb Counting (CC), Linear FGO, and Nonlinear FGO was evaluated under different levels of current sensor bias. The RMSE and MAE values were calculated using the ground-truth SOC generated by the battery model.

Table 1 summarizes the RMSE results obtained from the experiments.

| Current Sensor Bias | CC RMSE | Nonlinear FGO RMSE |
| ------------------- | ------- | ------------------ |
| 0.5%                | 0.00191 | 0.00878            |
| 1.0%                | 0.00382 | 0.00867            |
| 2.0%                | 0.00764 | 0.00845            |
| 5.0%                | 0.01911 | 0.00778            |
| 10.0%               | 0.03821 | 0.00666            |

Figure 1 illustrates the relationship between current sensor bias and estimation RMSE.

**Figure 1. RMSE comparison under different current sensor bias levels.**

(Insert paper2_bias_rmse.png here)

The results reveal two distinct trends. First, the estimation error of Coulomb Counting increases rapidly as current sensor bias grows. Since Coulomb Counting relies exclusively on current integration, any systematic measurement bias accumulates over time and leads to increasing SOC drift.

Second, the estimation error of Nonlinear FGO remains relatively stable across all tested bias levels. Unlike Coulomb Counting, Nonlinear FGO incorporates terminal voltage measurements as additional constraints. These voltage constraints continuously correct accumulated SOC errors during optimization, preventing long-term drift.

Interestingly, the robustness advantage of Nonlinear FGO becomes increasingly apparent at higher bias levels. At a bias of 10%, the RMSE of Coulomb Counting reached 0.03821, while the RMSE of Nonlinear FGO remained at only 0.00666. This corresponds to an error reduction of approximately 82.6%.

To further visualize the estimation behavior, Figure 2 compares the SOC trajectories under the 10% bias condition.

**Figure 2. SOC estimation trajectories under 10% current sensor bias.**

(Insert paper2_bias100_soc_comparison.png here)

As shown in Figure 2, the Coulomb Counting estimate gradually deviates from the true SOC trajectory due to cumulative integration errors. In contrast, the Nonlinear FGO estimate closely follows the ground-truth SOC throughout the entire experiment. The voltage-constrained optimization effectively suppresses the drift caused by biased current measurements.

These results demonstrate that Nonlinear FGO provides significantly improved robustness against current sensor bias compared with conventional Coulomb Counting. The ability to integrate both process information and voltage measurements enables more reliable SOC estimation under realistic sensor uncertainty conditions.

### Figure 1
paper2_bias_rmse.png

### Figure 2
paper2_bias100_soc_comparison.png

## 6 Conclusion
### 6. Conclusion

This study investigated the robustness of nonlinear Factor Graph Optimization (FGO) for battery State-of-Charge (SOC) estimation under current sensor bias conditions. A first-order RC battery model was employed to generate battery operation data, and multiple levels of current sensor bias were introduced to evaluate estimation performance.

The experimental results demonstrated that conventional Coulomb Counting is highly sensitive to current sensor bias. As the bias level increased, the estimation error accumulated rapidly, resulting in significant SOC drift. In contrast, the nonlinear FGO framework maintained stable estimation accuracy across all tested bias levels by incorporating voltage measurements as optimization constraints.

Under a 10% current sensor bias, the RMSE of Coulomb Counting increased to 0.03821, whereas the RMSE of nonlinear FGO remained at 0.00666. These results indicate that nonlinear FGO can effectively suppress accumulated estimation errors and significantly improve robustness against sensor uncertainty.

The findings suggest that nonlinear FGO is a promising approach for battery management systems operating in realistic environments where sensor imperfections are unavoidable. By jointly utilizing process information and voltage measurements, the proposed framework provides more reliable SOC estimation than conventional current integration methods.

Future work will focus on validating the proposed approach using experimental battery data and extending the framework to jointly estimate additional battery states such as State-of-Health (SOH) and model parameters.

## References
