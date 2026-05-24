"""Education-level tagger (requirements-first).

Returns ordered tags from:
  Intern, New Grad,
  PhD Student, MS Student, BS Student,
  PhD, Masters, Bachelors (degree required / completed path)

Requirements text is preferred over title; title wins for obvious program names.
"""

from __future__ import annotations

import re

from description_signals import extract_requirements_text
from filters import (
    has_explicit_ec_title,
    is_experienced_level_title,
    is_hard_experienced_ladder,
)

# --- Student / in-progress (requirements-first) --------------------------------

_BS_STUDENT = re.compile(
    r"\b("
    r"undergraduate\s+student|bachelor'?s\s+student|"
    r"pursuing\s+(?:a\s+)?(?:bachelor|undergraduate)|"
    r"currently\s+(?:enrolled|pursuing).{0,40}\b(?:bachelor|undergraduate)|"
    r"enrolled\s+in.{0,40}\b(?:bachelor|undergraduate)"
    r")\b",
    re.IGNORECASE,
)
_MS_STUDENT = re.compile(
    r"\b("
    r"master'?s\s+student|graduate\s+student(?!\s+researcher)|"
    r"pursuing\s+(?:a\s+)?master|"
    r"currently\s+(?:enrolled|pursuing).{0,40}\bmaster"
    r")\b",
    re.IGNORECASE,
)
_PHD_STUDENT = re.compile(
    r"\b("
    r"ph\.?\s?d\.?\s+(?:student|candidate)|doctoral\s+candidate|"
    r"pursuing\s+(?:a\s+)?(?:ph\.?\s?d|doctorate|doctoral)|"
    r"currently\s+(?:enrolled|pursuing).{0,40}\b(?:ph\.?\s?d|doctorate)"
    r")\b",
    re.IGNORECASE,
)

# --- Degree required (minimum qualifications) --------------------------------

_PHD_REQUIRED = re.compile(
    r"\b("
    r"ph\.?\s?d\.?(?:\s+degree)?\s+(?:required|preferred)|"
    r"doctorate\s+(?:required|preferred)|"
    r"doctoral\s+degree|"
    r"postdoc|post-doc"
    r")\b",
    re.IGNORECASE,
)
_MS_REQUIRED = re.compile(
    r"\b("
    r"master'?s\s+(?:degree\s+)?(?:required|preferred)|"
    r"m\.?s\.?\s+(?:degree\s+)?(?:required|preferred)|"
    r"graduate\s+degree\s+(?:required|preferred)"
    r")\b",
    re.IGNORECASE,
)
_BS_REQUIRED = re.compile(
    r"\b("
    r"bachelor'?s\s+(?:degree\s+)?(?:required|preferred)|"
    r"undergraduate\s+degree(?:\s+required)?|"
    r"four[\s-]?year\s+degree(?:\s+required)?|"
    r"minimum\s+education\s*:\s*bachelor"
    r")\b",
    re.IGNORECASE,
)

# --- Experience-level programs -------------------------------------------------

_INTERN = re.compile(r"\b(intern(ship)?|co-?op)\b", re.IGNORECASE)

_NEW_GRAD = re.compile(
    r"\b("
    r"new[\s-]?grad(?:uate)?|new\s+college\s+grad(?:uate)?|ncg|"
    r"college\s+grad(?:uate)?(?:\s+20[2-9][0-9])?|"
    r"university\s+graduate|recent\s+graduate|"
    r"graduating\s+(?:in\s+)?(?:20[2-9][0-9]|spring|fall|summer|winter)|"
    r"expected\s+graduation|class\s+of\s+20[2-9][0-9]|"
    r"college\s+grad\s+20[2-9][0-9]|"
    r"seeking\s+(?:20[2-9][0-9]\s*(?:&\s*20[2-9][0-9])?\s+)?grads?|"
    r"(?:20[2-9][0-9]\s+grads?|grads?\s+(?:for\s+)?20[2-9][0-9])"
    r")\b",
    re.IGNORECASE,
)

# Title-only cues (avoid tagging "entry-level" IC roles as New Grad from body alone).
_TITLE_NEW_GRAD = re.compile(
    r"\b("
    r"new[\s-]?grad(?:uate)?|new\s+college\s+grad(?:uate)?|university\s+graduate|"
    r"early[\s-]career|entry[\s-]level|campus|"
    r"seeking\s+(?:20[2-9][0-9]\s*(?:&\s*20[2-9][0-9])?\s+)?grads?|"
    r"(?:20[2-9][0-9]\s+grads?|grads?\s+(?:for\s+)?20[2-9][0-9])"
    r")\b",
    re.IGNORECASE,
)

