# Decision Layer: Planning Intelligence + RL Design — 2026-07-09

Written during the E4 training window (CPU-only work). Companion to
`docs/experiment_log_e4b_residual_2026_07.md` and the approved sequence
(memory: fpl-approved-sequence-2026-07-08). Covers: (1) audit of the current
optimizer, (2) empirical sweep of decision knobs, (3) planning-intelligence
roadmap (fixture lookahead, cup/Euro/international congestion), (4) the GRPO
decision-layer RL spec for post-GW1.

## 1. Current-state audit

Hard constraints are already handled correctly and stay in the exact optimizer
(per the agreed planning split — LLM parameterizes, never overrides):

- **Budget**: buy at `price`, sell at `sell_price`, bank tracked;
  initial-squad beam search prunes with a minimum-remaining-cost bound.
- **3-per-team**: enforced in `_is_legal_squad` and during beam expansion.
- **Position quotas / formations**: 2-5-5-3 squad, legal starting formations
  enumerated; autosubs respect formation validity.
- **Transfers**: FT banking to 2, −4 hits, `--max-transfers-per-week`,
  `--min-projected-gain`.
- **Chips**: bench boost + triple captain scheduled by an explicit
  remaining-season DP over estimated future chip values.

The gaps are **objectives and lookahead**, not legality:

- Transfer evaluation (`_evaluate_squad`) = starter 3GW sum + captain 1GW +
  small bench weights − threshold availability penalty (only fires < P=0.6).
  Minutes unused; P(appear) decision-inert above the threshold.
- No structural fixture lookahead in transfers: the 3GW/5GW forecast horizons
  embed schedule implicitly, but the optimizer never reasons about *which*
  future week is good (fixture swings, upcoming blanks/DGWs) except in the
  chip DP.
- Transfer policy is greedy (any positive projected gain fires).
- Captain = max predicted 1GW points, ignoring appearance risk.
- Labels are **unconditional** (`label_points_1gw = observed_points`, zero if
  benched), so predicted points already average over appearance —
  multiplying by P(appear) again double-counts availability. Any availability
  reweighting is a deliberate risk-aversion choice, not a calibration fix.

## 2. Decision-knob sweep (2026-07-09, GW12-30 2025-26 gate window)

`DecisionWeights` presets added (`decision.py`, `--decision-variant`), all
unit tests pass, and the `baseline` preset reproduces the classic gate total
exactly (validates the refactor).

| variant | actual points | vs baseline |
|---|---|---|
| baseline (3GW horizon, threshold penalty) | **1,058** | — |
| horizon5_avail (blend5 + soft availability) | 1,042 | −16 |
| avail_soft (soft availability weight, knee 0.80) | 1,031 | −27 |
| horizon5 (5GW+0.6·3GW+0.35·1GW transfer objective) | 996 | −62 |
| 2 transfers/wk allowed, gain ≥ 1.0 | 995 | −63 |

**Reading**: every hand-turned knob hurt on this window. The tuned baseline
is locally strong, and single-window comparisons carry huge variance (weekly
sd ~8-9 pts → season-total sd ~35-40). Two consequences:

1. Decision-layer changes must be evaluated on **multiple windows**
   (2024-25 and 2023-24 backtests) before accept/reject. A 2024-25 GW12-30
   validation run of the top variants is in flight.
2. Hand-tuning scoring weights on one trajectory is precisely the failure
   mode **GRPO at the decision layer** avoids: it optimizes expected reward
   across many sampled windows/rollouts instead of one realized path. The
   `DecisionWeights` knobs built today are the first draft of the RL action
   space.

## 3. Planning-intelligence roadmap

### 3a. Multi-window evaluation harness (prereq, CPU, cheap)

