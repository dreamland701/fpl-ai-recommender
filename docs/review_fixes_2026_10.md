# Review fixes, October 2026: data contract, scoring rules, re-baseline

*Written 2026-10-04. Responds to the external review in `Codex/` (REVIEW, PLAN, CODE_FINDINGS, EXPERIMENTS). Finding IDs below are the review's own.*

## The short version

- **The review was right on every data and scoring item I checked.** I fixed all the P0/P1 items that live in the classic pipeline, the scorer and the delta path. The RL-environment items stay deferred while RL is frozen.
- **The fixed pipeline beats the deployed one, but not conclusively.** Over 21 four-week backtest windows (84 gameweeks): classic+F6 on the fixed pipeline scores **5,162 vs 4,971** for the deployed pre-fix classic+F6. That is **+191**, about +9 per window or +2.3 per gameweek, with t = 1.54: positive, not yet proven. One-week forecast error is the best of any configuration (MAE 1.024 vs 1.036).
- **The largest new finding is a live-only bug that compressed popular players' forecasts.** Training stored ownership as raw manager counts while the live builder used percentages. For GW6 this cost Haaland about 5.6 points of 5-week forecast, João Pedro 5.4, and Bruno 2.7. Backtests could never see it, because they were consistently wrong in counts. It is a concrete mechanism behind the GW2 "Haaland ranked 43rd" complaint. The earlier premium-bias investigation was closed as "not actionable" because it looked only at backtests.
- **F6's headline was partly leakage.** Its edge shrinks once its centering uses only past data. Over 21 windows it is worth +33 decision points on the old pipeline and +74 on the fixed one (t = 1.30), not the +112 over 5 windows recorded before. It still improves accuracy in 16 of 21 windows, so it stays.
- **Tests: 117 passing (was 76 passing, 12 failing).** That includes 29 new tests pinning these defects. The data-contract and delta-parser tests fail on the old code; the rules tests pin the official rules, including every case the old code got wrong.
- **GW6 packet:** `reports/gw6_packet_2026_10/README.md`. With the bug fixed, the Haaland route (Bruno + Isak → Haaland + a £5.5–5.7m midfielder) is the model's top option, about 4 points over five weeks ahead of Bijol → De Cuyper. That margin is small, and the squad, selling prices and free transfers need confirming in the app.

Nothing here needed a GPU. No adapter was trained or decoded, and nothing was published.

## 1. Data contract (P0-01, P0-02, P0-03, P0-05, P1-01)

Every fix has an invariant test in `tests/test_data_contract.py`, written to fail on the old code (all 9 original tests failed there).

### P0-01: Ownership counts were stored as percentages

- **Problem:** vaastav's `selected` is a manager count (median 19,398, max 9.6 million in the old table). It went into `selected_by_percent_pre_deadline` unchanged.
- **Fix:** `_ownership_percent` (in `dataset.py`) converts counts to percentages. The denominator is derived from the data: in every week, the squad totals must sum to 15 × the number of entries. The entry count is the running maximum of `Σ selected / 15` up to that week, so it uses no future data and doesn't dip in blank weeks. Data already in percent passes through unchanged.
- **Check on real data:** the new column tops out at 93.2% (Haaland 2023-24) and Haaland averages 70.2% in 2026-27. In the median week, across rows for players with a fixture, ownership sums to **exactly 1500.0%**, the 15-player identity. It never exceeds 1500% in any week. The live API sum is also 1500.0.
- **Known limits:**
  - Placeholder rows for players whose team blanks carry their last observed ownership. That is valid as of the deadline but stale, and it pushes some blank weeks' totals to 1,509–1,701%. Those players can't score that week.
  - 2020-21 GW1, when four clubs blanked, has an under-counted denominator because there is no earlier week to carry forward.

### P0-02: Multi-week labels crossed the fit cutoff

- **Problem:** a training row for GW w−1 carried a 5-week label summing GW w−1…w+3, which are the outcomes being predicted.
- **Fix:** `training_rows_asof(frame, season, week)` keeps rows before the cutoff and blanks any same-season 3/5/8-week label whose window reaches the cutoff. `RidgeRegressor.fit` drops those blank-label rows instead of reading them as 0. The same function is now used by:
  - the backtest (`_training_frame_for_week`)
  - `train_model_suite`
  - the SFT corpus baseline (`llm_data.py`)
  - the live runbook (`build_live_gw_examples.py`)
  - the GRPO state cache (via the backtest helper)
- **Effect:** the old pipeline's 5-week error looked slightly better (MAE 3.628 vs 3.655) because its labels overlapped the weeks it was tested on. The new number is the honest one.

### P0-03: End-of-season status and news were used as weekly history

