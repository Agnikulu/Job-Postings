"""Label all cursor_eval_jobs in 200-job chunks (incremental write)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from _rigorous_manual_label import manual_judge

ROOT = Path(__file__).parent
JOBS_PATH = ROOT / "cursor_eval_jobs.jsonl"
LABELS_PATH = ROOT / "cursor_eval_labels.jsonl"
CHUNK = 200


def main() -> int:
    jobs = [
        json.loads(line)
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    total = len(jobs)
    include_count = 0
    labeled = 0

    with LABELS_PATH.open("w", encoding="utf-8") as fh:
        for start in range(0, total, CHUNK):
            chunk = jobs[start : start + CHUNK]
            for job in chunk:
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
                labeled += 1
            fh.flush()
            end = min(start + CHUNK, total)
            print(f"chunk {start // CHUNK + 1}: labeled {end}/{total}", flush=True)

    exclude_count = labeled - include_count
    print(f"total labeled: {labeled}")
    print(f"manual_include=true: {include_count}")
    print(f"manual_include=false: {exclude_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
