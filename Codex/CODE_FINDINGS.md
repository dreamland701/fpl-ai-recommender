# Code findings and repair acceptance criteria

Line references refer to the source hashed in `analysis/provenance.json`. P0 means fix before trusting a new training/deployment comparison; P1 means correctness or deployment behavior; P2 means model quality, reproducibility, or maintainability. Priorities concern future work, not a retrospective claim about exact points lost.

## P0-01 — Ownership counts are treated as percentages

**Confirmed, high confidence.** `src/fpl_ai/dataset.py:399` renames `selected`; `_normalize_percent` at line 223 only parses numbers. `src/fpl_ai/api.py:140` supplies true live percentages. `dataset.py:1522` subtracts the historical count from the current percentage. `scripts/attach_market_to_corpus.py:32` also copies the mislabeled quantity into SFT prompts.

Evidence: `analysis/units_and_status.json`. 2025-26 median 19,545, maximum 9,515,178, 96.37% above 100. First E13a train prompt: `owned by 6072.0% of managers`.

Repair: define `selected_count`, `entry_count_asof`, and `ownership_fraction` separately. Only calculate a percentage with a verified matching denominator. Mark unavailable percentages missing or drop that feature from the comparable historical/live model. Rebuild ownership changes and affected corpora.

Acceptance: percentage/fraction range assertions; unit-tagged schema; synthetic historical/live equality; no percentage outside its legal range; missing denominators remain explicitly missing. Check ablations without market features before assigning their previous failures to the modeling idea.

## P0-02 — Multiweek targets include outcomes across the prediction cutoff

**Confirmed, high confidence.** `src/fpl_ai/backtest.py:134` and `src/fpl_ai/llm_data.py:1206` filter origin weeks only. `dataset.py:1256` builds forward sums. `scripts/build_residual_player_forecast_split_v2.py:857` splits the SFT corpus by origin without target maturity.

Evidence: `analysis/table_audit.json`: before GW27, 1,634 three-week and 3,248 five-week selected targets cross the boundary. Haaland's GW26 three-week target includes GW27 and GW28 points. Source-level behavior applies to SFT completions as well; the precise affected count depends on each corpus's target version.

Repair: centralize target-specific selection using `label_end_at` and `label_available_at`. Split training separately by horizon; for joint SFT, mask immature fields or use the longest target's maturity constraint. Regenerate out-of-fold baselines, residual labels, and RL caches.

Acceptance: perturb every outcome at/after evaluation cutoff and assert unchanged training inputs, supervised targets, preprocessing parameters, and predictions produced at the cutoff. This must cover baseline training, corpus export, calibration, SFT, and RL state generation.

Measured scope: `analysis/leakage_sensitivity.json` shows changed long-horizon forecasts but identical realized totals in three partial-repair backtests. Do not describe this bug as a measured explanation of the 14-point live deficit.

## P0-03 — A season-level status/news lookup is used as historical information

**Confirmed provenance defect; predictive effect unquantified.** `dataset.py:272` reads one `players_raw.csv`; lines 422–425 merge status/news when raw weekly records lack them. Lines 962–963 shift the resulting series.

Evidence: all seven historical merged seasons through 2025-26 lack raw status; current season has it. The static lookup provides no historical timestamp contract. Club IDs also preferentially come from the lookup, so within-season club changes require audit.

Repair: use archived deadline snapshots. Otherwise use an unknown/missing signal and exclude nonhistorical status/news from retrospective claims. Preserve club membership valid at each fixture/deadline. Distinguish snapshot times from fact-validity times.

Acceptance: changing today's lookup cannot alter last season's pre-deadline state; players who move clubs retain their old membership before the move. Do not use the old 19–38% flagged rate as a calibration target for live flags.

## P0-04 — RL opening prompts expose later-week forecast information

**Confirmed, high confidence.** `src/fpl_ai/grpo_plan_env.py:354` reads each future state's forecasts into `state_prompt`. `scripts/build_grpo_state_cache.py:72` generates those forecasts using each state's own historical cutoff.

