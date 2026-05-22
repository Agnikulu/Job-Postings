import json
import re

jobs = json.load(open("_label_batch_5.json", encoding="utf-8"))
indices = [475, 479, 586, 595, 558, 550, 535, 448, 478, 9, 40]
with open("_quals2.txt", "w", encoding="utf-8") as f:
    for i in indices:
        j = jobs[i]
        d = j["description"]
        yrs = re.findall(r".{0,50}\d+\+?\s*years?.{0,50}", d, re.I)
        f.write(f"IDX {i}: {j['title']}\n")
        f.write("Years context:\n")
        for y in yrs[:10]:
            f.write("  " + y.strip() + "\n")
        idx = d.lower().find("qualification")
        if idx < 0:
            idx = d.lower().find("what we look")
        if idx < 0:
            idx = d.lower().find("requirements")
        f.write("QUAL SECTION:\n" + d[idx : idx + 1800] + "\n\n")