_TITLE_EARLY_CAREER = re.compile(
    r"\b(engineer\s+i\b|engineer\s+1\b)\b",
    re.IGNORECASE,
)

_TITLE_PHD = re.compile(
    r"\b(ph\.?\s?d\.?|doctoral|doctorate)\b",
    re.IGNORECASE,
)
_TITLE_MASTERS = re.compile(
    r"\b(master'?s|m\.?s\.?(?=[\s,.;:)]|$)|m\.?eng\.?)\b",
    re.IGNORECASE,
)
_TITLE_BACHELORS = re.compile(
    r"\b(bachelor'?s|undergrad(?:uate)?|b\.?s\.?(?=[\s,.;:)]|$))\b",
    re.IGNORECASE,
)

# Loose degree words in title (PhD Intern, MS Intern, etc.)
_TITLE_INTERN = _INTERN


def _ordered_unique(tags: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def _scan_student_and_required(req: str, title: str) -> list[str]:
    tags: list[str] = []
    blob = f"{title} {req}".strip()

    if _TITLE_PHD.search(title) and _TITLE_INTERN.search(title):
        tags.append("PhD")
    elif _PHD_STUDENT.search(req) or _PHD_STUDENT.search(title):
        tags.append("PhD Student")

    if _MS_STUDENT.search(req) or (
        _TITLE_MASTERS.search(title) and _TITLE_INTERN.search(title)
    ):
        tags.append("MS Student")
    elif _MS_STUDENT.search(title):
        tags.append("MS Student")

    if _BS_STUDENT.search(req) or (
        _TITLE_BACHELORS.search(title) and _TITLE_INTERN.search(title)
    ):
        tags.append("BS Student")
    elif _BS_STUDENT.search(title):
        tags.append("BS Student")

    if "PhD Student" not in tags and _PHD_REQUIRED.search(req):
        tags.append("PhD")
    elif "PhD Student" not in tags and _TITLE_PHD.search(title) and not is_experienced_level_title(title):
        tags.append("PhD")

    if "MS Student" not in tags and _MS_REQUIRED.search(req):
        tags.append("Masters")
    elif "MS Student" not in tags and _TITLE_MASTERS.search(title) and not is_experienced_level_title(title):
        tags.append("Masters")

    if "BS Student" not in tags and _BS_REQUIRED.search(req):
        tags.append("Bachelors")
    elif "BS Student" not in tags and _TITLE_BACHELORS.search(title) and not is_experienced_level_title(title):
        tags.append("Bachelors")

    if _NEW_GRAD.search(req) or _TITLE_NEW_GRAD.search(title):
        tags.append("New Grad")
    elif _NEW_GRAD.search(blob) and has_explicit_ec_title(title):
        tags.append("New Grad")

    if _INTERN.search(title):
        tags.append("Intern")

    if _TITLE_EARLY_CAREER.search(title) and "New Grad" not in tags:
        tags.append("Early Career")

    return tags


def extract_education_levels(
    title: str | None = None,
    *,
    requirements_text: str | None = None,
    description: str | None = None,
) -> list[str]:
    """Return ordered education tags for a matched posting."""
    title_text = (title or "").strip()
    if is_hard_experienced_ladder(title_text):
        return []
    if is_experienced_level_title(title_text) and not has_explicit_ec_title(title_text):
        return []

    req = (requirements_text or "").strip()
    if not req and description:
        req = (extract_requirements_text(description) or "").strip()

    if not req and title_text:
        req = ""

    tags = _scan_student_and_required(req, title_text)

    if not tags and title_text:
        skip_degree_tags = is_hard_experienced_ladder(title_text) or (
            is_experienced_level_title(title_text) and not has_explicit_ec_title(title_text)
        )
        if _TITLE_INTERN.search(title_text):
            tags.append("Intern")
        if _TITLE_NEW_GRAD.search(title_text) and not skip_degree_tags:
            tags.append("New Grad")
        if _TITLE_PHD.search(title_text) and not skip_degree_tags:
            tags.append("PhD")
        if _TITLE_MASTERS.search(title_text) and not skip_degree_tags:
            tags.append("Masters")
        if _TITLE_BACHELORS.search(title_text) and not skip_degree_tags:
            tags.append("Bachelors")
        if _TITLE_EARLY_CAREER.search(title_text) and "New Grad" not in tags:
            tags.append("Early Career")

    order = (
        "PhD Student",
        "MS Student",
        "BS Student",
        "PhD",
        "Masters",
        "Bachelors",
        "New Grad",
        "Early Career",
        "Intern",
    )
    rank = {name: i for i, name in enumerate(order)}
    tags.sort(key=lambda t: rank.get(t, 99))
    return _ordered_unique(tags)
