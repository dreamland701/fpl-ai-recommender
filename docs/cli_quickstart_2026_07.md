# FPL AI Recommender

An opinionated first implementation of a personal Fantasy Premier League assistant.

This repository focuses on four layers:

1. Canonical weekly snapshot and training-row generation.
2. Lightweight supervised baseline models for availability/minutes and expected points.
3. A decision engine for transfers, captaincy, starters, bench order, and chip advisories.
4. A grounded reporting layer that keeps curated text/news sources separate from the prediction model.

## What is implemented

- Historical-data ingestion from `vaastav/Fantasy-Premier-League` plus official FPL backfill for `2025-26 GW1-GW30`.
- Historical-data normalization for a `vaastav/Fantasy-Premier-League` style folder.
- Week eligibility rules with an explicit exclusion for `2025-26 GW31`.
- Feature engineering at `player x pre-deadline week`.
- Baseline trainable ridge-regression models using `numpy`.
- Recommendation search over legal single and double transfers.
- A curated-source registry plus cited report generation and freshness warnings.
- Timestamp-safe evidence normalization for future LLM fine-tuning datasets.
- Week-by-week LLM SFT export from backtest traces.
- A small CLI and a unittest suite.

## What is not implemented yet

- Automated scraping of third-party news sites.
- Online model serving or database-backed persistence.
- Offline RL / policy learning.
- End-to-end LLM fine-tuning / inference runs.

## Quickstart

Run tests (pytest; `unittest discover` skips the module-level test functions):

```bash
PYTHONPATH=src /home/wescheng/venvs/fpl-gemma-lite/bin/python -m pytest -q tests
```

Build a training table from a local historical dataset:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli build-training-table \
  --history-root /path/to/Fantasy-Premier-League/data \
  --output /tmp/fpl_training_rows.csv
```

Fetch the raw history automatically and build the training table in one step:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli bootstrap-training-data \
  --history-root /tmp/fpl_history \
  --output /tmp/fpl_training_rows.csv \
  --current-season 2025-26 \
  --current-max-gw 30
```

Train the baseline models:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli train-models \
  --training-data /tmp/fpl_training_rows.csv \
  --model-dir /tmp/fpl_models
```

Generate a recommendation bundle from trained models and a squad JSON file:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli recommend \
  --training-data /tmp/fpl_training_rows.csv \
  --model-dir /tmp/fpl_models \
  --season 2025-26 \
  --week 30 \
  --squad /path/to/squad.json
```

Normalize a local evidence export into curated JSONL:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli normalize-evidence \
  --input /path/to/raw_evidence.json \
  --output /tmp/fpl_evidence.jsonl
```

Collect a normalized evidence corpus from supported curated feeds plus optional local imports:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli collect-evidence \
  --output /tmp/fpl_evidence_recent.jsonl \
  --lookback-days 7 \
  --max-items-per-source 50 \
  --input /path/to/local_exports_dir
```

Export week-by-week LLM fine-tuning examples from a backtest report:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli export-llm-sft \
  --training-data /tmp/fpl_training_rows.csv \
  --backtest-report /path/to/rolling_squad_backtest.json \
  --evidence /tmp/fpl_evidence.jsonl \
  --output /tmp/fpl_llm_sft.jsonl
```

Export a larger multi-season LLM decision corpus:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli export-llm-sft-corpus \
  --training-data /tmp/fpl_training_rows.csv \
  --output /tmp/fpl_llm_corpus.jsonl \
  --initial-train-week-max 10 \
  --start-week 11
```

Split that corpus into a clean train/eval window:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli split-llm-sft \
  --input /tmp/fpl_llm_corpus.jsonl \
  --output-dir /tmp/fpl_llm_split \
  --eval-season 2025-26 \
  --eval-week-min 11 \
  --eval-week-max 30
```

Evaluate week-by-week JSON predictions from an external or local LLM run:

```bash
PYTHONPATH=src python3 -m fpl_ai.cli evaluate-llm-predictions \
  --examples /tmp/fpl_llm_split/eval.jsonl \
  --predictions /tmp/fpl_predictions.jsonl \
  --output-dir /tmp/fpl_llm_eval
```

## Historical dataset expectations

The historical loader is designed for the common `vaastav/Fantasy-Premier-League` layout. The new ingestion command creates that layout automatically under `--history-root`. The loader supports:

- `merged_gw.csv` if present.
- `gws/merged_gw.csv` if present.
- Fallback to `gws/gw*.csv`.
- Optional enrichment via `players_raw.csv` and `fixtures.csv`.

It intentionally excludes `2025-26 GW31` from training and backtests to avoid the postponed/rearranged fixture ambiguity discussed in the project plan.

For the official `2025-26` backfill, historical `status` and `news` fields are intentionally neutralized because the official API exposes current availability metadata but not trustworthy week-by-week historical snapshots for those fields.