Evidence: `analysis/code_probes.json`, `future_information_prompt`: changing only future forecasts changes the opening prompt from future squad projection 87 to 1,587. No opening state fact changed.

Repair: all future outlooks at origin t must be forecasts made at t using the schedule known at t. Later realized states can generate rewards/transitions only after their information becomes available. Prefer closed-loop weekly policy evaluation over an open-loop string of future decisions.

Acceptance: altering week t+1 results or reports cannot change the policy observation at t. Evaluate training and live inference through the same observation builder.

## P0-05 — Full-season centering violates preprocessing cutoffs

**Confirmed, high confidence; impact unquantified.** `dataset.py:999` uses a full-season mean for F6; line 1087 does the same for F12. The features are materialized before the train/test split.

Evidence: `analysis/season_centering.json`; also directly apparent from `groupby(season).transform("mean")`.

Repair: fit centering in each training fold or use a strictly lagged league reference. A league baseline should count team-fixtures, not weight teams implicitly by their number of player rows.

Acceptance: appending/changing future fixtures and results leaves all existing pre-deadline feature rows identical. Merely selecting past rows from a precomputed full-season feature file does not pass this test.

## P1-01 — Live form recomputation loses the adopted prior blend

**Confirmed, high confidence.** `dataset.py:1413` keeps only the live season; the prior lookup at line 930 needs the preceding season; lines 1588–1602 overwrite joined features with the recomputed values.

Evidence: `analysis/prior_blend_parity.json`: with the blend flag enabled, providing prior-season context changes 420/667 GW6 `points_avg_3` values. This is a current-code reproduction, not an assertion that the historical GW3 run used identical source and flags.

Repair: give the builder exactly the historical context required for its features, bounded by the requested deadline. Store feature recipe and prior parameters with the model. Use the same builder in historical replay and live inference.

Acceptance: from an archived deadline packet, batch and live paths produce identical model inputs and forecasts. Cover GW1, GW2, return from injury, a new signing, promoted club, and midseason player transfer.

## P1-02 — Availability is not modeled as appearance probability

**Confirmed modeling mismatch.** `src/fpl_ai/models.py:182` derives appearance probability from expected minutes / maximum minutes. The label actually means any appearance. A guaranteed 30-minute cameo is a direct counterexample. Minutes are clipped to 180 even for one fixture; doubles are not a probability union.

Repair: fit a probability model and conditional minutes model, or one coherent categorical minutes distribution per fixture. Define points as unconditional expected points, and remove accidental duplicate availability discounts.

Acceptance: reliability/Brier/log-loss tests on held-out weeks, separate cameo and 60-minute calibration, legal fixture-specific minute bounds, blank-week invariants, consistent aggregation over doubles. Model scoring tests should distinguish `P(appear)` from `P(start)` and `P(60+)`.

## P1-03 — Autosubs are suppressed when they cannot complete ten outfielders

**Confirmed scoring bug.** `src/fpl_ai/backtest.py:483` requires exactly ten outfield players; `_apply_automatic_substitutions` at line 544 tests only the active subset plus candidate bench players. With too many absent starters, no subset satisfies that count, so even legal available replacements are ignored.

Evidence: `analysis/code_probes.json`, `partial_autosubs`: four absent outfield starters, three legal available substitutes, zero substitutes used. The formation should be evaluated while retaining unfilled zero-point slots, rather than requiring eleven active scorers.

Repair: one official-rules scorer with ordered substitutions, unfilled places, captain/vice, BB/TC, and all formation constraints. Use it in backtests, G1/G2/G3/G4 rewards, and live settlement.

Acceptance: explicit cases with 0–5 missing starters; unavailable bench players; GK-only substitution; multiple missing defenders; captain missing, vice missing; BB with absent players; double-week partial appearances. Compare archived official `automatic_subs` and realized totals where obtainable.

## P1-04 — Valid 5-2-3 is missing; 3-3-4 is present

