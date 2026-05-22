"""Merge batch labels into cursor_eval_labels.jsonl and print summary."""
from __future__ import annotations

import glob
import json
from collections import Counter
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parents[1] / "eval"
BATCH_DIR = EVAL_DIR / "batches"
JOBS_PATH = EVAL_DIR / "cursor_eval_jobs.jsonl"
LABELS_PATH = EVAL_DIR / "cursor_eval_labels.jsonl"


def main() -> None:
    jobs = [json.loads(line) for line in JOBS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    job_urls = {j["url"] for j in jobs}
    labels: dict[str, dict] = {}

    for path in sorted(glob.glob(str(BATCH_DIR / "_labels_batch_*.jsonl"))):
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("url"):
                labels[row["url"]] = row

    labeled_urls = set(labels) & job_urls
    missing = job_urls - set(labels)
    extra = set(labels) - job_urls

    with LABELS_PATH.open("w", encoding="utf-8") as fh:
        for job in jobs:
            url = job["url"]
            if url in labels:
                fh.write(json.dumps(labels[url], ensure_ascii=False) + "\n")

    inc = sum(1 for u in job_urls if labels.get(u, {}).get("manual_include"))
    print(f"Jobs: {len(jobs)}")
    print(f"Labeled: {len(labeled_urls)}")
    print(f"Missing: {len(missing)}")
    print(f"Extra (not in jobs): {len(extra)}")
    print(f"Manual include=true: {inc} ({100*inc/len(jobs):.2f}%)")
    print(f"Wrote {LABELS_PATH.name}")


if __name__ == "__main__":
    main()
