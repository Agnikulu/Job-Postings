import json
with open("testing/eval/cursor_eval_report.json") as f:
    data = json.load(f)
disag = data.get("disagreements", [])
fns = [j for j in disag if j.get("bucket") == "fn"]
fps = [j for j in disag if j.get("bucket") == "fp"]
print(f"FN count: {len(fns)}")
for j in fns:
    print(f"  [{j.get('company','')}] {j.get('title','')[:80]!r}  regex_reason={j.get('regex_reason','')!r}")
print()
print(f"FP count: {len(fps)}")
for j in fps:
    print(f"  [{j.get('company','')}] {j.get('title','')[:80]!r}  regex_reason={j.get('regex_reason','')!r}")
