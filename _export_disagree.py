import json
from pathlib import Path

ROOT = Path(__file__).parent
jobs = [json.loads(l) for l in (ROOT / "cursor_eval_jobs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
labels = [json.loads(l) for l in (ROOT / "cursor_eval_labels.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

reg_only = [(j, l) for j, l in zip(jobs, labels) if j.get("regex_include") and not l["manual_include"]]
man_only = [(j, l) for j, l in zip(jobs, labels) if l["manual_include"] and not j.get("regex_include")]

for name, pairs in [("regex_only", reg_only), ("manual_only", man_only)]:
    lines = []
    for i, (j, l) in enumerate(pairs):
        desc = (j.get("description") or "")[:1200]
        lines.append(
            f"=== {i} ===\n"
            f"TITLE: {j['title']}\n"
            f"LOC: {j.get('location', '')}\n"
            f"URL: {j['url']}\n"
            f"REGEX: {j.get('regex_reason')}\n"
            f"MANUAL: {l['manual_reason']}\n"
            f"DESC: {desc}\n"
        )
    (ROOT / f"_disagree_{name}.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"{name}: {len(pairs)}")
