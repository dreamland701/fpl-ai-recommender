# FPL AI Recommender Project Summary

Updated: 2026-06-13

Project root: `/home/wescheng/projects/fpl/fpl`

## Objective

Build a personal Fantasy Premier League assistant that can recommend transfers, captain/vice captain, starters, bench order, and chip usage using pre-deadline information only.

The long-term goal is not just to ask a general LLM for FPL advice. The goal is to build an FPL-specific prediction and decision system that:

- Uses up-to-date official/statistical data.
- Avoids hallucinated player/team/news facts.
- Avoids post-deadline leakage.
- Learns from historical player outcomes.
- Reads curated football/FPL text evidence when useful.
- Produces forecasts that can be fed into a legal FPL optimizer.

The current working architecture is:

1. Build timestamp-safe structured player-week data.
2. Train classic ML baselines for availability/minutes and expected points.
3. Add curated text evidence packets from official PL/FPL Scout, Sky podcast summaries, and trusted source backfills.
4. Fine-tune an LLM to adjust or rank forecasts, not to replace the optimizer blindly.
5. Let the optimizer convert player forecasts into team actions.

## Data Boundary

The project intentionally uses:

- Completed historical seasons through `2024-25`.
- `2025-26 GW1-GW30`.
- No `2025-26 GW31` in training/backtests because GW31 had fixture rearrangement ambiguity.

The leakage rule is:

- Features and evidence for a gameweek must be available before that gameweek deadline.
- Labels are realized future FPL points after the deadline.
- Text evidence must satisfy `published_at <= deadline_ts`.
- Articles that look like post-gameweek recaps or defensive-contribution result summaries are filtered out of SFT evidence.

Important nuance: current anchored reranker concerns are mostly label-noise/overfitting concerns, not post-deadline leakage. The data boundary is already explicit; the model objective still needs to avoid learning unstable overrides from noisy realized outcomes.

## What Has Been Built

### Core Python Package

The package lives under `src/fpl_ai`.

Important modules:

- `src/fpl_ai/ingest.py`: historical FPL data ingestion and normalization.
- `src/fpl_ai/dataset.py`: player-week feature table construction.
- `src/fpl_ai/models.py`: classic supervised baseline models.
- `src/fpl_ai/decision.py`: legal FPL decision engine for transfers, captaincy, starters, bench order, and chips.
- `src/fpl_ai/backtest.py`: rolling historical backtests.
- `src/fpl_ai/evaluation.py`: model and decision evaluation helpers.
- `src/fpl_ai/evidence.py`: curated evidence abstractions and cited reporting.
- `src/fpl_ai/evidence_collect.py`: evidence collection interfaces.
- `src/fpl_ai/weekly_evidence.py`: weekly evidence packet construction and timestamp filtering.
- `src/fpl_ai/llm_data.py`: LLM SFT data export.
- `src/fpl_ai/llm_eval.py`: LLM output evaluation.
- `src/fpl_ai/hybrid.py`: hybrid classic-ML/LLM decision workflows.
- `src/fpl_ai/api.py`: public interface layer.
- `src/fpl_ai/cli.py`: command-line entry points.

### Tests

Tests are under `tests`.

Coverage includes:

- Dataset construction and integrity.
- Ingestion.
- Baseline models.
- Decision engine.
- Backtesting.
- Evidence collection and weekly evidence.
- LLM data and eval paths.
- Hybrid decision logic.

Main test command:

```bash
cd /home/wescheng/projects/fpl/fpl
PYTHONPATH=src python3 -m unittest discover -s tests
```

### Structured Training Data

Primary local structured data:

- `data/fpl_training_rows.csv`
- `data/fpl_history/`
- `models/fpl_models/`

The training table is `player x pre-deadline gameweek`.

Feature families include:

- Price and ownership.
- Fixture count, home/away, difficulty, blank/double indicators.
- Rolling points/minutes/starts/appearance rates.
- Team and opponent goal proxies.
- Bonus/BPS/ICT rolling features.
- Expected goals/assists/goal involvement where source data exists.
- Defensive-contribution feature fields where available.
- Official status/news fields where safe.

