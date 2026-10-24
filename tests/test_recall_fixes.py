"""Regression tests for the 2026-10-24 recall-first audit.

Each case is a real posting shape from the live audit of all active
companies: either a genuine new-grad role the filters dropped, or a
false positive that was cheap to fix without risking recall.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from adapters.greenhouse import _location as greenhouse_location
from adapters.jibe import _format_location as jibe_location
from classifier import classify_job_fields
from filters import (
    classify_title_confidence,
    description_invites_early_career,
    is_software_or_ai_role,
    is_us_location_with_description,
)


def _include(title: str, description: str | None = None, location: str = "San Francisco, CA") -> bool:
    return classify_job_fields(
        company="Acme", title=title, location=location, description=description
    ).include


@pytest.mark.parametrize(
    "title",
    [
        "Master's University Grad Data Scientist (USA)",
        "PhD University Grad Machine Learning Engineer (USA)",
        "Machine Learning Engineer - College Graduate",
        "Network Production Engineer (University Grad)",
        "Quantitative Sports Researcher – Graduate Hire",
        "AI Research Engineer, New PhD Graduate",
        "Entry Level & Senior Software Engineer, AI Software Platform (Onsite)",
        "[Junior / Senior / Staff] Software Engineer, Inference / Compute Infrastructure",
    ],
)
def test_new_grad_titles_included(title: str) -> None:
    assert _include(title), title


@pytest.mark.parametrize(
    "title",
    ["Back End Engineer 1", "Site Reliability Engineer Graduate: 2027", "Production Engineer, University Grad"],
)
def test_software_titles_pass_swe_only(title: str) -> None:
    assert is_software_or_ai_role(title), title


@pytest.mark.parametrize(
    "title",
    [
        "Senior Software Engineer, New Grad Team Lead",
        "Distinguished Engineer - Distinguished Engineer, Data Foundation",
        "Experienced/Lateral - Quantitative Researcher",
    ],
)
def test_senior_titles_excluded(title: str) -> None:
    assert not _include(title, "Requirements: Bachelor's degree in Computer Science."), title


def test_senior_fellow_rank_excluded() -> None:
    desc = "We are looking for a Fellow to lead GPU libraries. Requirements: 15+ years of experience."
    conf = classify_title_confidence("Fellow ROCm GPU Libraries", desc)
    assert conf.level == "high_exclude"
    assert conf.reason == "senior fellow rank"


@pytest.mark.parametrize(
    "requirements",
    [
        "prior work as a Distinguished Engineer, Fellow, Principal Architect, or equivalent",
        "1 year of experience in mentorship and leadership of junior software engineers",
        "experience expanding from a single department to a campus or system",
        "Must be a U.S. citizen or lawful permanent resident",
    ],
)
def test_requirements_keywords_about_others_are_not_ec(requirements: str) -> None:
    desc = f"About the role. Requirements: {requirements}. Strong Python skills."
    conf = classify_title_confidence("Software Engineer, Platform", desc)
    assert conf.reason not in {"explicit ec technical", "explicit ec technical (requirements)"}


@pytest.mark.parametrize(
    "body",
    [
        "We are looking for highly motivated new college graduates and experienced Design Verification Engineers.",
        "Recent College graduates may apply.",
        "Current university student graduating between September 2026 – July 2027.",
        "BS in CS/CE/EE and 0-2+ years of software engineer career experience.",
        "Entry-Level Quantitative Researchers are responsible for rigorous research.",
        "We welcome early-career engineers with exceptional technical depth.",
        "We are open to all levels from new grads to senior engineers.",
        "Career length is only a guideline. - Early Career - $160,000 - $275,000 + equity",
    ],
)
def test_description_invites(body: str) -> None:
    assert description_invites_early_career(body)


@pytest.mark.parametrize(
    "body",
    [
        "This is NOT a New/Recent College Grad-level position.",
        "If you are a current student or recent graduate, please take a look at our Entry Level and Intern positions.",
        "It is not intended for internship, new graduate, or entry-level applicants.",
        "Mentor early-career engineers to help them grow.",
        "Note: if you are an intern, new grad, or staff applicant, please do not apply using this link.",
    ],
)
def test_description_negations(body: str) -> None:
    assert not description_invites_early_career(body)


def test_description_rescue_includes_open_level_title() -> None:
    desc = (
        "About the role: build our cloud network. We welcome early-career engineers with "
        "exceptional technical depth. Requirements: strong C++ and networking fundamentals."
    )
    assert _include("Software Engineer, Infrastructure Services", desc)


@pytest.mark.parametrize(
    "location,expected",
    [
        ("Cambridge, UK", False),
        ("GB,Cambridge", False),
        ("United Kingdom - Cambridge", False),
        ("Cambridge", True),
        ("Cambridge, MA", True),
        ("Gurugram, IN", False),
        ("Haifa, IL", False),
        ("Chicago, IL", True),
        ("SF, SEA, NYC, CHI, ATL", True),
        ("Billerica (MA)", True),
        ("Bay Area", True),
    ],
)
def test_location_strings(location: str, expected: bool) -> None:
    assert is_us_location_with_description(location, None) is expected


@pytest.mark.parametrize(
    "body,expected",
    [
        ("We are a fully remote team. Come join us.", False),
        ("This role is remote within Germany. Tell us a bit about yourself.", False),
        ("Remote (US only). Join us!", True),
        ("Fully remote across the U.S.", True),
    ],
)
def test_remote_description_ignores_pronoun_us(body: str, expected: bool) -> None:
    assert is_us_location_with_description("Remote", body) is expected


def test_jibe_location_prefers_place_over_label() -> None:
    sig = {"location_name": "SIG", "full_location": "New York, New York", "country": "United States"}
    assert jibe_location(sig) == "New York, New York, United States"
    amd = {"location_name": "US,TX,Austin", "full_location": "Austin, Texas", "country": "United States"}
    assert jibe_location(amd) == "US,TX,Austin"


def test_greenhouse_location_uses_custom_field_for_work_mode() -> None:
    raw = {
        "location": {"name": "Hybrid"},
        "metadata": [
            {"name": "Cost Center", "value": "4700 - Security"},
            {"name": "Job Posting Location", "value": ["Austin, US", "New York, US"]},
        ],
    }
    assert greenhouse_location(raw) == "Austin, US; New York, US"
    assert greenhouse_location({"location": {"name": "San Francisco, CA"}}) == "San Francisco, CA"
