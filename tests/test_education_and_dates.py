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
    ("PhD Data Scientist, Intern", None, ["PhD", "Intern"]),
    ("PhD Machine Learning Engineer, Intern", None, ["PhD", "Intern"]),
    ("Ph.D. Research Intern", None, ["PhD", "Intern"]),
    # Masters / Bachelors students
    (
        "MS Computer Science Intern",
        "Currently pursuing a master's degree in CS.",
        ["MS Student", "Intern"],
    ),
    (
        "Undergraduate Software Engineer Intern",
        "You are an undergraduate student in computer science.",
        ["BS Student", "Intern"],
    ),
    # New Grad
    ("New Grad Software Engineer", None, ["New Grad"]),
    ("Software Engineering New Grad (2026)", None, ["New Grad"]),
    ("University Graduate - Machine Learning Engineer", None, ["New Grad"]),
    ("New College Grad - ASIC Engineer", None, ["New Grad"]),
    (
        "Field Application Engineer - New College Graduate 2026",
        None,
        ["New Grad"],
    ),
    (
        "Associate Software Engineer - Seeking 2025 & 2026 Grads",
        None,
        ["New Grad"],
    ),
    ("Machine Learning Engineer I", None, ["Early Career"]),
    ("Graduate 2026 PhD Software Engineer II", None, []),
    # Intern only
    ("Software Engineer Intern", None, ["Intern"]),
    ("Co-Op, Software Engineering", None, ["Intern"]),
    # Requirements-first
    (
        "Software Engineer",
        "Minimum qualifications: Bachelor's degree required. New grad hiring for 2026.",
        ["Bachelors", "New Grad"],
    ),
    (
        "Research Intern",
        "PhD candidates welcome. Pursuing a doctoral degree.",
        ["PhD Student", "Intern"],
    ),
    # Experienced ladder — no tags
    ("Software Engineer II", "Bachelor's degree required.", []),
    ("", None, []),
    ("Senior Engineer", None, []),
]


@pytest.mark.parametrize("title,requirements,expected", EDUCATION_CASES)
def test_extract_education_levels(
    title: str,
    requirements: str | None,
    expected: list[str],
) -> None:
    assert (
        extract_education_levels(title, requirements_text=requirements) == expected
    ), f"education tags mismatch for {title!r}"


def test_education_handles_none() -> None:
    assert extract_education_levels(None) == []


def test_entry_level_title_only_not_new_grad_from_body() -> None:
    tags = extract_education_levels(
        "Applied Scientist",
        requirements_text="This is an entry-level role with 5+ years of experience.",
    )
    assert "New Grad" not in tags


def test_residency_program_not_tagged_intern() -> None:
    tags = extract_education_levels(
        "Network Operations Residency Program, University Graduate, August 2026 Start",
        requirements_text="Looking for recent university graduates.",
    )
    assert "Intern" not in tags
    assert "New Grad" in tags


def test_year_in_title_alone_not_new_grad() -> None:
    tags = extract_education_levels(
        "Software Engineer, 2026",
        requirements_text=None,
    )
    assert "New Grad" not in tags


def test_intern_from_req_mention_not_tagged() -> None:
    tags = extract_education_levels(
        "University Graduate - Software Engineer",
        requirements_text="Prior internship experience is a plus.",
    )
    assert "Intern" not in tags
    assert "New Grad" in tags


# =============================================================================
# Posted-date parsing
# =============================================================================

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
    assert out == "2026-04-21"


def test_workday_unparseable() -> None:
    assert parse_posted_date("recently posted", "workday", ref=REF) is None


def test_none_returns_none() -> None:
    assert parse_posted_date(None, "greenhouse") is None
    assert parse_posted_date("", "lever") is None


def test_unknown_ats_falls_through() -> None:
    assert parse_posted_date("2026-05-20", "smartrecruiters") == "2026-05-20"


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2 days ago", "2026-05-19"),
        ("1 week ago", "2026-05-14"),
        ("Yesterday", "2026-05-20"),
        ("Just now", "2026-05-21"),
        ("May 24, 2026", "2026-05-24"),
    ],
)
def test_linkedin_relative_and_absolute(text: str, expected: str) -> None:
    assert parse_posted_date(text, "linkedin", ref=REF) == expected


def test_linkedin_unparseable_returns_none() -> None:
    assert parse_posted_date("Recently", "linkedin", ref=REF) is None
