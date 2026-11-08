# E4B Residual Experiment Ladder — Results Log

Updated: 2026-07-07. Runs per `project_plan_2026_07_05.md` Phase 1.
Eval: 2025-26 GW12-30 rolling window, top-128/week (2,432 player-weeks),
train window 2022-23 → 2025-26 GW11 (16,000 rows). Labels: shrunk (0.35) +
clipped residual deltas vs the classic ML anchor. Model: google/gemma-4-E4B-it,
bf16 LoRA, batch 2 × grad-accum 8, seq 1024, 1 epoch (1,000 steps, ~10-14h).

## Headline table (GW12-30)

| metric | classic ML | base E4B | E1 SFT (no text) | E2 SFT (evidence) |
|---|---|---|---|---|
| 1GW pts RMSE | **3.316** | 3.316 | 3.347 | 3.352 |
| 3GW pts RMSE | 6.406 | 6.406 | 6.384 | **6.375** |
| 5GW pts RMSE | 9.186 | 9.186 | 8.920 | **8.887** |
| 1GW pts MAE | 2.575 | 2.575 | 2.435 | **2.435** |
| 5GW pts MAE | 7.394 | 7.394 | 7.108 | **7.091** |
| appearance-prob MAE | 0.205 | 0.205 | 0.180 | **0.172** |
| minutes RMSE | **27.63** | 27.63 | 29.03 | 28.59 |
| Spearman 1GW (wk avg) | **0.165** | — | 0.150 | 0.145 |
| top-11 realized 1GW pts/wk | 49.47 | — | 49.26 | **51.00** |
| strict JSON | — | 68% | 100% | 100% |

## Findings

1. **E0 (base model)**: deltas are effectively zero; scores identical to classic
   ML. 32% of outputs aren't strict JSON. Fine-tuning owns all observed effects.
