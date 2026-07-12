from pathlib import Path

path = Path("manuscript/paper2_draft.md")
text = path.read_text(encoding="utf-8")

# Replace Table X with Table 2 for NASA validation
text = text.replace("Table X", "Table 2")

# Replace simulation figure captions
text = text.replace(
    "![Figure X. Simulation results: RMSE comparison under different current sensor bias levels.](figures/paper2_bias_rmse.png)",
    "![Figure 1. RMSE comparison under different current sensor bias levels.](figures/paper2_bias_rmse.png)"
)

text = text.replace(
    "![Figure X. Simulation results: SOC estimation comparison under 10% current sensor bias.](figures/paper2_bias100_soc_comparison.png)",
    "![Figure 2. SOC estimation trajectories under 10% current sensor bias.](figures/paper2_bias100_soc_comparison.png)"
)

# Replace NASA figure captions
text = text.replace(
    "![Figure X. NASA B0005 validation: SOC estimation comparison under 10% current sensor bias.](figures/nasa_B0005_fgo_soc_10bias.png)",
    "![Figure 3. NASA B0005 SOC estimation comparison under 10% current sensor bias.](figures/nasa_B0005_fgo_soc_10bias.png)"
)

text = text.replace(
    "![Figure X. NASA B0005 validation: RMSE comparison between Coulomb Counting and nonlinear FGO under different current sensor bias levels.](figures/nasa_B0005_fgo_vs_cc_rmse.png)",
    "![Figure 4. NASA B0005 RMSE comparison between Coulomb Counting and nonlinear FGO under different current sensor bias levels.](figures/nasa_B0005_fgo_vs_cc_rmse.png)"
)

# Remove duplicated bold figure title lines before image links
text = text.replace("**Figure 1. RMSE comparison under different current sensor bias levels.**\n\n", "")
text = text.replace("**Figure 2. SOC estimation trajectories under 10% current sensor bias.**\n\n", "")

# Remove duplicate NASA SOC figure if it appears twice
target = "![Figure 3. NASA B0005 SOC estimation comparison under 10% current sensor bias.](figures/nasa_B0005_fgo_soc_10bias.png)"
first = text.find(target)
if first != -1:
    second = text.find(target, first + len(target))
    if second != -1:
        text = text[:second] + text[second + len(target):]

# Remove duplicate NASA RMSE figure if it appears twice
target = "![Figure 4. NASA B0005 RMSE comparison between Coulomb Counting and nonlinear FGO under different current sensor bias levels.](figures/nasa_B0005_fgo_vs_cc_rmse.png)"
first = text.find(target)
if first != -1:
    second = text.find(target, first + len(target))
    if second != -1:
        text = text[:second] + text[second + len(target):]

path.write_text(text, encoding="utf-8")
print("Figure and table captions cleaned.")
