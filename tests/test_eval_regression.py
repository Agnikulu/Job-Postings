"""Regression tests for regex classifier against frozen eval gold cases."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from classifier import classify_job_fields

GOLD_PATH = Path(__file__).resolve().parent.parent / "testing" / "eval" / "eval_gold.jsonl"


def _load_gold() -> list[dict]:
    if not GOLD_PATH.exists():
        pytest.skip(f"missing {GOLD_PATH.name}")
    rows: list[dict] = []
    for line in GOLD_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


@pytest.mark.parametrize("case", _load_gold(), ids=lambda c: c.get("kind", c.get("url", "?"))[-40:])
def test_gold_regex_matches_expectation(case: dict) -> None:
    # Eval baseline was frozen with the raw classifier — disable the
    # new scope toggles (intern drop, SWE-only) so this regression test
    # keeps measuring classifier quality, not scope filtering.
    result = classify_job_fields(
        company=case.get("company", ""),
        title=case.get("title", ""),
        location=case.get("location"),
        url=case.get("url"),
        description=case.get("description"),
        us_only=False,
        drop_interns=False,
        swe_only=False,
    )
    expected = bool(case["expected_include"])
    if result.include == expected:
        return
    if case.get("xfail"):
        pytest.xfail(
            f"known gap: got include={result.include} ({result.reason}), "
            f"target={expected} — {case.get('reason')}"
        )
    pytest.fail(
        f"{case.get('title')}: expected include={expected}, got {result.include} "
        f"({result.reason}) — {case.get('reason')}"
    )