For historical backfill, official API current-only status/news fields are neutralized where trustworthy historical snapshots are unavailable.

### Evidence Data

Evidence documentation:

- `docs/evidence_generation.md`

Important evidence files:

- `reports/evidence_2025_26_gw1_30_google_news.jsonl`
- `reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl`
- `reports/evidence_packets_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl`
- `reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus_report.json`

Current evidence state:

- Official Premier League/FPL Scout full-text rows are available when canonical PL URLs were resolved.
- Sky Sports podcast data is available as RSS episode summaries after boilerplate cleanup.
- Sky rows are not full transcripts. Exact podcast dialogue would require separate audio transcription from MP3 enclosures.
- Google News rows are useful for historical backfill but often contain snippets only unless publisher URLs can be resolved.

Current preferred evidence order:

1. Direct official FPL/PL/FPL Scout source data.
2. Direct official club updates.
3. Direct RSS/source URLs from trusted free sources.
4. Sky Sports podcast summaries or future transcripts.
5. Google News RSS as a backfill fallback.

## LLM / SFT Work Done So Far

### Initial Squad/Transfer SFT

Earlier experiments tried to train Gemma to directly make squad/transfer decisions.

What worked:

- Fine-tuning improved machine-parseable formatting compared with base Gemma.
- Prompt examples helped strict JSON behavior.

What did not work:

- Direct action choice was too sparse and noisy.
- The action space is constrained by FPL rules, squad state, budget, hits, and chips.
- Asking the LLM to directly choose actions made it easy for it to produce invalid or suboptimal decisions.

Conclusion:

- Direct squad policy SFT should not be the main prediction objective yet.
- The LLM should feed an optimizer, not replace it.

### Per-Player Forecast SFT

Several per-player forecast datasets were built, including:

- `reports/llm_player_forecast_pilot_top96_2025_26_gw11_30`
- `reports/llm_player_forecast_2025_26_gw1_10_top128_eval_gw11`
- `reports/llm_player_forecast_residual_2025_26_gw1_10_top128_eval_gw11`
- `reports/llm_player_forecast_residual_2025_26_gw1_25_top128_eval_gw26`

Example eval files:

- `reports/player_forecast_top96_eval_summary_promptfix.json`
- `reports/player_forecast_gw1_10_top128_gw11_eval_summary.json`
- `reports/player_forecast_residual_gw1_10_top128_gw11_pilot_eval_summary.json`
- `reports/player_forecast_residual_gw1_25_top128_gw26_eval_summary.json`

Key findings:

- Base Gemma often produced parseable but not strict JSON.
- SFT improved strict JSON dramatically in some runs.
- Per-player forecast SFT did not reliably beat the classic ML baseline.
- Residual-style outputs are more promising than full forecast replacement.
- Some SFT runs over-adjusted and worsened RMSE, especially on longer horizons.

Representative per-player forecast results:

GW1-10 train, GW11 eval, direct forecast:

| Model | 1GW RMSE | 3GW RMSE | 5GW RMSE | Strict JSON |
|---|---:|---:|---:|---:|
| Base Gemma | 3.3091 | 6.8521 | 9.8013 | 1 / 128 |
| SFT Gemma | 3.3121 | 6.8590 | 9.8098 | 0 / 128 |

GW1-10 train, GW11 eval, residual forecast:

| Model | 1GW RMSE | 3GW RMSE | 5GW RMSE | Parseable |
|---|---:|---:|---:|---:|
| Classic ML | 3.3505 | 6.9017 | 9.8536 | n/a |
| Base Gemma residual | 3.3832 | 6.8187 | 9.2259 | 117 / 128 |
| SFT Gemma residual | 3.4162 | 6.5338 | 8.5461 | 107 / 128 |

GW1-25 train, GW26 eval, residual forecast:

| Model | 1GW RMSE | 3GW RMSE | 5GW RMSE | Strict JSON |
|---|---:|---:|---:|---:|
| Classic ML | 3.3068 | 6.2517 | 8.5784 | n/a |
| Base Gemma residual | 3.3612 | 6.2887 | 8.6674 | 0 / 128 |
| SFT Gemma residual | 3.7081 | 7.6928 | 11.5955 | 128 / 128 |

