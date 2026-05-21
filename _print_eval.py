import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
rows = json.load(open("_regex_eval_sample.json", encoding="utf-8"))
for i, r in enumerate(rows):
    print("=" * 72)
    print(f"[{i}] {r['company']} ({r['ats']}) bucket={r['bucket']}")
    print(f"TITLE: {r['title']}")
    print(
        f"REGEX: include={r['regex_include']} | {r['conf_level']} | {r['conf_reason']}"
    )
    print(
        f"SIG: senior={r['has_senior_exp']} ec={r['has_ec']} "
        f"strong={r['has_strong_ec']} req_len={r['req_len']}"
    )
    body = r.get("requirements_head") or r.get("description_head") or ""
    print(body[:950])
    print()
