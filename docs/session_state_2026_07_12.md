## E9-cleansplit launched 2026-07-30 (Wes's actual 2026-27 ship candidate — TOP PRIORITY)

Wes's idea, given 2026-27 launches in ~3 weeks: the standing "train through
current-season GW11, eval GW12-30" protocol isn't what he'll actually be
able to do at GW1 2026-27 (no same-season data will exist then). Proposed
training purely on complete prior seasons and testing on all of 2025-26
instead — matches the real deployment condition and widens the held-out
test substantially. **This superseded G2-v3 in priority — G2-v3 was
killed mid-training (step 6/232, ~47 min in, trivial loss) to free the
GPU.** G2-v3's code fix (season-level + half-renewing chip budget) is
committed, tested, and correct — only the training run was paused; resume
with `setsid nohup scripts/run_gemma_e4b_grpo_plan_v3.sh > logs/train_grpo_plan_v3.log 2>&1 < /dev/null & disown`
+ same for `run_g2v3_post_train_chain.sh` once E9 clears.

**E9 recipe**: byte-identical to E7 (corpus v7_scout) except
`--train-through 2024-25:38` (zero 2025-26 rows, was `2025-26:11`) and
`--eval-weeks 2025-26:2-30` (was `2025-26:12-30`). Split: train 29,184
rows (was 32,000), eval **7,424 rows** (was 4,864 — 53% bigger). Gate
widened to match: `backtest-squad --initial-train-week-max 1 --start-week 2
--end-week 30` (was `11`/`12`). Sanity-checked the widened backtest
standalone (CPU, classic-only) before spending GPU time: 1,471 total
actual points on GW2-30 — **not comparable to the old 1,058 (GW12-30
only)**. The E9 chain reruns this classic-only anchor on the same GW2-30
window as its last step so the verdict is self-contained and fair.

Launched 2026-07-30 22:02 (`scripts/run_gemma_e4b_residual_e9_cleansplit.sh`,
setsid-detached, verified ppid 1, oom 800), ETA ~40-44h. Chain armed 22:03
(`scripts/run_e9_post_train_chain.sh`): eval (7,424 rows) → top-128 subset
scoring (ladder comparability) → 3 gate configs on GW2-30 → classic-only
GW2-30 anchor rerun. **Stops at the gate for review.** Full detail:
[[fpl-e9-cleansplit]]. Progress: `logs/train_e4b_residual_e9_cleansplit.log`
→ `logs/e9_post_train_chain.log`.

## G2-v3 launched 2026-07-30 (season-level chip-budget fix + retrain — PAUSED, see E9-cleansplit above)

**E8 verdict (2026-07-29): NEGATIVE, do not ship.** Gate: all-fields
1,025 / availability_scaled 1,002 / avail_soft 1,060 — below E7 (1,069) in
all three, below classic (1,058) in two of three, despite better eval-set
MAE. Full writeup: `docs/experiment_log_e4b_residual_2026_07.md` §"E8-podcast
result"; [[fpl-e8-podcast-evidence]]. **E7 (1,069) remains the standing
forecast-layer champion.**

Next lever, per the already-queued item in [[fpl-g2-deployment-regime]]:
**G2-v3, the season-level chip-budget bug fix.** The bug: `PlanEpisodeEnv`
reset bench_boost/triple_captain legality fresh every 6-week window, so
G2-v2's composed 3-window season eval could replay a chip up to 3x —
impossible in real FPL (each chip once per season). Before committing to
a ~30h retrain, ran a cheap (~10 min inference) diagnostic: fixed
`src/fpl_ai/grpo_plan_env.py` (`PlanEpisodeEnv.available_chips`, illegal
replays masked in `rollout()`, prompt states real remaining chips) +
`scripts/run_grpo_plan_eval.py` (sequential per-window generation,
threading `remaining_chips` across a season) and re-ran the **existing
v2 adapter** through it:
- classic states: **+23 (3W/0L/0T)**, was +47 (buggy) — roughly half.
- adjusted states: **+20 (2W/0L/1T)**, was +27 (buggy) — about 74%.

