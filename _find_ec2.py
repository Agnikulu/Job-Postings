import json
import re

jobs = json.load(open("_label_batch_5.json", encoding="utf-8"))
patterns = [
    r"new grad",
    r"new college grad",
    r"university grad",
    r"expected graduation",
    r"graduat(?:e|ion) date of summer 2026",
    r"fall 2025 and summer 2026",
    r"\b0-2\b",
    r"0 to 2 year",
    r"1-2 year",
    r"2\+ years of professional software",
    r"internship.*(?:software|engineer|ml|data)",
    r"software engineering intern",
    r"engineering intern",
    r"campus hire",
    r"entry.level software",
]
for i, j in enumerate(jobs):
    t = j["title"].lower()
    d = j.get("description", "").lower()
    combined = t + " " + d
    if any(re.search(p, combined) for p in patterns):
        senior = re.search(
            r"senior|staff|principal|director|manager|head of|vp |postdoc|group leader",
            t,
        )
        print(f"{i}|{'SEN' if senior else 'OK'}|{j['title'][:55]}")
