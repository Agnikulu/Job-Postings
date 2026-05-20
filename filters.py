"""Regex filter engine.

Three regexes:
  TARGET — Must match. Identifies early-career roles.
  ANTI   — Must NOT match. Anything senior/managerial drops out.
  DOMAIN — Optional badge. If it matches, the role is technical.

`classify(title)` returns (passes_filters, is_technical).
Domain match is informational only — it adds a [TECHNICAL] badge to the
Discord notification but does not gate alerts. Per project decision, we want
all early-career roles surfaced so the user can sanity-check borderline ones.
"""

from __future__ import annotations

import re

TARGET = re.compile(
    r"\b("
    r"intern(ship)?|co-?op|new[\s-]?grad(uate)?|university\s+graduate|"
    r"early[\s-]career|entry[\s-]level|campus|"
    r"2026|2027"
    r")\b",
    re.IGNORECASE,
)

ANTI = re.compile(
    r"\b("
    r"senior|sr\.?|lead|"
    r"manager|principal|director|"
    r"head\s+of|staff|"
    r"vp|vice\s+president|president"
    r")\b",
    re.IGNORECASE,
)

DOMAIN = re.compile(
    r"\b("
    r"software|engineer(ing)?|"
    r"machine[\s-]learning|ml|"
    r"data|quant(itative)?|research|"
    r"computer\s+science|cs|"
    r"backend|frontend|full[\s-]?stack|"
    r"infrastructure|platform|systems|"
    r"ai|artificial\s+intelligence|"
    r"applied\s+scientist"
    r")\b",
    re.IGNORECASE,
)


def classify(title: str) -> tuple[bool, bool]:
    """Return (passes, is_technical).

    - passes is True when TARGET matches and ANTI does not.
    - is_technical is True when DOMAIN also matches.
    """
    if not title:
        return (False, False)
    if ANTI.search(title):
        return (False, False)
    if not TARGET.search(title):
        return (False, False)
    return (True, bool(DOMAIN.search(title)))
