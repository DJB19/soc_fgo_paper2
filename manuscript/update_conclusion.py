from pathlib import Path

path = Path("paper2_draft.md")
text = path.read_text()

start = text.index("## 6 Conclusion")
end = text.index("## References")

new_conclusion = """## 6 Conclusion

This study investigated the robustness of nonlinear Factor Graph Optimization (FGO) for battery State-of-Charge (SOC) estimation under current sensor bias. A first-order RC battery model was used to generate a 12,001-sample simulation dataset under random current profiles, and artificial current sensor biases ranging from 0.5% to 10% were introduced to evaluate the sensitivity of Coulomb Counting (CC) and nonlinear FGO.

The simulation results showed that Coulomb Counting is highly sensitive to current sensor bias because the bias is accumulated over time through current integration. As the current bias increased, the SOC estimation error of CC increased rapidly. In contrast, nonlinear FGO maintained stable estimation accuracy by jointly considering current-based process constraints and voltage-based measurement constraints. Under a 10% current sensor bias, the RMSE of Coulomb Counting increased to 0.0382, whereas nonlinear FGO achieved a much lower RMSE of 0.0067.

To further validate the proposed approach, an additional experiment was conducted using real battery data from the NASA B0005 lithium-ion battery aging dataset. The first discharge cycle of B0005 was extracted, and artificial current measurement biases of 5% and 10% were introduced. The NASA validation results further confirmed the simulation findings. Under 5% and 10% current bias, Coulomb Counting produced RMSE values of 0.02585 and 0.04941, respectively, while nonlinear FGO maintained a nearly stable RMSE of approximately 0.01618. These results demonstrate that nonlinear FGO can effectively reduce SOC drift caused by biased current measurements.

Overall, the proposed nonlinear FGO framework provides a robust SOC estimation approach under current sensor uncertainty. By incorporating voltage-related constraints into a global optimization framework, FGO can compensate for the cumulative drift that affects conventional Coulomb Counting. Future work will focus on extending the proposed method to joint SOC/SOH estimation, validating the framework using additional real-world battery datasets, and implementing the algorithm in real-time battery management systems.

"""

new_text = text[:start] + new_conclusion + text[end:]
path.write_text(new_text)

print("Conclusion updated.")