Edge survives but shrinks a lot — confirms the bug was real. Bigger
finding: v2's policy requests a chip almost every week regardless of
what's actually left (verified in raw responses — window 3 with zero
chips available still asked for bench_boost, silently masked to "none").
It never learned to condition on chip scarcity because training episodes
were independent bandit samples that always got a fresh two-chip budget.

**v3 fix**: `train_gemma_grpo_plan.py` now samples a chip-availability
budget per training episode (both/one/none, weighted 0.5/0.2/0.2/0.1,
seeded by state_key) so the policy has to learn to read the prompt's
"chips still available" line. Only change from v2's recipe (same adjusted
states, 59 episodes, horizon 6/stride 1/8 epochs/fresh LoRA). Dry-run
confirmed clean. Launched via `setsid nohup ... & disown` (both processes
verified ppid 1): `scripts/run_gemma_e4b_grpo_plan_v3.sh` (training, ETA
~28-30h) → `scripts/run_g2v3_post_train_chain.sh` (armed, waits for
`train_runtime` + adapter, then runs the season-chip-aware composed-stack
eval with `--min-new-tokens 8` from the start on both classic/adjusted
2025-26 GW12-30 states). **Stops at the gate for review** — compare v3
against the v2-corrected baseline (classic +23, adjusted +20), not v2's
original buggy numbers. Full detail: [[fpl-g2-v3-chip-budget]].
Progress: `logs/train_grpo_plan_v3.log` → `logs/g2v3_post_train_chain.log`.

## E8-podcast launched 2026-07-26 (GPU idle overnight, unattended chain)

