# Programme 2026-10-17: after the LLM runs (approved by Wes 10-17: "go ahead, no need to wait")

Order: 6 (instrument) → 1 (scoring regime) ∥ 2 (double-gameweek engine) → 3 (free-transfer banking + multi-week
plan) → 4 (set-piece duties) → 5 (autosub-aware bench). All CPU. Every item is reported on realised points AND
expected points (xPts) from item 6. Memory: `fpl-programme-2026-10-17`.

## Item 6 — expected-points scoring of the decision bench (done 2026-10-17 22:40)

Tools: `scripts/build_xpts_table.py` → `data/xpts_table.csv` (114,151 player-weeks, 2022-23 … 2026-27 GW6, from the
per-fixture `data/fpl_history/<season>/merged_gw.csv`); `scripts/xpts_rescore.py --baseline <prefix> --test <prefix>…`
replays every window's weeks exactly as `backtest.py` scores them (realised starters after autosubs, effective captain,
bench boost, triple captain, hits) on two point tables. Outputs `reports/xpts/summary.md`, `<label>_windows.csv`,
`<label>_weeks.csv`.

Definition: xPts replaces the four luck-dominated components with their expectation from the match stats and keeps
the rest realised: goals → xG × goal value, assists → xA × 3, clean sheet → exp(−xGC) × CS value when ≥ 60 minutes,
goals-conceded penalty → E[⌊GC/2⌋] under Poisson(xGC); appearance, bonus, saves, cards, own goals, penalties and
DefCon stay as they happened. Player-week level: corr(actual, xPts) 0.86–0.88, sd 2.39 → 2.01.

Validation: the replay reproduces every `actual_score` in 2,682 weeks over four bench families (0 mismatches); the
table's realised points equal the files' (0 mismatches); 39 missing player-weeks in ~40,000 (fallback to realised).

| family (baseline) | window pairs | sd of Δ per window, actual | xPts | ratio | corr(Δactual, Δxpts) |
|---|---|---|---|---|---|
| status-table experiments (ST1_F) | 210 | 15.5 | 9.3 | 0.60 | 0.79 |
| H3 availability arms (10 windows) | 50 | 10.6 | 6.7 | 0.63 | 0.81 |
| DGW / market, drafter variants (MP1_F) | 231 | 19.1 | 15.8 | 0.83 | 0.84 |
| review fixes (O_F) | 105 | 18.9 | 16.0 | 0.85 | 0.80 |

Feature experiments share most picks, so the finishing noise of the few players that differ is what xPts removes:
a 40% cut in sd, worth 2.8× the windows. Over 21 windows the 95% bar drops from ~142 to ~85 points. Engine/drafter
variants (per-fixture horizons, beam vs MILP drafts) change many players and keep more variance.

Re-reads of past verdicts (Δ vs baseline over 21 windows, actual → xPts):

| experiment | actual | xPts | reading |
|---|---|---|---|
| per-fixture 1GW fix, MILP draft (MP1_F vs MN_F) | +79 | +50 (t 1.7) | holds |
| full per-fixture 3GW/5GW horizons (MP_F vs MP1_F) | −84 | +32 (t 0.8) | the "−5/21" loss was luck; positive, unproven |
| same, beam draft (P1_F vs MP1_F) | +38 | +132 (t 1.2) | |
| hits allowed (HT2_F vs ST1_F) | +6 | +42 (t 1.4) | hit rule earns a little on xPts |
| review fixes, F6 (N_F vs O_F) | +191 (t 1.5) | +145 (t 1.3) | holds |
| review fixes, classic (N_C vs O_F) | +117 | +134 (t 1.65) | holds |
| depth chart (DC1_F) | −182 (t −2.2) | −70 (t −1.4) | half the loss was luck; still negative |
| per-position suites (PP1/PP2/AP2) | −142 … −179 | −78 … −101 | still negative |
| market odds (MK1_F / MKN_F vs MP1_F) | −32 / −163 | +35 / −8 | null either way |
| H3 availability arms vs classic | −1 … −29 | −9 … −22 | flat either way |

Caveat: xPts credits no finishing skill, so a configuration that holds consistent over-performers (Salah, Haaland)
reads lower on xPts than its true expectation. The "luck" column (actual − xPts) is +171 for MP1_F and +55 for
MP_F over the same 21 windows: the full per-fixture variant holds premiums less, and part of that gap is skill, not
luck. Rule: report both; a disagreement between the two metrics is a flag, not a verdict. A shrunken per-player
finishing adjustment is the follow-up inside item 2.

Correction to the 10-17 plan note: the 21 windows do contain the double and blank weeks (10 of 13 DGW weeks and
11 of 12 BGW weeks of 2023-26 fall inside them). The disagreement between −5/21 windows and +331/12 closed-loop
halves was realised-points noise plus the compounding of 19-week closed-loop halves over six seasons, not window
coverage.

## Item 1 — scoring-regime alignment (done 2026-10-17 22:30): NULL

Code (default off): `FPL_REGIME_TERM=1|pos` adds position dummies (GK reference) and DefCon-regime × position crosses
(`dataset.add_regime_columns`, REGIME_FEATURES); `FPL_RECENCY_HALFLIFE=<seasons>` down-weights older seasons in the
ridge (`RidgeRegressor._recency_weights`). Bench `scripts/run_regime_backtests.sh` → `reports/regime/`, 9-second
windows, 111 runs; scored by `xpts_rescore.py` (`reports/regime/summary.md`).

Mechanism check (`scripts/regime_accuracy_check.py`, walk-forward 1GW forecasts on the nine 2025-26 windows):
the baseline's position bias is already small because the rolling form features carry the new regime (predicted
starters: DEF −0.08, MID +0.09, FWD +0.11, GK −0.49); the regime term levels DEF/MID to +0.02/0.00 and changes
RMSE by −0.002. The 0.8-point DEF shift in the raw per-90 means was not a model error. The one real residual is
goalkeepers: predicted starters score 3.24 and are forecast 2.75 under every variant (ranking among GKs unaffected).

| config (vs ST1_F, 21 windows) | Δ actual | Δ xPts (t) | Δ xPts+skill | live GW2-6 Δ actual / xPts |
|---|---|---|---|---|
| RP_F position dummies only | −122 | −80 (−1.5) | −90 | +27 / +19 |
| RG1_F dummies + regime crosses | −106 | −68 (−1.35) | −78 | +27 / +19 |
| RW1_F recency half-life 1 season | −128 | −54 (−1.0) | −65 | +14 / +8 |
| RW2_F half-life 2 seasons | −48 | −18 (−0.5) | −27 | 0 / 0 |
| RGW_F regime + half-life 2 | −11 | +32 (+1.05) | +20 | +17 / +16 |

Lineups keep the same formation and captains; the configs reshuffle a few picks within positions and those
realise less. Nothing approaches the 85-point xPts bar; the flags stay in the code, off. Lesson for the list: the
ridge's form features already track scoring-rule changes within a season, so regime terms are not where the
points are.

## Item 3 quick test (2026-10-17 22:22): raising the banked free-transfer cap alone changes nothing

`--max-free-transfers 5` (HB5_F) on the 15 windows of 2024-25 and 2025-26 (the seasons with the 5-transfer rule)
reproduces ST1_F's squads and scores exactly (Δ 0 on every window): the engine's one-step lookahead never plans a
bank beyond two, so it rolls to three only incidentally (13 of 60 weeks) and then makes the same single move. The
cap is now correct to pass for live seasons, but any value from banking needs the multi-week plan (rolling-horizon
MILP with free-transfer state), which is the real item 3 and is deferred behind item 2.

## Item 5 measurement (2026-10-17): the bench is under-credited, but only the first sub matters

Across the 21 ST1_F windows (63 non-boost weeks) the first outfield bench player comes on in 33% of weeks (2.7
points when he does), the second in 6%, the third never; 17.9% of bench outfield points reach the score, against the
MILP's flat 10% credit for every outfield bench player. The right objective credits ~0.33 × value to the best bench
outfielder, ~0.06 to the next and nothing to the third (an at-most-one "first sub" binary per bench player in
`squad_milp.optimize`). Expected gain ≈ 0.3–0.5 points a week, below the 85-point bar but noise-free logic; queued
after item 2.

## Instrument calibration (2026-10-17 22:40) and item 2 verdict

Decomposing actual − xPts by component over the 84 bench weeks showed two league-wide biases common to every
configuration: FPL assists realise at 1.3–2.1× the xA-based expectation (penalties won, rebounds and own-goal
assists are assists but not xA) and clean sheets at 0.7–0.8× exp(−xGC); goals and goals-conceded are ~1.0.
`build_xpts_table.py` now scales each expected component by the season-position ratio of realised to expected
points (`calibrate_components`), so xPts is unbiased per season (mean = actual) and the "luck" column means luck.
Noise reductions and every verdict above are unchanged (feature and decision-variant families sd ratio 0.59–0.63,
drafter/engine families 0.84–0.88).

**Item 2 — per-fixture 3GW/5GW horizons and the terminal-value horizon: unresolved, not shipped.**
`PlayerForecast.rate_5gw` + `DecisionWeights.terminal_fixtures` (`--decision-variant 3gw_t3 | 3gw_t6 | blend5_t3`)
credit fixtures beyond the transfer window so a single blank no longer removes a third of a player's value.
Bench `scripts/run_horizon_backtests.sh` → `reports/horizon/` (vs MP1_F, the ship candidate, 21 windows):

| config | Δ actual | Δ xPts (t) | Δ xPts+skill |
|---|---|---|---|
| MP_F full per-fixture horizons | −84 | +32 (+0.84) | +32 |
| MPT3_F / MPT6_F (+ terminal 3 / 6 fixtures) | −120 / −119 | −4 / +17 | −6 / +11 |
| MPB5T3_F (blend5 + terminal 3) | −156 | −6 | −11 |
| MP1T3_F / MP1T6_F (terminal value on MP1_F) | +46 / −20 | +16 / −3 | +20 / −6 |

The terminal value does not help, and the full per-fixture variant's gap between actual (−84) and xPts (+32) sits
entirely in the goals component: the players MP1_F holds out-scored their xG by +50 points over the 84 weeks, the
full variant's by −41, with identical prior finishing skill (+304 vs +305). That is either luck or short-run
finishing persistence that neither metric credits (F8 found over-performance does not mean-revert quickly). With
the closed-loop halves at +331 on realised points and the windows at −84, the honest state is unresolved; MP1_F
stays the ship candidate and the full variant stays a candidate to resolve with a longer realised-points bench.

## Item 5 — bench credit in the weekly evaluation (2026-10-17 22:30): negligible, closed

`FPL_BENCH_WEIGHTS="gk,sub1,sub2,sub3"` (decision.py `_bench_weights`, default = legacy 0.05/0.12/0.06/0.04) with
the measured usage 0.05/0.33/0.06/0.0 (SB1_F) changes 3 of 84 weeks' decisions: +3 actual / +6 xPts over 21 windows,
identical autosubs (26, 72 points) and bench spend. A softer 0.05/0.25/0.08/0.02 (SB2_F) reproduces the baseline
exactly. Transfers are decided on starter value; the bench credit is not a lever. Flag kept, default off.

## Item 4 — weekly set-piece duties (2026-10-17 22:35): NULL

`backfill_history_status_from_vaastav.py --setpiece --out-name weekly_setpiece.csv` replays the pre-deadline
snapshots for penalty, corner and direct free-kick order (columns exist from 2020-21; 2025-26 has snapshots for 13
of 38 weeks, forward-filled; ~20 first-choice takers per week, 8–12 penalty-taker changes a season).
`scripts/add_setpiece_features.py` writes pen_taker / pen_order_inv / corner_taker / fk_taker / setpiece_score into
`data/fpl_training_rows_v3_contract_f6_setpiece.csv`. Penalty takers score 4.94 a start against 3.54 for other
starters, but the ridge gives the five columns standardised coefficients of ±0.02 (ranks 54–78 of 80): the gap is
already carried by ICT, threat and xGI. Bench SP1_F vs ST1_F: −56 actual, −16 xPts (t −0.3), 6 windows won / 7 lost.
Closed; the table and flags stay for reference.

## Where the programme stands (2026-10-17 22:40)

| item | result |
|---|---|
| 6 instrument | DONE: xPts bench, replay-validated, calibrated per component; sd per window 15.5 → 9.3 on feature experiments |
| 1 scoring regime | NULL: residual position bias ±0.1, decisions −65 xPts; form features already carry the regime |
| 2 DGW horizon | unresolved: full per-fixture +32 xPts / −84 actual (goals component), terminal value null; MP1_F stays |
| 3 FT banking | cap alone changes nothing (one-step lookahead never banks); multi-week MILP deferred |
| 4 set-piece duties | NULL: −16 xPts, coefficients ±0.02 |
| 5 bench credit | negligible: +6 xPts |

Two things changed for good: the decision bench now runs a 4-week window in 9 seconds (a 21-window experiment is a
3-minute job, not an afternoon), and every past and future verdict can be read on realised and expected points
side by side. The classic pipeline's remaining ideas (per-position, regime, set pieces, bench value, horizon length)
have all been tested within the noise; the forecaster is close to the information in its inputs, and the open
question that could still move points is the long-horizon transfer plan around doubles and blanks (item 3 proper)
read on realised points over the closed-loop halves.

## 2026-10-18 — Wes: "better scale": the SFT article audit

`scripts/sft_article_audit.py` → `reports/sft_article_audit/summary.md` (rows.csv, docs.csv). Headline: the text is
stale (newest doc 64 h old at the median, 10% within 24 h), 83% Guardian with 56% live-blog match reports of the
previous match, 1.6 snippets of 265 characters per row, and NOT actionable: on nailed starters whose flag said
available and who then did not play, a document naming them with an availability cue was present 38% of the time
versus 34% when they played the full match. Information ceiling of a perfect pre-deadline availability feed ≈ 1
point a week. Full verdict in the audit summary. Consequence: no E4B rerun on this text (it would reproduce H1);
the 31B run goes ahead as a capacity test on the same corpus under the memory rule (QLoRA 4-bit).

### H31 status 2026-10-21 09:15 PDT (checkpoint before a possible power cut at 14:30)

