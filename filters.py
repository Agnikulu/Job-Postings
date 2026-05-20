"""Regex filter engine.

Three title regexes:
  TARGET — Must match. Identifies early-career roles.
  ANTI   — Must NOT match. Anything senior/managerial drops out.
  DOMAIN — Optional badge. If it matches, the role is technical.

Plus a location filter for US-only operation (configurable).

`classify(title)` returns (passes_filters, is_technical).
`is_us_location(loc)` returns True for US-based locations.
`diagnose_weak_signal(title)` returns the first weak early-career signal
matched, for the --diagnose tool in review.py.

Domain match is informational only — it adds a [TECHNICAL] badge but does
not gate alerts. Per project decision, we surface all early-career roles
so the user can sanity-check borderline ones.
"""

from __future__ import annotations

import re

# =============================================================================
# Title filters
# =============================================================================

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
    # Core software / engineering
    r"software|engineer(ing)?|"
    r"backend|frontend|full[\s-]?stack|"
    r"infrastructure|platform|systems|"
    # Data + ML + AI
    r"machine[\s-]learning|ml|"
    r"data(\s+(scientist|engineer|analyst))?|"
    r"ai|artificial\s+intelligence|"
    r"applied\s+scientist|deep\s+learning|"
    r"inference|llm|generative|"
    # Research / quant
    r"quant(itative)?|research|"
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
_N_LOCATIONS = re.compile(r"^\d+\s+locations?$", re.IGNORECASE)


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
