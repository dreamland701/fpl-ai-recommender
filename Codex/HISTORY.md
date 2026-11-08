# Codex review history

## 2026-10-03 — Independent review started

Requested scope: deeply review the FPL forecasting, SFT, RL, live-season performance, missing capabilities, code quality, and a practical improvement plan.

Working agreement: all new review documents, analysis scripts, outputs, and logs stay under `Codex/`. Existing application code, training artifacts, and reports are read-only. No model training or FPL account actions are authorized by this review.

Initial inventory: roughly 703 MB data, 75 GB training artifacts, 52 GB reports, 43 MB logs. README is substantially older than the implemented SFT/RL pipelines. Found a live 2026-27 ledger and GW1–5 artifacts; awaiting optional user context on manual decisions.

## Existing project history reconstructed from artifacts

This is a condensed artifact-based history, not an audit of every prior conversation or an endorsement of every historical conclusion. Some session-state documents contain later appended updates despite older filenames.

| Period | Recorded development | Review implication |
|---|---|---|
| April–June 2026 | Baseline recommendation system; direct forecast/transfer-choice SFT; format and ranking experiments | Useful foundations, but current code and later corpora supersede the README |
| Early July | Bounded/shrunk residual SFT and richer prompt/evidence variants | Better formatting and MAE do not automatically establish decision value |
| Mid/late July | E6/E7 evidence results, chronological adapter surfaces, G1 bandit and G2 multiweek plans | Shared baselines, state caches, label maturity, and future observations need revalidation |
| Late July–August | G2 variants, G3 candidate-transfer actions, E9 clean-season split, E10 prelaunch and E11 defensive-contribution/full-data training | Historical evaluation and production artifacts are distinct; frozen adapters depend on exact baseline recipes |
| August–September live GW1–5 | Identity fixes, live form recomputation, prior blending, bench-order output, status backfill, settlement checks, multiple conversational overrides | Live process was evolving; treating all five weeks as one fixed model trial is inaccurate |
| September | E12–E19, market/context/opponent features, G4 forecast-reward experiment | More experiments on reused windows increase the need for prospective confirmation |
| September 26 | E19 evaluation on GW27–38, three four-week decision windows | Wider coverage is useful but not immune to repeated selection or target overlap |
| September 29 artifact directory | Adapter decomposition and reported broader decision comparisons | Core shrink decomposition independently reproduced; whole 21-window benchmark not independently recreated |

Sources include `docs/project_history_2026_07_12.md`, `docs/session_state_2026_07_12.md`, `docs/g2_results_and_faq_2026_07_26.md`, `docs/rl_forecast_design.md`, live ledger/artifacts, E-series manifests, and `reports/adapter_bench_2026_09_29/README.md`.

## 2026-10-03 — User clarification

User reports broadly following recommendations, with back-and-forth discussion and fine-tuning. Review attribution therefore distinguishes raw saved forecasts, optimizer proposals, conversational overrides, and final entered squads. Saved ledger and recommendation artifacts were available; no claim is made that all conversations were read.

## 2026-10-03 — Verified findings and measurements

- Ledger total: 283 versus 297 summed weekly averages.
- Full pytest suite: 76 passed, 12 failed; system-Python import failures are separately recorded.
- Confirmed ownership count/percentage mismatch, historical status provenance problem, multiweek target overlap, full-season centering, future RL observation dependency, and live prior-context loss.
- Reproduced several scoring/rule/parser defects in small counterexamples.
- Live saved SFT outputs improve all-player MAE in five of five weeks and worsen RMSE in five of five; top-11 unconstrained diagnostic loses or ties each week.
- Independently reproduced E19's shrink-driven MAE improvement.
- A naive chip schedule earns +13/+15 against the RL no-chip reference in the current flawed environment.
- Purging immature multiweek targets changes forecasts but leaves realized totals unchanged in three tested windows. This limits causal claims about that defect's score impact.

## 2026-10-03 — Review recommendation

Proceed in order: data/timestamp/unit integrity; shared scorer and game state; stronger calibrated numerical forecasts; evidence-extraction SFT with controlled ablations; deterministic multiweek planner; then a small RL pilot against equal-resource baselines. Keep future deployment in shadow comparison until the gates in `PLAN.md` are met.

No production repair has been applied by this review. Recommendations are intentionally separated from verified implemented changes. All new persistent artifacts are inside `Codex/`.