Conclusion:

- Format learning is achievable.
- Prediction quality needs a better objective, better scale, smaller/faster model iteration, and stronger anchoring to classic ML.
- The next mainline should return to per-player residual/adjustment forecasting.

### Free Listwise Reranking

A listwise value-ranking dataset was built:

- `reports/llm_ranking_value_2025_26_gw1_25_eval_gw26`
- `scripts/build_ranking_value_sft_split.py`
- `scripts/run_gemma_ranking_value_gw1_25_eval_gw26.sh`
- `score_ranking_value_eval.py`

Task:

- Given a slate of 12 candidates, rank the top 5 by realized utility.
- Utility formula: `0.20 * points_1gw + 0.30 * points_3gw + 0.50 * points_5gw`.

Unanchored checkpoint results on GW26 eval:

| Model | Value / example | NDCG@5 | Top1 accuracy | Strict JSON |
|---|---:|---:|---:|---:|
| Classic ML | 79.9016 | 0.7937 | 0.3047 | 128 / 128 |
| SFT checkpoint 160 | 70.9320 | 0.7039 | 0.1875 | 128 / 128 |
| SFT checkpoint 320 | 73.3648 | 0.7289 | 0.1797 | 128 / 128 |
| SFT checkpoint 480 | 72.6117 | 0.7150 | 0.1484 | 128 / 128 |
| SFT checkpoint 600 | 73.0336 | 0.7195 | 0.1719 | 128 / 128 |

What worked:

- Strict JSON was solved.
- The model learned the task format.

What did not work:

- It underperformed classic ML.
- It overrode the baseline too freely.
- Best checkpoint was 320, but still materially below classic ML.

Conclusion:

- Free reranking is too unconstrained for noisy FPL outcomes.
- The LLM needs an anchored correction role.

### Anchored Reranking

Anchored dataset:

- `reports/llm_anchored_ranking_value_2025_26_gw1_25_eval_gw26`
- `scripts/build_anchored_ranking_value_sft_split.py`

Anchored training/eval scripts:

- `scripts/run_gemma_anchored_ranking_value_gw1_25_eval_gw26.sh`
- `scripts/run_gemma_anchored_ranking_value_gw1_25_eval_gw26_eval.sh`
- `scripts/pause_eval_stop_anchored_ranking_value_checkpoint160.sh`
- `scripts/watchdog_anchored_ranking_value_training.sh`

Task:

- Start with the classic ML top 5.
- Allow at most 2 swaps.
- Train on outcome-supervised swaps that improve realized utility.
- Still use the same utility formula: `0.20 * points_1gw + 0.30 * points_3gw + 0.50 * points_5gw`.

Dataset summary:

- Train weeks: `2025-26 GW1-GW25`.
- Eval week: `2025-26 GW26`.
- Train examples: `16,000`.
- Eval examples: `128`.
- Slate size: `12`.
- Rank size: `5`.
- Candidate pool: top `128` by classic ML baseline.
- Max swaps: `2`.

Eval split theoretical values:

| Policy | Value / example |
|---|---:|
| Classic ML baseline | 76.6922 |
| Anchored target, max 2 swaps | 93.4813 |
| Full oracle top 5 | 94.1773 |

Interpretation:

- On the eval slates, allowing two perfect swaps captures most oracle upside.
- This is not expected to be achievable in real inference, but it defines a useful bounded correction target.

Current run state:

- Running on Gemma `google/gemma-4-31B-it`.
- LoRA training only.
- Output dir: `artifacts/gemma4_31b_lora_anchored_ranking_value_gw1_25_eval_gw26`
- Latest observed checkpoint when this doc was written: `checkpoint-100`.
- Last observed checkpoint metrics at step 100: loss `0.1747`, mean token accuracy `0.9263`.
- Stop/eval monitor is waiting for `checkpoint-160`.
- Training will be intentionally stopped at `checkpoint-160`, evaluated, and not auto-resumed.

