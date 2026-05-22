import json
from classifier import classify_job_fields

jobs = [json.loads(l) for l in open("cursor_eval_jobs.jsonl", encoding="utf-8")]
labels = {
    json.loads(l)["url"]: json.loads(l)
    for l in open("cursor_eval_labels.jsonl", encoding="utf-8")
    if l.strip()
}

tp = fp = tn = fn = skipped = 0
for j in jobs:
    lab = labels.get(j["url"])
    if not lab or "manual_include" not in lab:
        skipped += 1
        continue
    m = lab["manual_include"]
    r = classify_job_fields(
        company=j["company"],
        title=j["title"],
        location=j.get("location"),
        url=j["url"],
        description=j.get("description"),
        us_only=False,
    ).include
    if m and r:
        tp += 1
    elif not m and not r:
        tn += 1
    elif not m and r:
        fp += 1
    else:
        fn += 1

manual = tp + fn
scored = tp + fp + tn + fn
fin_us = sum(
    1
    for j in jobs
    if classify_job_fields(
        company=j["company"],
        title=j["title"],
        location=j.get("location"),
        url=j["url"],
        description=j.get("description"),
        us_only=True,
    ).include
)

print(
    "METRICS",
    tp,
    fp,
    tn,
    fn,
    f"acc={((tp + tn) / scored):.3f}" if scored else "acc=n/a",
    f"prec={tp / (tp + fp):.3f}" if (tp + fp) else "prec=n/a",
    f"rec={tp / manual:.3f}" if manual else "rec=n/a",
    f"scored={scored}",
    f"skipped={skipped}",
    f"us_alerts={fin_us}",
)

print("\nFN:")
for j in jobs:
    lab = labels.get(j["url"])
    if not lab or not lab["manual_include"]:
        continue
    r = classify_job_fields(
        company=j["company"],
        title=j["title"],
        location=j.get("location"),
        url=j["url"],
        description=j.get("description"),
        us_only=False,
    )
    if not r.include:
        print(" ", j["company"], "|", j["title"][:70], "|", r.reason)

print("\nFP by reason:")
from collections import Counter

c = Counter()
for j in jobs:
    lab = labels.get(j["url"])
    if not lab or lab["manual_include"]:
        continue
    r = classify_job_fields(
        company=j["company"],
        title=j["title"],
        location=j.get("location"),
        url=j["url"],
        description=j.get("description"),
        us_only=False,
    )
    if r.include:
        c[r.reason or "?"] += 1
for reason, n in c.most_common():
    print(f"  {reason}: {n}")
