"""Unit tests for the filter engine.

Run from the project root:

    pytest -q
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from filters import classify


# (title, expected_passes, expected_is_technical)
CASES: list[tuple[str, bool, bool]] = [
    # ---- Positive: should pass, technical ----
    ("Software Engineer Intern", True, True),
    ("Machine Learning Engineer, New Grad 2026", True, True),
    ("Data Scientist - Early Career", True, True),
    ("Quant Research Intern", True, True),
    ("Backend Software Engineer (University Graduate, 2027)", True, True),
    ("New Grad Software Engineer", True, True),
    ("Software Engineering Intern, Platform", True, True),
    ("Entry-Level Applied Scientist", True, True),
    ("AI Research Intern", True, True),
    ("Full-Stack Engineer, New Grad", True, True),
    ("Co-Op, Software Engineering", True, True),
    ("Coop Data Engineer", True, True),
    ("ML Engineer Intern (Summer 2026)", True, True),
    # ---- Positive: pass, but non-technical (no DOMAIN match) ----
    ("Marketing Intern", True, False),
    ("Recruiting Coordinator, Early Career", True, False),
    ("Campus Recruiting Specialist", True, False),
    # ---- Negative: senior / mgmt keywords ----
    ("Senior Software Engineer", False, False),
    ("Staff Machine Learning Engineer", False, False),
    ("Engineering Manager", False, False),
    ("Principal Quant Researcher", False, False),
    ("Director of Data Science", False, False),
    ("Head of AI", False, False),
    ("VP of Engineering", False, False),
    ("Vice President, Platform Engineering", False, False),
    ("Lead Software Engineer", False, False),
    ("Sr. Backend Engineer", False, False),
    # ---- Negative: no early-career signal ----
    ("Software Engineer", False, False),
    ("Machine Learning Engineer", False, False),
    ("Data Scientist", False, False),
    # ---- Tricky: senior wins over early-career (anti is strict) ----
    ("Senior Software Engineer, New Grad Team Lead", False, False),
    # ---- Empty / weird input ----
    ("", False, False),
]


@pytest.mark.parametrize("title,expected_passes,expected_tech", CASES)
def test_classify(title: str, expected_passes: bool, expected_tech: bool) -> None:
    passes, is_tech = classify(title)
    assert passes is expected_passes, f"passes mismatch for {title!r}"
    assert is_tech is expected_tech, f"is_technical mismatch for {title!r}"


def test_none_title_is_safe() -> None:
    passes, is_tech = classify(None)  # type: ignore[arg-type]
    assert passes is False
    assert is_tech is False
