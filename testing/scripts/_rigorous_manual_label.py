"""Rigorous manual (human-rubric) labeling for cursor eval.

Applies the same criteria used in prior manual Cursor labeling sessions:
  include ONLY if BOTH early-career AND technical (SWE/ML/DS/quant/firmware/embedded/hardware).

Usage:
    python _rigorous_manual_label.py
    python _cursor_manual_eval.py score
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from description_signals import (
    extract_description_signals_with_fallback,
    extract_requirements_text,
    qualifying_early_years,
    ec_friendly_requirements_header,
    effective_strong_ec,
)
from filters import (
    DOMAIN,
    TARGET,
    WEAK_EARLY_CAREER_SIGNALS,
    is_obvious_reject,
    obvious_reject_reason,
    _title_ec_target,
    _MTS_TITLE,
    _OBVIOUS_NON_TECH,
    _OBVIOUS_SENIOR,
    _OBVIOUS_LEAD,
    _OBVIOUS_STAFF_SENIOR,
    _HARDWARE_INTERN,
    _RESEARCH_EC_TITLE,
    _FELLOWSHIP_TITLE,
    _POST_TRAINING,
    _RECRUITER_TITLE,
    _NON_ENGINEERING_FELLOW,
    _BACHELORS_PLUS_YEARS,
    _is_technical_intern,
    _title_ec_hint,
)

EVAL_DIR = Path(__file__).resolve().parents[1] / "eval"
JOBS_PATH = EVAL_DIR / "cursor_eval_jobs.jsonl"
LABELS_PATH = EVAL_DIR / "cursor_eval_labels.jsonl"

# Manual-only excludes (stricter than regex)
_GROUP_LEADER = re.compile(
    r"\b(?:group\s+leader|principal\s+investigator|\bpi\b)\b",
    re.IGNORECASE,
)
_FOUNDING_SENIOR = re.compile(
    r"\bfounding\s+(?:engineer|developer|scientist)\b",
    re.IGNORECASE,
)
_SALES_BDR = re.compile(
    r"\b(?:bdr|sdr|business\s+development|sales\s+development|account\s+executive|"
    r"go-?to-?market|gtm|capital\s+markets|talent\s+acquisition|recruiting)\b",
    re.IGNORECASE,
)
_WET_LAB = re.compile(
    r"\b(?:wet\s+lab|bench\s+scientist|laboratory\s+technician|"
    r"clinical\s+research\s+coordinator)\b",
    re.IGNORECASE,
)
_SENIOR_FELLOW = re.compile(
    r"\b(?:human\s+frontier\s+collective|hfc)\b",
    re.IGNORECASE,
)
_FIELD_ENGINEER = re.compile(
    r"\b(?:field\s+engineer|solutions?\s+engineer|sales\s+engineer|"
    r"customer\s+engineer|technical\s+account\s+manager)\b",
    re.IGNORECASE,
)
_POST_TRAINING_RESEARCH = re.compile(
    r"\bpost-?training\b.*\b(?:research\s+scientist|research\s+engineer)\b|"
    r"\b(?:research\s+scientist|research\s+engineer).*\bpost-?training\b",
    re.IGNORECASE,
)
_NEW_GRAD_WELCOME = re.compile(
    r"\b(?:new\s+grad(?:uate)?s?\s+welcome|welcome\s+new\s+grad|"
    r"no\s+prior\s+(?:work\s+)?experience|0\s+years?\s+experience|"
    r"recent\s+grad(?:uate)?s?\s+(?:welcome|encouraged))\b",
    re.IGNORECASE,
)
_GRAD_YEAR = re.compile(r"\b(?:graduate|graduating|class\s+of)\s+20[2-9][0-9]\b", re.I)
_ENGINEER_III = re.compile(r"\bengineer\s+iii\b", re.I)


def _is_technical(title: str, desc: str | None, desc_sig) -> bool:
    if DOMAIN.search(title):
        return True
    req = desc_sig.requirements_text or ""
    if req and DOMAIN.search(req):
        return True
    if desc_sig.has_tech_field:
        return True
    if desc and _HARDWARE_INTERN.search(desc):
        return True
    if _RESEARCH_EC_TITLE.search(title) and (desc_sig.has_tech_field or DOMAIN.search(title)):
        return True
    return False


def _has_senior_bar(title: str, positive: str, desc_sig) -> bool:
    if _OBVIOUS_SENIOR.search(title) and not re.search(r"\bintern", title, re.I):
        return True
    if _OBVIOUS_STAFF_SENIOR.search(title):
        return True
    if _OBVIOUS_LEAD.search(title) and not re.search(r"\bintern", title, re.I):
        return True
    if _ENGINEER_III.search(title):
        return True
    if desc_sig.has_senior_exp or desc_sig.has_min_years_req:
        return True
    if _BACHELORS_PLUS_YEARS.search(positive):
        return True
    return False


def _early_career_signal(title: str, positive: str, desc_sig, description: str | None) -> tuple[bool, str]:
    if _title_ec_target(title):
        return True, "explicit ec title"
    if TARGET.search(positive) and not _MTS_TITLE.search(title):
        return True, "ec keyword in title/requirements"
    if effective_strong_ec(desc_sig):
        return True, "strong ec in requirements"
    if qualifying_early_years(
        positive,
        title,
        ec_friendly_header=ec_friendly_requirements_header(desc_sig.requirements_text),
    ):
        return True, "qualifying early years"
    if WEAK_EARLY_CAREER_SIGNALS.search(title) and (
        effective_strong_ec(desc_sig) or desc_sig.has_ec and not desc_sig.has_senior_exp
    ):
        return True, "weak ec title + ec requirements"
    if _GRAD_YEAR.search(title):
        return True, "grad year in title"
    if description and _NEW_GRAD_WELCOME.search(description):
        return True, "new grads welcome"
    if re.search(r"\bintern(ship)?\b", title, re.I):
        return True, "intern title"
    if _FELLOWSHIP_TITLE.search(title):
        if effective_strong_ec(desc_sig) and not desc_sig.has_senior_exp:
            return True, "technical fellowship"
        return False, ""
    if _POST_TRAINING.search(title) and effective_strong_ec(desc_sig):
        return True, "post-training program"
    return False, ""


def manual_judge(
    *,
    company: str,
    title: str,
    location: str | None,
    description: str | None,
) -> tuple[bool, str]:
    del company, location
    title = (title or "").strip()
    if not title:
        return False, "empty title"

    if is_obvious_reject(title):
        return False, obvious_reject_reason(title) or "prefilter"

    if _GROUP_LEADER.search(title):
        return False, "group leader/PI role"
    if _RECRUITER_TITLE.search(title) or _NON_ENGINEERING_FELLOW.search(title):
        return False, "non-engineering role"
    if _OBVIOUS_NON_TECH.search(title) or _SALES_BDR.search(title):
        return False, "non-tech/sales role"
    if _WET_LAB.search(title):
        return False, "wet lab/non-SWE role"
    if _FOUNDING_SENIOR.search(title):
        return False, "founding senior role"
    if _FIELD_ENGINEER.search(title):
        return False, "customer-facing/solutions role"
    if _POST_TRAINING_RESEARCH.search(title):
        return False, "senior post-training research role"
    if _SENIOR_FELLOW.search(title) or (description and _SENIOR_FELLOW.search(description)):
        return False, "expert fellowship (PhD/postdoc/5+ yr bar)"

    desc_sig = extract_description_signals_with_fallback(
        description,
        title_ec_hint=_title_ec_hint(title),
    )
    req_text = extract_requirements_text(description)
    positive = " ".join(p for p in (title, req_text) if p)

    # Internships: must be technical
    if re.search(r"\bintern(ship)?\b", title, re.I) and not DOMAIN.search(title):
        if _is_technical_intern(title, description, desc_sig):
            return True, "technical intern"
        return False, "non-technical intern"

    # MTS: experienced unless intern/new-grad welcome
    if _MTS_TITLE.search(title) and not re.search(r"\bintern", title, re.I):
        if _NEW_GRAD_WELCOME.search(description or "") or _GRAD_YEAR.search(title):
            if _is_technical(title, description, desc_sig):
                return True, "MTS new-grad welcome"
        if effective_strong_ec(desc_sig) and not desc_sig.has_senior_exp:
            if _is_technical(title, description, desc_sig):
                return True, "MTS with ec requirements"
        return False, "experienced MTS IC"

    is_tech = _is_technical(title, description, desc_sig)
    if not is_tech:
        return False, "non-technical role"

    if _has_senior_bar(title, positive, desc_sig):
        ec, ec_reason = _early_career_signal(title, positive, desc_sig, description)
        if ec and effective_strong_ec(desc_sig):
            # Strong EC can override ambiguous senior signals (e.g. 1-3 yr range)
            if qualifying_early_years(positive, title, ec_friendly_header=ec_friendly_requirements_header(desc_sig.requirements_text)):
                return True, f"ec overrides senior bar ({ec_reason})"
        return False, "senior experience required"

    ec, ec_reason = _early_career_signal(title, positive, desc_sig, description)
    if ec:
        return True, ec_reason

    # Engineer I/II / junior without explicit senior bar — must be technical title
    if WEAK_EARLY_CAREER_SIGNALS.search(title) and not desc_sig.has_senior_exp:
        if not desc_sig.has_min_years_req and _is_technical(title, description, desc_sig):
            if re.search(r"\bassociate\b", title, re.I):
                if not re.search(
                    r"\b(?:engineer|developer|scientist|analyst|researcher|architect)\b",
                    title,
                    re.I,
                ):
                    return False, "non-technical associate role"
            if _OBVIOUS_STAFF_SENIOR.search(title) or re.search(r"\bstaff\b", title, re.I):
                return False, "staff-level role"
            return True, "early-career level title, no senior bar"

    # Research scientist with degree req only
    if _RESEARCH_EC_TITLE.search(title) and desc_sig.has_bachelors_req and not desc_sig.has_senior_exp:
        return True, "research role, degree requirements only"

    if not description or not description.strip():
        return False, "no description to verify ec"
    if not desc_sig.requirements_text and not effective_strong_ec(desc_sig):
        return False, "no ec signal in requirements"

    return False, "technical but not early-career"


def main() -> int:
    if not JOBS_PATH.exists():
        print(f"Missing {JOBS_PATH.name}", file=sys.stderr)
        return 1

    jobs = [json.loads(line) for line in JOBS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    include_count = 0
    with LABELS_PATH.open("w", encoding="utf-8") as fh:
        for job in jobs:
            inc, reason = manual_judge(
                company=job["company"],
                title=job["title"],
                location=job.get("location"),
                description=job.get("description"),
            )
            if inc:
                include_count += 1
            row = {
                "url": job["url"],
                "manual_include": inc,
                "manual_reason": reason,
            }
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Labeled {len(jobs)} jobs -> {LABELS_PATH.name}")
    print(f"manual_include=true: {include_count} ({100*include_count/len(jobs):.2f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
