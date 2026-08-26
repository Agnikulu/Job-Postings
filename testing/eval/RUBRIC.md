# Early-career technical role rubric

Canonical rubric for labeling `testing/eval/eval_gold.jsonl`. Any human or
LLM labeling pass must apply this rubric directly against the posting's
title + full description — never by calling into `filters.py` or
`description_signals.py`. Those modules are the classifier under test;
using their regexes to produce "ground truth" makes the eval circular (see
`testing/README.md` for the incident this rubric exists to prevent).

## INCLUDE (`expected_include: true`) only when ALL three hold

**1. Early-career.** One of:
- Explicit: intern, co-op, new grad / new-grad, university graduate, campus
  hire, "early career", "entry level", apprentice, trainee, Engineer I /
  Engineer 1 / L3 or equivalent lowest IC rung, fellowship explicitly for
  new grads.
- Implicit: requirements state 0-2 years experience, "no prior experience
  required", "new grads welcome", graduating class of 2025-2028.

Exclude even if the title looks junior when: Engineer II/III/IV or higher,
Staff/Principal/Senior/Lead/Director/Manager, 3+ years required,
postdoc/postdoctoral, "expert" fellowships requiring a PhD or 3+ years
(e.g. Human Frontier Collective-style programs), founding engineer, group
leader / PI, or a title carries a cohort year (e.g. "2026") but the
requirements clearly state a senior experience bar anyway — cohort
branding does not override an explicit YOE requirement.

**2. Technical.** Software / ML / data / AI / quant-dev / firmware /
embedded / hardware / security engineering, or research
scientist/engineer work in CS/ML (not wet-lab, bench, or clinical
research). Technical internships count even without "engineer" in the
title if the description confirms a coding/technical scope.

Exclude: sales, BDR/SDR, recruiting/talent acquisition, PM/TPM (unless
explicitly an engineering-track intern), finance/legal/HR, customer
success, solutions/field/forward-deployed/pre-sales engineering (customer-
facing, not build), non-dev trading roles, marketing, ops/business
analyst, technical writing, IT/helpdesk/network technician.

**3. US-relevant.** US-based or explicitly remote-friendly for US new
grads. If location is empty or ambiguous, ignore this criterion (don't
let it drive the label either way) — the location gate is handled
separately in production, not part of what this rubric certifies.

## When uncertain

Read the full description, especially the Minimum/Basic Qualifications
section, not just the title — titles alone are frequently misleading
(e.g. "Member of Technical Staff" is senior at most companies unless
paired with an explicit new-grad/intern marker). When genuinely
ambiguous after reading the description, **exclude** (precision over
recall — a missed alert is cheaper than a noisy one).

## Label schema

Each row in `eval_gold.jsonl`:

```json
{
  "url": "...",
  "company": "...",
  "title": "...",
  "location": "...",
  "description": "... (full or a representative excerpt)",
  "expected_include": true,
  "reason": "short human-readable justification, specific to this posting",
  "kind": "tp_regression | fp_regression | fn_regression | tn_baseline",
  "difficulty": "easy | hard",
  "labeled_by": "claude-sonnet-5-manual-review"
}
```

`difficulty: hard` marks cases picked specifically because a prior classifier
version got them wrong, or because they sit near a real rubric boundary
(MTS, cohort-branded ladder titles, post-training research, associate
titles, forward-deployed engineer, open-level "Software Engineer, X",
physical design engineer, network engineer, SpaceX-style non-standard
titles). `difficulty: easy` marks unambiguous baseline cases included for
general coverage, not because they were ever a source of disagreement.
