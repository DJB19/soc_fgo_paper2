from pathlib import Path

path = Path("paper2_draft.md")
text = path.read_text()

nasa_marker = "## 5.4 Validation Using NASA B0005 Battery Aging Dataset"
conclusion_marker = "## 6 Conclusion"
references_marker = "## References"

if nasa_marker not in text:
    raise SystemExit("NASA section marker not found")
if conclusion_marker not in text:
    raise SystemExit("Conclusion marker not found")

nasa_start = text.index(nasa_marker)

# NASA section is currently at the end after References.
nasa_section = text[nasa_start:].strip() + "\n"

# Remove NASA section from original location
text_without_nasa = text[:nasa_start].rstrip() + "\n\n"

# Insert NASA section before Conclusion
conclusion_start = text_without_nasa.index(conclusion_marker)

new_text = (
    text_without_nasa[:conclusion_start].rstrip()
    + "\n\n"
    + nasa_section
    + "\n"
    + text_without_nasa[conclusion_start:].lstrip()
)

path.write_text(new_text)

print("Reordered NASA section before Conclusion.")
