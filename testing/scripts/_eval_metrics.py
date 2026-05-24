"""Print per-ATS eval metrics and regex-positive precision."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1] / "eval"
REPORT = EVAL / "cursor_eval_report.json"


def main() -> None:
    jobs_path = EVAL / "cursor_eval_jobs.jsonl"
    labels_path = EVAL / "cursor_eval_labels.jsonl"
    if not jobs_path.exists():
        print(f"Missing {jobs_path.name}", file=sys.stderr)
        sys.exit(1)

    jobs = [
        json.loads(line)
        for line in jobs_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    labels = {
        json.loads(line)["url"]: json.loads(line)
        for line in labels_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    by_ats: dict[str, dict[str, int]] = defaultdict(lambda: {"tp": 0, "fp": 0, "tn": 0, "fn": 0})
    tp = fp = tn = fn = 0

    for j in jobs:
        label = labels.get(j["url"])
        if not label:
            continue
        a = j["ats"]
        r, m = j["regex_include"], bool(label["manual_include"])
        if m and r:
            by_ats[a]["tp"] += 1
            tp += 1
        elif not m and not r:
            by_ats[a]["tn"] += 1
            tn += 1
        elif not m and r:
            by_ats[a]["fp"] += 1
            fp += 1
        else:
            by_ats[a]["fn"] += 1
            fn += 1

    regex_pos = tp + fp
    prec_regex_pos = tp / regex_pos if regex_pos else 0
    prec = tp / (tp + fp) if (tp + fp) else 0
    rec = tp / (tp + fn) if (tp + fn) else 0

    print(f"Overall: TP={tp} FP={fp} TN={tn} FN={fn}")
    print(f"  precision={prec:.1%}  recall={rec:.1%}  precision_on_regex+={prec_regex_pos:.1%}")
    print()
    print(f"{'ATS':16} {'n':>5} {'TP':>4} {'FP':>3} {'FN':>3} {'Prec':>7} {'Recall':>7}")
    for a in sorted(by_ats):
        d = by_ats[a]
        ttp, tfp, ttn, tfn = d["tp"], d["fp"], d["tn"], d["fn"]
        tot = ttp + tfp + ttn + tfn
        p = ttp / (ttp + tfp) if (ttp + tfp) else 0
        r = ttp / (ttp + tfn) if (ttp + tfn) else 0
        print(f"{a:16} {tot:5} {ttp:4} {tfp:3} {tfn:3} {p:6.1%} {r:6.1%}")

    if REPORT.exists():
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        recs = report.get("recommendations") or []
        if recs:
            print("\nTop recommendations:")
            for rec in recs[:5]:
                key = rec.get("regex_reason") or rec.get("manual_reason")
                print(f"  - {rec['type']}: {key} ({rec['count']})")


if __name__ == "__main__":
    main()
