# RL on the Forecast Layer (G4) — Design

**Status**: draft for Wes, 2026-09-04. **Author**: Claude. **Decision needed**: go / no-go on a 1-season pilot (GPU idle now).

## 1. Problem and hypothesis

The residual adapter (E11-full) is trained with an MAE objective over all
player-weeks. Decisions are won on ~2% of those rows — premiums, captaincy
targets, DefCon weeks, cold starts — and the ledger shows the adapter is
*worst* exactly there (premium band 3.45 predicted vs 5.64 realized; it
shrinks Haaland like a one-week wonder). Every input-side change (podcasts,
digests, market line, DefCon numbers) measured null because none changed
what the adapter is rewarded for.

**Hypothesis**: fine-tuning the same adapter with a *decision-value* reward
— realized points of the squad the decision layer picks from its
forecasts — moves its deltas where MAE cannot, without breaking the
bounded-residual discipline that makes it stable.

This is RL on a **new environment** (the forecast layer), not more scale
on the saturated plan-policy env (G2/G3: three flat results).

## 2. Environment

**State** `s = (season, week)`: an entry from the chrono-legal adjusted
state caches (`reports/grpo_states_adjusted/*.jsonl`): the classic
trajectory's squad, bank, free transfers, all 752 classic forecasts, and
realized `actual_points` / `actual_minutes`. Prompts for any (state,
player) come from the E11 corpus via the split builder's own prompt
function (schema identical to training).

**Policy** π_θ: Gemma-4-E4B + LoRA, initialized from **E11 (thru-34)**.
Input = the E11 prompt for player p in state s; output = the strict-JSON
delta object (same bounds, same parser). *The policy is the forecaster.*

**Decision function** D (fixed, deterministic — not learned): apply deltas
→ `recommend_actions` (take the best 1-transfer if projected gain > 0) →
`_optimize_lineup` (XI, captain, bench). Default `DecisionWeights`.

**Reward, per-player marginal (fits TRL's per-prompt groups)**: for player
p in state s, sample G completions. For each completion c, build forecasts
F_c = reference forecasts (E11 deltas for everyone else) with p's delta
replaced by c. Reward

    R(s, p, c) = realized_points( D(F_c) )   − hit cost, autosubs applied

Group-relative advantage A = R − mean_G(R). Players far from any decision
boundary get identical rewards across the group → zero advantage → no
gradient (correct: the objective focuses on boundary players). To spend
generation where it matters, **restrict prompts per state to the
decision-relevant set**: current squad ∪ recommender incoming pool ∪
captain candidates (~40–60 players), not all 752.

Format reward: −1 for unparseable JSON (E11 starts at 100% strict, so this
is a guardrail, not a signal). Bounds enforced by the parser as in SFT.

## 3. Training

- Trainer: TRL `GRPOTrainer` (existing `train_gemma_grpo.py` pattern; rows
  = `{prompt, state_key, player_id}`; reward closure looks up the state).
- Init: E11 adapter (thru 2025-26:34). Reference for KL = same E11 weights
  (β ≈ 0.04, G2 setting). This is what keeps deltas *residual* — RL nudges
  E11, it cannot wander to free-form outputs.
- G = 4 generations/prompt, temperature 0.8, `max_completion_length` 96,
  `min_new_tokens` 8 (empty-EOS attractor lesson from G2).
- Per step: one state × its ~50 relevant players × G = ~200 completions
  (~25 min generation-bound on the GB10). One epoch over the training
  states ≈ 60 states ≈ 1 day.

## 4. Data and chrono-legality

- **Train states**: 2023-24 + 2024-25 adjusted caches (all weeks with
  realized outcomes). Optionally 2025-26 GW1–11 (`2025-26-early`).
- **Held-out decision eval**: 2025-26 GW12–30 (`2025-26.jsonl`, 19 states)
  — the G2 eval windows; E11 saw those rows in SFT but the RL phase does
  not, so E11 vs E11+RL is a fair comparison of the *RL* effect.
- **Held-out MAE eval**: 2025-26 GW35–38 (E11's 1,024-row holdout).
- Everything reads timestamp-safe caches; no live data enters training.

## 5. Evaluation and gates (all must pass to ship)

1. **Decision value**: realized points of harness-drafted squads with
   RL deltas vs E11 deltas over the 2025-26 GW12–30 windows (existing
   `run_grpo_decision_eval.py` / two-model ledger). Gate: **wins ≥ 3 of 6
   windows and net positive**, same bar as G2.
2. **MAE non-regression**: 1gw MAE on GW35–38 within **+0.05** of E11
   (2.060). RL may trade a little MAE for decision value, but not
   collapse the forecaster.
3. **Strict JSON ≥ 99%**; delta magnitude distribution within E11's family
   (mean |Δ1gw| 0.3–0.6 on eval rows).
4. **Premium slice**: the +adapter premium-band gap must not get worse
   than E11's (−2.19); improvement here is the whole point.
5. Then the standing rule: the weekly ledger arbitrates in production;
   freeze-back to E11-full on two losing weeks.

## 6. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Reward noise (squad points sd ≈ 15/week) | group-relative advantage; G=4; ~60 states × ~50 players; verdict on ≥3 windows, never one |
| Reward hacking (inflate everyone) | per-player *marginal* reward: inflating p only helps if p's inclusion actually scores; KL to E11 |
| Empty / malformed completions | min_new_tokens 8; format reward −1; parser bounds |
| MAE collapse | gate 2; KL β; init from E11 |
| Compute | generation-bound ~1 day/epoch; pilot = 1 epoch; no other GPU job during (oom rule) |
| Off-regime early season | train states span GW2–38 across two seasons; eval includes early states if 2025-26-early is held out instead |

## 7. Pilot plan and cost

- **Phase 0 (CPU, today)**: `grpo_forecast_env.py` (state loading, prompt
  build for relevant players, reward = decision realized points), unit
  test: reward on cached E11 deltas reproduces the ledger's adjusted
  totals; smoke a dozen prompts end-to-end.
- **Phase 1 (GPU, ~1 day)**: 1 epoch GRPO from E11 on 2023-24 + 2024-25
  states → adapter `g4_forecast_v1`.
- **Phase 2 (GPU, ~5 h)**: gates 1–4. Verdict ~48 h after go.
- Cost: ~30 GPU-hours; blocks no GW work (GW3 ingestion is CPU; next
  live decode is Thursday).

## 8. Decisions for Wes

1. Go / no-go on the pilot.
2. Reward variant: absolute realized points (proposed) vs realized minus
   classic-trajectory baseline (same gradient, lower variance; can switch
   for free — I'll log both).
3. Include 2025-26 GW1–11 in training (more states, early-season regime)
   or hold it out as a second eval window (my preference: hold out).
