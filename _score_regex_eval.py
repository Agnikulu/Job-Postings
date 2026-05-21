"""Apply manual ground truth and compute regex precision/accuracy."""

from __future__ import annotations

import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from classifier import classify_job_fields

GROUND_TRUTH: dict[int, bool] = {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False,
    16: False,
    17: False,
    18: False,
    19: False,
    20: False,
    21: False,
    22: True,
    23: False,
    24: False,
    25: False,
    26: False,
    27: False,
    28: False,
    29: False,
    30: False,
    31: False,
    32: False,
    33: False,
    34: False,
    35: True,
    36: False,
    37: False,
    38: False,
    39: False,
    40: False,
    41: True,
    42: False,
    43: False,
    44: False,
    45: True,
    46: False,
    47: False,
    48: False,
    49: False,
    50: False,
    51: False,
    52: False,
    53: False,
    54: False,
    55: False,
    56: False,
    57: False,
}

rows = json.load(open("_regex_eval_sample.json", encoding="utf-8"))

tp = fp = tn = fn = 0
errors: list[dict] = []
by_source: dict[str, dict[str, int]] = {}

for i, r in enumerate(rows):
    if i not in GROUND_TRUTH:
        continue
    truth = GROUND_TRUTH[i]
    desc = r.get("description") or r.get("description_head") or ""
    result = classify_job_fields(
        company=r["company"],
        title=r["title"],
        location=r.get("location"),
        description=desc,
        us_only=False,
    )
    pred = result.include
    src = r["company"]
    by_source.setdefault(src, {"tp": 0, "fp": 0, "tn": 0, "fn": 0})
    if truth and pred:
        tp += 1
        by_source[src]["tp"] += 1
    elif truth and not pred:
        fn += 1
        by_source[src]["fn"] += 1
        errors.append({"idx": i, "type": "FN", "reason": result.reason, **r})
    elif not truth and pred:
        fp += 1
        by_source[src]["fp"] += 1
        errors.append({"idx": i, "type": "FP", "reason": result.reason, **r})
    else:
        tn += 1
        by_source[src]["tn"] += 1

total = tp + fp + tn + fn
accuracy = (tp + tn) / total if total else 0
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

print("=" * 72)
print("REGEX CLASSIFIER EVAL (manual ground truth, n=58)")
print("=" * 72)
print(f"Accuracy:  {accuracy:.1%}  ({tp + tn}/{total})")
print(f"Precision: {precision:.1%}  ({tp}/{tp + fp} includes correct)")
print(f"Recall:    {recall:.1%}  ({tp}/{tp + fn} EC targets caught)")
print(f"F1:        {f1:.2f}")
print()
print(f"Confusion: TP={tp} FP={fp} TN={tn} FN={fn}")
print()
print("Per source:")
for src, c in sorted(by_source.items()):
    s_tp, s_fp, s_tn, s_fn = c["tp"], c["fp"], c["tn"], c["fn"]
    s_total = s_tp + s_fp + s_tn + s_fn
    s_prec = s_tp / (s_tp + s_fp) if (s_tp + s_fp) else float("nan")
    s_acc = (s_tp + s_tn) / s_total if s_total else 0
    print(f"  {src:12} acc={s_acc:.0%} prec={s_prec:.0%}  TP={s_tp} FP={s_fp} TN={s_tn} FN={s_fn}")

print()
print("FALSE POSITIVES:")
for e in errors:
    if e["type"] != "FP":
        continue
    print(f"  [{e['idx']}] {e['company']}: {e['title'][:70]}")
    print(f"       {e['reason']}")

print()
print("FALSE NEGATIVES:")
for e in errors:
    if e["type"] != "FN":
        continue
    print(f"  [{e['idx']}] {e['company']}: {e['title'][:70]}")
    print(f"       {e['reason']}")
