"""Shared types and exceptions for ATS adapters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Job:
    """Normalized job posting, ATS-agnostic."""

    id: str
    company: str
    title: str
    location: str
    url: str
    posted_at: str | None         # Raw value as returned by the ATS.
    department: str | None
    ats: str
    category: str
    # Populated by the orchestrator after fetch:
    posted_date: str | None = None        # YYYY-MM-DD normalized.
    education_levels: tuple[str, ...] = ()  # ("PhD", "Intern", ...)
    is_us: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "company": self.company,
            "title": self.title,
            "location": self.location,
            "url": self.url,
            "posted_at": self.posted_at,
            "posted_date": self.posted_date,
            "department": self.department,
            "ats": self.ats,
            "category": self.category,
            "education_levels": list(self.education_levels),
            "is_us": self.is_us,
        }


class AdapterError(Exception):
    """Raised when a single company's fetch ultimately fails.

    The orchestrator catches this so one broken company never aborts the run.
    """


DEFAULT_TIMEOUT = 20
DEFAULT_HEADERS = {
    "User-Agent": (
        "serverless-ats-sniper/1.0 "
        "(+https://github.com/your-username/serverless-ats-sniper)"
    ),
    "Accept": "application/json",
}