Important operational files:

- Training log: `logs/train_anchored_ranking_value_gw1_25_eval_gw26.log`
- Stop/eval log: `logs/interim_eval_stop_anchored_ranking_value_checkpoint160.log`
- Watchdog log: `logs/watchdog_anchored_ranking_value_training.log`

Expected checkpoint-160 eval outputs:

- `reports/gemma4_anchored_ranking_value_gw1_25_eval_gw26_sft_checkpoint160_predictions.jsonl`
- `reports/gemma4_anchored_ranking_value_gw1_25_eval_gw26_base_checkpoint160_predictions.jsonl`
- `reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint160_summary.json`
- `reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint160_rows.json`
- `reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint160_eval_complete.stop`

## What Worked

### The Structured Data Layer Works

The project now has a reusable player-week feature pipeline, historical data ingestion, and rolling backtest infrastructure.

This is the most important foundation. It lets future LLM experiments be evaluated against the same baseline and same labels.

### The Classic ML Baseline Is Strong Enough To Anchor On

The classic ML model is not perfect, but it is a defensible baseline. It provides:

- Expected points over 1/3/5 gameweeks.
- Minutes and appearance probability.
- Stable ranking behavior.
- Legal optimizer inputs.

Most LLM approaches should use the classic model as an anchor rather than predicting from scratch.

### Strict JSON Can Be Learned

Several SFT runs showed that format quality can be fixed.

This means future failures are likely not just prompt-format failures. The real issue is the learning objective and signal quality.

### Residual Forecasting Is More Promising Than Direct Forecast Replacement

Residual/adjustment tasks are better aligned with the desired role:

- Classic ML handles structured priors.
- LLM reads text evidence and context.
- LLM outputs bounded corrections.
- Optimizer consumes corrected forecasts.

### Evidence Infrastructure Is Useful

The evidence layer now preserves:

- Published timestamps.
- Gameweek deadlines.
- Source names and URLs.
- Full text when available.
- Extraction status.
- Packet selection boundaries.

This is essential for avoiding training/serving skew.

## What Did Not Work

### Large 31B Runs Are Too Slow For Iteration

The DGX Spark can run the 31B LoRA job, but each optimizer step takes roughly 16 minutes in the current setup.

This is too slow for objective design. The next phase needs smaller models so we can run many controlled experiments quickly.

### Direct Squad Policy SFT Was Premature

Directly training the LLM to choose team actions combines too many problems:

- Forecasting player points.
- Understanding availability.
- Handling legal FPL constraints.
- Managing budget and transfer hits.
- Captaincy/chips.
- JSON validity.

This should be decomposed. The LLM should first improve player forecasts, then the optimizer should choose legal actions.

### Free Reranking Overfits Noisy Outcomes

The unanchored ranking model learned valid output format but underperformed classic ML.

The likely failure mode:

- Realized FPL points are noisy.
- The model sees small samples.
- Free reranking lets it override too many baseline decisions.
- It learns unstable patterns that do not generalize.

Anchoring limits the damage, but the better mainline is still per-player residual forecasting.

### Text Data Is Not Automatically Helpful

Adding text evidence is only useful if:

- It is timestamp-safe.
- It contains real signal, not boilerplate.
- It is linked to the right player/team/week.
- The model is trained to make bounded forecast adjustments.

Full-text PL/FPL Scout articles are valuable. Sky podcast summaries are less rich than transcripts. Google News snippets are useful for recall but not enough as primary training text.

## Current Code Structure

Top-level scripts:

- `train_gemma_sft.py`: generic Gemma LoRA SFT trainer using env vars.
- `eval_gemma_responses.py`: generic Gemma/base/SFT response generation.
- `score_player_forecast_eval.py`: direct player forecast scoring.
- `score_player_forecast_residual_eval.py`: residual forecast scoring.
- `score_ranking_value_eval.py`: ranking/reranking scoring.

Dataset builders:

- `scripts/build_top_player_llm_split.py`
- `scripts/build_residual_player_forecast_split.py`
- `scripts/build_ranking_value_sft_split.py`
- `scripts/build_anchored_ranking_value_sft_split.py`
- `scripts/build_fpl_sky_fulltext_corpus.py`

Training/eval runners:

- `scripts/run_gemma_gw1_10_top128_768.sh`
- `scripts/run_gemma_residual_gw1_10_top128_pilot.sh`
- `scripts/run_gemma_residual_gw1_25_top128.sh`
- `scripts/run_gemma_ranking_value_gw1_25_eval_gw26.sh`
- `scripts/run_gemma_anchored_ranking_value_gw1_25_eval_gw26.sh`

Checkpoint automation:

- `scripts/pause_eval_resume_ranking_value_checkpoint160.sh`
- `scripts/pause_eval_resume_anchored_ranking_value_checkpoints.sh`
- `scripts/pause_eval_stop_anchored_ranking_value_checkpoint160.sh`
- `scripts/watchdog_ranking_value_training.sh`
- `scripts/watchdog_anchored_ranking_value_training.sh`

Docs:

- `README.md`
- `docs/evidence_generation.md`
- `docs/project_summary_2026-06-13.md`

Important report directories:

- `reports/honest_backtest_2025_26_gw1_30`
- `reports/rolling_squad_backtest_2025_26_gw11_30`
- `reports/llm_player_forecast_2025_26_baseline_adjustment_fpl_sky_compact_v1_split_gw26_30`
- `reports/llm_player_forecast_2025_26_baseline_adjustment_fpl_sky_fulltext_v4_split_gw26_30`
- `reports/llm_player_forecast_residual_2025_26_gw1_25_top128_eval_gw26`
- `reports/llm_ranking_value_2025_26_gw1_25_eval_gw26`
- `reports/llm_anchored_ranking_value_2025_26_gw1_25_eval_gw26`

Important artifact directories:

- `artifacts/gemma4_31b_lora_player_forecast_residual_gw1_25_top128`
- `artifacts/gemma4_31b_lora_ranking_value_gw1_25_eval_gw26`
- `artifacts/gemma4_31b_lora_anchored_ranking_value_gw1_25_eval_gw26`

## Current Decision

Let the current 31B anchored run continue only until `checkpoint-160`.

At `checkpoint-160`:

1. Stop training.
2. Run anchored GW26 eval.
3. Save summary and row-level examples.
4. Do not resume the 31B run automatically.

Rationale:

- The run is expensive and slow.
- We need one anchored result as a datapoint.
- The next mainline should move to smaller models and per-player forecasts.

## Recommended Next Mainline

### Direction

Pivot from 31B listwise reranking to smaller-model per-player residual forecasting.

Recommended model size:

- `4B-9B`, not `31B`, for the next iteration loop.

Reason:

- This task is mostly structured extraction, calibration, and bounded JSON prediction.
- Smaller models can be fine-tuned and evaluated much faster.
- Faster iteration matters more than raw model size right now.
- Generative retrieval and domain SFT work often shows smaller models can match larger models when the task is constrained and the data format is strong.

### Core Example Unit

Use one example per:

```text
player x gameweek x pre-deadline snapshot
```

Input should include:

- Player identity and team.
- Position.
- Gameweek and deadline timestamp.
- Classic ML forecast.
- Structured rolling features.
- Fixture context.
- Official availability/status fields.
- Timestamp-safe evidence packet for player/team/week.

Output should be strict JSON:

```json
{
  "player_id": 123,
  "expected_points_1gw": 5.4,
  "expected_points_3gw": 14.8,
  "expected_points_5gw": 23.1,
  "minutes_1gw": 82.0,
  "appearance_probability": 0.91,
  "points_delta_1gw": 0.4,
  "points_delta_3gw": 1.1,
  "points_delta_5gw": 1.7,
  "confidence": 0.62,
  "risk_flags": ["rotation"],
  "reason": "..."
}
```

The important design choice:

- Train the model to predict bounded residuals from classic ML, not unconstrained forecasts from scratch.

### Data Scale Plan

Expand beyond just 2025-26.

Recommended first expanded training window:

