"""Extract qualification/requirements signals from job descriptions.

Full descriptions are noisy (marketing copy triggers DOMAIN regex). We slice
the requirements / qualifications section and match EC + education patterns
there only.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# --- Section header tiers (higher = preferred) ---------------------------

# Explicit candidate-fit blocks.
_TIER1_HEADERS = (
    r"you\s+may\s+be\s+(?:a\s+)?(?:good\s+)?fit\s+if",
    r"you(?:'re|\s+are)\s+(?:a\s+)?(?:good\s+)?fit\s+if",
    r"skills?\s+you(?:'ll|\s+will)\s+need\s+to\s+bring",
    r"skills?\s+(?:&|and)\s+experience\s+you(?:'ll|\s+will)\s+need",
    r"who\s+you\s+are",
    r"about\s+you(?:\s+because)?\s+(?!and\b)",
    r"what\s+you\s+bring(?:\s+to\s+the\s+team)?",
    r"what\s+you\s+should\s+have",
    r"what\s+we\s+look\s+for",
    r"what\s+we(?:'re|\s+are)\s+looking\s+for",
    r"we(?:'d|\s+would)\s+love\s+to\s+hear\s+from\s+you(?:\s+if\s+you\s+have)?",
    r"ideal\s+candidate",
    r"your\s+background",
    r"your\s+profile",
)

# Structured qualification labels (common on GH / enterprise boards).
_TIER2_HEADERS = (
    r"minimum\s+education",
    r"minimum\s+years\s+of\s+experience",
    r"minimum\s+(?:qualifications?|requirements?)",
    r"preferred\s+(?:qualifications?|requirements?)",
    r"basic\s+(?:qualifications?|requirements?)",
    r"required\s+qualifications?",
    r"required\s+field\s+of\s+study",
    r"candidate\s+requirements?",
    r"education\s+(?:&|and)\s+experience",
    r"what\s+you(?:'ll|\s+will)\s+need",
    r"what\s+we\s+need\s+to\s+see",
)

# Header must include colon or be a clear section title.
_TIER3_HEADERS = (
    r"qualifications?",
    r"requirements?",
)

# Duties / role-description blocks (used for fallback slicing).
_DUTIES_HEADERS = (
    r"what\s+you(?:'ll|\s+will)\s+do",
    r"what\s+you(?:'ll|\s+will)\s+achieve",
    r"responsibilities",
    r"the\s+impact\s+you\s+will\s+have",
    r"about\s+the\s+role",
    r"about\s+this\s+role",
    r"the\s+role",
)

# Footers — stop extraction here.
_FOOTER_HEADERS = (
    r"about\s+(?:databricks|notion|the\s+company|us)\b",
    r"benefits(?:\s+at|\s+&|\s+and|\s*:)?",
    r"compensation(?:\s+&|\s+and|\s*:)?",
    r"pay\s+transparency",
    r"our\s+commitment",
    r"equal\s+opportunity",
    r"equal\s+opportunity\s+employer",
    r"privacy\s+notice",
    r"we\s+are\s+committed",
    r"notion\s+is\s+proud",
    r"compliance(?:\s*:)?",
    r"annual\s+salary",
    r"location-based\s+hybrid\s+policy",
    r"#li-",
)

# Inline candidate search when no section header exists.
_INLINE_LOOKING_FOR = re.compile(
    r"(?:we(?:'re|\s+are)\s+)?looking\s+for\s+(?:a|an|someone|motivated|talented|passionate|researchers?)",
    re.IGNORECASE,
)

# "requirements" preceded by these words is a duties bullet, not a section.
_REQ_FALSE_POSITIVE = re.compile(
    r"\b(?:technical|data|key|job|system|product|internal|platform|legal|"
    r"regulatory|compliance|reporting|business|functional|"
    r"architectural|design|software|quality)\s+requirements?\b",
    re.IGNORECASE,
)

_APOSTROPHE_CHARS = re.compile(r"[''\u2018\u2019`]")
DESC_STRONG_EC = re.compile(
    r"\b("
    r"ph\.?\s?d\.?\s+candidate|"
    r"doctoral\s+candidate|"
    r"postdoc|post-doc|"
    r"recent\s+ph\.?\s?d|"
    r"rising\s+(?:4th|fourth|3rd|third)\s+year|"
    r"currently\s+(?:enrolled|pursuing)|"
    r"pursuing\s+(?:a\s+)?(?:degree|bachelor|master|doctorate|ph\.?\s?d)|"
    r"graduating\s+(?:in\s+)?(?:20[2-9][0-9]|spring|fall|summer|winter)|"
    r"expected\s+graduation|"
    r"class\s+of\s+20[2-9][0-9]|"
    r"graduate\s+20[2-9][0-9]|"
    r"intern(ship)?(?:\s+experience|\s+program)?|"
    r"internship\s+program|"
    r"fellows?\s+program|"
    r"fellowship|"
    r"co-?op(?:\s+experience|\s+program)?|"
    r"previous\s+internship|"
    r"new[\s-]?grad(uate)?|"
    r"new\s+college\s+grad|"
    r"university\s+graduate|"
    r"recent\s+graduate|"
    r"early[\s-]career|"
    r"entry[\s-]level|"
    r"campus\s+(?:recruiting|hire|program)|"
    r"undergraduate\s+student|"
    r"bachelor'?s\s+student|"
    r"master'?s\s+student|"
    r"graduate\s+student|"
    r"(?:0|zero|no|less\s+than|up\s+to)\s*[-–—]?\s*[12]\s+years?(?:\s+of)?(?:\s+experience)?|"
    r"0\s*[-–—]\s*2\s+years?|"
    r"[01]\s*[-–—]\s*3\s+years?(?:\s+of)?(?:\s+experience)?"
    r")\b",
    re.IGNORECASE,
)

DESC_BACHELORS_REQ = re.compile(
    r"\b("
    r"bachelor'?s\s+(?:degree|or\s+equivalent)(?:\s+(?:in|required|preferred))?|"
    r"bachelor'?s\s+(?:degree\s+)?(?:required|preferred)|"
    r"undergraduate\s+degree(?:\s+required)?|"
    r"four[\s-]?year\s+degree(?:\s+required)?|"
    r"minimum\s+education\s*:\s*bachelor|"
    r"BS,?\s+MS\s+or\s+PhD|"
    r"MS\s+or\s+PhD|"
    r"\bBS\b.*\b(?:MS|PhD)\b"
    r")\b",
    re.IGNORECASE,
)

DESC_EC = DESC_STRONG_EC

DESC_TECH_FIELD = re.compile(
    r"\b("
    r"computer\s+science|"
    r"computer\s+engineering|"
    r"software\s+engineering|"
    r"electrical\s+engineering|"
    r"statistics|"
    r"applied\s+mathematics|"
    r"machine\s+learning|"
    r"data\s+science|"
    r"information\s+technology|"
    r"\bcs\b|\bml\b"
    r")\b",
    re.IGNORECASE,
)

DESC_SENIOR_EXP = re.compile(
    r"\b("
    r"(?<![0-9\-–—])[1-9]\s*[-–—]\s*(?:[5-9]|10)\+?\s*years?|"
    r"(?:minimum|at\s+least)\s+(?:of\s+)?(?<![0-9\-–—])(?:[3-9]|10)\+?\s*years?|"
    r"(?<![0-9\-–—])(?:[3-9]|10)\+\s*years?|"
    r"(?<![0-9\-–—])(?:[3-9]|10)\+?\s*years?\s+(?:of\s+)?(?:[\w/-]+\s+){0,8}experience|"
    r"(?<![0-9\-–—])(?:[3-9]|10)\+?\s*years?(?:\s+of)?(?:\s+professional|\s+industry|\s+relevant|\s+software)?\s+experience(?:\s+required|\s+in\s+the\s+job\s+offered)?|"
    r"(?:employer will accept|will accept).{0,200}?\b(?:and\s+)?(?<![0-9\-–—])(?:[3-9]|10)\+?\s*years?\s+of\s+experience|"
    r"(?:employer will accept|will accept).{0,200}?\b(?:and\s+)?three\s+years\s+of\s+experience|"
    r"significant\s+experience|"
    r"experienced\s+(?:backend|software|engineer)|"
    r"deep\s+expertise|"
    r"proven\s+track\s+record|"
    r"operating\s+as\s+a\s+(?:staff|principal)\s+engineer|"
    r"(?:staff|principal)\s+(?:software\s+)?engineer|"
    r"significant\s+experience\s+(?:leading|managing)"
    r")\b",
    re.IGNORECASE,
)

# Minimum experience bars in qualification blocks (3+ years — 0–2 yr roles stay EC).
DESC_MIN_YEARS_REQ = re.compile(
    r"\b("
    r"(?:minimum\s+of\s+)?(?<![0-9\-–—])(?:[3-9]|10)\+?\s*years?(?:['\u2019]s?)?(?:\s+of)?(?:\s+\w+\s+){0,4}experience|"
    r"(?<![0-9\-–—])[3-9]\s*[-–—]\s*12\+?\s*years?(?:\s+of)?(?:\w+\s+){0,4}experience"
    r")\b",
    re.IGNORECASE,
)

_YEAR_RANGE_EC = re.compile(
    r"\b("
    r"[01]\s*[-–—]\s*3\s*years?|"
    r"0\s*[-–—]\s*2\s*years?|"
    r"1[\s–—-]+3\s+years?"
    r")\b",
    re.IGNORECASE,
)

_EARLY_YEARS_EC = re.compile(
    r"\b("
    r"(?:minimum\s+of\s+)?(?:0|1)\s+years?(?:\s+of)?(?:\s+experience)?|"
    r"(?:minimum\s+of\s+)?2\s*\+\s*years?(?:['\u2019]s?)?(?:\s+of)?(?:\s+experience)?|"
    r"2\s*\+\s*years?(?:\s+of)?(?:\s+experience)?|"
    r"1\s*\+\s*years?\s+(?:of\s+)?(?:work\s+)?experience"
    r")\b",
    re.IGNORECASE,
)

_EC_FRIENDLY_REQ_HEADER = re.compile(
    r"^(?:(?:your\s+)?ideal\s+\w+(?:\s+\w+){0,4}\s+will\s+have|"
    r"what you should have|what you bring(?: to the team)?|what you have|"
    r"minimum\s+qualifications?)\b",
    re.IGNORECASE,
)

_RESEARCH_TITLE = re.compile(
    r"\b(?:research\s+scientist|data\s+scientist|quantitative\s+researcher|"
    r"equity\s+quantitative\s+researcher|research\s+engineer)\b",
    re.IGNORECASE,
)

_SOFTWARE_FAMILY_TITLE = re.compile(
    r"\b(?:(?:application|embedded|ai|backend|frontend|full[\s-]?stack|wireless)\s+)?"
    r"(?:software\s+engineer|network\s+software\s+integration\s+engineer)\b",
    re.IGNORECASE,
)

_SPACEX_CREDENTIAL_BAR = re.compile(
    r"(?:"
    r"1\+?\s*years?(?:\s+of)?(?:\s+[\w/]+\s+){0,8}(?:experience|building)|"
    r"in\s+lieu\s+of\s+a\s+degree|"
    r"including\s+internship"
    r")",
    re.IGNORECASE,
)

_MOBILE_ENGINEER_TITLE = re.compile(
    r"\b(?:mobile|android|ios)\s+engineer\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DescriptionSignals:
    requirements_text: str | None
    has_strong_ec: bool
    has_bachelors_req: bool
    has_tech_field: bool
    has_senior_exp: bool
    has_min_years_req: bool

    @property
    def has_ec(self) -> bool:
        return self.has_strong_ec or self.has_bachelors_req


def _normalize(description: str) -> str:
    text = _APOSTROPHE_CHARS.sub("'", description.strip())
    text = re.sub(r"\*+", " ", text)
    return re.sub(r"\s+", " ", text)


def _header_pattern(header: str, *, require_colon: bool = False) -> re.Pattern[str]:
    suffix = r"\s*:\s*" if require_colon else r"\s*"
    return re.compile(
        rf"(?:^|[.!?]\s+|\s)({header}){suffix}",
        re.IGNORECASE,
    )


def _compile_headers(headers: tuple[str, ...], *, require_colon: bool = False) -> list[re.Pattern[str]]:
    return [_header_pattern(h, require_colon=require_colon) for h in headers]


_TIER1_RES = _compile_headers(_TIER1_HEADERS)
_TIER2_RES = _compile_headers(_TIER2_HEADERS)
_TIER3_RES = _compile_headers(_TIER3_HEADERS, require_colon=True)
_DUTIES_RES = _compile_headers(_DUTIES_HEADERS)
_FOOTER_RES = _compile_headers(_FOOTER_HEADERS)


def _is_false_positive_requirements(text: str, start: int) -> bool:
    window = text[max(0, start - 40): start + 20]
    return bool(_REQ_FALSE_POSITIVE.search(window))


def _find_header_matches(
    text: str,
    patterns: list[re.Pattern[str]],
    *,
    priority: int,
) -> list[tuple[int, int, str]]:
    out: list[tuple[int, int, str]] = []
    for pat in patterns:
        for m in pat.finditer(text):
            label = m.group(1)
            if label.lower().startswith(("requirement", "qualification")):
                if _is_false_positive_requirements(text, m.start(1)):
                    continue
            out.append((m.start(), priority, label))
    return out


def _find_footer_start(text: str, after: int) -> int | None:
    tail = text[after:]
    best: int | None = None
    for pat in _FOOTER_RES:
        m = pat.search(tail)
        if m:
            pos = after + m.start()
            if best is None or pos < best:
                best = pos
    return best


def _slice_section(text: str, start: int) -> str:
    end = _find_footer_start(text, start + 1)
    section = text[start: end if end is not None else len(text)]
    section = section.strip()
    # Trim at inline footer phrases that lack a header boundary.
    m = re.search(
        r"\b(?:benefits\s+at|equal\s+opportunity\s+employer|notion\s+is\s+proud)\b",
        section,
        re.IGNORECASE,
    )
    if m:
        section = section[: m.start()].strip()
    return section


def _score_req_section(section: str) -> int:
    """Rank how qualification-like a sliced section is."""
    score = 0
    if DESC_STRONG_EC.search(section):
        score += 10
    if DESC_BACHELORS_REQ.search(section):
        score += 5
    if DESC_TECH_FIELD.search(section):
        score += 3
    if DESC_SENIOR_EXP.search(section):
        score += 2
    if re.search(r"\b(?:degree|years?\s+of\s+experience|qualification)\b", section, re.I):
        score += 1
    if re.search(
        r"\b(?:wellness|reimbursement|benefits\s+package|employee\s+assistance|"
        r"base\s+pay|salary\s+range)\b",
        section,
        re.I,
    ):
        score -= 8
    if re.search(
        r"\b(?:you use the word|customers.*million times|real users)\b",
        section,
        re.I,
    ):
        score -= 10
    return score


def _best_header_match(text: str) -> int | None:
    """Return start index of the best requirements header, or None."""
    matches: list[tuple[int, int, str]] = []
    matches.extend(_find_header_matches(text, _TIER1_RES, priority=3))
    matches.extend(_find_header_matches(text, _TIER2_RES, priority=2))
    matches.extend(_find_header_matches(text, _TIER3_RES, priority=1))
    if not matches:
        return None

    tier2_starts = [m[0] for m in matches if m[1] == 2]
    has_tier1 = any(m[1] == 3 for m in matches)
    if tier2_starts and not has_tier1:
        return min(tier2_starts)

    ranked: list[tuple[int, int, int]] = []
    for start, priority, _label in matches:
        ranked.append((priority, _score_req_section(_slice_section(text, start)), start))
    ranked.sort(key=lambda t: (-t[0], -t[1], t[2]))
    best = ranked[0][2]
    # Prefer a later minimum-requirements block over an earlier marketing "Who you are".
    for start, priority, label in matches:
        if priority >= 2 and re.search(
            r"minimum\s+(?:qualifications?|requirements?)",
            label,
            re.I,
        ):
            section = _slice_section(text, start)
            if _score_req_section(section) >= 3:
                return start
    return best


def _fallback_after_duties(text: str) -> str | None:
    """Take text after the last duties block until a footer."""
    duty_positions = []
    for pat in _DUTIES_RES:
        for m in pat.finditer(text):
            duty_positions.append(m.start())
    if not duty_positions:
        return None
    start = max(duty_positions)
    section = _slice_section(text, start)
    # Skip very short slices — likely just the duties header with no qual content.
    if len(section) < 120:
        return None
    # Must look like qualifications, not pure duties repetition.
    if not (
        DESC_STRONG_EC.search(section)
        or DESC_BACHELORS_REQ.search(section)
        or DESC_TECH_FIELD.search(section)
        or DESC_SENIOR_EXP.search(section)
        or re.search(r"\b(?:degree|experience|education|qualification)\b", section, re.I)
    ):
        return None
    return section


def _fallback_inline_looking_for(text: str) -> str | None:
    m = _INLINE_LOOKING_FOR.search(text)
    if not m:
        return None
    section = _slice_section(text, m.start())
    if len(section) < 80:
        return None
    return section


def _fallback_minimum_education_block(text: str) -> str | None:
    m = re.search(
        r"minimum\s+education\s*:",
        text,
        re.IGNORECASE,
    )
    if not m:
        return None
    return _slice_section(text, m.start())


def _fallback_h1b_qualifications(text: str) -> str | None:
    """H1B/legal postings (common on Uber): qual text at tail or after Duties."""
    for pattern in (
        r"Employer will accept",
        r"Employer:\s*",
        r"\bDuties:\s*",
    ):
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        section = text[match.start():]
        if len(section) < 80:
            continue
        if re.search(
            r"\b(?:degree|years?\s+of\s+experience|bachelor|master|employer will accept)\b",
            section,
            re.IGNORECASE,
        ):
            return section[:3500]
    return None


def _fallback_you_have_block(text: str) -> str | None:
    """Discord-style 'You have:' qualification bullets."""
    match = re.search(r"\bYou have\s*:", text)
    if not match:
        return None
    section = _slice_section(text, match.start())
    if len(section) < 40:
        return None
    return section


def _fallback_requirements_no_colon(text: str) -> str | None:
    """Requirements/REQUIREMENTS blocks without a colon (common on Point72 and similar)."""
    match = re.search(
        r"\b(?:minimum\s+)?requirements?\b(?!\s*:)\s+"
        r"(?:BS|MS|PhD|B\.?S\.?|M\.?S\.?|Ph\.?D|bachelor|master|undergraduate)",
        text,
        re.IGNORECASE,
    )
    if not match:
        match = re.search(r"\bREQUIREMENTS\b\s+", text)
    if not match:
        return None
    if _is_false_positive_requirements(text, match.start()):
        return None
    section = _slice_section(text, match.start())
    if len(section) < 40:
        return None
    return section


def _fallback_ideal_candidate_block(text: str) -> str | None:
    """Snowflake-style 'YOUR IDEAL SOFTWARE ENGINEER WILL HAVE' blocks."""
    match = re.search(
        r"\b(?:your\s+)?ideal\s+\w+(?:\s+\w+){0,4}\s+will\s+have\b",
        text,
        re.IGNORECASE,
    )
    if not match:
        return None
    section = _slice_section(text, match.start())
    if len(section) < 40:
        return None
    return section


def _fallback_minimum_experience_line(text: str) -> str | None:
    """Inline 'Minimum N year(s) of experience' without a section header."""
    match = re.search(
        r"\bminimum\s+(?:0|1|2|[3-9])\s*\+?\s*years?\b",
        text,
        re.IGNORECASE,
    )
    if not match:
        return None
    start = max(0, match.start() - 80)
    return text[start : match.start() + 400].strip()


def qualifying_early_years(
    text: str | None,
    title: str | None,
    *,
    ec_friendly_header: bool = False,
) -> bool:
    """Low years-of-experience bars that count as EC only in friendly contexts."""
    title_text = title or ""
    if text and _SOFTWARE_FAMILY_TITLE.search(title_text):
        if _EARLY_YEARS_EC.search(text) or _SPACEX_CREDENTIAL_BAR.search(text):
            return True
    if not text or not _EARLY_YEARS_EC.search(text):
        return False
    if _RESEARCH_TITLE.search(title_text):
        return True
    if _MOBILE_ENGINEER_TITLE.search(title_text):
        return True
    return ec_friendly_header


def ec_friendly_requirements_header(requirements_text: str | None) -> bool:
    if not requirements_text:
        return False
    text = requirements_text.strip().lstrip(". ")
    return bool(_EC_FRIENDLY_REQ_HEADER.match(text))


def year_range_only_ec(signals: DescriptionSignals) -> bool:
    """True when the only EC signal in requirements is a low years-of-experience range."""
    text = signals.requirements_text or ""
    if not text or not signals.has_strong_ec:
        return False
    if not _YEAR_RANGE_EC.search(text):
        return False
    stripped = _YEAR_RANGE_EC.sub(" ", text)
    stripped = re.sub(r"\bintern(?:ship)?\b", " ", stripped, flags=re.IGNORECASE)
    return not DESC_STRONG_EC.search(stripped)


def effective_strong_ec(signals: DescriptionSignals) -> bool:
    """Strong EC that still counts when senior bars appear alongside year ranges."""
    if not signals.has_strong_ec:
        return False
    if not signals.has_senior_exp:
        return True
    text = signals.requirements_text or ""
    if not text:
        return True
    stripped = _YEAR_RANGE_EC.sub(" ", text)
    stripped = re.sub(
        r"\b(?:internship|previous\s+internship)\s+experience\b",
        " ",
        stripped,
        flags=re.IGNORECASE,
    )
    return bool(DESC_STRONG_EC.search(stripped))


def _fallback_qualifications_block(text: str) -> str | None:
    """Unstructured 'Qualifications' blocks (Workday and similar)."""
    match = re.search(
        r"\b(?:minimum\s+)?qualifications?\b\s*:?",
        text,
        re.IGNORECASE,
    )
    if not match:
        return None
    if _is_false_positive_requirements(text, match.start()):
        return None
    section = _slice_section(text, match.start())
    if len(section) < 60:
        return None
    return section


def extract_requirements_text(description: str | None) -> str | None:
    """Return the qualifications/requirements slice of a plain-text description."""
    if not description or not description.strip():
        return None

    text = _normalize(description)

    start = _best_header_match(text)
    if start is not None:
        section = _slice_section(text, start)
        if section:
            return section

    for fallback in (
        _fallback_minimum_education_block,
        _fallback_inline_looking_for,
        _fallback_requirements_no_colon,
        _fallback_ideal_candidate_block,
        _fallback_you_have_block,
        _fallback_qualifications_block,
        _fallback_h1b_qualifications,
        _fallback_minimum_experience_line,
        _fallback_after_duties,
    ):
        section = fallback(text)
        if section:
            return section

    return None


def _signals_from_text(text: str, *, requirements_text: str | None) -> DescriptionSignals:
    return DescriptionSignals(
        requirements_text=requirements_text,
        has_strong_ec=bool(DESC_STRONG_EC.search(text)),
        has_bachelors_req=bool(DESC_BACHELORS_REQ.search(text)),
        has_tech_field=bool(DESC_TECH_FIELD.search(text)),
        has_senior_exp=bool(DESC_SENIOR_EXP.search(text)),
        has_min_years_req=bool(DESC_MIN_YEARS_REQ.search(text)),
    )


def scan_full_description(description: str | None) -> DescriptionSignals:
    """Scan the full description body (used when requirements slice is missing)."""
    if not description or not description.strip():
        return DescriptionSignals(None, False, False, False, False, False)
    return _signals_from_text(_normalize(description), requirements_text=None)


def merge_description_signals(
    primary: DescriptionSignals,
    secondary: DescriptionSignals,
) -> DescriptionSignals:
    """Combine requirement-slice and full-body signals (OR on flags)."""
    return DescriptionSignals(
        requirements_text=primary.requirements_text or secondary.requirements_text,
        has_strong_ec=primary.has_strong_ec or secondary.has_strong_ec,
        has_bachelors_req=primary.has_bachelors_req or secondary.has_bachelors_req,
        has_tech_field=primary.has_tech_field or secondary.has_tech_field,
        has_senior_exp=primary.has_senior_exp or secondary.has_senior_exp,
        has_min_years_req=primary.has_min_years_req or secondary.has_min_years_req,
    )


def extract_description_signals(description: str | None) -> DescriptionSignals:
    """Parse EC / tech-field / senior-exp signals from requirements text only."""
    req = extract_requirements_text(description)
    if not req:
        return DescriptionSignals(None, False, False, False, False, False)
    return _signals_from_text(req, requirements_text=req)


def extract_description_signals_with_fallback(
    description: str | None,
    *,
    title_ec_hint: bool = False,
) -> DescriptionSignals:
    """Requirements slice first; scan full body when title hints EC and slice is weak."""
    req_sig = extract_description_signals(description)
    if not description or not description.strip():
        return req_sig
    if not title_ec_hint:
        return req_sig

    body_sig = scan_full_description(description)
    if not req_sig.requirements_text:
        return body_sig

    if req_sig.has_ec or req_sig.has_senior_exp:
        return req_sig

    if body_sig.has_ec or body_sig.has_senior_exp:
        return merge_description_signals(req_sig, body_sig)
    return req_sig
