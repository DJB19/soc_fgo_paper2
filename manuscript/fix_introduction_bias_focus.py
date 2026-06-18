from pathlib import Path

path = Path("paper2_draft.md")
text = path.read_text(encoding="utf-8")

intro_start = text.index("## 1 Introduction")
section2_start = text.index("## 2 Battery Model")

new_intro = """## 1 Introduction

Accurate State-of-Charge (SOC) estimation is essential for the safe and reliable operation of electric vehicles and battery energy storage systems. In practical Battery Management Systems (BMSs), SOC cannot be measured directly and is usually estimated from measurable signals such as current, voltage, and temperature. Among these signals, current measurement plays a central role because many SOC estimation methods rely on current integration or current-based state transition models. Therefore, even a small current sensor bias can accumulate over time and cause significant SOC estimation drift.

Coulomb Counting (CC) is one of the most widely used SOC estimation methods due to its simplicity and low computational cost. However, CC directly integrates the measured current, which makes it highly sensitive to current measurement errors. When a constant or slowly varying current sensor bias exists, the resulting SOC error accumulates monotonically during battery operation. This drift problem becomes especially serious during long-term operation and can reduce the reliability of energy management, driving range prediction, and battery protection functions.

To reduce accumulated estimation errors, model-based and optimization-based methods have been investigated for battery state estimation. Factor Graph Optimization (FGO) provides a flexible framework for combining multiple sources of information, such as current-based process constraints and voltage-based measurement constraints, into a unified optimization problem. Compared with simple current integration, FGO can use voltage measurements to correct the SOC trajectory and suppress drift caused by biased current measurements.

This study investigates the robustness of nonlinear FGO for battery SOC estimation under current sensor bias conditions. A first-order RC battery model is employed to generate battery operation data under random current profiles. Several levels of artificial current sensor bias are introduced into the measurements. The performance of conventional Coulomb Counting and nonlinear FGO is then compared using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). In addition, a preliminary real-data validation is conducted using the NASA B0005 lithium-ion battery aging dataset to further evaluate the proposed method under realistic voltage and current measurement conditions.

Unlike general SOC estimation studies that mainly compare estimation accuracy under nominal measurement conditions, this work focuses specifically on the robustness of SOC estimation under current sensor bias. The main objective is not only to evaluate whether nonlinear FGO can estimate SOC accurately, but also to investigate whether it can suppress the cumulative drift caused by biased current measurements.

The main contributions of this study are summarized as follows:

1. A current-sensor-bias-oriented SOC estimation problem is formulated to analyze the cumulative drift of Coulomb Counting under biased current measurements.

2. A nonlinear FGO-based SOC estimation framework is developed by combining current-based process constraints and voltage-based measurement constraints to improve robustness against current sensor bias.

3. The proposed method is evaluated using both controlled simulation data with multiple current bias levels and preliminary real battery validation based on the NASA B0005 dataset.

"""

new_text = text[:intro_start] + new_intro + text[section2_start:]
path.write_text(new_text, encoding="utf-8")

print("Introduction updated with current-sensor-bias focus.")
