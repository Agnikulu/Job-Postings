"""Tests for requirements-section extraction and description signals."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from description_signals import extract_description_signals, extract_requirements_text
from filters import classify_title_confidence

DOORDASH_LIKE = """
About the Role
We are building the next generation of ML systems.

What you'll do
- Ship research prototypes
- Collaborate with product teams

You may be a good fit if you have
Progress in a degree in Computer Science, Computer Engineering, Statistics,
Applied Mathematics, or related fields.
Previous internship experience in high-ownership, high-pressure roles within
startup environments.

About you because you're a researcher with a strong track record — PhD candidates (rising 4th
year or beyond), recent PhDs, or independent researchers with published work
at top ML venues.

About you and your overall well-being. That's why we offer wellness benefits.
"""


def test_extract_requirements_text_finds_section() -> None:
    req = extract_requirements_text(DOORDASH_LIKE)
    assert req is not None
    assert "PhD candidates" in req
    assert "internship experience" in req
    assert "What you'll do" not in req


def test_extract_description_signals_ec_and_field() -> None:
    sig = extract_description_signals(DOORDASH_LIKE)
    assert sig.has_ec is True
    assert sig.has_tech_field is True
    assert sig.has_senior_exp is False


def test_classify_generic_title_with_requirements_ec() -> None:
    conf = classify_title_confidence(
        "Research Engineer",
        DOORDASH_LIKE,
    )
    assert conf.level == "high_include"
    assert conf.is_technical is True
    assert "requirements" in (conf.reason or "")


def test_senior_exp_in_requirements_excludes_without_ec() -> None:
    desc = """
    Requirements:
    Minimum of 8 years of professional experience leading engineering teams.
    Bachelor's degree in Computer Science preferred.
    """
    conf = classify_title_confidence("Software Engineer", desc)
    assert conf.level == "high_exclude"


def test_bachelors_only_without_ec_signal_excludes_bare_swe() -> None:
    desc = """
    Qualifications:
    Bachelor's degree required in Computer Science or related field.
    """
    conf = classify_title_confidence("Software Engineer", desc)
    assert conf.level == "high_exclude"
    assert conf.is_technical is True


def test_intern_in_title_still_includes_despite_senior_in_description() -> None:
    desc = """
    You may be a good fit if you have
    Comfort working with senior engineers and engineering managers.
    """
    conf = classify_title_confidence("Software Engineer Intern", desc)
    assert conf.level == "high_include"


CURSOR_LIKE = """
Our mission is to automate coding.
ABOUT THE ROLE As a Product Engineer on the Growth team, you'll design systems.
YOU MAY BE A FIT IF
- You have an entrepreneurial spirit and love creating outsized business impact.
- You're passionate about building great products.
"""

DATABRICKS_LIKE = """
The impact you will have:
Develop cutting-edge GenAI solutions.
What we look for:
Experience building GenAI applications with LangChain.
Graduate degree in Computer Science or equivalent practical experience.
Benefits At Databricks, we strive to provide comprehensive benefits.
"""

NOTION_LIKE = """
ABOUT THE ROLE: We're looking for a motivated early career sales professional.
WHAT YOU'LL ACHIEVE: - Sell a product people love.
SKILLS YOU'LL NEED TO BRING: - You have at least 6 months of outbound experience.
Notion is proud to be an equal opportunity employer.
"""

ANTHROPIC_DUTIES = """
Responsibilities: Understand the data needs of stakeholder teams in terms of
key data models and translate that into technical requirements Define, build
and manage key data pipelines in dbt.
Minimum education: Bachelor's degree or equivalent combination of education.
Minimum years of experience: 5+ years of professional experience required.
"""


def test_cursor_you_may_be_a_fit_if() -> None:
    req = extract_requirements_text(CURSOR_LIKE)
    assert req is not None
    assert "entrepreneurial" in req.lower()


def test_databricks_what_we_look_for() -> None:
    req = extract_requirements_text(DATABRICKS_LIKE)
    assert req is not None
    assert "genai" in req.lower()
    assert "benefits" not in req.lower()


def test_notion_skills_youll_need_to_bring() -> None:
    req = extract_requirements_text(NOTION_LIKE)
    assert req is not None
    assert "6 months" in req
    assert "equal opportunity" not in req.lower()


def test_anthropic_skips_technical_requirements_false_positive() -> None:
    req = extract_requirements_text(ANTHROPIC_DUTIES)
    assert req is not None
    assert "minimum education" in req.lower()
    assert "define, build and manage key data pipelines" not in req.lower()


ANTHROPIC_SENIOR_YEARS = """
You may be a good fit if you:
Have 10+ years of software engineering experience, with a track record of
operating as a Staff or Principal engineer (or equivalent) at a high-caliber organization.
"""

CURSOR_EXPERIENCED = """
YOU MAY BE A FIT IF
- You have experience building internal developer platforms, service frameworks,
  or infrastructure abstractions that other engineers depend on.
