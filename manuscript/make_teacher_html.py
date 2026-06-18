from pathlib import Path
import markdown

md_path = Path("paper2_draft.md")
html_path = Path("paper2_draft_for_teacher.html")

md = md_path.read_text(encoding="utf-8")

lines = md.splitlines()
new_lines = []

for line in lines:
    stripped = line.strip()
    is_formula = (
        "\\frac" in stripped
        or "\\alpha" in stripped
        or "V_{RC}" in stripped
        or stripped.startswith("x_k =")
        or stripped.startswith("SOC(k+1)")
        or stripped.startswith("V(k) =")
        or stripped.startswith("e_")
        or stripped.startswith("r_")
    )

    if is_formula:
        new_lines.append("")
        new_lines.append("```text")
        new_lines.append(stripped)
        new_lines.append("```")
        new_lines.append("")
    else:
        new_lines.append(line)

md_safe = "\n".join(new_lines)

body = markdown.markdown(md_safe, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Paper2 Draft for Teacher Review</title>
<style>
body {{
    font-family: Arial, "Noto Sans CJK JP", "Hiragino Sans", "Yu Gothic", sans-serif;
    max-width: 900px;
    margin: 40px auto;
    padding: 0 20px;
    line-height: 1.65;
    font-size: 16px;
    color: #222;
}}
h1 {{
    font-size: 26px;
    line-height: 1.3;
    text-align: center;
    margin-bottom: 30px;
}}
h2 {{
    font-size: 22px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 6px;
    margin-top: 36px;
}}
h3 {{
    font-size: 18px;
    margin-top: 28px;
}}
p {{
    text-align: justify;
}}
img {{
    max-width: 100%;
    display: block;
    margin: 22px auto;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    font-size: 14px;
}}
th, td {{
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}}
th {{
    background: #f2f2f2;
}}
pre {{
    background: #f7f7f7;
    border: 1px solid #ddd;
    padding: 10px;
    overflow-x: auto;
    font-size: 14px;
}}
code {{
    font-family: Consolas, Monaco, monospace;
}}
@media print {{
    body {{
        max-width: none;
        margin: 20mm;
        font-size: 12pt;
    }}
    h1, h2, h3 {{
        page-break-after: avoid;
    }}
    img {{
        page-break-inside: avoid;
    }}
}}
</style>
</head>
<body>
{body}
</body>
</html>
"""

html_path.write_text(html, encoding="utf-8")
print("Created paper2_draft_for_teacher.html")
