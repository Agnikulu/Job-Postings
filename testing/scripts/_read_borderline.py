import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("_label_batch_2.json", encoding="utf-8") as f:
    jobs = json.load(f)
for i in [558, 618, 646, 649, 655, 658, 630]:
    j = jobs[i]
    d = j.get("description") or ""
    print("=" * 60)
    print(i, j["title"])
    for kw in ["Requirements", "Qualifications", "About you", "Who you are", "What you"]:
        idx = d.find(kw)
        if idx >= 0:
            print(d[idx:idx+1200])
            break
    else:
        print(d[:1200])