- You've worked extensively with Temporal, durable workflow engines, or similar.
"""

BARE_EC_YEARS = """
Qualifications:
1-3 years of experience building web applications.
Bachelor's degree in Computer Science preferred.
"""


def test_senior_years_with_intervening_words() -> None:
    sig = extract_description_signals(ANTHROPIC_SENIOR_YEARS)
    assert sig.has_senior_exp is True
    conf = classify_title_confidence("Software Engineer", ANTHROPIC_SENIOR_YEARS)
    assert conf.level == "high_exclude"
    assert conf.reason == "senior experience required"


def test_bare_swe_excludes_when_requirements_have_no_ec() -> None:
    conf = classify_title_confidence("Software Engineer", CURSOR_EXPERIENCED)
    assert conf.level == "high_exclude"
    assert conf.reason == "no ec in requirements"
    assert conf.is_technical is True


def test_bare_swe_excluded_without_description() -> None:
    conf = classify_title_confidence("Software Engineer")
    assert conf.level == "high_exclude"
    assert conf.reason == "no description"


def test_one_to_three_years_promotes_ec() -> None:
    conf = classify_title_confidence("Software Engineer", BARE_EC_YEARS)
    assert conf.level == "high_include"
    assert conf.is_technical is True


GOOGLE_CURVY_APOSTROPHE = """
Minimum qualifications: Bachelor\u2019s degree or equivalent practical experience.
2 years of experience with software development in one or more programming languages.
"""

UBER_H1B = """
**Employer:** Uber Technologies, Inc.
**Job Title:** Software Engineer
**Duties:** Design, develop, and test software applications.
Employer will accept a Master's degree in Computer Science and 4 years of experience
in the job offered or related occupation.
"""

WORKDAY_QUALS = """
WHAT YOU'LL BE DOING
- Develop GPU system software

WHAT WE NEED TO SEE
- BS or MS in Computer Science
- 5+ years of software engineering experience
"""


def test_curly_apostrophe_bachelors_detected() -> None:
    sig = extract_description_signals(GOOGLE_CURVY_APOSTROPHE)
    assert sig.has_bachelors_req is True
    conf = classify_title_confidence(
        "Software Engineer, Mobile iOS, Maps",
        GOOGLE_CURVY_APOSTROPHE,
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "minimum experience required"


def test_uber_h1b_senior_years_excluded() -> None:
    sig = extract_description_signals(UBER_H1B)
    assert sig.requirements_text is not None
    assert sig.has_senior_exp is True
    conf = classify_title_confidence("Software Engineer", UBER_H1B)
    assert conf.level == "high_exclude"
    assert conf.reason == "senior experience required"


def test_workday_what_we_need_to_see() -> None:
    req = extract_requirements_text(WORKDAY_QUALS)
    assert req is not None
    assert "what we need to see" in req.lower()
    sig = extract_description_signals(WORKDAY_QUALS)
    assert sig.has_senior_exp is True


def test_implementation_lead_excluded_despite_bachelors_in_description() -> None:
    desc = """
    Qualifications:
    Bachelor's degree required in Computer Science or related field.
    """
    conf = classify_title_confidence("Implementation Lead, Uber for Business", desc)
    assert conf.level == "high_exclude"
    assert conf.reason in {"senior keyword", "non-tech"}


GOOGLE_TWO_YEARS = """
Minimum qualifications: Bachelor's degree or equivalent practical experience.
2 years of experience with software development in one or more programming languages.
"""

UBER_H1B_THREE_YEARS = """
Employer will accept a Bachelor's degree in Computer Science and three years of
experience in the job offered or in a related occupation.
"""


def test_bachelors_plus_two_years_excludes() -> None:
    conf = classify_title_confidence("Software Engineer, Mobile iOS, Maps", GOOGLE_TWO_YEARS)
    assert conf.level == "high_exclude"
    assert conf.reason == "minimum experience required"


def test_h1b_three_years_excludes() -> None:
    sig = extract_description_signals(UBER_H1B_THREE_YEARS)
    assert sig.has_senior_exp is True
    conf = classify_title_confidence("Software Engineer", UBER_H1B_THREE_YEARS)
    assert conf.level == "high_exclude"


def test_hfc_fellowship_excluded() -> None:
    conf = classify_title_confidence(
        "Machine Learning Fellow - Human Frontier Collective (US)",
        "Education: PhD or postdoctoral degree. Professional Background: 1-3+ years.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "expert fellowship"


def test_post_training_research_scientist_excluded() -> None:
    conf = classify_title_confidence(
        "Machine Learning Research Scientist, Post-Training",
        "Ph.D. in Computer Science. Deep understanding of reinforcement learning.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "senior post-training role"


def test_capital_markets_intern_excluded() -> None:
    conf = classify_title_confidence(
        "Capital Markets & Corporate Development Intern - Summer 2026",
        "Support the finance team with market analysis.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "non-technical intern"


def test_associate_field_engineer_excluded() -> None:
    conf = classify_title_confidence(
        "Associate Field Engineer",
        "Lead onboarding sessions and live demos for customers.",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "non-tech"


def test_cursor_open_level_swe_included() -> None:
    conf = classify_title_confidence("Software Engineer, Growth", CURSOR_LIKE)
    assert conf.level == "high_include"
    assert conf.reason == "open-level technical ic"


def test_bare_swe_still_excluded_without_team_suffix() -> None:
    conf = classify_title_confidence("Software Engineer", CURSOR_LIKE)
    assert conf.level == "high_exclude"
    assert conf.reason == "no ec in requirements"


def test_perplexity_mts_policy_excluded() -> None:
    conf = classify_title_confidence(
        "Member of Technical Staff (AI Policy and Strategic Initiatives)",
        "Exceptionally talented early-career engineers (new grads welcome).",
    )
    assert conf.level == "high_exclude"
    assert conf.reason == "experienced mts title"