2. **E1 (structured-only)**: passes parity-or-better on error metrics — 5GW RMSE
   −2.9%, MAE better everywhere, appearance-prob MAE −12%. The model learned the
   anchor over-forecasts the top-128 pool and shrinks it. But ranking is
   flat-to-negative (uniformish shrinkage can't reorder), so E1 alone fails the
   "positive top-k lift" acceptance clause.
3. **E2 (per-player evidence packets, 2 docs × 260 chars)**: marginally better
   than E1 on nearly every error metric, and flips top-11 1GW lift positive:
   **+1.53 pts/week** vs classic (E1: −0.21). Not statistically significant on
   19 weeks (sd 8.66, paired t = 0.77; 10W/6L/3T).
4. **Evidence-usage diagnostic**: E2's delta magnitudes are nearly identical on
   evidence-present vs evidence-absent rows (mean |Δ1gw| 0.586 vs 0.566) — the
   model is not yet visibly conditioning on text. The current packets are thin
   (headline + ~1 sentence); the E1≈E2 risk flagged in the plan is live but not
   settled: token budget allows ~2× richer packets before hitting seq 1024.

## Infrastructure facts (for future runs)

- Batch 8 × seq 1024 bf16, no grad-ckpt OOM-kills the GB10 (119GB unified).
  Batch 2 × accum 8 fits: E1 peaked ~60GB free, E2 (longer prompts) ~7GB free.
  If tight, raise trainer `oom_score_adj` so system services survive an OOM.
- Batched generation (`eval_gemma_responses.py --batch-size 16 --resume`) gives
  ~11×: full base+SFT eval + scoring in ~30 min.
- Scorer now emits week-wise Spearman + top-11 realized points and a
  `ranking_lift` block (`score_player_forecast_residual_eval.py`).

## Artifacts

- E1: `artifacts/gemma4_e4b_lora_residual_v2_e1_structured`, summary
  `reports/e4b_residual_e1_structured_gw12_30_eval_summary.json`
- E2: `artifacts/gemma4_e4b_lora_residual_v2_e2_evidence`, summary
  `reports/e4b_residual_e2_evidence_gw12_30_eval_summary.json`
- Datasets: `reports/llm_residual_v2_e1_structured_only_thru_gw11_eval_gw12_30`,
  `reports/llm_residual_v2_e2_player_evidence_thru_gw11_eval_gw12_30`
  (identical rows/labels; prompts differ only by evidence)
- Evidence: Guardian 2022-26 backfill (25,852 articles) + PL/Sky canonical
  full text, attached per player by `scripts/attach_player_evidence_to_corpus.py`
- Fixture outlook (added 2026-07-08, ready for the next run): corpus v3
  (`..._v3_evidence_fixtures.jsonl`) carries `metadata.fixture_outlook`
  (next-5 GWs: opponent/venue/difficulty, blanks and DGWs explicit; 97.5%
  coverage — historical team_ids were -1 in the corpus, backfilled from
  merged_gw). Builder flag `--include-fixtures` renders it (~60 tokens);
  evidence+fixtures max 1,126 tokens → use seq 1152, batch 1 + grad ckpt.

## E3a result (2026-07-08): text verdict is null

E3a (2 docs × 450 chars) ≈ E2 ≈ E1 across the board: appearance-prob MAE
0.169 (ladder best), 1GW MAE 2.429 (best), 1GW Spearman 0.160 (best of the
SFT runs, still below classic's 0.165), top-11 lift +1.53/wk (same as E2,
t = 0.69, n.s.). Evidence-usage diagnostic still flat (mean |Δ1gw| 0.589
with articles vs 0.568 without) — doubling packet size did not make the
model condition on articles, so "packet too thin" is rejected.

Interpretation: E1 was never text-free — the structured snapshot already
carries official `status`/`news` (the highest-signal availability text), so
news articles add little for bounded delta prediction. Fine-tuning itself
works (100% strict JSON, consistent error gains, best availability
calibration); article packets are dropped from the forecast prompt.
Evidence still feeds the weekly report's cited explanations.

**E4 launched (2026-07-08)**: pool-widened top-256/wk (32k rows, 2× data),
structured + fixture outlook, no articles; max 753 tokens → fast batch-2
profile, ~2,000 steps ≈ 23h. Eval set is 4,864 rows (top-256); compare to
the ladder on its top-128 subset.

## Phase 3 gate, first pass (2026-07-08): E3a-adjusted FAILS

Rolling GW12-30 squad backtest (synthetic initial squad, 1 transfer/wk,
chips optimized, `backtest-squad --llm-examples/--llm-predictions`):

| pipeline | predicted total | actual total |
|---|---|---|
| classic ML only | 1,154.9 | **1,058** |
| E3a-adjusted (all fields) | 928.1 | 1,000 |

The LLM's calibration is better (predicts 928 vs realized 1,000; classic
over-predicts 1,155 vs 1,058) but squad selection is an ordering problem and
the selection score leans on 5GW — E3a's weakest ranking horizon. Per the
plan, classic-only remains the GW1 default; the LLM runs in shadow mode
unless a later run passes the gate.

Application-mode sweep (all with E3a deltas, same protocol):

