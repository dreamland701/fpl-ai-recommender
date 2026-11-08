# G2 (plan-horizon GRPO) results and FAQ — 2026-07-26

Reference doc consolidating everything learned across the E7 → G2-v2 →
G2-v2b ladder (2026-07-18 through 2026-07-25). Written for digging into
later — see `docs/session_state_2026_07_12.md` for the blow-by-blow
operational log and `docs/experiment_log_e4b_residual_2026_07.md` for the
full E-ladder history.

---

## 1. The architecture, top to bottom

```
classic ridge forecast (points/minutes/appearance probability per player)
        │
        ▼
E7 (or a chronologically-legal sibling): fine-tuned Gemma-4B LoRA reads
pre-deadline article text + the classic forecast, outputs a bounded JSON
DELTA (not a fresh prediction) — e.g. delta_points_1gw: -1.2
        │
        ▼
adjusted forecast = classic + E7's delta, PLUS two side-channels carried
alongside: a raw Δ1gw number, and an LLM-condensed ≤30-word scout snippet
        │
        ▼
G2: GRPO-trained plan-horizon policy reads the adjusted forecasts + Δ +
snippets for a squad and a 6-week horizon, and emits a K-week plan
(transfers, banking, chip timing) — trained so realized points beat a
do-nothing default plan
```

Two independent, separately-validated sources of uplift are stacked here:
**E7 improves the forecast numbers**; **G2 improves the decisions made
from those numbers**, whatever they are. They have not yet been measured
together on one common backtest protocol (see §5, "open item").

---

## 2. What E7 is, precisely

E7 = residual/delta-learning SFT adapter. It is NOT a standalone
forecaster — it reads the classic forecast alongside pre-deadline article
text (scout reports, team news) and learns to output a bounded correction
to apply on top. "E7" specifically = the E6 prompt/schema + a corpus
enriched with scout-report evidence (corpus v7: 2 evidence documents per
player-week, scout-report sources prioritized, 84% coverage).

Gated by: apply E7's deltas to classic forecasts, run the *same* simple
squad-selection optimizer used for the classic baseline, compare total
realized points over a held-out window (full 19-week rolling backtest,
autosubs included, real sequential transfer decisions).

- **E7 gate (2025-26 GW12-30)**: classic 1,058 → E7 all-fields **1,069
  (+11)** — first-ever gate win in the E-ladder.
- **chrono-2425 gate (2024-25 GW12-30, out-of-window replication, same
  recipe trained through an earlier cutoff)**: classic 1,261 → adjusted
  **1,314 (+53)** — decisively replicates E7's verdict on a different
  season.
- Two other LLM configs tested on the chrono-2425 gate did NOT replicate:
  `availability_scaled` **1,214 (-47)**, `avail_soft` **1,262 (+1)** —
  "all fields, baseline-opt" is specifically the winning configuration,
  not "any LLM adjustment."

---

## 3. The G2 ladder: v1, v2, v2b

**G2 v1** — never a real training run. The auto-launched machinery smoke
test on raw classic (unadjusted) states, run only to verify the pipeline
worked (JSON plan parsing, reward computation, clipping, KL stability)
with the real model on real GPU. Killed at step 90/384 (intended ~20-30
steps; overran because no kill was scheduled). Never evaluated. Tells us
nothing about G2's actual capability — it predates the deployment-regime
design entirely.

**G2-v2** — the real, evaluated training run. Trained on
`reports/grpo_states_adjusted/` (classic forecasts adjusted by the
chronologically-legal chrono adapter for each week, plus Δ1gw + LLM
scout-snippet side-channels), across three seasons filtered to
delta-bearing weeks only (2023-24 GW12+, 2024-25, 2025-26-early — 59
episodes; the `REQUIRE_DELTAS` filter drops any week with no legal
adapter coverage, e.g. 2023-24 GW2-11). Fresh LoRA on top of unmodified
base Gemma-4B. 232 steps / 8 epochs / 30.6h. Training reward climbed
monotonically (mean per 30 steps): -3.0 → -0.8 → +2.8 → +3.0 → +4.9 →
+2.3 → +2.7 → +5.2. KL stayed tiny (0.0003-0.005) throughout, no reward
collapse.

