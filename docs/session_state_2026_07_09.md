# Session State — 2026-07-09 (SUPERSEDED by session_state_2026_07_12.md)

Companion to `docs/experiment_log_e4b_residual_2026_07.md` (results & findings)
and `project_plan_2026_07_05.md` (approved plan). This file is the operational
"what is running and what to type next". Written before a context compaction;
treat as ground truth for resuming.

## Running right now

- **E6 training** (full base-anatomy schema: decomposition + provenance +
  role + congestion + fixtures, compact; labels byte-identical to E4/E5):
  `scripts/run_gemma_e4b_residual_e6_top256_full_schema.sh`.
  **Relaunched 2026-07-11 ~21:15 at batch 1 × accum 16** (first attempt at
  batch 2 hit 0GB free by step 186 — the 926-token schema sits on the
  batch-2 memory edge; same effective batch, expect ~30-40h). Trainer pid
  98624, oom_score_adj=800, monitor b2pumd39j.
  Log: `logs/train_e4b_residual_e6_top256_full_schema.log`.
  Output: `artifacts/gemma4_e4b_lora_residual_v2_e6_top256_full_schema`.
  - If it dies: resume with
    `FPL_GEMMA_RESUME_FROM_CHECKPOINT=<abs path to latest checkpoint-N> nohup scripts/run_gemma_e4b_residual_e6_top256_full_schema.sh > logs/e6_resume_launcher.log 2>&1 &`
- E5: DONE + evaluated — congestion NULL (see experiment log §E5). Adapter
  `..._e5_top256_congestion`; subset summary
  `reports/e4b_residual_e5_top128subset_gw12_30_eval_summary.json`.
- Corpus v7 (`..._v7_scout.jsonl`): v6 + official PL Scout (2,808 articles,
  Scout Selection every GW of every season) + Sky expert tips (49) attached
  per player — E7 evidence experiment ready (`--prefer-scout`).

## Wes's 4 tasks (2026-07-10): ALL DONE

1. Provenance block: `--include-provenance` in the builder (text derived
   from SAFE_FEATURE_COLUMNS; 867 max tokens with all blocks). For next run.
2. Oracle lookahead test: **lookahead closed for good** — full-oracle
   banking option value is exactly 0 on all 3 windows; oracle-vs-classic
   greedy gap = +738 pts/season = pure forecast-quality headroom. See
   experiment log §oracle. `reports/oracle_lookahead_test.json`.
3. Masking audit: completion-only loss verified end-to-end (TRL
   prompt/completion path); `tests/test_sft_masking.py` pins it. All past
   runs were trained correctly.
4. GRPO weekly-bandit env scaffolded: `src/fpl_ai/grpo_env.py` +
   `tests/test_grpo_env.py` (state prompt, bounded action parse, paired
   reward vs classic, group-normalized advantages, reset-to-baseline).

## E4: DONE (2026-07-10) — results in experiment log

Eval + top-128 subset + gate re-run all complete. Verdict: best
availability calibration (MAE 0.161), ranking flat, gate still fails
(all-fields 1,020; avail_soft+availability ties at 1,056). Classic ships
GW1 default; LLM shadow mode. E4 eval artifacts:
`reports/e4b_residual_e4_top256_gw12_30_eval_summary.json`,
`reports/e4b_residual_e4_top128subset_gw12_30_eval_summary.json`,
`reports/backtest_gw12_30_llm_e4_{all_baselineopt,availscaled_baselineopt,avail_softopt}`.

## E6 prompt schema READY (2026-07-10, Wes's ideas)

Canonical corpus is now `reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v6_role.jsonl`
(supersedes v4/v5; adds `baseline_decomposition` — exact additive ridge
breakdown, 0 drift rows — and `role_context`). E6 build command:

```
python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v6_role.jsonl \
  --output-dir reports/llm_residual_v2_e6_top256_full_schema_thru_gw11_eval_gw12_30 \
  --train-through 2025-26:11 --eval-weeks 2025-26:12-30 --top-n 256 \
  --no-evidence --include-fixtures --include-congestion \
  --include-provenance --include-decomposition --include-role --compact-context
```

Max 926 tokens (batch 2 × accum 8 safe; limit ~930). New blocks: baseline
composition (exact, grouped), provenance (what baseline knows/lacks), role
line (L3 vs L8 starts + fragility read). Labels stay byte-identical to
E4/E5. Launch after E5 eval by cloning the E5 runner with the new dataset.

## GRPO Phase-1 READY (2026-07-10; Wes promoted it — offline, no GW1 dependency)

Queue (Wes-approved): E5 eval → E6 → **GRPO Phase-1** → chrono-2425 (optional).