| mode | actual total | vs classic |
|---|---|---|
| classic only | 1,058 | — |
| all fields | 1,000 | −58 |
| availability only | 1,058 | ±0 (decision-inert: optimizer's availability penalty only fires below P=0.65, minutes unused) |
| availability_scaled (points × P_llm/P_classic, clamped [0.6,1.4]) | 1,001 | −57 (6W/12L) |

Reading: the availability-calibration edge concentrates on doubtful players
the optimizer already avoids; among nailed starters the LLM's small deltas
are ordering noise. Better MAE ≠ better decisions — squad value needs rank
skill, which no current adapter has. Next chances: E4 (2× data + fixture
visibility, targeting ranking), and post-GW1 the decision-layer RL/GRPO
direction where the objective *is* decision quality.

Infrastructure: `src/fpl_ai/llm_adjust.py` (clipped delta lookup/application,
unit-tested), threaded through `run_rolling_squad_backtest` and the CLI.

## Decision-layer knob sweep (2026-07-09, CPU during E4 training)

`DecisionWeights` presets added to `decision.py` (`--decision-variant`);
`baseline` preset reproduces the 1,058 gate total exactly (refactor validated;
56/56 tests pass). Multi-window results (GW12-30 actual points):

| variant | 2025-26 | 2024-25 | 2023-24 |
|---|---|---|---|
| baseline | **1,058** | 1,261 | 1,056 |
| avail_soft (starter/captain points × min(1, P/0.80)) | 1,031 | **1,270** | **1,067** |
| horizon5 (5GW-blend transfer objective) | 996 | 1,241 | — |
| horizon5_avail | 1,042 | — | — |
| 2 transfers/wk, gain ≥ 1.0 | 995 | — | — |

Findings:

1. **horizon5 and 2-transfer variants are consistently worse** — reject. The
   3GW transfer objective + greedy 1-transfer policy is locally well-tuned.
2. **avail_soft is a wash across windows** (−27/+9/+11, mean −2) — the
   single gate window materially overstated its cost. Single-window
   comparisons of decision changes carry ~35-40 pts of season-total noise;
   all future decision-layer accept/reject calls use ≥3 windows.
3. **Key interaction result**: E3a availability deltas + avail_soft
   optimizer = **1,056** on 2025-26 — +25 over avail_soft with classic
   P(appear) (1,031), vs ±0 under the threshold optimizer. The LLM's
   availability calibration *is* decision-relevant once the optimizer
   consumes P(appear) continuously; it was the threshold penalty that made
   it inert. Still ties (−2) the tuned classic baseline, and multi-window
   validation of LLM variants needs 2023-25 eval-set generation (GPU,
   ~12 min/window — queue after E4 eval).

Design/spec for the next planning steps (multi-GW transfer lookahead,
congestion data, decision-layer GRPO): `docs/decision_layer_plan_2026_07_09.md`.

### Structural 2-week transfer lookahead (2026-07-09): rejected, informative

`--transfer-lookahead 2` (backtest.py): each week compares hold-and-bank vs
the top transfer options, valuing each action as immediate squad value +
0.9 × best next-week transfer gain (hold branch searches next week with the
banked 2-FT allowance). Two next-week projections tested, 3 windows each:

| projection | 2025-26 | 2024-25 | 2023-24 | banked wks |
|---|---|---|---|---|
| greedy baseline | 1,058 | 1,261 | 1,056 | — |
| schedule-rescaled 1GW | 1,002 | 1,255 | 1,055 | 7-9 |
| horizon_diff ((3GW−1GW)/2, model's own t+2 view) | 1,058 | 1,210 | 1,056 | 0-2 |

Reading: with a crude projection the lookahead banks often and loses; with
the model's own next-week estimate it (correctly) almost never banks and
collapses to greedy. **FT banking has ~zero option value under the current
forecast stack — greedy weekly transfers are near-optimal given what the
models know.** Planning depth is not the bottleneck; forecast/judgment
quality is. This sharpens the case that planning gains must come from
better inputs (per-week forecasts, congestion/rotation signals, LLM
judgment via GRPO) rather than deeper search over the same forecasts.

### Oracle lookahead test (2026-07-10, Wes's design): question CLOSED

`scripts/run_oracle_lookahead_test.py` (uses `--lookahead-projection oracle`
and the new `oracle_forecasts` diagnostic mode; deliberate label leakage,
diagnostic only). Two experiments, three windows each:

1. **Hybrid** (classic forecasts now, oracle *valuation* of next week):
   −53/−101/+41, mean **−38**. Banking driven by information the future
   executor won't have is actively harmful — value model and execution
   capability must match.
2. **Full oracle "actual space"** (all decisions on realized outcomes; the
   only difference is banking structure): greedy 1,796/2,024/1,731 vs
   lookahead **identical on all three windows, 0 banked weeks, delta +0.0**.

**Even with perfect information, banking a free transfer is never worth it
at 1 transfer/week — the structural option value is exactly zero.** The
lookahead direction is closed for good, independent of forecast quality.

Bonus quantification: oracle greedy (1,796) vs classic greedy (1,058) on
2025-26 = **+738 points/season of pure forecast-quality headroom, zero of
which is planning structure**. Every point the project can still win lives
in forecast/rank skill (and captaincy/chip judgment), which is exactly
where the LLM + GRPO sequence is aimed.

## E4 results (2026-07-10): best availability calibration; ranking still flat; gate FAILS

Training: 2,000 steps, 23.1h, final loss 0.182. Eval on the top-256 set
(4,864 rows), ladder comparison on the top-128 subset (classic column
reproduces the ladder exactly):

| metric (top-128 subset) | classic | E4 SFT | ladder best before |
|---|---|---|---|
| 1GW pts MAE | 2.575 | **2.423** | 2.429 (E3a) |
| 5GW pts RMSE | 9.186 | 8.931 | 8.887 (E2) |
| appearance-prob MAE | 0.205 | **0.161** | 0.169 (E3a) |
| Spearman 1GW | 0.165 | 0.166 | 0.160 (E3a) |
| top-11 1GW lift/wk | — | +0.32 | +1.53 (E2/E3a, n.s.) |
| top-11 5GW lift/wk | — | −5.8 | — |

E4 (2× data, pool-widened, fixture outlook) sets a new best on availability
calibration (0.161) and posts the first non-negative Spearman, but ranking
is still statistically flat and 5GW ordering is negative. **Pool widening +
fixture context did not unlock rank skill.**

Phase 3 gate re-run (2025-26 GW12-30, classic = 1,058):

| pipeline | actual | vs classic |
|---|---|---|
| E4 all fields, baseline optimizer | 1,020 | −38 (E3a was −58) |
| E4 availability_scaled, baseline optimizer | 992 | −66 |
| E4 availability + avail_soft optimizer | **1,056** | −2 (identical to E3a's 1,056) |

**Gate verdict unchanged: classic-only ships GW1; LLM in shadow mode.** The
avail_soft + LLM-availability configuration ties classic at 1,056 for both
E3a and E4 — the LLM availability signal reliably recovers the soft
optimizer's risk-aversion cost (+25 vs soft/classic-P) but does not beat
the tuned baseline. Squad value still hinges on rank skill no adapter has.

**Multi-window caveat (important)**: LLM variants cannot be validated on
2023-25 windows with these adapters — those seasons are in the training
data (in-sample). Genuine multi-window LLM validation requires a
chronological retrain (train through 2023-24 GW11, eval 2023-24 GW12-30),
~23h GPU per window. Decision for Wes: spend the GPU there, or accept
single-window evidence for GW1 and lean on the decision-layer GRPO plan.

## E5 launched (2026-07-10): congestion signal

E5 = E4 recipe + squad-rotation congestion block (UCL/UEL/UECL proximity +
post-break flags from corpus v4; `--include-congestion`). Labels
byte-identical to E4 → isolates the congestion signal. Max prompt 772
tokens (E4: 753), batch 2 × accum 8, ~23h. Dataset:
`reports/llm_residual_v2_e5_top256_congestion_thru_gw11_eval_gw12_30`.
Adapter: `artifacts/gemma4_e4b_lora_residual_v2_e5_top256_congestion`.
Hypothesis: rotation-risk context should sharpen the availability head
(already the LLM's strongest axis) and possibly minutes.

## E5 result (2026-07-11): congestion block is a NULL

E5 (= E4 + UCL/UEL/UECL proximity + post-break flags; labels byte-identical)
≈ E4 on every top-128 metric: appear MAE 0.162 (E4 0.161), 1GW MAE 2.427
(2.423), 5GW RMSE 8.910 (8.931), Spearman 0.158 (0.166), 100% strict JSON.
Usage diagnostic flat (mean |Δappear| 0.105 with congestion block vs 0.100
without) — the model does not visibly condition on it, mirroring the
article-packet null. Interpretation: whatever rotation signal survives the
label noise is already captured by the structured status/news + form
features; ~24% row coverage is too dilute to shift aggregates. The
congestion layer stays in the corpus (costless) and remains useful for the
decision layer/weekly report, but is not expected to carry forecast lift.
E6 (base-anatomy schema) launched immediately after — that hypothesis is
independent (it targets how the model *uses the baseline*, not new events).

## E6 result (2026-07-13): first significant ranking win; gate TIES classic

E6 = E5 data + base-anatomy schema (provenance, exact ridge decomposition,
role context, compact-context; 926 tokens max; batch 1 × accum 16, 30.6h,
final train loss 0.182). Eval: 4,864 rows (top-256), 100% strict JSON.

Full eval set, E6 SFT vs classic: 1GW MAE **2.151 vs 2.271**, 3GW 4.560 vs
4.659, 5GW 6.640 vs 6.856, minutes **22.85 vs 24.33** (first run to beat
classic on minutes), appear MAE **0.250 vs 0.308** (best ever). Top-128
subset: 1GW MAE 2.424 vs 2.575, appear 0.160 vs 0.205, Spearman 0.159 vs
0.165 (still a tie).

**Top-11 realized (1GW): 52.42/wk vs classic 49.47 — +2.95/wk, paired
per-week t = 2.41 (n = 19, p ≈ 0.03), 13W/4L/2T.** First statistically
significant selection-relevant win of the ladder (E4's +1.53/wk was
t = 0.69 n.s.). The lift is top-of-board picking, not global ordering
(Spearman ties); per-week diffs: worst −9 (GW24), best +17 (GW29).

Gate re-run (rolling GW12-30 squad backtest):

| config | actual total | ladder trend |
|---|---|---|
| classic only | 1,058 | — |
| E6 all fields, baseline opt | 1,035 | E3a 1,000 → E4 1,020 → **E6 1,035** |
| E6 availability_scaled | 1,000 | still harmful (E3a 1,001, E4 992) |
| **E6 availability + avail_soft** | **1,058** | **exact tie** (E3a/E4: 1,056) |

Reading: the availability edge now fully closes the gap under the soft
optimizer — first config to match classic's 1,058. The +2.95/wk top-11
lift does NOT convert in the gate because the optimizer's selection score
leans on 5GW, where E6 ties classic (top-11 5GW: 213.7 vs 214.7/wk); the
significant edge is concentrated in 1GW final points. Candidate lever: a
decision variant that up-weights 1GW when LLM deltas are applied — but
per the standing rule this needs ≥3 windows, i.e. the chrono-2425 retrain
first (2025-26-only evidence is a single window). G1 GRPO may also learn
this re-weighting itself (captain + lineup use 1GW).

## E7-scout result (2026-07-18): FIRST GATE WIN — all-fields 1,069 vs classic 1,058

E7 = E6 schema + scout evidence (corpus v7: PL Scout + Sky tips,
--prefer-scout, 2 docs × 260 chars; 84% train-row coverage vs 24% for the
old null article packets). Seq 1536 + grad ckpt, 48h, 100% strict JSON.

Forecast metrics ≈ E6 (1GW MAE 2.154, avail 0.249, minutes 22.9), except:
best-ever 5GW MAE **6.613** (E6 6.640, classic 6.856) and Spearman-1GW
0.2703 exactly ties classic (0.2705). **E6's significant top-11 lift did
NOT replicate: +0.79/wk, t = 0.37 (E6: +2.95, t = 2.41)** — that metric is
fragile across adapters.

Gate (2025-26 GW12-30):

| config | actual | ladder trend |
|---|---|---|
| **all fields, baseline opt** | **1,069 (+11 vs classic)** | 1,000 → 1,020 → 1,035 → **1,069** |
| availability_scaled | 1,027 | best ever, still below |
| availability + avail_soft | 1,058 | tie (= E6) |

Reading: the win came through 5GW ordering — the optimizer's selection
score leans on 5GW, where E7 is the ladder's best. Scout evidence converts
at the decision layer, not in weekly showcase metrics.

**Caveat (honest validation): +11 is a single window inside the ±40 noise
band; ship decisions need ≥3 windows and 2023-25 is in-sample for this
adapter.** → **E7-chrono-2425 launched 2026-07-18** (identical recipe,
train through 2024-25 GW11 = 22,272 rows, eval/gate on 2024-25 GW12-30;
1,392 steps ≈ 36h, `scripts/run_gemma_e4b_residual_e7chrono2425.sh`).
If the all-fields config also beats classic on 2024-25, that's 2/2
held-out windows and E7 becomes the GW1 ship candidate.

## Protocol caveat noted 2026-07-19: label lookahead at the cutoff

Cutoff-week training rows carry 3GW/5GW labels, so every "train through
GW11, eval GW12-30" adapter has seen GW12-15 outcomes in label form. All
rungs E0→E7 (and the chrono runs) share this identically → rung-vs-rung
and LLM-vs-classic comparisons remain fair, but absolute margins on
GW12-15 specifically are slightly flattered. Post-GW1 tightening: trim
3GW/5GW label components within 5 weeks of the cutoff, or start the gate
at GW16. (Surfaced during the G2 deployment-regime discussion with Wes —
see docs/decision_layer_plan_2026_07_09.md §6.)

## E8-podcast result (2026-07-29): NEGATIVE — podcast evidence hurts, E7 stays champion

E8 = E7 recipe (corpus v7 evidence + `--prefer-scout`, 2 docs × 260 chars,
same seq-1536/lr/batch hyperparams) + one added evidence source: Whisper
large-v3 transcripts of 79 Sky Sports Fantasy Podcast episodes, attached
alongside all 8 files v7 already used (mention-centered truncation window
fixed pre-launch so long transcripts don't get prefix-cut before the
player's actual mention — see [[fpl-e8-podcast-evidence]]). Corpus v8
coverage 84.4% (26,998/32,000), a hair above v7's 84.3% — a clean
single-variable ablation. Trained 2,000 steps / 50.7h, 100% strict JSON,
final train_loss 0.1842.

Eval-set error metrics looked *better* than both base and classic ML:
5GW points MAE 6.609 (classic 6.856, base 6.744), appearance-probability
MAE 0.244 (classic 0.308, base 0.323). But `ranking_lift` (top-11 realized
points if squad were picked from this signal alone) was already negative
vs classic on this eval slice (−8.79 pts/wk on 5GW, −0.53 on 1GW) — the
red flag that played out at the gate:

| config | E8 actual | E7 (1,069) | classic (1,058) |
|---|---|---|---|
| all fields, baseline opt | **1,025** | −44 | −33 |
| availability_scaled, baseline opt | **1,002** | −67 | −56 |
| availability + avail_soft | **1,060** | −9 | +2 |

**E8 underperforms E7 in all three configs, and underperforms classic ML
in two of three.** Better per-row error metrics did not translate to
better squad-selection decisions — exactly the gap the ranking_lift flag
warned about. Likely cause (from the independent article-quality review,
[[fpl-e8-podcast-evidence]]): podcast transcripts are noisier evidence
than scout/Guardian text (Whisper mis-hearings, ~16% chunk-duplication
artifacts, and even mention-centered windowing only samples one moment of
a long meandering conversation vs. a dense written article) — plausibly
teaching the adapter to react to noise.

**Verdict: do not ship E8. E7 (1,069) remains the standing forecast-layer
champion.** Recorded as a negative result, not pursued further — no
transcription of the larger Sky Sports Premier League Podcast planned.
Next GPU-track lever: G2-v3 (season-level chip-budget bug fix), built on
E7's deployment-regime states, not E8's.

## E9-cleansplit result (2026-08-02): BIGGEST WIN YET — clean train/test split, zero same-season leakage

Wes's idea (2026-07-30): since 2026-27 launches in ~3 weeks with zero
same-season data (same condition every future season faces at GW1), test
whether training purely on complete prior seasons and evaluating on all
of the next season is both more realistic and still works. E9 = E7's
exact recipe (corpus v7_scout, `--prefer-scout`, same hyperparameters)
with `--train-through 2024-25:38` (zero 2025-26 rows, was `2025-26:11`)
and `--eval-weeks 2025-26:2-30` (was `2025-26:12-30`) — eval set grows
from 4,864 to **7,424 rows** (53% bigger). Gate window widened to match
(`--start-week 2 --end-week 30`, was `12`/`30`); the classic-only anchor
was rebuilt on this same wider window for a fair comparison (1,471, not
the old GW12-30-only 1,058).

Trained 1,824 steps / 45.9h, 100% strict JSON, final train_loss 0.1871.

| config | E9 actual | vs classic-only (1,471, same window) |
|---|---|---|
| **all fields, baseline opt** | **1,553** | **+82** |
| availability_scaled, baseline opt | 1,414 | −57 |
| **availability + avail_soft** | **1,549** | **+78** |

Both winning configs beat classic by a much wider margin than E7's +11 —
and on a genuinely clean, zero-leakage test that matches the real 2026-27
deployment condition exactly. 5GW MAE 6.68 (classic 6.86), appearance MAE
0.241 (classic 0.302).

**DefCon check (Wes's question)**: 2025-26 is the first season with
Defensive Contribution bonus scoring; 2022-24 data has zero
tackles/clearances/interceptions/recoveries columns (verified — not in
this project's data at all, not just unused). Tested whether the SFT
adapter could pick up the DefCon pattern purely from evidence text despite
never training on it: **no** — on the 962/7,424 (13%) player-weeks where a
player actually hit the bonus threshold, SFT MAE (2.892) is *worse* than
classic (2.593); on the other 87% SFT improves classic by +0.19 MAE, which
is what carries the overall positive gate. Contained, not disqualifying.
Full detail: [[fpl-defcon-gap]] in memory.

**Verdict: E9 is the strong ship candidate for GW1 2026-27.** Before
actual launch, retrain through 2025-26 inclusive (not `2024-25:38`) so the
LLM adapter gets real DefCon-era training data, not just the classic
baseline's in-season walk-forward absorption of it.

## Sequence (approved by Wes 2026-07-08)

1. **E3a** (done — see verdict above): 2 docs × 450 chars; batch 1 ×
   accum 16 + grad ckpt (batch 2 OOMs at this prompt length, even with grad
   ckpt — the peft target_parameters path appears to defeat activation
   recomputation).
2. If text moves the needle → **rationale-augmented SFT** (teacher-annotated
   risk flags/reasons per evidence packet) + podcast transcript season runs.
3. Regardless → **widen player pool** (top-128 → top-256 or all-eligible;
   corpus already holds 106,699 rows) for one more forecast run.
4. **Phase 3 optimizer** with multi-GW lookahead + **fixture context in
   prompts** (launch-critical; prompts currently carry zero schedule info).
5. **Strategy corpus** collection in parallel (CPU-only).
6. Post-GW1 research: **GRPO at the decision layer** (backtest = reward;
   TRL 1.0 in venv), one-shot 12B scale check. LoRA stays the FT approach —
   capacity is not the bottleneck (train loss 0.16; label noise is).