- **Problem:** vaastav has no weekly status, so the old normalizer copied `players_raw.csv` (the season's final snapshot) onto every week. Every injury that ended someone's season showed up in GW1, giving a 19–38% "flagged" rate. The status was then also shifted a week.
- **Fix:** seasons without weekly status now carry status "unknown" and no news. The 2026-27 rows, which do have real pre-deadline snapshots from the live backfill, keep them unshifted.
- **Check:** historical flagged rate is now 0. The 2026-27 statuses are real: a 2,484, i 274, u 358, d 90, s 10.

### P0-03 (club part): End-of-season club

- **Problem:** players took their final club for the whole season, so every team-form feature mixed in the wrong club's matches.
- **Fix:** `_team_at_fixture` resolves the club from each row's fixture (`team_h` if home, otherwise `team_a`).
- **Check:** within-season movers went from 0 to 23–29 per season. For example, Eze is at Palace for 2025-26 GW1–2 and at Arsenal from GW3.

### P0-05: Full-season centering

- **Problem:** F6's opponent weakness and F12's team attack were centred on full-season means, which include future matches.
- **Fix:** `_asof_league_reference` uses each week's cross-section of teams' already-lagged values, counting each team once rather than weighting by player rows. This is the review's suggested repair.
- **Effect:** F6's spread fell from sd 1.18 to 0.76, and its correlation with the old feature is 0.66.

### P1-01: The live builder dropped the prior-season blend

- **Fix:** the synthetic next-week rows now include the previous season, so F2b reproduces live exactly. `LiveBatchParityTest` builds features through both paths and requires them to be identical.

### Found during validation, not in the review

- **Market timing.** Training used *last* round's price and ownership, while live used the *current* snapshot. A round's `value`/`selected` are its deadline state, so training now uses them directly. The price and ownership changes are round minus previous round, within season (`MarketTimingTest`).
- **New players' price change.** Live, a player with no history got "price change" equal to his full price (e.g. +6.0), and ownership change equal to his full ownership. Changes are now 0 when the last row is missing or from an earlier season.
- **First-row price.** GW1 rows had price 0 (`FirstRowPriceTest`).
- **Junk feature.** `primary_opponent_team_id`, a raw team number used as a numeric feature, was removed from the feature set.

## 2. Scoring and decision rules (P1-03, P1-04, P1-06, P1-11)

The rules now live in one module, `src/fpl_ai/rules.py`. Backtests, the legacy LLM-decision scorer (`llm_eval.py`) and the live scripts all use it. Tests are in `tests/test_rules.py` (14 tests).

| Finding | Before | After |
|---|---|---|
| P1-04 formations | Hand-written list with illegal 3-3-4, missing 5-2-3 | Generated from the rules: exactly the 8 legal shapes. An exhaustive search over all 15-choose-11 XIs matches the optimizer. An illegal squad raises an error instead of fielding an illegal fallback XI. |
| P1-03 autosubs | Four absent outfielders and three playing subs → **0** substitutions (old code, verified) | Official order: each absent starter gets the highest-priority playing sub who keeps the XI legal. Unfilled slots stay empty, so that case now makes 3 substitutions. Applied in the backtest and `llm_eval.py`. |
| P1-06 sell prices | Refreshed to the full current price (buy 5.0, now 5.4 → sells 5.4) | Purchase price tracked on `SquadPlayer`. Selling price keeps half of any rise, rounded down in tenths (→ 5.2). Refreshed at each week's *deadline* price before decisions, not carried from last week. Live scripts use the same `selling_price`. |
| P1-11 deltas | Backtest: JSON `NaN` → **+2.0** (Python min/max). Live: NaN → 0 points, and **no clipping at all**. Lookup keyed by (week, player) only. | One parser rejects NaN, infinity and booleans. One `apply_deltas_to_forecast` with one set of bounds, used by the backtests and both live scripts. Keys are (season, week, player). Predictions carrying IDs are joined on identity, so reordering rows changes nothing and mismatched IDs raise an error. Points are not floored at 0 in any path; that matches the evaluated backtests. |
| P1-14 tests | 76 passed, 12 failed (`KeyError: goals_scored`). README ran `unittest`, which misses module-level tests. | 117 passed. README now runs pytest with the project interpreter. |

Old-versus-new behaviour on the same inputs: `reports/review_fixes_2026_10/probe_old.json` and `probe_new.json`, produced by `probe_old_new.py` under each code tree. The table checks are `validate_tables.py` and `validate_tables2.py`.

## 3. Re-baseline

`reports/review_fixes_2026_10/run_rebaseline.sh`: 6 configurations × 21 windows = 126 squad backtests, CPU only. The windows are the 21 from the September replication: 2025-26 GW2–25 and GW27–38, and 2023-24 and 2024-25 GW12–35.

The six configurations:

- **O:** pre-fix code on pre-fix tables (what every earlier verdict used)
- **M:** fixed code on pre-fix tables (isolates the rules and label fixes)
- **N:** fixed code on the rebuilt tables (`data/fpl_training_rows_v3_contract{,_f6}.csv`)

Each is run as classic (`_C`) and classic + F6 (`_F`).

| Total points, 21 windows | Classic | Classic + F6 |
|---|---|---|
| O (pre-fix) | 4,938 | 4,971 |
| M (fixed code, old tables) | 4,988 | 5,039 |
| N (fixed code and tables) | 5,088 | **5,162** |

| Paired comparison | Total | Mean per window | sd | t | Wins/losses |
|---|---|---|---|---|---|
| All fixes, F6 (O_F → N_F) | **+191** | +9.1 | 27.1 | +1.54 | 10/9 |
| All fixes, classic | +150 | +7.1 | 17.5 | +1.87 | 11/10 |
| Rules + label fix only (F6) | +68 | +3.2 | 7.7 | +1.92 | 9/3 |
| Rules + label fix only (classic) | +50 | +2.4 | 4.9 | +2.23 | 9/5 |
| Table fixes only (F6) | +123 | +5.9 | 26.8 | +1.00 | 10/10 |
| F6 effect, pre-fix | +33 | +1.6 | 17.7 | +0.41 | 11/9 |
| F6 effect, fixed | +74 | +3.5 | 12.4 | +1.30 | 12/5 |

Part of the rules gain is accounting rather than better decisions: partial autosubs and 5-2-3 credit points the old scorer dropped.

**Forecast accuracy** (`walkforward_accuracy.py`: models fit exactly as in the backtest, every eligible player, the same 84 weeks; 3- and 5-week metrics only where the label window lies inside the season):

| | O_C | O_F | N_C | N_F |
|---|---|---|---|---|
| MAE, 1 week | 1.083 | 1.036 | 1.039 | **1.024** |
| RMSE, 1 week | 1.989 | 1.980 | 1.976 | **1.974** |
| MAE, 5 weeks | 3.806 | **3.628** | 3.702 | 3.655 |
| Bias, 5 weeks | +0.378 | +0.093 | +0.058 | **−0.022** |
| Premium (≥ £10m) bias, 1 week | −0.516 | −0.202 | +0.048 | **−0.010** |
| Premium bias, 5 weeks | −0.808 | +0.627 | +1.449 | +1.247 |

F6 versus classic on the fixed pipeline: better 1-week MAE in 16 of 21 windows and better 5-week MAE in 16 of 20. On the old pipeline it was 21 of 21 and 20 of 20, but full-season centering flattered it there.

**Noise.** Per-window sd of paired deltas runs 12–27 for configuration changes, consistent with the 14.9 noise floor recorded earlier. At this sd, a +2 points-per-gameweek effect needs about 30–40 windows to confirm at 95%.

## 4. The live ownership-unit bug, quantified

`reports/gw6_packet_2026_10/ownership_units_decomposition.py` refits the pre-fix model and reads its learned weights (with the same input clipping `predict()` applies). The ownership level, in counts, carries +0.634 standardized weight on the 5-week head.

Live, Haaland's 73.9 was read as 73.9 managers, about −0.34 sd, when his true count sits about +13 sd above the mean. His ownership change, −7,989,275, was clipped to the training minimum of −3.15 million.

Net effect on the pre-fix GW6 forecasts, against each player's own training-scale values:

| Player | 1 week | 5 weeks |
|---|---|---|
| Haaland | −0.80 | −5.62 |
| João Pedro | −0.63 | −5.39 |
| Bruno | −0.23 | −2.72 |
| Cherki | +0.13 | −1.17 |

The effect grows with ownership. A first version of this analysis was off by one coefficient and showed the opposite sign; it was caught and discarded before use.

## 5. Deferred, with reasons

| Item | Why deferred | What it needs |
|---|---|---|
| P0-04, P1-07 to P1-10, P1-13 (RL environments and evaluation) | RL is frozen; G2–G4 verdicts were flat or negative | Rebuild on `rules.py` (same scorer, chips, sell prices), with same-resource baselines and season-continuous replay |
| P1-05 season-versioned `Ruleset` | Backtests use one transfer per week, so the 2- vs 5-FT cap rarely binds | Do before any chip or transfer-policy work |
| P1-02 appearance model | Modelling work: P(appear) vs P(start) vs P(60+) | Logistic appearance head plus conditional minutes (the earlier check found logistic beats the LLM on P(appear)) |
| P1-12 live double-gameweek fixtures | No DGW before GW6 | Fixture-level projections; `fixture_count` now passes through the live delta scripts when present |
| P2 candidate pruning (the decision layer only sells the bottom 6) | Changes decisions, so it needs its own backtest | Owned-asset and enabler candidates, exact-optimizer comparison |
| SFT corpora | Market and status lines and classic baselines were built with the old units and labels | Rebuild corpora on the fixed tables before any adapter retraining (GPU, needs your go-ahead) |
| Adapter shadow decode | GPU gate | Note: live baselines now come from the fixed pipeline, a shift from what the adapter was trained on |

## 6. What changed where

- **Backup of the pre-fix code:** `/home/wescheng/fpl_backups/2026-10-03_pre_review_fixes/`. The full unified diff is `reports/review_fixes_2026_10/changes_vs_backup.diff` (19 files).
- **Code:**
  - `dataset.py`: ownership, status, club, as-of centering, market timing, label maturity, live builder
  - `models.py`: NaN labels dropped, fit cutoff
  - `backtest.py`: autosubs, sell prices, as-of fit
  - `rules.py` (new)
  - `config.py`: generated formations
  - `decision.py`: no illegal fallback
  - `types.py`: purchase price
  - `llm_adjust.py`: parser, shared apply, identity join
  - `llm_eval.py`, `llm_data.py`
  - live scripts: `apply_llm_deltas_and_draft.py`, `recommend_gw2_actions.py`, `run_g2v3_live_read.py`, `build_live_gw_examples.py`, `build_adjusted_grpo_states.py`
- **Tables:**
  - `data/fpl_training_rows_v3_contract.csv` (classic)
  - `data/fpl_training_rows_v3_contract_f6.csv` (classic + F6)
  - Both built with `FPL_PRIOR_BLEND=1` (+ `FPL_OPPONENT_INTERACTION=1`). Old tables are untouched.
- **Weekly runbook:** after `run_weekly_ingest.sh`, rebuild `v3_contract_f6` with the fixed code and pass it as `--training-data`. `build_live_gw_examples.py --stage corpus` still rewrites the season's `fixtures.csv`/`teams.csv`, as before.

## 7. Follow-up, 2026-10-04 (GPU approved)

- **Entry reconciliation:** your FPL entry (6535607) is now pulled from the public API (`reports/gw6_packet_2026_10/fetch_entry.py`, `entry_state.py`). Selling prices recomputed from purchase prices match the app on all 15 players. No chips have been used.
- **Live corpus fix:** `build_live_gw_examples.py --stage corpus` used to rewrite the live season's `fixtures.csv` with 8 schedule columns. That drops the score columns the table builder reads. It now writes every API field, as `sync-history` does, and passes `fixture_count` through to the live delta scripts.
- **GW6 shadow decode:** E11-full on fixed-pipeline classic baselines (`reports/live_gw6_2627_*`), read with `shadow_sheet.py`.
- **E20:** the E19 recipe rebuilt on the fixed tables.
  - `scripts/run_e20_contract_pipeline.sh` builds the corpus and split, and gates on prompt parity with E19 and neutral historical status lines.
  - `scripts/run_e20_contract_chain.sh` then trains (~55h), decodes and scores the 12-week holdout, computes availability AUC among likely starters, and backtests E20 against fixed classic+F6.
  - At 2026-10-09 17:00 UTC the chain builds the GW6 final packet (`reports/gw6_packet_2026_10/final/`).
- **Reference for E20:** E19's existing holdout deltas applied on the fixed pipeline give +30 over the three windows (−21, +52, −1). On the pre-fix pipeline they gave +9 (−38, −22, +69). Both are inside the adapter noise of about 24 points per window.

### E20 verdict (holdout read 2026-10-06; `reports/review_fixes_2026_10/e20_early_eval.json`, `bt_e20_early/`)

E20 is the E19 recipe trained on the fixed data. It trained for 53.6 hours with a final loss of 0.14, and parsed 3,072 of 3,072 holdout responses.

| 2025-26 GW27–38 | Classic (fixed baselines) | E20 |
|---|---|---|
| MAE, 1 week | 2.251 | **2.119** (better in all 3 windows) |
| RMSE, 1 week | **3.025** | 3.039 |
| MAE, 5 weeks | 7.136 | **7.046** |
| Availability AUC, likely starters | 0.549 | **0.727** (GW31–34: 0.487 → 0.819) |
| Squad points, 3 windows | **753** | 704 (−41, −13, +5) |

- **Clean data reproduces the adapter's accuracy profile but not decision value.** The accuracy profile is the familiar shrink (mean delta −0.48, correlation with the baseline −0.66) plus an availability edge in the rotation-heavy GW31–34 stretch. The −49 decision gap is about −1.2 standard deviations at the adapter noise of ~24 points per window. For reference, E19's deltas applied on the fixed pipeline give +30. Neither is distinguishable from zero.
- **The availability edge is not the status leak.** E20's prompts carry no status letters, so the edge is real on the holdout. It has not shown up live, though: the 2026-27 GW2–5 AUC was unchanged with E11-full.
- **Decision:** the adapter stays in shadow and classic + F6 decides. The live promotion rule (rolling four-week availability AUC at least 0.03 above classic) remains the gate. This recipe has now been tried on clean data, so further adapter training on it is not recommended.

### Why E20 forecasts better but picks worse squads (diagnosis 2026-10-06; `reports/review_fixes_2026_10/e20_diagnosis.py`)

1. **It forecasts toward the typical outcome, not the average.** Within every band of the classic forecast, classic matches the mean outcome. E20 sits between the mean and the median. For example, in the top band the mean is 4.58 and the median 3.0: classic says 4.79, E20 says 3.86. Its bias is −0.29 to −0.85 points per game by position, against roughly 0 for classic. Absolute error rewards the median, but squad choices need the mean, and FPL points are right-skewed. This is what greedy decoding of a token-trained model produces.
2. **Its points corrections carry the whole decision loss.** On the holdout (fixed classic+F6 = 753):

   | Variant | Points | vs classic |
   |---|---|---|
   | Points corrections only | 704 | −49 |
   | Uniform per-week shrink only | 752 | −1 |
   | Player-specific remainder | 715 | −38 |
   | Availability corrections only (as the optimizer applies them, threshold-style) | 753 | 0 |

   The captain pick was never better than classic's in any of 12 weeks. The top-11 picks were no better (57.5 vs 57.8 points a week), despite a slightly better rank order in the top 60 (rank correlation 0.237 vs 0.197).
3. **Its availability signal helps when it is allowed to scale points.** Availability rescaling points scored 798 (+45). Relative availability routed into points (the 29 September V3) scored 789 (+36). Both won all three windows, but these are the windows that generated the idea, so a fresh test is running: `scripts/run_e20_live_season_test.sh`, E20 on the unseen 2026-27 GW2–5.
4. **The live shadow adapter is incompatible with the fixed pipeline.** Replaying E11-full's GW2–5 live deltas gives +2 on the pre-fix pipeline but −55 (classic) and −31 (classic+F6) on the fixed one, because its deltas were learned against the old baselines.

**Iteration path.** (a) Use the adapter only as an availability signal routed into points, if the 2026-27 test confirms it; it then goes through the live promotion rule. (b) Fix the cause rather than the symptom: train the next adapter on availability targets only (P(start), P(60+)) and leave points to classic, or decode for the mean (sample and average) instead of greedily. Both need GPU approval.

**Replication of the availability route** (`reports/review_fixes_2026_10/run_avail_replication.sh`). This uses three earlier adapters' out-of-sample predictions on the other 18 windows, on the fixed pipeline:

| Variant | Total over 18 windows | Wins–losses | t |
|---|---|---|---|
| Raw adapter | −104 | 10–8 | −0.87 |
| Availability rescaling points | −107 | 9–9 | −0.85 |
| V3 | +35 | 11–7 | +0.36 |

The +45 on E20's holdout does not carry over, and V3 is within noise. The availability route is unproven, not adopted.

**E20 on the unseen live season** (2026-27 GW2–5, real statuses in the prompts; `scripts/run_e20_live_season_test.sh`):

| | Classic+F6 | E20 |
|---|---|---|
| Squad points | 242 | 247 (+5) |
| Squad points, availability rescaling | — | 238 (−4) |
| Squad points, V3 | — | 238 (−4) |
| MAE, 1 week | 2.237 | 2.155 |
| RMSE, 1 week | 3.086 | 3.151 |
| Bias | −0.21 | −0.65 |
| Availability AUC, likely starters | 0.683 | 0.692 |

The availability edge seen in 2025-26 GW31–34 does not appear early in a live season; E11-full showed the same live. **Conclusion:** this adapter recipe adds no decision value on clean data. The next step is a different formulation, not another run of this one:

1. A proper appearance model plus conditional points on the classic side (review P1-02, CPU). A logistic P(appear) already beat the LLM on AUC.
2. The LLM as an extractor of fresh, near-deadline team news feeding that availability model.
3. Mean-seeking outputs if the LLM keeps forecasting points.

## 8. RL rebuild (G5), 2026-10-08

The deferred RL items (P0-04, P1-07 to P1-10) are now done in a new environment, `src/fpl_ai/grpo_plan_env_v2.py`, with 11 tests. Design and schedule: [docs/rl_g5_rebuild_2026_10.md](rl_g5_rebuild_2026_10.md).

- **Training data:** state caches on the fixed pipeline in `reports/grpo_states_v2/`.
- **Holdout references (closed loop, 2025-26 GW27–38):** same-chips planner 766, classic with no chips 735.
- **Training:** `scripts/run_g5_now.sh`. The first launch (2026-10-08 23:16 PDT) died after two minutes because the longest prompt is 1,687 tokens and the guard was 1,536; the dry run had only counted characters. The guard is now 2,048 and the dry run counts tokens. Training waits on `logs/gpu_hold`, which is cleared when the expectation-decoding inference finishes. It pauses for the GW6 final refresh and resumes from the latest checkpoint.

The second launch ran at 270 s per step, which is 27 hours for 360 steps. The cause was general, not G5-specific.

- **What is slow:** all our adapters are target_parameters LoRA. Unmerged, PEFT re-registers a parametrization on every wrapped weight in every forward call, costing ~1.4 s per call. Generation makes one call per token.
- **Fix for inference:** merge the adapter for inference. Decode steps drop from 1.52 s to 0.16 s, with identical outputs (32/32 GW6 responses for E20 and E11-full; max |dP| 0.0). This now applies in eval_gemma_responses.py, expectation_decode.py, sft_interpret_v2.py and run_grpo_plan_eval.py.
- **Fix for GRPO training:** `merged_generation()` merges only while sampling and restores the base weights bit-exactly from a copy. `tests/gpu_check_merged_generation.py` checks this: same tokens, bit-identical weights, 5.7x faster generation.
- **Relaunch:** 2026-10-09 ~14:00 UTC with the fix. It was still 260 s per step, and a generation check at step 0 showed why. The run would have learned nothing:
  1. **Untemplated prompts.** The prompts were raw text with no chat template. The instruct model wrote five newline-separated objects instead of a JSON array, so **0 of 8** samples parsed. Every sample got the same −5, and GRPO learns only from reward differences within a group. With the chat template, 24 of 24 samples parse and rewards vary.
  2. **Wrong stop token.** TRL replaced Gemma's stop tokens [1, 106, 50] with `<eos>` (1) alone, so samples ran to the 256-token cap repeating `<turn|>`. The tokenizer's eos is now `<turn|>`.
  3. **The flat −5 penalty beat bad valid plans**, which reached −43 at step 0. That would have taught the policy to emit garbage in hard weeks. An unparseable plan now scores 10 below the worst valid plan in its group and below holding all five weeks.
- **Take 3:** `scripts/run_g5_v2.sh`, 2026-10-09 ~15:00 UTC, 3 epochs (180 steps).
  - It shares the GPU with the GW6 final refresh. The trainer runs as `g5_grpo_train.py`, so the E20 chain's GPU wait does not block the refresh.
  - The eval scores both the trained policy and the untrained base (`--adapter-path none`), with the chat template (`load_generator(..., chat_template=True)`).
- **Take 3 verdict (2026-10-10): flat.** Closed loop on the 2025-26 GW27–38 holdout:
  - trained policy 749, untrained 749, with identical decisions in all 12 weeks;
  - same-chips planner 766; classic with no chips 735.
  - Training reward vs the planner by epoch: −17.6, −17.6, −16.8. KL stayed ≤ 0.0016, and 26–33% of groups had zero reward spread, so the policy barely moved.
  - The planner stays the captaincy/chip policy.
- **G5b** (`scripts/run_g5b.sh`, 2026-10-10) repeats take 3 with learning rate 5e-5 and temperature 1.0, nothing else changed.
- **G5b verdict: worse, 731.** That is exactly the planner's 766 minus its two chip plays: G5b never played a chip in the closed loop.
  - Its training reward rose from −14.7 to +5.0 against the planner, through two exploits of the open-loop plan reward:
    - **Procrastination:** it schedules chips in weeks 2–5 of the window. Re-planned each week, it never plays them.
    - **End-of-window dumping:** it puts free hit and wildcard in the window's last week, where nothing after it is counted.
- **Fix: receding-horizon reward, now the default (`receding_value` in `grpo_plan_env_v2.py`, 4 tests).**
  - Only the first action is scored, followed by the same-chips planner re-planned from the state it leaves. This is how the closed-loop evaluation plays: one-step policy improvement over the planner.
  - Chips still held at the window's end are worth 22 (free hit) and 29 (wildcard). These are the 75th percentiles of realised week-1 gains over the 120 training windows (`reports/grpo_states_v2/chip_values.json`); median gains are only +8 and +5.
- **G6** (`scripts/run_after_g5b.sh`): imitation SFT on the planner's plans (480 examples), then GRPO from that adapter with the receding reward (learning rate 5e-5, temperature 1.0, no KL), then the closed-loop evaluation.

## 9. Why the SFT cuts: interpretability (2026-10-09)

**Tool.** `reports/review_fixes_2026_10/sft_interpret_v2.py` reads the exact probability of every `delta_points_1gw` value from −2.0 to +2.0. The adapter writes sign, digit, ".", digit, so this takes one prompt pass plus cached continuations. It then attributes the average with Shapley values over six inputs swapped for neutral versions (64 combinations).

For all eight GW6 players checked, the scored most-likely value equals:
- the live output;
- a fresh batch-1 decode;
- a re-run of the original 16-row batch.

The first version (`sft_interpret.py`) loaded the model differently from the decoder (attention implementation and tokenizer options). Its spreads were wrong, and it is retired.

**Finding: the written delta is not the adapter's belief.** Greedy decoding picks the sign first, then the most likely size of a cut. The chance of a rise (33–50%) is dropped.

| Player | Classic | Written | Expected | P(cut) | Forecast level | Articles |
|---|---|---|---|---|---|---|
| Groß | 6.38 | −1.2 | −0.34 | 65% | −0.49 | +0.06 |
| Rogers | 5.06 | −1.1 | +0.05 | 50% | −0.22 | +0.10 |
| B.Fernandes | 6.15 | −1.1 | −0.22 | 61% | −0.40 | 0 (none) |
| Haaland | 8.15 | −1.1 | −0.54 | 64% | −0.51 | −0.10 |
| De Cuyper | 4.83 | −1.0 | −0.33 | 66% | −0.25 | −0.05 |
| Isak | 3.67 | −0.6 | −0.01 | 59% | −0.21 (status −0.23) | +0.09 |
| Konsa | 2.81 | −0.6 | −0.08 | 67% | +0.04 | −0.12 |
| João Pedro | 2.90 | −0.7 | +0.07 | 62% | −0.11 | +0.04 |

Across these eight, written deltas average −0.92 and expected deltas −0.17.

The articles move the expected value with sensible signs but little size:
- praise pushes it up;
- injury or absence news pulls it down.

The forecast level is the main push down: it learned that high forecasts usually fall short in a typical week. The 3GW and 5GW fields show the same written-vs-expected gap.

**Is it too conservative?** No:
- Training targets are 0.35 × the realised surprise, capped at ±2.
- Undoing the 0.35 makes forecasts worse (scale study, section 7).
- The player-specific part costs 38 squad points on the holdout at its current size.
- Only the availability adjustments are too timid (best at 1.5–2×), and rescaling them has not paid in decisions.

The real distortion is greedy writing, which exaggerates cuts.

**Expectation decoding (2026-10-09).** `scripts/expectation_decode.py` via `scripts/run_expectation_chain.sh` replaces each points delta with the mean of the adapter's own distribution, with no retraining. It ran on the 2025-26 GW27–38 holdout (3,072 rows), 2026-27 GW2–5 (1,024) and GW6 (667).

| Squad points | Classic + F6 | E20 as written | E20 average |
|---|---|---|---|
| Holdout GW27–30 / 31–34 / 35–38 | 266 / 229 / 258 | 225 / 216 / 263 | 224 / 248 / 264 |
| Live 2026-27 GW2–5 | 242 | 247 | 256 |
| Four windows | **995** | 951 | **992** |

| 1-week RMSE (bias) | Classic + F6 | E20 as written | E20 average |
|---|---|---|---|
| Holdout | 3.025 (+0.04) | 3.039 (−0.44) | **2.972 (+0.02)** |
| Live | 3.086 (−0.21) | 3.151 (−0.65) | 3.082 (−0.20) |

Reading the average:
- removes the greedy bias and gives the best 1-week accuracy;
- wins back 41 of the 44 squad points the written deltas lose;
- finishes level with classic.

It is a strict improvement on greedy decoding, but still no evidence of decision value over classic; classic + F6 keeps deciding. The 5GW expectation stays negatively biased (−1.50 on the holdout) because it is conditioned on the greedy text before it.

The weekly side-by-side (`scripts/sft_side_by_side.py --expected-predictions`) now shows the average and a third XI. For GW6 the only difference is the goalkeeper, a coin flip.

Page for Wes: https://claude.ai/artifact/W7V5eyxS4ng6QJkQsyZc6t

## 10. Which articles help, and E21 (2026-10-10)

**Source study** (out of sample: E20 on the 2025-26 holdout plus 2026-27 GW2–5; `reports/review_fixes_2026_10/article_source_value.md`):
- **Mix:** the Guardian supplies 91% of articles and the Premier League site 9%.
- **Points:** articles add little. The SFT's player-specific signal points the right way even with no article (correlation +0.16), and article types differ only within their error bars (team news best at +0.23).
- **Availability:** articles help here. AUC classic → SFT:
  - no article: 0.635 → 0.700
  - Guardian team news: 0.638 → 0.754
  - Scout articles: 0.608 → 0.778
  - price-change articles: worse
  - transfer news: worse

**Timing:**
- The Guardian's team-news piece comes out on Fridays around 17:00 UTC, so 80% of team-news articles fall inside the last 24 hours before the deadline.
- **Late-article test:** removing last-day articles from the 752 affected holdout rows leaves points accuracy unchanged, but cuts the SFT's availability edge from +0.105 to +0.040 AUC. Backtests were crediting the SFT with information live decisions usually lack. Squad points are unaffected: the holdout scores 741 without last-day articles against 736 with them, and live weeks score 256 either way. The SFT's decision value does not depend on late news.

**Scout signal** (`scout_signal.py`):
- Scout-mentioned players beat their classic forecast by +0.33 points a week relative to similar unmentioned players (Scout XI +0.72), over 2022-23 to 2025-26.
- The edge has faded: +0.72 in 2022-23, +0.09 in 2025-26, and −0.11 on the holdout and live weeks. The classic model now prices it in.

**E21** (`scripts/run_e21_clean_focused.sh`): E20's recipe with four changes.
- Articles only up to 12 hours before the deadline, in training and evaluation alike; the live refresh moves to about 12 hours before the deadline to match. A 24-hour cutoff would drop about 95% of team-news pieces.
- Price-change, transfer-trend and transfer-news articles are dropped.
- Team news ranks first.
- The top 96 players per week, so training takes about 20 hours rather than 55.

It is compared with classic + F6 and E20 on accuracy, availability AUC and squad points. Training is queued after G6.

## 11. Nonlinearity, text coverage, and the decision layer (2026-10-10)

**Does classic cover the text?** (`classic_covers_text.md`, 39,936 rows, one season held out at a time)
- **Points:** yes. Keyword signals add nothing in any season (RMSE −0.008 to +0.002).
- **Availability:** mostly. Injury, doubt and suspension words add a small, consistent +0.01 AUC.

**Nonlinearity** (`nonlinear/accuracy.md`, `run_nonlinear_backtest.sh`)
- **Accuracy:** gradient-boosted trees beat the ridge.
  - 1GW RMSE 1.929 vs 1.983; 3GW 3.956 vs 4.048; 5GW 5.801 vs 5.926.
  - Appearance AUC 0.948 vs 0.923.
  - Their top-11 forecasts score 5.376 vs 5.165 real points per player per week.
- **Squad points:** no configuration helps (21 windows, ridge 5,162):

  | Configuration | Squad points |
  |---|---|
  | All heads trees | 5,100 |
  | Trees for 1GW and minutes | 5,114 |
  | Trees for minutes only | 5,149 |

- **Why:** the trees over-predict top players' 3GW/5GW totals (+0.46 / +0.84 top-decile bias), which drive transfers.
- **Decision:** keep the ridge.

**Transfer discipline in the real engine** (`run_transfer_discipline.sh`)
- The engine makes 59 transfers in 84 weeks, thanks to its lookahead.
- Requiring a minimum projected gain of 1 / 2 / 3 / 5 points scores +7 / −21 / −59 / −108.
- It is already well tuned.

**RL decision layer**
- **Bank bug fixed:** the first state of every RL state file carried a spurious £100m bank.
- **Re-evaluated holdout** (2025-26 GW27–38): planner 668, no chips 654, untrained LLM 706, G5 714.
- **Caveat:** the LLM's edge came from holding against a planner that transfers every week. That planner was a strawman; see the sweep above.
- **G7** (chip advisor with priced options plus reasoning) **overfit**: +135 in-sample, −68 held out. Its prompt named the season and gameweek.
- **G7b** fixes this:
  - anonymised prompt;
  - two more seasons of decisions;
  - KL regularisation;
  - a disciplined planner baseline (transfer only when it beats holding by 1 projected point);
  - chips-and-captain-only decisions;
  - two held-out half-seasons.

**RL verdicts (2026-10-11):**
- **G6** (imitation of the planner, then RL, five-week plan format): flat. It scored 656 both after imitation alone and after RL; the planner scored 668.
- **G7b** (chip and captain advisor, anonymised prompt, disciplined planner, KL regularisation) reached parity with the planner on two unseen half-seasons, with no overfitting:
  - 2025-26 GW20–38: 1,243 vs 1,206.
  - 2023-24 GW20–38: 1,157 vs 1,189.
  - Total: 2,400 vs 2,395. The untrained advisor scored 2,330.
- **Behaviour:** G7b plays Triple Captain and Bench Boost early in the half, like the planner. It still spends Free Hit and Wildcard every half, around GW24–26.
- **Noise:** chip timing swings about ±70 points per half-season. A real edge of +20 per half would need about ten held-out halves to show.
