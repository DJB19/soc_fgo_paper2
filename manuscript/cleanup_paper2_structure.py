from pathlib import Path

path = Path("manuscript/paper2_draft.md")
text = path.read_text(encoding="utf-8")

# 1. Clean duplicated section headings
text = text.replace("## 4 Experimental Design\n### 4. Experimental Setup\n", "## 4 Experimental Design\n\n")
text = text.replace("## 5 Results and Discussion\n### 5. Results and Discussion\n", "## 5 Results and Discussion\n\n")

# 2. Remove standalone Figure headings that should not be section titles
text = text.replace("### Figure 1\npaper2_bias_rmse.png\n\n", "")
text = text.replace("### Figure 2\npaper2_bias100_soc_comparison.png\n\n", "")

# 3. Rename NASA section to a cleaner subsection title
text = text.replace(
    "## 5.4 Validation Using NASA B0005 Battery Aging Dataset",
    "### 5.2 NASA B0005 Validation under Current Sensor Bias"
)

# 4. Rename Section 5 opening subsection if present
text = text.replace(
    "### 5. Results and Discussion",
    "### 5.1 Simulation Results under Current Sensor Bias"
)

# 5. If there is no 5.1 title after Section 5, insert one before the first results paragraph
old = "## 5 Results and Discussion\n\nThe estimation performance"
new = "## 5 Results and Discussion\n\n### 5.1 Simulation Results under Current Sensor Bias\n\nThe estimation performance"
text = text.replace(old, new)

# 6. Remove duplicate NASA RMSE figure if it appears twice
target = "![Figure X. NASA B0005 validation: RMSE comparison between Coulomb Counting and nonlinear FGO under different current sensor bias levels.](figures/nasa_B0005_fgo_vs_cc_rmse.png)"
first = text.find(target)
if first != -1:
    second = text.find(target, first + len(target))
    if second != -1:
        text = text[:second] + text[second + len(target):]

path.write_text(text, encoding="utf-8")
print("Paper2 structure cleaned.")
