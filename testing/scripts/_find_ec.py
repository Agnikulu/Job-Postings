import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

jobs = json.load(open("_label_batch_5.json", encoding="utf-8"))
for i, j in enumerate(jobs):
    t = j["title"].lower()
    d = j["description"].lower()
    combined = t + " " + d[:3000]
    if re.search(
        r"new grad|internship|intern\b|2026 grad|expected graduation|campus|"
        r"university grad|entry.level|0-2|0 to 2|1-2 year|2\+ year|"
        r"2 \+ year|prior software engineering internship|graduation date",
        combined,
    ):
        if not re.search(
            r"senior|staff|principal|director|manager|head of|vp |postdoc|"
            r"group leader|account executive|sales executive|business development",
            t,
        ):
            print(f"{i}|{j['title'][:60]}")
