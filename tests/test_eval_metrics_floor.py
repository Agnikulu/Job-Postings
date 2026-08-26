"""Ensure classifier precision/recall on the hand-labeled gold set do not
regress vs eval_baseline.json.

See testing/eval/RUBRIC.md and testing/README.md for how eval_gold.jsonl is
produced (independently hand-labeled, not derived from filters.py) and
eval_baseline.json's `note` field for why recall on this set is a
regression-only signal, not a true production recall estimate - the gold
set is stratified toward regex-positive and known-hard-exclude categories,
not randomly sampled.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from classifier import classify_job_fields

EVAL = Path(__file__).resolve().parent.parent / "testing" / "eval"
GOLD_PATH = EVAL / "eval_gold.jsonl"
BASELINE_PATH = EVAL / "eval_baseline.json"

# Gold set is ~226 rows, not ~25k - a single case flipping moves precision/
# recall by a few points, so the regression floor needs more slack than the
# old 0.005 delta (tuned for a much larger corpus).
FLOOR_DELTA = 0.03


def _load_baseline() -> dict:
    if not BASELINE_PATH.exists():
        pytest.skip(f"missing {BASELINE_PATH.name}")
    return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))


def test_eval_metrics_not_below_baseline() -> None:
    if not GOLD_PATH.exists():
        pytest.skip("eval gold set not present")

    tp = fp = fn = 0
    for line in GOLD_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        job = json.loads(line)
        result = classify_job_fields(
            company=job.get("company", ""),
            title=job.get("title", ""),
            location=job.get("location"),
            url=job.get("url"),
            description=job.get("description"),
            us_only=False,
            # Baseline metrics measure raw classifier output; opt out of
            # the scope toggles (intern drop, SWE-only narrowing).
            drop_interns=False,
            swe_only=False,
        )
        predicted = result.include
        expected = bool(job["expected_include"])
        if predicted and expected:
            tp += 1
        elif predicted and not expected:
            fp += 1
        elif not predicted and expected:
            fn += 1

    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    base = _load_baseline()
    assert prec >= base["precision"] - FLOOR_DELTA, (
        f"precision {prec:.3f} < baseline {base['precision']:.3f}"
    )
    assert rec >= base["recall"] - FLOOR_DELTA, (
        f"recall {rec:.3f} < baseline {base['recall']:.3f}"
    )
