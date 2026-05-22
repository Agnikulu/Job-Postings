import json

with open("_label_batch_2.json", encoding="utf-8") as f:
    jobs = json.load(f)

out = []
for i, j in enumerate(jobs):
    desc = j.get("description") or ""
    snippet = ""
    for kw in [
        "What you bring",
        "Requirements",
        "Qualifications",
        "What we",
        "Minimum",
        "You have",
        "You will need",
        "Who you are",
        "About you",
    ]:
        idx = desc.find(kw)
        if idx >= 0:
            snippet = desc[idx : idx + 500].replace("\n", " ")
            break
    if not snippet and desc:
        snippet = desc[-800:].replace("\n", " ")
    out.append(
        {
            "i": i,
            "company": j["company"],
            "title": j["title"],
            "location": j.get("location", ""),
            "url": j["url"],
            "regex_include": j.get("regex_include"),
            "regex_reason": j.get("regex_reason"),
            "snippet": snippet[:400],
        }
    )

with open("_review_batch_2.txt", "w", encoding="utf-8") as f:
    for o in out:
        f.write(f"[{o['i']}] {o['company']} | {o['title']} | {o['location']}\n")
        f.write(f"  regex={o['regex_include']} ({o['regex_reason']})\n")
        f.write(f"  {o['snippet']}\n\n")
print("written", len(out))
