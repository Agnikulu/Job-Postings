"""Smoke test Pure Storage, Crusoe, Cerebras, Baseten, Samsara."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from adapters import ADAPTER_REGISTRY
from scraper import load_registry

NAMES = {"Pure Storage", "Crusoe", "Cerebras", "Baseten", "Samsara"}


def main() -> int:
    failed = 0
    for c in load_registry():
        if c["name"] not in NAMES:
            continue
        try:
            jobs = ADAPTER_REGISTRY[c["ats"]](c)
            sample = jobs[0].title if jobs else "-"
            print(f"OK  {c['name']:15} {c['ats']:12} {len(jobs):4}  {sample[:50]}")
            if not jobs:
                print(f"    WARN zero jobs")
        except Exception as e:
            print(f"ERR {c['name']:15} {e}")
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
