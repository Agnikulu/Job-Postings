"""Apply human-reviewed overrides to cursor_eval_labels.jsonl."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent
LABELS_PATH = ROOT / "cursor_eval_labels.jsonl"

# Human adjudication on regex/manual disagreements and clear rubric fixes.
OVERRIDES: dict[str, tuple[bool, str]] = {
    # --- INCLUDE: regex was right, manual_judge too strict ---
    "https://job-boards.greenhouse.io/togetherai/jobs/5101651007": (
        True,
        "early-career 0-4yr analytics/data engineering",
    ),
    "https://job-boards.greenhouse.io/togetherai/jobs/5074064007": (
        True,
        "early-career 0-4yr data warehouse engineering",
    ),
    "https://job-boards.greenhouse.io/figureai/jobs/4656559006": (
        True,
        "hardware engineer 1-3 years",
    ),
    "https://apply.careers.microsoft.com/careers/job/1970393556655958": (
        True,
        "PhD research intern ML",
    ),
    "https://www.pinterestcareers.com/jobs/?gh_jid=7767046": (
        True,
        "SWE II band, no 3+ year minimum",
    ),
    "https://www.uber.com/careers/list/157638": (
        True,
        "SWE II band role",
    ),
    "https://www.uber.com/careers/list/155564": (
        True,
        "SWE II band role",
    ),
    "https://apply.careers.microsoft.com/careers/job/1970393556621082": (
        True,
        "SWE II band role",
    ),
    "https://apply.careers.microsoft.com/careers/job/1970393556637527": (
        True,
        "SWE II band role",
    ),
    "https://jobs.ashbyhq.com/physicalintelligence/f83ba447-2261-4832-95db-a2f88454e0ba": (
        True,
        "research scientist open to all levels",
    ),
    "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Research-Scientist_R167353": (
        True,
        "research scientist welcomes new graduates",
    ),
    # --- EXCLUDE: manual_judge false positives ---
    "https://boards.greenhouse.io/point72/jobs/8500397002?gh_jid=8500397002": (
        False,
        "finance analyst academy, not technical SWE/ML",
    ),
    "https://boards.greenhouse.io/point72/jobs/8539265002?gh_jid=8539265002": (
        False,
        "finance analyst academy, not technical SWE/ML",
    ),
    "https://boards.greenhouse.io/point72/jobs/8538913002?gh_jid=8538913002": (
        False,
        "finance analyst academy, not technical SWE/ML",
    ),
    "https://boards.greenhouse.io/point72/jobs/8539271002?gh_jid=8539271002": (
        False,
        "finance analyst academy, not technical SWE/ML",
    ),
    "https://jobs.ashbyhq.com/runway-ml/2ca5c5d1-725d-4c44-907b-5d808ec248fe": (
        False,
        "non-technical creative support",
    ),
    "https://job-boards.greenhouse.io/gleanwork/jobs/4665628005": (
        False,
        "non-technical CA trainee",
    ),
    "https://job-boards.greenhouse.io/figureai/jobs/4671442006": (
        False,
        "staff/senior IC role",
    ),
    "https://databricks.com/company/careers/open-positions/job?gh_jid=8476500002": (
        False,
        "solutions architect customer-facing",
    ),
    "https://job-boards.greenhouse.io/biohub/jobs/7902395": (
        False,
        "wet-lab postdoc, not SWE",
    ),
    "https://job-boards.greenhouse.io/biohub/jobs/7779105": (
        False,
        "wet-lab postdoc, not SWE",
    ),
    "https://job-boards.greenhouse.io/biohub/jobs/7769739": (
        False,
        "wet-lab postdoc, not SWE",
    ),
    "https://job-boards.greenhouse.io/biohub/jobs/7769713": (
        False,
        "wet-lab postdoc, not SWE",
    ),
    "https://job-boards.greenhouse.io/biohub/jobs/7922556": (
        False,
        "wet-lab postdoc, not SWE",
    ),
    "https://jobs.ashbyhq.com/headway/3e71f549-4318-48ff-9be6-57ffc5f3aece": (
        False,
        "staff product designer, non-tech",
    ),
    "https://careers.roblox.com/jobs/7779304?gh_jid=7779304": (
        False,
        "non-technical design fellowship",
    ),
    "https://job-boards.greenhouse.io/discord/jobs/8445676002": (
        False,
        "product designer, non-tech",
    ),
    "https://job-boards.greenhouse.io/doordashusa/jobs/7014816": (
        False,
        "staff product designer, non-tech",
    ),
    "https://job-boards.greenhouse.io/doordashusa/jobs/7517534": (
        False,
        "FPV pilot, non-SWE",
    ),
    "https://job-boards.greenhouse.io/doordashusa/jobs/7898797": (
        False,
        "marketing associate, non-tech",
    ),
}


def main() -> None:
    lines = []
    changed = 0
    for line in LABELS_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        url = row["url"]
        if url in OVERRIDES:
            inc, reason = OVERRIDES[url]
            if row["manual_include"] != inc or row["manual_reason"] != reason:
                changed += 1
            row["manual_include"] = inc
            row["manual_reason"] = reason
        lines.append(json.dumps(row, ensure_ascii=False))

    LABELS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    inc = sum(1 for l in lines if json.loads(l)["manual_include"])
    print(f"overrides applied: {changed} urls touched: {len(OVERRIDES)}")
    print(f"total: {len(lines)} include: {inc} exclude: {len(lines)-inc}")


if __name__ == "__main__":
    main()