Training finished at 09:03 after 71.5 h (840 steps of batch 1 × accum 16, 306 s/step, 25.9 GB torch peak, no memory
incident). Adapter `artifacts/gemma4_31b_h31_reghead_e22` (r16/α32 on q/k/v/o/gate/up/down of all 60 layers,
head 5376→5, 490 MB), checksums in `artifacts/gemma4_31b_h31_reghead_e22.md5`, read-only copy with the training log in
`~/fpl_freeze/2026-10-21_h31_adapter/`. Training loss over the last 100 steps: regression 1.46, appearance 0.23 (mean of the logged steps ≥ 740),
against H1's 1.40 / 0.21 on the same rows and schedule — the larger model did not fit the residual targets any
tighter. The chain then started the predictions (1,152 holdout + 480 live rows at ~4 s/row), followed by the ledgers,
the four decision windows and the xPts re-score; expected done around noon. Everything the chain writes is
skip-guarded, so after a power loss the same script resumes from the last finished file (see the memory note
`fpl-scale-runs-2026-10-18` for the resume command). Comparison: `scripts/h_series_compare.py h1 h31`.

### H31 result (chain done 2026-10-21 12:09 PDT): capacity was not the constraint

Same recipe, corpus, split, ledgers, decision windows and scoring as H1; the only change is the backbone,
Gemma-4-E4B → Gemma-4-31B-it loaded in nf4. Every accuracy number below is recomputed on identical rows by
`scripts/h_series_compare.py h1 h31` (`reports/h_series/h31_vs_h1.md`); chain log `logs/h31_chain.log`; frozen copy
of adapter and results in `~/fpl_freeze/2026-10-21_h31_adapter/`.

**Points: the same constant shrink, read by a model ten times the size.**

| 1GW points | classic | H1 (E4B) | H31 (31B) |
|---|---|---|---|
| holdout RMSE 1GW / 3GW / 5GW (1,152 rows) | 3.420 / 6.807 / 10.035 | 3.419 / 6.737 / 9.922 | 3.415 / 6.768 / 9.983 |
| holdout MAE / bias | 2.609 / +0.10 | 2.557 / −0.15 | 2.561 / −0.09 |
| live RMSE / MAE / bias (480 rows) | 3.424 / 2.614 / −0.23 | 3.441 / 2.568 / −0.47 | 3.441 / 2.580 / −0.42 |
| delta mean / sd (holdout) | | −0.25 / 0.11 | −0.19 / 0.07 |
| corr(delta, classic residual) holdout / live | | +0.04 / +0.09 | +0.07 / +0.03 |
| RMSE with the mean shift only vs the full read (holdout) | | 3.421 vs 3.419 | 3.420 vs 3.415 |

Both heads subtract about a fifth of a point from everyone; the row-level variation around that shift is tiny (sd
0.07–0.11), is worth 0.001–0.005 RMSE, and the two arms' variations barely agree with each other (correlation 0.30
holdout, 0.35 live; H31 lands nearer the actual than H1 on 53–54% of rows, a coin flip). The MAE gain and the "closer
on 61–62% of rows" are the median effect already documented for H1: shifting a right-skewed target down lands nearer
the mode. The 31B shrinks less and more uniformly; it did not find row-level signal E4B had missed.

**Availability: the extra capacity went into the base rate, not into reading.**

| appearance | classic | H1 (E4B) | H31 (31B) |
|---|---|---|---|
| holdout AUC all / uncertain rows (914) | 0.704 / 0.574 | 0.771 / 0.706 | 0.739 / 0.644 |
| holdout Brier all / uncertain | 0.0767 / 0.0851 | 0.0604 / 0.0646 | 0.0597 / 0.0632 |
| live AUC all / uncertain (395) | 0.645 / 0.701 | 0.760 / 0.855 | 0.682 / 0.755 |
| live Brier all / uncertain | 0.0444 / 0.0490 | 0.0252 / 0.0257 | 0.0235 / 0.0236 |
| mean ΔP on uncertain rows, holdout / live | | +0.077 / +0.088 | +0.128 / +0.121 |
| sd of ΔP on uncertain rows | | 0.069 / 0.080 | 0.062 / 0.058 |

H31's Brier is marginally better than H1's (−0.0007 holdout, −0.0017 live) and its ranking is clearly worse (AUC
−0.03 holdout, −0.08 live; −0.06 and −0.10 on the uncertain rows). Its probability shifts are larger and less
dispersed: it pushes everyone towards the 90–97% base rate, which is exactly what the Platt fit of the classic
probability does (with-text uncertain rows, holdout Brier: classic 0.0888, Platt 0.0710, H1 0.0676, H31 0.0670;
live: 0.0502, 0.0245, 0.0250, 0.0253). The 31B learned the calibration defect better and the text worse. The two
arms' ΔP correlate 0.75 / 0.69, so the part they share is the status/news fields already shown to carry the
availability signal, not anything new in the articles.

**Decisions: a tie with the classic pipeline.**

| window | classic actual / xPts | H1 | H31 |
|---|---|---|---|
| 2025-26 GW27-30 | 281 / 249 | 246 / 232 | 248 / 237 |
| 2025-26 GW31-34 | 254 / 229 | 237 / 215 | 254 / 229 (identical squads) |
| 2025-26 GW35-38 | 253 / 229 | 267 / 229 | 270 / 234 |
| 2026-27 GW2-6 (live) | 315 / 280 | 335 / 288 | 351 / 291 |
| total (Δ vs classic, t) | 1,103 / 987 | 1,085 / 964 (−18, t −0.35 / −23, t −0.93) | 1,123 / 991 (+20, t +0.34 / +4, t +0.22) |

Realised sd per window 26–29, xPts sd 10–12: neither arm is distinguishable from the classic pipeline, and on
expected points the H31 arm's squads are the classic squads (+4 over 17 weeks; one window literally identical).
The live-window +36 realised is the +11 xPts plus luck. Nothing here reaches the +100 gate set for H3.

**Cost.** Training 71.5 h against 6.6 h (10.8×, 306 vs 28 s/step); inference 6.3 s/row unmerged on the 4-bit base
against 0.7 s/row for the merged E4B (9×); the load transient reached 80 GB system memory against ~20 GB, so a
31B read cannot share the box with anything. No memory incident; the watchdog never fired.

**Verdict.** Model capacity is not the constraint and the scale line is closed: Gemma-4-E4B stays (decision in
`docs/iteration_plan_2026_10_15.md` §7.4, now confirmed by the direct test), no 12B or 31B retrain on this corpus.
Together with the article audit the picture is consistent: the reader has nothing to read. The 31B reproduced the
E4B's two findings, a decision-inert constant shrink on points and a Platt-level recalibration on availability,
and did not add a row-level signal. The text line reopens only with a different input, a genuine pre-deadline
team-news feed, whose ceiling the audit put at about one point a week. The remaining classic lever is unchanged:
the multi-week transfer plan around doubles and blanks (item 3 proper).

### GW7 settled (ledger 2026-10-21, `reports/gw7_packet_2026_10/final/ledger_gw7.md`)

68 gross / 64 net of the −4 (Isak → Haaland, B.Fernandes → McGinn) against an average of 59; overall rank 3.88M →
3.72M. Haaland (captain) 13 vs Isak 9 paid for the hit; McGinn 1 vs Bruno 1 was a wash; Cherki 0 minutes with no
warning in either pipeline. Classic XI = entered = 68; the SFT XI's one specific call (McGinn over Evanilson) was
−11 and was rescued by the Cherki auto-sub. Weekly ingest for GW7 ran clean (flagged rate 0.208).
H1 shadow accuracy on GW7 (667 players): RMSE 1.995 classic vs 2.028 SFT, bias −0.02 vs −0.35; decision-relevant
rows 3.673 vs 3.643. Weekly data steps done 10-21: ingest, cutoff → GW7, both production tables rebuilt (+668 GW7
rows, backups in `data/backup_2026_10_21/`), GW8 parity audit in `reports/gw8_packet_2026_10/parity_audit.md`.
Rebuild note: the F6 table now carries `chance_of_playing` (127 columns, was 126; the classic table is unchanged at
121). It is not in SAFE_FEATURE_COLUMNS, so the production ridge ignores it unless FPL_CHANCE_FEAT=1 (tested null
10-14). GW8 parity audit: 24 flags, all the known ones (DefCon columns absent in 2023-25 history; live status flag
share 30% against 12% in the reconstructed history, same as GW7's audit; 106 of the 203 flagged live players are
'u', not in a squad).

### GW8 interim (2026-10-21 18:30 PDT, after Saka's injury at Bayern)

Saka went off after 10 minutes with a thigh-muscle injury; Arteta: "a number of weeks", scans pending; the FPL feed
shows d / 50% as of 20:30 UTC. The classic sheet on the feed as-is (`reports/gw8_packet_2026_10/interim_1021/`)
still prices him at P(appear) 0.76 and would only move Cunha → Rogers (+9.2); the Saka-out scenario
(`interim_1021_saka_out/`, his forecasts zeroed over GW8-12) is the sheet that matters: Saka → Rogers free +12.6
(bank 1.7), Konsa+Saka → Calafiori+Rogers −4 +17.1 net, wildcard +15.1 (below the free move), free hit +5.4.
Recommendation: Saka → Rogers, captain Haaland, no chip; keep Konsa → Calafiori for the GW9 free transfer rather than
pay the hit for a +4.5 margin over five weeks. Interim H1 side-by-side: `scripts/run_gw8_interim_sft.sh` (E4B read,
sheets `side_by_side_h1_saka_rogers.md` / `_hold.md`). Final refresh armed for Friday 07:00 PDT
(`scripts/run_gw8_final_refresh.sh`, pid in `logs/pids/gw8_final_refresh.pid`); its GPU step runs only if
`logs/gw8_gpu_ok` exists.

## Konsa case, 2026-10-21 22:50 PDT: does fine-tuning fix a new signing's minutes?

Wes's challenge: Konsa (new Arsenal signing) had 0 and 11 minutes in GW1-2, then started GW3-7 (five 90s), and the
classic model still forecasts 73 minutes / P(app) 0.81 / 3.23 GW points for GW8, which benched him. He expected the
fine-tuned reader to know he is now nailed. Everything below is from reads already on disk plus CPU runs; no GPU.

**The adapters' reads of Konsa, every week, split into the generic recalibration (quadratic fit of delta on the
classic P across the week's rows) and the player-specific remainder (with the sd of that remainder in his band):**

| week | read | classic P(app) | delta | generic | specific | band sd | what happened |
|---|---|---|---|---|---|---|---|
| GW3 | E11-full written | 0.165 | −0.06 | +0.04 | **−0.10** | 0.107 | first start, 90 min |
| GW3 | H3 head | 0.158 | +0.19 | +0.16 | +0.04 | 0.129 | |
| GW4 | E11-full / H3 | 0.55 / 0.66 | +0.16 / +0.25 | +0.09 / +0.22 | +0.07 / +0.03 | 0.074 / 0.080 | 90 min |
| GW5 | E11-full / H3 | 0.74 / 0.63 | +0.09 / +0.25 | +0.08 / +0.19 | +0.01 / +0.06 | 0.043 / 0.125 | 90 min |
| GW6 | E11-full / H3 | 0.72 / 0.73 | +0.10 / +0.08 | +0.06 / +0.16 | +0.04 / −0.08 | 0.072 / 0.087 | 90 min |
| GW7 | H1 head | 0.80 | +0.15 | | points specific −0.03 | | 90 min, 9 pts |
| GW8 | H1 head | 0.81 | +0.13 | +0.11 | +0.02 | 0.026 | points 3.23 → 2.93 (generic −0.21, specific −0.08) |

No week singles him out beyond one band sd; at the moment of the role change (GW3) the written-delta adapter moved him
down. The GW8 lift to 0.94 is the head's generic curve (the classic P is a minutes share; the Platt fit says a classic
0.81 means 0.94 played), so the coupling route (`avail_couple_preds.py`) multiplies his points by 0.940/0.942 = 1.00
(3.22) while N.Williams becomes 3.29. The XI in the side-by-side is picked on points, where the head is a constant
shrink. No route from the fine-tuned reads moves Konsa into the XI.

**Why the text did not carry it.** `attach_player_evidence_to_corpus.py` keeps at most two documents per player,
ranked by mention count (3 × title + content hits) with recency only as a tiebreak. Konsa's prompts therefore got
match-blog play-by-play every week (GW3: a PL "triple up on Arsenal" piece and "Villa fans bid farewell"; GW4-5 the
Chelsea and Sunderland blogs; GW7 the Leeds blog and Croatia 0-7 England; GW8 "Konsa bullish …" with 18 mentions and
the Forest blog). The role statements were in the stores and lost the ranking: 09-03 "buying Ezri Konsa to cover the
long-term absence of William Saliba"; 08-28 predicted lineups (Konsa among the subs, Saliba back, unknown); 09-15
Scout "Gabriel, Calafiori and new signing Ezri Konsa are the safest picks for now"; 10-12 "Gabriel … likely to be
partnered by Ezri Konsa again … Saliba: still talking about weeks"; 10-16 predicted lineups. Attaching them is a
cheap fix, but E17 already showed the written-delta adapter ignores a structured depth-chart block (partial corr
−0.03) and the H heads' availability edge sits on status-flagged/news rows only (`fpl-h3-avail-head`).

**What the classic model is doing is the population answer.** Production table, status-a rows (146,500):

| cell | n | played | minutes | started (≥ 60) | pts |
|---|---|---|---|---|---|
| 3 straight starts, 8-week minutes avg ≥ 85 | 8,208 | 0.942 | 81.9 | 0.894 | 3.30 |
| 3 straight starts, 8-week avg 55-75 (Konsa: 66) | 4,092 | 0.904 | 70.1 | 0.750 | 3.00 |
| 5 straight starts, all 90s, 8-week avg 55-75 | 555 | 0.892 | 76.7 | 0.814 | 2.86 |

His 72.9 minutes / 0.81 / 3.23 is what his cell does. Splitting the cell by signing class (club change in the PL vs
same club vs no prior PL rows) moves the next-week play rate by under 0.01 in weeks ≤ 12 (0.922 vs 0.916) and by
+4 minutes in the "missed an early week, now on a streak, weeks 5-10" path (76.6 vs 72.8, n 173 vs 218); a
positional rival being unavailable (F7 table) moves it by 2 minutes (70.5 vs 68.7). The structured data cannot tell
"new signing, now nailed" from "rotation player on a streak"; that is a judgment call.

**What the call is worth (counterfactual).** Scratch history root with Konsa's GW1-2 rows removed, same fitted
suite, same snapshot (21 s on CPU): GW 3.23 → 3.46, 3GW 8.85 → 9.68, 5GW 14.19 → 15.77, minutes 72.9 → 80.1,
P(app) 0.81 → 0.89; DEF rank 29 → 19 on GW points, 34 → 18 on 5GW; no other player moves. That flips the marginal
pick: Konsa into the XI for N.Williams (57.2 → 57.3), the same call Wes made. Cunha is a different case (0.56 share
from cameos, no start streak) and is not caught by the rule.

