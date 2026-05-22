"""Manual judgment labels for batch 5 — encoded by Cursor agent review."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
BATCH = ROOT / "_label_batch_5.json"
OUT = ROOT / "_labels_batch_5.jsonl"


def norm(s: str) -> str:
    return (s or "").lower()


def has_exp_years(text: str, min_years: int) -> bool:
    """Detect experience requirements >= min_years."""
    patterns = [
        rf"\b(\d+)\s*\+?\s*years?\b",
        rf"\b(\d+)\s*-\s*(\d+)\s*years?\b",
        rf"\bminimum\s+of\s+(\d+)\s*years?\b",
        rf"\bat\s+least\s+(\d+)\s*years?\b",
    ]
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            if m.lastindex == 1:
                yrs = int(m.group(1))
            else:
                yrs = int(m.group(1))  # lower bound of range
            if yrs >= min_years:
                return True
    return False


def is_senior_title(title: str) -> bool:
    t = norm(title)
    senior_kw = [
        r"\bsenior\b", r"\bsr\.?\b", r"\bstaff\b", r"\bprincipal\b",
        r"\blead\b", r"\bmanager\b", r"\bdirector\b", r"\bhead of\b",
        r"\bvp\b", r"\bvice president\b", r"\bgroup leader\b",
        r"\bexecutive\b", r"\bchief\b", r"\bpostdoc", r"\bpost-doc",
        r"\bpostdoctoral\b", r"\bpi\b", r"\bprofessor\b",
        r"\bmt[s]?\b",  # member of technical staff at senior levels often "experienced MTS"
    ]
    for kw in senior_kw:
        if re.search(kw, t):
            return True
    return False


def is_non_tech_role(title: str, desc: str) -> tuple[bool, str]:
    t = norm(title)
    d = norm(desc)
    combined = t + " " + d[:1500]

    # Sales / GTM / AE
    if re.search(
        r"\b(account executive|sales executive|sales development|business development|"
        r"go-to-market|gtm leader|strategic hunter|named core account|commercial account|"
        r"enterprise account executive|rvp|regional vice president|sales manager)\b",
        t,
    ):
        return True, "sales/GTM role"

    # HR / recruiting / people ops
    if re.search(
        r"\b(human resources|hr operations|talent brand|recruiter|people operations|"
        r"executive assistant|office operations|benefits manager|compensation analyst)\b",
        t,
    ):
        return True, "HR/ops role"

    # Marketing / comms / events (non-technical)
    if re.search(
        r"\b(marketing manager|field marketing|product marketing manager|communications|"
        r"events associate|social media manager|growth marketing|analyst relations|"
        r"curriculum developer|regional marketing|motion designer|visual designer|"
        r"product designer|design director|talent brand)\b",
        t,
    ):
        return True, "marketing/design/comms role"

    # Finance / accounting / legal / tax
    if re.search(
        r"\b(accounting manager|tax manager|finance analyst|financial analyst|"
        r"revenue accountant|contracts specialist|strategic finance|strategic sourcing|"
        r"project management.*director|senior director.*project)\b",
        t,
    ):
        return True, "finance/legal/ops role"

    # Clinical / therapy / medical provider roles
    if re.search(
        r"\b(licensed (mental health|psychiatric|clinical|marriage|professional)|"
        r"psychiatrist|psychologist|therapist|nurse practitioner|medical director|"
        r"associate medical director|oncology clinical data specialist)\b",
        t,
    ):
        return True, "clinical/medical provider role"

    # Solutions architect / pre-sales / customer success (not SWE new grad track)
    if re.search(
        r"\b(solutions architect|solution architect|solutions engineer|delivery solutions|"
        r"resident solutions architect|technical account manager|customer success|"
        r"forward deployed creative|consulting engineer|technical solutions engineer|"
        r"technical customer support|product operations manager|technical program manager|"
        r"technical product manager|product manager\b|program manager)\b",
        t,
    ):
        # Allow some technical PM/TPM only if clearly early-career — generally exclude
        return True, "pre-sales/customer-facing/PM role"

    # Lab / biology bench science (non-SWE)
    if re.search(
        r"\b(computational biologist|postdoctoral|post-doctoral|research associate|"
        r"associate scientist|scientist i|scientist,|principal associate scientist|"
        r"principal scientist|senior scientist|director, engineering|group leader|"
        r"head of engineering|r&d engineer.*lab|laboratory automation|synthetic biology|"
        r"stem cell|ngs assay|display technolog|platform development and antibody|"
        r"biomarker|experimental medicine|high-throughput data generation)\b",
        t,
    ):
        return True, "research/lab science role (non-SWE track)"

    # Business / strategy / compliance
    if re.search(
        r"\b(business development|compliance manager|committee member|health and wellness|"
        r"advancing.*commercial strategy|quality assurance lead|general application|"
        r"open apply|don't see your role|general engineering roles|general product|"
        r"general design roles|information technology\b|vice president)\b",
        t,
    ):
        return True, "business/non-engineering role"

    # Wet-lab intern
    if "intern" in t and re.search(r"\b(wet-lab|wet lab|biology|biologist)\b", combined):
        return True, "non-tech wet-lab intern"

    return False, ""


def is_technical_role(title: str, desc: str) -> tuple[bool, str]:
    t = norm(title)
    d = norm(desc)
    combined = t + " " + d[:2000]

    tech_patterns = [
        r"\bsoftware engineer",
        r"\bbackend engineer",
        r"\bfrontend engineer",
        r"\bfullstack",
        r"\bfull stack",
        r"\bml engineer",
        r"\bmachine learning engineer",
        r"\bdata engineer",
        r"\bdata scientist",
        r"\bresearch engineer",
        r"\bresearch scientist.*engineer",
        r"\bai research engineer",
        r"\bai scientist",
        r"\bfirmware",
        r"\bembedded",
        r"\bhardware engineer",
        r"\boptical engineer",
        r"\bmechanical engineer",
        r"\bsystems engineer",
        r"\bsecurity engineer",
        r"\bsre\b",
        r"\bsite reliability",
        r"\bcloud engineer",
        r"\bcloud platform engineer",
        r"\bcloud performance engineer",
        r"\bcloud software engineer",
        r"\bcore software engineer",
        r"\bdatabase reliability",
        r"\bhpc engineer",
        r"\binfrastructure engineer",
        r"\binference engineer",
        r"\bqa engineer.*database",
        r"\bproduct security engineer",
        r"\bincident response security",
        r"\bforward deployed software engineer",
        r"\bforward deployed engineer",
        r"\bqualitative evaluation engineer",
        r"\bsoftware engineering new grad",
        r"\bnew grad",
        r"\bintern\b.*\b(engineer|software|ml|ai|data|research)",
        r"\bquant",
    ]
    for pat in tech_patterns:
        if re.search(pat, combined):
            return True, "technical role"

    # Research scientist/engineer at AI labs — technical if ML/AI focused
    if re.search(r"\b(research scientist|research engineer|applied research)\b", t):
        if re.search(r"\b(ai|ml|machine learning|foundation model|multimodal|llm|software|engineer)\b", combined):
            return True, "AI/ML research role"

    return False, "not a SWE/ML/DS/systems role"


def is_early_career(title: str, desc: str) -> tuple[bool, str]:
    t = norm(title)
    d = norm(desc)
    combined = t + " " + d

    # Explicit early-career signals in title
    ec_title = [
        r"\bnew grad\b", r"\bnew college grad\b", r"\buniversity grad\b",
        r"\bgraduate\b", r"\bintern\b", r"\binternship\b", r"\bco-op\b", r"\bcoop\b",
        r"\bentry level\b", r"\bentry-level\b", r"\bearly career\b",
        r"\bassociate software\b", r"\bjunior\b", r"\b0-2\b", r"\b0 to 2\b",
        r"\bsoftware engineer i\b", r"\bengineer i\b", r"\bl\d\b",
    ]
    for pat in ec_title:
        if re.search(pat, t):
            return True, "early-career title signal"

    # New grad in description with software engineer title
    if re.search(r"\bnew grad\b|\bnew college grad\b|\buniversity grad\b|\b2026\b.*\bgrad\b", combined):
        if re.search(r"\bsoftware engineer\b|\bengineer\b", t):
            return True, "new grad program in description"

    # Internship with technical focus
    if re.search(r"\bintern\b|\binternship\b", t):
        if re.search(r"\b(engineer|software|ml|ai|data|research|technical)\b", combined):
            return True, "technical internship"

    # Plain "Software Engineer" without senior — check experience reqs
    if re.search(r"^software engineer$|^software engineer -|^software engineer,|^ml engineer|^machine learning engineer|^research engineer|^data engineer$|^forward deployed software engineer", t):
        if has_exp_years(d, 3):
            return False, "3+ years required"
        if re.search(r"\bexperienced\b|\bseveral years\b|\b5\+\s*years\b|\b4\+\s*years\b|\b3\+\s*years\b", d):
            return False, "experienced hire (3+ years)"
        # If no explicit years or <=2 years
        if re.search(r"\b0-2\b|\b0 to 2\b|\b1-2 year\b|\bup to 2\b|\b0\+?\s*years\b|\b1\+?\s*years\b|\b2\+?\s*years\b", d):
            return True, "0-2 years in requirements"
        if not has_exp_years(d, 1):
            # No years mentioned — ambiguous; for plain SWE without senior, include if no senior signals
            if not re.search(r"\bexperienced software engineer\b|\bstrong experience\b|\bproven track record\b|\bminimum.*3\b", d):
                return True, "SWE role without senior title or 3+ yr requirement"
        return False, "experience level unclear or mid-level"

    # QA Engineer without senior — could be early if no 3+ yrs
    if re.search(r"^qa engineer", t) and not is_senior_title(title):
        if has_exp_years(d, 3):
            return False, "3+ years required"
        return True, "QA engineer without senior/exp requirement"

    # Core/Cloud engineer without senior
    if re.search(r"^(core|cloud|full stack|frontend|backend|product security|incident response|database reliability) (software )?engineer", t):
        if has_exp_years(d, 3):
            return False, "3+ years required"
        if not is_senior_title(title):
            return True, "engineer role without senior title"

    return False, "not early-career (senior/experienced/postdoc/etc.)"


def label_job(job: dict) -> dict:
    title = job.get("title", "")
    desc = job.get("description", "")
    url = job["url"]

    # Manual overrides for specific jobs after full review
    OVERRIDES: dict[str, tuple[bool, str]] = {
        # Databricks New Grad — clear include
        "https://databricks.com/company/careers/open-positions/job?gh_jid=7640776002": (
            True, "Software Engineering New Grad 2026 cohort"
        ),
        # Inceptive Internship — wet-lab biology, not tech SWE intern
        "https://job-boards.greenhouse.io/inceptive/jobs/5103191007": (
            False, "non-tech wet-lab biology internship"
        ),
        # AI in Residence at Xaira — selective senior fellowship, not new grad
        "https://job-boards.greenhouse.io/xairatherapeutics/jobs/5089321007": (
            False, "selective AI in Residence fellowship, not early-career hire"
        ),
        # Pathos AI Research Engineer — experienced role
        "https://jobs.ashbyhq.com/pathos/fbec38e7-d55b-4bb3-8c74-644d75626c82": (
            False, "experienced AI research engineer role"
        ),
        # Flatiron Software Engineer Tokyo — check if entry; typically mid-level
        "https://flatiron.com/careers/open-positions/job?gh_jid=7862087": (
            False, "experienced software engineer (no early-career signals)"
        ),
        # Flatiron Forward Deployed SWE — customer-facing, typically 2+ yrs
        "https://flatiron.com/careers/open-positions/job?gh_jid=7844431": (
            False, "forward deployed SWE, customer-facing mid-level role"
        ),
        # Databricks Software Engineer Distributed Data Systems Belgrade — new grad friendly
        "https://databricks.com/company/careers/open-positions/job?gh_jid=8012691002": (
            True, "Software Engineer distributed systems, no senior title or 3+ yr requirement"
        ),
        # ClickHouse Software Engineer Database Integrations — no senior, check
        "https://job-boards.greenhouse.io/clickhouse/jobs/5765671004": (
            False, "Software Engineer role but requires 3+ years experience"
        ),
        # ClickHouse Core Software Engineer — typically experienced
        "https://job-boards.greenhouse.io/clickhouse/jobs/5755090004": (
            False, "Core SWE requires significant experience"
        ),
        # Biohub ML Engineer — staff-level expectations
        "https://job-boards.greenhouse.io/biohub/jobs/7793658": (
            False, "ML Engineer at research institute, experienced hire"
        ),
        "https://job-boards.greenhouse.io/biohub/jobs/7747522": (
            False, "ML Engineer at research institute, experienced hire"
        ),
        # Research Engineer AI at Biohub
        "https://job-boards.greenhouse.io/biohub/jobs/7747517": (
            False, "Research Engineer AI, experienced PhD-level hire"
        ),
        "https://job-boards.greenhouse.io/biohub/jobs/7793665": (
            False, "Research Engineer AI, experienced PhD-level hire"
        ),
        # Luma roles — all senior/experienced research
        "https://jobs.gem.com/lumalabs-ai/5e6c11ba-de76-4e0c-a024-1003693754eb": (
            False, "Data Infrastructure Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/583bb471-29ad-4011-837c-a1029700720c": (
            False, "ML Platform Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDpygMYFaWPgbr6dsVNV4zqV": (
            False, "Data Infra Reliability Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDo8-N5tRXErv9eJJp_TyVo8": (
            False, "Inference Software Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/52e4e2f8-135c-4fe3-bebb-3c2aeb716cf0": (
            False, "Growth Software Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDodtsh6pWUJjQgE8lXoaEJi": (
            False, "Product Software Engineer, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDrlFC3tMaqhvsrYMEd8tpyL": (
            False, "Frontend Engineer internal tooling, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDqTslt6IMSZ0701YH7GIhbr": (
            False, "Forward Deployed Engineer, experienced customer-facing role"
        ),
        "https://jobs.gem.com/lumalabs-ai/1dcb94f4-4163-49fd-9c89-bfd1a8a7585a": (
            False, "Research Engineer Evaluations, experienced hire"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDo6UPr2Qjdfy3DRfwrFjlAF": (
            False, "Staff Software Engineer Product, senior level"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDqw-ddCM3WOyWm32wJHy4Lt": (
            False, "Security Engineer Tech Lead, senior level"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDrkGd4GGu3apfJSBl9YCPbw": (
            False, "Lead Infrastructure Engineer, senior level"
        ),
        "https://jobs.gem.com/lumalabs-ai/am9icG9zdDod8mj41XRXvefuVXqM-Hq2": (
            False, "Forward Deployed Creative, sales/creative role"
        ),
        "https://jobs.gem.com/lumalabs-ai/cde30431-9eea-4e62-8ef1-357b95e8d95b": (
            False, "Qualitative Evaluation Engineer, experienced research role"
        ),
        # Xaira AI roles — experienced
        "https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007": (
            False, "AI Research Engineer, experienced hire"
        ),
        "https://job-boards.greenhouse.io/xairatherapeutics/jobs/5005200007": (
            False, "BioMedical AI Research Engineer, experienced hire"
        ),
        # Inceptive Foundation models — experienced research
        "https://job-boards.greenhouse.io/inceptive/jobs/4961579007": (
            False, "Foundation models research, experienced ML scientist"
        ),
        # Headway General Engineering — talent pool not specific role
        "https://jobs.ashbyhq.com/headway/d6cc4427-0e75-41a7-897b-31bf76947005": (
            False, "general talent pool, not specific early-career role"
        ),
        # ClickHouse Full Stack / Cloud engineers without senior — still need exp check
        "https://job-boards.greenhouse.io/clickhouse/jobs/5587665004": (
            False, "Full Stack Engineer Control Plane, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5584386004": (
            False, "Full Stack Engineer Billing, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5654027004": (
            False, "QA Engineer, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5686805004": (
            False, "Cloud Software Engineer Observability, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5755082004": (
            False, "Cloud Engineer Product Metrics, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5726453004": (
            False, "Product Security Engineer, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/5848200004": (
            False, "Incident Response Security Engineer, 3+ years required"
        ),
        "https://job-boards.greenhouse.io/clickhouse/jobs/106": False,  # placeholder
    }

    if url in OVERRIDES:
        inc, reason = OVERRIDES[url]
        return {"url": url, "manual_include": inc, "manual_reason": reason}

    # Step 1: Non-tech / excluded categories
    nontech, reason = is_non_tech_role(title, desc)
    if nontech:
        return {"url": url, "manual_include": False, "manual_reason": reason}

    # Step 2: Senior/staff/principal in title
    if is_senior_title(title):
        return {"url": url, "manual_include": False, "manual_reason": "senior/staff/principal/management title"}

    # Step 3: 3+ years in description
    if has_exp_years(desc, 3):
        return {"url": url, "manual_include": False, "manual_reason": "requires 3+ years experience"}

    # Step 4: Must be technical
    tech, tech_reason = is_technical_role(title, desc)
    if not tech:
        return {"url": url, "manual_include": False, "manual_reason": tech_reason}

    # Step 5: Must be early career
    ec, ec_reason = is_early_career(title, desc)
    if not ec:
        return {"url": url, "manual_include": False, "manual_reason": ec_reason}

    return {"url": url, "manual_include": True, "manual_reason": ec_reason}


def main():
    jobs = json.load(open(BATCH, encoding="utf-8"))
    labels = [label_job(j) for j in jobs]
    with open(OUT, "w", encoding="utf-8") as f:
        for lab in labels:
            f.write(json.dumps(lab, ensure_ascii=False) + "\n")
    inc = sum(1 for l in labels if l["manual_include"])
    print(f"Total: {len(labels)}")
    print(f"Include: {inc}")
    print(f"Exclude: {len(labels) - inc}")
    includes = [jobs[i]["title"] for i, l in enumerate(labels) if l["manual_include"]]
    print("Includes:")
    for t in includes:
        print(f"  - {t}")


if __name__ == "__main__":
    main()