Next rung after the G2-v2/v2b ablation (full comparison in
`docs/g2_results_and_faq_2026_07_26.md`): **E8 = E7 recipe (E6 schema +
scout evidence, --prefer-scout, 2 docs × 260 chars) + a new evidence
source** — Whisper large-v3 transcripts of the Sky Sports Fantasy Podcast
(RSS `feeds.captivate.fm/sky-sports-fantasy`, available since the Aug-2024
feed migration, so it covers all of 2024-25 + 2025-26). This was a
standing queued item ("Whisper transcription of 87 podcast episodes,
~19 GPU-h", see [[fpl-evidence-sources-audit]]) never actually run at
production scale — the only prior transcript was a 1-episode pilot. Chose
this over G2-v3 (fresh RL run) because: (a) it's SFT on the load-bearing
forecast layer per the standing rule ([[fpl-llm-load-bearing]]), (b) it's
the explicitly-approved-but-not-yet-executed lever from
[[fpl-approved-sequence-2026-07-08]] ("more supervision per row... over
more rows" / rationale-augmented text), (c) it reuses an already-audited,
already-smoke-tested pipeline rather than inventing new label schemes
unattended, and (d) real new article/text data was requested — this is
exactly that, not a resample of existing signal.

Recipe (byte-identical to E7 except the added evidence file, so this is a
clean single-variable ablation): corpus v6_role → attach **all 8**
evidence files together in one call — `evidence_guardian_football_2022_23/
2023_24/2024_25/2025_26.jsonl` + `evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl`
+ `evidence_pl_scout_2022_26.jsonl` + `evidence_sky_fpl_expert_tips_2022_26.jsonl`
+ new `evidence_sky_podcast_transcripts_fantasy_2024_26.jsonl` (79 relevant
episodes after title filtering) — with `--include-non-curated` (Sky isn't in
`DEFAULT_CURATED_SOURCES`) → v8_podcast.jsonl →
`build_residual_player_forecast_split_v2.py` with E7's exact flags
(`--include-fixtures --include-congestion --include-provenance
--include-decomposition --include-role --compact-context --prefer-scout
--preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260
--train-through 2025-26:11 --eval-weeks 2025-26:12-30 --top-n 256`) → same
seq-1536/grad-ckpt/lr5e-5/batch1×accum16 training hyperparams as E7.

**Launch mishap + fix (2026-07-27 morning)**: `attach_player_evidence_to_corpus.py`
*replaces* `metadata.evidence_documents` wholesale on every call rather than
merging across calls — the true v7 corpus was built from all 8 files above
in one call. My first attempt only passed the 2 new scout-adjacent files,
silently discarding the Guardian ×4 + PL-fulltext evidence v7 also relied
on. The pipeline's sanity gate did its job: `train_evidence_present`
dropped from v7's 26,987 to 8,785 and the chain correctly refused to
launch training. Rebuilt attach with the complete 8-file list (also missed
`evidence_guardian_football_2025_26.jsonl` on the first correction pass —
2025-26 coverage lagged at 3,529 rows until it was added) → final v8:
train_evidence_present **26,998/32,000 (84.4%)**, eval_evidence_present
4,267 — both a hair above v7's 26,987/4,239, confirming the podcast source
is adding a small incremental amount on top of, not instead of, everything
v7 already had. Training relaunched from this corrected corpus.

**Process-management lesson (new)**: the first training launch attempt
combined `nohup ... &` with a `sleep 120` verification step inside one
Bash-tool call; the tool's own 2-minute foreground timeout sent SIGTERM to
the whole process group when it expired, killing the *nohup'd* trainer
along with it (caught it stalled mid-tokenize at 65%, log stopped exactly
at the timeout boundary). Fix: launch with `setsid nohup ... < /dev/null &
disown` so the child is in its own session (ppid 1) and immune to the
launching call's own timeout, then verify with a short separate call.
Apply this any time a background job is started directly from the agent's
Bash tool (as opposed to from within an already-running shell script,
which was already fine).

Chain (fully unattended, artifact-verified at each stage, matches
[[fpl-chain-pipeline-stages]] conventions):
`scripts/run_e8_podcast_evidence_pipeline.sh` (original launch 2026-07-26
00:25, pid 429007; corpus/split rebuilt by hand 2026-07-27 after the
sanity-gate catch above) — transcribes the podcast backlog → builds v8
corpus + split → **sanity gate**: asserts train/eval row counts unchanged
from v7 (32,000/4,864) and `train_evidence_present` strictly above v7's
26,987 (84.3%) before spending GPU time training → launches E8 training
(`scripts/run_gemma_e4b_residual_e8_top256_podcast_evidence.sh`, relaunched
2026-07-27 08:24 via setsid, pid 450188, oom guard 800) → arms
`scripts/run_e8_post_train_chain.sh` (relaunched 2026-07-27 08:25 via
setsid, pid 450323) — eval + top-128 subset scoring + the same 3-window
gate backtest as E7: all/baseline, availability_scaled/baseline,
availability/avail_soft. **Stops at the gate for review** — comparing E8
against E7 (1,069) and classic (1,058) is a judgment point, not
auto-cascaded into a G2 retrain.

Rough timeline from the 08:24 relaunch: training ~40-48h (E7 precedent) +
eval/gate ~2-3h ≈ 2 days from 2026-07-27 morning.
Progress: `logs/e8_podcast_evidence_pipeline.log` (original pipeline run),
`logs/train_e4b_residual_e8_top256_podcast_evidence.log` (training —
restarted 2026-07-27 08:24, ignore any tokenizing progress before that
timestamp, it belongs to the killed first attempt), `logs/e8_post_train_chain.log`
(eval/gate, once armed). Verdict lands in
`reports/backtest_gw12_30_llm_e8_all_baselineopt/rolling_squad_backtest.json`
(`total_actual_points`, compare to E7's 1,069 / classic's 1,058).

Not done tonight (deliberately scoped down to keep this bounded and
reviewable): the Sky Sports Premier League Podcast (bigger show, covers
all 4 seasons back to 2015, but ~3-4x the transcription volume and no
existing index/estimate) — natural next data-expansion step if E8 gates
positively. Also not started: G2-v3 (season-level chip-budget bug fix +
retrain) — flagged in [[fpl-g2-deployment-regime]] as the next G-track
lever but intentionally not run in parallel with E8 to keep this a clean,
reviewable single change.

---

# Session State — 2026-07-12 (supersedes session_state_2026_07_09.md)

Covers 2026-07-09 → 2026-07-12. Companion docs:
`docs/experiment_log_e4b_residual_2026_07.md` (all experiment results),
`docs/decision_layer_plan_2026_07_09.md` (planning/GRPO design),
`project_plan_2026_07_05.md` (approved plan). This file is the operational
"what is running, what happened, what to type next".

## Running right now (updated 2026-07-13)

- **E6 training COMPLETE** (2026-07-13 04:28): 2000/2000 steps, train loss
  0.182, adapter `artifacts/gemma4_e4b_lora_residual_v2_e6_top256_full_schema`.
- **E6 eval running** (`scripts/run_gemma_e4b_residual_e6_eval.sh`,
  log `logs/e6_eval.log`): SFT + base predictions on 4,864 eval rows, then
  residual scoring → `reports/e4b_residual_e6_top256_gw12_30_eval_summary.json`.
- **Auto-chain armed** (`scripts/run_e6_post_eval_chain.sh`, log
  `logs/e6_post_eval_chain.log`): when the eval summary lands it launches
  G1 GRPO on the freed GPU (`logs/train_grpo_v1.log`, oom 800) and runs the
  CPU analysis — top-128 subset scoring + 3 gate backtests (all/baseline,
  availability_scaled/baseline, availability/avail_soft → dirs
  `reports/backtest_gw12_30_llm_e6_*`, oom 900). Lesson (Wes, 07-13): chain
  approved stages on disk; never leave the GPU idle waiting for a human or
  a monitor notification.

## Approved queue (Wes; updated 2026-07-15)

E6 ✅ → E6 eval + gate ✅ (ties classic 1,058) → **G1 running** (ETA
2026-07-15 ~13:00; auto decision-eval chained) → **E7-scout auto-launches
when G1 chain finishes** (`scripts/run_e7_launch_chain.sh` armed; runner
`scripts/run_gemma_e4b_residual_e7_top256_scout_evidence.sh`, seq 1536 +
grad ckpt, dataset built: 32k train rows, 84% with scout evidence, max
1,502 tokens). **Wes 2026-07-15 (delegated call): G2 stays after E7**
regardless of G1 eval — G1's bandit construct caps RL's multi-step upside
and 117 states is thin; G1 training rewards were flat (~−0.4, no trend).
Chrono-2425 retrain optional (staged, ~16h). GPU-gap fillers:
torch.compile benchmark, Whisper transcription of 87 podcast episodes.

**Naming**: E-runs = forecast SFT ladder; G1/G2 = decision-layer GRPO.

## Experiment verdicts (2026-07-09 → 12; details in experiment log)

| what | verdict |
|---|---|
| E4 (2× data, top-256, fixtures) | Best availability MAE (0.161 top-128) + first non-negative Spearman; ranking still flat; **gate FAILS** (all-fields 1,020 vs classic 1,058) |
| E5 (= E4 + congestion block) | **NULL** — ≈E4 everywhere; model ignores the block (usage diagnostic flat) |
| Decision-knob sweep (horizon5, 2-transfers, avail_soft) | horizon5/2-transfers rejected on 3 windows; avail_soft a wash (−27/+9/+11) |
| **LLM availability + avail_soft optimizer** | **1,056 for BOTH E3a and E4** (vs 1,031 soft/classic-P): signal is real & decision-relevant, ties classic (1,058), never beats it |
| 2-week transfer lookahead | Rejected 3 windows, both projections |
| **Oracle test (Wes's design)** | Full-oracle banking option value **exactly 0** (identical totals, 0 banked weeks, all 3 windows). Hybrid (oracle valuation, classic execution) harmful (−38). **Oracle greedy − classic greedy = +738 pts/season = pure forecast-quality headroom; 0 from planning structure** |
| SFT masking audit (Wes's task) | Clean — completion-only loss verified end-to-end, pinned by tests/test_sft_masking.py; all E-runs trained correctly |

Standing rules locked: decision changes need **≥3 backtest windows**;
never revisit transfer-lookahead depth; LLM variants can't be validated on
2023-25 with current adapters (in-sample) — needs chrono retrain.

## New data/prompt layers (all corpus versions in reports/)

- v4: congestion (UCL/UEL/UECL proximity + post-break; fixturedownload
  feeds, browser UA required).
- v5: **exact ridge decomposition** of the classic 1GW baseline (grouped
  contributions; 96,477 rows, 0 drift vs stored baselines).
- v6: **role context** (L3 vs L8 start rates + fragility read:
  nailed/recently-promoted/losing-spot/rotation/fringe).
- **v7 (canonical)**: v6 + scout evidence attached per player.
- Builder flags: `--include-fixtures --include-congestion
  --include-provenance --include-decomposition --include-role
  --compact-context --prefer-scout --preferred-chars 800`.
  E6 schema max 926 tokens (batch-1 territory).

## Expert-recommendation corpus (Wes's Sky idea → bigger)

- Sky written weekly tips: 49 articles 2022-23→2023-24 GW14 (series then
  discontinued; enumerated via Wayback CDX, fetched live).
- **Official PL Scout via Pulselive API** (`scripts/backfill_pl_scout_articles.py`):
  **2,808 articles**, Scout Selection (weekly best XI) 38-39×/season in
  EVERY season 2022-26; tag `content-creator:The-Scout`, API paginates to
  2021; note tag pages are non-chronological (stale-pages stop condition).
- Sky Fantasy Podcast: own captivate feed, 87 episodes Dec 2024→present
  indexed (`reports/evidence_sky_fantasy_podcast_index.jsonl`); Whisper
  transcription queued (~19 GPU-h).
- v7 corpus has 9,771 PL-Scout + 398 Sky doc-attachments player-matched.
- **E7-scout recipe**: E6 flags minus --no-evidence, plus
  `--prefer-scout --max-evidence-docs 2 --max-evidence-chars 260`
  on corpus v7; seq 1280, batch 1 × accum 16, ~40-47h.

## GRPO (G1 ready; Wes promoted from post-GW1 — fully offline)

- State cache `reports/grpo_states/`: **117 train states** (2022-23 GW6-38,
  2023-24/2024-25 GW2-38, 2025-26-early GW2-11) + `2025-26.jsonl`
  (GW12-30, 19 states) = untouched held-out gate.
- Env `src/fpl_ai/grpo_env.py` (bounded actions: DecisionWeights + captain
  + transfer aggressiveness; paired reward vs classic; tests green).
- Trainer `train_gemma_grpo.py` (TRL 1.0 GRPOTrainer, G=8, KL β=0.04;
  `--dry-run` validated: default action reward-neutral, range −3..+17).
  Launch: `nohup python3 train_gemma_grpo.py > logs/train_grpo_v1.log 2>&1 &`
  (+oom guard). Eval: `scripts/run_grpo_decision_eval.py` (paired per-week
  delta is the metric; env scoring excludes autosubs/chips).
- Signal risk: tie-rate (single-knob actions tie baseline ~70% of weeks);
  captain_pick carries early signal; next lever = squad-diversity
  augmentation from variant trajectories on disk (~4×).
- **G2** (sequential rollouts, chips, per-player multipliers, 2-4 GPU-days):
  decision ~07-16 after G1 results; falls back post-GW1 if G1 marginal.

## Hardware lessons (added to auto-memory)

- **"Fits at launch ≠ survives"**: 926-token batch-2 run drifted 22GB→0GB
  free by step 186 (allocator growth). Above ~900 max tokens → batch 1 ×
  accum 16 from the start (same effective batch; ~62GB free, stable).
- **save_steps=100** now in all runners (was 400 = 7.8h between checkpoints
  at batch-1 pace; box has power-cut history).
- Kernel audit: SDPA already dispatches to native flash kernel on GB10;
  flash-attn pkg unnecessary; box is bandwidth-bound (~273GB/s) so free RAM
  ≠ speed; torch.compile is the one untested lever (queued, risky due to
  peft ParamWrapper + sm_121 Triton).
- Monitor hygiene: stop stale monitors before relaunching same-named
  trainers; verify pids with ps (pgrep can match transient shells).

## Gate scoreboard (2025-26 GW12-30, the ship/no-ship number)

classic 1,058 | E3a all-fields 1,000 | E4 all-fields 1,020 |
E6 all-fields 1,035 | **E7-scout all-fields 1,069 — FIRST WIN (+11)** |
E6/E7 availability + soft optimizer 1,058 (tie) | oracle greedy 1,796.
**Pending out-of-window confirmation**: E7-chrono-2425 running (launched
2026-07-18, pid 262740, ~36h → ETA 07-20 morning; eval/gate on 2024-25
GW12-30). If it also beats classic → E7 is the GW1 ship candidate; if not,
+11 was single-window noise and classic stays default. E7 details in the
experiment log; G1 GRPO verdict: marginal (+7 total, 7W/5L/7T held-out).

## G2 plan-GRPO (built 2026-07-18; Wes approved G2 next over waiting)

**Formulation**: TRL is single-turn → policy emits a K-week PLAN (JSON
array of weekly actions) in one completion; env rolls it through chained
weekly states with squad/bank/FTs evolving under the policy's own choices.
Actions = G1 knobs + bank_transfer + chip_play (bench_boost /
triple_captain, once per window). Reward = cumulative realized − paired
all-defaults sequential baseline. This expresses exactly what G1's bandit
couldn't: banking, chip timing, transfer sequencing.
- `src/fpl_ai/grpo_plan_env.py` (8 tests, suite 74 green),
  `train_gemma_grpo_plan.py` (dry-run: 97 episodes h6/s1, prompts ≤782
  tok, default-plan neutral, canned rewards −34..+25 — 10× G1's variance).
- **Auto-chain armed** (`scripts/run_e7chrono_post_train_chain.sh`):
  chrono done → chrono eval → 2024-25 gate (classic_only anchor + 3 LLM
  configs) → G2 auto-launches on classic states (`logs/train_grpo_plan_v1.log`).
- **Wes's 07-18 refinement: G2 must train in the deployment regime — on
  E7-adjusted forecasts, leak-free via chrono adapters** (chrono-2425
  adjusts 2024-25 GW12-38, chrono-2324 adjusts 2023-24 GW12-38; 2022-23 /
  2025-26-early have no clean adapter → classic or dropped). Policy stays
  base + fresh LoRA (E7's value flows through state numbers; TRL's KL ref
  is adapter-disabled base, so E7-weight-init washes out — ablation only).
  Revised plan: treat auto-launched classic-state G2 as a ~50-step
  machinery smoke (kill it) → chrono-2324 train (~20h, runner + dataset
  READY: `scripts/run_gemma_e4b_residual_e7chrono2324.sh`) → SFT-only
  inference over the adjustment surfaces → build adjusted state caches →
  **G2-v2 on adjusted states** → two-way composed-stack eval on 2025-26.
  **Wes 07-18 clarifications**: the GW12-38 "eval" splits are inference
  surfaces for G2 training states, NOT evaluations — the only
  decision-driving eval is 2025-26 GW12-30. Cross-season legality maximizes
  training data (~74 adjusted states / ~62 episodes): chrono-2425 adjusts
  2024-25 GW12-38 + 2025-26 GW2-11; chrono-2324 adjusts 2023-24 GW12-38 +
  2024-25 GW2-11. Surfaces all READY (6,912 + 6,912-in-dataset + 2,560 +
  2,560 rows). G2 state rows must show classic AND adjusted numbers (the
  delta = the distilled text signal, so the policy can act on what the
  scouts moved). E7-LoRA-init: parked (weights don't carry articles;
  outputs do — but v2b ablation = G2 init from E7 LoRA, booked ~07-25).
- **State-adjustment pipeline BUILT (07-18 evening)**:
  `scripts/build_adjusted_grpo_states.py` — applies chrono deltas
  (llm_adjust, fields=all), stores per-player `llm_deltas` {d1,dP} + scout
  `evidence_snippets` (snippets are timestamp-safe for ALL weeks; only
  deltas need chrono legality). Two snippet modes: `window`
  (mention-centered, 180 chars) and `llm` (base-model condensation;
  `--emit-condense-prompts` → 4,308 prompts READY at
  `reports/grpo_condense_prompts.jsonl`, ~25 min GPU via
  eval_gemma_responses.py greedy decode, feed back via `--summaries`).
  WeeklyState/loader + PlanEpisodeEnv extended (Δ1gw column + Scout notes
  block, ≤10 × 180 chars); adjusted 2025-26 cache built with E7 preds
  (19/19 states have deltas+snippets); prompts max 2,530 tokens → launch
  G2-v2 with FPL_GRPO_MAX_PROMPT_LENGTH=2688; expect ~450-500s/step ≈
  2.5d. For 2023-24, episodes straddling GW11/12 mix unadjusted weeks —
  filter to delta-bearing weeks at trainer launch.
- **G2 eval script BUILT**: `scripts/run_grpo_plan_eval.py` (greedy plan
  per non-overlapping 6-wk window, paired vs all-defaults baseline; run
  with both `grpo_states/2025-26.jsonl` and `grpo_states_adjusted/…` for
  the composed-stack comparison; --mock smoke-tested on both).
  **Everything for the revised sequence is now staged.**

**Full consolidated results + FAQ (all comparison data points, what
works/doesn't, direct Q&A on E7 vs G2-v1/v2/v2b): see
`docs/g2_results_and_faq_2026_07_26.md`.**

### G2-v2 RESULTS (trained 07-22→07-24, evaluated 07-24)

**The revised sequence executed end-to-end via armed chains** (chrono-2324
train 19.7h loss 0.244/acc 0.934 → SFT inference both surfaces → adjusted
caches 2023-24/2024-25 with snippet-mode=llm → dry-run 59 episodes → G2-v2
launch). G2-v2: 232 steps / 8 epochs / 30.6h on 59 deployment-regime
episodes (2023-24 GW12+, 2024-25, 2025-26-early; REQUIRE_DELTAS filter
drops adapterless weeks). Training reward climbed monotonically: mean/30
steps −3.0 → −0.8 → +2.8 → +3.0 → +4.9 → +2.3 → +2.7 → +5.2; KL tiny
(0.0003-0.005); clipping 0.25-0.75; no collapse.

**Empty-EOS decode attractor found at eval**: greedy decoding returned
EMPTY completions on 4/6 windows (immediate EOS). Cause: GRPO never
penalizes the empty mode when a whole group is empty (zero std → zero
advantage), so the policy kept probability mass on immediate EOS; argmax
falls into it even though sampling (temp 0.8, the training regime) usually
escapes. **Fix: `--min-new-tokens 8` at decode** (deployment-legal; added
to run_grpo_plan_eval.py). Sampled decodes confirmed: parseable samples of
the same window land on identical realized outcomes.

**Composed-stack eval, 2025-26 GW12-30, 3 non-overlapping h6 windows,
greedy+min8** (env scoring excludes autosubs — paired delta is the metric,
totals NOT comparable to the 1,058 backtest gate):
- classic states:  policy 1015 vs baseline 968 → **+47, 3W/0L/0T**
- adjusted states: policy  967 vs baseline 940 → **+27, 3W/0L/0T**
- 6/6 windows won, 0 unparseable. Dominant learned behavior = chip
  timing (bench_boost placement; one triple_captain call worth +13).
- Caveats: only 3 windows per config (minimum for the ≥3 rule, small n);
  the env legalizes one chip PER WINDOW so a full season would replay
  bench_boost 3× (season chip budget is a known simplification, post-GW1
  fix); policy trained on adjusted states transfers to classic states
  (+47) — the plan skill is robust to the state variant, and the
  classic-vs-adjusted comparison within this env is noisy at n=3.
- Artifacts: `artifacts/gemma4_e4b_grpo_plan_v2`,
  `reports/grpo_plan_eval_2526_{classic,adjusted}_min8.json` (the
  no-min8 originals kept alongside for the attractor record).

**v2b ablation (E7-init) RESULT (07-25): does not beat v2 — v2 stays the
leading G2 candidate.** Implementation: peft only allows one
`target_parameters` adapter per model, so continuing the E7 adapter
directly failed; fixed by `PeftModel.from_pretrained(...).merge_and_unload()`
— merge E7 into base weights, then attach a fresh LoRA on top. This also
improves the ablation's validity: TRL's KL reference becomes base+E7
instead of raw base, so the init actually anchors training (old
"washes out" caveat no longer applies to this variant). Trained 232
steps/8 epochs/28.1h; reward climbed similarly to v2 (−1.9 → −1.1 → +0.2
→ +1.0 → +3.4 → +1.4, ending +8.6). Composed-stack eval (min8,
`--base-adapter` stacking):
  - adjusted states: **+28 (3W/0L/0T)** — matches v2's +27; identical
    per-window chip choices (bench_boost/triple_captain/bench_boost).
  - classic states: **+3 (1W/1L/1T)** — v2 scored +47 (3W/0L/0T) here.
    v2b played `triple_captain` in EVERY window regardless of state
    (rigid, undifferentiated) vs v2's per-window-adapted bench_boost.
  **Interpretation**: merging E7 specializes the policy to the exact
  adjusted-state input distribution it trained on — ties v2 there, no
  measurable edge — but at the cost of generalization: off-distribution
  (classic, no Δ/snippets) it collapses to a canned response instead of
  adapting. No offsetting benefit on the regime that matters, real
  robustness cost off it. **Decision: v2 (fresh LoRA) is the better G2
  candidate — simpler, ties on deployment-relevant metric, more robust.**
  Artifacts: `artifacts/gemma4_e4b_grpo_plan_v2b`,
  `reports/grpo_plan_eval_2526_{classic,adjusted}_v2b_min8.json`.

## E6 verdict (2026-07-13; details in experiment log)

Best run of the ladder: beats classic on every MAE (1GW/3GW/5GW points,
minutes, availability 0.250 vs 0.308) and — first ever — a **significant
top-11 realized lift: +2.95/wk, t = 2.41, 13W/4L/2T**. Gate ties but
doesn't beat: the optimizer leans on 5GW where E6 ties classic; the edge
lives in 1GW. Levers: 1GW-up-weighting decision variant (needs chrono-2425
for ≥3 windows) and G1 GRPO (launched 2026-07-13 evening, pid 153630,
`logs/train_grpo_v1.log`; fixes: TRL 1.0 dropped GRPOConfig
max_prompt_length → removed, prompt-length assertion added, budget
FPL_GRPO_MAX_PROMPT_LENGTH=1792 — longest state prompt is 1,734 tokens).
Restarted once more at step 120/464 (2026-07-14): 96-token completion cap
truncated 81% of rollouts mid-JSON (−1.0 penalty) and the policy was
collapsing to 2-token "{}" default outputs (safe 0.0) — the tie-trap.
Relaunched (pid 161184) with FPL_GRPO_MAX_COMPLETION_LENGTH=192 and a
"single line, no markdown fences" instruction added to the env prompt.
Watch completions/clipped_ratio (should be near 0) and reward (should
leave the −1..0 band) in `logs/train_grpo_v1.log`; ~188s/step ≈ 24h total.
**Dual-trainer incident (07-14)**: the v1 kill hit the background subshell,
not python — v1 ran 12h alongside v2 (contended GPU, interleaved log at
different byte offsets, shared checkpoint dir). Killed v1 by real pid
(153984), removed its checkpoints (50/100/150). v2 = python pid 161185,
verified env (completion 192, prompt 1792); its log lines carry the
`'completions/max_length': '192'` signature — read the log with
`tr -d '\000'` and filter on that. v2 health at ~step 80: rewards
oscillating −3..+2.6 (std ~2-3, groups not tying), KL ~0.005-0.013,
full JSON parses. ETA ~10h uncontended (~350-430s/step).