- Train on `2023-24`, `2024-25`, and early `2025-26`.
- Evaluate on the last 19 gameweeks of `2025-26`, likely `GW12-GW30`.

Rolling evaluation policy:

- To evaluate `2025-26 GW12`, train only on completed prior seasons plus `2025-26 GW1-GW11`.
- To evaluate `2025-26 GW13`, train only on completed prior seasons plus `2025-26 GW1-GW12`.
- Continue through `GW30`.

This gives:

- More examples.
- More realistic eval.
- A real view of whether the model improves as the season accumulates.

Approximate data scale:

- Around 20 teams x 25 players x 38 gameweeks per season.
- Roughly 19k player-week rows per season before filtering.
- Multiple seasons should produce enough data for a small model SFT/residual-calibration experiment.

### Chronological Training

Main requirement:

- Splits must be chronological.
- No eval gameweek can use future labels or future evidence.

Training batch order:

- It is acceptable to shuffle within the allowed training window for optimization stability.
- A chronological curriculum can also be tested, but chronological split integrity matters more than strict SGD ordering.

### Evidence Expansion

Keep evidence curated and timestamped.

Near-term useful additions:

- More official PL/FPL Scout historical article bodies.
- Official club injury/team news pages where timestamps are reliable.
- Sky Sports podcast transcripts if audio transcription is implemented.
- Reddit only if timestamped and clearly separated as noisy social signal.

Recommendation:

- Do not mix large unfiltered Reddit/news text into SFT yet.
- First build compact, evidence-linked player-week examples.
- Add source type, timestamp quality, and extraction status as explicit fields.

### Metrics For Next Mainline

Primary metrics:

- 1GW points RMSE/MAE.
- 3GW points RMSE/MAE.
- 5GW points RMSE/MAE.
- Minutes RMSE/MAE.
- Appearance probability calibration.
- Rank correlation against actual utility.
- Top-k lift over classic ML.

Downstream metrics:

- Optimizer-selected squad weekly score.
- Transfer value after hit accounting.
- Captain points.
- Bench/start correctness.
- Rolling season total versus classic ML-only optimizer.

The acceptance criterion should not be "LLM beats classic ML on every metric." A useful intermediate win is:

- Same or slightly better RMSE.
- Better top-k lift.
- Better availability/rotation adjustments.
- Better downstream optimizer points.

## Concrete Next Engineering Tasks

1. Finish the current 31B anchored checkpoint-160 eval.
2. Summarize checkpoint-160 results against classic ML and unanchored SFT.
3. Build expanded multi-season player-week residual dataset.
4. Add rolling chronological split generator for `2025-26 GW12-GW30`.
5. Define a strict residual JSON schema.
6. Add bounded residual clipping in both training labels and inference parsing.
7. Train a `4B-9B` model on the expanded residual task.
8. Evaluate per-player metrics and downstream optimizer metrics.
9. Compare against classic ML-only optimizer.
10. Only after that, revisit direct action/reranking policy SFT.

## Current Working Hypothesis

The best near-term system is not:

```text
LLM directly chooses FPL team
```

The best near-term system is:

```text
classic ML forecast
  + timestamp-safe text evidence
  + small LLM residual adjustment
  + legal optimizer
  + cited explanation layer
```

This preserves the strengths of each component:

- Classic ML handles numeric priors and stability.
- LLM handles text context and exceptional cases.
- Optimizer handles FPL legality and combinatorial search.
- Report generator explains decisions with citations.

## Open Risks

- FPL outcomes are intrinsically noisy.
- Text evidence may not contain enough signal for most players.
- Historical article availability is uneven.
- Sky podcast summaries are not transcripts.
- LLMs may learn formatting faster than forecasting.
- Small eval sets can mislead; rolling GW12-GW30 eval is needed.
- If the LLM outputs unbounded corrections, it can degrade a strong baseline.

Mitigation:

- Use rolling chronological eval.
- Use residuals and clipping.
- Keep classic ML as fallback.
- Track downstream optimizer points, not only raw forecast RMSE.
- Keep evidence source/timestamp quality explicit.
