"""Regex filter engine.

  1. `is_obvious_reject(title)` — ultra-conservative pre-filter.
  2. `classify_title_confidence()` — high-confidence include/exclude.
  3. `classify(title)` — title-level pass/fail helper for review tools.

Also provides US location matching via `is_us_location(loc)`.

`diagnose_weak_signal(title)` powers the --diagnose tool in review.py.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from description_signals import (
    DESC_STRONG_EC,
    DescriptionSignals,
    extract_description_signals,
    extract_requirements_text,
)

ConfidenceLevel = Literal["high_include", "high_exclude", "borderline"]

# =============================================================================
# Title filters
# =============================================================================

TARGET = re.compile(
    r"\b("
    r"intern(ship)?|co-?op|new[\s-]?grad(uate)?|new\s+college\s+grad|"
    r"university\s+graduate|"
    r"early[\s-]career(?:s)?|entry[\s-]level|campus|"
    r"apprentice|trainee|recent\s+graduate|"
    r"member\s+of\s+technical\s+staff|\bmts\b|"
    r"engineer\s+i[i]?|engineer\s+[123]|"
    r"junior|jr\.?|"
    r"fellow(?:ship)?|"
    r"resident(?:cy)?|"
    r"202[4-9]"
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
    # Core software / engineering
    r"software|engineer(ing)?|"
    r"backend|frontend|full[\s-]?stack|"
    r"infrastructure|platform|systems|"
    # Data + ML + AI
    r"machine[\s-]learning|ml|"
    r"data(\s+(scientist|engineer|analyst))?|"
    r"ai|artificial\s+intelligence|"
    r"applied\s+scientist|research\s+scientist|scientist|deep\s+learning|"
    r"inference|llm|generative|"
    # Research / quant
    r"quant(itative)?|research|"
    r"technical\s+staff|"
    r"computer\s+science|cs|"
    # Hardware / chip / firmware (added in v2)
    r"firmware|embedded|hardware|"
    r"chip|asic|fpga|silicon|vlsi|"
    r"rtl|verification|dft|dv|"
    r"circuit|gpu|cuda|kernel|compiler|"
    r"architect|simulation|semiconductor"
    r")\b",
    re.IGNORECASE,
)

# Weak signals for the diagnostic mode. These are NOT used by classify()
# because they're too noisy to gate alerts on, but they help the human
# auditor spot companies that might be using non-standard early-career
# titles (e.g., Anthropic's "Member of Technical Staff", "Engineer I",
# residency programs).
# Early-career cues — if present, never pre-filter.
_PREFILTER_EARLY_CAREER = re.compile(
    r"\b("
    r"intern(ship)?|co-?op|new[\s-]?grad(uate)?|university\s+graduate|"
    r"early[\s-]career|entry[\s-]level|campus|apprentice|trainee|"
    r"202[4-9]"
    r")\b",
    re.IGNORECASE,
)

# Ambiguous titles — never pre-filter; full classify decides.
_PREFILTER_NEVER_REJECT = re.compile(
    r"\b("
    r"member\s+of\s+technical\s+staff|"
    r"\bmts\b|"
    r"engineer\s+i[i]?|engineer\s+[123]|"
    r"junior|jr\.?"
    r")\b",
    re.IGNORECASE,
)

_MTS_TITLE = re.compile(
    r"\bmember\s+of\s+technical\s+staff|\bmts\b",
    re.IGNORECASE,
)

# Hardware / silicon intern titles without "software" in the name.
_HARDWARE_INTERN = re.compile(
    r"\b("
    r"mech(?:anical)?|thermal|chipsim|chip\s*sim|physical\s+design|\bpd\b|"
    r"mechatronics|asic|silicon|semiconductor|rtl|verification|\bdft\b|\bdv\b|"
    r"firmware|embedded|hardware|chip|gpu|layout|analog|mixed[\s-]?signal"
    r")\b",
    re.IGNORECASE,
)

_GENERIC_INTERNSHIP_TITLE = re.compile(
    r"^(?:internship(?:\s+program)?|intern(?:\s+program)?)\s*$",
    re.IGNORECASE,
)

_OBVIOUS_SENIOR = re.compile(
    r"\b("
    r"senior|sr\.?|principal|director|"
    r"manager|head\s+of|"
    r"vp|vice\s+president|president"
    r")\b",
    re.IGNORECASE,
)

_OBVIOUS_STAFF_SENIOR = re.compile(
    r"\bstaff\s+(?:software|machine|ml|data|platform|systems|backend|"
    r"frontend|full[\s-]?stack|research|infrastructure|security|"
    r"site\s+reliability|devops|sre|hardware|firmware|embedded)\b",
    re.IGNORECASE,
)

_OBVIOUS_LEAD = re.compile(
    r"\b(?:"
    r"(?:lead|leading)\s+(?:software|engineer|developer|architect|"
    r"data|ml|machine\s+learning|ai|platform|infrastructure|research)|"
    r"(?:implementation|integration|engineering|technical|product)\s+lead"
    r")\b",
    re.IGNORECASE,
)

# Unmistakably non-technical — never SWE/DS/AI-ML intern or new grad targets.
_OBVIOUS_NON_TECH = re.compile(
    r"\b("
    r"(?:campus\s+)?recruiting(?:\s+specialist|\s+coordinator|\s+manager)?|"
    r"talent\s+(?:acquisition|partner|coordinator)|"
    r"human\s+resources|\bhr\s+(?:generalist|business\s+partner|coordinator)|"
    r"(?:marketing|sales|account)\s+(?:intern|manager|director|coordinator|"
    r"representative|specialist)|"
    r"business\s+development\s+representative|"
    r"(?:strategic\s+)?sales\s+development\s+representative|"
    r"legal\s+(?:counsel|intern)|"
    r"(?:corporate|tax|financial)\s+accountant|"
    r"paralegal|"
    r"retail\s+(?:specialist|expert)|"
    r"store\s+(?:manager|leader)"
    r")\b",
    re.IGNORECASE,
)

WEAK_EARLY_CAREER_SIGNALS = re.compile(
    r"\b("
    r"engineer\s+i|engineer\s+1|"
    r"engineer\s+ii|engineer\s+2|"
    r"member\s+of\s+technical\s+staff|"
    r"mts|"
    r"resident(?:cy)?|"
    r"residency|"
    r"associate(?!\s+(?:professor|director|partner))|"
    r"l[1-3]|p[1-3]|"
    r"trainee|apprentice|"
    r"junior|jr\.?|"
    r"recent\s+graduate"
    r")\b",
    re.IGNORECASE,
)


def is_obvious_reject(title: str | None) -> bool:
    """Return True only for titles that are never early-career technical targets.

    Conservative by design — when in doubt, returns False so the LLM decides.
    """
    if not title or not title.strip():
        return True
    text = title.strip()

    if _PREFILTER_NEVER_REJECT.search(text):
        return False

    if _OBVIOUS_NON_TECH.search(text):
        return True

    if _PREFILTER_EARLY_CAREER.search(text):
        return False

    if _OBVIOUS_SENIOR.search(text):
        return True
    if _OBVIOUS_STAFF_SENIOR.search(text):
        return True
    if _OBVIOUS_LEAD.search(text):
        return True

    return False


def obvious_reject_reason(title: str | None) -> str | None:
    """Return why a title was pre-filtered, or None if it passes to the LLM."""
    if not title or not title.strip():
        return "empty title"
    text = title.strip()

    if _PREFILTER_NEVER_REJECT.search(text):
        return None
    if _OBVIOUS_NON_TECH.search(text):
        return "non-tech"
    if _PREFILTER_EARLY_CAREER.search(text):
        return None
    if _OBVIOUS_SENIOR.search(text):
        return "senior/management"
    if _OBVIOUS_STAFF_SENIOR.search(text):
        return "staff-level"
    if _OBVIOUS_LEAD.search(text):
        return "lead"
    return None


def is_suspicious_prefilter_reject(title: str | None) -> bool:
    """True when pre-filter dropped a title that may still be a relevant EC tech role."""
    if not is_obvious_reject(title):
        return False
    if not title:
        return False
    # Should never happen — always-LLM titles must not reject.
    if _PREFILTER_NEVER_REJECT.search(title):
        return True
    if not DOMAIN.search(title):
        return False
    if _PREFILTER_EARLY_CAREER.search(title):
        return True
    if WEAK_EARLY_CAREER_SIGNALS.search(title):
        return True
    return False


def _anti_safe_title(title: str) -> str:
    """Prevent MTS titles from tripping the \\bstaff\\b ANTI keyword."""
    return re.sub(
        r"\bmember\s+of\s+technical\s+staff\b",
        "member of technical mts",
        title,
        flags=re.IGNORECASE,
    )


def _classification_context(
    title: str | None,
    description: str | None = None,
) -> tuple[str, str | None, DescriptionSignals]:
    """Build title text, requirements slice, and parsed description signals."""
    title_text = (title or "").strip()
    req_text = extract_requirements_text(description)
    desc_signals = extract_description_signals(description)
    return title_text, req_text, desc_signals


def _positive_text(title: str, req_text: str | None) -> str:
    """Title + requirements section for EC/technical positive matching."""
    parts = [p for p in (title, req_text) if p and p.strip()]
    return " ".join(parts)


def _has_anti(title: str) -> bool:
    return bool(ANTI.search(_anti_safe_title(title)))


def _title_ec_target(title: str) -> bool:
    """True when the title itself carries an early-career signal.

    Bare \"Member of Technical Staff\" alone is treated as experienced at most
    companies — not an EC title cue unless paired with intern/new-grad/etc.
    """
    if not TARGET.search(title):
        return False
    if _MTS_TITLE.search(title) and not re.search(
        r"\bintern(ship)?\b|co-?op|new[\s-]?grad|202[4-9]|engineer\s+i[i]?|engineer\s+[123]",
        title,
        re.IGNORECASE,
    ):
        return False
    return True


def _is_hardware_intern_title(title: str) -> bool:
    return bool(
        re.search(r"\bintern(ship)?\b|co-?op\b", title, re.IGNORECASE)
        and _HARDWARE_INTERN.search(title)
    )


def _is_technical_intern(
    title: str,
    description: str | None,
    desc_sig: DescriptionSignals,
) -> bool:
    if _is_hardware_intern_title(title):
        return True
    if desc_sig.has_tech_field or (desc_sig.requirements_text and DOMAIN.search(desc_sig.requirements_text)):
        return True
    if description and _HARDWARE_INTERN.search(description):
        return True
    return False


@dataclass(frozen=True)
class TitleConfidence:
    level: ConfidenceLevel
    is_technical: bool
    reason: str | None = None


def classify_title_confidence(
    title: str | None,
    description: str | None = None,
) -> TitleConfidence:
    """Classify title confidence for hybrid regex + LLM routing.

    Positive signals search title + requirements section (not full description).
    DESC_EC / degree-field patterns catch bullets like "PhD candidate" or
    "Previous internship experience". Senior excludes stay title-only; senior
    experience *requirements* can demote when no EC cue exists.
    """
    if not title or not title.strip():
        return TitleConfidence("high_exclude", False, "empty title")

    title_text, req_text, desc_sig = _classification_context(title, description)
    positive_text = _positive_text(title_text, req_text)

    title_tech = bool(DOMAIN.search(title_text))
    req_tech = bool(
        (req_text and DOMAIN.search(req_text))
        or desc_sig.has_tech_field
    )
    is_tech = title_tech or req_tech

    if _OBVIOUS_NON_TECH.search(title_text):
        return TitleConfidence("high_exclude", False, "non-tech")

    if _OBVIOUS_SENIOR.search(title_text) and not re.search(
        r"\bintern(ship)?\b", title_text, re.IGNORECASE
    ):
        return TitleConfidence("high_exclude", False, "senior keyword")

    if _OBVIOUS_LEAD.search(title_text) and not re.search(
        r"\bintern(ship)?\b", title_text, re.IGNORECASE
    ):
        return TitleConfidence("high_exclude", False, "senior keyword")

    if re.search(r"\bintern(ship)?\b", title_text, re.IGNORECASE) and not title_tech:
        if _is_technical_intern(title_text, description, desc_sig):
            return TitleConfidence("high_include", True, "technical intern")
        return TitleConfidence("high_exclude", False, "non-technical intern")

    if _GENERIC_INTERNSHIP_TITLE.match(title_text.strip()):
        if _is_technical_intern(title_text, description, desc_sig):
            return TitleConfidence("high_include", True, "technical intern program")
        return TitleConfidence("high_exclude", False, "non-technical intern")

    if re.search(r"\binternship\s+program\b", title_text, re.IGNORECASE) and not title_tech:
        if _is_technical_intern(title_text, description, desc_sig):
            return TitleConfidence("high_include", True, "technical intern program")
        return TitleConfidence("high_exclude", False, "non-technical intern")

    if re.search(r"\barchitect\b", title_text, re.IGNORECASE) and not desc_sig.has_strong_ec:
        return TitleConfidence("high_exclude", False, "senior keyword")

    has_target = bool(
        _title_ec_target(title_text)
        or (req_text and TARGET.search(req_text))
        or desc_sig.has_ec
    )
    has_weak = bool(WEAK_EARLY_CAREER_SIGNALS.search(positive_text))

    if _MTS_TITLE.search(title_text) and not re.search(
        r"\bintern(ship)?\b", title_text, re.IGNORECASE
    ):
        if not (
            desc_sig.has_strong_ec
            or desc_sig.has_ec
            or _PREFILTER_EARLY_CAREER.search(title_text)
        ):
            if desc_sig.has_senior_exp or desc_sig.has_min_years_req:
                return TitleConfidence("high_exclude", True, "experienced mts role")
            return TitleConfidence("high_exclude", True, "experienced mts title")

    if _has_anti(title_text) and not (
        _PREFILTER_EARLY_CAREER.search(positive_text) or desc_sig.has_strong_ec
    ):
        return TitleConfidence("high_exclude", False, "senior keyword")

    if desc_sig.has_senior_exp and not desc_sig.has_strong_ec:
        return TitleConfidence("high_exclude", False, "senior experience required")

    if (
        desc_sig.has_bachelors_req
        and not desc_sig.has_strong_ec
        and desc_sig.has_min_years_req
        and is_tech
        and not _PREFILTER_EARLY_CAREER.search(title_text)
    ):
        return TitleConfidence("high_exclude", True, "minimum experience required")

    if has_target and is_tech:
        if not (
            title_tech
            or desc_sig.has_strong_ec
            or desc_sig.has_tech_field
        ):
            return TitleConfidence("high_exclude", False, "ec but non-technical title")
        if (
            _title_ec_target(title_text)
            and not title_tech
            and not desc_sig.has_strong_ec
        ):
            return TitleConfidence("high_exclude", False, "ec but non-technical title")
        reason = (
            "explicit ec technical (requirements)"
            if desc_sig.has_ec and not TARGET.search(title_text)
            else "explicit ec technical"
        )
        return TitleConfidence("high_include", True, reason)

    if has_target and not is_tech:
        return TitleConfidence("borderline", False, "ec but non-technical title")

    if is_tech and has_weak:
        if _MTS_TITLE.search(title_text) and not re.search(
            r"\bintern(ship)?\b", title_text, re.IGNORECASE
        ) and not desc_sig.has_strong_ec:
            return TitleConfidence("high_exclude", True, "experienced mts title")
        if re.search(r"\bassociate\b", positive_text, re.IGNORECASE) and not re.search(
            r"\b(engineer|developer|scientist|analyst|researcher)\b",
            positive_text,
            re.IGNORECASE,
        ):
            return TitleConfidence("borderline", True, "associate title")
        return TitleConfidence("high_include", True, "implicit ec technical")

    if is_tech and desc_sig.has_ec:
        return TitleConfidence("high_include", True, "requirements ec technical")

    if is_tech:
        if desc_sig.requirements_text and not desc_sig.has_ec:
            return TitleConfidence("high_exclude", True, "no ec in requirements")
        if not description or not description.strip():
            return TitleConfidence("high_exclude", True, "no description")
        if not desc_sig.requirements_text:
            if desc_sig.has_ec or DESC_STRONG_EC.search(description):
                return TitleConfidence("high_include", True, "description ec technical")
            return TitleConfidence("high_exclude", True, "unparsed requirements")
        return TitleConfidence("high_exclude", True, "bare technical title")

    return TitleConfidence("high_exclude", False, "no ec or technical signal")


def classify(
    title: str,
    description: str | None = None,
) -> tuple[bool, bool]:
    """Return (passes, is_technical) — only high-confidence includes pass."""
    if not title:
        return (False, False)
    conf = classify_title_confidence(title, description)
    if conf.level == "high_include":
        return (True, conf.is_technical)
    return (False, conf.is_technical if conf.is_technical else False)


def diagnose_weak_signal(title: str) -> str | None:
    """Return the first weak early-career signal in `title`, or None.

    For diagnostic use only — these are signals that the main TARGET regex
    is intentionally NOT matching to avoid false positives, but which may
    indicate a legit early-career role at companies that use non-standard
    titles. Run `python review.py --diagnose` to see them.

    NOTE: We deliberately do NOT gate on ANTI here. Anthropic's
    "Member of Technical Staff" contains "staff" (an ANTI keyword) but is
    exactly the kind of title we want surfaced for human review.
    """
    if not title:
        return None
    m = WEAK_EARLY_CAREER_SIGNALS.search(title)
    return m.group(0).lower() if m else None


# =============================================================================
# Location filter (US-only by default)
# =============================================================================

US_INDICATOR = re.compile(
    r"\b("
    r"united\s+states|"
    r"u\.?\s?s\.?\s?a\.?|"
    r"u\.?s\.?(?!\w)|"
    # Full state names
    r"alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|"
    r"florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|"
    r"louisiana|maine|maryland|massachusetts|michigan|minnesota|mississippi|"
    r"missouri|montana|nebraska|nevada|new\s+hampshire|new\s+jersey|"
    r"new\s+mexico|new\s+york|north\s+carolina|north\s+dakota|ohio|oklahoma|"
    r"oregon|pennsylvania|rhode\s+island|south\s+carolina|south\s+dakota|"
    r"tennessee|texas|utah|vermont|virginia|washington|west\s+virginia|"
    r"wisconsin|wyoming|district\s+of\s+columbia"
    r")\b",
    re.IGNORECASE,
)

# Two-letter state codes — only matched after a comma (e.g. "San Jose, CA").
# We deliberately do NOT allow hyphen-prefix here because "DE-Berlin",
# "PL-Warsaw" etc. are ISO country codes, not Delaware/Pennsylvania.
# Hyphen-prefixed cases like "US-CA-Santa Clara" are caught by US_INDICATOR
# instead because the "US-" portion matches the broader US regex.
# Case-sensitive: lowercase versions like "in" or "or" are common words.
_US_STATE_CODES = (
    "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA "
    "ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI "
    "SC SD TN TX UT VT VA WA WV WI WY DC"
).split()
US_STATE_CODE = re.compile(
    r",\s*(" + "|".join(_US_STATE_CODES) + r")(?=[,\s]|$)",
)

# Common US cities — catches plain "San Francisco" or "Seattle" with no state.
US_CITY = re.compile(
    r"\b("
    r"san\s+francisco|new\s+york\s+city|new\s+york|los\s+angeles|chicago|"
    r"seattle|austin|boston|denver|portland|atlanta|miami|dallas|houston|"
    r"san\s+diego|san\s+jose|palo\s+alto|mountain\s+view|menlo\s+park|"
    r"sunnyvale|cupertino|redwood\s+city|santa\s+monica|santa\s+clara|"
    r"durham|raleigh|cambridge|brooklyn|philadelphia|phoenix|"
    r"hillsboro|westford|salt\s+lake\s+city|bellevue|kirkland|"
    r"san\s+mateo|costa\s+mesa|sunnyvale|santa\s+ana"
    r")\b",
    re.IGNORECASE,
)

# Strong non-US indicators. Used only as a tiebreaker — a "Remote, US"
# location wins over a "Remote, Canada" if both appear (mixed posting).
NON_US_INDICATOR = re.compile(
    r"\b("
    r"canada|toronto|montreal|vancouver|ottawa|"
    r"united\s+kingdom|uk\b|england|scotland|wales|london|edinburgh|manchester|"
    r"ireland|dublin|"
    r"germany|berlin|munich|hamburg|frankfurt|"
    r"france|paris|lyon|"
    r"netherlands|amsterdam|"
    r"spain|madrid|barcelona|"
    r"italy|rome|milan|"
    r"poland|warsaw|krakow|"
    r"switzerland|zurich|geneva|"
    r"austria|vienna|"
    r"sweden|stockholm|"
    r"norway|oslo|"
    r"finland|helsinki|"
    r"denmark|copenhagen|"
    r"belgium|brussels|"
    r"portugal|lisbon|porto|"
    r"czech\s+republic|prague|"
    r"romania|bucharest|"
    r"serbia|belgrade|"
    r"israel|tel\s+aviv|jerusalem|"
    r"india|bangalore|bengaluru|hyderabad|mumbai|delhi|noida|pune|chennai|"
    r"china|beijing|shanghai|shenzhen|hong\s+kong|"
    r"japan|tokyo|osaka|"
    r"south\s+korea|korea|seoul|"
    r"singapore|"
    r"taiwan|taipei|hsinchu|"
    r"australia|sydney|melbourne|brisbane|"
    r"new\s+zealand|auckland|"
    r"mexico|mexico\s+city|guadalajara|"
    r"brazil|sao\s+paulo|s\?o\s+paulo|rio\s+de\s+janeiro|"
    r"argentina|buenos\s+aires|"
    r"chile|santiago|"
    r"colombia|bogota|"
    r"egypt|cairo|"
    r"south\s+africa|cape\s+town|johannesburg|"
    r"uae|dubai|abu\s+dhabi|"
    r"thailand|bangkok|"
    r"vietnam|ho\s+chi\s+minh|hanoi|"
    r"indonesia|jakarta|"
    r"malaysia|kuala\s+lumpur|"
    r"philippines|manila"
    r")\b",
    re.IGNORECASE,
)

_REMOTE_ONLY = re.compile(r"^remote(\s+opportunity)?$", re.IGNORECASE)
_REMOTE_US = re.compile(
    r"(?:"
    r"remote[^;]*?(?:united\s+states|u\.?\s?s\.?\s?a\.?|\bus\b|usa\b)|"
    r"(?:united\s+states|u\.?\s?s\.?\s?a\.?|\bus\b|usa\b)[^;]*?remote|"
    r"remote\s*[-–—]\s*(?:united\s+states|u\.?\s?s\.?\s?a\.?|usa\b)|"
    r"remote\s*,\s*(?:united\s+states|u\.?\s?s\.?\s?a\.?|usa\b)|"
    r"(?:united\s+states|u\.?\s?s\.?\s?a\.?|usa\b)\s*[-–—]\s*remote"
    r")",
    re.IGNORECASE,
)
_N_LOCATIONS = re.compile(r"^\d+\s+locations?$", re.IGNORECASE)


def is_location_ambiguous(location: str | None) -> bool:
    """True when US eligibility cannot be determined from the location string."""
    if not location or not location.strip():
        return True
    text = location.strip()
    if _REMOTE_ONLY.match(text):
        return True
    if _N_LOCATIONS.match(text):
        return True
    if re.match(r"^remote\b", text, re.IGNORECASE) and not _REMOTE_US.search(text):
        if not (
            US_INDICATOR.search(text)
            or US_STATE_CODE.search(text)
            or US_CITY.search(text)
        ):
            return True
    return False


def is_us_location(location: str | None) -> bool:
    """Return True if the location is US-based.

    Strict mode (default): an empty/unknown/ambiguous location returns False.
    A "Remote" with no country qualifier returns False (we can't confirm US).
    Workday's "N Locations" placeholder returns False (multi-location, can't
    verify). Mixed postings (US + non-US locations in one string) return True.
    """
    if not location or not location.strip():
        return False
    text = location.strip()

    if _REMOTE_ONLY.match(text):
        return False
    if _N_LOCATIONS.match(text):
        return False
    if _REMOTE_US.search(text):
        return True

    has_us = bool(
        US_INDICATOR.search(text)
        or US_STATE_CODE.search(text)
        or US_CITY.search(text)
    )
    if has_us:
        return True

    if NON_US_INDICATOR.search(text):
        return False

    return False