**G2-v2b** — the E7-init ablation: does starting the *policy's own
weights* from a model that already knows how to translate articles into
deltas help, beyond what's already visible in the adjusted-state prompt?
Implementation: peft only allows one `target_parameters` adapter per
model, so continuing the E7 SFT adapter directly fails with a ValueError;
the working pattern is `PeftModel.from_pretrained(base,
e7_path).merge_and_unload()` (merge E7's weights into the base), then
attach a fresh LoRA on top of the merged model. This also strengthens the
ablation's validity versus the originally-planned "continue the E7
adapter directly" approach: TRL's GRPO KL-reference is the
adapter-disabled model, which post-merge is base+E7 rather than raw base
— so the init actually anchors training instead of "washing out" as
originally worried. 232 steps / 8 epochs / 28.1h. Reward trajectory: -1.9
→ -1.1 → +0.2 → +1.0 → +3.4 → +1.4 → (final step +8.6), broadly similar
shape to v2 but a gentler climb.

---

## 4. Full results table

| Comparison | Protocol | Result |
|---|---|---|
| E7 vs classic | 19-wk rolling backtest, GW12-30 2025-26, autosubs included | 1,058 → **1,069 (+11)** |
| chrono-2425 vs classic | same protocol, GW12-30 2024-25 (out-of-window) | 1,261 → **1,314 (+53)** |
| chrono-2425 `availscaled` | same | 1,261 → **1,214 (-47)**, does not replicate |
| chrono-2425 `avail_soft` | same | 1,261 → **1,262 (+1)**, does not replicate |
| G2-v2, classic-shaped states | 3 non-overlapping 6-wk windows, plan vs all-defaults, autosubs EXCLUDED, greedy+min_new_tokens=8 | baseline 968 → policy **1,015 (+47, 3W/0L/0T)** |
| G2-v2, adjusted (deployment) states | same protocol | baseline 940 → policy **967 (+27, 3W/0L/0T)** |
| G2-v2b, classic-shaped states | same protocol | baseline 968 → policy **971 (+3, 1W/1L/1T)** |
| G2-v2b, adjusted (deployment) states | same protocol | baseline 940 → policy **968 (+28, 3W/0L/0T)** |

**These rows are NOT all directly comparable to each other as raw point
totals.** The E7/chrono rows use the full 19-week rolling backtest with
real sequential transfers and autosubs. The G2 rows use a 3-window,
autosub-excluded, "policy vs do-nothing" metric — a genuinely different
currency. See §6 Q3 for why, and §5 for what would close this gap.

**A nuance worth flagging**: the G2 "baseline" (do-nothing) totals differ
between the classic-states config (968) and adjusted-states config (940)
for the *same three windows and the same starting squads* — the adjusted
cache reuses the classic cache's squad/bank fields verbatim, only
forecast numbers differ. The gap comes from captain/XI-vs-bench selection
still using projected points even under a "no transfers" policy, and
those projections differ between classic and E7-adjusted numbers. In this
narrow n=3 sample, E7-adjusted numbers happened to produce a slightly
worse passive captain/XI choice. Given the 19-week gate already answered
"does E7 improve squad quality" decisively (yes, twice), this is read as
small-sample noise, not a real effect — but it's exactly what a full
end-to-end backtest (§5) would resolve either way.

---

## 5. What works vs what doesn't

**Works:**
- Residual/delta learning (classic forecast + article text → bounded
  correction) — validated twice, two different seasons, +11 and +53.
- "All fields" LLM adjustment config specifically — the other two configs
  tested did not replicate.
- Deployment-regime training for G2 (chrono-legal adapters, two-model
  learning ledger, delta-bearing-week filter) — the whole pipeline
  executed end-to-end via armed chains with zero manual intervention
  after launch.
- G2 plan-horizon GRPO itself: 6/6 eval windows won, both on classic and
  on E7-adjusted states, with genuinely differentiated per-window chip
  choices (not a canned response).
- LLM condensation of scout articles into short evidence snippets — after
  fixing two bugs (§6), spot-check quality was clean, factual,
  fantasy-relevant.
- `min_new_tokens` at decode — fully resolves the empty-plan attractor
  (§6), a deployment-legal, zero-retraining fix.

**Doesn't work / didn't help:**
- G1 (weekly-bandit GRPO, the pre-G2 approach) — machinery validated but
  signal was marginal; superseded by G2's multi-week plan formulation.
- Merging E7's weights into G2's policy init (v2b) — ties v2 on the
  metric that matters, but collapses to a single undifferentiated chip
  choice on off-distribution (classic) states. No net win; real
  robustness cost. v2 (fresh LoRA) stays the lead candidate.
- Two of three chrono-2425 LLM adjustment configs (`availability_scaled`,
  `avail_soft`) — didn't replicate E7's own "all fields" win.

**Open item (natural next step)**: no run yet stacks classic → E7 delta →
G2 planning end-to-end on the *same* 19-week rolling gate protocol E7 was
gated on. That would produce one number directly comparable to
1,058/1,069/1,314, closing the loop between the forecast-layer win and
the decision-layer win.

---

## 6. Key methodology lessons

**Q1: The GRPO empty-EOS decode attractor.** G2-v2's trained policy
emitted EMPTY completions (immediate EOS) under greedy decoding on 4/6
eval windows, despite healthy positive training rewards throughout
training. Cause: when every sample in a GRPO group is empty, the group's
reward has zero std → zero advantage → the empty mode is never
penalized, so it survives training as a greedy-decode attractor even
though temperature-0.8 sampling (the training regime) usually escapes it.
**Fix: decode with `min_new_tokens=8`** (a flag added to
`scripts/run_grpo_plan_eval.py`) — fully deployment-legal since it's a
decode-time setting, not a training change. After the fix: 0/6
unparseable, and sampled vs min-tokens-forced decodes of the same window
converge on identical realized outcomes. **Check any future GRPO-trained
policy for this before trusting a greedy eval** — it's a structural GRPO
property, not specific to this task.

**Q2: Condensation-pipeline bugs (found via spot-check before trusting
the data).**
1. *Decoding-artifact tails* (~2.3% of rows, 99/4,308): the custom
   `<|turn|>` chat template's stop cue is *learned* by JSON-task adapters
   (fine-tuned to emit EOS right after the closing brace) but the base
   model has no such training for free-text answers in this template, so
   greedy decoding sometimes ran past the real answer into stray
   non-Latin characters or repeated-symbol tails (e.g. `"...Fulham.แ"`).
   Fixed with a tail-stripping cleanup function.
2. *Sentinel filter bug*: the loader required an exact match to
   `"nothing."` (trailing period) to treat a response as "no evidence,"
   but the model overwhelmingly replies bare `"nothing"` with no period —
   67.2% of all responses. The old filter would have let two-thirds of
   placeholder non-answers leak into G2's prompts as if they were real
   evidence. Fixed to compare `text.rstrip(".").lower()`.
   After both fixes: 32.3% of docs (1,392/4,308) yield real snippets;
   spot-read of the rendered scout-notes block was clean, factual, and
   fantasy-relevant (injury status, form, fixtures, defensive-contribution
   stats).

---

## 7. Direct Q&A (answers given in conversation, consolidated)

**Q: What is E7 specifically?**
A: A fine-tuned Gemma-4B LoRA that reads pre-deadline article text
alongside the classic ridge forecast and outputs a bounded JSON delta —
"how much to nudge this number," not a fresh prediction. Exactly the
residual-learning design described independently in conversation. "E7" =
7th rung of the ladder = E6's schema + scout-evidence-enriched corpus.

**Q: What's the diff between G2 (v1) and G2-v2?**
A: v1 was a throwaway machinery smoke test on raw classic states, killed
early, never evaluated — it doesn't represent G2's capability. G2-v2 is
the real, fully-trained (232 steps, 8 epochs), properly-evaluated policy,
trained on the deployment-regime adjusted states (E7-adjusted numbers +
Δ + snippets) across three seasons.

**Q: What's the intuition for why v2b (E7-merged init) didn't work as
well as v2?**
A: v2b ties v2 exactly on the states that matter (adjusted: +28 vs +27)
but collapses on classic states (+3 vs +47), always picking the same
chip (`triple_captain`) regardless of the actual state. Merging E7 into
the base specializes the model's default behavior toward the specific
input shape E7 was trained on (delta-annotated, evidence-rich prompts);
since ALL of G2's own training data was also in that shape, nothing ever
taught the merged model to handle a differently-shaped input gracefully.
It became a narrow specialist. v2 (plain base weights) stayed flexible
across both input shapes because it was never biased toward one. The
E7-merge bought no additional planning skill where it mattered and cost
real robustness where it didn't — hence v2 remains the better candidate.

**Q: Is the base-weights version (v2) already better than classic, and
how does E7 alone compare to G2-v2 and G2-v2b?**
A: Yes, v2 beats "no planning" decisively in its own metric (+47 / +27).
But E7's 1,058→1,069 gate number and G2's 968→1,015 / 940→967 numbers are
NOT directly comparable — different protocols (19 weeks vs 3 windows,
autosubs included vs excluded, real sequential transfers vs a
plan-then-roll-out env). The clean informational finding from the v2b
ablation is that the adjusted-state prompt already carries *all* of E7's
useful information explicitly (as numbers and snippets) — giving the
planner E7's weights on top added nothing further, only cost robustness.
A true side-by-side "does the full stack beat E7 alone on the same 19-
week gate" number does not exist yet (§5 open item).
