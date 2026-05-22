import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

data = json.load(open("_label_batch_5.json", encoding="utf-8"))
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(data)
for i, j in enumerate(data[start:end], start):
    desc = (j.get("description") or "")[:800].replace("\n", " ")
    print(f"=== {i} ===")
    print(f"TITLE: {j['title']}")
    print(f"LOC: {j.get('location', '')}")
    print(f"URL: {j['url']}")
    print(f"DESC: {desc}")
    print()