Any decision change gets scored on ≥3 windows: 2025-26 GW12-30,
2024-25 GW12-30, 2023-24 GW12-30 (plus GW20-38 variants later). Accept only
if mean lift > 0 and no window is catastrophic. This is also the RL eval
protocol (train on 2 seasons' windows, hold out the third).

### 3b. Structural multi-GW transfer lookahead

Replace horizon blends with explicit planning over the *known* schedule:

- For each candidate transfer, simulate the squad over the next H=3 weeks
  using per-week forecasts scaled by known future fixture context
  (`fixture_count`, difficulty, venue — the machinery already exists in
  `_estimated_future_forecasts_for_current_squad`), including the option to
  bank the FT this week and make a 2-transfer move next week.
- This is a small tree (this-week action × next-week action), not a full DP;
  ~10× current transfer-eval cost, still trivially CPU-feasible.
- Catches: fixture swings ("bring him in one week early/late"), pre-blank
  planning, pre-DGW loading — the things Wes flagged that greedy 1-week
  search cannot see.

### 3c. Congestion / duty signals (Euro, domestic cups, internationals)

FPL's own API only covers PL fixtures, so rotation pressure from other
competitions is invisible to the model today. Plan:

- **Data** (spiked 2026-07-09): per-team all-competition fixture calendar.
  - **UCL / UEL / UECL**: `fixturedownload.com/feed/json/{champions-league,europa-league,conference-league}-2025`
    — verified working (needs a browser User-Agent; plain curl UA gets 403),
    kickoff-level UTC dates, English club names present (Arsenal, Villa,
    Forest, …). Backup: `openfootball/champions-league` repo (Football.TXT).
  - **football-data.org free tier**: PL + UCL only — no UEL/FA Cup/EFL Cup.
  - **FA Cup / EFL Cup**: no free structured feed found; encode round dates
    as season constants and infer participation from progression (or FBref
    scrape later). Lower priority — European midweeks are the dominant
    rotation driver.
  - **International windows**: fixed FIFA calendar — season constants.
- **Features** (classic ML + LLM prompt fields, timestamp-safe):
  - `team_fixtures_last_14d` / `next_14d` (all competitions) — congestion.
  - `midweek_cup_before_gw` / `after_gw` flags — classic rotation spots
    ("manager rests starters before a UCL knockout").
  - `first_gw_after_international_break` + player-level
    `likely_international` (from nationality + squad history) — travel/
    fatigue/late-return risk.
- **Consumption**: (i) features for the classic minutes/appearance models,
  (ii) prompt fields so the LLM's rotation-risk judgment (already the plan
  for optimizer parameterization) has grounding, (iii) a rotation-risk
  multiplier the optimizer applies to P(appear) for cup-congested weeks.
- Effort: data plumbing is the bulk; start with 2025-26 + 2026-27 only
  (historical backfill for backtests can follow).

### 3d. Chip coverage gaps

✅ Built (2026-07-09): `--simulate-wildcard` / `--simulate-free-hit`
(backtest.py). Wildcard = mid-season full rebuild via `build_initial_squad`
with bank + sell value, played when the squad-value gain clears
`--wildcard-min-gain` (default 12); Free Hit = one-week rebuild that
reverts, gated on the one-week lineup gain (`--free-hit-min-gain`,
default 10). One chip per week (overrides the BB/TC DP that week). Both
mechanisms verified: wildcard spends the bank correctly; the free-hit
squad reverts exactly next week. **Default off** — all gate numbers remain
comparable; threshold-rule play is a heuristic, and chip *timing* is a
natural GRPO action (§4). Not yet swept for point gains — do that
alongside the E4 gate re-runs if useful, or leave to the RL layer.

## 4. GRPO at the decision layer (post-GW1)

**Environment**: `run_rolling_squad_backtest` — already deterministic,
CPU-cheap per week, and validated against the gate. One episode = one season
window; weekly steps.

**Policy**: Gemma-4-E4B + LoRA (the forecast adapter stays frozen; a separate
decision adapter). Input prompt = weekly decision state: squad, bank, FTs,
chips left, top-N candidate forecasts, fixture outlook, congestion flags.
Output = **bounded structured JSON**, never free-form squad picks:

