"""Split cursor_eval_jobs.jsonl into batch files for manual labeling."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).parent
JOBS_PATH = ROOT / "cursor_eval_jobs.jsonl"
NUM_BATCHES = 8


def main() -> None:
    jobs = [json.loads(line) for line in JOBS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    chunk = math.ceil(len(jobs) / NUM_BATCHES)
    for i in range(NUM_BATCHES):
        batch = jobs[i * chunk : (i + 1) * chunk]
        if not batch:
            continue
        out = ROOT / f"_label_batch_{i + 1}.json"
        out.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Batch {i + 1}: {len(batch)} jobs -> {out.name}")
    print(f"Total: {len(jobs)} jobs in {NUM_BATCHES} batches")


if __name__ == "__main__":
    main()
