"""Sample bare Software Engineer roles and inspect description signals."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from adapters import ADAPTER_REGISTRY
from scraper import load_registry
from filters import classify_title_confidence
from description_signals import extract_description_signals

BARE_EXCLUDE = (
    "intern",
    "new grad",
    "newgrad",
    "entry",
    "junior",
    " i ",
    " ii",
    "early career",
    "campus",
    "associate",
    "staff",
    "senior",
    "principal",
    "lead",
    "manager",
    "director",
)


def is_bare_swe(title: str) -> bool:
    tl = title.lower()
    if "software engineer" not in tl:
        return False
    return not any(k in tl for k in BARE_EXCLUDE)


def main() -> None:
    by = {c["name"]: c for c in load_registry()}
    targets = [
        "Cursor",
        "Databricks",
        "Stripe",
        "Anthropic",
        "Notion",
        "DoorDash",
        "Figma",
        "Google",
        "Microsoft",
    ]
    samples = []
    for name in targets:
        c = by.get(name)
        if not c or c["ats"] == "tier3_todo":
            continue
        try:
            jobs = ADAPTER_REGISTRY[c["ats"]](c)
        except Exception as exc:
            print(f"SKIP {name}: {exc}")
            continue
        for j in jobs:
            if not is_bare_swe(j.title or ""):
                continue
            conf = classify_title_confidence(j.title, j.description)
            if conf.level != "borderline" or not conf.is_technical:
                continue
            sig = extract_description_signals(j.description)
            samples.append((name, j, conf, sig))
            if len([x for x in samples if x[0] == name]) >= 3:
                break

    print(f"BARE SOFTWARE ENGINEER BORDERLINE SAMPLES: {len(samples)}\n")
    for name, j, conf, sig in samples:
        req = sig.requirements_text or ""
        desc = j.description or ""
        print("=" * 70)
        print(f"{name} | {j.title}")
        print(f"  has_desc={bool(desc)} desc_len={len(desc)} req_len={len(req)}")
        print(
            f"  strong_ec={sig.has_strong_ec} bach={sig.has_bachelors_req} "
            f"senior={sig.has_senior_exp} tech_field={sig.has_tech_field}"
        )
        print(f"  conf={conf.level} reason={conf.reason}")
        if req:
            print(f"  REQ: {req[:400]}...")
        elif desc:
            print(f"  DESC HEAD: {desc[:250]}...")
        print()


if __name__ == "__main__":
    main()