```json
{
  "transfer_aggressiveness": 0.0-2.0,     // scales min_projected_gain
  "bank_transfer": true/false,            // explicit FT-banking action
  "captain_pick": <id from top-5 list>,
  "chip_play": "none|bench_boost|triple_captain",
  "player_risk_multipliers": {"<id>": 0.6-1.4, ...}  // ≤5 players
}
```

The exact optimizer consumes these (legality preserved by construction —
same principle as the residual-delta forecast design, and same reward-hacking
guard: bounded, clipped, optimizer-final).

**Reward**: weekly realized points minus the classic-baseline optimizer's
realized points on the same week/state (paired baseline kills most of the
week-to-week noise — this matters because weekly sd ~8-9 pts vs expected
policy edge ~0.5-1 pt/wk). Episode-level bonus (season total vs classic) at
low weight for long-horizon credit (chips, banking).

**GRPO mechanics**: for each weekly state, sample G=8 responses (temperature
~0.8), roll each through the optimizer + realized scoring, group-normalize
advantages. Weekly-bandit formulation first (each week an independent group,
squad state advanced by the greedy/baseline action); full sequential rollout
only if the bandit version shows signal. TRL 1.0 GRPOTrainer is already in
the venv; generation is the GPU cost — ~2,300 states (4 seasons × ~29 wks ×
G=8 with ~700-token prompts, 60-token responses) ≈ well within a few GPU-days
on the GB10 with batched generation.

**Evaluation**: held-out season window (train 2022-25 windows, eval 2025-26
GW12-30 vs the 1,058 gate). Success = beats classic on held-out window mean
across ≥3 windows.

**Why RL here and not at the forecast layer** (recap of the locked decision):
forecast rewards are noise-dominated per sample; decision rewards aggregate
11+ players per week and can be baselined against the classic optimizer,
and the objective *is* the thing we ship.

## 5. Immediate next steps (this window)

1. ✅ `DecisionWeights` + `--decision-variant` (action-space scaffolding).
2. ✅ Multi-window validation: horizon5 & 2-transfer rejected (worse on all
   windows); avail_soft a wash (−27/+9/+11) — results in the experiment log.
3. ✅ E3a `availability` deltas + `avail_soft` optimizer: 1,056 on 2025-26 —
   **+25 over avail_soft/classic-P (1,031)**, proving the LLM availability
   signal is decision-relevant once the optimizer consumes P(appear)
   continuously (it was inert under the threshold penalty). Ties classic
   baseline (−2). To validate multi-window, generate 2024-25/2023-24
   GW12-30 eval sets + adapter predictions (GPU, ~12 min/window) after the
   E4 eval — if avail_soft+LLM beats baseline on 2/3 windows, it becomes
   the shipping configuration.
4. ✅ Congestion data spike (§3c) — UCL/UEL/UECL feeds verified; domestic
   cups deferred to round-date constants.
   ✅ **Built** (2026-07-09): `scripts/fetch_competition_fixtures.py`
   (1,594 matches, UCL/UEL 2022-25 + UECL 2024-25) →
   `data/competition_fixtures/european_fixtures.jsonl`;
   `scripts/attach_congestion_to_corpus.py` → corpus
   `..._v4_congestion.jsonl` (106,699 rows; 15,508 euro-flagged, 12,547
   post-break; flags validated against 2025-26 UCL matchdays and intl
   breaks); builder `--include-congestion` renders a compact
   squad-rotation block (~25% of top-128 rows, ~40 tokens). Ready for the
   next LoRA run (E5 candidate: E4 recipe + congestion).
