import json
with open("_label_batch_2.json", encoding="utf-8") as f:
    jobs = json.load(f)
for i in range(588, 659):
    j = jobs[i]
    print(f"{i}|{j['title'][:70]}")
print("TOTAL", len(jobs))
