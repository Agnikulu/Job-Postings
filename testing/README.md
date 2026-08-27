# Testing & evaluation artifacts

Production code lives in the repo root. This folder holds eval data and eval helper scripts.

## Layout

| Path | Contents |
|------|----------|
| `eval/RUBRIC.md` | Canonical labeling rubric — the single source of truth for what counts as early-career + technical |
| `eval/eval_gold.jsonl` | **Authoritative, committed accuracy set** (1455 rows) — independently hand-labeled against `RUBRIC.md`. `tests/test_eval_regression.py` and `tests/test_eval_metrics_floor.py` run against this in CI on every PR/push touching `*.py`. |
| `eval/eval_baseline.json` | Pinned precision/recall floor for `eval_gold.jsonl`, with provenance + measurement-caveat notes |
| `eval/` (other files) | Non-committed, regenerable eval run outputs (`cursor_eval_*.jsonl`, reports) from the optional larger "extended audit" pipeline below |
| `eval/batches/` | Per-batch manual labels for that extended-audit pipeline |
| `scripts/` | Eval helpers (`_cursor_manual_eval.py`, `_merge_labels.py`, etc.) |

## Ground-truth governance

`eval_gold.jsonl` must only be updated by labeling that is independent of
`filters.py`/`description_signals.py` — by hand against `RUBRIC.md`, or a
genuine external LLM API pass (`_llm_eval_label.py` with `OPENAI_API_KEY`
set). **Never** from `_rigorous_manual_label.py`'s deterministic
`manual_judge()` fallback (used automatically when no API key is set) — it
imports regex primitives directly from `filters.py`, so scoring the
classifier against it is circular and silently inflates apparent accuracy.
That fallback is a fine cheap smoke-test for quick local dry runs; it is
not ground truth. See `README_TECH.md`'s "Manual eval vs regex" section
for the full incident this rule exists to prevent.

## Commands (from repo root)

```bash
# Run the CI-equivalent accuracy checks locally
pytest tests/test_eval_regression.py tests/test_eval_metrics_floor.py -q
```

### Optional: larger, non-committed "extended audit"

```bash
# Fetch sample jobs for manual eval
python testing/scripts/_cursor_manual_eval.py fetch --per-company 100

# Re-apply regex to existing jobs file (after filter changes)
python testing/scripts/_cursor_manual_eval.py rescore

# Score regex vs merged manual labels
python testing/scripts/_cursor_manual_eval.py score

# Merge batch label files into eval/cursor_eval_labels.jsonl
python testing/scripts/_merge_labels.py
```

## Production scrape

```bash
python scraper.py
```

Environment:

- `ATS_SNIPER_FETCH_WORKERS` — parallel company fetches (default `4` in GitHub Actions)
- `ATS_SNIPER_ALL_LOCATIONS=1` — disable US-only filter