5. ✅ Structural 2-week transfer lookahead (§3b): implemented
   (`--transfer-lookahead 2`, `--lookahead-projection`), **rejected on 3
   windows with both projections** (results in experiment log). Key
   learning: with the model's own next-week estimate the lookahead
   collapses to greedy — FT banking has ~zero option value under current
   forecasts. Planning depth is not the bottleneck; forecast/judgment
   quality is. §3b's machinery (action-vs-hold valuation, future
   projection) is reusable as the GRPO environment's action evaluator.
6. E4 eval + gate re-run when training completes (per
   `docs/session_state_2026_07_09.md`) — takes priority when the GPU frees.

## 6. G2: plan-horizon GRPO in the deployment regime (2026-07-18/19, Wes)

G1 verdict (2026-07-15): +7 total on held-out 2025-26 (7W/5L/7T) —
marginal; the weekly-bandit construct caps RL's multi-step upside (Wes's
read, confirmed by flat training rewards). G2 supersedes it.

**Formulation** (TRL is single-turn → no interactive weekly rollouts): the
policy emits a K-week PLAN — one JSON array of bounded weekly actions
(§4's knobs + `bank_transfer` + `chip_play`: bench_boost/triple_captain,
each once per window) — and `PlanEpisodeEnv` rolls it through K chained
weekly states with squad/bank/FTs evolving under the policy's own choices.
Reward = cumulative realized − the all-defaults plan's cumulative on the
same window (paired sequential baseline). Chips, FT banking, and transfer
sequencing — exactly what the bandit couldn't express — are now the action
space. Code: `src/fpl_ai/grpo_plan_env.py`, `train_gemma_grpo_plan.py`,
eval `scripts/run_grpo_plan_eval.py`.

**Deployment-regime training data (Wes's requirement)**: at a live GW x the
policy will see text-adjusted forecasts, so it must train on them. Leak-free
via chronological stand-in adapters (the classic suite's rolling-refit
discipline, applied at season granularity because an LLM refit costs
~20-36h — per-week rolling would be ~2 GPU-months; acceptable because the
adapter learns the slowly-changing article→delta skill, not current facts;
E7 won the gate 19 weeks stale):

| states | legal adjuster (cutoff) |
|---|---|
| 2024-25 GW12-38 | chrono-2425 (24-25 GW11) |
| 2025-26 GW2-11 | chrono-2425 |
| 2023-24 GW12-38 | chrono-2324 (23-24 GW11) |
| 2024-25 GW2-11 | chrono-2324 |
| 2025-26 GW12-30 (held-out gate) | E7 (25-26 GW11) |
| 2022-23, 2023-24 GW2-11 | none — classic-only or dropped |

Evidence snippets (pre-deadline articles) are timestamp-safe for ALL weeks;
only adapter deltas need the legality map.

**Two-model learning ledger** (the invariant that keeps this honest): the
forecast adapter never trains on a week it adjusts — at that week it runs
inference only, exactly like a live adapter. The week's OUTCOME teaches
only the layer above (it scores G2's sampled plans). Facts flow downward at
inference; outcomes teach upward only.

**Text→decision channel** (Wes: the scalar delta alone is not enough):
state rows carry adjusted numbers + Δ1gw + a per-player scout snippet
(default: base-model LLM condensation, greedy + disk-cached =
deterministic; mention-centered window as fallback). Ablation v2b: policy
init from E7 LoRA (caveat: TRL's KL reference is the adapter-disabled base,
partially washing out the init). Post-GW1: rationale-augmented forecast
SFT; full-article ~10k-token plan prompts (fine at inference, ~6× GRPO
training cost).

**Label-lookahead caveat (applies to the whole E-ladder)**: cutoff-week
rows carry 3GW/5GW labels → a "through GW11" adapter has seen GW12-15
outcomes in label form; the first ~4 gate weeks are slightly flattered.
Shared identically by every rung, so rung-vs-rung comparisons are fair;
treat absolute GW12-15 margins as soft. Post-GW1 tightening: trim
long-horizon labels near the cutoff or start the gate at GW16.
