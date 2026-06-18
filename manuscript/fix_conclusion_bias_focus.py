from pathlib import Path

path = Path("paper2_draft.md")
text = path.read_text(encoding="utf-8")

conclusion_start = text.index("## 6 Conclusion")
references_start = text.index("## References")

new_conclusion = """## 6 Conclusion

This study investigated the robustness of nonlinear Factor Graph Optimization (FGO) for battery State-of-Charge (SOC) estimation under current sensor bias. Unlike general SOC estimation studies under nominal measurement conditions, this work focused specifically on the cumulative drift caused by biased current measurements and evaluated whether voltage-constrained nonlinear FGO can mitigate this error.

Simulation results based on a first-order RC battery model showed that Coulomb Counting is highly sensitive to current sensor bias. As the bias level increased from 0.5% to 10%, the SOC estimation error of Coulomb Counting increased continuously. In contrast, nonlinear FGO maintained stable estimation accuracy by jointly using current-based process constraints and voltage-based measurement constraints. Under a 10% current sensor bias, Coulomb Counting produced an RMSE of 0.0382, whereas nonlinear FGO achieved an RMSE of 0.0067.

A preliminary real-data validation was also conducted using the first discharge cycle of the NASA B0005 lithium-ion battery aging dataset. Under 5% and 10% artificial current bias, Coulomb Counting produced RMSE values of 0.02585 and 0.04941, respectively, while nonlinear FGO maintained a nearly stable RMSE of approximately 0.01618. These results further support the conclusion that nonlinear FGO can reduce current-bias-induced SOC drift under realistic voltage and current measurement conditions.

The main finding of this study is that nonlinear FGO can improve SOC estimation robustness under sensor uncertainty by using voltage measurements to constrain the SOC trajectory. Future work will extend the validation to multiple battery cells, different aging stages, various temperature conditions, and real experimental current sensor bias scenarios.

"""

new_text = text[:conclusion_start] + new_conclusion + text[references_start:]
path.write_text(new_text, encoding="utf-8")

print("Conclusion updated with current-sensor-bias focus.")
