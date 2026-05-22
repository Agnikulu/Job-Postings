"""Full eval statistics report."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from classifier import classify_job_fields

ROOT = Path(__file__).parent
JOBS = ROOT / "cursor_eval_jobs.jsonl"
LABELS = ROOT / "cursor_eval_labels.jsonl"
REPORT = ROOT / "cursor_eval_full_stats.json"


def main() -> None:
    jobs = [json.loads(l) for l in JOBS.read_text(encoding="utf-8").splitlines() if l.strip()]
    labels = {json.loads(l)["url"]: json.loads(l) for l in LABELS.read_text(encoding="utf-8").splitlines() if l.strip()}

    tp = fp = tn = fn = 0
    manual_inc = regex_inc = 0
    desc_ok = us_alerts = 0
    by_company: dict[str, Counter] = defaultdict(Counter)
    fp_reasons: Counter = Counter()
    fn_reasons: Counter = Counter()
    fp_titles: list[dict] = []
    fn_titles: list[dict] = []

    for j in jobs:
        url = j["url"]
        lab = labels.get(url)
        if not lab:
            continue
        m = bool(lab["manual_include"])
        r = j["regex_include"]
        if m:
            manual_inc += 1
        if r:
            regex_inc += 1
        if j.get("desc_len", 0) > 0:
            desc_ok += 1

        cls = classify_job_fields(
            company=j["company"],
            title=j["title"],
            location=j.get("location"),
            url=url,
            description=j.get("description"),
            us_only=True,
        )
        if cls.include:
            us_alerts += 1

        co = j["company"]
        by_company[co]["jobs"] += 1
        if m:
            by_company[co]["manual_ec"] += 1
        if r:
            by_company[co]["regex_ec"] += 1

        if m and r:
            tp += 1
            by_company[co]["tp"] += 1
        elif not m and not r:
            tn += 1
        elif not m and r:
            fp += 1
            by_company[co]["fp"] += 1
            fp_reasons[j["regex_reason"]] += 1
            fp_titles.append({"company": co, "title": j["title"], "reason": j["regex_reason"], "manual": lab["manual_reason"]})
        else:
            fn += 1
            by_company[co]["fn"] += 1
            fn_reasons[lab["manual_reason"]] += 1
            fn_titles.append({"company": co, "title": j["title"], "manual": lab["manual_reason"]})

    total = len(jobs)
    acc = (tp + tn) / total
    prec = tp / (tp + fp) if tp + fp else 0
    rec = tp / (tp + fn) if tp + fn else 0

    companies = len(by_company)
    fetch_fail = 79 - companies  # approx

    stats = {
        "fetch": {
            "companies_attempted": 79,
            "companies_with_jobs": companies,
            "companies_failed": ["Nvidia (403)", "Isomorphic Labs (0)", "Atlassian (0)"],
            "total_jobs": total,
            "per_company_target": 100,
            "avg_jobs_per_company": round(total / companies, 1),
        },
        "coverage": {
            "description_present": desc_ok,
            "description_pct": round(100 * desc_ok / total, 2),
            "missing_description": total - desc_ok,
        },
        "ground_truth": {
            "manual_ec_total": manual_inc,
            "manual_ec_rate_pct": round(100 * manual_inc / total, 2),
            "regex_ec_total": regex_inc,
            "regex_ec_rate_pct": round(100 * regex_inc / total, 2),
            "us_alerts": us_alerts,
            "us_alert_rate_pct": round(100 * us_alerts / total, 2),
        },
        "regex_vs_manual": {
            "labeled": total,
            "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "accuracy": round(acc, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(2 * prec * rec / (prec + rec) if prec + rec else 0, 4),
        },
        "fp_by_regex_reason": dict(fp_reasons.most_common(15)),
        "fn_by_manual_reason": dict(fn_reasons.most_common(15)),
        "fp_samples": fp_titles[:30],
        "fn_samples": fn_titles,
        "by_company": {
            c: dict(v) for c, v in sorted(by_company.items(), key=lambda x: -x[1].get("manual_ec", 0))
        },
    }
    REPORT.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("=== RIGOROUS EVAL STATISTICS ===")
    print(f"Jobs fetched: {total} from {companies} companies (target 100/co)")
    print(f"Description coverage: {desc_ok}/{total} ({100*desc_ok/total:.1f}%)")
    print(f"Manual EC (ground truth): {manual_inc} ({100*manual_inc/total:.2f}%)")
    print(f"Regex EC: {regex_inc} ({100*regex_inc/total:.2f}%)")
    print(f"US alerts (production funnel): {us_alerts} ({100*us_alerts/total:.2f}%)")
    print(f"\nRegex vs Manual (n={total}):")
    print(f"  Accuracy:  {acc:.1%}")
    print(f"  Precision: {prec:.1%}  (TP={tp}, FP={fp})")
    print(f"  Recall:    {rec:.1%}  (TP={tp}, FN={fn})")
    print(f"\nTop FP regex reasons: {fp_reasons.most_common(5)}")
    print(f"FN count by reason: {fn_reasons.most_common(5)}")
    print(f"\nFull report: {REPORT.name}")


if __name__ == "__main__":
    main()
