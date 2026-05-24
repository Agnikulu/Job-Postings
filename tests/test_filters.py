"""Unit tests for the filter engine.

Run from the project root:

    pytest -q
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from filters import (
    classify,
    classify_title_confidence,
    diagnose_weak_signal,
    is_location_ambiguous,
    is_obvious_reject,
    is_us_location,
    obvious_reject_reason,
)


# =============================================================================
# Title classification
# =============================================================================

# (title, expected_passes, expected_is_technical)
TITLE_CASES: list[tuple[str, bool, bool]] = [
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
    # ---- DOMAIN expansion: hardware / firmware / chip ----
    ("Firmware Engineer Intern", True, True),
    ("Hardware Systems Intern, Fall 2026", True, True),
    ("Embedded Software Intern (2026)", True, True),
    ("Chip Simulation Software Intern - Fall 2026", True, True),
    ("ASIC Design Engineer - New College Grad 2026", True, True),
    ("FPGA Engineer - 2026 Intern", True, True),
    ("RTL Intern, Spring 2027", True, True),
    ("DFT Verification Intern - Fall 2026", True, True),
    ("Inference Optimization Intern (2026)", True, True),
    ("CUDA Kernel Engineer, New Grad", True, True),
    ("GPU Architecture Intern - 2026", True, True),
    ("Compiler Engineer, Early Career", True, True),
    ("Silicon Validation Intern", True, True),
    ("VLSI Physical Design Intern (2026)", True, True),
    ("Software Engineer II", False, True),
    ("Software Engineer III, Full Stack", False, True),
    ("Junior Backend Engineer", True, True),
    # ---- Negative: non-tech early career ----
    ("Marketing Intern", False, False),
    ("Recruiting Coordinator, Early Career", False, False),
    ("Campus Recruiting Specialist", False, False),
    ("Talent Intern - Fall 2026", False, False),
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
    # ---- Bare titles without EC signals: exclude ----
    ("Software Engineer", False, True),
    ("Machine Learning Engineer", False, True),
    ("Data Scientist", False, True),
    ("Member of Technical Staff", False, True),
    # ---- Tricky: senior wins over early-career (anti is strict) ----
    ("Senior Software Engineer, New Grad Team Lead", False, False),
    # ---- Empty / weird input ----
    ("", False, False),
]


@pytest.mark.parametrize("title,expected_passes,expected_tech", TITLE_CASES)
def test_classify(title: str, expected_passes: bool, expected_tech: bool) -> None:
    passes, is_tech = classify(title)
    assert passes is expected_passes, f"passes mismatch for {title!r}"
    assert is_tech is expected_tech, f"is_technical mismatch for {title!r}"


def test_none_title_is_safe() -> None:
    passes, is_tech = classify(None)  # type: ignore[arg-type]
    assert passes is False
    assert is_tech is False


# =============================================================================
# Weak-signal diagnostics
# =============================================================================

@pytest.mark.parametrize("title,expected_signal", [
    ("Software Engineer I", "engineer i"),
    ("Software Engineer 1", "engineer 1"),
    ("Software Engineer II", None),
    ("Member of Technical Staff", "member of technical staff"),
    ("AI Resident", "resident"),
    ("Engineering Residency Program", "residency"),
    ("Associate Software Developer", "associate"),
    ("Junior Backend Engineer", "junior"),
    ("Trainee Engineer", "trainee"),
    # Negatives — main TARGET would already catch these
    ("Software Engineer Intern", None),
    ("New Grad Engineer", None),
    # Negatives — pure senior / no signal
    ("Senior Software Engineer", None),  # ANTI guard
])
def test_diagnose_weak_signal(title: str, expected_signal: str | None) -> None:
    result = diagnose_weak_signal(title)
    if expected_signal is None:
        assert result is None, f"expected None, got {result!r} for {title!r}"
    else:
        assert result == expected_signal, (
            f"expected {expected_signal!r}, got {result!r} for {title!r}"
        )


# =============================================================================
# US location filter
# =============================================================================

US_CASES = [
    # ---- Clear US ----
    ("San Francisco, CA", True),
    ("New York, NY", True),
    ("San Mateo, CA, United States", True),
    ("US, CA, Santa Clara", True),
    ("Remote - United States", True),
    ("United States - Remote", True),
    ("Remote, US", True),
    ("Remote Opportunity - United States; Salt Lake City, Utah", True),
    ("Costa Mesa, California, United States", True),
    ("Boston", True),
    ("Seattle, WA", True),
    ("San Jose, CA", True),
    ("Sunnyvale", True),
    ("Cambridge", True),
    ("Bellevue", True),
    ("Mountain View, CA", True),
    ("Hillsboro", True),
    ("Salt Lake City, Utah", True),
    # ---- Mixed (US + non-US): keep ----
    ("San Francisco, CA; Toronto, Ontario, Canada", True),
    ("New York, NY, US; London, UK", True),
    # ---- Clear non-US ----
    ("Toronto, Ontario, Canada", False),
    ("London, UK", False),
    ("Sydney, Australia", False),
    ("Belgrade", False),
    ("Mexico City, Mexico", False),
    ("Paris", False),
    ("Korea", False),
    ("Hong Kong, STP", False),
    ("Taiwan, Hsinchu", False),
    ("China, Shanghai", False),
    ("Switzerland, Zurich", False),
    ("Bangalore", False),
    ("Hyderabad", False),
    ("Tel Aviv", False),
    ("Singapore", False),
    ("Dublin, IE", False),
    ("Hamburg", False),
    ("DE-Berlin-Trion Building", False),
    ("PL-Warsaw", False),
    # ---- Ambiguous: strict mode drops ----
    ("Remote", False),
    ("", False),
    ("7 Locations", False),
    ("3 Locations", False),
    # ---- The "in" / "or" state-code false-positive guard ----
    # "Indianapolis, IN" should match (IN = Indiana state)
    ("Indianapolis, IN", True),
    # But the word "in" inside a sentence should NOT trigger
    ("Engineer in Office", False),  # no actual US marker
]


@pytest.mark.parametrize("location,expected", US_CASES)
def test_is_us_location(location: str, expected: bool) -> None:
    assert is_us_location(location) is expected, (
        f"is_us_location({location!r}) -> expected {expected}"
    )


def test_is_us_location_none() -> None:
    assert is_us_location(None) is False


# =============================================================================
# Obvious-reject pre-filter (LLM path)
# =============================================================================

@pytest.mark.parametrize("title,expected", [
    ("Senior Software Engineer", True),
    ("Staff Software Engineer", True),
    ("Engineering Manager", True),
    ("Director of Data Science", True),
    ("Lead Software Engineer", True),
    ("Marketing Intern", True),
    ("Campus Recruiting Specialist", True),
    ("Talent Acquisition Coordinator", True),
    ("Group Leader, Immune Cell Reprogramming", True),
    ("Postdoctoral Researcher", True),
    ("Postdoc Fellow, Machine Learning", True),
    ("", True),
    # Must reach LLM — never pre-filter
    ("Member of Technical Staff", False),
    ("Software Engineer II", False),
    ("Software Engineer Intern", False),
    ("Machine Learning Engineer, New Grad 2026", False),
    ("Software Engineer", False),
    ("Junior Software Development Engineer", False),
])
def test_is_obvious_reject(title: str, expected: bool) -> None:
    assert is_obvious_reject(title) is expected


@pytest.mark.parametrize("title,expected_reason", [
    ("Senior Software Engineer", "senior/management"),
    ("Marketing Intern", "non-tech"),
    ("Software Engineer Intern", None),
    ("Member of Technical Staff", None),
    ("", "empty title"),
])
def test_obvious_reject_reason(title: str, expected_reason: str | None) -> None:
    assert obvious_reject_reason(title) == expected_reason


def test_classify_title_confidence_high_include() -> None:
    conf = classify_title_confidence("Software Engineer Intern")
    assert conf.level == "high_include"
    assert conf.is_technical is True


def test_classify_title_confidence_bare_title_excluded() -> None:
    conf = classify_title_confidence("Software Engineer")
    assert conf.level == "high_exclude"
    assert conf.is_technical is True
    assert conf.reason == "no description"


def test_classify_title_confidence_hardware_intern() -> None:
    conf = classify_title_confidence("ChipSim Intern - Spring 2027")
    assert conf.level == "high_include"
    assert conf.is_technical is True


def test_engineer_ii_excluded_without_new_grad() -> None:
    conf = classify_title_confidence(
        "Software Engineer II",
        "Minimum qualifications: Bachelor's degree. 2+ years of experience.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "experienced level title"


def test_technical_support_engineer_1_included() -> None:
    conf = classify_title_confidence(
        "Technical Support Engineer 1",
        "Bachelor's degree. 0-2 years experience supporting production systems.",
    )
    assert conf.level == "high_include"


def test_tech_fellowship_included() -> None:
    conf = classify_title_confidence("American Tech Fellowship for Veterans")
    assert conf.level == "high_include"
    assert conf.reason == "fellowship program"


def test_group_leader_excluded() -> None:
    conf = classify_title_confidence(
        "Group Leader, Immune Cell Reprogramming",
        "PhD required. Looking for experienced group leader.",
    )
    assert conf.level == "high_exclude"


def test_postdoctoral_excluded() -> None:
    conf = classify_title_confidence("Postdoctoral Researcher, ML Systems")
    assert conf.level == "high_exclude"


def test_program_manager_intern_excluded() -> None:
    conf = classify_title_confidence(
        "Program Manager, uBecome Intern Experience & Community"
    )
    assert conf.level == "high_exclude"


def test_network_operations_technician_excluded() -> None:
    conf = classify_title_confidence("Network Operations Technician")
    assert conf.level == "high_exclude"


def test_data_center_technician_excluded() -> None:
    conf = classify_title_confidence("Data Center Technician")
    assert conf.level == "high_exclude"


# --- Production precision fixes (2026-05) ------------------------------------


@pytest.mark.parametrize(
    "title",
    [
        "Graduate 2026 PhD Software Engineer II (AV Labs), United States",
        "Graduate 2026 PhD Scientist II (Economists Only), Reservations",
        "DevOps Engineer, Level 4",
        "Engineering Business Analyst - P2 - (Hybrid)",
        "HWIL Mechanical Engineer - P2",
        "Raytheon Full Time 2026 - Power & Analog Design Engineer II",
    ],
)
def test_cohort_branding_does_not_save_ladder_levels(title: str) -> None:
    conf = classify_title_confidence(
        title,
        "New grads welcome. PhD preferred. Bachelor's degree required.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason in {"experienced level title", "non-tech"}


def test_open_level_team_swe_excluded_without_strong_ec() -> None:
    conf = classify_title_confidence(
        "Software Engineer, Starlink Network",
        "Bachelor's degree in Computer Science or related field.",
    )
    assert conf.level == "high_exclude"


def test_open_level_team_swe_included_with_new_grad_in_title() -> None:
    conf = classify_title_confidence(
        "Software Engineer, New Grad - Starlink",
        "Bachelor's degree required.",
    )
    assert conf.level == "high_include"


def test_bare_swe_with_early_years_still_included() -> None:
    conf = classify_title_confidence(
        "Software Engineer",
        "Qualifications:\n1-3 years of experience building web applications.\n"
        "Bachelor's degree in Computer Science preferred.",
    )
    assert conf.level == "high_include"


@pytest.mark.parametrize(
    "title",
    [
        "Counsel, Commercial",
        "Founder's Office, Applied AI",
        "Administrative Generalist",
        "DoorDash for Business Support Representative",
        "Associate Strategic Account Development Executive - Platform",
        "Division Operations Associate",
        "Deployment Systems Technician",
        "Junior Clinical Trials Data Specialist",
        "IT Services Technician",
        "Enterprise AI Associate",
        "Associate Marketing Data Analyst - Marketing Analytics",
        "GSOC Operator",
        "Equipment Technician, Vacuum, Semiconductor",
        "Quantitative Portfolio Analyst – 2026 Grad",
        "Equity Quantitative Researcher",
        "Fundamental Research Fellowship, Canvas",
    ],
)
def test_safe_non_tech_prefilter(title: str) -> None:
    assert is_obvious_reject(title) is True


@pytest.mark.parametrize(
    "title",
    [
        "Associate Software Engineer - Seeking 2025 & 2026 Grads",
        "Quantitative Software Developer",
        "Quantitative Research Intern",
        "Quantitative Developer Intern",
        "Support Engineer",
    ],
)
def test_safe_prefilter_does_not_drop_viable_eng(title: str) -> None:
    assert is_obvious_reject(title) is False


def test_classify_title_confidence_mts_excluded() -> None:
    conf = classify_title_confidence(
        "Member of Technical Staff (Backend Software Engineer)",
        "Qualifications: 5+ years of software engineering experience required.",
    )
    assert conf.level == "high_exclude"


def test_classify_title_confidence_description_ec_signal() -> None:
    conf = classify_title_confidence(
        "Software Engineer",
        "You may be a good fit if you have\n"
        "This is a new grad role for 2026 university graduates.",
    )
    assert conf.level == "high_include"
    assert conf.is_technical is True


def test_classify_title_confidence_description_does_not_trigger_senior() -> None:
    conf = classify_title_confidence(
        "Software Engineer Intern",
        "What you'll do: collaborate with senior engineers on platform work.",
    )
    assert conf.level == "high_include"
    assert conf.is_technical is True


def test_full_description_domain_does_not_inflate_borderline() -> None:
    """Marketing copy with 'software' must not create bare-technical borderline."""
    conf = classify_title_confidence(
        "Account Executive",
        "We build software platforms used by millions of customers worldwide.",
    )
    assert conf.level == "high_exclude"


@pytest.mark.parametrize("location,expected", [
    ("Remote", True),
    ("", True),
    ("7 Locations", True),
    ("San Francisco, CA", False),
    ("Remote - United States", False),
])
def test_is_location_ambiguous(location: str, expected: bool) -> None:
    assert is_location_ambiguous(location) is expected


# --- Eval-driven precision fixes (2026-05) ------------------------------------


@pytest.mark.parametrize(
    "title",
    [
        "Writing Specialist",
        "Technical Advisor Specialist (Part-Time Internship)",
        "2027 Point72 Academy Investment Analyst Summer Internship Program",
        "Mission Control Specialist",
        "Customer Enablement Specialist",
        "Field Application Engineer - New College Graduate 2026",
        "Anthropic Fellows Program",
        "Anthropic Fellows Program, AI Safety",
        "UK Internship Program",
        "Network Engineer",
        "Software Engineer, Post-Training Research",
        "Researcher, Agent Post-Training",
    ],
)
def test_eval_precision_excludes(title: str) -> None:
    conf = classify_title_confidence(
        title,
        "Minimum qualifications: 5+ years of experience. PhD required.",
    )
    assert conf.level == "high_exclude"


def test_anthropic_fellows_not_included_with_ec_requirements() -> None:
    conf = classify_title_confidence(
        "Anthropic Fellows Program",
        "New grads welcome. Bachelor's degree required.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "corporate fellowship program"


def test_tech_fellowship_still_included() -> None:
    conf = classify_title_confidence("American Tech Fellowship for Veterans")
    assert conf.level == "high_include"


def test_physical_design_excluded_without_ec_bar() -> None:
    conf = classify_title_confidence(
        "Physical Design Engineer",
        "Minimum qualifications: Bachelor's degree. 4+ years in physical design.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "experienced hardware ic"


def test_physical_design_intern_still_included() -> None:
    conf = classify_title_confidence(
        "Physical Design Engineer Intern - Fall 2026",
        "Currently enrolled in a Bachelor's program.",
    )
    assert conf.level == "high_include"


def test_research_engineer_excluded_with_senior_yoe() -> None:
    conf = classify_title_confidence(
        "Research Engineer, Pretraining",
        "Minimum qualifications: PhD plus 3 years of ML research experience.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "experienced research role"


def test_research_intern_still_included() -> None:
    conf = classify_title_confidence(
        "Research Scientist Intern - Summer 2026",
        "Currently pursuing a PhD in Computer Science.",
    )
    assert conf.level == "high_include"


def test_network_ops_residency_not_blocked() -> None:
    conf = classify_title_confidence(
        "Network Operations Residency Program, University Graduate, 2026 Start",
        "Bachelor's degree required. No prior experience required.",
    )
    assert conf.reason != "non-ec network engineer"


def test_nvidia_ncg_architect_not_senior_keyword() -> None:
    conf = classify_title_confidence(
        "GPU System and Scheduling Architect - New College Grad 2026",
        "Bachelor's or Master's degree. New college grad hiring.",
    )
    assert conf.level != "high_exclude" or conf.reason != "senior keyword"


def test_spacex_application_swe_included_with_bar() -> None:
    desc = (
        "Bachelor's degree; OR 2+ years of professional experience building software "
        "in lieu of a degree. 1+ years of experience in full stack development."
    )
    conf = classify_title_confidence(
        "Application Software Engineer",
        desc,
        company="SpaceX",
    )
    assert conf.level == "high_include"
    assert conf.reason == "spacex early swe credential"


def test_spacex_build_engineer_excluded() -> None:
    conf = classify_title_confidence(
        "Build Engineer (Starship)",
        "1+ years of experience in manufacturing environments.",
        company="SpaceX",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "spacex non-swe role"


def test_spacex_comma_swe_requires_early_bar() -> None:
    conf = classify_title_confidence(
        "Software Engineer, Starlink Network",
        "Bachelor's degree in computer science required.",
        company="SpaceX",
    )
    assert conf.level == "high_exclude"


def test_research_engineer_pretraining_excluded() -> None:
    conf = classify_title_confidence(
        "Research Engineer, Pretraining",
        "Minimum qualifications: PhD plus 3 years of ML research experience.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "experienced research role"


def test_spacex_comma_swe_included_with_bachelor_qual() -> None:
    desc = (
        "BASIC QUALIFICATIONS: Bachelor's degree in computer science and "
        "1+ year of industry and/or internship experience."
    )
    conf = classify_title_confidence(
        "Software Engineer, Starlink Growth",
        desc,
        company="SpaceX",
    )
    assert conf.level == "high_include"


def test_spacex_embedded_with_or_3yr_excluded() -> None:
    desc = (
        "BASIC QUALIFICATIONS: Bachelor's degree and 1+ years of experience; "
        "OR 3+ years of professional experience in software engineering."
    )
    conf = classify_title_confidence(
        "Embedded Software Engineer (Starlink)",
        desc,
        company="SpaceX",
    )
    assert conf.level == "high_exclude"


def test_meta_entry_research_engineer_included() -> None:
    conf = classify_title_confidence(
        "Research Engineer, Monetization AI",
        "Minimum qualifications: Bachelor's degree in CS. "
        "We are looking for strong engineers to join our team.",
    )
    assert conf.level == "high_include"
    assert conf.reason == "entry-level research or ds"


def test_doordash_ai_research_fellowship_included() -> None:
    conf = classify_title_confidence(
        "AI Research Fellowship, (Summer and Fall 2026)",
        "Undergraduate or graduate students pursuing technical degrees.",
    )
    assert conf.level == "high_include"
