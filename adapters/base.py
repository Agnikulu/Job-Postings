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
    posted_at: str | None
    department: str | None
    ats: str
    category: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "company": self.company,
            "title": self.title,
            "location": self.location,
            "url": self.url,
            "posted_at": self.posted_at,
            "department": self.department,
            "ats": self.ats,
            "category": self.category,
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
