"""Apply manual judgment corrections to _labels_batch_5.jsonl."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
LABELS = ROOT / "_labels_batch_5.jsonl"

# Explicit manual judgments after reading title/location/description for each job.
CORRECTIONS: dict[str, tuple[bool, str]] = {
    # --- INCLUDES (early-career AND technical) ---
    "https://databricks.com/company/careers/open-positions/job?gh_jid=7640776002": (
        True,
        "Software Engineering New Grad 2026; BS grad fall 2025–summer 2026",
    ),
    "https://jobs.ashbyhq.com/benchling/c83238cc-1f7c-4216-b2a5-418306ca4d2b": (
        True,
        "New grad SWE: BS/MS enrollment, graduation Summer 2026, prior SWE internship",
    ),
    "https://jobs.ashbyhq.com/benchling/815d941c-dff6-40cb-8307-57695acb37a7": (
        True,
        "SWE Agents role requires 2+ years professional SWE (within 0–2yr band)",
    ),
    # --- EXCLUDE corrections (fix heuristic false positives) ---
    "https://databricks.com/company/careers/open-positions/job?gh_jid=8012691002": (
        False,
        "requires 3+ years production Java/Scala/C++ experience",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5755093004": (
        False,
        "Core C++ SWE mid-level role ($141k+); no early-career signal",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5767816004": (
        False,
        "Core C++ SWE mid-level role; no early-career signal",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5755092004": (
        False,
        "Core C++ SWE mid-level role; no early-career signal",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5755091004": (
        False,
        "Core C++ SWE mid-level role; no early-career signal",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5654023004": (
        False,
        "QA Engineer; description truncated but no early-career qualification visible",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5654026004": (
        False,
        "QA Engineer; description truncated but no early-career qualification visible",
    ),
    "https://job-boards.greenhouse.io/clickhouse/jobs/5802967004": (
        False,
        "Product Security Engineer; experienced hire, no EC qualification",
    ),
    "https://jobs.ashbyhq.com/benchling/14002943-e011-425c-8f72-3c727c543668": (
        False,
        "Full Stack Enterprise Lifecycle SWE; mid-level scope, no EC qualification in posting",
    ),
    "https://jobs.ashbyhq.com/benchling/671d4911-7cb5-41da-9bb0-e497fa1874f8": (
        False,
        "Developer Enablement SWE; qualifications truncated, no EC signal in available text",
    ),
    "https://jobs.lever.co/enveda/c14d0b11-a2a5-4411-ae5f-52cc33c6707c": (
        False,
        "Software Engineer; no years/grad requirement stated, general experienced hire",
    ),
    "https://boards.greenhouse.io/andurilindustries/jobs/5042721007?gh_jid=5042721007": (
        False,
        "Product Security Engineer; embedded/firmware security, experienced + TS clearance",
    ),
    "https://boards.greenhouse.io/andurilindustries/jobs/5062357007?gh_jid=5062357007": (
        False,
        "Modeling & Simulation SWE; requires proven sensor-modeling experience",
    ),
}


def main() -> None:
    lines = LABELS.read_text(encoding="utf-8").splitlines()
    labels = [json.loads(ln) for ln in lines if ln.strip()]
    assert len(labels) == 659, f"expected 659 labels, got {len(labels)}"

    for lab in labels:
        url = lab["url"]
        if url in CORRECTIONS:
            inc, reason = CORRECTIONS[url]
            lab["manual_include"] = inc
            lab["manual_reason"] = reason

    with LABELS.open("w", encoding="utf-8") as f:
        for lab in labels:
            f.write(json.dumps(lab, ensure_ascii=False) + "\n")

    inc = sum(1 for l in labels if l["manual_include"])
    print(f"Total: {len(labels)}")
    print(f"Include: {inc}")
    print(f"Exclude: {len(labels) - inc}")
    print("\nIncludes:")
    for l in labels:
        if l["manual_include"]:
            print(f"  {l['url']}")
            print(f"    {l['manual_reason']}")


if __name__ == "__main__":
    main()
