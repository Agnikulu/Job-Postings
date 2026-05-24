"""Patch README_TECH company table from company_portal_links.py output."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
readme = (ROOT / "README_TECH.md").read_text(encoding="utf-8")
table = (ROOT / "testing" / "scripts" / "_company_table.txt").read_text(encoding="utf-8-sig").strip()

start_marker = "### Active companies ("
end_marker = "---\n\n## Project layout"

start = readme.index(start_marker)
end = readme.index(end_marker, start)

# Preserve heading with updated count
active_line = next(l for l in table.splitlines() if l.startswith("<!-- "))
active_count = active_line.split()[1]
new_section = f"### Active companies ({active_count})\n\n{table}\n\n"

readme = readme[:start] + new_section + readme[end:]
(ROOT / "README_TECH.md").write_text(readme, encoding="utf-8")
print(f"Patched README_TECH.md ({active_count} active companies)")
