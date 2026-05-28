"""Live smoke test for May 2026 big-tech batch."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from adapters import ADAPTER_REGISTRY
from scraper import load_registry

NEW = {
    "Broadcom",
    "Brex",
    "Affirm",
    "Duolingo",
    "GitHub",
    "ServiceNow",
    "Instacart",
    "Arm Holdings",
    "Qualcomm",
    "Marvell",
    "Intuit",
    "Okta",
    "Zscaler",
    "Arista Networks",
    "Rubrik",
    "dbt Labs",
    "Aurora Innovation",
    "Zoox",
    "Chime",
    "Fivetran",
    "Etsy",
}


def main() -> int:
    companies = [c for c in load_registry() if c["name"] in NEW]
    failed = 0
    for c in companies:
        fn = ADAPTER_REGISTRY.get(c["ats"])
        if not fn:
            print(f"FAIL {c['name']}: no adapter for {c['ats']}")
            failed += 1
            continue
        try:
            jobs = fn(c)
            print(f"OK  {c['name']:22} {c['ats']:16} {len(jobs):4} jobs")
            if not jobs:
                print(f"     WARN {c['name']}: zero jobs returned")
        except Exception as e:
            print(f"ERR {c['name']:22} {c['ats']:16} {e}")
            failed += 1
    if len(companies) != len(NEW):
        missing = NEW - {c["name"] for c in companies}
        print(f"MISSING from registry: {sorted(missing)}")
        failed += len(missing)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
