"""Unit tests for education tagging and posted-date parsing."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from date_parser import parse_posted_date
from education import extract_education_levels


# =============================================================================
# Education tagging
# =============================================================================

EDUCATION_CASES = [
    # PhD
    ("PhD Data Scientist, Intern", ["PhD", "Intern"]),
    ("PhD Machine Learning Engineer, Intern", ["PhD", "Intern"]),
    ("PhD GenAI Research Scientist Intern", ["PhD", "Intern"]),
    ("Ph.D. Research Intern", ["PhD", "Intern"]),
    ("Doctoral Research Fellow", ["PhD"]),
    ("Postdoc Researcher", ["PhD"]),
    # Masters
    ("Master's Fall Machine Learning Internship", ["Masters", "Intern"]),
    ("MS Computer Science Intern", ["Masters", "Intern"]),
    ("M.S. Graduate Student Researcher", ["Masters"]),
    # Bachelors
    ("Undergraduate Software Engineer Intern", ["Bachelors", "Intern"]),
    ("Bachelor's Student Intern", ["Bachelors", "Intern"]),
    # New Grad (no degree level)
    ("New Grad Software Engineer", ["New Grad"]),
    ("Software Engineering New Grad (2026)", ["New Grad"]),
    ("Early Career Software Engineer", ["New Grad"]),
    ("Entry-Level Applied Scientist", ["New Grad"]),
    ("University Graduate - Machine Learning Engineer", ["New Grad"]),
    ("New College Grad - ASIC Engineer", ["New Grad"]),
    # Intern only
    ("Software Engineer Intern", ["Intern"]),
    ("Coop Data Engineer", ["Intern"]),
    ("Co-Op, Software Engineering", ["Intern"]),
    ("Internship - Search Backend Infra Engineer", ["Intern"]),
    # Combinations
    ("[2026] Data Scientist - PhD Early Career", ["PhD", "New Grad"]),
    ("Master's New Grad Software Engineer", ["Masters", "New Grad"]),
    # Empty / no match
    ("", []),
    ("Software Engineer", []),
    ("Senior Engineer", []),  # ANTI keyword still gets tagged by extract,
    # ... because the education tagger doesn't filter; the orchestrator
    # only invokes it on titles that already passed classify().
]


@pytest.mark.parametrize("title,expected", EDUCATION_CASES)
def test_extract_education_levels(title: str, expected: list[str]) -> None:
    assert extract_education_levels(title) == expected, (
        f"education tags mismatch for {title!r}"
    )


def test_education_handles_none() -> None:
    assert extract_education_levels(None) == []


# =============================================================================
# Posted-date parsing
# =============================================================================

# Use a fixed reference date so Workday relative-date tests are deterministic.
REF = datetime(2026, 5, 21, 12, 0, 0, tzinfo=timezone.utc)


def test_greenhouse_iso() -> None:
    assert parse_posted_date(
        "2026-05-19T14:32:00Z", "greenhouse"
    ) == "2026-05-19"


def test_ashby_iso_with_zulu() -> None:
    assert parse_posted_date(
        "2026-05-15T10:00:00.000Z", "ashby"
    ) == "2026-05-15"


def test_greenhouse_iso_with_offset() -> None:
    assert parse_posted_date(
        "2026-05-20T22:00:00-04:00", "greenhouse"
    ) == "2026-05-20"


def test_lever_epoch_ms() -> None:
    # 1747257600000 = 2025-05-14 21:00:00 UTC
    assert parse_posted_date(1747257600000, "lever") == "2025-05-14"


def test_lever_epoch_ms_as_string() -> None:
    assert parse_posted_date("1747257600000", "lever") == "2025-05-14"


@pytest.mark.parametrize("text,expected_offset_days", [
    ("Posted Today", 0),
    ("Posted Yesterday", 1),
    ("Posted 1 Day Ago", 1),
    ("Posted 3 Days Ago", 3),
    ("Posted 30+ Days Ago", 30),
])
def test_workday_relative(text: str, expected_offset_days: int) -> None:
    expected_date = (REF.date()
                     - __import__("datetime").timedelta(days=expected_offset_days))
    assert parse_posted_date(text, "workday", ref=REF) == expected_date.isoformat()


def test_workday_weeks_ago() -> None:
    out = parse_posted_date("Posted 2 Weeks Ago", "workday", ref=REF)
    assert out == "2026-05-07"


def test_workday_months_ago() -> None:
    out = parse_posted_date("Posted 1 Month Ago", "workday", ref=REF)
    # 30-day approximation -> 2026-04-21
    assert out == "2026-04-21"


def test_workday_unparseable() -> None:
    assert parse_posted_date("recently posted", "workday", ref=REF) is None


def test_none_returns_none() -> None:
    assert parse_posted_date(None, "greenhouse") is None
    assert parse_posted_date("", "lever") is None


def test_unknown_ats_falls_through() -> None:
    # Unknown ATS still tries ISO parsing
    assert parse_posted_date("2026-05-20", "smartrecruiters") == "2026-05-20"
