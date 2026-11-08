# FPL Predictor — Complete Project History & Reference (as of 2026-07-12)

One-stop context document: mission, architecture, all data assets, every
experiment and verdict from the beginning, decisions log, hardware handbook,
and the forward plan. Written so a fresh session (or compacted context) can
reconstruct the entire project from this file plus the living docs:

- `docs/session_state_2026_07_12.md` — operational state (what's running now)
- `docs/experiment_log_e4b_residual_2026_07.md` — full experiment numbers
- `docs/decision_layer_plan_2026_07_09.md` — planning + GRPO design
- `project_plan_2026_07_05.md` — the original approved plan

## 1. Mission & ground rules

- **Wes is building an FPL predictor for the 2026-27 season** on a DGX Spark
  (GB10, 119GB unified memory, aarch64). Hard deadline: GW1, mid-August 2026.
- **The fine-tuned LLM must be load-bearing**: classic ML is one input
  signal; the LLM (Gemma-4-E4B + LoRA) is the forecaster. Goal #2 is
  *honestly validating* whether LLM fine-tuning works — negative results are
  deliverables, not failures.
- Every experiment is timestamp-safe (only pre-deadline information) and
  gated on realized decision value, not proxy metrics.

## 2. Architecture

**Classic ML baseline**: ridge regression suite (availability/minutes,
points 1/3/5GW heads) on ~68 SAFE_FEATURE_COLUMNS (1-8GW form, xG/xA/ICT,
team/opponent goal form, fixture difficulty/venue, blanks/doubles, market
trends, binary status/news flags). Rolling protocol: refit weekly on
strictly-prior data, alpha 1.0. Labels are UNCONDITIONAL (zero-minute weeks
count) — availability is partially priced into points forecasts, so naive
P(appear) reweighting double-counts.

**LLM forecast layer (residual/anchored SFT)**: the model outputs bounded
JSON deltas vs the classic baseline — {Δpts_1gw ±2, Δpts_3gw ±4, Δpts_5gw ±6,
Δmin ±20, ΔP(appear) ±0.25}, labels shrunk (0.35) then clipped. Never
free-form forecasts (every free-override experiment failed pre-project).
Training: `train_gemma_sft.py`, env-var driven, TRL SFTTrainer
prompt/completion path (completion-only loss VERIFIED and pinned by
`tests/test_sft_masking.py`). Eval: `eval_gemma_responses.py --batch-size 16
--resume` (11× batched generation), scorer emits error + ranking metrics
(week-wise Spearman, top-11 realized).

**Decision layer**: exact optimizer holds all hard constraints (budget with
sell/buy prices, 3-per-team, position quotas, formations, FT banking, hits,
BB/TC chip DP; wildcard/free-hit simulation added, flag-gated).
`DecisionWeights` presets expose scoring knobs (`--decision-variant`).
LLM deltas apply via `--llm-examples/--llm-predictions/--llm-fields`
(all/points/availability/availability_scaled) in `src/fpl_ai/llm_adjust.py`.

**The gate**: rolling GW12-30 2025-26 squad backtest (synthetic initial
squad, 1 transfer/wk, chips optimized) = the ship/no-ship test.
**Classic-only = 1,058 actual points.** LLM ships as GW1 default only if it
beats that; otherwise classic ships + LLM shadow mode.

## 3. Data assets

- **History**: vaastav FPL data 2022-23 → 2025-26 (GW30 as of July),
  `data/fpl_training_rows.csv` canonical (~106,699 corpus rows).
- **Evidence stores** (`reports/evidence_*`): Guardian football 2022-26
  (25,852 articles, full backfill); PL/Sky fulltext 2025-26; **official PL
  Scout 2,808 articles 2021-26 via Pulselive API** (Scout Selection weekly
  best-XI in EVERY season, 38-39/season; tag `content-creator:The-Scout`);
  Sky written FPL expert tips 49 articles (2022-23 → 2023-24 GW14, series
  then discontinued → became the Sky Fantasy Podcast, 87 episodes indexed
  with MP3s, transcription queued).
- **Corpus lineage** (`reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_*`):
  v1 base → v2 player evidence → v3 +fixture outlook → v4 +congestion
  (UCL/UEL/UECL proximity, post-break) → v5 +exact ridge decomposition
  (0 drift) → v6 +role context → **v7 (canonical) +scout evidence attached**
  (9,771 PL-Scout doc-attachments player-matched).
- **Builder** `scripts/build_residual_player_forecast_split_v2.py` flags:
  `--no-evidence --include-fixtures --include-congestion --include-provenance
  --include-decomposition --include-role --compact-context --prefer-scout
  --preferred-chars`. E6 full schema max 926 tokens.
- European fixtures: `data/competition_fixtures/european_fixtures.jsonl`
  (fixturedownload.com feeds, browser UA needed; UCL/UEL 2022-25, UECL 2024+).

## 4. Forecast ladder — all results (top-128 GW12-30 2025-26)

| metric | classic | E1 struct | E2 evid | E3a rich | E4 pool+fix | E5 +congest |
|---|---|---|---|---|---|---|
| 1GW MAE | 2.575 | 2.435 | 2.435 | 2.429 | **2.423** | 2.427 |
| 5GW RMSE | 9.186 | 8.920 | **8.887** | ~8.9 | 8.931 | 8.910 |
| appear MAE | 0.205 | 0.180 | 0.172 | 0.169 | **0.161** | 0.162 |
| Spearman 1GW | 0.165 | 0.150 | 0.145 | 0.160 | **0.166** | 0.158 |
| strict JSON | — | 100% | 100% | 100% | 100% | 100% |

- **E0 (base model)**: zero deltas, 68% strict JSON — fine-tuning owns all
  effects.
- **E1**: structured-only already beats classic on error metrics (learned
  shrinkage); ranking flat.
- **E2/E3a**: article evidence NULL (E1≈E2≈E3a; usage diagnostics flat;
  official status/news in the structured prompt already carries the
  availability signal). Articles dropped from forecast prompts.
- **E4** (2× data, top-256 pool, fixture outlook): best availability
  calibration; first non-negative Spearman; ranking still flat.
- **E5** (+congestion block, labels identical): NULL — model ignores it.
- **E6** (running, ETA 07-13 AM): + exact baseline decomposition,
  provenance ("adjust only for what the classic signal cannot see"), role
  fragility line (L3 vs L8 starts), compact context. Wes's base-anatomy
  hypothesis: teach the model what the base is made of so text/status
  models the residual.
- **Recurring pattern**: SFT reliably improves calibration/error via learned
  shrinkage; no adapter yet has rank skill (Spearman/top-k ≈ classic).

## 5. Gate & decision-layer findings

**Gate scoreboard**: classic 1,058 | E3a all-fields 1,000 | E4 all-fields
1,020 | availability+soft-optimizer **1,056 for BOTH E3a and E4** |
oracle greedy 1,796. Classic ships GW1 unless something beats 1,058.

- **Proven mechanism**: the optimizer's old threshold availability penalty
  made LLM availability decision-inert (±0); with the `avail_soft` variant
  (soft multiplicative weight), LLM P(appear) recovers +25 vs soft/classic-P
  — real, reproducible, but ties classic.
- **Multi-window rule** (locked): decision changes need ≥3 windows
  (2023-24/2024-25/2025-26 GW12-30); single-window totals carry ~±40 pts
  noise (avail_soft went −27/+9/+11). horizon5 and 2-transfers-per-week
  rejected on all windows.
- **Transfer lookahead: permanently closed** (Wes's oracle test design):
  full-oracle (all decisions on realized outcomes) lookahead = greedy
  EXACTLY on all 3 windows, 0 banked weeks → structural option value of FT
  banking is zero at 1 transfer/wk. Hybrid (oracle valuation, classic
  execution) actively harmful (−38): never bank on information your future
  executor won't have. **Oracle greedy − classic greedy = +738 pts/season =
  the entire prize pool is forecast/rank quality; none is planning depth.**
- **In-sample trap**: 2023-25 windows can't validate current adapters
  (those seasons are training data). True multi-window LLM validation needs
  chronological retrains (chrono-2425 staged: dataset + runner, ~16h,
  optional pending Wes).

## 6. GRPO decision-layer track (G1/G2)

Wes promoted GRPO from post-GW1 to next-in-line (it's fully offline: train
on 2022-25 states, test on the untouched 2025-26 GW12-30 gate).

- **G1 (weekly-bandit, ready)**: state = classic-trajectory squad at week W;
  policy emits bounded JSON (DecisionWeights + captain pick + transfer
  aggressiveness); reward = realized points − classic baseline realized
  (paired, kills most noise); group-normalized advantages (G=8); next state
  resets to classic trajectory (no cascade). ~70M trainable LoRA params but
  KL-leashed (β=0.04) → effectively fitting ~5 knobs; on-policy resampling
  per epoch → ~7,500 rollouts at 8 epochs.
  Assets: `reports/grpo_states/` (117 train states: 2022-23 GW6-38,
  2023-24/2024-25 GW2-38, 2025-26 GW2-11; eval file quarantined),
  `src/fpl_ai/grpo_env.py` + tests, `train_gemma_grpo.py` (+`--dry-run`,
  validated), `scripts/run_grpo_decision_eval.py` (paired per-week delta is
  the metric; env scoring excludes autosubs/chips).
  Known risk: tie-rate (~70% of single-knob actions tie baseline) →
  captain_pick carries early signal; next lever = squad-diversity
  augmentation from variant trajectories (~4× states).
- **G2 (sequential, compute-heavy, 2-4 GPU-days)**: policy's squad carries
  across weeks (chips, transfer sequencing, fixture-swing planning);
  gated on G1 showing signal; decision ~07-16; falls back post-GW1 if
  marginal. 12B one-shot check may fold in.

## 7. Decisions log (chronological)

1. LLM load-bearing; classic ML is a signal (project founding).
2. Residual bounded deltas, never free-form (pre-July experiments).
3. LoRA stays; full FT rejected (capacity not bottleneck; loss ~0.16).
4. RL at decision layer only, forecast rewards too noisy (2026-07-08);
   revised 2026-07-10: GRPO needs nothing from GW1 → promoted.
5. Planning split: optimizer owns constraints; LLM parameterizes via
   structured outputs (2026-07-08).
6. Articles out of forecast prompts (E2/E3a null); evidence kept for
   reports/citations; scout-genre re-test queued as E7-scout.
7. Multi-window (≥3) evaluation for all decision changes (2026-07-09).
8. Lookahead/planning-depth permanently closed (oracle test, 2026-07-10).
9. Classic ships GW1 default; LLM shadow unless gate beaten (standing).
10. Naming: E-runs = forecast SFT; G1/G2 = GRPO decision layer.

## 8. Hardware & ops handbook (GB10 / DGX Spark)

- venv `/home/wescheng/venvs/fpl-gemma-lite`; model `google/gemma-4-E4B-it`;
  `HF_HUB_DISABLE_XET=1`; `PYTORCH_ALLOC_CONF=expandable_segments:True`.
- Memory law: batch 2 × accum 8 fits ≤ ~900-token prompts, but **"fits at
  launch ≠ survives"** — allocator drift took a 926-token batch-2 run from
  22GB → 0GB free by step 186. Above ~900 tokens: batch 1 × accum 16 from
  the start (same effective batch, ~62GB free, stable, no grad-ckpt needed;
  grad-ckpt doesn't help anyway — peft target_parameters defeats recompute).
- **save_steps=100** in all runners (~1.9h max loss; box has power-cut
  history — 2026-07-08 outage killed a run at step 985).
- Protect the box: `echo 800 > /proc/$PID/oom_score_adj` on every trainer.
- Kernels: SDPA already dispatches to native flash kernel on GB10;
  flash-attn package unnecessary/unavailable (aarch64, sm_121). Box is
  bandwidth-bound (~273GB/s): free RAM ≠ speed. torch.compile = the one
  untested lever (benchmark queued; risky: peft ParamWrapper + sm_121
  Triton). TF32 irrelevant (bf16 training).
- Monitors: persistent Monitor per training run (progress/low-mem/death);
  stop stale monitors before relaunching same-named scripts; verify pids
  with ps (pgrep catches transient shells). pgrep patterns must be quoted.
- Backtests are CPU (~15 min/window); run with oom_score_adj 900,
  2-3 concurrent max alongside training.
- 2026-27 FPL API not launched as of 07-08; re-check weekly. Guardian
  shared 'test' API key is throttled — Wes should register a real one.

## 9. Current status & forward plan (2026-07-12)

- **Running**: E6 (step ~800/2000, ETA 07-13 AM, healthy at 51GB free).
- **Queue**: E6 eval + gate re-run (all-fields + availability/avail_soft —
  the 1,056 config is where E6's availability gains would convert) →
  **G1** (hours) → **E7-scout** (scout evidence at 800-char budget on v7,
  seq 1280 batch-1, ~2 days) → G2 decision (~07-16).
- **GPU-gap fillers**: torch.compile benchmark; Whisper transcription of
  87 podcast episodes (~19 GPU-h).
- **Open decisions for Wes**: chrono-2425 retrain (validate the 1,056
  config out-of-window, ~16h); G2 timing after G1 results.
- **Runway**: ~4.5 weeks to GW1. Remaining launch-critical work beyond
  experiments: weekly runbook (Phase 4 plumbing), live evidence collection
  incl. PL Scout + podcast, 2026-27 API integration when it launches.
