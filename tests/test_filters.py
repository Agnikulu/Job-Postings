"""Unit tests for the filter engine.

Run from the project root:

    pytest -q
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from filters import classify, diagnose_weak_signal, is_us_location


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
    # ---- Positive: pass, but non-technical (no DOMAIN match) ----
    ("Marketing Intern", True, False),
    ("Recruiting Coordinator, Early Career", True, False),
    ("Campus Recruiting Specialist", True, False),
    ("Talent Intern - Fall 2026", True, False),
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
    ("Software Engineer II", "engineer ii"),
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