**Tool.** `scripts/role_override_sheet.py` (CPU, ~40 s): `--auto` flags squad players who started each of the last
three weeks with an 8-week minutes average under 75 and status a, re-forecasts them with history restarted at the
first start of the run, prints the standard and "if nailed" XIs, and writes a packet-shaped forecast jsonl so
decide/milp_routes/route_lineups can be re-run on it. GW8 interim output: `reports/gw8_packet_2026_10/interim_1021/
role_override_sheet.md` and `forecasts_role_override.jsonl`. Run it by hand after Friday's refresh (the refresh script
is executing and must not be edited). The GW9 Konsa → Calafiori plan was valued on the standard forecast; under
"if nailed" Konsa's 5GW is +1.6, so re-run milp_routes on the override jsonl before taking it.

**Also fixed:** the GW8 packet's `forecast.py` (cloned from GW7) trained as-of GW6, i.e. on rows strictly before GW6;
now as-of 8 (through GW7). Effect on GW8 forecasts: mean −0.001, sd 0.008, max 0.04 points.

**Where this leaves the LLM question:** the reader has never read a role for Konsa, the text that states the role
never reached its prompt, and when a role block was put in the prompt (E17) it was ignored. Ranked proposal: (1) keep
the override sheet as the weekly instrument, the model's arithmetic plus the manager's role knowledge; (2) the
attachment re-ranking (role lexicon and predicted-lineup paragraphs above mention counts) only as part of a head
retrain whose target is points per start, because availability alone is decision-inert; (3) a club-tenure feature for
the ridge is worth ~4 minutes in one slice and would likely sit inside the 21-window noise.

## F16 Guardian team news, 2026-10-21 23:30 PDT: the first extractor, measured

Wes's follow-up to the Konsa case: "we haven't let the SFT read enough … the path to scale that? … go back to the 4B
model but really expand the articles (number and length)". Before answering, measured what the stores hold and what
one article type is worth when read properly.

**What the stores hold.** Guardian full text 2022-23..2025-26: 25,852 docs, median 4.8k chars (p90 14k); PL Scout
2022-26: 2,808 docs, median 3.2k chars. The SFT sees 1.6 snippets × 265 chars per row = ~2% of one article, chosen by
mention count. On 2025-26 uncertain rows, a role-cue sentence within 72 h of the deadline exists in the full store
for 48% of surprise starts (classic P < 0.5, played 60+) vs 41% of other rows; the weekly "Premier League team news:
predicted lineups" article accounts for most of it (37% vs 30%).

**The article is list-shaped and parseable** ("Subs from … Doubtful … Injured … Suspended …" per team; a squad player
not named is the implied XI), one per gameweek (32-35/season), published a median 17 h before the deadline (88-94%
within 24 h). `scripts/build_team_news_table.py` parses 2022-23..2026-27 (team-week coverage 589/579/597/534 of 760,
65 so far this season; 85% of listed names matched) and writes gn_article/gn_xi/gn_sub/gn_doubtful/gn_out onto
`data/fpl_training_rows_v3_contract_f6_teamnews.csv`; `FPL_TEAM_NEWS_FEATS=1` adds them to the ridge
(`dataset.get_feature_columns`), `FPL_TEAM_NEWS_OVERRIDE=1|minutes` applies them multiplicatively (`models.py`).

**Information (2025-26 uncertain rows, next-week started ≥ 60 min):**

| classic P band | implied XI | named sub | doubtful | injured | suspended |
|---|---|---|---|---|---|
| < 0.5 | 0.354 (n 1,321) | 0.200 (1,686) | 0.228 (184) | 0.008 (257) | 0.000 (54) |
| 0.5-0.8 | 0.750 (2,226) | 0.497 (380) | 0.457 (70) | 0.000 (59) | 0.000 (28) |
| ≥ 0.8 | 0.913 (1,970) | 0.717 (46) | 0.500 (22) | 0.000 (7) | 0.000 (11) |

Surprise starts were implied-XI 55% of the time vs 32% for low-P non-starts. Pooled 2022-26, players with a real
chance of starting (minutes_avg_5 ≥ 30): named sub = 0.65 × the implied XI's points and 0.6 × minutes, doubtful
0.6 / 0.5, injured or suspended 0.03 / 0.03. The classic ridge, given the columns, moves a named sub by only +7
minutes / +0.22 points relative to the implied XI and leaves an injured player at 9 forecast minutes (realised 0.1).

**Decisions, 21-window bench, control = same table with nothing on (`reports/team_news_f16/backtest.md`, `xpts/`):**

| arm | actual Δ | t | xPts Δ | t | W/T/L |
|---|---|---|---|---|---|
| TN1 ridge term | +31 | 1.35 | +33 | 1.61 | 4/14/3 |
| TN2 ridge + multiplicative override (minutes and points) | −5 | −0.08 | −2 | −0.04 | 7/7/7 |
| TN3 ridge + override on minutes only | +24 | 1.27 | +13 | 0.85 | 5/13/3 |
| TN4 override only | −36 | −0.64 | −24 | −0.54 | 6/8/7 |

The additive ridge term is the right use: positive on both instruments, same size as F6's realised gain, 14 ties
(it changes a few picks, not the squad). The strong structural use is null to negative: the Guardian's own error
rate (half the regulars it names as subs start) makes a 0.65 override worse than a nudge, and the sd of the window
diffs triples. Ship candidate at zero training cost, pending live parity: the live frame must carry the parsed
categories (the Friday 14:00 UTC refresh precedes the article at ~17:00 UTC; Saturday-deadline weeks, 24 of 38 this
season, need a Friday-evening pass; Friday-deadline weeks get gn_article = 0, a state 30% of training team-weeks share).

**What this says about scaling the reader.** The informative text is list-shaped, sparse, and late; it is best read
once by an extractor into facts, and the facts are worth a few points per window on decisions through the minutes
axis. Raw length and count of snippets in the SFT prompt (E14 3×700, E15 5 docs + multi-window, E8 podcasts, the
June 31B full-text 2k/4k/8k runs that never finished) were never going to find two sentences in a 5k-char article by
mention count. Path: extractors over the full stores (deterministic for lists; E4B or an API model for press-conference
prose, ~4k injury/team-news docs for 2022-26 ≈ 9 h GPU or ~$15 API; the whole store 26k docs ≈ 2.5 days GPU or
~$60) → per-player-week facts → ridge features (bench in minutes) and a ≤ 300-token team sheet in the SFT prompt →
one H-recipe retrain on E4B with a surprise-row mechanism check before any decision bench.

## Extractor pilot, 2026-10-23 01:00 PDT: Gemma-4-31B-it vs E4B-it vs Haiku on 90 documents

Wes (10-22): "instead of calling APIs since it's non zero cost, can you just load my Gemma 31B model (no SFT) to get
the extraction you need? of course pls compare using some maybe 10-100 examples against Haiku models; anyway, you
have my permission to proceed w the plan." Everything below runs on the box; Haiku = Claude Code subagents (no API
key or package here, zero API cost; workers need explicit filenames, see memory fpl-haiku-subagent-extraction).

