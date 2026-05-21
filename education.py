"""Education-level tagger.

`extract_education_levels(title)` returns a list of tags from
{"PhD", "Masters", "Bachelors", "New Grad", "Intern"} ordered from most
specific to most general. A title can have multiple tags (e.g.
"PhD ML Engineer, Intern" -> ["PhD", "Intern"]).

The tags are multi-label because in practice many roles legitimately
span multiple levels (a PhD internship, a Masters/New Grad combo posting,
etc.).

Order rules:
1. Degree levels (PhD, Masters, Bachelors) come first, most specific first.
2. Then experience-level (New Grad, Intern).
3. If no degree level matches and no experience-level matches but TARGET
   still matched somehow, we fall back to ["Early Career"].
"""

from __future__ import annotations

import re

# Degree-level patterns. PhD and Masters are kept narrow to avoid noise.
_PHD = re.compile(
    r"\b(ph\.?\s?d\.?|doctoral|doctorate|postdoc|post-doc|post\s+doctoral)\b",
    re.IGNORECASE,
)
_MASTERS = re.compile(
    r"\b("
    r"master'?s|"
    r"m\.?s\.?(?=[\s,.;:)]|$)|"  # MS with boundary on the right
    r"m\.?eng\.?|"
    r"msc\b|"
    r"graduate\s+student"
    r")\b",
    re.IGNORECASE,
)
_BACHELORS = re.compile(
    r"\b("
    r"bachelor'?s|"
    r"undergrad(uate)?|"
    r"b\.?s\.?(?=[\s,.;:)]|$)|"
    r"b\.?eng\.?|"
    r"bsc\b"
    r")\b",
    re.IGNORECASE,
)

# Experience-level patterns.
_NEW_GRAD = re.compile(
    r"\b("
    r"new[\s-]?grad(uate)?|"
    r"new\s+college\s+grad|ncg|"
    r"university\s+graduate|"
    r"recent\s+graduate|"
    r"early[\s-]career|"
    r"entry[\s-]level|"
    r"campus"
    r")\b",
    re.IGNORECASE,
)
_INTERN = re.compile(
    r"\b(intern(ship)?|co-?op)\b",
    re.IGNORECASE,
)


def extract_education_levels(title: str | None) -> list[str]:
    """Return ordered, deduplicated list of education tags for `title`."""
    if not title:
        return []
    tags: list[str] = []
    if _PHD.search(title):
        tags.append("PhD")
    if _MASTERS.search(title):
        tags.append("Masters")
    if _BACHELORS.search(title):
        tags.append("Bachelors")
    if _NEW_GRAD.search(title):
        tags.append("New Grad")
    if _INTERN.search(title):
        tags.append("Intern")
    return tags
