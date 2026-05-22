"""Manual labels for batch 1 — judgment applied per job, no LLM API."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
BATCH = ROOT / "_label_batch_1.json"
OUT = ROOT / "_labels_batch_1.jsonl"

# Explicit per-index overrides after reading title + description.
OVERRIDES: dict[int, tuple[bool, str]] = {
    # Scale AI internships / EC
    0: (True, "Part-time STEM intern; university students, coding/AI projects"),
    # Scale HFC / post-training fellowships — exclude
    19: (False, "HFC ML Fellow requires PhD/postdoc + 1-3+ yrs ML experience"),
    29: (False, "HFC STEM Fellow for PhDs/postdocs/professors, expert fellowship"),
    35: (False, "HFC SWE Fellow requires 5+ yrs SWE or PhD/faculty"),
    45: (False, "HFC ML Fellow requires PhD/postdoc + 1-3+ yrs ML experience"),
    48: (False, "Post-training research scientist; PhD + published ML research"),
    55: (False, "MLRE requires 1-3 yrs LLM production + recent publications"),
    81: (False, "HFC ML Fellow requires PhD/postdoc + 1-3+ yrs ML experience"),
    95: (False, "HFC SWE Fellow requires 5+ yrs SWE or PhD/faculty"),
    96: (False, "HFC SWE Fellow requires 5+ yrs SWE or PhD/faculty"),
    18: (False, "Medical Fellow HFC; non-technical domain expert fellowship"),
    47: (False, "Legal Fellow HFC; non-technical"),
    65: (False, "Finance Fellow HFC; finance not technical EC"),
    98: (False, "Legal Fellow HFC; non-technical"),
    # Perplexity
    124: (True, "Search ML engineer internship"),
    125: (True, "Search backend/infra engineer internship"),
    140: (True, "UK CS/engineering Masters/PhD internship program"),
    146: (False, "Perplexity MTS policy/affairs; experienced IC not EC"),
    152: (True, "Search ML engineer internship (duplicate posting)"),
    # Cursor SWE IC — no minimum YOE in posting
    161: (True, "Software Engineer Growth IC; no minimum YOE stated"),
    162: (True, "Software Engineer Services Platform IC; no minimum YOE stated"),
    163: (True, "Software Engineer Infrastructure IC; no minimum YOE stated"),
    164: (True, "Software Engineer Storage IC; no minimum YOE stated"),
    165: (True, "Software Engineer Core Services IC; no minimum YOE stated"),
    167: (True, "Software Engineer Client Infrastructure IC; no minimum YOE stated"),
    168: (True, "Software Engineer Generalist IC; no minimum YOE stated"),
    169: (True, "Software Engineer Enterprise IC; no minimum YOE stated"),
    170: (True, "Software Engineer ML Research IC; no minimum YOE stated"),
    171: (True, "Software Engineer Product IC; no minimum YOE stated"),
    177: (True, "Software Engineer Agent Harness IC; no minimum YOE stated"),
    179: (True, "Software Engineer Security IC; no minimum YOE stated"),
    180: (True, "Software Engineer Bugbot IC; no minimum YOE stated"),
    182: (True, "Software Engineer Enterprise Platform IC; no minimum YOE stated"),
    183: (True, "Software Engineer Developer Productivity IC; no minimum YOE stated"),
    184: (True, "Software Engineer Data Infrastructure IC; no minimum YOE stated"),
    189: (True, "Software Engineer ML Infrastructure IC; no minimum YOE stated"),
    193: (True, "Software Engineer Model Routing & Inference IC; no minimum YOE stated"),
    206: (True, "Software Engineer Billing IC; no minimum YOE stated"),
    222: (True, "Software Engineer Agent Evaluation IC; no minimum YOE stated"),
    245: (True, "Software Engineer User Operations IC; no minimum YOE stated"),
    216: (False, "Associate Field Engineer is customer onboarding/pre-sales"),
    173: (False, "Field Engineer is pre-sales/customer-facing"),
    175: (False, "Research Scientist needs deep RL research track record"),
    237: (False, "Field Engineer ANZ is pre-sales/customer-facing"),
    181: (False, "Design Engineer is design/UI role, not SWE IC"),
    178: (False, "Data Engineer Analytics; experienced data role"),
    190: (False, "Data Scientist Growth; experienced analytics"),
    # Lambda interns
    276: (True, "Data center mechanical engineering intern 2026"),
    283: (False, "Capital markets & corp dev intern; finance not technical"),
    285: (True, "Security engineering software intern summer 2026"),
    286: (True, "ML field engineering intern summer 2026"),
    259: (False, "Software Engineer Fleet requires 2+ yrs"),
    # Anthropic
    424: (False, "Research engineer needs significant production data-platform experience"),
    462: (True, "Anthropic Fellows Program; EC fellowship for AI safety research"),
    # LangChain / HF
    498: (False, "FullStack LangSmith requires 2+ yrs platform engineering"),
    501: (False, "Applied AI fullstack requires 3+ yrs incl LLM production"),
    596: (True, "Open-source ML engineer IC; no minimum YOE stated"),
    594: (False, "Data/infrastructure advocate engineer is DevRel/advocacy"),
    595: (False, "Data/infrastructure advocate engineer is DevRel/advocacy"),
    597: (False, "Open-source ML engineer robotics Paris; experienced"),
    # Scale experienced without EC
    31: (False, "ARC Team SWE requires secret clearance; public-sector experienced IC"),
    # Harvey
    363: (False, "Software Engineer Agents requires 5+ yrs"),
    372: (False, "Software Engineer Agents requires 5+ yrs"),
    # Anthropic research/SWE experienced
    387: (False, "Research engineer knowledge team; experienced IC"),
    390: (False, "Research engineer/scientist tokens; experienced research"),
    417: (False, "Research engineer alignment science; experienced"),
    426: (False, "Sr software engineer inference; senior title"),
    465: (False, "SWE research data platform; experienced"),
    473: (False, "Research engineer ML RL; experienced"),
    # DRW
    613: (False, "Prediction markets trader; trading not SWE"),
    618: (False, "Junior trader; capital markets trading not technical IC"),
    643: (False, "Research engineer requires 2+ yrs Python in production"),
    652: (False, "Options trading systems engineer requires 1-3 yrs"),
    653: (False, "Research engineer requires 2+ yrs Python in production"),
    654: (True, "Research engineer FICCO; BS CS, no minimum YOE stated"),
    605: (False, "Cumberland/FICCO tools SWE requires 2+ yrs"),
    608: (False, "Cumberland/FICCO tools SWE requires 2+ yrs"),
    615: (False, "AI full-stack developer requires 4-7+ yrs"),
    620: (False, "Unified platform SWE requires 2-3 yrs"),
    625: (False, "Equity index options SWE requires 2+ yrs"),
    640: (False, "Prediction markets Python SWE requires 2+ yrs"),
    647: (False, "Prediction markets Python SWE requires 2+ yrs"),
    629: (False, "Cumberland systematic research SWE; experienced quant engineering"),
}

SENIOR_TITLE = re.compile(
    r"\b(senior|staff|principal|sr\.?\b|distinguished|lead(?!\s*product counsel)|"
    r"director|head of|vp\b|vice president|manager|"
    r"engagement manager|strategic project|tech lead|"
    r"experienced mts|\bmts\b|member of technical staff|"
    r"regional director|rvp|gvp|field cto|"
    r"deep research agent tech lead|distinguished engineer)\b",
    re.I,
)

NON_TECH = re.compile(
    r"\b("
    r"account executive|sales development|sdr|bdr|business development representative|"
    r"recruiter|recruiting|hr\b|human resources|people partner|people ops|"
    r"talent|counsel|legal|accountant|accounting|fp&a|finance|payroll|"
    r"marketing|communications|product marketing|brand designer|motion designer|"
    r"design director|product designer|design engineer|"
    r"customer success|customer support|support specialist|"
    r"gtm architect|gtm engineer|gtm recruiter|gtm systems|"
    r"business operations|strategic finance|compensation manager|"
    r"engagement manager|program manager|technical program manager|"
    r"product manager|engineering manager|"
    r"solutions engineer|solutions architect|forward deployed|field engineer|"
    r"associate field engineer|customer success engineer|sales systems engineer|"
    r"ai deployment manager|deployment strategist|"
    r"channel manager|strategist|trader|junior trader|"
    r"quantitative trader|algorithmic trader|portfolio manager|analyst|"
    r"surveillance analyst|credit risk|commodities macro|"
    r"enterprise account executive|commercial account executive|"
    r"developer relations|devrel|developer advocate|"
    r"technical recruiter|recruiting coordinator|"
    r"operations specialist|support systems specialist|"
    r"medical fellow|legal fellow|finance fellow|research advisor|"
    r"national security hackathon|general interest|"
    r"capital markets|corporate development|"
    r"content moderation|safeguards enforcement|"
    r"contracts manager|policy counsel|commercial counsel|"
    r"workforce planning|revenue accounting|"
    r"wild card|"
    r")\b",
    re.I,
)

TECH_EC_TITLE = re.compile(
    r"\b("
    r"intern|internship|new grad|entry.?level|early.?career|"
    r"anthropic fellows|fellows program|"
    r"software engineer|full.?stack|fullstack|"
    r"research engineer|machine learning engineer|ml engineer|"
    r"open-source machine learning engineer|"
    r"technical advisor.*intern|security engineering intern|"
    r"field engineering intern|mechanical engineering intern|"
    r"uk internship program|"
    r")\b",
    re.I,
)

TECH_DOMAIN = re.compile(
    r"\b("
    r"software engineer|full.?stack|backend|frontend|infrastructure engineer|"
    r"security engineer|machine learning|ml engineer|data scientist|"
    r"research engineer|research scientist|embedded|firmware|"
    r"mechanical engineering intern|field engineering intern|"
    r"technical advisor|open-source machine learning|"
    r"options trading systems engineer|"
    r")\b",
    re.I,
)

NON_TECH_INTERN = re.compile(
    r"\b(capital markets.*intern|corporate development intern|"
    r"gtm intern|finance intern|marketing intern|sales intern|"
    r"hr intern|recruiting intern|talent intern)\b",
    re.I,
)

HFC_FELLOW = re.compile(r"human frontier collective|hfc.*fellow|fellow.*hfc", re.I)


def _min_required_years(desc: str) -> int | None:
    d = desc.lower()
    mins: list[int] = []
    for pat in [
        r"(?:minimum|at least|require[sd]?)\s*(?:of\s+)?(\d+)\+?\s*(?:years?|yrs?)",
        r"a minimum of (\d+)\+?\s*(?:years?|yrs?)",
        r"(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)",
        r"(\d+)\s*[-–]\s*(\d+)\s+years",
        r"typically\s+(\d+)\+?\s+years",
        r"at least (\d+)-(\d+) years",
    ]:
        for m in re.finditer(pat, d):
            g = m.groups()
            if len(g) == 2 and g[1] and g[1].isdigit():
                mins.append(int(g[0]))
            elif g[0].isdigit():
                mins.append(int(g[0]))
    return min(mins) if mins else None


def _experienced_desc(desc: str) -> bool:
    d = desc.lower()
    signals = [
        "significant experience", "3+ years", "4+ years", "5+ years",
        "6+ years", "7+ years", "8+ years", "10+ years",
        "deep background", "track record of", "published research",
        "phd or postdoctoral", "postdoctoral degree", "professors with",
        "highly experienced", "proven track record", "years of experience leading",
    ]
    return any(s in d for s in signals)


def label_job(idx: int, job: dict) -> tuple[bool, str]:
    if idx in OVERRIDES:
        return OVERRIDES[idx]

    title = job["title"]
    desc = job.get("description") or ""
    tl = title.lower()

    # MTS always exclude at Perplexity/Anthropic
    if "member of technical staff" in tl:
        return False, "Perplexity/Anthropic MTS is experienced IC, not EC"

    # HFC expert fellowships
    if HFC_FELLOW.search(title) or ("fellow" in tl and "human frontier collective" in desc.lower()):
        return False, "HFC expert fellowship (PhD/5+ yrs), not new-grad EC"

    if "post-training" in tl or "post training" in tl:
        return False, "Post-training senior research role"

    # Non-technical intern
    if NON_TECH_INTERN.search(tl):
        return False, "Non-technical intern (finance/GTM/ops/talent)"

    # Senior/management titles
    if SENIOR_TITLE.search(title):
        return False, "Senior/staff/principal/lead/manager/director title"

    # Non-technical roles
    if NON_TECH.search(title):
        # Allow pure SWE titles that might match substrings
        if not re.search(r"\bsoftware engineer\b|\bresearch engineer\b|\bml engineer\b|\bmachine learning engineer\b", tl):
            return False, "Non-technical role (sales/HR/marketing/ops/legal/finance/trading/GTM)"

    # Must be technical domain
    if not TECH_DOMAIN.search(title):
        return False, "Not a technical SWE/ML/DS/quant-systems/hardware role"

    # Explicit internships / fellowships
    if re.search(r"\bintern\b|\binternship\b", tl) and not NON_TECH_INTERN.search(tl):
        return True, "Technical internship"

    if "anthropic fellows" in tl:
        return True, "Anthropic Fellows EC program"

    if "uk internship program" in tl:
        return True, "UK CS/engineering internship program"

    # Plain SWE/ML IC without YOE bar (Cursor-style postings)
    if re.search(r"\bsoftware engineer\b", tl) and not SENIOR_TITLE.search(title):
        if _min_required_years(desc) is not None:
            my = _min_required_years(desc)
            return False, f"Requires {my}+ years experience"
        if _experienced_desc(desc):
            return False, "Description signals experienced IC, not EC"
        return True, "Software Engineer IC; no minimum YOE stated"

    if re.search(r"\bresearch engineer\b", tl):
        if _min_required_years(desc) is not None:
            my = _min_required_years(desc)
            if my >= 2:
                return False, f"Requires {my}+ years experience"
        if _experienced_desc(desc):
            return False, "Research engineer requires experienced track record"
        if "anthropic" in job.get("company", "").lower():
            return False, "Anthropic research engineer; experienced IC not EC"
        if "cumberland" in tl or "systematic" in tl:
            return False, "Quant research SWE; experienced trading engineering"
        return True, "Research engineer; BS hire without 3+ yr bar"

    if "open-source machine learning engineer" in tl:
        if _experienced_desc(desc):
            return False, "Open-source ML engineer expects experienced background"
        return True, "Open-source ML engineer IC; no minimum YOE stated"

    # Default: no EC signal
    if _min_required_years(desc) is not None:
        my = _min_required_years(desc)
        return False, f"Requires {my}+ years experience"
    if _experienced_desc(desc):
        return False, "Experienced IC; no EC signal in title"

    return False, "No early-career signal in title/description"


def main() -> None:
    jobs = json.loads(BATCH.read_text(encoding="utf-8"))
    assert len(jobs) == 659, len(jobs)

    lines: list[str] = []
    includes = 0
    for i, job in enumerate(jobs):
        inc, reason = label_job(i, job)
        if inc:
            includes += 1
        row = {
            "url": job["url"],
            "manual_include": inc,
            "manual_reason": reason,
        }
        lines.append(json.dumps(row, ensure_ascii=False))

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} labels to {OUT.name}")
    print(f"INCLUDE: {includes}")
    print(f"EXCLUDE: {len(lines) - includes}")
    print("\nIncluded titles:")
    for i, job in enumerate(jobs):
        if label_job(i, job)[0]:
            print(f"  [{i}] {job['title']} | {job['company']}")


if __name__ == "__main__":
    main()
