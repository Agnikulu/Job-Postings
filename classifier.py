"""Regex-only job classification.

Pipeline:
  1. `is_obvious_reject()` — drop titles never EC technical targets.
  2. `classify_title_confidence()` — include only on high-confidence matches.
  3. US location gate (unless ATS_SNIPER_ALL_LOCATIONS=1).
"""

from __future__ import annotations

from dataclasses import dataclass

from adapters.base import Job
from education import extract_education_levels
from description_signals import extract_requirements_text
from filters import classify_title_confidence, is_obvious_reject, is_us_location
from location_resolver import resolve_job_location


@dataclass(frozen=True)
class JobClassification:
    include: bool
    is_technical: bool
    education_levels: tuple[str, ...]
    is_us: bool
    reason: str | None
    source: str  # prefilter | regex


def _prefilter_reject(title: str) -> JobClassification:
    return JobClassification(
        include=False,
        is_technical=False,
        education_levels=(),
        is_us=False,
        reason="obvious non-target title",
        source="prefilter",
    )


def classify_job_fields(
    *,
    company: str,
    title: str,
    location: str | None,
    url: str | None = None,
    description: str | None = None,
    us_only: bool = True,
) -> JobClassification:
    """Classify a single posting by title, description, and location."""
    del company, url  # reserved for future company-specific rules

    if is_obvious_reject(title):
        return _prefilter_reject(title or "")

    resolved_location = (location or "").strip()
    confidence = classify_title_confidence(title, description)
    include = confidence.level == "high_include"

    req = extract_requirements_text(description)
    search_text = " ".join(p for p in (title, req) if p)
    levels = tuple(extract_education_levels(search_text)) if include else ()

    result = JobClassification(
        include=include,
        is_technical=confidence.is_technical,
        education_levels=levels,
        is_us=is_us_location(resolved_location),
        reason=confidence.reason,
        source="regex",
    )

    if us_only and result.include and not result.is_us:
        return JobClassification(
            include=False,
            is_technical=result.is_technical,
            education_levels=(),
            is_us=False,
            reason="non-US location",
            source="regex",
        )
    return result


def classify_job(
    job: Job,
    *,
    us_only: bool = True,
) -> JobClassification:
    resolved = resolve_job_location(job)
    return classify_job_fields(
        company=job.company,
        title=job.title,
        location=resolved,
        url=job.url,
        description=job.description,
        us_only=us_only,
    )
