# Testing & evaluation artifacts

Production code lives in the repo root. This folder holds **manual eval data and one-off scripts** only.

## Layout

| Path | Contents |
|------|----------|
| `eval/` | Current eval run outputs (`cursor_eval_*.jsonl`, reports) |
| `eval/batches/` | Per-batch manual labels (`_labels_batch_*.jsonl`, `_label_batch_*.json`) |
| `scripts/` | Eval helpers (`_cursor_manual_eval.py`, `_merge_labels.py`, etc.) |

## Commands (from repo root)

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