**Set-up.** `scripts/build_extract_docs.py` routes the Guardian 2022-27 + Scout stores into 3,716 prose documents
(club-tagged, not live blogs or women's football, title/standfirst/lead availability cues; classes avail 2,291 /
role 1,425; sign 1,761 excluded by default) and keys each to the next deadline (season, gw, hours_before). The 137
Guardian predicted-lineups articles stay with the deterministic F16 parser; their per-fixture segments are the pilot's
ground truth (30 "team blocks", 2 teams each, Subs from = bench, Doubtful = doubt, Injured/Suspended = out). Pilot =
60 prose docs stratified by season/source + 30 team blocks. One shared zero-shot prompt (`scripts/extract_availability_facts.py`,
strict JSON facts {player, team, status in xi/bench/doubt/out/return/role, detail, until}); greedy decode, thinking
off, left-padded batches of 8 longest-first, resumable, stop file + Friday GPU-gate pause window. Scoring
`scripts/score_extract_pilot.py`: team-block precision/recall vs the parser, pairwise agreement on prose, and outcome
validity (each prose fact joined to the player's next-GW minutes/starts in merged_gw.csv).

| arm | s/doc | facts/doc prose | team blocks P / R | prose out → appeared | prose xi → started | agreement with Haiku v1 (name,status) |
|---|---|---|---|---|---|---|
| E4B-it bf16 | 22 | 8.1 | 0.75 / 0.23 | 29% | 69% | 0.18 |
| 31B-it nf4 | 62 | 2.1 | 0.99 / 0.29 | 13% | 88% | 0.52 |
| Haiku v1 | - | 1.8 | 0.95 / 0.67 | 10% | 86% | - |
| Haiku v2 prompt | - | 2.0 | 0.95 / 0.95 | 9% | 81% | 0.74 |

**Reading.** E4B is not an extractor on this prompt: it relabels everyone who played or scored in a match report as
"xi" (336 xi facts, 69% started = "played last week"), turns contract talk into "out", and cannot read the lists (the
August E12 finding again). The 31B reads like Haiku: sparse, precise (2 false positives in 283 team-block names),
empty on match reports, outcome-valid; the hand audit of 14 disagreements has each catching facts the other misses
(31B: Gallagher's red card → out, Mateta's stitches → doubt, Neto's muscle injury; Haiku: Toney's lay-off, Karius's
start, Marquinhos on loan). Both v1 arms under-read the long "Subs from" lists; the v2 prompt (explicit "not facts":
past matches, praise, contracts; explicit list instruction) lifts Haiku's team-block recall 0.67 → 0.95 at the same
0.95 precision and keeps prose validity (out → 9% appeared). Cost model for the 31B on the GB10: bitsandbytes nf4
prefill ≈ 60 tok/s and decode ≈ 1.4 s/step at batch 8 (peak 37 GB), so a document costs ≈ prompt_tokens/60 s plus the
batch's longest output × 1.4 s.

**Decision (01:00).** Backfill on the 31B (Wes's ask, quality confirmed) with the v2 prompt, pending the v2 GPU pilot
(E4B v2 then 31B v2, queued): availability-class documents first (2,291, 5,000-char article cap, batch 12, two-pass
caps 320 then 768 ≈ 20-25 GPU h), then `scripts/build_extract_features.py` (97% of names resolve to player ids) →
EX0/EX1/EX2 on the 21-window bench + xPts, all chained in `scripts/run_extract_backfill.sh` (queued by
`scripts/queue_extract_backfill.sh`; pause window Fri 13:45-17:30 UTC only if logs/gw8_gpu_ok exists). Role-class
documents are a second pass if the availability bench pays.

**v2 pilot result (04:00) and launch.** Prompt v2 on the GPU arms (`reports/extract_facts/pilot.md`, all six arms):

| arm | s/doc | facts/doc prose | team blocks P / R | prose out → appeared / started | prose xi → started | agreement w/ Haiku v2 |
|---|---|---|---|---|---|---|
| E4B v2 | 27 | 5.8 | 0.89 / 0.53 | 29% / 19% | 70% | 0.25 |
| 31B v2 | 90* | 1.8 | 0.99 / 0.46 | 13% / 5% | 83% | 0.53 |
| 31B v1 | 62 | 2.1 | 0.99 / 0.29 | 13% / 5% | 88% | 0.49 |
| Haiku v2 | - | 2.0 | 0.95 / 0.95 | 9% / 6% | 81% | - |

*the v2 team blocks ran to the 768-token cap (the 31B writes long "detail" strings for every listed sub; 7 of 30
truncated, prose never), which is where the extra time went. On prose v2 is the more conservative read: it drops the
dubious v1 extras (Neves "set to depart" → out, Jesus "first start in four months" → return, James "one of three
right-backs on the bench") and agrees with Haiku v2 on the Maguire/Casemiro and De Bruyne/Silva cases; the residual
disagreement with Haiku is mostly doubt-vs-out granularity for "pulled up injured" statements. E4B v2 still floods
"xi" (227 facts, 70% started) and truncates: E4B is not an extractor at any prompt.

Launched 03:57 PDT: `scripts/run_extract_backfill.sh` via the queue script, label 31b_v2, 2,291 availability-class
documents, 5,000-char cap, batch 12, caps 320 then 768, prompt v2, pause window Fri 13:45-17:30 UTC only if
logs/gw8_gpu_ok exists; then features → EX0/EX1/EX2 bench → xPts, sentinel "EXTRACT BACKFILL DONE" in
logs/extract_backfill.log. Stop cleanly with `touch logs/stop_extract`; resume by re-launching the chain.

**Step 3 queued (04:25).** `scripts/run_h4_team_sheet_chain.sh` waits for the backfill sentinel, then builds the
team-sheet splits (`scripts/attach_team_sheet_to_split.py`: a ≤ 1,100-char "Pre-deadline team sheet" section before
the evidence block with the player's own facts, the team's facts by status and the Guardian predicted-lineup
categories; smoke test on the E22 eval rows: 77% of rows get a Guardian lineup, team facts depend on the backfill),
trains the H1 recipe on E4B (batch 1 × accum 16, checkpointing on, ~9 h), predicts the H1 holdout/live rows, runs
`scripts/team_sheet_mechanism_check.py` (P(appear) movement and AUC/Brier on own-fact / team-fact / no-fact rows and
on the rows where the classic P was surprised, vs H1 on identical rows) and only then the 4 decision windows + xPts
(`reports/h_series/h4_*`, `h4_vs_h1.md`). Sentinel "H4 CHAIN DONE" in logs/h4_chain.log; `touch logs/stop_h4`
leaves the queue before it starts.

### Haiku full-scope arm and the resolver fix (2026-10-23 10:00 PDT)

Wes asked for the whole availability-document scope on Haiku through the subagent route on his Max subscription
(zero API cost). 191 workers of 12 documents (scripts/build_haiku_batches.py, the pilot v2 prompt, 5,000-char cap),
ten in flight, 07:58-09:45 PDT: 2,291/2,291 documents parsed (scripts/haiku_batch_status.py), 4,886 facts
(out 2,082, return 817, xi 711, doubt 656, role 375, bench 245), ~120k tokens and 2.5-7 minutes per worker.

- Outcome validity at scale (facts joined to the next gameweek's minutes, reports/extract_facts/backfill_compare.md):
  out → 19% appeared / 13% started; xi → 90% / 70%; doubt → 53% / 37%; bench → 62% / 28%; return → 74% / 50%;
  role → 89% / 75%. The 31B's partial run (432 longest documents) has the same profile (out 19%/13%, xi 85%/56%,
  1.7 facts/doc vs 2.1); agreement on the 243 documents both had read 0.52 (name+status), 0.58 names only.
- Name resolution bug: scripts/build_extract_features.py keyed only the last token of second_name/web_name, so Rodri
  ("Rodrigo 'Rodri' Hernandez", web "Rodrigo"), Diogo Jota ("Diogo J."), Alisson ("A.Becker"), Núñez ("Darwin"),
  Ederson ("Ederson M."), Bruno Guimarães ("Bruno G."), Ødegaard and Groß (ø/ß dropped by the normaliser) never
  resolved: 150 facts on star players. Fixed (every surname token, first names, abbreviated web names, ß/ø mapping,
  guarded aliases, first-name consistency on the surname fallback): resolved 95% → 97% (3,948 of 4,070 in-window facts),
  3,017 player-weeks with facts. The 31B chain picks the fix up automatically at its features step.
- Ridge bench on the Haiku facts (scripts/run_haiku_backfill_post.sh → reports/extract_facts/backtest_haiku.md,
  xpts_haiku/): EX1_F (ex_* features) −104 actual / −38 xPts over 21 windows (t −1.2 / −0.5), EX2_F (ex_* + Guardian
  lineups) −69 / −1 (t −0.8 / −0.0); first pass with the old resolver −66/−27 and −70/−18. NULL to negative: the
  extracted facts add nothing to the ridge beyond the status flag and the F16 lineups term, the same saturation seen
  for F15 and H3. The decision-relevant test is the SFT team sheet (H4), which reads the facts as text.
- Option on the table: H4 is queued behind the 31B backfill (~22 h of GPU left) and wired to the 31B facts; it could
  run tonight on the Haiku facts instead (FPL_H4_FACTS=reports/extract_facts/facts_by_player_week_haiku_v2.json,
  stop the 31B with logs/stop_extract, resume it afterwards). Wes's call: the 31B was his stated extractor.

## 31B backfill complete, EX verdict, H4 launched (2026-10-24 15:05 PDT)

- Backfill: 2,291 availability documents through Gemma-4-31B-it nf4 (prompt v2, 5,000-char cap, batch 12, caps 320
  then 768): 4,634 facts, 100% parse, 1 truncated row after pass 2, 46.5 s/doc, peak 43.6 GB. A DGX power cut at
  18:20 PDT on 10-23 stopped it at 996 docs; resumed 22:41 (by doc_id, nothing lost), finished 10-24 15:02.
- Validity, 31B vs Haiku (facts joined to the next GW's minutes, appeared/started): xi 93%/81% vs 90%/70%, out 17%/11%
  vs 19%/13%, doubt 48%/34% vs 53%/37%, return 72%/47% vs 74%/50%. Agreement over the 1,653 docs where either arm
  found facts: 0.58 on (name, status), 0.67 on names. Two readers, one profile.
- Name resolution 97% (3,817 of 3,942 facts within 168 h). Residual misses: "Gabriel" alone (29, genuinely ambiguous
  at Arsenal), Kanté (15, left the league), curly-apostrophe names O'Reilly/O'Nien (18; LETTER_MAP now maps ’ → ',
  fixed after this run, not re-benched: 0.4% of facts).
- EX ridge bench on the 31B facts (21 windows, base EX0_F): EX1_F −104 actual (sd 19.8, t −1.15) / −41 xPts (t −0.59);
  EX2_F (with the F16 lineups term) −53 (t −0.69) / −4 (t −0.07). Haiku arm: −104/−38 and −69/−1. VERDICT: null to
  negative with both readers; once the status flag and the Guardian lineups term are in, availability facts add nothing
  to the ridge. Same saturation as F15/H3. The decision-relevant test is the SFT team sheet (H4).
- H4 launched 15:03 PDT (E4B, H1 recipe, batch 1 × accum 16, ckpt on): holdout train 13,440 rows (46% with team facts,
  5.8% own facts, 77% Guardian lineup), holdout eval 1,152 (506 / 91 / 871), live eval 480 (205 / 30 / 176). Prompt
  p50 3,549 chars, max 4,604. measured 51.7 s/step at step 20 (H1: 28.4; longer prompts), peak 17.2 GB → training ends ~03:10 PDT Sun 10-25, predictions + 4 windows → ~05:00 PDT. Read
  reports/h_series/h4_mechanism_{holdout,live}.md BEFORE h4_vs_h1.md.

## H4 team-sheet retrain: mechanism PASSES, decisions NULL (2026-10-25 03:40 PDT)

Setup: Gemma-4-E4B, H1 recipe (regression + availability heads, LoRA modules), E22 top-96 splits with a ≤ 1,100-char
"Pre-deadline team sheet" (31B facts for the player and his team + Guardian predicted-lineup categories) placed before
the evidence block; 840 steps, 12.0 h at 51.3 s/step, peak 17.3 GB. Same rows, eval sets, classic backtests and ledgers
as H1, so H4 − H1 isolates the sheet. Adapter artifacts/gemma4_e4b_h4_teamsheet; outputs reports/h_series/h4_*.

Mechanism check (read first), holdout 2025-26 GW27-38, 1,152 rows (reports/h_series/h4_mechanism_holdout.md):

| slice | n | AUC classic / H1 / H4 | Brier classic / H1 / H4 | mean abs dP H1 / H4 |
|---|---|---|---|---|
| own fact (sheet names the player) | 91 | 0.746 / 0.798 / 0.848 | 0.1029 / 0.0862 / 0.0628 | 0.063 / 0.100 |
| team fact only | 415 | 0.675 / 0.743 / 0.759 | 0.0928 / 0.0783 / 0.0740 | 0.076 / 0.100 |
| no fact | 646 | 0.717 / 0.780 / 0.793 | 0.0627 / 0.0454 / 0.0431 | 0.070 / 0.086 |
| all | 1,152 | 0.704 / 0.771 / 0.788 | 0.0767 / 0.0604 / 0.0558 | 0.072 / 0.092 |

- The block is USED (the E17 test): H4 and H1 differ by > 0.1 on 17.6% of own-fact rows vs 5.1% of all rows, and the
  gain concentrates where the sheet names the player: own-fact Brier −27% vs H1 and AUC +0.05, a rank gain that no
  Platt recalibration of the classic P can produce (the H3 objection does not apply here). Surprise & own fact (n = 6):
  movement toward the truth +0.142 vs H1 +0.029. Team-level facts alone do nothing on surprise rows (n = 25: +0.026 vs
  +0.030). First SFT prompt block in this project whose use is provable.
- Live 2026-27 GW2-6, 480 rows: all AUC 0.760 → 0.780, Brier flat (0.0252 → 0.0250); own-fact rows (n = 30) AUC
  0.840 → 0.864 but Brier WORSE 0.0892 → 0.1183 (bigger, sometimes wrong, moves; audit below); team-fact-only AUC
  0.677 → 0.630. Classic ≥ 4 rows: Brier 0.0132 → 0.0096.
- Points: the median shrink is unchanged (holdout RMSE 1GW 3.411 vs H1 3.419 vs classic 3.420; mean Δ1 −0.27, sd 0.13;
  own-fact rows cut harder, −0.38 vs −0.26). The sheet gives the points head nothing, as every text block before it.

Decisions (4 windows, same engine, all fields): H4 1,067 vs classic 1,103 = −36 actual (sd 31.8/window, t −0.57) /
−29 xPts (t −0.95); H1 −18 / −23. Holdout 739 vs 788 (H1 750): windows −54 / −9 / +14; live GW2-6 328 vs 315 (H1 335).
NULL to negative inside the noise floor, the H1/H3 pattern again: the best availability read yet is decision-inert
through the threshold optimizer and the points shrink costs in GW27-30.

VERDICT: the "read facts, not snippets" path works as a MECHANISM and fails as a DECISION lever on these 4 windows.
Not a ship. Open question for Wes: three readers (H1, H3, H4) now improve P(appear) without moving squads, so the
constraint is how P(appear) enters the optimizer (threshold), not the reader; the earlier soft-optimizer (+25) and
Platt-ratio coupling (+54/4 windows, tie-breaks) are the only places availability ever cashed out.

Decision side, same prediction files through the engine's other modes (CPU, 03:34 PDT; 4 windows, actual / xPts vs classic):

| mode | H1 | H4 |
|---|---|---|
| all fields (points deltas + P) | −18 / −23 | −36 / −29 |
| availability only (LLM P(appear) replaces classic's, points untouched) | +37 / +11 | 0 / 0 (identical squads in all 4 windows) |
| availability_scaled (points × P ratio, clamped 0.6-1.4) | −53 / −14 | −56 / −16 |

H1's +37 is a GW2 bench-slot tie (Ajayi/Davies/Gonzalo ↔ De Cuyper/McBurnie/Palmer, same GW2 points) that cascaded into
different GW3/GW5/GW6 transfers; no availability call was involved. P(appear) deltas on their own never flip a pick in
this engine (threshold penalty), and rescaling points by them loses for both arms.

Live audit of the 30 own-fact rows: on the two clearest "out" cases, Gakpo and Isak GW6 (own fact "out" 49 h before,
team OUT list, Guardian "injured"; both missed the match) H4 RAISED P(appear) 0.64 → 0.79 and 0.53 → 0.58 while H1
cut to 0.39 / 0.28. It got Scott right (out, 0.83 → 0.58, missed) and followed a wrong extractor fact on Mendy GW3
("injured goalscorer", 0.74 → 0.49, played). The signal was learnable (train: 128 own-fact "out" rows, 30% played;
76 Guardian-injured, 13% played) and the holdout "out" rows (n 6, none played) did move 0.61 → 0.40, so the holdout
mechanism is real, but at live n 6 it is unreliable where it matters most.

FINAL VERDICT: mechanism real on holdout, unreliable live, decision value nil in every engine mode. Team-sheet path
CLOSED at the reader; the only untested lever is on the decision side (downside-only or soft P(appear) coupling in the
optimizer, a CPU test on these prediction files), proposed to Wes, not started.

Soft availability knee (decision variant avail_soft, weight min(1, P/0.8) on horizon points; CPU, 10-25 22:35 PDT), 4 windows
vs classic under the same variant (1,096 actual / 982 xPts; the threshold classic is 1,103): H4 availability-only +7 / +7
(t 1.2 / 1.6; squads differ in one window), H1 availability-only +38 / +13 (the same GW2 bench-tie cascade), all-fields
H4 −39 / −27, H1 −6 / −15. Three couplings tested (threshold, soft knee, ratio rescale): the readers' P(appear) never
cashes out in squad points. Decision-side question CLOSED as well.

H4 ablation probe (10-25 22:44 PDT, reports/h_series/h4_ablation/: the 121 own-fact eval rows re-predicted with the sheet
intact / without the player's line / without the team line / without the Guardian line / without the sheet):
- Holdout "out" rows (n 6, none played): classic 0.61, no sheet 0.71, full sheet 0.40; dropping the own line 0.47,
  the team line 0.46, the Guardian line 0.40. The sheet is read, in the right direction, through the own AND team lines
  (the Guardian line adds nothing once facts exist). "xi"/"return"/"role" rows move up ~+0.07 (correct, 94-100% played).
- Live "out" rows (n 6, 50% played): classic 0.75, no sheet 0.74, full 0.64, but every line removed lowers P further
  (0.58-0.60): the lines cancel. Gakpo GW6: no sheet 0.58 -> full 0.79; the OWN line alone adds +0.23, the team line
  +0.12, the Guardian line +0.07. Isak: 0.28 -> 0.58, own line +0.30. Scott (0.93 -> 0.58) and the mis-extracted Mendy
  (0.93 -> 0.49) went the way the sheet said. The adapter's reading of a fact line is phrase-sensitive, not status-token
  driven: "sustaining injuries with the Netherlands/Sweden" was read as a positive; "strained a hamstring with France"
  (Jacquet) as the negative it is. Points deltas: the sheet adds −0.09 shrink on own-fact rows (−0.29 -> −0.38).

### GW8 settled (ledger 2026-10-26, `reports/gw8_packet_2026_10/final/ledger_gw8.md`)

55 with the Triple Captain on Haaland (Wes's call; the sheet said no chip; 8 raw ×3, +8 over a plain captain, projected
+8.4), 47 without it, against an average of 45; overall rank 3.72M → 3.15M, total 486. Saka → Rogers free as
recommended: Rogers 1, Saka 0 minutes, 0 on the day; the −4 double to Calafiori was rightly left (Calafiori 1 in 22
minutes vs Konsa 14). Wes's XI override paid: Konsa 14 over N.Williams 8 (+6), Cunha 1 over Cherki 0 (+1). João Pedro 0
minutes with no warning anywhere (P(appear) 0.91 / 0.97; the feed flagged him "unspecified injury" after the game),
and the auto-sub went to Cherki 0 rather than N.Williams 8 (bench order −8; the model's own order would have done the
same). Hindsight XIs at a plain captain: entered 47, classic sheet 54 (Konsa 14 via the auto-sub), classic+SFT 41 (the
SFT's one specific call, Cunha over Cherki, was +1; the gap is the auto-sub path), MILP wildcard squad 39 and Free Hit
squad 32 against the hold's 54 (WC +48 projected over five weeks: the chip-calibration finding holds). H1 shadow
accuracy, interim read of 10-21 (668 players): RMSE 2.107 classic vs 2.136 SFT, bias −0.06 vs −0.40; the 19 rows ≥ 4:
4.567 vs 4.495. The ingest, cutoff bump and table rebuilds are scheduled for 13:07 PDT after the H5 chain releases the
training table. GW9: Konsa → Calafiori is now doubtful on both ends (Konsa 14; Calafiori d/75% hip, 22 minutes);
N.Williams d/75%; chips left BB, FH, WC.

### H5 (MSE loss + team sheet + role facts): shrink removed, points channel still empty, decisions NULL-positive (2026-10-26 11:50 PDT)

Chain `scripts/run_h5_mse_role_chain.sh` ran 22:59 PDT 10-25 → 11:33 PDT 10-26: training 840 steps, 12.09 h at 51.8 s/step,
peak 17.3 GB; predictions 26 min; adapter `artifacts/gemma4_e4b_h5_teamsheet_mse`. Same rows, eval sets and windows as H4;
the only recipe changes are `FPL_RH_LOSS=mse` (H1-H4 used Huber δ=1) and the 1,415 Haiku role facts merged into the sheet.

**Points (the question H5 was asked; `h5_mechanism_holdout.md` points section).** The mean-targeting loss did what it was
meant to: the 1GW delta mean is −0.09 (H4 −0.27, H1 −0.25), bias on holdout +0.01 against classic +0.10 (H4 −0.17), live
−0.31 against −0.23 (H4 −0.46). RMSE 3.415 vs classic 3.420 on holdout, 3.421 vs 3.424 live; 3GW/5GW 6.765/9.962 vs
6.807/10.035. But the player-specific channel did not open: the delta sd fell with the mean (0.106 vs H4 0.134 holdout;
0.124 vs 0.159 live), corr(delta, realised residual) 0.047 (H4 0.103) holdout and 0.096 (0.091) live, own-fact rows
0.160 (0.216) and −0.006 (0.106), own-role-fact rows (n 9 / 6) −0.239 / −0.178. "Closer than classic" 58% (H4 61%).
The role facts moved nothing. Three losses on the points head on E4B (H1 Huber, H4 Huber + sheet, H5 MSE + sheet +
role): the points channel is closed for this recipe.

**Availability.** Holdout own-fact AUC 0.860 (H4 0.857, classic 0.740), Brier 0.0771 (0.0784); all rows 0.776 (H4 0.788,
H1 0.771). Live: all-row AUC 0.727 (H4 0.780, H1 0.760) but own-fact Brier 0.0890, better than classic 0.0917 where H4 was
worse (0.0937); Gakpo GW6 0.64 → 0.65 (H4 0.79, H1 0.39), Isak 0.53 → 0.59 (H4 0.58), Scott 0.83 → 0.58 (right), Mendy
GW3 0.49 on the mis-extracted fact (same as H4). Availability deltas correlate 0.914 with H4's.

**Decisions (`h5_arms`, `--llm-fields all`).** H5 1,132 vs classic 1,103 (+29 actual, sd 16.5/window, t 0.88; +24 xPts,
sd 17.1, t 0.70; corr 0.77); vs H1 +47/+47, vs H4 +65/+53. The first H arm positive on both metrics, and still inside the
noise floor (need > 65 actual over 5 windows, xPts t > 2). Where it comes from: H5 equals H1 in 31-34 (237, identical
xPts), 35-38 (266 vs 267) and GW2-6 (335), and equals classic in weeks 27-28; the whole gain sits in weeks 29-30 of one
window: TC Bruno (8 raw) over Semenyo (7), Hill 8 over Mané 2 in the XI, and a bench-boost-week squad pair (+5). Three
marginal picks, not a mechanism.

**VERDICT.** H5 is the best adapter on every metric against H1 (RMSE, bias, holdout AUC, Brier, decisions +47) because
the MSE loss removed the constant shrink that made H1/H4 harmful in all-fields mode; it is decision-neutral, not
decision-positive, and carries no points information. The load-bearing-forecaster claim is not supported by it. Use:
promote H5 to the weekly shadow arm in the classic-vs-classic+SFT side-by-side (replacing H1) once the team-sheet
block can be built live (extractor on the week's docs + Guardian predicted-lineups parse); do not train further
H-series variants on E4B. Memory: `fpl-h5-mse-role.md`.

### GW8 weekly ingest + rebuild (2026-10-26 13:22 PDT, `scripts/run_weekly_rebuild_gw8.sh`, `logs/weekly_rebuild_gw8.log`)

Ingest (settled gate, sync through GW8, status backfill, verify), cutoff 7 → 8, both production tables rebuilt
(196,244 rows, +669 GW8 rows; pre-ingest backups in `data/backup_2026_10_26/`), F16 team-news table and the
extract-features table (combined 31B + Haiku facts, 4,943 facts resolved, 98%) rebuilt on top, GW9 parity audit in
`reports/gw9_packet_2026_10/parity_audit.md` (17 flags, the known DefCon-history and ownership-zero-share ones; the
status-flag row is no longer flagged: live 0.296 vs history 0.331).

**Bug found and fixed on the way.** The first run left GW8's 669 rows at status "a" (flag 0.000), and GW7's 668 rows
had been "a" since 10-21: `backfill_live_status_from_corpus.py` globbed `live_gw*_2627_corpus_bare.jsonl` while the
refresh has written `live_gw{N}{interim|final}_2627_{classic|f6}_corpus_bare.jsonl` since GW6, so the backfill filled
the same 3,831 rows each week and the aggregate gate (season rate 0.18-0.21) passed. The GW7 section above ("ingest ran
clean, flagged rate 0.208") was wrong on that point. Fixed: the script matches every bare snapshot of the season in
mtime order (the Friday final wins over the interim) and lists the files and weeks covered; the ingest gate now checks
the just-finished GW alone. After the fix: 5,178/5,220 rows filled, flagged by week GW1 0.19 … GW6 0.32, GW7 0.29,
GW8 0.30, season 0.266; tables rebuilt on it. The dead-flag run is kept as `logs/weekly_rebuild_gw8.run1_deadflag.log`.

**Second gap, not fixed.** The Guardian predicted-lineups article for GW8 was published Fri 10-23 15:42 UTC, after the
final refresh pulled the store (14:00 UTC) and before the 17:30 UTC deadline, so the team-news table has no GW8 rows
(gn_article 0.00; also 0.00 for GW2, GW3, GW5). For GW9 (deadline Sat 10-31 11:00 UTC) the store needs a re-pull about
an hour before the deadline before the F16 feature or an H5 live sheet is built.

GW9: free-move candidate Konsa → Calafiori re-checked on the GW9 sheet (Konsa 14 and nailed; Calafiori d/75% hip);
N.Williams and João Pedro d/75%; chips left BB, FH, WC. No GPU job was run.

### GW9 interim + the Calafiori question + a data-contract bug (2026-10-27, Tue, 08:30-09:00 PDT; all CPU)

**Wes's question.** Calafiori is rated high but his minutes run low, as last season; early-season highs are a fresh-start
artifact; Arsenal's defence (Saliba etc.) keeps picking up injuries. Facts: 2026-27 he started 7/7 (80-90 min) then came off
the bench for 22 min in GW8 (1 pt) against a GW8 forecast of 5.5 / 90 min / P(appear) 1.00, the top defender; 2025-26 he
started GW1-15 then missed 8 of 9 and was rotated to the end (22 starts of 38, 1,697 min); 2024-25 11 starts. The Guardian's
Friday predicted-lineups article (`scratchpad guardian_gw8_lineups.json`, fetched with the API key) had him in the Arsenal XI;
the hip flag (d/75%) was added Sat 18:30 UTC, after the match → GW8 was not readable before the deadline.

**Mechanism.** The minutes/appearance heads are current-season-only by Wes's 2026-09-01 constraint (F2b blends quality only);
7 straight starts → 90 min / P 1.00 regardless of prior seasons. Tested whether that is a systematic error
(`scripts/minutes_prior_study.py` → `reports/gw9_packet_2026_10/minutes_prior_study.md`, 37,617 single-fixture walk-forward
rows, excess = residual minus the same-season same-forecast-bin mean): nailed-looking players by PRIOR-season start share
<40% / 40-60% / 60-80% / 80%+: excess +0.03 / −0.03 / +0.10 / +0.08 (± 0.09-0.13) → NOT over-forecast; the Calafiori profile
(two prior seasons < 60%) +0.01 ± 0.09; defenders only −0.17 ± 0.15 / −0.20 ± 0.21 (borderline). NO prior PL season and
nailed-looking: −0.23 ± 0.09, defenders −0.35 ± 0.14, weeks 1-10 −0.38 ± 0.20 → the one real "fresh season" effect. Hot starts
(current PPG > prior PPG + 2) at weeks 7-14: −0.10 ± 0.22 → no measurable regression beyond the 6-week ramp. OLS on nailed
rows: actual minutes = 53.4 + 0.356 × forecast + 4.2 × prior start share (± 1.3), i.e. holding the forecast fixed a full-share player plays ~4 min more than a zero-share one: Wes's direction, small. (CORRECTED 10-28: the 10-27 text called this the opposite sign.)

**Bug.** The table's `player_id` is the per-season element id, re-used by another player next season (841/866 ids → 2+ codes;
element 8 = Mavropanos, Leno, Marí, Tierney, Jesus, Kiwior, Timber, Calafiori); `code` is stable. F13
(`add_injury_history_features.py`) and the 10-11 injury-pattern study keyed cross-season history on player_id → both re-keyed
on code. Corrected pattern table `reports/review_fixes_2026_10/injury_pattern_codekey.md`: 1st game back +0.34 ± 0.20 (was
+0.10), missed 10+ of last 38 −0.16 ± 0.06 (was −0.08), long lay-off last season −0.08 ± 0.06. Memory fpl-player-id-reuse.

**F17 + F13 re-run** (`scripts/add_prior_season_features.py`, `run_prior_f17_chain.sh`, 21 windows in 2.5 min at 4 workers,
`reports/prior_f17/README.md`): base 5,314; PI_F (F13 corrected) −64 actual (t −1.37) / −7 xPts, MAE a hair better → F13 stays
closed on a valid test; PP_F (prior_pl_games, no_prior_pl_season, prior_start_share, prior_minutes_share, prior_unknown)
+41 actual (t 0.55) / +56 xPts (t 1.23), 11-6-4, 5GW MAE 3.6576 → 3.6337, 1GW MAE 1.0009 → 1.0037; PN_F (without the shares)
−31 / −8 → the gain is the share columns. NULL-positive, below the bar; not shipped (columns stay in SAFE_FEATURE_COLUMNS,
used only when present; a ship needs the dataset.py port for live parity).

**GW9 interim packet** (`scripts/run_gw9_interim.sh` → `reports/gw9_packet_2026_10/`, `RECOMMENDATION_2026_10_27_interim.md`):
João Pedro now i/0% (thigh, unknown return; 69.8% owned); Calafiori d/75% hip → P(appear) 0.59, Konsa → Calafiori moves
nothing (XI 55.2 either way). Do: João Pedro → Thiago (BRE, 7.8) free, +7.2 GW9-13 / +1.7 GW9; C Haaland, VC Rogers; no
chip (WC +33.9 projected by the exact optimizer, calibration says no). XI 56.5: Donnarumma; De Cuyper, Konsa, Justin; Rogers,
Groß, Cherki, Cunha; Haaland, Thiago, Evanilson; bench Sels > McGinn > Mitchell > N.Williams. Role-override sheet: no one in
the Konsa cell. Fixes landed: decide.py + milp_routes.py zero i/s/u/n players with chance < 25 (João Pedro had carried
3.57/18.8 and sat in the optimizer's hold XI); live_chip_line.py takes `_classic_` or `_f6_` examples (GW8 tag mismatch).
New `scripts/live_team_news.py` (Guardian predicted lineups → per-player categories for the coming GW, 19/20 teams on the
GW7 article; ALIAS extended for "Manchester Utd"); `attach_team_sheet_to_split.py` falls back to a player's latest team for a
week the table lacks. `scripts/run_gw9_final_refresh.sh` ARMED (pid in logs/pids/gw9_final_refresh.pid): sleeps to Sat
2026-10-31 09:15 UTC (02:15 PDT), rebuilds final/, re-pulls Guardian (from 10-10) + Scout, builds the F6 live examples, the
live team-news json and the H5 team-sheet examples; the H5 read + side-by-side run only if `logs/gw9_gpu_ok` exists.
Open: Haiku extraction of the GW9-week docs into `reports/extract_facts/facts_by_player_week_live_gw9.json` (optional; the
sheet falls back to the backfill facts + Guardian categories); Wes's go-ahead for the GPU read; a Saturday check-in.

### Rotation risk: what the numbers carry vs what the best text carries (2026-10-28, Wed, 07:30 PDT; CPU, 2 min)

**Wes's pushback.** The classic rates Calafiori high and "likely omits the rotation risk and his history under Arteta of not
playing full games; that's why reading a large amount of high-quality text would help." Tested both halves on the F16 table
(`scripts/rotation_text_ceiling.py` → `reports/gw9_packet_2026_10/rotation_text_ceiling.md`; 15,198 nailed-looking
player-weeks 2023-24 to 2026-27 GW8 = started the last three with ≥ 75 min, unflagged; non-start = under 60 min; prior-season
profile keyed on `code`).

**Half 1, history (raw rates).** By PRIOR-season Guardian "sub" share < 10% / 10-25% / 25-50% / 50%+: non-start 12.8% /
16.0% / 18.3% / 17.2% (± 0.8-2.1), minutes 80.0 / 76.7 / 75.5 / 75.2, points 3.50 / 3.27 / 3.16 / 3.12; defenders 11.9% →
19.0%; weeks 1-10 9.6% → 16.4%; by prior start share 80%+ 10.0% vs < 40% 17.8%. So Wes is right in the raw data: a nailed-looking
player with a rotation history sits out ~5-7 points more often. Most of that is already inside the forecast (current-season
minutes averages and the F2b quality blend are lower for these players): against same-forecast peers the residual gradient
is ~2-3 min and, for defenders, −0.17/−0.20 vs +0.02/+0.03 pts a week (minutes_prior_study.md A2/A3). The 10-27 OLS was
mis-described: +4.2 min per unit prior start share IS Wes's direction (corrected above). F17 (prior_start_share etc.) is the
feature for exactly this residual: +41 actual / +56 xPts over 21 windows, below the bar, re-measure. Calafiori's own profile:
prior sub share 0.38 (29 articles), prior start share 0.50 → the 25-50% bucket.

**Half 2, text.** This week's Guardian predicted lineup is a much stronger signal than any history: nailed-looking AND listed
as a sub → 39.2% non-start (± 4.9, n 401; 44% when the history was clean) vs XI 12.2%, doubtful 49.6%, out 95.7%. The ridge
already consumes it (F16 TN1: a named sub −7 min / −0.22 pts; +31 actual / +33 xPts over 21 windows, 4-14-3). The ceiling:
of 2,304 surprise non-starts, 69% had an article and the article foresaw 17.8% of those (sub/doubtful/out); 82% were in the
predicted XI (defenders 19.4%, 2025-26 23.6%, 2026-27 5.6% with the article in the table for only 38% of rows: pull timing).
Calafiori GW8: in the XI (fetched article), hip flag after the match → not in the 18%.

**Conclusion.** The rotation risk is real and small (history ~0.1-0.2 pts/wk for defenders; same-week text 3x that but on
3% of nailed rows and foreseeing 1 in 5 benchings); both are already measured as ridge features (F17, F16) at +31..+56 per
21 windows, below the noise bar, with F16 not yet live. "Reading a large amount of high-quality text" was tested as E8/E12/
E17/E18/H4/H5/H31 and never beat the distilled lineup the journalists publish; the deliverable for text is the live F16 wiring
plus a Friday-evening Guardian pull, not more reading. Memories: fpl-prior-season-f17 (sign corrected), fpl-team-news-f16.

### F16 live wiring, the GW9 Wednesday packet and the Isak question (2026-10-28, Wed, 09:15-09:40 PDT; CPU)

**Wes:** "sg pls proceed" (wire F16 live for GW10 behind a parity check, re-measure F17 alongside); "at 4pm Wednesday
could you run another one for GW9 - I will set my squad then"; "ideally I can get Isak back - should I couple it with
another move from midfield, defence or keeper to enable that?"

**F16 live.** `FPL_TEAM_NEWS_LIVE_JSON` → `_attach_live_team_news` in `dataset.build_live_week_frame` maps
`scripts/live_team_news.py` categories onto gn_* exactly as the table builder does (needs the _teamnews table and
`FPL_TEAM_NEWS_FEATS=1`; missing/empty file = no-article state). Parity on GW7 (`scripts/team_news_live_parity.py` →
`reports/team_news_f16/live_parity_gw7.md`): categories identical on 633/634 shared keys; the 34 live-only keys were all
Man Utd, which the table (built 10-26) had failed to resolve before the 10-27 ALIAS fix → table rebuilt 10-28 (2026-27
article coverage 0.38 → 0.43; GW7's article lives in the gw8interim/gw8final stores, not gw7final). Forecast movement
from the article alone (classic+F6+F16 with vs without, 667 players): XI +0.07 pts / +1.6 min, sub −0.11 / −4.2,
doubtful −0.11 / −2.6, out −0.20 / −3.3. `scripts/f16_shadow_diff.py` = the base-vs-shadow sheet (squad with categories,
both XIs, top-150 movers); tested on the Wednesday packet (no article yet → no-article model, XI unchanged, −0.04/player).
Saturday refresh killed, patched (F16 shadow forecast + sheet after the live team-news step) and re-armed (pid
264676). Combined bench `scripts/run_f16_f17_chain.sh` → `reports/f16_f17_combo/` (PB_F / TN1_F / PP_F / TP_F on the
rebuilt tables; first launch on the stale table killed and cleared) running; results appended below when done.

**Wednesday packet.** `scripts/run_gw9_wed.sh` (wed/, SLEEP_UNTIL arms it): built 09:25 PDT; armed copy fires 22:35 UTC
(15:35 PDT, pid in logs/pids/gw9_wed.pid); session cron d2d33343 at 15:50 PDT writes RECOMMENDATION_2026_10_28_wed.md.
New: `forced_routes.py` (exact routes with a named player forced in), `returner_counterfactual.py`,
`role_override_sheet.py --drop NAME:GW` (no effect for a mid-season blank: the history builder fills gaps with zero
rows; kept for completeness). Wed 09:20 PDT snapshot: Isak 9.1 a/100%, GW9 3.87 / GW9-13 20.25 / 64 min / P 0.72 (his GW6
injury blank sits in the 3/5/8-week windows; GW7-8 78 + 76 min, 9 + 9 pts); João Pedro (7.7) + bank 1.7 = 9.4 → Isak
affordable alone, bank 0.3. Routes (GW9-13 vs hold, net of hits): João Pedro → Isak +5.9 (GW9 +0.9); Isak + Cunha →
Tavernier (−4) +7.0; Isak + Cunha + Donnarumma → Tavernier + Raya (−8) +9.9; João Pedro → Thiago +7.2 (GW9 +1.7); João Pedro
→ N.Jackson GW9 +2.0; Cunha + N.Williams → Gabriel + Tavernier (−4) +11.0 (leaves the injured João Pedro on the bench).
Returner counterfactual (GW6 blank → 78 min in the availability features only): Isak GW 4.16 / 5GW 21.43 / 73 min / P
0.81 ≈ Thiago 4.66 / 21.4 / P 1.00 → by the model the Isak-vs-Thiago choice is a coin flip if he is fit, −1.3 over five
weeks if the 0.72 read is right; a second move adds +1.1 after the hit (not worth it). Konsa → Calafiori still dead
(Calafiori d/75%, 3.18 / 17.2).

**F16 + F17 combined bench (done 09:34 PDT, `reports/f16_f17_combo/`, 21 windows, base PB_F 5,314 actual / 5,127 xPts,
rebuilt tables):** TN1_F (F16 alone) +33 actual (t 1.41, 4-3-14) / +29 xPts (t 1.39); PP_F (F17 alone) +41 (t 0.55,
11-6-4) / +56 xPts (t 1.23); TP_F (both) +43 (t 0.61, 10-6-5) / +46 xPts (t 1.23); accuracy TP_F best but marginal
(RMSE 1GW 1.9368 vs 1.9411, MAE 5GW 3.6336 vs 3.6576). The two do NOT stack (+46 < +56 + 29): they overlap on the
availability axis. Neither alone nor together clears the 2σ xPts bar (≈ 85). VERDICT: F16 stays a live shadow sheet
(Saturday), F17 stays unshipped; re-measure both when more 2026-27 weeks exist; no ship on this evidence.


**GW9 Wednesday packet, 15:35 PDT rebuild (`reports/gw9_packet_2026_10/wed/`, `RECOMMENDATION_2026_10_28_wed.md`).**
The armed sleeper fired on time (15:35-15:39 PDT). Hold 273.9; João Pedro → Thiago +7.2 (free, GW9 XI 56.9 vs 55.5);
João Pedro → N.Jackson +7.1 (GW9 57.3, bank 2.6); João Pedro → Isak +6.0 (bank 0.3, affordable alone; with Cunha →
Tavernier −4 = +7.2, with Donnarumma → Raya as well −8 = +10.1, none earns the hit); Cunha + N.Williams → Gabriel +
Tavernier −4 = +11.2 keeps the injured João Pedro as 4th sub; wildcard +35.8 projected, not used. Isak counterfactual
on this snapshot (GW6 blank → 78 min): 4.17 / 21.5 / 73 min / P 0.81, level with Thiago (4.69 / 21.5) and Jackson
(5.03 / 21.4) over five weeks. Nothing changed status since Tuesday; the forecast moves are the price/ownership/transfer
features (Jackson transfers in 526k → 916k, 19.3 → 21.4 over 5 GW), which the model carries since the 10-04 live-parity
fix. Sent to Wes 15:50 PDT: Thiago, C Haaland, VC Rogers, no chip, Jackson flagged as the equal cheaper pick.

### The Isak question: is the low P(appear) a classic-ML defect? (2026-10-28, Wed evening; CPU)

Wes: Isak is fully fit (78 and 76 minutes in GW7-8, 51 points in 7 starts, xGI/90 0.70) yet the classic read is 65 min /
P(appear) 0.72 / GW9-13 20.3 against Thiago 21.5 and N.Jackson 21.4. Three findings
(`scripts/returner_pattern_calibration.py`, `reports/gw9_packet_2026_10/returner_pattern_calibration.md`,
`reports/gw9_packet_2026_10/forecast_decomposition.py`):
1. P(appear) in this pipeline is predicted minutes / 90 (per-fixture mode), not a probability, and the optimizer never
   reads it. 94.7% of players with Isak's pattern appeared.
2. The minutes head under-forecasts his pattern (injury blank 3 games back, two 70+ games since, unflagged) by ~18 min:
   61 → 79 ± 3 (n 360). ~8 min is the blank inside the 3/5/8-week windows (counterfactual 65 → 73), the rest is ridge
   shrinkage that hits every nailed player forecast at 60-72 min (67 → 76). Injury blanks and benching blanks get the
   same forecast but realise 79 vs 71 min; in points they realise the same (+0.36 vs +0.43).
3. Points: the pattern is under-forecast by +0.37 ± 0.30/GW, identical to the 60-72 minutes band (+0.36 ± 0.10); the
   86+ band (Thiago, Jackson) is calibrated (−0.01 ± 0.25). Corrected, Isak ≈ 22.1 vs 21.5 / 21.4 over GW9-13: a coin
   flip. The decomposition shows his finishing is credited (points_avg_8 +1.9, xG +1.5, price +1.7) and the gap is
   availability (−1.7), Thiago's creativity/xA (−1.1) and defensive contributions (−1.9), plus the GW6 zero in his
   3-game xGI average. Setting FPL_PRIOR_BLEND / FPL_OPPONENT_INTERACTION at forecast time changes nothing (table-build
   flags), so that decomposition path is invalid.
Untested next levers: a minutes-band recalibration of the heads (systematic; cheap on the 21-window bench) and F18
availability-conditional rolling windows (expected decision value small). Told Wes: Isak is a defensible pick on his own
read, the model cannot separate the three; the 0.3 bank after Isak blocks the GW10 Raya upgrade without a second sale.

### Wes bought Isak; next training round launched (2026-10-28, 22:00-22:40 PDT)

**XI with Isak** (`reports/gw9_packet_2026_10/wed2b/`, hand-edited entry state because the FPL API had not yet shown the
transfer): Donnarumma; De Cuyper, Konsa, Justin; Rogers, Groß, Cherki, McGinn; Haaland, Evanilson, Isak; bench Sels >
Cunha > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 56.2; no chip; no hit route worth it (Cunha → Tavernier −4 nets
+1.2 over five weeks).

**Why the adapters never learned the returner/band pattern.** The E22/H prompt (checked on Isak's GW6 row) carries the
classic's five baseline numbers, status/news, fixtures, congestion, team sheet and two articles, but no week-by-week
minutes/points, xG or prior-season record. `band_delta_check`: H5 Δpts −0.08..−0.21 and Δmin ≈ 0 in every minutes band
(H1 −0.23..−0.32 / ≈ 0) against classic residuals of +8 / +3 / −7 min; H5's training loss moved 3.59 → 3.29 over 840 steps,
about what a constant predictor scores. The head has been fitting a constant because nothing in the prompt varies with
the thing that is wrong.

**H6** (`scripts/run_h6_numeric_chain.sh`, `logs/h6_chain.log`): H5 recipe + `scripts/attach_numeric_history_to_split.py`
block ("GW1 90/2; … GW6 0/0 (i); GW7 78/9 (d); GW8 76/9 | season totals, no-shows, last-5 xG/xA | prior season start share")
on the same splits as H5, plus a new live window 2026-27 GW7-8 (corpus rebuilt through gw8final) scored for classic, H5
and H6; mechanism test = `scripts/band_delta_check.py` (does Δmin track the classic residual by band / on returner rows);
then H6b (2 epochs, head LR 2e-3, LoRA LR 1e-4). ETAs Thu ~14:00 PDT / Fri ~16:00 PDT. Pointer `logs/gw9_shadow_adapter`
switches the Saturday read to H6 only on a pass; `logs/gw9_gpu_ok` touched (Wes's go-ahead), refresh re-armed.

**Classic-side fix in parallel** (CPU, `scripts/run_minutes_band_chain.sh` → `reports/minutes_band_cal/`): additive
offsets by band of the per-fixture minutes forecast (`FPL_MINUTES_BAND_CAL`, leave-one-season-out residuals), three
variants (all rows / unflagged only / bands < 80 only) on the 21 windows vs the rebuilt PB_F.

## 2026-10-29 Thursday morning: the H6 stall, the minutes-band verdict, N.Williams cleared

**H6 chain idled 10 h.** At 08:30 PDT the GPU was at 0% with no trainer log: `gpu_wait` in `run_h6_numeric_chain.sh`
(`pgrep -f "reghead_predict.py|train_gemma_reghead.py|extract_availability_facts.py"`, unanchored) matched the Bash
launcher shell that re-armed the Saturday refresh at 22:32 — its command text quoted that pattern inside the script patch,
and it stayed alive as the parent of the setsid'd sleeper. Killed the launcher (pid 283100; the sleeper 283104 has its own
session and kept sleeping); the chain resumed by itself. Cost: the H6 verdict moves from Thu ~14:00 to Thu ~23:00 PDT, and
the chain's time gate will skip H6b, which is to be queued after the Saturday GPU read instead. Rule added to memory:
anchor every guard on `^python3`, never quote a guard pattern in a launcher command, and confirm the first GPU step
started within two minutes of any launch.

**Minutes-band calibration (classic-side fix for the returner/band residual): NEGATIVE.** 21 windows vs PB_F
(5,314 actual / 5,127 xPts): MB1 all rows −142 actual / −80 xPts (t −1.38 / −0.95), MB2 unflagged only −132 / −14, MB3
bands < 80 only −38 / −8 with 13 ties. The band residual is real but the players it would lift are the rotation-risk pool,
already ranked correctly against nailed players; lifting them costs squads points. Same shape as the premium-bias result:
calibration defect, not a ranking one. Flag stays off; closed.

**N.Williams's arm flag cleared overnight** (d/75% → a/100% in the API at 08:30 PDT; Isak a/100%; Calafiori still d/75%,
João Pedro i/0%). The public API still lists no GW9 transfer: current-GW transfers and picks are hidden until the deadline,
so "no Isak in the API" is expected, not a sign the move failed. Re-pick built in `reports/gw9_packet_2026_10/thu/` on a
fresh snapshot with the Isak hand-edit (bank 0.3, 0 FT).
Re-pick result (08:38 PDT): N.Williams 2.78 → 3.30 GW (68 → 79 min, P 0.76 → 0.88); the optimizer puts him in for Justin
(3.30 v 3.24, both away at 15:00Z Saturday): GW9 XI 56.3 v 56.2, hold EV 281.2; bench Sels > Cunha > Justin > Mitchell;
no hit route (Cunha → Tavernier −4 nets +1.5); role override --auto Konsa only, XI unchanged. A coin flip on the numbers;
the real adjustment is N.Williams off the last bench slot. H6b follow-on armed (`scripts/run_h6b_followon.sh`, pid in
`logs/pids/h6b_followon.pid`): waits for the H6 chain pid, runs H6b if the chain did not and it is before 06:30Z Fri,
else logs "H6B DEFERRED" for a Saturday-afternoon start.

**Thu 14:30 PDT, Wes: does Bournemouth's midweek cup game change Justin v N.Williams?** Facts (Sky/SI/roundups):
Carabao Cup round 4 on Wed 28 Oct, Bournemouth 3-0 Aston Villa at home, Sunderland 3-2 Brentford; Leeds went out in
round 3 (3-6 v Chelsea), Forest are not in the cup and neither Leeds nor Forest are in Europe; Bournemouth are also in the
Europa League (played 22 Oct, next 5 Nov). Both opponents played Wednesday, so the pair is symmetric. Study
`scripts/congestion_residual_study.py` → `reports/gw9_packet_2026_10/congestion_residual_study.md` (European midweeks as
the proxy, 37,617 forecast rows): opponent-congestion residual for defenders +0.11 ±0.20, raw CS rate 0.215 v 0.190
against the same European clubs, sign flips by rest band (3 days +0.18, 4 days −0.36); own-team congestion nil (F9 again).
Verdict: not a model opportunity, no hand adjustment, no domestic-cup feed. Pick unchanged. H6 at 62.7 s/step → verdict
~01:30 PDT Fri; H6b deferred to Saturday after the GW9 read.

## 2026-10-30 Fri: H6 verdict

H6 finished 23:53 PDT Thu (14.6 h training, 62.7 s/step). **The numeric-history block went unused.** Band check over
1,632 holdout + live rows: H6 Δmin −3.2 / +0.1 / +0.5 / +0.3 / +0.7 / +0.6 by forecast-minutes band against classic
residuals of +2.0 / +8.2 / +3.3 / +1.1 / −0.9 / −6.8; corr(Δmin, residual) 0.156 (H5 0.152); Δpts a constant −0.09
everywhere (sd 0.128); the Isak-pattern rows get −0.7 min against +21 realised; H6 and H5 availability deltas correlate
0.95; the training-loss curve is block-for-block H5's. Accuracy = H5 (RMSE 3.416 v 3.420, AUC 0.782 v 0.776). Decisions:
holdout 777 v classic 788 v H5 797, live GW2-6 325 / 315 / 335, GW7-8 129 all three; xPts +5 over 5 windows (H5 +24).
Gate failed on both counts; the shadow pointer stays unset and Saturday's GW9 read uses H5. The premise was also killed
from the classic side on Wednesday night: the minutes-band calibration that would have realised the same correction lost
38-142 points over 21 windows. Reading: on 13k rows with points noise of sd 3.4 the head converges to baseline + constant
whatever the prompt says; inputs, capacity and loss are now all ruled out. H6b (2 epochs, LoRA LR 1e-4, head LR 2e-3) is
the last knob, deferred by its own gate (the chain ended 23 min past it, and at 62.7 s/step H6b needs 31 h, so it could
not have cleared the GW9 read anyway) → start Sat ~03:00 PDT after the read, verdict Sun ~10:00 PDT. GPU idle since.

## 2026-10-31 Sat: GW9 final packet, H6b start

The final refresh (`scripts/run_gw9_final_refresh.sh`) fired 02:15 PDT and logged "GW9 FINAL REFRESH DONE" at 02:32 PDT:
fresh entry + snapshot (09:15Z), classic+F6 forecasts, decision sheet, exact optimizer, lineups, role override, Guardian
re-pull (350 new rows; the predicted-lineups article published Fri 16:19Z, 18.7 h before the deadline), Scout pull (38
articles), live corpus (669 rows, baseline P(app) p50/p90 0.16/0.87, no cold-start), live team-news categories
(XI 379 / sub 207 / injured 55 / doubtful 24 / suspended 4), F16 shadow sheet, H5 team-sheet read on the GPU (669 rows,
9.8 min) and the side-by-side. As expected the API still showed the pre-transfer squad (João Pedro, bank 1.7, 1 FT: the
public API hides current-GW transfers until the deadline), so the Isak hand-edit was replayed at 02:55 PDT (scratchpad
`final_handedit.sh` → `final/build.log`; decide, milp, route_lineups, role override, side-by-side, final summary and chip
line re-run on CPU; the API-state outputs kept as `final/*_api.*`). Lesson for the runbook: the refresh script should
carry the hand-edit block itself whenever a transfer has been confirmed before the deadline.

**Final call (`RECOMMENDATION_2026_10_31_final.md`, sent 03:05 PDT): hold, no chip.** XI Donnarumma; De Cuyper, Konsa,
N.Williams; Rogers, Groß, Cherki, McGinn; Haaland, Evanilson, Isak; bench Sels > Justin > Cunha > Mitchell; C Haaland
VC Rogers; GW9 57.7 (Thu 56.3), hold EV 285.3 (281.2). Same XI as Thursday; the bench order flipped (Justin 3.24 > Cunha
3.22), which makes Justin the first auto-sub behind Cherki (XI at P 0.51 / 46 min; Guardian XI; H5 reads 0.76). No hit
earns itself (Cunha → Tavernier +4.6 now v +6.0 rolled; −8 +7.6; −12 +11.9); WC +38.5 projected / +5.6 on the sheet,
FH +10.7 / +5.8. Guardian lineups: all 14 fit squad players in their XIs; the F16 shadow would swap Cunha for Justin
(3.34 v 3.29), not deciding. No squad status moved overnight (29 league-wide changes, none ours). Forecast moves since
Thursday are momentum only (Evanilson 4.66 → 5.44 on ownership 9.7 → 14.1%; Isak 3.95 → 4.34; Cherki 3.71 → 3.54).
H5 side by side: identical XI bar Justin for N.Williams (57.5 v 57.7), generic shrink +0.099x − 0.308, player-specific
remainders ≤ 0.25, availability read high across the squad, evidence text = match-report filler plus two Cunha name
matches. Chip planning item from GW10: BB, FH and WC all expire after GW19 with no double or blank published this half.

**H6b started itself at 02:32:43 PDT**, 30 s after the refresh exited (`scripts/run_h6b_after_gw9.sh`, pid in
`logs/pids/h6b_after_gw9.pid`): 13,440 rows, step 1 at 02:35:13, 63.2 s/step, 1,680 steps, peak 17.3 GB; training ends
~Sun 07:45 PDT, scoring ~1.5 h, verdict ~10:00 PDT Sunday (`logs/train_h6b.log`, `logs/h6b_after_gw9.log`). The GPU had
been idle since Thursday 23:53.

## 2026-10-31 Sat evening: standing training go-ahead, team-trajectory question, F19 bench

**Wes (~17:00 PDT):** "kick off any retry of the training, SFT or RL, no need to worry about the game week" → recorded as a
standing go-ahead (memory `fpl-training-go-ahead-2026-10-31`): training launches no longer wait for gameweek reads; one
GPU job at a time still holds. H6b was already the retry (step 850/1,680 at 17:20 PDT, 62.6 s/step, verdict ~08:15 PST Sun).

**Wes's question:** Villa and Spurs are on the up (a Zhan Jun round-review channel says so); does the classic model see it,
and if not is that an SFT/RL argument? Answered with `scripts/team_trajectory_study.py` →
`reports/team_trajectory_study/README.md` on the stored walk-forward forecasts (39,619 player-weeks, 2022-23 → 2026-27 GW8).
Team level: next-game GD/game = 0.55 × prior-season level + 0.09 ±0.11 × last-5 streak; "rising" clubs (last-4 ≥ 8 pts,
finished ≥ 8th) manage −0.05 next game against +0.19 for the rest — streaks revert. Player residuals: rising-club players
+0.15 ±0.13 vs everyone else +0.17 ±0.04; own trend coefficient −0.03 ±0.05; regulars of clubs in a cold run +0.13 vs hot
run +0.02 (the model follows short team form a touch too far); attackers facing a hot opponent +0.34 ±0.12 (over-penalised).
2026-27 so far: Brighton's players +119 points above forecast on regulars (3.2 GF / 0.2 GA over five), Leeds +56,
Bournemouth +54, Villa +32 (Jackson, Suzuki, McGinn), Spurs 0 (defence +44, attackers −30), Chelsea −40. The features
already carry Villa at 1.8 GF/game and Spurs at 1.0 GA/game going into GW9. Verdict: not an SFT/RL argument; the only
measurable gap is the reverse one, which a longer baseline could fix → **F19** (`scripts/add_team_level_features.py`:
own/opponent prior-season GD/game, season-to-date GD/game, promoted flags; `FPL_TEAM_LEVEL_FEATS=1`, default off;
config TL1_F; `scripts/run_f19_teamlevel_chain.sh`, 21 windows at JOBS=3 against the PB_F baseline, xPts label
f19_teamlevel). Lesson re-learned while wiring it: a process guard that names the script matches the shell running the
guard AND any parallel shell whose command text contains the name — exclude `$$` and run such guards alone.
**F19 verdict (17:33 PDT; the 21 windows took about a minute at JOBS=3):** TL1_F 5,233 vs PB_F 5,314 actual (−81, t −1.10,
wins 6-9, ties 6), xPts 5,122 vs 5,127 (−5, t −0.12), walk-forward MAE 1.0095 vs 1.0009, RMSE level. The columns reached
the fit (per-player forecasts move by 0.01-0.05) and bought nothing: null-to-negative, flag stays off, closed. Anchor features
added on intuition or on a small measured residual are now 0 for 11. Answer to Wes: the classic model already prices
team form at face value; beyond its 5-week window the "up-and-coming" story carries no points, so it is not an SFT/RL
argument either. Files: `reports/team_level_f19/` (bt, accuracy, xpts), `logs/f19_teamlevel_chain.log`.

## 2026-11-03 Tue evening: H6b verdict (late), GW9 settlement, H12 launched

**What went wrong first.** The H6b chain (`scripts/run_h6b_after_gw9.sh`) finished training Sunday 06:46 PST (29.2 h, 1,680
steps, 62.6 s/step, peak 17.4 GB) and both prediction sets by 07:16, then died on `N78: unbound variable` — `train_and_score`
was copied from the H6 chain without the GW7-8 split variables, `bash -n` cannot see that, and `set -u` ended the script
before any scoring and before the FAILED sentinel. The session had also lost its login, so the Sunday verdict cron and the
Tuesday settlement cron fired into nothing. Recovered tonight with `scripts/run_h6b_score.sh` (scoring half only, 5 min).
Lesson recorded in memory `fpl-chain-pipeline-stages`: assert path variables at the top of a chain, write FAILED from a trap,
keep scoring re-runnable.

**H6b verdict: FAILED the gate; the E4B points-residual recipe is closed.** Two epochs at the higher learning rates produced
the best-fitting adapter so far and the first with any mechanism, and it still bought nothing at the squad level.

| | H5 (MSE, 1 epoch) | H6 (+ numeric block) | H6b (+ 2 epochs, LR 1e-4 / 2e-3) |
|---|---|---|---|
| corr(Δmin, classic minutes residual) / corr(Δpts, residual) | 0.152 / 0.096 | 0.156 / 0.088 | 0.218 / 0.141 |
| sd Δpts / sd Δmin | 0.124 / 1.9 | 0.128 / — | 0.180 / 2.9 |
| 45-60 min band: Δmin vs classic residual +8.2 | +0.5 | +0.1 | +2.2 |
| Holdout RMSE (classic 3.420) / bias (classic +0.10) | 3.415 | 3.416 | 3.402 / +0.04 |
| Decisions, 3 holdout windows (classic 788) | 797 | 777 | 781 |
| Live GW2-6 (classic 315) / GW7-8 (classic 129) | 335 / 129 | 325 / 129 | 325 / 119 |
| 5-window Δactual / ΔxPts vs classic | +29 / +24 | −1 / +5 | −7 / +13 (t 0.40) |

Accuracy file `reports/h_series/h6b_accuracy.md` (decision-relevant rows 3.963 vs 3.995, closer 60%), mechanism
`h6b_band_check.md`, `h6b_mechanism_holdout.md`, xPts section `h6b_arms`. Loss (H5), inputs (H6), capacity (H31) and
optimisation (H6b) are now all measured on this recipe. GW10 shadow stays H5.

**GW9 settled: 49 vs average 47** (`reports/gw9_packet_2026_10/final/ledger_gw9.md`, season ledger row 9). Wes entered the
final call exactly. Konsa 10, De Cuyper 9, Rogers 9, Evanilson 9 against Haaland 2 (captain), Isak 2, Groß 2, McGinn 0;
57.7 expected. The transfer was −7 on the day against the Wednesday sheet's Thiago or Jackson (both 9) and −1 against holding
João Pedro; the captaincy −7 against the vice; N.Williams −1 against Justin (the SFT H5 XI scores 50); no hit was right
(−4 nets 48, −8 nets 47); Bench Boost would have been 57; the MILP wildcard/free-hit squads would have scored 79 (Van Hecke 15,
Jackson 9, Palmer 8) — one week after GW8's 39/32 vs 54, so the chip-calibration zero stands. H5 shadow read on 669 players:
points RMSE 1.831 vs 1.817, availability Brier 0.092 vs 0.130 (uncertain rows 0.139 vs 0.216). New tools: `scripts/settle_gw.py`
(API fetch + FPL auto-sub evaluator for hindsight XIs), `scripts/score_shadow_week.py` (shadow read vs settled points without
the table rebuild), `scripts/run_post_ingest_rebuild.sh` (cutoff bump + both tables + parity audit). Ingest OK, GW9 flagged 0.30,
cutoff now 9, GW10 parity audit in `reports/gw10_packet_2026_11/`.

**H12 launched 21:56 PST** (Wes: "would love to scale things further with latest AI/LLM approach", "could you run something
leveraging my free GPU"): Gemma-4-12B-it bf16 LoRA on the H6 recipe, `scripts/run_h12_chain.sh` (memory `fpl-h12-gemma12b`).
Rationale: H31's 31B tie was measured on the Huber recipe whose shrink defect the MSE loss later fixed, so capacity has not been
tested on the fixed loss; 12B is the largest dense Gemma that trains in bf16 under the 55 GB rule with a clean holdout. The
chain waits for the 24 GB download, smoke-tests three steps (abort above 50 GB), trains ~40-45 h, and scores against the frozen
GW8-cutoff table so the baselines stay comparable. Odds ~10-15%; if it ties, the reader line is closed at every scale on this
corpus and the honest next GPU candidate is data scaling (all players), otherwise the CPU decision-engine work.

**22:25-22:44 PST, H12 first attempt failed before the GPU, relaunched.** `google/gemma-4-12B-it` turned out to be the Gemma 4
*Unified* checkpoint (model type `gemma4_unified`, 11.96 B parameters in one 23.9 GB safetensors, saved with transformers 5.10),
which the production venv's transformers 5.6.0.dev0 cannot load (it knows `gemma4` only: E4B, 31B). Fix: a second venv,
`/home/wescheng/venvs/fpl-gemma-12b`, with transformers 5.22.1 and peft 0.21.2 on the same torch, used only by the chain's two
GPU steps through a subshell that activates it and execs `python3`, so the anchored guards and the memory watchdog still see
the job. Production venv untouched. Smoke test relaunched 22:44 PST; the layer tensors carry the standard q/k/v/o and
gate/up/down names, so the LoRA targets apply unchanged.
Smoke test 22:48 PST: 148.5 s/step, peak 25.4 GB (E4B 62.6 s / 17.4 GB), 65.6M LoRA params on hidden 3840; full run 840 steps
≈ 34.6 h → training ends ~Thu 09:30 PST, verdict ~Thu 11:00 PST.

## 2026-11-04 Wed late: GW10 interim packet (CPU), SFT read queued behind H12

Wes (22:20 PST): "what should i change my squad for the next GW ... run the pipeline (classic and SFT etc) for the upcoming GW10",
happy to wait for the GPU. One GPU job at a time, and `train_gemma_reghead.py` has no resume (checkpoints are saves, not restart
points), so the E4B H5 read waits for the 12B chain rather than pausing it. Done on CPU at 22:26-22:30 PST: the GW9 packet scripts
cloned to `reports/gw10_packet_2026_11/` with GW10 parameters (as-of week 10, GW10-14 horizon, event 10), `scripts/run_gw10_interim.sh`
(entry, snapshot, forecasts on the GW9-ingested table, decision sheet, exact optimizer, lineups, role override --auto, README),
`RECOMMENDATION_2026_11_04_interim.md`. State: bank 0.3, 1 FT, chips BB/FH/WC. **Call: Cunha → Rice (free), +4.8 GW10-14 / +1.3 GW10,
XI 62.2 vs hold 60.9, C Haaland VC Rogers, no chip**; Cherki → Rice is the single-week optimizer's equivalent; Donnarumma → Raya is the
GW11 free transfer the 0.7 left over makes affordable (two-step ≈ +10.7 vs the −4 pair +8.5 / rolled pair +9.4). Evanilson's P(appear)
1.00 → 0.74 traced to the minutes head (78/86/75 minutes, away, transfer surge), not the data; no route turns on him.
Queued: `scripts/run_gw10_interim_sft.sh` (waits for the chain sentinel after the re-arm marker or the chain pid, then Guardian/Scout
pulls, F6 live examples, team-news categories, H5 team-sheet examples, the H5 read, side-by-side, chip line; sentinel "GW10 INTERIM SFT
DONE"); `scripts/run_gw10_final_refresh.sh` armed for Fri 16:35Z (08:35 PST) with `scripts/apply_hand_edit.py` replaying confirmed
moves from `logs/gw10_hand_edit`; the F16 team-news table rebuilt on the GW9-ingested table (`scripts/run_teamnews_rebuild_gw10.sh`,
196,915 lines). H12 at step 540/840 (22:17 PST), 155.7 s/step (smoke 148.5) → training ends ~Thu 11:15 PST, verdict ~13:30-14:00 PST.
Crons: Thu 07:07 re-pick (ebcd3461), Thu 15:07 H12 verdict + GW10 SFT (6deba560), Fri 06:23 fallback (529dcc41), Fri 09:37 final
recommendation (329b6007).
Minutes-head quirk (decomposed 22:45 PST): Evanilson's 97.7 → 66.9 raw minutes is feature movement, not refit drift: transfers_in 961k −11.4 min, selected_change −9.4, transfer_balance −3.4; football terms net ≈ 0. The ridge reads a transfer bandwagon as a minutes risk. No GW10 route turns on it; candidate CPU bench: minutes head without the market-momentum features.

## 2026-11-05 Thu 07:07 PST: GW10 Thursday re-pick (CPU) — unchanged, no note sent
`PACKET_DIR=reports/gw10_packet_2026_11/thu scripts/run_gw10_interim.sh` (pid 646110, 07:07-07:10, snapshot 15:07Z, 670 forecasts on
the same GW9-ingested table, no step failed). Nothing moved: every squad player and target still `a` with no news (Saka `i` 0%);
forecasts drifted ≤ 0.05 on the market features (Evanilson 4.33 → 4.38 / P 0.75, Isak 4.73, Rice 4.86, Cherki 3.48 / P 0.46). Same
XI, bench, C Haaland VC Rogers. Routes: Cunha → Rice +4.9 now / +3.6 rolled (XI 62.3 v hold 61.0, hold EV 286.0); Donnarumma + Cunha →
Raya + Rice −4 +8.6 / rolled +9.5; three moves +7.8; WC +28.9 exact / −2.7 sheet; FH +7.3 / +1.1; GW10-only Cherki → Rice +1.4.
Call stands: **Cunha → Rice free, C Haaland VC Rogers, no chip.** Checks: sleepers 620297 (SFT waiter), 620569 (Fri refresh), chain
554315 and trainer 555162 alive; H12 step 740/840 at 06:58 PST, 155.8 s/step, eta 4.33 h → training ends ~11:20 PST, verdict
~13:30-14:00 PST as planned; `_teamnews` table (11-04 22:33) newer than the production table → no rebuild. Tonight's Europa/Conference
games (AVL, CRY, NFO) fall after this re-pick; the Fri 08:35 PST refresh picks up their fallout and the Guardian lineups.
Cosmetic: `final_summary.py` labels any non-root PACKET_DIR "GW10 final packet" with an empty "What moved since the interim packet"
table, so `thu/README.md` carries the wrong heading; harmless for `final/`.

## 2026-11-05 Thu ~07:50 PST: Wes — Cunha's Champions League brace; "fine-tune for much more football context?"
**Cunha.** MUN 3-2 Roma (UCL MD4, Tue 11-03): Cunha 83' + 86' from 0-2 down, second yellow in stoppage time (UEFA ban only; the
PL game v AVL Sun 16:30Z is unaffected). The model never sees European games (PL rows only; the own-team midweek effect tested
null), so the numbers did not move. What it holds against him is 6 / 45 / 65 minutes in GW7-9 → 61 min / P 0.68 / 3.55 GW10 /
17.1 GW10-14. Priced as a nailed starter from his GW9 start (`role_override_sheet.py --override Cunha:9`, `thu/role_override_cunha.md`):
3.64 / 17.3 (67 min, P 0.74), still short of Rice 4.86 / 22.0. (`--drop` is the wrong tool for "he is fit": a removed row reads as a
blank, Cunha 3.09.) Exact optimizer with the swap forced (`forced_routes.py`, `thu/forced_routes.json`): Cherki → Rice +4.3 GW10-14 /
+1.4 GW10 vs Cunha → Rice +4.9 / +1.3, a 0.6-point coin flip; both land on Rice with bank 0.7 (Raya affordable in GW11 either way).
Answer: call unchanged (Rice in); which midfielder leaves is Friday's Guardian-lineup question, and keeping Cunha on the strength
of the brace costs nothing material.
**Fine-tune for context.** Nothing could launch this morning (H12 holds the GPU to ~11:20 PST, then the chain's scoring and the GW10
H5 read). Assessment sent: knowledge is not the bottleneck (H31 31B tie, E18 blocks worth nothing, H6/H6b null, article audit: text
already priced by the market; the team sheet is the only text block that works, on availability); a 2025-26 football corpus leaks the
holdout (Gemma 4 cutoff Jan 2025) and pre-2025 text is already in pre-training, so the only clean corpus is 2026-27 text scored on
the live windows. One-line proposal on file: E4B continued pre-training on dated 2026-27 text + the H5 head, ~1 GPU day after H12,
odds 5-10%, ranked behind all-player data scaling; not launched without Wes's word.
**Follow-up, Wes: "this is what the SFT could help by reading the Europe game, right?"** Checked rather than argued. (1) The reader
already gets European text: the Guardian pull is the umbrella `football/football` tag (gw9final store: 39 UCL-tagged docs of 350),
the attach step keeps 14 days and 3 docs per player, and in GW9 122 of 669 prompts carried a UCL/UEL doc (835 of 1,575 attached docs
were live blogs). The training stores hold 34-51 UCL live blogs a season, so the model saw them in training too. (2) What it did with
them: Cunha's GW9 prompt quoted the Como 4-1 United blog ("comes on for Da Cunha", Como's player) and Forest 0-1 Arsenal ("Wood on
for Cunha", a Forest player) — `_name_pattern` is surname-only with no club check — and the H5 read moved his points by +0.01 and his
P(appear) 0.66 → 0.91 off the team sheet (he started, 65 min, 2 pts). (3) So the Roma brace will be in front of the reader this
afternoon if the API returns the blog, and the side-by-side will show the text behind any move; the honest expectation is a
P(appear) move, not a points move. Proposed, not applied (CPU, needs Wes's word): club-tag filter in the attach step, re-attach GW9
to count changed rows, and a "scored/assisted in Europe this week" fact parsed from the 2022-26 UCL blogs tested as a structured
feature against the PL residual. Recorded in memory `fpl-evidence-wrong-player-match.md`.

## 2026-11-05 Thu 15:07 PST: H12 verdict (tie → reader line closed at every scale), GW10 SFT sheet, Konsa flag
**H12 (chain done 12:48 PST, training 840 steps / 36.3 h / 155.7 s/step / peak 26.3 GB, no incident): FAILED the gate, a tie.**
Points: holdout RMSE 3.417 vs classic 3.420 (H5 3.415, H6b 3.402), live 3.426 vs 3.424; the 12B's delta is an almost constant shift
(mean −0.08, sd 0.031 holdout / 0.036 live vs H5 0.106 / 0.124, H6b 0.180), corr(Δpts, residual) 0.060 holdout / 0.086 live (gate
> 0.16-0.2), band check flat at −0.06 in every minutes band. Availability: holdout AUC 0.707 vs classic 0.704 vs H5 0.776, live
corr(Δmin) 0.042 vs H5 0.152 — the bigger model learned less of the availability head. Decisions over 5 windows (xPts section
h12_arms): +9 actual (sd/window 3.5, the squads are nearly classic's) / +14 xPts (t 0.70) vs H5 +29 / +24, H6 −1 / +5, H6b −7 / +13;
RESULT holdout 796 vs classic 788 vs H5 797; live GW2-6 316 vs 315 vs 335; GW7-8 129 = classic = H5. With loss (H5), inputs (H6),
optimisation (H6b), capacity on the Huber recipe (H31) and now capacity on the fixed loss (H12) all measured null, the SFT
points-residual line is closed at E4B, 12B and 31B on this corpus. `logs/gw10_shadow_adapter` not written: the Friday read stays H5.
Proposed with odds, none launched: all-player data scaling on E4B (~90k rows, ~4 GPU days, ~10%); CPU multi-week transfer MILP
(~40% of a measurable +20-40/half on the 21-window xPts bench); the CPU lines from this morning (club-tag evidence matcher +
European-form fact study; minutes head without market momentum).
**GW10 SFT (H5 read 13:00 PST, 670 rows in 8.7 min; Guardian 333 new docs, Scout 36; no predicted-lineups article yet — Friday):**
XI, bench, C/VC identical to classic; 60.6 vs 59.6 as written; generic shrink +0.086 × classic − 0.308. Movers: Konsa 3.75 → 3.44
(knee, "subbed off during the midweek win"), Haaland −0.56 specific (+0.44 generic), Cunha 3.55 → 3.43 with P(appear) 0.68 → 0.91
reading the Roma blog + match report (right player this time: "Cunha double floors Roma") — the availability channel moved, the
points channel went DOWN 0.11 on a brace, exactly the pattern H5's verdict measured; Cherki P 0.46 → 0.71, McGinn 0.82 → 0.95,
Evanilson 0.76 → 0.96, Isak 0.76 → 0.94. Chip line (`reports/chip_line_gw10_interim.md`): no DGW/BGW published this half, planner
rule = Bench Boost now (+12.0, bench Sels 2.4 / McGinn 3.4 / Justin 3.2 / Mitchell 3.0; best of the next 4 weeks 11.1).
**Konsa flagged since the morning:** `d`, "Knee injury - 75% chance of playing" (ARS, v HUL Sat 15:00Z). Afternoon re-pick
`thu_pm/` (pid 665490, snapshot 23:09Z): Konsa 4.24 → 3.75 GW10 / 18.1 → 16.3, P 0.81, still in the XI (Justin 3.18, Mitchell 3.00);
routes unchanged — Cunha → Rice +4.9 / rolled +3.6 (XI 62.0 v hold 60.7), pair +8.7 / +9.5, three +7.8, WC +30.9 exact / +0.9 sheet,
FH +7.9 / +1.6, GW10-only Cherki → Rice +1.4. Call stands; Friday's Guardian lineups decide Konsa (Justin/Mitchell cover) and Cherki v
Cunha. GPU idle; final refresh sleeper 620569 alive for Fri 16:35Z.

### 2026-11-05 Thu ~16:30 PST: Wes confirms Cunha -> Rice

Wes: "got it so i transfer out cuhna for rice - what's my bench order?" Answered from the thu_pm re-pick: XI Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Gross, Rice, Cherki; Haaland (C), Isak, Evanilson; VC Rogers; bench Sels > McGinn > Justin > Mitchell (62.0 before the Konsa doubt resolves). Recorded `Cunha:Rice` in `logs/gw10_hand_edit` for the Friday refresh replay (dry-run on the thu_pm entry state passed). Autosub logic checked for the Konsa 75% flag: McGinn cannot replace a DEF (2 DEF invalid), so Justin comes in automatically; McGinn first still right because he covers any MID/FWD absence at 3.4 vs Justin 3.2.

### 2026-11-06 Fri 09:45 PST: GW10 final recommendation

Refresh fired 08:35 PST and finished 08:50 with no failed step; the Cunha → Rice hand edit replayed (bank 0.7, 0 FT). Final:
Cunha → Rice (confirmed), no further transfer, no chip; XI Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Rice, McGinn;
Haaland (C), Isak, Evanilson; VC Rogers; bench Sels > Cherki > Justin > Mitchell; GW10 XI 63.2, hold EV 293.6. Konsa cleared
overnight. McGinn over Cherki by 0.09 (classic decides); the Guardian lineups (published 16:43Z, eight minutes after the refresh's
pull, so re-pulled at 09:40 and the F16 shadow replayed on CPU, no-article outputs kept as final/*_noarticle.*) list all 15 in XIs
and the lineup-aware shadow prefers Cherki (+0.16). SFT H5 sheet identical XI (63.3 v 62.6). Chip line's planner rule = BB now
(+11.9); recommendation no chip (projected-gain trigger loses; WC at the GW11 break, BB on the rebuilt bench). Donnarumma → Raya
is GW11's free move (+6.0 rolled). File: reports/gw10_packet_2026_11/RECOMMENDATION_2026_11_06_final.md. Runbook note: wake the
final refresh ~17:00Z (GW8 lineups 15:42Z, GW9 16:19Z, GW10 16:43Z).

### 2026-11-08 Sun: the project goes on GitHub

Wes asked for the work to be checked in so he can show it in interviews. Created the private repo
https://github.com/dreamland701/fpl-ai-recommender from this directory (first commit 2,845 files, 27.5 MB): code, tests,
docs, markdown write-ups, the Codex review and the ridge coefficients. Excluded by `.gitignore`: weights (87 GB), data tables
(4.8 GB), evidence stores (Guardian/Scout article text), logs, forecast/snapshot payloads. Scans before the push: Guardian key
value, email address and raw article dumps all absent from the staged tree. Root README rewritten for an outside reader; the
July CLI quickstart moved to docs/cli_quickstart_2026_07.md. Commits are identified by the GitHub noreply address.

Later the same day Wes asked for the repository to be made public. Re-ran the scans on the tracked tree (no secret patterns,
no credential-looking paths, email and Guardian key value absent); the only third-party text in the tree is 164 short
attributed excerpt lines (122 Guardian, 42 Premier League) inside the side-by-side write-ups, no article bodies. Added an MIT
LICENSE (copyright Wes Cheng) and a license note to the README, pushed, then flipped the visibility to public and set topics.