- State cache (wide, 2026-07-11): `reports/grpo_states/{key}.jsonl` —
  train = 2022-23 GW6-38 (33) + 2023-24 GW2-38 (37) + 2024-25 GW2-38 (37) +
  2025-26-early GW2-11 (10) = **117 states**; `2025-26.jsonl` (GW12-30, 19)
  = held-out gate, never in FPL_GRPO_TRAIN_SEASONS. Rebuilt by
  `scripts/build_grpo_state_cache.py`. Next scaling lever if signal is
  starved: squad-diversity augmentation from the decision-variant
  trajectories already on disk (~4× states).
- Env: `src/fpl_ai/grpo_env.py` (+ `load_states`); trainer:
  `train_gemma_grpo.py` (TRL 1.0 GRPOTrainer, fresh LoRA, reward =
  realized − classic baseline per state, G=8, KL beta 0.04).
- Validated via `python3 train_gemma_grpo.py --dry-run`: 117 states,
  prompts ~656 tokens, default action reward-neutral, reward range −3..+17.
- Launch (GPU): `nohup python3 train_gemma_grpo.py > logs/train_grpo_v1.log 2>&1 &`
  (set oom_score_adj=800 on the process; 117 states × 8 epochs × G=8 ≈
  7,500 rollouts — expect hours, not days).
- Eval after training: `python3 scripts/run_grpo_decision_eval.py
  --adapter-path artifacts/gemma4_e4b_grpo_decision_v1
  --output reports/grpo_decision_eval_2526.json` (greedy action per held-out
  2025-26 state, paired vs the classic default action; `--mock` = CPU smoke
  test, verified). Note env realized score excludes autosubs/chips — the
  paired delta is the metric, not the 1,058 backtest total.

## E7 candidate: scout-report/preview evidence (Wes's idea, 2026-07-11)

Sky scout reports are high quality but we only hold 89 Sky docs (2025-26) —
not trainable alone. Historical proxy: Guardian team-news/preview articles
(~9-10k/season attached). Builder now supports `--prefer-scout`
(+`--preferred-chars 800`): scout-genre docs (title: scout report/team news/
predicted line/preview/tips) rank first with a bigger budget. Smoke-tested:
640 train rows pin a scout doc. E7 recipe = E6 flags minus --no-evidence,
plus `--prefer-scout --max-evidence-docs 2 --max-evidence-chars 260` —
needs seq 1280 → batch 1 × accum 16 (known-good). Run only after E6 verdict;
it re-tests text with the strongest genre instead of generic packets.
Live 2026-27: weekly evidence collection should include skysports.com scout
reports — they'll auto-pin via the same pattern.

## GPU-gap queue (approved 2026-07-12)

When the GPU has idle windows between queued runs:
1. torch.compile benchmark (50-100 steps vs eager; watch peft ParamWrapper
   graph breaks + sm_121 Triton; adopt if clean +5%).
2. Whisper transcription of 87 Sky Fantasy Podcast episodes (~19 GPU-h,
   `reports/evidence_sky_fantasy_podcast_index.jsonl` has MP3 URLs;
   scripts/transcribe_sky_podcasts.py exists) — fits alongside G1.

## When E5 training completes

1. Copy `scripts/run_gemma_e4b_residual_e4_eval.sh` → e5 variant (swap
   dataset dir `llm_residual_v2_e5_top256_congestion_...`, adapter
   `..._e5_top256_congestion`, output names e5) and run it (GPU, ~1h).
2. Score top-128 subset (pattern: `reports/e4_top128_subset/` build script
   in transcript; per-week rank by builder `_baseline_score`, keep ≤128).
   Compare vs E4: availability MAE is the axis congestion should move.
3. Gate re-run only if availability/minutes improve: modes
   `availability` × `--decision-variant avail_soft` (the 1,056 config) and
   `all` baseline.
4. **Open decision for Wes**: chronological retrain for true multi-window
   LLM validation vs accepting single-window evidence + moving to GRPO.
   Assets pre-built (2026-07-10): dataset
   `reports/llm_residual_v2_chrono2425_top256_fixtures_thru_gw11_eval_gw12_30`
   (22,272 train / 4,864 eval rows) + runner
   `scripts/run_gemma_e4b_residual_chrono2425.sh` (~1,392 steps ≈ 16h).
   One command to launch when the GPU frees:
   `nohup scripts/run_gemma_e4b_residual_chrono2425.sh > logs/chrono2425_launcher.log 2>&1 &`
   (then set trainer oom_score_adj=800 and re-arm the monitor pattern).

## Decision-layer work done during the E4 window (2026-07-09)

- `DecisionWeights` presets in `decision.py` + `--decision-variant` CLI flag
  (baseline/horizon5/avail_soft/horizon5_avail); baseline reproduces 1,058
  exactly; 56/56 tests pass.
