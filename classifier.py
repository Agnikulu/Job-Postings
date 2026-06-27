"""Regex-only job classification.

Pipeline:
  1. `is_obvious_reject()` — drop titles never EC technical targets.
  2. `classify_title_confidence()` — include only on high-confidence matches.
  3. Intern + SWE-only post-filters (configurable, on by default).
  4. US location gate (unless ATS_SNIPER_ALL_LOCATIONS=1).

Environment toggles:
  ATS_SNIPER_DROP_INTERNS=0   — keep intern/co-op titles (default: drop)
  ATS_SNIPER_SWE_ONLY=0       — keep non-software disciplines (default: SWE-only)
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from adapters.base import Job
from education import extract_education_levels
from description_signals import extract_requirements_text
from filters import (
    classify_title_confidence,
    is_intern_only,
    is_obvious_reject,
    is_software_or_ai_role,
    is_us_location_with_description,
)
from location_resolver import resolve_job_location


def _drop_interns_enabled() -> bool:
    return os.environ.get("ATS_SNIPER_DROP_INTERNS", "1").strip() != "0"


def _swe_only_enabled() -> bool:
    return os.environ.get("ATS_SNIPER_SWE_ONLY", "1").strip() != "0"


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
    drop_interns: bool | None = None,
    swe_only: bool | None = None,
) -> JobClassification:
    """Classify a single posting by title, description, and location.

    `drop_interns` defaults to `ATS_SNIPER_DROP_INTERNS` (on unless set to "0").
    `swe_only` defaults to `ATS_SNIPER_SWE_ONLY` (on unless set to "0").
    """
    if is_obvious_reject(title):
        return _prefilter_reject(title or "")

    if drop_interns is None:
        drop_interns = _drop_interns_enabled()
    if swe_only is None:
        swe_only = _swe_only_enabled()

    if drop_interns and is_intern_only(title):
        return JobClassification(
            include=False,
            is_technical=False,
            education_levels=(),
            is_us=False,
            reason="intern-only role (new-grad/full-time only)",
            source="prefilter",
        )

    resolved_location = (location or "").strip()
    confidence = classify_title_confidence(
        title,
        description,
        company=company,
        url=url,
    )
    include = confidence.level == "high_include"

    if include and swe_only and not is_software_or_ai_role(title):
        return JobClassification(
            include=False,
            is_technical=confidence.is_technical,
            education_levels=(),
            is_us=False,
            reason="non-software discipline (cs/swe/ai-ml only)",
            source="regex",
        )

    req = extract_requirements_text(description)
    levels = (
        tuple(
            extract_education_levels(
                title,
                requirements_text=req,
                description=description,
            )
        )
        if include
        else ()
    )

    result = JobClassification(
        include=include,
        is_technical=confidence.is_technical,
        education_levels=levels,
        is_us=is_us_location_with_description(resolved_location, description),
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
    drop_interns: bool | None = None,
    swe_only: bool | None = None,
) -> JobClassification:
    resolved = resolve_job_location(job)
    return classify_job_fields(
        company=job.company,
        title=job.title,
        location=resolved,
        url=job.url,
        description=job.description,
        us_only=us_only,
        drop_interns=drop_interns,
        swe_only=swe_only,
    )