**Confirmed, high confidence.** `src/fpl_ai/config.py:40` lists 3-3-4, which a legal three-forward squad cannot field, and omits valid 5-2-3.

Evidence: the toy squad in `analysis/code_probes.json` scores 74 under existing enumeration versus 83 with legal 5-2-3.

Repair: generate all legal formations from positional bounds and total count instead of maintaining an error-prone hand list.

Acceptance: exhaustive feasible XI comparison for a fixed 15-player squad and clear rejection of an illegal input squad. The optimizer must never silently use an illegal fallback XI.

## P1-05 — Transfer/chip rules are not versioned by season

**Confirmed.** `grpo_plan_env.py:38` caps FTs at two. `backtest.py:1072` defaults to two. The plan environment's comment and behavior apply two half-season chip sets even to 2023-24, although the two-set system started in 2025-26. General backtests track one BB/TC copy for the requested window and can reset resources at each window start.

Evidence: bank four FTs in the probe and the next count becomes two. [Current official transfer rules](https://www.premierleague.com/en/news/2174907) allow five; [official 2025-26 changes](https://www.premierleague.com/en/news/4373187) and [2026-27 changes](https://www.premierleague.com/en/news/4679873) establish the rule eras.

Repair: `Ruleset(season)` with transfer caps, chip availability windows, scoring era, special transfer allocations, and WC/FH transfer-retention behavior. Historical seasons should follow historical rules or be explicitly labeled counterfactual current-rules simulations. Account for the 2024-25 Assistant Manager chip if claiming complete official-season reproduction.

Acceptance: fixtures at rule boundaries, GW19/20, saved FT caps, multiple transfers/hits, WC/FH persistence, special 2025-26 AFCON allocation. Rules should never be inferred from a comment or current season constant.

## P1-06 — Sell prices are wrong in historical simulation

**Confirmed.** `backtest.py:572` replaces a player's sell price with current raw price, without purchase-price profit sharing. It prefers current raw `price` over `price_pre_deadline`, introducing another timing issue. RL carries acquisition prices without refreshing them.

Evidence: buy 5.0, market 5.4: historical helper produces 5.4 rather than 5.2. The live G2 script separately implements half-profit logic, confirming divergent paths.

Repair: track purchase cost, deadline market cost, and sell value in integer tenths. Never overwrite purchase cost. [Official price rules](https://www.premierleague.com/en/news/2174907).

Acceptance: rises of 0.1/0.2/0.3, falls, sale and repurchase, multiple transfers, and FH reversion all conserve the correct bank.

## P1-07 — RL's action space makes genuine transfer banking ineffective

**Confirmed design limitation.** `grpo_plan_env.py:223` sets `max_transfers_considered=1`. Policy can bank or select one of at most three proposals. It cannot execute two banked transfers together, WC, or FH. Starting at one FT, spending at most one per week means the buffer's core strategic use cannot be realized.

Repair: enumerate/prune complete legal transfer sets, including hold, coordinated two/three-player moves, budget-enabling moves, and chip plans. Expose candidate identities and utilities for the actual state in which they will be chosen.

Acceptance: a constructed case where banking then making a double transfer is optimal must be expressible and recoverable by the planner/policy. Cap search by principled candidate pruning rather than excluding the action category.

## P1-08 — No-chip baseline overstates evidence for RL skill

**Confirmed evaluation design problem.** `grpo_plan_env.py:326` evaluates all-default actions with no chips. Policy can spend chips. A paired reward subtracts a baseline but does not make resources equal.

Evidence: `analysis/rl_naive_chip_benchmark.json`, no-model rule earns +13/+15. Saved v3 adjusted result is +20 against the no-chip baseline; the naive result is not directly a complete deployment challenger but narrows what that +20 establishes.

Repair: compare against a deterministic planner with identical initial state, information, horizon, chip budget, transfer rights, and scoring. Report chip-only, captain-only, transfer-only, and full-policy ablations.

Acceptance: a policy that simply consumes chips cannot pass a promotion gate without outperforming the same-resource reference strategy.

## P1-09 — Evaluation carries chips but resets other season state

**Confirmed.** `scripts/run_grpo_plan_eval.py:124` carries chip sets across episodes. `PlanEpisodeEnv.rollout` starts each episode from `states[0].squad/bank/free_transfers`. Policy-induced squad changes do not persist between evaluated windows. `build_episodes` truncates incomplete tails.

Repair: continuous season replay, or explicitly independent episodes with all initial resources reset consistently and no claim of season return. Score the last partial episode.

Acceptance: changing an action in one window changes the next window's squad/bank/FT as appropriate. Every intended gameweek is scored once. GW30 should not disappear from a purported GW12–30 gate.

## P1-10 — Plan parse success can mean “first object plus defaults”

**Confirmed, high confidence.** `grpo_plan_env.py:124` extracts a single JSON object after array recovery fails. A response consisting of six newline-separated objects becomes one action and five defaults.

Evidence: `analysis/code_probes.json` loses the second action's bench boost while reporting successful parsing. Saved `grpo_plan_eval_2526_adjusted_v3_min8.json` contains newline-object responses.

Repair: require a schema-valid array of exactly the requested horizon. Keep fallback behavior safe but label partial/fallback/defaulted output separately. Use constrained generation where supported.

Acceptance: `valid_json`, `valid_schema`, `legal_action`, and `executed_as_requested` are separate metrics. Missing, extra, NaN, duplicate, and malformed fields are covered. No silent padding counts as a compliant plan.

## P1-11 — Prediction joins and clipping differ across paths

**Confirmed latent failure modes; saved live rows checked were aligned.** `src/fpl_ai/llm_adjust.py:104` and the live draft scripts zip examples and predictions by order, checking only length. The key excludes season. The shared parser clips deltas, but `scripts/apply_llm_deltas_and_draft.py` uses a different parser without the same bound checks. `llm_adjust.py:160` permits negative adjusted points while the live script floors them to zero. Some bounds are duplicated in three places.

Evidence: `analysis/code_probes.json` maps JSON `NaN` to a +2 points delta via Python min/max behavior, and produces -1.9 points in one path versus 0 in another. No such bad live response was demonstrated; the defects are reproducible parser/application behavior.

Repair: join on `(season, week, stable_player_id, snapshot_id, baseline_version)` and reject mismatches/duplicates. One finite-value schema, one bounds definition, one application function. Specify whether negative expected FPL points are supported; apply that choice consistently.

Acceptance: permuting prediction rows leaves results unchanged; mismatched identifiers fail; NaN/infinity/bools fail numeric validation; live and backtest application is byte-identical for the same inputs. Preserve the fact that realized FPL points can be negative when choosing output constraints.

## P1-12 — Live future fixture construction is incomplete

**Confirmed code limitations, not measured GW1–5 harm.** `dataset.py:1434` stores one opponent per team, overwriting one fixture in a double week. The synthetic week retains identity fields including an old kickoff time. `scripts/apply_llm_deltas_and_draft.py:113` and `run_g2v3_live_read.py` hardcode `fixture_count=1`. The live G2 script's offset-2 projection uses `(5GW−3GW)/2`, which describes weeks 4–5, not week 3.

Repair: fixture-level projections from a schedule snapshot, aggregate to gameweeks only afterward. Never infer an exact future-week allocation from two horizon sums without stating the approximation.

Acceptance: live/replay parity for blank and double weeks; no overwritten opponent; correct kickoff/rest dates; future weeks reconcile to horizon totals under the chosen forecast definition.

## P1-13 — G4 reward does not match its deployment pool or design document

**Confirmed.** `src/fpl_ai/grpo_forecast_env.py:115` replaces one player's delta in a classic pool; `realized_points_for_forecasts` omits autosubs. `docs/rl_forecast_design.md` describes adjusted peers and autosubs. The prompt does not encode squad-dependent decision state. `train_gemma_grpo_forecast.py:106` selects boundary examples by realized reward differences.

Repair: use a coherent joint adjusted reference pool and exact scorer; train on diverse actual squad states if reward depends on squad context; select decision boundaries by changes in legal actions/projections without filtering on held-out outcomes. Keep forecast calibration objectives if outputs are advertised as expected points.

Acceptance: applying reference deltas reproduces the deployed reference decision and score. Train-time sampled reward and eval reward agree. Explicit unit/integration coverage for G4, which currently has no dedicated test module.

## P1-14 — Current suite is broken and README runs only part of it

**Confirmed.** `python -m pytest -q -p no:cacheprovider tests` in the existing environment yields **76 passed, 12 failed**. Failures share `KeyError: goals_scored` in `dataset.py:797`; `_ensure_columns` omits that column and `assists` while later code assumes them. Plain system Python cannot import pandas/TRL. `unittest discover` runs 63 tests and misses module-level pytest functions.

Repair: make required versus optional raw fields explicit, fix fixtures or defaults according to the schema, and use pytest in the documented/CI path. Do not treat older “green suite” notes as a current result.

Acceptance: green existing suite plus meaningful invariants for the defects above; record the interpreter and dependency lock. GPU/model-loading tests should be separately marked so ordinary correctness checks remain cheap.

## P2 — Additional improvements requiring controlled experiments

| Area | Evidence / implication | Next step |
|---|---|---|
| Expected points objective | SFT token loss on clipped numeric targets; MAE improves while live RMSE worsens | Separate expected-value calibration from token generation and MAE reporting |
| Position/era | `SAFE_FEATURE_COLUMNS` has no position encoding; old and new scoring labels pooled | Position interactions or component forecasts, scoring rules versioned by season |
| Horizon tail semantics | `dataset.py:1258` scales one remaining week to a fictitious full-horizon rate | Store observed horizon length; distinguish rate targets from actual remaining-season totals |
| Candidate pruning | `decision.py:524` outgoing bottom six, incoming global top 24 | Candidate sets stratified by position/price, owned assets, enablers, and horizon; compare exact optimizer |
| Draft vs fielded value | Initial beam weights all 15; backup-GK weight differs live/backtest; captain leverage defaults differ | Unified expected-fielded-points objective and matching draft settings |
| Captain/vice | Captain override can leave captain and vice equal; lineup objective lacks joint fallback value | Enforce distinct identities and evaluate fallback with minutes scenarios |
| Transfer horizon | Future squad utility uses this week's XI and a 1GW captain bonus | Explicit per-week XI/captain variables over the horizon; terminal value for resources |
| Serialization | `train_model_suite` / `load_model_suite` do not persist `band_calibration` | Round-trip equality tests and versioned complete bundles |
| Missing features | `predict_frame` silently fills absent model features with zero | Required schema validation and explicit supported missingness |
| API caching | `api.py:34` reads a cached endpoint indefinitely | Immutable timestamped snapshots plus explicit fresh acquisition; no silent stale cache |
| Deadline provenance | `build_week_state` infers first kickoff minus 90 minutes; blank strings can defeat `min` | Official event deadlines; parse timestamps before taking a minimum |
| Text provenance | Publication-time filter exists, but later article updates can overwrite earlier content | Content hashes and version capture; archival uncertainty labeled |
| Entity matching | Surname-based mention matching, including diacritic-sensitive prompt truncation | Stable entity resolution and club context; measure wrong-player rate |
| Reproducibility | No Git repository found at cwd or its parents; many env flags and manual scripts | Initialize/version the project deliberately; immutable run manifests and a locked environment |
| Test multiplicity | Many E-series variants reuse small historical windows | Treat these windows as development data; nested chronology and future shadow evaluation |

These items are proposals or source-level risks unless a reproduction is explicitly stated. Feature absence in a prompt is not proof that the feature would improve outcomes, and a one-window win is not sufficient evidence to adopt it.