- Multi-window sweep results in experiment log §decision-layer: horizon5 and
  2-transfer variants rejected; avail_soft a wash; **E3a availability +
  avail_soft optimizer = 1,056 (+25 over avail_soft/classic)** — LLM
  availability signal is decision-relevant under a continuous-availability
  optimizer. Follow-up: generate 2024-25/2023-24 eval predictions post-E4
  to multi-window-validate avail_soft+LLM.
- Design/spec: `docs/decision_layer_plan_2026_07_09.md` (planning roadmap,
  congestion data sources verified, GRPO decision-layer spec).
- 2-week transfer lookahead implemented (`--transfer-lookahead 2`,
  `--lookahead-projection {schedule,horizon_diff}`) and **rejected on 3
  windows** — greedy transfers are near-optimal under current forecasts
  (FT banking ~zero option value). Details in experiment log.
- Congestion layer built: `data/competition_fixtures/european_fixtures.jsonl`
  (UCL/UEL 2022-25, UECL 2024-25), corpus
  `reports/..._v4_congestion.jsonl` (canonical; supersedes v3), builder
  `--include-congestion`. E5 candidate run = E4 recipe + `--include-congestion`
  on the v4 corpus (add `--corpus ..._v4_congestion.jsonl`).
- Wildcard/free-hit simulation added to the backtest
  (`--simulate-wildcard`/`--simulate-free-hit` + min-gain thresholds,
  default OFF so gate numbers stay comparable; mechanisms verified incl.
  free-hit revert). Chip timing is a GRPO action candidate.
- CPU queue is now empty; next work is GPU-gated (E4 eval → gate re-run →
  E5 with congestion prompts → LLM-availability multi-window validation).

## Results so far (detail in experiment log)

- Ladder E1/E2/E3a: SFT beats classic on error metrics (5GW RMSE −3%,
  appearance-prob MAE −18%) with 100% strict JSON; base model contributes zero.
  Text/articles verdict NULL (E1≈E2≈E3a; model ignores packets; official
  status/news already in structured prompt). Ranking (Spearman/top-k) still ≤ classic.
- Phase 3 gate first pass: ALL E3a application modes fail or tie
  (all-fields −58, availability-only ±0 because the optimizer's availability
  penalty only fires below P=0.65, availability_scaled −57). Better MAE ≠
  better decisions; squad value needs rank skill.
- Best current adapter: E3a (`artifacts/gemma4_e4b_lora_residual_v2_e3a_rich_packets`).

## Sequence (Wes-approved 2026-07-08; memory: fpl-approved-sequence-2026-07-08)

E4 → eval+gate → Phase 3 optimizer work (multi-GW lookahead; make decision
layer consume availability properly) → weekly runbook (Phase 4) → post-GW1:
GRPO at decision layer, 12B one-shot. LoRA stays; no forecast-layer RL.
2026-27 FPL game not launched as of 07-08 (API still 2025-26) — re-check weekly.

## Key infrastructure built this cycle (all tested)

- `scripts/attach_player_evidence_to_corpus.py` — per-player evidence matching.
- `scripts/attach_fixture_outlook_to_corpus.py` — next-5-GW schedule per row;
  corpus v3 = `reports/..._v3_evidence_fixtures.jsonl` (canonical).
- Builder `scripts/build_residual_player_forecast_split_v2.py`:
  `--no-evidence`, `--include-fixtures`, evidence doc/char knobs.
- `eval_gemma_responses.py --batch-size 16 --resume` (~11× faster eval).
- `src/fpl_ai/llm_adjust.py` + `backtest-squad --llm-examples/--llm-predictions/--llm-fields`
  (modes: all/points/availability/availability_scaled) + `tests/test_llm_adjust.py`.
- Scorer `score_player_forecast_residual_eval.py`: emits week-wise Spearman,
  top-11 realized, `ranking_lift` block.
- Guardian evidence 2022-26: `reports/evidence_guardian_football_{2022_23,2023_24,2024_25,2025_26}.jsonl`.

## Hardware/env gotchas (also in auto-memory fpl-project-environment)

- GB10 unified 119GB: E4B bf16 LoRA batch 2×accum 8 fits ≤ ~930-token prompts;
  ~1,050 tokens needs batch 1×accum 16 (grad ckpt alone does NOT save enough —
  peft target_parameters defeats recompute). Guard: `echo 800 > /proc/$PID/oom_score_adj`.
- Monitor pgrep patterns must be `pgrep -f "python train_gemma_sft.py"` (quote
  to avoid matching the monitor's own shell).
- Backtest classic forecasts == corpus baselines (same rolling protocol, alpha 1.0),
  which is why precomputed eval deltas apply cleanly in the backtest.
