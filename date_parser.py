"""Normalize posted-date values across ATSes to YYYY-MM-DD strings.

Each ATS encodes posted/updated dates differently:
  - Greenhouse  -> ISO8601 string "2026-05-20T22:00:00-04:00"
  - Lever       -> epoch milliseconds (int)
  - Ashby       -> ISO8601 string "2026-05-20T22:00:00Z"
  - Workday     -> human strings ("Posted Today", "Posted 5 Days Ago",
                   "Posted 30+ Days Ago", sometimes a date)
  - LinkedIn    -> relative strings ("2 days ago", "1 week ago") or
                   "May 24, 2026" from guest search cards

`parse_posted_date(raw, ats)` returns a normalized ISO date (YYYY-MM-DD)
or None when we can't extract one.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Any

_WORKDAY_REL = re.compile(
    r"posted\s+(today|yesterday|(\d+)\+?\s+(day|week|month)s?\s+ago)",
    re.IGNORECASE,
)

_LINKEDIN_REL = re.compile(
    r"(?:"
    r"(?P<n>\d+)\+?\s+(?P<unit>second|minute|hour|day|week|month|year)s?\s+ago|"
    r"(?P<fixed>just\s+now|today|yesterday)"
    r")",
    re.IGNORECASE,
)

_LINKEDIN_MONTH_DAY = re.compile(
    r"\b([A-Za-z]{3,9})\s+(\d{1,2}),?\s+(\d{4})\b"
)

_MONTH_FORMATS = ("%B %d %Y", "%B %d, %Y", "%b %d %Y", "%b %d, %Y")


def _parse_iso(s: str) -> str | None:
    """Best-effort ISO8601 -> YYYY-MM-DD."""
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except (ValueError, AttributeError):
        # Try date-only formats
        for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%B %d, %Y"):
            try:
                return datetime.strptime(s.strip(), fmt).date().isoformat()
            except ValueError:
                continue
    return None


def _parse_workday(raw: str, ref: datetime) -> str | None:
    if not raw:
        return None
    s = raw.strip()
    m = _WORKDAY_REL.search(s)
    if not m:
        # Some Workday installs return a real date instead — fall through.
        return _parse_iso(s)
    body = m.group(1).lower()
    if body == "today":
        return ref.date().isoformat()
    if body == "yesterday":
        return (ref - timedelta(days=1)).date().isoformat()
    n = int(m.group(2))
    unit = m.group(3).lower()
    if unit == "day":
        return (ref - timedelta(days=n)).date().isoformat()
    if unit == "week":
        return (ref - timedelta(weeks=n)).date().isoformat()
    if unit == "month":
        # ~30-day month approximation; sufficient for Vansh-style "Date Posted".
        return (ref - timedelta(days=n * 30)).date().isoformat()
    return None


def _parse_linkedin_month_day(raw: str) -> str | None:
    m = _LINKEDIN_MONTH_DAY.search(raw.strip())
    if not m:
        return None
    month_s, day_s, year_s = m.group(1), m.group(2), m.group(3)
    for text in (f"{month_s} {day_s}, {year_s}", f"{month_s} {day_s} {year_s}"):
        for fmt in _MONTH_FORMATS:
            try:
                return datetime.strptime(text, fmt).date().isoformat()
            except ValueError:
                continue
    return None


def _parse_linkedin_relative(raw: str, ref: datetime) -> str | None:
    s = raw.strip()
    if not s:
        return None
    fixed = s.lower()
    if fixed in {"just now", "today"}:
        return ref.date().isoformat()
    if fixed == "yesterday":
        return (ref - timedelta(days=1)).date().isoformat()

    m = _LINKEDIN_REL.search(s)
    if not m:
        return None
    if m.group("fixed"):
        word = m.group("fixed").lower()
        if word == "yesterday":
            return (ref - timedelta(days=1)).date().isoformat()
        return ref.date().isoformat()

    n = int(m.group("n"))
    unit = (m.group("unit") or "day").lower()
    if unit in {"second", "minute", "hour"}:
        return ref.date().isoformat()
    if unit == "day":
        return (ref - timedelta(days=n)).date().isoformat()
    if unit == "week":
        return (ref - timedelta(weeks=n)).date().isoformat()
    if unit == "month":
        return (ref - timedelta(days=n * 30)).date().isoformat()
    if unit == "year":
        return (ref - timedelta(days=n * 365)).date().isoformat()
    return None


def _parse_linkedin(raw: str, ref: datetime) -> str | None:
    if not raw:
        return None
    iso = _parse_iso(raw)
    if iso:
        return iso
    absolute = _parse_linkedin_month_day(raw)
    if absolute:
        return absolute
    return _parse_linkedin_relative(raw, ref)


def parse_posted_date(
    raw: Any,
    ats: str,
    ref: datetime | None = None,
) -> str | None:
    """Normalize a raw posted-date field from any ATS to YYYY-MM-DD.

    Returns None when no usable date can be extracted.
    """
    if raw is None or raw == "":
        return None
    now = ref or datetime.now(timezone.utc)

    if ats == "lever":
        try:
            ms = int(raw)
            return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).date().isoformat()
        except (ValueError, TypeError):
            return None

    if ats == "workday":
        return _parse_workday(str(raw), now)

    if ats == "linkedin":
        return _parse_linkedin(str(raw), now)

    # Greenhouse, Ashby, and any other ATS that returns ISO8601.
    if isinstance(raw, str):
        return _parse_iso(raw)
    return None
