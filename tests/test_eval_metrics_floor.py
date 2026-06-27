"""Ensure full-corpus eval metrics do not regress vs eval_baseline.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from classifier import classify_job_fields

EVAL = Path(__file__).resolve().parent.parent / "testing" / "eval"
BASELINE_PATH = EVAL / "eval_baseline.json"
FLOOR_DELTA = 0.005


def _load_baseline() -> dict:
    if not BASELINE_PATH.exists():
        pytest.skip(f"missing {BASELINE_PATH.name}")
    return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))


def test_eval_metrics_not_below_baseline() -> None:
    jobs_path = EVAL / "cursor_eval_jobs.jsonl"
    labels_path = EVAL / "cursor_eval_labels.jsonl"
    if not jobs_path.exists() or not labels_path.exists():
        pytest.skip("eval corpus not present")

    labels = {
        json.loads(line)["url"]: json.loads(line)
        for line in labels_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    tp = fp = fn = 0
    for line in jobs_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        job = json.loads(line)
        lab = labels.get(job["url"])
        if not lab:
            continue
        result = classify_job_fields(
            company=job.get("company", ""),
            title=job.get("title", ""),
            location=job.get("location"),
            url=job.get("url"),
            description=job.get("description"),
            us_only=True,
            # Baseline metrics measure raw classifier output; opt out of
            # the new scope toggles (intern drop, SWE-only narrowing).
            drop_interns=False,
            swe_only=False,
        )
        predicted = result.include
        expected = bool(lab["manual_include"])
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
