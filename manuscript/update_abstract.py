from pathlib import Path

path = Path("paper2_draft.md")
text = path.read_text()

start = text.index("## Abstract")
end = text.index("## 1 Introduction")

new_abstract = """## Abstract

Accurate battery State-of-Charge (SOC) estimation is essential for the safe and efficient operation of electric vehicles and battery energy storage systems. Conventional Coulomb Counting (CC) methods are widely used due to their simplicity; however, their estimation accuracy is highly sensitive to current sensor bias, which causes cumulative SOC drift over time. In this study, a nonlinear Factor Graph Optimization (FGO) framework is proposed to improve SOC estimation robustness under biased current measurements by jointly considering current-based SOC transition constraints and voltage-based measurement constraints.

A first-order RC battery model was first used to generate a 12,001-sample simulation dataset under random current profiles. Artificial current sensor biases of 0.5%, 1%, 2%, 5%, and 10% were introduced into the measurements. The performance of conventional Coulomb Counting and nonlinear FGO was evaluated using Root Mean Square Error (RMSE) and Mean Absolute Error (MAE). In addition, a real-data validation experiment was conducted using the first discharge cycle of the NASA B0005 lithium-ion battery aging dataset. In the NASA validation, artificial current measurement biases of 5% and 10% were introduced to evaluate the robustness of both methods under realistic voltage and current measurement conditions.

Simulation results show that the estimation error of Coulomb Counting increases significantly as current sensor bias grows, while the nonlinear FGO approach maintains stable estimation accuracy through voltage-constrained optimization. Under a 10% current sensor bias in the simulation dataset, the RMSE of Coulomb Counting increased to 0.0382, whereas the RMSE of nonlinear FGO remained at 0.0067. The NASA B0005 validation further confirmed this trend. Under 5% and 10% current bias, Coulomb Counting produced RMSE values of 0.02585 and 0.04941, respectively, while nonlinear FGO maintained a nearly stable RMSE of approximately 0.01618. These findings demonstrate that nonlinear FGO can effectively mitigate SOC drift caused by current sensor bias and provide robust battery state estimation under sensor uncertainty.

**Keywords:** Battery Management System, State of Charge, Factor Graph Optimization, Sensor Bias, Electric Vehicle, State Estimation

"""

new_text = text[:start] + new_abstract + text[end:]
path.write_text(new_text)

print("Abstract updated.")
