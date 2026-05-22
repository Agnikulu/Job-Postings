"""Manual labels for batch 3 — judgment applied per job, no LLM API."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
BATCH = ROOT / "_label_batch_3.json"
OUT = ROOT / "_labels_batch_3.jsonl"

# Explicit per-index overrides after rule pass (index -> (include, reason))
OVERRIDES: dict[int, tuple[bool, str]] = {
    # Mistral — SWE frontend has no year floor; research roles need track record
    19: (True, "Software Engineer Frontend IC; no minimum YOE in requirements"),
    27: (False, "AI Scientist Robotics needs hands-on deployed AI/robotics track record, not EC"),
    # Vercel — backend/next.js SWE with no explicit YOE floor
    87: (True, "Software Engineer Backend IC; no minimum YOE stated"),
    95: (True, "Software Engineer Next.js IC; no minimum YOE stated"),
    # ElevenLabs — no-degree SWE roles
    261: (True, "Full-Stack Engineer; no formal experience required"),
    264: (True, "Full-Stack Growth Engineer; no formal experience required"),
    273: (True, "Full-Stack Engineer backend-leaning; no formal experience required"),
    244: (True, "Forward Deployed SWE; student/side-project customer experience acceptable"),
    245: (True, "Forward Deployed SWE Spain; student/side-project customer experience acceptable"),
    # Warp
    334: (True, "Product Engineer IC; no minimum YOE stated"),
    # Glean — IC SWE/infra without YOE floor; CA trainee is finance not SWE
    341: (False, "CA Industrial Trainee is accounting/finance trainee, not technical"),
    343: (True, "Software Engineer Developer Productivity; no minimum YOE stated"),
    352: (True, "Software Engineer Fullstack; no minimum YOE stated"),
    365: (True, "Software Engineer Frontend; no minimum YOE stated"),
    411: (True, "Cloud Infrastructure Engineer; no minimum YOE stated"),
    417: (True, "Software Engineer Product Backend; no minimum YOE stated"),
    427: (True, "Cloud Security Engineer; no minimum YOE stated"),
    # Hebbia
    448: (True, "Backend Engineer Agents IC; no minimum YOE stated"),
    449: (True, "Applied Research Engineer Agents; no minimum YOE stated"),
    # Clay
    481: (True, "Software Engineer Developer Experience AI; no minimum YOE stated"),
    486: (True, "Software Engineer Backend; no minimum YOE stated"),
    # Retool
    559: (True, "Software Engineer Core Infrastructure; no minimum YOE stated"),
    # Figma
    618: (True, "Data Scientist PhD 2026 new-grad pipeline role"),
    620: (False, "Inside Sales Representative Early Career is sales, not technical"),
    # Etched full-time roles that look EC-open but require prior production/specialist experience
    145: (False, "Accelerator SWE requires shipped production firmware/driver experience"),
    154: (False, "Inference SWE expects accelerator porting and distributed-systems depth"),
    159: (False, "Performance Profiling SWE is senior tooling role, not EC"),
    170: (False, "Supercomputing SWE Taiwan expects experienced systems/firmware background"),
    199: (False, "Chip Simulation SWE full-time role without EC signals"),
    226: (False, "DV Internal IP requires hands-on UVM/SV verification experience"),
    456: (False, "Site Reliability Engineer requires 5+ years"),
    # Research/scientist roles needing track record, not new-grad EC
    0: (False, "Applied Scientist needs expert ML track record, not EC"),
    23: (False, "Discovery Scientists requires domain publications/research track record"),
    # Sales / GTM / ops misclassified as technical EC
    107: (False, "Vercel Development Representative is outbound sales, not SWE"),
    251: (False, "Product & Platform Partnerships is biz-dev, not IC engineering"),
    280: (False, "Impact Strategy & Operations is program/ops, not technical IC"),
    287: (False, "Data Operations is ops/analytics support, not SWE/ML IC"),
    465: (False, "Account Development Representative is sales outbound"),
    475: (False, "Product Design is design role, not SWE/ML IC"),
    488: (False, "Data Partnerships is business partnerships, not engineering"),
    497: (False, "Founding Marketer is marketing, not technical"),
    498: (False, "Data Analyst is analytics, not SWE/ML IC"),
    517: (False, "Technical Partnerships Engineer is partnerships/GTM, not product SWE"),
    535: (False, "GTME Community Strategy & Ops is GTM ops, not engineering"),
    536: (False, "GTME & AI Teacher is enablement/training, not engineering"),
    537: (False, "GTME Create Your Own Role is GTM ecosystem, not engineering"),
    545: (False, "GTM Engineer CX is revenue/customer GTM tooling, not product SWE"),
    640: (False, "Designer Advocate is design/marketing advocacy, not SWE"),
    608: (False, "Enterprise Support Specialist is customer support, not SWE"),
    # Experienced hardware/infra full-time without EC signals
    148: (False, "Power Validation Engineer expects deep PDN/bench experience"),
    161: (False, "Supercomputing Engineer Network expects datacenter networking experience"),
    164: (False, "Platform Validation Engineer expects hardware validation experience"),
    166: (False, "Mechanical DFM Engineer expects manufacturing/DFM experience"),
    171: (False, "Design Verification Engineer SoC expects experienced DV background"),
    179: (False, "Lab Operations expects 3+ years lab/ops experience"),
    192: (False, "Supercomputing Engineer Test expects burn-in/reliability experience"),
    203: (False, "Developer Experience Engineer expects mature DX/platform experience"),
    225: (False, "Security Engineer expects production security/SIEM experience"),
    # Hebbia / ElevenLabs / Figma experienced ICs
    263: (False, "ElevenLabs Data Engineer expects early-team scaling/data pipeline ownership"),
    444: (False, "Hebbia Data Engineer requires 5+ years"),
    445: (False, "Hebbia Platform Engineer requires 5+ years"),
    446: (False, "Hebbia Backend Engineer Growth requires 5+ years"),
    447: (False, "Hebbia Backend Agent Platform requires 5+ years"),
    524: (False, "Clay Security Engineer expects experienced appsec background"),
    607: (False, "Figma Data Platform Engineer requires 5+ years"),
    613: (False, "Figma Data Engineer expects experienced data infra background"),
}

NON_TECH_TITLE = re.compile(
    r"\b("
    r"account executive|account manager|sales development|sdr|bdr|vdr|"
    r"recruiter|recruiting|hr\b|human resources|people partner|people operations|"
    r"talent|workplace ops|executive assistant|counsel|legal|accountant|accounting|"
    r"fp&a|finance|payroll|accounts payable|accounts receivable|revenue accountant|"
    r"marketing|communications|events manager|brand designer|motion designer|"
    r"product marketing|developer marketing|growth generalist|growth content|"
    r"deal desk|deal strategy|chief of staff|general manager|"
    r"customer success|customer support specialist|customer experience specialist|"
    r"product support|technical recruiter|gtm recruiter|sales recruiter|"
    r"deployment strategist|ai strategist|ai deployment strategist|"
    r"business development|partner manager|partner sales|partner lead|"
    r"revenue partnerships|strategic business development|"
    r"inside sales|solutions consultant|designer, web|product designer|"
    r"design engineer(?!\s*,)|web developer|brand designer|"
    r"translator|linguist|dubbing|audio engineering|creative producer|"
    r"workplace operations|ap specialist|executive sourcer|"
    r"industrial trainee|lab technician|pcb rework technician|"
    r"technical recruiter|founding recruiter|founding sourcer|"
    r"gtm enablement|enablement program|trainer, gtm|"
    r"media engineer, social|corporate events|field marketing|"
    r"lifecycle marketing|integrated campaign|launch strategy|"
    r"compensation partner|it audit|business systems analyst|"
    r"pricing strategic|gtm strategic finance|strategic finance|"
    r"revenue operations|revops|sales compensation|"
    r"ai outcomes manager|ai success manager|business value consultant|"
    r"technical delivery|forward deployed banker|forward deployed investor|"
    r"client partner|growth strategist|"
    r"product manager(?!\s*,\s*intern)|product design lead|"
    r"engineering manager|tech lead manager|manager,|director|head of|"
    r"regional vice president|rvp|vice president|vp\b|"
    r"principal product|staff accountant|staff brand|staff product manager|"
    r"senior / staff|senior counsel|senior accountant|senior manager|"
    r"senior partner|senior product|senior communications|senior hr|"
    r"senior legal|senior corporate|senior integrated|senior escalation|"
    r"senior business development|senior payroll|senior technical program|"
    r"senior solutions consultant|senior account executive|"
    r"sr\.|group leader|\bpi\b|"
    r"program manager(?!\s*,\s*intern)|technical program manager|"
    r"contract manufacturing manager|materials program manager|"
    r"manufacturing engineering lead|lab operations manager|"
    r"asic technical program manager|head of manufacturing|"
    r"global supply manager|global benefits|"
    r"gtm engineer(?!\s*-)|gtm ops|gtm systems|"
    r"developer advocate|technical marketing|"
    r"design engineer|site engineer|mobile engineer|"
    r"developer success engineer|solutions architect|solutions engineer|"
    r"enterprise solutions engineer|partner solutions|"
    r"forward.?deployed engineer|forward deployed gtme|"
    r"it ops engineer|it engineer|technical support engineer|"
    r"quality assurance lead|quality assurance engineer|"
    r"compliance engineer"
    r")\b",
    re.I,
)

SENIOR_TITLE = re.compile(
    r"\b(senior|staff|principal|sr\.|lead(?!\s*product counsel)|"
    r"director|head of|vp |vice president|manager|"
    r"experienced mts|\bmts\b|group leader|\bpi\b)\b",
    re.I,
)

EC_TITLE = re.compile(
    r"\b(intern|internship|new grad|graduate|entry.?level|early.?career|"
    r"early career|campus|university|0.?2\s*y|0-2|associate\b|junior|"
    r"trainee|2026|2027)\b",
    re.I,
)

TECH_TITLE = re.compile(
    r"\b("
    r"software engineer|full.?stack|fullstack|backend engineer|frontend engineer|"
    r"product engineer|platform engineer|infrastructure engineer|"
    r"cloud infrastructure|cloud security|security engineer|"
    r"application security|machine learning engineer|ml engineer|"
    r"data scientist|data engineer|applied research|applied scientist|"
    r"research engineer|ai scientist|ai applied scientist|"
    r"developer experience|developer productivity|"
    r"firmware|embedded|rtl|design verification|\bdv\b|\bdft\b|"
    r"physical design|\bpd\b|asic|inference|supercomputing|"
    r"accelerator software|chip sim|chip simulation|"
    r"performance profiling|agentic runtime|"
    r"quality assurance engineer|qa engineer|"
    r"site reliability|sre\b|"
    r"hardware|electrical engineer|mechanical engineer|"
    r"thermo|cfd|inference intern|electrical platform|"
    r"chipsim|rtl intern|pd intern|"
    r")\b",
    re.I,
)

NON_TECH_INTERN = re.compile(
    r"\b(gtm intern|finance intern|core ops intern|talent intern|"
    r"marketing intern|sales intern|hr intern|recruiting intern)\b",
    re.I,
)

TECH_INTERN = re.compile(
    r"\b("
    r"firmware intern|dv intern|dft intern|rtl intern|pd intern|"
    r"inference intern|infrastructure intern|supercomputing intern|"
    r"chipsim intern|chip simulation software intern|chip sim intern|"
    r"electrical platform intern|thermo.?mech.*intern|mech\s*/\s*thermal intern"
    r")\b",
    re.I,
)

MIN_YEARS = re.compile(
    r"(?:minimum|at least|require[sd]?|must have|"
    r"(?<!\d)(?:\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp))"
    r"|(?:\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)",
    re.I,
)


def _min_required_years(desc: str) -> int | None:
    """Return minimum years if clearly required (conservative for EC)."""
    d = desc.lower()
    mins: list[int] = []
    patterns = [
        r"(?:minimum|at least|require[sd]?)\s*(?:of\s+)?(\d+)\+?\s*(?:years?|yrs?)",
        r"(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)",
        r"(\d+)\+?\s*(?:years?|yrs?)\s+in\s+",
        r"(\d+)\+?\s*(?:years?|yrs?)\s+as\s+",
        r"(\d+)\+?\s*(?:years?|yrs?)\s+of\s+",
        r"(\d+)\s*[-–]\s*(\d+)\s+years",
    ]
    for pat in patterns:
        for m in re.finditer(pat, d):
            g = m.groups()
            if len(g) == 2 and g[1]:
                mins.append(int(g[0]))
            elif g[0]:
                mins.append(int(g[0]))
    # "1-5 years" style — use lower bound for EC check
    for m in re.finditer(r"(\d+)\s*[-–]\s*(\d+)\s+years", d):
        mins.append(int(m.group(1)))
    if not mins:
        return None
    return min(mins)


def _is_non_tech(title: str) -> bool:
    t = title.lower()
    if NON_TECH_INTERN.search(t):
        return True
    if TECH_INTERN.search(t):
        return False
    if TECH_TITLE.search(t) and not NON_TECH_TITLE.search(t):
        return False
    return bool(NON_TECH_TITLE.search(t))


def _is_technical(title: str, desc: str) -> bool:
    t = title.lower()
    if TECH_INTERN.search(t):
        return True
    if NON_TECH_INTERN.search(t):
        return False
    if TECH_TITLE.search(t):
        # Exclude if title is primarily non-tech despite tech words
        if _is_non_tech(title):
            # FDE SWE is technical
            if "forward deployed" in t and "engineer" in t and "software" in t:
                return True
            if "software engineer" in t or "full-stack" in t or "fullstack" in t:
                return True
            return False
        return True
    return False


def _is_early_career(title: str, desc: str) -> bool:
    t = title.lower()
    d = desc.lower()

    if NON_TECH_INTERN.search(t):
        return False
    if TECH_INTERN.search(t):
        return True
    if EC_TITLE.search(t):
        return True

    # Explicit no-experience-required signals
    if "do not require any formal experience" in d:
        return True
    if "no formal experience" in d and "require" in d:
        return True
    if "0–2 years" in d or "0-2 years" in d:
        return True
    if "recent grad" in d or "new grad" in d:
        return True
    if "internship experience can be considered" in d:
        return True
    if "first-author publications" in d or "track record of success through personal projects" in d:
        return False
    if "early data engineer" in d or "one of the first or early data engineers" in d:
        return False

    # Etched entry-level recruiter
    if "entry level" in t and "recruiter" in t:
        return True

    mins = _min_required_years(d)
    if mins is not None:
        if mins >= 3:
            return False
        if mins >= 2:
            return False  # 2+ minimum excludes new grads / 0-1 YOE
        return True

    # No explicit year requirement — EC-friendly for IC tech roles
    if SENIOR_TITLE.search(t):
        return False
    if "significant experience" in d or "highly experienced" in d:
        return False
    if "highly skilled" in d and "intern" not in t:
        return False
    if "experience shipping" in d and "products that have gone to production" in d:
        return False
    if "proven track record of leading teams" in d:
        return False
    if "7+" in d or "8+" in d or "10+" in d:
        return False
    if "hands-on experience verifying" in d:
        return False

    return True


def label_job(idx: int, job: dict) -> tuple[bool, str]:
    if idx in OVERRIDES:
        return OVERRIDES[idx]

    title = job["title"]
    desc = job.get("description") or ""
    tl = title.lower()

    # Hard excludes from title
    if SENIOR_TITLE.search(title) and not TECH_INTERN.search(title):
        if "entry level" not in tl:
            return False, "Senior/staff/principal/lead/manager/MTS title"

    if NON_TECH_INTERN.search(title):
        return False, "Non-technical intern (GTM/finance/ops/talent)"

    if _is_non_tech(title) and not (
        "software engineer" in tl
        or "full-stack" in tl
        or "fullstack" in tl
        or "machine learning" in tl
        or "data scientist" in tl
        or TECH_INTERN.search(title)
    ):
        return False, "Non-technical role (sales/HR/marketing/ops/legal/finance/GTM)"

    if not _is_technical(title, desc):
        return False, "Not a technical SWE/ML/DS/hardware/firmware role"

    if TECH_INTERN.search(title):
        return True, "Technical intern (firmware/DV/RTL/infra/simulation/etc.)"

    if not _is_early_career(title, desc):
        mins = _min_required_years(desc)
        if mins and mins >= 3:
            return False, f"Requires {mins}+ years experience"
        if mins and mins >= 2:
            return False, f"Requires {mins}+ years minimum (above 0-2yr EC band)"
        if SENIOR_TITLE.search(title):
            return False, "Senior/staff/principal/lead title"
        return False, "Not early-career (experienced IC or unclear YOE floor)"

    return True, "Early-career technical IC role"


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


if __name__ == "__main__":
    main()
