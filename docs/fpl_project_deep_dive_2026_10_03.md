# Teaching a Small LLM to Play Fantasy Football

### The complete record of the FPL forecasting project, April – October 2026: what we built, every experiment and its verdict, what worked, what didn't, what surprised us, and what it all means

*Written 3 October 2026, between GW5 and GW6 of the 2026-27 season, for Wes to read slowly and reflect on. Sources: every design doc and experiment log in `docs/`, all 41 project memory notes, the full main-session transcript (5 July – 29 September), the code itself (read line by line for the algorithm chapters), and the on-disk reports (96 decision backtests, 50+ trained adapters, dozens of evaluation summaries). Where a number appears, it was read from a file or a recorded verdict, not reconstructed from memory. Where something is uncertain, the text says so.*

---

## How to read this document

This is long on purpose. It is meant to be a reference you can come back to, so it is organized so that you can read it in more than one way.

- **If you have thirty minutes:** read Part 0 (the short version), then Part VI (the surprises) and Part VII (the lessons). Those three together carry most of the meaning.
- **If you want to understand the machine:** Part II describes the system exactly as it is built today, with the actual formulas, parameter values and file locations, including a real prompt the model sees.
- **If you want the story:** Part III is chronological, from the first 31-billion-parameter experiments in April to the adapter analysis of 29 September and the audit done while writing this (3 October). Every experiment is written up the same way: *the intuition, what we changed, what happened, the verdict, and what it taught us.*
- **If you only read one new thing:** Section 3.10 and Part II §2.12. Writing this document meant reading every algorithm line by line, and that surfaced findings that revise earlier conclusions. The most important are why the adapter "shrinks" (it is a median estimator), what it really adds over a fair baseline (little), and four data defects that are probably the best work available now.
- **If you want to look something up:** Part IV is a master ledger of every experiment with its numbers, and the appendices hold the glossary, the file map, the training-run table, the complete backtest scoreboard, and a timeline.

A few conventions are used throughout:

- **GW** means gameweek. "GW12-30" means gameweeks 12 through 30 inclusive.
- **Classic** or **the anchor** means the ridge-regression forecaster. **The adapter** means the LoRA fine-tuned Gemma model that corrects it.
- **MAE** is mean absolute error of a points forecast against what the player actually scored. It is a *diagnostic* in this project, not the shipping metric.
- **Decision value** means the actual FPL points scored by the squad that the decision layer builds and manages from a given set of forecasts, in a walk-forward backtest. This is the shipping metric.
- **A window** is one decision backtest over a contiguous block of gameweeks (usually 4). **σ (sigma)** expresses a decision-value difference in units of its measured noise.
- **E-numbers** (E1 … E19) are forecast-layer supervised fine-tuning runs. **G-numbers** (G1 … G4) are reinforcement-learning runs. **F-numbers** (F1 … F12) are changes to the classic anchor or decision layer that were tested on CPU.


---

# Part 0 — The short version

## The story in one paragraph

The project set out to build a Fantasy Premier League assistant for the 2026-27 season in which a **fine-tuned language model does real forecasting work**, not a wrapper around a spreadsheet model. After a spring of failures with a 31-billion-parameter Gemma asked to pick squads, rank players or forecast points from scratch, we settled on an architecture that held for the rest of the project. A classic ridge-regression model produces a forecast for every player. A small Gemma-4-E4B model, fine-tuned with LoRA, reads that forecast, the player's structured context and a couple of short, timestamp-safe news snippets, and outputs **bounded corrections** as strict JSON. An exact optimizer turns the corrected forecasts into a legal squad, transfers, captain and bench order. That stack shipped for GW1 on 21 August 2026. It reliably improves forecast *accuracy*. Whether it improves *decisions* turned out to be the hard question. The best-supported answer, after twelve weeks of holdout in E19 and a 21-window replication on 29 September, is that **the adapter's net decision value is close to zero**. Meanwhile, the largest measured gains came from fixing specific, diagnosed defects in the classic model and the pipeline: label truncation, a cold-start bug, a dead injury flag, and most of all a fixture-blindness defect (F6) worth +112 points across five backtest windows. Writing this record turned up more of the same kind: the adapter's "shrink" is a median-seeking artifact of greedy decoding; a plain logistic classifier beats the LLM at predicting who plays; and four defects in the data foundation (end-of-season injury snapshots, end-of-season club assignments, mismatched ownership units live, a blend that never went live) are now the most promising work available (Section 3.10).

## The scoreboard

**Live season 2026-27, five settled gameweeks:**

| GW | Our score | Overall average | Difference | Captain (raw pts) | Transfer |
|---|---|---|---|---|---|
| 1 | 38 | 50 | −12 | B. Fernandes (2) | — (initial draft) |
| 2 | 85 | 79 | +6 | João Pedro (9) | Watkins → João Pedro |
| 3 | 38 | 51 | −13 | B. Fernandes (2) | O. Dango → Cherki |
| 4 | 61 | 69 | −8 | B. Fernandes (2) | Richarlison → Isak |
| 5 | 61 | 48 | +13 | Saka (2) | Shaw → Konsa |
| **Total** | **283** | **297** | **−14** | | |

Two things stand out. First, captaincy has been brutal: Bruno Fernandes was captained three times for 2 raw points each, and the week he scored 23 we had captained João Pedro. Second, two of the five weeks include a defect we found and fixed afterwards. In GW1 the sheet never specified bench order, which cost 9 points. In GW2 a walk-forward bug would have collapsed every forecast; it was caught before decoding.

**The research ledger:**

- **Forecast accuracy:** every adapter from E1 onward beats the classic model on MAE. The best, E15, reached a 1-gameweek MAE of 2.059 against classic's 2.211. Strict-JSON output is 100%, against about 68–76% for the un-tuned base model.
- **Decision value:** adapters beat classic in single windows (E7 +11, E7-chrono +53, E9 +82 over 29 weeks). On the properly powered test (E19's three independent windows plus 18 more replicated from older decodes), the deployed-style adapter nets **+39 points over 21 windows**. That is indistinguishable from zero.
- **Input and capacity scale-ups** (more evidence, longer windows, a market line, podcasts, more RL agency, more epochs): **none paid.** That is 0 for 10 by the September retrospective's count, and about 0 for 14 by the broader count in Part IV.
- **Diagnosed fixes** (rate-normalized labels, walk-forward live frame, F2b prior blend, F6 opponent interaction, the status backfill, bench-order output, settled-data gate): almost all paid. F6 is the largest measured win in the project.

## The ten things this project taught

1. **Accuracy and decisions are different targets, and the adapter optimizes the wrong one by construction.** Fine-tuned with cross-entropy on number tokens and decoded greedily, the adapter returns roughly the *most likely* residual, the median of a right-skewed distribution, not the mean. That improves MAE, worsens RMSE, cuts the biggest forecasts hardest, and leaves rankings unchanged. On E19, a one-line linear shrink recovers about 90% of the adapter's accuracy gain and has zero decision value.
2. **The LLM's genuine information is smaller than it looked.** Against the classic model's crude "minutes ÷ 90" appearance probability, the LLM looked strong late in the season (AUC 0.72 vs 0.55 among likely starters). Against a proper logistic classifier built from the same features, it is weaker on its own (0.72 vs 0.74), and adds only +0.01 to +0.02 AUC when combined. Live in 2026-27 it adds nothing over classic alone.
3. **Diagnosis beats scaling.** Every large win started from someone naming a specific defect, usually Wes looking at one player: Haaland ranked 43rd, Konsa below his own backups, Evanilson unpunished against Liverpool. Every attempt to win by adding more inputs or more capacity came back flat.
4. **The prompt can switch a channel off.** The adapter was told in its own prompt that fixtures were "already priced" by the anchor. It obeyed, so neither layer was modelling the fixture.
5. **A single evaluation window can mislead you for months.** From E10 in August until late September, every adapter verdict was measured on GW35-38 of 2025-26. That turned out to be the one window of three where the adapter wins.
6. **Know your noise floor, and measure it for the kind of change you are testing.** About 15 points per 4-week window for small anchor tweaks; 24–40 for adapter comparisons, because adapters change the drafted squad far more.
7. **Never promote a proxy to a verdict.** A cheap "top-11" proxy overstated the decision-weighted loss 30×. G4's reinforcement-learning reward used a proxy that inverted the sign of the thing we cared about.
8. **Gates pay for themselves the first time they fire.** Sanity gates caught a corpus that had silently lost two-thirds of its evidence, a prompt block missing from all 37,888 training rows, and a mid-week score narrated as final. Each would have cost days.
9. **Planning depth is worth nothing here; forecast quality is worth everything.** With perfect information, banking free transfers never helped at one transfer per week. The gap between perfect forecasts and ours is about 738 points a season, and all of it is ranking skill.
10. **Calibration fixes can cost points.** Premiums really are over-forecast by about a point a week. Correcting that makes the forecast honest and the squad worse, because at equal forecast levels premiums still out-score the alternatives.

## Where things stand on 3 October 2026

- **Deployed today:** the old classic anchor plus the E11-full adapter (trained through 2025-26 GW38). The F6 anchor has been adopted for evaluation but not yet flipped live, because the deployed adapter was trained against the old anchor's baselines.
- **Recommended for GW6 (deadline 10 October):**
  - Fix the live ownership units and the live F2b blend first; both are small CPU fixes.
  - Then let classic+F6 make the decisions. This is the shadow-mode fallback your own rule allows when the LLM fails its gate.
  - Keep logging the adapter weekly, measured against a *proper* appearance classifier rather than minutes ÷ 90.
  - The first adapter experiment worth GPU time is expectation decoding, which tests the median-seeking diagnosis without retraining.
- **Found while writing this (3 October), and worth fixing before anything else:**
  - historical injury status and news are end-of-season snapshots copied onto every week (leaky and noisy);
  - players' clubs are end-of-season clubs, contaminating ~30% of team-form values, including F6's inputs;
  - ownership is a raw count in training but a percentage live, so live forecasts have under-rated popular players all season;
  - the F2b blend never reached live features.

  The last two affect the GW6 sheet directly, and the backtest harness has smaller defects of its own (Part II §2.12).
- **The research question that remains, stated as precisely as possible:** *can an LLM reading pre-deadline news predict who plays better than the best simple model can, consistently enough to change squads?* The measured answer so far: a small complementary signal (+0.017 AUC live over a logistic classifier), and not yet a decision gain.


---

# Part I — The mission, the game, the machine, and the data

## 1.1 Two goals, and why the second one shaped everything

Your own words, written into the project summary on 3 July 2026, set the terms:

> 1. I wanted to make this ready as a predictor for the next FPL season, which I can use every GW to pick my squad / make transfers / use chips if needed
> 2. also for me to validate how LLM fine-tuning could work successfully (so let's not use a pure classical ML solution)

When you approved the season plan on 5 July you sharpened the second goal into a standing rule that every later session inherited: **the fine-tuned LLM must be load-bearing.** Classic machine learning is welcome as one input signal the LLM reads, but not as the authority the LLM merely nudges. A system that is 95% ridge regression with cosmetic LLM adjustments would not answer the question you were asking.

That rule had three consequences that run through the whole record:

1. **Negative results are deliverables.** If fine-tuning does not help, measuring that honestly is itself an answer to goal #2. This is why so many experiments below end with "NULL" or "NEGATIVE" written plainly.
2. **A classic-only system is acceptable only as a fallback.** The plan of 5 July said that if the LLM failed its gate, classic would ship as the default with the LLM in shadow mode, logging its counterfactual picks, "and the season launch does not slip." That clause matters again at the end of this document.
3. **"Load-bearing" has to be measured, not assumed.** By September we had learned that a model can sit in the pipeline, change every number, improve accuracy, and still contribute nothing to decisions. Section 3.7 shows how its prompt even talked it out of the one job it should have been doing.

## 1.2 The game, in the detail that matters for modelling

Fantasy Premier League has rules that shape the modelling problem in non-obvious ways, so they are worth stating once.

- **The squad** is 15 players: 2 goalkeepers, 5 defenders, 5 midfielders and 3 forwards. The budget is £100.0m, with at most 3 players from any one club. Positions are fixed by the game. A player like Matheus Cunha is a "midfielder" even if he plays up front, which is why a straight Cunha → Haaland swap is illegal.
- **Each gameweek** you choose a starting XI in a legal formation (1 GK, at least 3 DEF, at least 2 MID, at least 1 FWD) and a captain, whose points are doubled. The vice-captain is doubled only if the captain doesn't play. The four bench players are **ordered**. If a starter doesn't play, the first bench player in your listed order who keeps the formation legal comes on automatically. GW1 taught us that this ordering is a decision output in its own right.
- **Transfers**: one free transfer per gameweek, which can be banked; extra transfers cost 4 points each (a "hit"). Our backtests model a simpler version (at most 2 banked, 1 transfer per week). The oracle test in Section 3.3 shows that banking has essentially no value at that cadence anyway.
- **Prices** move with demand. When you sell, you receive your purchase price plus *half* of any rise, rounded down to £0.1m. Your budget is therefore path-dependent, and the code reconstructs selling prices from purchase prices.
- **Chips**: since 2025-26 each manager has two of each chip (Wildcard, Free Hit, Bench Boost, Triple Captain). One copy is legal in GW1-19 and a fresh copy in GW20-38, whether or not the first was used. Section 3.4 records how the first chip-budget fix got this wrong and you caught it mid-training.
- **Scoring** rewards minutes (an appearance point, and a second for 60+ minutes), goals (worth more for defenders than forwards), assists, clean sheets (mainly for GK/DEF), bonus points awarded from a statistic called BPS, and since 2025-26 a **defensive contribution** ("DefCon") bonus of 2 points. DefCon is awarded when a defender reaches 10, or a midfielder or forward reaches 12, combined tackles, interceptions, clearances, blocks (and recoveries for non-defenders) in a match.
- **Deadlines** fall 90 minutes before the first kickoff of the gameweek. Rearranged fixtures create **double gameweeks** (a team plays twice) and **blank gameweeks** (a team doesn't play).

Three features of this game make it statistically hostile:

1. **Points are spiky.** Most player-weeks are 1–3 points; the money is in rare hauls. A forecaster that predicts "about 2" for everyone has a decent MAE and is useless for picking a squad.
2. **Decisions depend on the top of the distribution.** Of roughly 650 players, you own 15, start 11 and captain 1. Errors on the 600 you never consider don't matter; errors at the top matter enormously, and the captain multiplier doubles them.
3. **Outcomes are noisy.** A single four-week stretch of squad points has about 15 points of irreducible randomness for small changes, and more for large ones (Section 3.9). This is the root of most of the false positives this record will catalogue.

## 1.3 The machine

Everything runs locally on a **DGX Spark** with a GB10 Grace-Blackwell chip: aarch64, 119 GB of *unified* memory shared between CPU and GPU, CUDA capability 12.1, and roughly 273 GB/s of memory bandwidth. That bandwidth figure is the important one. The box is bandwidth-bound, so free memory does not translate into speed, and long prompts cost almost linearly in time.

Facts about the machine that shaped decisions:

| Fact | Consequence |
|---|---|
| Gemma-4-31B LoRA took ~16 minutes per optimizer step | One epoch took ~9 days; iteration was impossible. Pivoted to Gemma-4-E4B (an "effective-4B", ~8B-raw model) on 5 July. |
| E4B steps take ~41 s (short prompts) to ~87–110 s (1,000–1,250-token prompts, batch 1 × grad-accum 16) | A full forecast-adapter run is 45–72 hours. "One experiment per day" was the hope; one every 2–3 days was the reality. |
| Batch 8 × seq 1024 bf16 OOM-kills the box (and takes down tailscale and the desktop with it) | Batch 2 × accum 8 for prompts under ~900 tokens; above that, batch 1 × accum 16 from the start. |
| "Fits at launch ≠ survives" | A 926-token batch-2 run drifted from 22 GB free to 0 by step 186 (allocator growth) and had to be killed. |
| The box has lost power (8 July) and rebooted (8 September) | `save_steps=100` everywhere. Trainers get `oom_score_adj 800`, so the kernel kills the trainer before system services. Chains on disk must be re-armed after any reboot. |
| No CUDA CTranslate2 on aarch64 | faster-whisper is unusable; podcast transcription used transformers Whisper large-v3 at ~2–4× realtime. |
| SDPA already dispatches to a native flash kernel | The flash-attn package is unnecessary (and unavailable for sm_121). |
| Batched left-padded generation (batch 16) | ~11× faster decoding: a 2,432-row eval pass in ~12 minutes, a weekly live decode of ~650 players in a few minutes. |
| HF xet downloads stall | `HF_HUB_DISABLE_XET=1`. |

## 1.4 The data

### Structured history

- **Seasons 2019-20 through 2024-25** come from the public `vaastav/Fantasy-Premier-League` archive (`merged_gw.csv`, `players_raw.csv`, `fixtures.csv` per season).
- **2025-26** originally came from the official FPL API's backfill path for GW1-30. It was refreshed from the vaastav mirror for the full season (GW1-38) in early August.
- **2026-27** comes from the official API, synced weekly by `scripts/run_weekly_ingest.sh`.
- The canonical training table is one row per **player × pre-deadline gameweek**. It held ~184k rows in July; the current F6 table has 194,240 rows eligible for training.

### Data facts that turned out to matter

These are the less obvious ones, each found the hard way:

1. **FPL's numeric `player_id` is not stable across seasons.** Live id 411 was Haaland in 2026-27, but id 411 in 2025-26 belonged to Nico O'Reilly. The stable per-person key is `code`, and every cross-season join must use it. Historical seasons also store full names ("Gabriel dos Santos Magalhães") while 2026-27 stores web names ("Gabriel").
2. **Club identity changes format, and is an end-of-season value.** `merged_gw.csv` stores a club *name* for 2020-21 to 2025-26 and a numeric *id* for 2026-27. A script that keyed on `int(team)` silently produced zero opponent records for every training season; the E17 prompt gate caught it. Separately, the pipeline takes each player's club from the end-of-season snapshot. Mid-season movers therefore carry their old club's matches into their new club's team-form statistics, contaminating 24–36% of team-weeks (Section 3.10).
3. **Rearranged fixtures are tagged with the round they were actually played in.** Arsenal-Wolves moved from GW31 to GW26 of 2025-26, and City-Palace to GW36. The source data already handled this correctly, so no fix was needed. A stale guard that excluded 2025-26 GW31+ from training was removed on 6 August.
4. **Historical status and news have never been genuine pre-deadline values.** The official-API backfill neutralizes them, writing `status = a` and empty news on every historical row to avoid leaking current injury news into the past. So every adapter from E1 to E9 trained and evaluated on 2025-26 rows with blank injury flags. In August, E10 switched 2025-26 to the vaastav archive (status distribution a 14,316 / u 6,181 / i 1,332 / d 319 / s 116), believing those were real historical values. **They are not.** As verified on 3 October, they are each player's *end-of-season* status from `players_raw.csv`, copied onto every week; no player has more than one status in any historical season. Martínez is "suspended" for all of 2024-25 despite playing 3,195 minutes. The same holds for every historical season used in training, so the anchor's injury features and the prompts' status/news lines were learned from leaky, noisy values (Section 3.10).
5. **The same neutralization hit the live 2026-27 season.** Every row read `a`, so Saliba was "available" with zero minutes for four straight weeks. The fix restores pre-deadline status from our own archived weekly corpora. That is chrono-legal by construction, since we observed the values before each deadline. It now runs every week.
6. **Defensive contribution data exists only from 2025-26.** The 2022-24 files have no tackles, clearances, blocks or recoveries columns at all, because FPL did not publish them before the rule existed. Labels from those seasons never include a DefCon bonus.
7. **"Selected by percent" is a raw count in history and a percentage live.** The vaastav column is a count of managers (median ~20,000, max ~9.5 million), stored under the name `selected_by_percent`. The live API gives a percentage. The model was trained on counts and is fed percentages every week (Section 3.10).

### Evidence corpora (text)

| Source | How collected | Coverage | Notes |
|---|---|---|---|
| The Guardian (football tag) | Open Platform API, full `bodyText` | 25,852 articles, 2022-26; ~150/week | General football, not FPL. About 40% of a random sample was fantasy-irrelevant, but per-player name matching filters most of it. Was ~90% of evidence documents. The shared "test" key died with a 401 on 10 September; you registered a real key the same day. |
| Official PL / FPL Scout | Pulselive API, tag `content-creator:The-Scout` | 2,808 articles, 2021-26; Scout Selection every week of every season | The highest-value source: first-party FPL analysis (captaincy, differentials, price changes, team news). |
| Sky Sports written FPL tips | Wayback CDX + live fetch | 49 articles, 2022-23 to 2023-24 GW14 | High quality, but the column was discontinued and contributes nothing after 2023-24. |
| Sky Sports Fantasy Podcast | RSS → MP3 → Whisper large-v3 | 79 relevant episodes, 2024-26 (feed only from Aug 2024) | Richest raw content (30–50k chars/episode). Noisy: ~16% chunk-boundary duplication, name mis-hearings ("Claude Palmer"). |
| Sky Sports Premier League Podcast | RSS audited | 1,697 episodes back to 2015 | Audited, never transcribed (E8's negative result closed this). |
| PL / Sky full text 2025-26 | canonical URL resolution | 2025-26 | |
| Google News RSS, BBC RSS | RSS | snippets / current only | Fallback only. |
| Competition fixtures | fixturedownload.com feeds (browser UA required) | UCL/UEL 2022-25, UECL 2024+ | Used for congestion features and prompt blocks. |

### The leakage rules

Every experiment respects these, and most are enforced mechanically rather than by convention:

1. Features and evidence for gameweek *k* must have been available before gameweek *k*'s deadline. Evidence rows carry `published_at`, and anything published after the deadline is excluded.
2. Labels are realized points after the deadline, computed per **deadline window**: all fixtures between this deadline and the next, regardless of nominal round. This handles double gameweeks.
3. **An adapter never adjusts a week inside its own training window** (the "two-model ledger", Section 3.4). The classic model can be refit weekly in seconds; an LLM refit costs 20–70 GPU hours, so adapters are trained to a season-level cutoff and only do inference beyond it.
4. **A known soft spot:** training rows at the cutoff carry 3-gameweek and 5-gameweek labels, so an adapter trained "through GW11" has seen GW12-15 outcomes in label form. All rungs share this identically, so comparisons between them stay fair, but absolute margins on the first ~4 eval weeks are slightly flattered.
5. **Two violations found on 3 October** (Part II §2.12). Historical "pre-deadline" status and news are end-of-season snapshots, so they leak future availability into past weeks. And the backtest's weekly refit uses 3- and 5-gameweek labels that reach into the weeks being tested. Neither breaks the comparisons between arms, but both make absolute numbers optimistic.


---

# Part II — The system, precisely

This part describes the system as it exists on 3 October 2026, read from the code. File paths are relative to the project root; line references are approximate.

## 2.1 The architecture in one picture

```
                FPL history (vaastav 2019-26, official API 2026-27)       evidence corpora (Guardian, PL Scout, Sky, …)
                                   │                                                     │
                       normalize_vaastav_history                          attach_player_evidence_to_corpus
                                   │                                     (name match, 7-day lookback, top 3 docs)
                         build_training_frame                                            │
             (player × week; lagged rolling features; labels)                           │
                                   │                                                     │
                     ridge suite, refit weekly  ──►  classic forecast ──►  prompt builder (one prompt per player-week)
                (minutes, 1GW, 3GW, 5GW points)        (6 numbers)                 │
                                   │                                     Gemma-4-E4B + LoRA adapter (greedy decode)
                                   │                                               │
                                   └──────────► forecast + clipped deltas ◄────────┘
                                                       │
                       decision layer: lineup / captain / bench / transfers / draft (exact, deterministic)
                                                       │
                                weekly sheet (entered by hand)  ·  rolling backtest (evaluation)
```

## 2.2 From raw data to a player-week table (`src/fpl_ai/dataset.py`)

**Normalization** (`normalize_vaastav_history`): one row per player per fixture. `player_id` is the season-specific FPL id; `code` is the stable person id used for every cross-season join. Club (`team_id`), position, and in historical seasons also **status and news**, come from the season's `players_raw.csv`. That file is an end-of-season snapshot, so these values are the same for every week of a historical season (see §2.12, defects A and B). Era flags record whether a season has xG data (from 2022-23) and defensive-contribution data (from 2025-26).

**Aggregation** (`build_training_frame`): fixtures are summed into player-weeks (a double gameweek sums two matches). **Blank weeks are inserted as zero rows**, so rolling windows count them.

**Rolling form features.** Every one is `series.shift(1).rolling(window, min_periods=1).mean()` within (season, player). It describes the state *before* the week, resets at each season boundary, and is zero in week 1:

| family | windows |
|---|---|
| points, minutes, appearance rate, played-60 rate | 1, 3, 5, 8 |
| bonus, BPS, influence, creativity, threat, ICT, starts | 3, 5 |
| expected goals / assists / goal involvement / goals conceded (0 before 2022-23) | 3, 5 |
| defensive contribution average, DefCon hit rate (0 before 2025-26) | 3, 5 |

**Team and opponent form.** `team_goals_{for,against}_avg_{3,5}` and the opponent equivalents are lagged means of the club's weekly goals, computed from the fixtures attached to player rows.

**Market, fixture and status features**, lagged one week: price, ownership, transfers in/out and balance, price and ownership change, fixture count, difficulty (FPL's 1–5 FDR, mean and min), home ratio, blank and double flags, and binary status/news flags. The opponent's team id also enters as a plain numeric feature.

**Flag-gated blocks** (all default off unless noted), the experimental history in code form:

| flag | features | status |
|---|---|---|
| `FPL_PRIOR_BLEND` (F2b) | `points_avg_{1,3,5,8} ← w·current + (1−w)·prior-season per-week mean`, `w = min(1, appearances_so_far / 6)`; w = 1 with no prior season; availability features never blended | Adopted in training tables; never reached live features (§2.12, D) |
| `FPL_OPPONENT_INTERACTION` (F6) | `opp_def_weakness_w = opp_GA_w − season mean`; `form_x_opp_weakness_w = points_avg_w × weakness`; `xgi_x_opp_weakness_w = xGI_avg_w × weakness` (w = 3, 5) | Adopted (E17–E19, classic+F6) |
| `FPL_PRIOR_BLEND_TEAM` (F2c) | the same blend for team goal rates | Rejected |
| `FPL_CLEAN_SHEET_FEATS` (F5) | clean-sheet rate, goals-conceded average (3, 5) | Rejected |
| `FPL_DEPTH_CHART` (F7) | positional minutes share, rivals unavailable, rival minutes vacated, unit size | Rejected |
| `FPL_FINISHING_REGRESSION` (F8) | goals − xG, assists − xA, involvement − expected (3, 5) | Rejected |
| `FPL_CONGESTION_FEATS` (F9) | European game within 4/7 days, rest days, club matches in 14 days, × minutes | Rejected |
| `FPL_FORM_VS_UNDERLYING` (F10) | pct_rank(xGI) − pct_rank(points) within week, × minutes | Unresolved |
| `FPL_TEAM_ATTACK_INTERACTION` (F12) | centred team attack × xGI, × minutes | Unresolved |

The code holds 106 possible features. The current F6 table has **76 active** (70 base + 6 F6) over 194,240 rows.

**Labels:**

```
label_points_1gw  = points scored in the week (0 if he didn't play; summed over a double gameweek)
label_minutes_1gw = minutes (up to 180 in a double gameweek)
label_appearance  = 1 if minutes > 0
label_points_Hgw  = (Σ points over weeks k … k+H−1) × H / (number of those weeks that exist)   for H = 3, 5
```

The last factor is the **rate normalization** added on 21 August. Before it, multi-week labels shrank toward zero in the last four weeks of every season. Points labels are **unconditional**: a player who doesn't play scores zero, so availability is already priced into the points heads.

**The live frame** (`build_live_week_frame`): the official API snapshot supplies price, ownership, status, news and this week's fixture. Form features come from `_build_next_week_form_features`, which appends one synthetic week-(k+1) row per player (identity kept, match statistics blank, next opponent from the fixtures file) and runs the ordinary feature pipeline. This is the fix for the GW2 cold-start bug.

## 2.3 The classic anchor (`src/fpl_ai/models.py`)

- **Four independent ridge regressions** on the same standardized features: minutes, 1GW, 3GW and 5GW points. The intercept is unpenalized and α = 1.0. With ~190,000 rows this is effectively ordinary least squares.
- At prediction time, inputs are clipped to the range seen in training. Minutes are clipped to [0, 180] and points to ≥ 0.
- **Appearance probability is not a model.** It is `clip(predicted_minutes / (90 × fixture_count), 0, 1)`. A player expected to play 60 minutes gets P = 0.67, even if he appears 90% of the time with some substitute cameos. This matters a great deal for the availability findings in Section 3.10.
- **Uncertainty** = `clip((RMSE_3gw + RMSE_minutes/90) / max(points_3gw, 1), 0.05, 1)`.
- **Walk-forward everywhere:** the SFT corpus, the backtest and the live forecast all fit on rows strictly before the target week, though without an embargo for multi-week labels (§2.12).
- Optional and default-off: per-price-band calibration offsets from a 10-week shadow refit (`FPL_BAND_CALIBRATION`), and weighted least squares (`FPL_DECISION_WEIGHTED`).

## 2.4 The LLM residual forecaster: data (`scripts/build_residual_player_forecast_split_v2.py`)

**Corpus:** `export-llm-player-forecast-corpus` writes one row per player-week (113,360 for 2022-26) with the six-number classic forecast and the labels. Attach scripts then add evidence documents, a fixture outlook, a congestion block, a depth chart and DefCon averages.

**Row selection:** within each gameweek, keep the top N players (N = 256 since E4) by a score built only from the classic forecast, so nothing post-deadline leaks into selection:

```
S = 5gw + 0.75·3gw + 1.5·1gw + 0.02·minutes + 2.0·P(appear)
```

**Residual labels** (the training target):

```
δ = round( clip( 0.35 × (actual − classic), ±bound ), digits )
```

| key | bound | rounding |
|---|---|---|
| delta_points_1gw | ±2.0 | 0.1 |
| delta_points_3gw | ±4.0 | 0.1 |
| delta_points_5gw | ±6.0 | 0.1 |
| delta_minutes_1gw | ±20 | integer |
| delta_appearance_probability | ±0.25 | 0.01 |

The builder's docstring records the rationale for the 0.35 shrink: realized deltas have a standard deviation of ~3.5 points, so clipping alone saturated ~75% of labels and "teaches a degenerate 'always output the bound' policy." On E19's training set, the 1GW label has mean −0.029, **median −0.300** and sd 0.894, with 6.8% at the upper bound and 0.4% at the lower. The distribution is right-skewed: most weeks a player slightly under-performs his expected value, and a few hauls pull the mean up. That asymmetry turns out to explain the adapter's behavior (Section 3.10).

**Train/eval split:** by (season, week) cutoff, with an error if any eval week falls on or before the cutoff. E19 trained on 140 weeks × 256 = 35,840 rows (2022-23 to 2025-26 GW26) and evaluated on 12 × 256 = 3,072 rows (GW27-38). Evidence was present on 84.7% of training rows. Shown documents were mostly Guardian (49,764), then PL Scout (5,045) and Sky (394).

## 2.5 The prompt, verbatim

Every prompt has the same skeleton. The current one (E18/E19, "v1" prompts) contains, in order:

1. a system line ("You are an FPL player forecaster…");
2. the task and the delta bounds;
3. the output schema with an example;
4. player context: season, gameweek, deadline, name, position, status, official news, and the DefCon line when tracked;
5. the classic forecast as JSON;
6. the provenance line;
7. the fixture outlook for the next five gameweeks;
8. a congestion block when European fixtures fall within 5 days;
9. up to two evidence documents.

Each document is a mention-centered window of 260 characters, or 800 for Scout-titled pieces, with up to two merged windows per document. Here is the real first row of E19's evaluation set, unedited:

```
<|turn>system
You are an FPL player forecaster. You combine a classic ML statistical signal with pre-deadline text evidence and output bounded forecast deltas as strict JSON. No hidden reasoning, no extra text.<|turn>
<|turn>user
Forecast this player's post-deadline FPL outcomes. You are the forecaster; the classic ML signal below is one statistical input, and the text evidence tells you what it cannot see (injuries, rotation, form context, tactical changes). Express your forecast as bounded deltas to add to the ML signal.

Delta bounds (values outside are clipped): delta_points_1gw in [-2, 2], delta_points_3gw in [-4, 4], delta_points_5gw in [-6, 6], delta_minutes_1gw in [-20, 20], delta_appearance_probability in [-0.25, 0.25].
Use deltas at or near zero when the evidence gives no clear reason to move.

Return exactly one JSON object, no prose/markdown/extra text, with numeric fields:
- "delta_points_1gw"
- "delta_points_3gw"
- "delta_points_5gw"
- "delta_minutes_1gw"
- "delta_appearance_probability"

Example:
{"delta_points_1gw": -0.5, "delta_points_3gw": 1.2, "delta_points_5gw": 2.0, "delta_minutes_1gw": -8, "delta_appearance_probability": -0.1}

Player context:
- Season: 2025-26
- Gameweek: 27
- Deadline: 2026-02-21T13:30:00+00:00
- Player: Erling Haaland
- Position: FWD
- Status pre-deadline: a
- Official player news pre-deadline: none
- Defensive contribution (rule since 2025-26: +2 pts at 10+ for DEF, 12+ for MID/FWD, per match): L3 avg 1.3/GW, L5 avg 1.0/GW

Classic ML signal (statistical forecast from structured pre-deadline features):
{
  "baseline_points_1gw": 6.9562,
  "baseline_points_3gw": 20.4102,
  "baseline_points_5gw": 33.7288,
  "baseline_minutes_1gw": 88.2847,
  "baseline_appearance_probability": 0.9809,
  "baseline_uncertainty": 0.2242
}

Baseline provenance:
The classic signal already prices in recent form, xG/ICT trends, team/opponent form, this GW's fixture (incl. blanks/doubles), market trends, and a binary injury flag. It cannot see status/news wording, fixtures beyond this GW, cup congestion, or post-break effects — adjust only for those.

Fixture outlook (team schedule, diff 1=easiest to 5=hardest):
GW27: NEW (H, diff 3); GW28: LEE (A, diff 3); GW29: NFO (H, diff 3); GW30: WHU (A, diff 3); GW31: blank

Timestamp-safe text evidence:
[1] Premier League | 2026-02-17T11:20:00Z
Title: Is Semenyo now a better pick than Haaland in FPL?
Text: ... etter Fantasy Premier League pick than his illustrious team-mate Erling Haaland . Antoine Semenyo 's (£8.0m) fine start to life at … ed 33 points from Gameweek 22 onwards. Why is Semenyo outscoring Haaland at Man City? Crucially, Semenyo has started all five of ...

[2] Premier League | 2026-02-20T05:00:00Z
Title: Who is the best FPL captain for Gameweek 27?
Text: The ongoing concerns over Erling Haaland 's (£14.9m) fitness gives a number of form players the chance to outscore the Manchester City forward in Gameweek 27, with Chelsea pair Joao Pedro (£7.7m) and Cole Palmer (£10.6m) and Haaland's new team-mate Antoine ...
<|turn>
<|turn>model
```

- **The training target** for this row was `{"delta_points_1gw":-0.3,"delta_points_3gw":-4.0,"delta_points_5gw":-6.0,"delta_minutes_1gw":1.0,"delta_appearance_probability":0.01}`. Haaland scored 6, then 8 over three weeks and 10 over five, so the 3- and 5-week deltas sit at their bounds.
- **E19 output:** −2.0, −4.0, −6.0, −20, +0.01. It read the fitness concern.
- **Base Gemma output:** −1.0, −1.5, −2.5, −15, −0.15.

The provenance paragraph is the sentence that, in its full v1 form, told the adapter that "this GW's fixture" was already priced (Section 3.7). Note also the custom turn markers: `<|turn>` closes each turn, where Gemma 4's own template uses `<turn|>`, and there is no BOS token. Training and decoding match, so the adapter is unaffected, but the *base-model* comparisons ran on a slightly malformed template.

## 2.6 Training (`train_gemma_sft.py`, E19 settings)

| setting | value |
|---|---|
| base model | `google/gemma-4-E4B-it`, bf16 (no quantization), SDPA attention |
| LoRA | rank 16, alpha 32 (scale 2.0), dropout 0, on attention q/k/v/o and MLP gate/up/down weights via PEFT `target_parameters` |
| LoRA coverage | 258 weight matrices: layers 0–23 have all seven; layers 24–41 have no k/v projections, consistent with cross-layer KV sharing |
| trainable parameters | 34.9 million (adapter file 139.6 MB) |
| loss | completion-only cross-entropy on the JSON tokens and EOS (prompt tokens masked; pinned by `tests/test_sft_masking.py`) |
| optimizer | fused AdamW, β = (0.9, 0.999), weight decay 0, max grad norm 1.0 |
| schedule | learning rate 5e-5, cosine decay, 30 warm-up steps |
| batch | 1 sequence × gradient accumulation 16 = 16 sequences per step |
| length | prompts mean ~960 tokens (max 1,404); completions 56–63 tokens |
| epochs / steps | 1 epoch = 2,240 steps; 36.5 million tokens; ~54 hours |
| checkpoints | every 100 steps, keep 3 |
| fit | loss 1.135 at step 10 → 0.389 at step 30 → 0.147 at the end; token accuracy 0.939 |

The configured maximum sequence length and truncation mode are silently ignored (TRL 1.0 truncates inside its own collator, and the script supplies a custom one). That had no effect on E19, whose longest sequence (1,462 tokens) fits. It also means the 0.8% of E17 rows that exceeded the configured 1,536-token cap were trained in full, not truncated as the E17 notes assumed.

## 2.7 Decoding, scoring and applying deltas

- **Decoding** (`eval_gemma_responses.py`): the prompt is used verbatim; left padding; **greedy decoding** (`do_sample=False`), stopping at EOS; up to 96 new tokens; batch 16; resumable. A single-instance guard (`scripts/decode_live.sh`) stops two decoders appending to the same file.
- **Scoring** (`score_player_forecast_residual_eval.py`):
  - *Strict JSON*: the response starts with `{` and ends with `}`.
  - *Parseable*: the first balanced JSON object parses.
  - *Forecast and MAE*: the final forecast is classic + predicted delta, and MAE/RMSE are taken against actual values.
  - *Ranking*: week-wise Spearman, and the realized points of the top-11 forecasts ("ranking lift").
  - *Unparseable rows* fall back to classic.
- **Application** (`src/fpl_ai/llm_adjust.py`): deltas are parsed, clipped to the bounds, and looked up by (week, player). Four modes:

  | mode | what changes |
  |---|---|
  | `all` | add every delta |
  | `points` | points deltas only |
  | `availability` | minutes and P(appear) only |
  | `availability_scaled` | multiply all points horizons by clip(P_llm / P_classic, 0.6, 1.4) |

  Players without a prediction keep the classic forecast.

**E19's evaluation, for reference** (3,072 rows, GW27-38):

| metric | classic | base Gemma | E19 adapter |
|---|---|---|---|
| 1GW MAE | 2.2716 | 2.2591 | **2.1358** |
| 1GW RMSE | **3.0423** | 3.0605 | 3.0593 |
| 5GW MAE | 7.1098 | 7.0374 | **6.9868** |
| 5GW RMSE | 9.0377 | **9.0250** | 9.2161 |
| minutes MAE | 28.35 | 28.46 | **26.17** |
| P(appear) MAE | 0.3467 | 0.3582 | **0.2734** |
| 1GW Spearman (week-wise) | 0.284 | 0.294 | **0.321** |
| strict JSON | — | 2,199 / 3,072 | **3,072 / 3,072** |

MAE improves while RMSE gets worse. That is the signature of an estimator pulled toward the *median* rather than the mean, the subject of Section 3.10.


## 2.8 The decision layer (`src/fpl_ai/decision.py`)

The decision layer is deterministic and exact given forecasts. It never sees text. Every piece of judgment reaches it as a number.

### Decision weights

`DecisionWeights` holds the scoring knobs, which doubled as the action space for the first RL runs:

| field | default | meaning |
|---|---|---|
| `horizon` | `"3gw"` | the points horizon for transfer evaluation, `H(f)`. `"blend5"` uses `5gw + 0.6·3gw + 0.35·1gw` |
| `availability` | `"threshold"` | `"soft"` multiplies a starter's points by `w(f) = min(1, P / 0.80)` |
| `captain_leverage` | `1.0` | multiplier on the captain bonus in squad evaluation |

Seven presets exist (`baseline`, `horizon5`, `avail_soft`, `horizon5_avail`, `captlev2`, `captlev3`, `avail_soft_captlev3`), selected with `--decision-variant`.

### Choosing the XI, captain and bench (`_optimize_lineup`)

1. Score each squad player as `lineup_score = predicted_points_1gw × w(f)` (w = 1 in threshold mode).
2. Sort within position. For each legal formation, take the top-k per position and sum. The best formation wins (ties go to the earlier one in the list). Because the score is separable, this is exact over the listed formations.
3. **Bench order:** the reserve goalkeeper first, then the three outfield reserves in descending `lineup_score`.
4. **Captain** = the highest `lineup_score` in the XI; **vice-captain** = the second highest. There is no minimum-availability rule for the captain.

### Valuing a squad (`_evaluate_squad`): the number every transfer is compared on

```
V(S) = Σ_{i ∈ XI} H(f_i) · w(f_i)                         # starters, on the 3GW horizon by default
     + captain_leverage · f_captain.1gw · w(f_captain)     # the captain's doubling, counted once
     + 0.05·bench_GK.1gw + 0.12·bench_1.1gw + 0.06·bench_2.1gw + 0.04·bench_3.1gw
     − Σ_{i ∈ XI} max(0, 0.6 − P_i) · s                    # threshold mode only; s = 2 (or 4 for blend5)
```

The XI is *chosen* on 1-week points but *valued* on 3-week points. The availability penalty only bites below P = 0.6. That is why the LLM's availability deltas were "decision-inert" under the default optimizer (Section 3.3): a change from P = 0.9 to P = 0.7 alters nothing.

### Recommending transfers (`recommend_actions`)

- **Out-pool:** the 6 squad players with the lowest `H`. **In-pool:** the 24 best non-squad players by `H`, any position or price.
- Enumerate every 1- and 2-transfer combination (144 + 4,140 candidates). Keep those that are affordable (`bank + Σ selling prices ≥ Σ buy prices`) and legal (exactly 2/5/5/3, at most 3 per club). Charge `hit = 4 × max(0, k − free_transfers)`.
- `projected_gain = V(new) − V(current) − hit`. Keep positive gains and rank them.
- The restricted out-pool is why the optimizer can never propose selling a top player (such as Bruno) to fund a premium (such as Haaland). Those routes have to be searched separately, as was done for the Haaland question.

### Chip advice

Chip advisories are heuristic scores with thresholds: Bench Boost when the bench is strong and nobody blanks; Triple Captain only when the captain has a double gameweek; Free Hit when 4+ starters are blank or doubtful; Wildcard when 5+ squad players look weak. In the backtest, Bench Boost and Triple Captain timing comes instead from a small dynamic program over the remaining weeks (below).

### The draft (`build_initial_squad`)

A **beam search** builds a 15-man squad from scratch:

```
selection score S(f) = 5gw + 0.6·3gw + 0.35·1gw − 4·max(0, 0.65 − P)
slots: GK, GK, DEF×5, MID×5, FWD×3
beam width 300 (retries at 800, 1,600, 3,000, then a cheapest-legal fallback)
pruning: half the beam by score, half by cost; de-duplicated on player set
feasibility: current cost + cheapest possible remaining slots ≤ budget
goalkeeper pair: max(S_a, S_b) + bench_gk_weight · min(S_a, S_b)   (1.0 in backtests, 0.15 live)
optional captain leverage (default off): re-rank the final beam by score + λ · max_i S(f_i)
```

The selection score is **dominated by the 5-week horizon**. That is why the 5GW head's attenuation kept elite defenders out of the draft (Section 3.6), and why adapters that rank well on 1GW but not on 5GW didn't convert at the gate (E6).

## 2.9 The evaluation harness (`run_rolling_squad_backtest`)

Every "decision value" number in this document comes from this function. Its structure explains a great deal about why the results behave as they do.

**For each simulated week W:**

1. **Refit** the four ridge heads on every eligible training row strictly before week W (`season·100 + week < test·100 + W`), then forecast week W. If LLM predictions are supplied, apply the deltas in the chosen field mode.
2. **First week of the window only:** draft a fresh squad with the beam search. No transfer that week.
3. **Later weeks:** optionally simulate Wildcard / Free Hit (off by default). Otherwise call `recommend_actions` with one transfer allowed, and take the best transfer if its projected gain ≥ 0. Optionally run the two-week lookahead.
4. **Lineup** from `_optimize_lineup`. **Bench Boost / Triple Captain** scheduled by a memoized dynamic program over (week, BB available, TC available), using projected future values.
5. **Score with realized points:** the XI's actual points, the effective captain's points again (vice if the captain didn't play), automatic substitutions, minus hits. Bench Boost counts all 15.
6. **Free transfers** roll as `min(2, max(1, ft − used + 1))`. Selling prices reset to the current price (the 50%-of-profit rule is not modeled).

**Three structural facts about this harness matter for interpretation:**

- **A 4-week window is mostly a draft test.** Each window starts from a squad drafted from that window's first-week forecasts, then makes at most one transfer per week. So 15 players are chosen at once by the 5GW-dominated selection score, and at most 3 change afterwards. Adapter comparisons therefore mostly measure *which 15 players each forecast set drafts*. A change that reorders the top of the 5GW distribution changes many players at once, which is why adapter comparisons are noisier (24–40 points per window) than small anchor tweaks (~15).
- **Totals are comparable only within a run family.** Window, anchor, training table and flags all shift absolute totals. The same "classic on GW35-38" reads 247, 267, 268 or 270 depending on table version and anchor. Always compare an arm against its own control in the same family.
- **The scoring is close to, but not exactly, real FPL.** Selling prices are approximate, chips are once per window, banking is capped at 2, and (see §2.12) automatic substitution is all-or-nothing.

### The noise floor and the mechanism check

- **Noise floor:** the standard deviation of decision-value differences between configurations judged equivalent. About **14.9 points per 4-week window for small anchor changes** (from 12 null windows), and **24.3 (raw adapter) to 39.6 (V3)** for adapter comparisons (from 21 windows). To detect an edge of X points per window at 95%, you need n > (1.96·σ/X)² windows.
- **Mechanism check** (`scripts/check_delta_mechanism.py`): for each designed signal (opponent defensive weakness, injured team-mates, …), compute the partial correlation of the adapter's 1GW delta with that signal *controlling for the classic baseline*. This control matters because the raw correlation is contaminated by the baseline-proportional shrink. The check distinguishes "signal absent from the prompt" from "signal present and ignored". Count patterns are scoped to their own prompt block, so injury words in news text aren't mistaken for the depth-chart block.

## 2.10 The reinforcement-learning environments

All RL runs use TRL 1.0's `GRPOTrainer` on Gemma-4-E4B in bf16. Each uses a fresh LoRA (rank 16, alpha 32, attention projections via `target_parameters`), raw prompt strings, a −1.0 reward for unparseable output, and a default action that is reward-neutral by construction. State caches (`scripts/build_grpo_state_cache.py`) store, per week, the classic trajectory's squad, bank and free transfers, a refit forecast pool, and realized outcomes for every player. "Adjusted" caches additionally bake in chrono-legal adapter deltas and ≤180-character scout snippets.

| | G1 | G2 / G2-v3 / G3 | G4 |
|---|---|---|---|
| Task | One week's decision knobs | A 6-week plan in one completion | The residual forecast itself |
| Prompt | Squad + top-24 outsiders (1GW, 3GW, P), bank, FT | Squad + top-20 outsiders, per-half chips left, first-week top-3 transfer proposals, ≤10 scout notes, week-by-week outlook | The E11 SFT prompt for one player-week |
| Action | `{horizon, availability, soft_knee, transfer_aggressiveness, captain_pick}` | Per week: G1 knobs + `bank_transfer`, `chip_play`, and (G3) `transfer_pick` ∈ {0, 1, 2} | Delta JSON (same bounds as SFT) |
| Rollout | One transfer if gain ≥ 2 − aggressiveness; lineup; captain override | Chained weeks; squad, bank and FT evolve; chips legal once per half | Apply this player's delta only; transfer + lineup with default weights |
| Reward | realized(action) − realized(default) on the same state | Σ realized(plan) − Σ realized(all-default plan) | realized(with delta) − realized(without) |
| G, β, LR, temp | 8, 0.04, 1e-5, 0.8 | 8, 0.04, 1e-5, 0.8; 8 epochs | 4, 0.04, 1e-5 → 2e-5, 0.8 |
| Data | 117 classic states | 59 adjusted episodes (G3: 236 with augmentation) | 102 states (v2: 2,655 boundary-sensitive player rows) |
| Scoring simplifications | No autosubs, bench or chips | No autosubs | No autosubs, bench or chips |

The **chip rule** in the plan environment is one copy each of Bench Boost and Triple Captain per half (GW ≤ 19 and GW ≥ 20). An illegal request is downgraded to "none". The **augmentation** in G3 perturbs each episode's starting squad with 1–3 same-position swaps within ±£0.5 plus bank jitter.

## 2.11 The weekly live runbook

1. **Settled gate** (`scripts/gw_status.py --require-settled`): proceed only when FPL marks the gameweek `finished` and `data_checked` (bonus confirmed).
2. **Ingest** (`scripts/run_weekly_ingest.sh <gw>`): sync the season through the completed week; restore pre-deadline status/news from the archived corpora; stop if the flagged-status rate is still 0.000.
3. **Rebuild** the training table with the current cutoff and flags (`FPL_PRIOR_BLEND=1`, and `FPL_OPPONENT_INTERACTION=1` once F6 is live).
4. **Corpus** (`build_live_gw_examples.py --stage corpus`): fit the ridge suite, build the live frame (walk-forward synthetic rows), forecast every player, attach status/news, market and DefCon.
5. **Evidence:** pull fresh pre-deadline articles (Guardian, PL Scout), attach per player with the same flags the deployed adapter trained on (parity), and render prompts (`--stage prompts`).
6. **Eyeball gate:** compare the median / 90th-percentile 1GW and P(appear) with last week; spot-check three premiums; run the premium-rank alarm.
7. **Decode** (`scripts/decode_live.sh`, single-instance guard) with the deployed adapter.
8. **Sheet** (`scripts/recommend_gw2_actions.py`): apply deltas, compute selling prices with the 50% rule, enumerate 1–2 transfer options, and print the XI, captain, vice, and "BENCH (enter EXACTLY this order)".
9. **After the deadline:** the case-study round (largest misses, investigated by hand), then settle the gameweek and write the ledger entry, including every judgment call and its outcome.

## 2.12 Defects found while writing this document

Reading the code line by line for this Part turned up defects that no earlier session had recorded. The serious ones were verified with CPU checks on 3 October (Section 3.10). They are ordered by expected impact.

**Data foundation: high impact.**

| # | defect | evidence | effect |
|---|---|---|---|
| A | **Historical "pre-deadline" status and news are end-of-season snapshots**, copied from `players_raw.csv` onto every week | 0 players with more than one status in any season 2019-20 to 2025-26; Martínez "suspended" all of 2024-25 (3,195 min); Saliba "injured" all season (3,039 min) | Leaky, noisy anchor injury features; status/news lines in 13.8% of E19 training prompts; F7; possibly part of the late-season availability "edge" |
| B | **A player's club is his end-of-season club**, so mid-season movers pollute team-form tables | 24–36% of team-weeks contaminated in 2022-26; Man City's first 8 weekly goals in 2025-26 recorded as 6,2,5,5,3,9,5,8 vs real 4,0,1,3,1,5,1,2 | Noise in every team and opponent feature, including F6's inputs, plus the fixture-outlook, congestion and depth-chart prompt blocks |
| C | **Ownership: a manager count in training, a percentage live** | Table median ~20,000, max 9.5 million; live 0–100. Simulated: Haaland 5GW 35.3 → 28.9, João Pedro 27.3 → 21.1 | Live forecasts under-rate popular players (every sheet this season); backtests unaffected. E13a's market line read "owned by 6171553.0%" |
| D | **The F2b blend never reaches the live walk-forward features** (built from the live season alone) | Live output identical with the flag on or off | Train/live mismatch for players with under six appearances (GW3–5) |

**Evaluation harness: medium impact.**

| # | defect | effect |
|---|---|---|
| E | **No embargo on multi-week labels.** The anchor fitted for week W trains on rows from W−4…W−1 whose 3GW/5GW labels include points from week W onward. E19's training rows from GW23-26 similarly overlap its first eval window. | Slightly optimistic multi-week forecasts in backtests (both arms; ~1–2% of rows). 1GW unaffected |
| F | **Automatic substitution is all-or-nothing:** if not every non-playing outfield starter can be replaced, none is | ~3% of non-Bench-Boost backtest weeks lose a playing substitute |
| G | **The chip dynamic program inflates future weeks** (single-fixture multiplier ~1.21 rather than 1.0) | Bench Boost / Triple Captain timing biased toward later weeks |
| H | **The first state of every RL cache has a £100 pre-draft bank** alongside a full squad | Spurious cash in a handful of training states and the first eval window of G1, G2/G3 and G4 (e.g. the baseline "buys" Haaland at GW12) |

**Smaller issues.**

| # | defect | effect |
|---|---|---|
| I | **Surname-only evidence matching collides** ("Michael Keane" collected a Robbie Keane passage; "Matheus Nunes" a Swansea team sheet) | Wrong-person evidence in some prompts |
| J | **Evidence timestamps are first-publication times**, but article bodies were fetched later (live blogs first published under 6 hours before a deadline appear 6 times) | A leak *risk*; none confirmed in the cases inspected |
| K | **Non-standard chat template:** each turn is closed with the opening marker (token 105) instead of Gemma 4's closing marker (token 106), and no BOS token is added (see the prompt in §2.5) | Consistent across training and decoding, so the adapter is fine; base-model comparisons ran on a malformed template |
| L | **Configured maximum length and truncation mode are ignored** (TRL 1.0 truncates in its own collator; the script supplies a custom one) | No effect on E19 (longest sequence 1,462 tokens) |
| M | **Blank-week rows zero the era flags**, so the DefCon line disappears in blank weeks | All 126 E19 eval rows without a DefCon line |
| N | **Two prompt lines are mislabelled:** the depth chart's "min/game last 3" shows predicted minutes; the role line's "starts" shows appearance rate | Prompt semantics (neither block is in E18/E19) |
| O | **`team_id = −1` in the 2022-25 RL caches**, so the 3-per-club rule never binds in RL training on those seasons | Minor (RL track closed) |
| P | **Plan completions truncated at the cap in ~60% of samples**, including G3b, whose larger cap was meant to fix it | G3b says nothing about whether truncation mattered |
| Q | **G4 trained on adjusted forecast pools**, contrary to its docstring and design doc, and differed from the design on autosubs, held-out window and gate | Its training regime was not the designed one; the failure diagnosis stands |
| R | **The formation list omits 5-2-3** (legal) and includes 3-3-4 (unreachable) | Rarely suboptimal XIs |
| S | **Live scripts don't clip parsed deltas** (the backtest path does); the backtest's `apply_llm_deltas` doesn't floor points at zero | Live/backtest inconsistency |

None of these is known to overturn a comparative verdict in Part III, because compared arms shared the same data and harness. But A, B and E affect the absolute level of every number. A also clouds the interpretation of the adapter's late-season availability edge. And A–D are the most promising fixes available (Part VIII).


---

# Part III — The story, chronologically

Each experiment below is written up as a card with the same five parts: **the intuition** (why we thought it would work), **the change** (exactly what differed from the baseline), **the result** (numbers), **the verdict**, and **the lesson**. Experiments are grouped into eras; each era opens with what we believed at the time, because several of those beliefs turned out to be wrong in instructive ways.

## 3.1 Era 0 (April – May 2026): asking a big model to do everything

**What we believed:** a large instruction-tuned model, fine-tuned on FPL history, could learn to make FPL decisions directly. That meant choosing a squad, choosing transfers, or forecasting player points from a description of the situation.

The code base already existed in a first form: an ingestion layer for the vaastav archive, a player-week feature table, ridge-regression baselines for points and minutes, a legal decision engine, a rolling backtest, and an evidence layer with timestamps. The README of the time describes it as "an opinionated first implementation", and its "not implemented yet" list included "end-to-end LLM fine-tuning / inference runs" and "offline RL / policy learning." The spring was about filling that gap with **Gemma-4-31B-it** and LoRA.

### Card: direct squad and transfer SFT (31B, April)

- **Intuition:** show the model the state (budget, squad, candidates) and the action a good manager would take, and let it learn the policy.
- **Change:** three squad-selection runs (`squad_v1`, `squad_v2_textonly`, `squad_v3_format_json`) and one `transfer_choice_v1` run, each only 11–12 optimizer steps. These were pilots, not production runs.
- **Result:** fine-tuning improved machine-parseable output relative to base Gemma, and prompt examples helped strict JSON. The decisions themselves were not good. The model produced invalid or suboptimal actions easily, because the action space is constrained by squad rules, budget, hits and chips all at once.
- **Verdict:** direct action choice is "too sparse and noisy" as a learning target.
- **Lesson — decompose.** Forecasting player points, understanding availability, obeying FPL legality, managing budget and hits, captaincy and chips, and producing valid JSON are six different problems. Asking one model to learn all six from realized outcomes means it learns none of them. **The LLM should feed an optimizer, not replace it.** This principle held for the rest of the project.

### Card: direct per-player forecast SFT (31B, April)

- **Intuition:** if actions are too hard, forecast points per player and let the optimizer decide.
- **Change:** a ladder of pilots that asked the model for absolute forecasts (1/3/5-gameweek points, minutes, appearance probability) for the top 2, top 8, then top 96 players per week (`player_forecast_pilot_top2/top8/top96`; the top-96 run was 1,140 steps on 1,920 examples).
- **Result (top-96 eval, 1,920 rows):**

| | strict JSON | 1GW MAE | 1GW RMSE | 3GW MAE | 5GW MAE | P(appear) MAE |
|---|---|---|---|---|---|---|
| Base Gemma-31B | 0 / 1,920 | 2.666 | 3.440 | 5.809 | 8.797 | 0.183 |
| SFT Gemma-31B | **1,920 / 1,920** | **2.373** | 3.900 | 6.414 | 10.208 | **0.133** |

- **Verdict:** format solved, prediction not.
- **Lesson — fine-tuning on a skewed target learns to shrink.** The 1-gameweek MAE improved while RMSE got *worse*, and the longer horizons got worse. That is the signature of a model that has learned to predict low numbers. On a target that is usually 1–3 points with rare hauls, predicting low improves median-type error and destroys the tails, which is exactly where FPL decisions live. Here, in April, was the first appearance of the theme that defines the whole project: **error metrics reward shrinkage; decisions punish it.**

## 3.2 Era 1 (May – early July 2026): residuals, ranking, and the end of 31B

**What we believed:** absolute forecasts are too hard because the model must re-learn everything the classic model already knows. Anchor the LLM to the classic forecast and ask it for **corrections**.

### Card: residual forecast pilots (31B, May – June)

- **Intuition:** the classic model handles the numeric prior; the LLM only has to learn when and how much to move it. The output is a delta, not a forecast.
- **Change:** `player_forecast_residual_gw1_10_top128` (train on 2025-26 GW1-10, evaluate GW11, 128 players) and later `gw1_25_top128` (train GW1-25, evaluate GW26). An artifact tagged `..._dirty_leakage_20260603` sits beside the first pilot: that run was set aside on 3 June after a leakage problem was found.
- **Result:**

| GW1-10 → GW11 | 1GW RMSE | 3GW RMSE | 5GW RMSE | parseable |
|---|---|---|---|---|
| Classic ML | **3.351** | 6.902 | 9.854 | — |
| Base Gemma residual | 3.383 | 6.819 | 9.226 | 117 / 128 |
| SFT Gemma residual | 3.416 | **6.534** | **8.546** | 107 / 128 |

| GW1-25 → GW26 | 1GW RMSE | 3GW RMSE | 5GW RMSE | strict JSON |
|---|---|---|---|---|
| Classic ML | **3.307** | **6.252** | **8.578** | — |
| SFT Gemma residual | 3.708 | 7.693 | 11.596 | 128 / 128 |

- **Verdict:** the first pilot was the first genuinely promising result in the project; the second blew up. The GW26 model over-adjusted badly, worse at every horizon.
- **Lesson — residuals need bounds.** An unbounded residual can do more damage than an absolute forecast, because it starts from a good number and walks away from it. The 5 July plan made **clipping** non-negotiable, in both the training labels and at inference parse time, with starting bounds of ±2 points (1GW), ±4 (3GW) and ±6 (5GW).

### Card: free listwise reranking (31B, June)

- **Intuition:** decisions are about order, so train the model on order directly. Given a slate of 12 candidates, rank the top 5 by realized utility, with utility defined as `0.20 × points_1gw + 0.30 × points_3gw + 0.50 × points_5gw`.
- **Result (GW26 eval, 128 slates):**

| | value / example | NDCG@5 | top-1 accuracy | strict JSON |
|---|---|---|---|---|
| Classic ML | **79.90** | **0.794** | **0.305** | 128 / 128 |
| SFT checkpoint 160 | 70.93 | 0.704 | 0.188 | 128 / 128 |
| SFT checkpoint 320 (best) | 73.36 | 0.729 | 0.180 | 128 / 128 |
| SFT checkpoint 600 | 73.03 | 0.720 | 0.172 | 128 / 128 |

- **Verdict:** format perfect, decisions materially worse than the baseline at every checkpoint.
- **Lesson — free overrides learn noise.** With noisy realized outcomes and small samples, a model allowed to reorder everything learns unstable patterns. Anchoring limits the damage.

### Card: anchored reranking (31B, June – July 3)

- **Intuition:** start from the classic top 5 and allow at most 2 swaps, trained on swaps that improved realized utility. On the eval slates, two perfect swaps would capture almost all of the oracle's upside (93.48 vs the oracle's 94.18, from classic's 76.69). The headroom was real.
- **Change:** 16,000 training slates from 2025-26 GW1-25, 128 eval slates at GW26, candidate pool = classic top 128. Training was deliberately stopped and evaluated at checkpoint 160 because each step took ~16 minutes.
- **Result:** classic 76.69, base Gemma 77.05, **SFT 72.92**. Top-1 accuracy fell from 0.305 to 0.125. Strict JSON was 128/128.
- **Verdict:** closed. The model learned the format perfectly and degraded the decisions.
- **Lesson — and the pivot.** Three things were now clear. First, **size had bought nothing**: the 31B model lost to a ridge regression at every task. Second, **iteration speed was the binding constraint**: at 16 minutes per step, one epoch was nine days, so we could not afford enough experiments to find an objective that worked. Third, across four task framings, **every experiment that let the LLM freely override the baseline on noisy outcomes failed.** Long-context full-text variants (2k, 4k and 8k-token evidence prompts, `player_forecast_v4_*`) were also attempted in this period; none reached a checkpoint.

**The 5 July plan** turned these lessons into an architecture and a schedule, and you approved it with the "load-bearing" clarification:

- Switch to **Gemma-4-E4B-it** (effective 4B, ~8B raw parameters, no gating) for all iteration. The task is "calibration + extraction, not open-ended reasoning", and a training step should go from ~16 minutes to under a minute (in practice 41–110 seconds).
- Use **per-player residual forecasting** with **clipped deltas**, one example per player × gameweek × pre-deadline snapshot.
- Expand training to **multiple seasons** (2022-23 onward), evaluated chronologically on 2025-26 GW12-30.
- Define the ship gate: the LLM-adjusted pipeline must beat classic-only on **realized squad points** over the rolling GW12-30 backtest. Otherwise classic ships with the LLM in shadow.


## 3.3 Era 2 (5 – 13 July 2026): the E4B ladder, the gate, and the oracle

**What we believed:** with a fast small model, clipped residuals and multi-season data, the LLM would learn to read news and improve forecasts. The open question was which inputs mattered.

**The common setup for E0–E3a:** train on 2022-23 through 2025-26 GW11, using the top 128 players per week by classic forecast (16,000 rows). Evaluate on 2025-26 GW12-30, top 128 per week (2,432 player-weeks). Labels are the realized residual (actual minus classic) multiplied by a **shrink factor of 0.35**, then clipped to the bounds. E4B bf16 LoRA, batch 2 × grad-accum 8, seq 1024, one epoch (1,000 steps, 10–14 hours).

A note on the 0.35 shrink, because it matters for interpreting everything later. Training directly on realized residuals asks the model to predict noise: a player forecast at 4 who scores 13 has a residual of +9, and almost all of that is luck. Multiplying by 0.35 says "learn the *direction* and a damped magnitude." It is a variance-reduction choice, and it also builds in a bias toward small corrections.

### Card: E0 — the base model as a control

- **Change:** un-tuned Gemma-4-E4B with the same prompts.
- **Result:** deltas effectively zero; scores identical to classic; **32% of outputs not strict JSON**.
- **Lesson:** every effect measured from here on is owned by fine-tuning, not by the base model's world knowledge.

### Card: E1 — structured features only (no text)

- **Intuition:** isolate what the model can do with the numbers alone, before giving it articles.
- **Result (top-128, GW12-30):** 1GW MAE 2.435 vs classic 2.575; 5GW RMSE 8.920 vs 9.186 (−2.9%); appearance-probability MAE 0.180 vs 0.205 (−12%); 100% strict JSON. But week-wise Spearman rank correlation was 0.150 vs classic's 0.165, and top-11 realized points were −0.21 per week.
- **Verdict:** passes parity-or-better on error, fails the "positive top-k lift" clause.
- **Lesson — learned shrinkage.** The model had learned that the anchor over-forecasts the top-128 pool and shrinks it. A near-uniform shrink cannot reorder players, so ranking stayed flat. This one card contains the whole project's central tension in miniature.

### Card: E2 — per-player evidence packets (2 docs × 260 chars)

- **Intuition:** the text is the LLM's comparative advantage, so give it the news.
- **Change:** identical rows and labels; prompts gain up to two Guardian / PL / Sky documents per player, 260 characters each.
- **Result:** marginally better than E1 almost everywhere (appearance MAE 0.172, 5GW RMSE 8.887). Top-11 1GW lift became positive at **+1.53 points/week**, but not significant (sd 8.66, paired t = 0.77, 10W/6L/3T). Evidence-usage diagnostic: mean |Δ1gw| was 0.586 on rows with evidence vs 0.566 without, i.e. the model was barely conditioning on the text.

### Card: E3a — richer packets (2 docs × 450 chars)

- **Intuition:** maybe 260 characters was too thin (a headline and a sentence).
- **Result:** E3a ≈ E2 ≈ E1 across the board (appearance MAE 0.169, 1GW MAE 2.429, top-11 lift +1.53, t = 0.69). The usage diagnostic was still flat (0.589 vs 0.568).
- **Verdict:** article text is **NULL** for the forecast. "Packet too thin" was rejected.
- **Lesson — E1 was never text-free.** The structured snapshot already carried the official FPL `status` and `news` fields ("Knee injury — 75% chance of playing"), and that is the highest-signal availability text there is. News articles added little on top for bounded delta prediction. Articles were dropped from forecast prompts but kept for the report's citations, and revisited in E7 with a different genre.

### The first gate (8 July): E3a fails

The ship gate is a rolling squad backtest over 2025-26 GW12-30. It builds a synthetic initial squad at GW12, makes 1 transfer per week, and optimizes chips. (Part II §2.9 explains why this is mostly a *draft* test.)

| pipeline | predicted total | actual total |
|---|---|---|
| classic only | 1,154.9 | **1,058** |
| E3a-adjusted, all fields | 928.1 | 1,000 |

The LLM was *better calibrated*: it predicted 928 and the squad got 1,000, whereas classic predicted 1,155 and got 1,058. But it chose a worse squad. Squad selection is an ordering problem, and the selection score leans on the 5-gameweek forecast, which was E3a's weakest ranking horizon.

The application-mode sweep revealed something more specific:

| mode (E3a deltas) | actual | vs classic |
|---|---|---|
| all fields | 1,000 | −58 |
| availability only (minutes + P(appear)) | 1,058 | **±0 — decision-inert** |
| availability_scaled (points × P_llm / P_classic, clamped [0.6, 1.4]) | 1,001 | −57 |

"Availability only" changed nothing because the optimizer's availability penalty only fires below P = 0.6, and minutes were unused. **The channel the LLM was best at was wired into the optimizer in a way that ignored it.** We would rediscover exactly this on 29 September (Section 3.9).

### Card: decision-layer knob sweep (9 July, CPU)

- **Change:** the `DecisionWeights` presets were added to `decision.py`. `baseline` reproduces 1,058 exactly. Each variant was run on three windows (GW12-30 of 2025-26, 2024-25, 2023-24).

| variant | 2025-26 | 2024-25 | 2023-24 |
|---|---|---|---|
| baseline | **1,058** | 1,261 | 1,056 |
| avail_soft (starter/captain points × min(1, P/0.80)) | 1,031 | **1,270** | **1,067** |
| horizon5 (5GW-blend transfer objective) | 996 | 1,241 | — |
| horizon5_avail | 1,042 | — | — |
| 2 transfers/week, gain ≥ 1.0 | 995 | — | — |

- **Result:** horizon5 and 2-transfers lost on every window, so both were rejected. avail_soft was a wash: −27, +9, +11, mean −2. The single gate window had overstated its cost.
- **The key interaction:** E3a's availability deltas combined with the avail_soft optimizer scored **1,056**, against 1,031 for avail_soft with classic P(appear). That is +25. The LLM's availability calibration *is* decision-relevant once the optimizer consumes P(appear) continuously. It still only tied the tuned classic baseline.
- **Lesson — the multi-window rule.** Single-window season totals carry about ±35–40 points of noise for decision changes. From 9 July, **every decision-layer change needs at least three windows.**

### Card: two-week transfer lookahead (9 July)

- **Intuition:** bank a free transfer when next week offers a better move.
- **Change:** `--transfer-lookahead 2` compares hold-and-bank against the top transfer options. Each action is valued as immediate squad value + 0.9 × the best next-week transfer gain.

| projection | 2025-26 | 2024-25 | 2023-24 | banked weeks |
|---|---|---|---|---|
| greedy baseline | 1,058 | 1,261 | 1,056 | — |
| schedule-rescaled 1GW | 1,002 | 1,255 | 1,055 | 7–9 |
| horizon_diff ((3GW−1GW)/2) | 1,058 | 1,210 | 1,056 | 0–2 |

- **Verdict:** rejected on three windows with both projections. A crude projection banks often and loses; the model's own next-week view almost never banks and collapses to greedy.

### Card: the oracle test (10 July, your design) — planning depth is worth exactly zero

- **Intuition (yours):** separate the value of *planning structure* from the value of *forecast quality* by giving the planner perfect information.
- **Change:** two diagnostic modes with deliberate label leakage: (1) **hybrid**, where classic forecasts make today's decision but the next week is valued with realized outcomes; (2) **full oracle**, where every decision is made on realized outcomes, so the only difference between greedy and lookahead is the banking structure.
- **Result:** the hybrid was actively harmful (−53, −101, +41; mean −38). The full oracle was **identical for greedy and lookahead on all three windows (1,796 / 2,024 / 1,731), with zero banked weeks.**
- **Verdict:** closed permanently. **Even with perfect information, banking a free transfer is never worth it at one transfer per week.**
- **Lesson — where the prize is.** Oracle greedy (1,796) minus classic greedy (1,058) on 2025-26 is **+738 points per season of pure forecast-quality headroom, none of it planning.** Every point the project could still win lived in ranking skill, captaincy and chip judgment. The hybrid result added a second principle: **never bank on information your future executor won't have.**

### Card: E4 — twice the data, top-256 pool, fixture outlook

- **Intuition:** maybe the model needed more rows, and it needed to see the schedule (prompts so far contained zero fixture information).
- **Change:** top-256 players per week (32,000 rows), a fixture-outlook block (next 5 gameweeks: opponent, venue, difficulty, blanks and doubles), no articles. 2,000 steps, 23.1 hours.
- **Result (top-128 subset):** best-ever appearance MAE 0.161, 1GW MAE 2.423, the first non-negative Spearman (0.166 vs 0.165). Top-11 1GW lift +0.32, and 5GW lift −5.8. Gate: all fields 1,020 (−38), availability + avail_soft 1,056 (−2).
- **Verdict:** ranking still flat; gate fails; classic ships GW1 unless something beats 1,058.

### Card: E5 — the congestion block

- **Intuition:** rotation risk after European games should sharpen the availability head.
- **Change:** E4 plus Champions League / Europa League / Conference League proximity and post-international-break flags. Labels byte-identical to E4.
- **Result:** ≈ E4 on every metric (appearance MAE 0.162, Spearman 0.158). Usage diagnostic flat (mean |Δappear| 0.105 with the block vs 0.100 without).
- **Verdict:** **NULL**. Whatever rotation signal survives label noise is already in status/news and form, and only ~24% of rows had a congestion signal at all. (Two months later, F9 would test the same idea in the classic model and falsify its premise outright: premiums start 80.5% of the time without a European game and 79.0% with one.)

### Card: E6 — teach the model what the base is made of

- **Intuition (your "base-anatomy" hypothesis):** if the model knows *what the classic forecast is made of*, it can spend its effort on what the base can't see.
- **Change:** the E5 data plus four prompt blocks: a **provenance** line ("adjust only for what the classic signal cannot see"), the **exact ridge decomposition** of the 1GW baseline into grouped contributions (zero drift vs stored baselines), a **role-context** line (starts in the last 3 vs last 8 games, read as nailed / recently promoted / losing spot / rotation / fringe), and compact context. Max 926 tokens; batch 1 × 16; 30.6 hours.
- **Result:** best ladder run on error. Full eval set: 1GW MAE 2.151 vs 2.271; the first run to beat classic on minutes (22.85 vs 24.33); appearance MAE 0.250 vs 0.308. **Top-11 realized: 52.42/week vs 49.47, +2.95/week, paired t = 2.41 (p ≈ 0.03), 13W/4L/2T.** That was the first statistically significant selection-relevant win. Gate: all fields 1,035; availability + avail_soft **1,058, an exact tie.**
- **Verdict:** best so far, but it doesn't beat the gate. The edge lived in 1GW picks while the optimizer's selection score leans on 5GW, where E6 tied classic.
- **Lesson in hindsight:** E7 failed to replicate E6's significant top-11 lift (+0.79, t = 0.37). That metric was fragile across adapters, and a single "p ≈ 0.03" on 19 weeks was not the solid ground it looked like. More importantly, the provenance line written here (the classic signal already prices "team/opponent form, this GW's fixture … adjust only for" news, congestion and future fixtures) would be found in September to have **switched off the adapter's fixture channel** (Section 3.7).

Two process decisions from this era held for good. You audited **SFT loss masking**: completion-only loss was verified end-to-end and pinned by `tests/test_sft_masking.py`, so every E-run trained on the deltas only. And the approved sequencing of 8 July locked in several decisions: **LoRA stays** (train loss ~0.16 means capacity isn't the bottleneck; label noise is); **reinforcement learning belongs at the decision layer**, because forecast rewards are noise-dominated; and the **optimizer owns all hard constraints**, with the LLM parameterizing it through structured outputs and never free-form overrides.


## 3.4 Era 3 (13 July – 2 August 2026): the first gate win, reinforcement learning, and the clean split

**What we believed:** the forecast adapter was close; the right evidence genre might tip it over. Separately, reinforcement learning at the decision layer could learn judgment (captaincy, chip timing, banking) that a deterministic optimizer can't.

### Card: G1 — a weekly-bandit GRPO policy over decision knobs

- **Intuition:** let the LLM parameterize the optimizer each week. It chooses bounded settings (DecisionWeights knobs, a captain pick, transfer aggressiveness) and is rewarded by what actually happens.
- **Change:** state = the classic trajectory's squad at week *W*; action = bounded JSON; **reward = realized points minus the classic baseline's realized points** (paired, which cancels most weekly noise). GRPO with group size G = 8, KL penalty β = 0.04. The next state always resets to the classic trajectory, so there are no cascades. 117 training states (2022-23 GW6-38, 2023-24 and 2024-25 GW2-38, 2025-26 GW2-11); 19 held-out states (2025-26 GW12-30). 464 steps.
- **What went wrong first:** a 96-token completion cap truncated 81% of rollouts mid-JSON (−1.0 penalty), and the policy collapsed to emitting `{}`, a 2-token "use defaults" answer that scored a safe 0.0. This is **the tie trap**: when ~70% of single-knob actions tie the baseline anyway, the cheapest way to avoid negative reward is to do nothing. The run was relaunched with a 192-token cap and a "single line, no markdown fences" instruction. A **dual-trainer incident** followed: the kill command hit the background subshell instead of Python, so two trainers ran for 12 hours against the same checkpoint directory and log.
- **Result:** training rewards stayed flat (~−0.4 mean, no trend) over 464 steps (36 hours). Held-out: **+7 total (989 vs 982), 7W / 5L / 7T**, one unparseable. The policy mostly learned to switch on soft availability handling and occasionally pick a captain. (Its largest single loss, −14 at GW12, came on a state carrying a spurious £100 pre-draft bank; see Part II §2.12.)
- **Verdict:** marginal. You decided (15 July, delegated call) that G2 should come after E7 regardless, because RL's main upside is multi-step planning, which the bandit construct deliberately caps, and 117 states is thin.

### Card: E7-scout — the first gate win

- **Intuition:** E2/E3a's null came from the wrong *genre* of text, not text itself. General news reports a match; **Scout articles reason about FPL** (captaincy, differentials, price rises, team news). And the official PL Scout API reaches back to 2021 in every season, with a Scout Selection each week.
- **Change:** corpus v7 attaches PL Scout (2,808 articles) and Sky tips per player; `--prefer-scout` ranks those first; 2 docs × 260 chars. Train-row evidence coverage rose to **84%** (vs 24% for the old null packets). Seq 1536 with gradient checkpointing, 48 hours.
- **Result:** forecast metrics ≈ E6, with a best-ever 5GW MAE of 6.613 (classic 6.856). Spearman tied classic exactly (0.2703 vs 0.2705). E6's significant top-11 lift did *not* replicate (+0.79, t = 0.37). The gate:

| config | actual | |
|---|---|---|
| **all fields, baseline optimizer** | **1,069** | **+11 vs classic — first win** |
| availability_scaled | 1,027 | |
| availability + avail_soft | 1,058 | tie |

- **The out-of-window check (E7-chrono-2425):** an identical recipe trained through 2024-25 GW11 and gated on 2024-25 GW12-30 scored **1,314 vs classic 1,261 (+53)**. avail_soft was +1 and availability_scaled −47. All-fields E7 had now won **2 of 2 held-out windows.** On its eval rows the chrono adapter improved 1GW MAE (2.080 vs 2.184) and appearance MAE (0.269 vs 0.324) but tied classic on 1GW Spearman (0.3263 vs 0.326) and was slightly below on 5GW Spearman (0.409 vs 0.427).
- **Lesson:** scout evidence converted at the decision layer, through 5GW ordering, rather than in the weekly showcase metrics. The win was small and still within single-window noise, which is why the chrono replication mattered. (A protocol caveat surfaced on 19 July: cutoff-week training rows carry 3/5GW labels, so every "through GW11" adapter has seen GW12-15 outcomes. All rungs share this, so rung-vs-rung comparisons stay fair.)

### Card: G2 — plan-horizon GRPO in the deployment regime

- **Intuition:** give RL the thing G1 couldn't express, **sequencing**: banking, chip timing, and transfers across weeks.
- **Change:** because TRL's GRPO is single-turn, the policy emits a **K-week plan** (a JSON array of weekly actions) in one completion. The environment rolls it through chained weekly states in which squad, bank and free transfers evolve under the policy's own choices. Actions are G1's knobs plus `bank_transfer` and `chip_play` (bench boost / triple captain). Reward = cumulative realized points minus a paired all-defaults sequential baseline. Horizon 6, stride 1, 8 epochs, a fresh LoRA.
- **Your two design rules (18–19 July), which became durable principles:**
  1. **The deployment-regime rule.** G2 must train on states whose forecasts are text-adjusted the way they will be live: classic plus legal adapter deltas plus scout snippets, not raw classic.
  2. **The two-model learning ledger.** A forecast adapter never trains on the week it adjusts. At week 20, chrono-2324 does inference only (articles in, deltas out), exactly like a live adapter, and week 20's *outcome* teaches only the layer above, as G2's reward. *Facts flow down at inference time; outcomes teach upward only.* This required a **chrono legality map**: chrono-2425 (cutoff 2024-25 GW11) may legally adjust 2024-25 GW12-38 and all of 2025-26; chrono-2324 (cutoff 2023-24 GW11) adjusts 2023-24 GW12-38 and 2024-25 GW2-11; 2022-23 has no legal adapter. Snippets (pre-deadline articles) are timestamp-safe for every week; only deltas need legality.
- **Text in the RL state:** per-player Δ1gw plus scout snippets condensed by the base model (greedy decode, cached, so deterministic). A spot-check before committing found two real bugs. Greedy decoding ran past the answer into non-Latin junk tails on 2.3% of rows (fixed with a tail cleanup). Worse, the "no evidence" sentinel check required `"nothing."` with a period, but the model answered bare `"nothing"` 67.2% of the time, so two-thirds of non-answers would have leaked into prompts as evidence. After both fixes, 32.3% of documents yielded real snippets.
- **Result (G2-v2, 232 steps, 30.6 hours, 59 deployment-regime episodes):** training reward climbed from −3.0 to +5.2 (means over 30 steps), KL tiny (0.0003–0.005), no collapse. Held-out 2025-26 GW12-30, three non-overlapping 6-week windows: **classic states +47 (3W/0L), adjusted states +27 (3W/0L), 6 of 6 windows won.** The learned behavior was mostly **chip timing**, i.e. bench-boost placement, plus one triple-captain call worth +13.
- **The empty-EOS attractor:** under greedy decoding the trained policy emitted an *empty completion* on 4 of 6 windows. When every completion in a GRPO group is empty, the group's reward has zero variance, so the advantage is zero and the empty mode is never penalized. It survives training, and argmax falls into it even though the training regime (temperature 0.8 sampling) usually escapes. Fix: `min_new_tokens = 8` at decode. **Check any GRPO-trained policy for this before trusting a greedy eval.**
- **v2b ablation (init from E7 merged into the base):** adjusted states +28 (ties v2, identical chip choices); classic states +3, where it played triple captain in every window regardless of state. Merging the SFT adapter specialized the policy to its training distribution and cost generalization. **v2 (fresh LoRA) stayed the candidate.**

### Card: E8 — podcast transcripts (a clean negative)

- **Intuition:** you asked for more and richer text. The Sky Fantasy Podcast is the richest FPL content there is (30–50k characters per episode), and the transcription pipeline was already built.
- **Change:** the E7 recipe plus Whisper large-v3 transcripts of 79 episodes (2024-26). Same rows and labels; coverage 84.4% vs 84.3%.
- **Two bugs found before training, both of which would have silently corrupted the result:**
  1. The attach script **replaces** a row's evidence documents on every call rather than merging, and v7 had been built from 8 files in a single call. The first E8 attach passed only 2 files, so coverage collapsed from 26,987 rows to 8,785. **The sanity gate (evidence coverage must exceed v7's) refused to launch training.**
  2. Both the attach and split stages truncated documents with a **prefix cut**. A player's first mention in a podcast averages ~70% of the way in (Cole Palmer at character 36,680 of 52,392), so the model would have seen only cold-open banter. Truncation was rewritten to **centre the window on the player's first mention**, with prefix fallback. That fix benefited every later run.
- **Result:** gate all-fields **1,025** (vs E7 1,069, classic 1,058), availability_scaled 1,002, avail_soft 1,060. Below E7 on all three configs and below classic on two. Eval MAE looked *better* than classic (5GW 6.609), but the `ranking_lift` diagnostic was already negative (−8.79 points/week on 5GW) before the gate ran.
- **Verdict:** do not ship; E7 stays champion; no Premier League Podcast transcription.
- **Lesson — bad text actively hurts.** Whisper mis-hearings, ~16% chunk duplication, and one moment sampled from a meandering conversation taught the adapter to react to noise. From here on, **precision of evidence beats recall.** A process lesson too: launching `nohup … &` and `sleep 120` inside one tool call let the tool's own timeout kill the trainer. Detached launches use `setsid nohup … < /dev/null & disown`.

### Card: G2-v3 — season-level chip budget (and a rule you caught)

- **The bug:** the plan environment reset chip legality for every 6-week window. The composed 3-window season eval therefore let v2 replay bench boost three times, which is impossible in real FPL.
- **Cheap diagnostic first:** fixing the environment and eval and re-running the *existing* v2 adapter (about 10 minutes of inference) gave **classic +23 (was +47), adjusted +20 (was +27).** The edge was real but inflated. The bigger finding was that v2 requested a chip in almost every week regardless of availability: it had never been trained in a world where chips run out.
- **Change:** a curriculum that samples a chip budget per training episode (both / bench-boost only / triple-captain only / none, weights 0.5 / 0.2 / 0.2 / 0.1).
- **Your correction mid-training:** the first fix modeled each chip as usable *once per season*. The real rule since 2025-26 is **one copy per half**, with GW1-19 and GW20-38 independent. The GW12-30 gate straddles the boundary, so the run (13 hours in, step 101 of 232) was killed and rebuilt half-aware: `chip_half(week)`, per-half availability, and legality enforced only in `rollout()`, which knows each week's half.
- **Result (after a pause for E9):** **+23 / +20, identical to the corrected v2 baseline.** The chip-scarcity curriculum made no measurable difference. G2-v3 nonetheless became the frozen decision-layer policy for GW1.

### Card: E9 — train on complete prior seasons, test on all of the next one (the biggest gate margin)

- **Intuition (yours, 30 July):** the "train through GW11, evaluate GW12-30" protocol isn't what you'll actually be able to do at GW1 2026-27, when no same-season data exists. Train purely on complete prior seasons and test on all of 2025-26: more realistic, and a bigger held-out set.
- **Change:** the E7 recipe byte-identical except `--train-through 2024-25:38` (zero 2025-26 rows) and `--eval-weeks 2025-26:2-30`. Train 29,184 rows; eval **7,424 rows** (53% more than before). The classic-only anchor was rebuilt on the same GW2-30 window (1,471) for a fair comparison. 1,824 steps, 45.9 hours.
- **Result:**

| config | E9 actual | vs classic-only (1,471) |
|---|---|---|
| **all fields, baseline optimizer** | **1,553** | **+82** |
| availability_scaled | 1,414 | −57 |
| **availability + avail_soft** | **1,549** | **+78** |

5GW MAE 6.68 (classic 6.86); appearance MAE 0.241 (0.302); SFT strict JSON 100% (base 76.6%).

- **The DefCon generalization test (your reframe):** 2025-26 introduced DefCon scoring, which E9 had never seen in any label. Could it pick the pattern up from evidence text alone? **No.** On the 962 of 7,424 player-weeks (13%) where a player actually hit the bonus, SFT MAE was 2.892 against classic's 2.593, i.e. **worse by 0.30**. On the other 87% SFT beat classic by 0.19, which is what carried the gate. Plain position slicing (DEF +0.118, MID +0.133) did not reveal this; only joining on the actual bonus threshold did.
- **Verdict:** E9 became the 2026-27 ship candidate, with a mandate to retrain through 2025-26 inclusive so the adapter sees real DefCon-era labels.
- **Lesson in hindsight:** the GW2-30 gate was one long 29-week window. Against a noise floor that grows with the square root of the number of windows, +82 over ~7 windows' worth of weeks is roughly 1.3σ using the adapter-comparison noise measured in September (24 per 4-week window), or ~2σ using the anchor-tweak figure (15). It looked like the strongest evidence in the project. It was real evidence, but weaker than it seemed at the time, and it was measured with an older anchor that F6 later improved (Section 3.9).


## 3.5 Era 4 (3 – 20 August 2026): building the ship

**What we believed:** the method was validated (E9), so the job was to train the real artifact on everything available, freeze it, and get the weekly pipeline ready.

### Card: E10-prelaunch — the GW1 ship model

- **Change:** E7/E9's recipe with the 7-file evidence set (podcast excluded per E8), trained through **2025-26 GW34** (37,888 rows), with GW35-38 (1,024 rows) held out only as a sanity check, not a discovery gate. 2,368 steps, 52 hours, final loss 0.182, 100% strict JSON.
- **Two findings along the way:**
  1. **The rearranged-fixture question (yours).** You asked whether the pipeline tracks *when* a rearranged match was actually played. Both source files tag each fixture with the round it was played in, so double gameweeks aggregate correctly and the deadline arithmetic is right. No fix was needed. But the stale guards `TRAINING_CUTOFF_WEEK = 30` and the GW31 exclusion were removed and the table rebuilt.
  2. **Status and news had been neutralized for all of 2025-26** (Section 1.4). Every adapter up to E9 had trained without the injury flag for its most recent season. E10 switched to the vaastav archive's values, believing them to be real history. *Correction, 3 October:* those values are end-of-season snapshots copied onto every week, so E10 and every later adapter learned from leaky status lines instead of blank ones (Section 3.10).
- **Result:** sanity backtest on GW35-38: 270 adjusted vs 268 classic, a wash. Eval MAE looked dramatically better (5GW 7.543 → 5.358), but that was largely a **measurement artifact**. The 5GW label is a forward sum that shrinks to almost nothing in the last weeks of a season (mean 10.75 at GW35, 2.64 at GW38), so both models were being scored against shrinking targets.
- **Verdict:** ship (the decision was already made via E9).

### Operational milestones

- **7 August — the GPU launch gate.** You said: after E10 and its eval, "not launch any more GPU runs unless I told you otherwise." From then on, every new GPU run needed your explicit go-ahead. CPU work was unaffected.
- **10 August — the season is live.** The API showed GW1 with a deadline of 21 August, eleven days out, sooner than the "~3 weeks" assumed in planning.
- **16 August — the ship freeze.** A read-only 1.0 GB snapshot at `~/fpl_freeze/2026-08-16_gw1_ship/` (code, data, evidence, and the E10 / E9 / G2-v3 adapters with md5s verified) so that continued development could not break the season deployment. Your publishing decision: **code only, no weights.**
- **Keeper strategy analysis.** Weekly lineup choice, including which owned keeper starts, is *not* an RL problem: it has no carry-over state, and the deterministic optimizer inside every rollout is already optimal given forecasts. Draft-time keeper-pair planning (expected max over the pair) was worth about 3 points a season by a fixture-slope estimate. That is below the noise floor, so it was not built.

### Card: G3 / G3b — give RL the transfer choice

- **Intuition:** G2 could only gate the greedy recommender (bank or don't, aggressive or not). It could never pick transfer A over transfer B, so multi-week squad planning was inexpressible.
- **Change:** `transfer_pick` (0–2) indexes the recommender's top three legal candidate transfers, with 0 reproducing the old behavior exactly. Plus squad-diversity augmentation: each episode's starting squad perturbed with 1–3 same-position swaps and bank jitter, taking 59 episodes to 236. Plus v3's chip curriculum. Two epochs, ~33 hours, compute-matched to v3. G3b resumed for a third epoch with the completion cap raised from 512 to 640 tokens, because about 65% of G3's completions were being truncated.
- **A bug on the way:** the G2 state caches predated a team-id fix and carried `team_id = -1` everywhere, so the 3-per-club check blocked almost every augmentation (74 episodes instead of 236). It was fixed with the same `team_id > 0` guard the rollout used.
- **Result:** G3 classic +8, adjusted +21; G3b classic +10, adjusted +15; v3 was +23 / +20. All within the noise of three windows.
- **Verdict:** **flat; stop scaling the G-track on this environment.** Transfer-choice agency, 4× augmentation and more training together produced no gain. (At the time we concluded that "truncation was not the bottleneck either." Reading the logs for this document shows the larger cap did *not* actually fix truncation: about 64% of G3b's completions still hit the limit, as did ~60% of v2's and v3's. So G3b says nothing about whether truncation mattered.) If the G-track resumes, it needs a richer evaluation environment (more and longer windows, scoring integrated with the real backtest) and completions that fit, before more training is worth GPU time.


## 3.6 Era 5 (21 August – 4 September 2026): the season starts, and the defects start talking

**What we believed:** the shipped stack was sound, and the season would be about operations. In fact the live season became the best diagnostic tool the project ever had, because every week produced specific, inspectable mistakes.

### GW1 (deadline 21 August): the draft, and the bench-order lesson

The GW1 squad was drafted on Wednesday 19 August from E10-adjusted forecasts by the beam-search draft, and you entered it verbatim: Sels, Donnarumma; Bijol, Shaw, Mitchell, Justin, N. Williams; B. Fernandes (C), Cunha, Saka, Groß, O. Dango; Watkins, Richarlison, Evanilson; £4.5m in the bank.

**Result: 38 against an average of 50.** Bruno captained for 2 raw points, Watkins played zero minutes, and the costly part was **our sheet never specified a bench order**. Mitchell was first on the bench, came on, and scored 1, while Bijol sat behind him with 10. With the right order the week would have been 47. You caught it. The fix was permanent: `apply_llm_deltas_and_draft.py` now prints "BENCH (enter EXACTLY this order)", ranking outfield bench players by expected fielded points (1GW points × availability weight), and writes `bench_order` and `vice_captain` into the squad file. The season ledger (`reports/season_2627_ledger.jsonl`) started the same day.

- **Lesson:** a decision you don't output is still a decision, made by default. Bench order is a model output, not an afterthought.

### Card: why no Arsenal defenders? — the 5GW head and season-end label truncation

- **Your question (21 August):** Arsenal had the league's best defence (19 clean sheets) and Gabriel was FPL's top-scoring defender (209 points), yet the draft contained zero Arsenal defenders.
- **The causal chain, measured:** Gabriel's 1GW baseline was excellent (4.74, second-best DEF), but his 5GW baseline was not (12.7, vs Bijol 17.1), and the draft's selection score is 5GW-dominated (5GW + 0.6 × 3GW + 0.35 × 1GW). Across 69 defenders with 1,500+ minutes, corr(real points-per-game, baseline_1gw) was 0.43 but corr(real PPG, baseline_5gw/5) only **0.20**. The most-deflated were the elite: Gabriel's 5GW/5 was 0.54× his own 1GW.
- **Root cause:** the 5GW label is a forward sum that shrinks to almost nothing in the last ~4 weeks of every season. About 13% of training rows carried artificially tiny multi-week labels: classic regression attenuation, hitting high-feature (elite) players hardest. E10's calibration shrink (correlation −0.75 with the baseline) stacked on top.
- **Fix — rate-normalized labels:** scale partial-horizon sums to full-horizon equivalents, `label_5gw = raw_5gw × 5 / weeks_available`. You preferred this to dropping season tails because it keeps every row.
- **Result:** corr(PPG, 5GW/5) 0.20 → **0.40**; Gabriel's ratio 0.54 → **0.89**; the classic draft's defence became Virgil / Guéhi / Senesi / Muñoz / Bijol with the full £100m spent. (Re-measured on 21 September, the 5GW head now correlates *better* with outcomes than the 1GW head: 0.353 vs 0.298.)
- **Lesson:** a label definition can silently bias a model against exactly the players you most want. Look at *who* is excluded, not just at aggregate error.

### Card: E11 — DefCon surfaced in the prompt, and the DefCon trilogy

- **Change:** E7's hyperparameters on corpus v10 (the new labels) plus evidence, fixtures, congestion, and a numeric DefCon line (last-3/last-5 averages plus the rule text, on 2025-26+ rows). Trained through 2025-26 GW34 and evaluated on GW35-38. The decomposition and role blocks were dropped to match what the live pipeline can produce. (E10, it turned out, had accidentally trained with no attach blocks at all.)
- **Result:** 1GW MAE **2.060** vs classic 2.211; 5GW 7.836 vs 8.162; +0.218 on the 89% of weeks without a DefCon bonus. But the DefCon-bonus slice was **still −0.390**, the third adapter with the same sign (E9 −0.299, E10 −0.424).
- **The trilogy, all three measured-closed:**
  1. *Classic threshold features* (`defcon_hit_rate_3/5`, the lagged share of matches clearing the position threshold): bonus-week MAE 2.496 → 2.494. Collinear with existing averages, so null.
  2. *Prompt-surfaced numeric DefCon* (E11): −0.390. A text feature does not override a learned shrink policy.
  3. *An inference guard* that shrinks negative deltas for high-hit-rate players (6 variants): every variant net-negative overall, because only about a third of high-hit-rate player-weeks actually convert to a bonus, so the shrink is right more often than wrong.
- **Verdict:** accept the drag (−0.39 on ~11% of rows, net clearly positive). **E11-full** (identical recipe, trained through 2025-26 GW38, 58.7 hours, loss 0.178, smoke test 48/48 strict JSON with delta magnitudes in E11's family) became the live adapter from GW2.

### Card: the evidence-quality investigation, extraction pilots, and digests

Your standing concern was whether we use enough articles, long enough, with real information ("before, we had the issue of only including the title"). You wanted this **tracked, not assumed**.

- **The audit tool** (`scripts/audit_evidence_quality.py`) on E10's training split: 84.3% of rows had evidence, at most 2 documents each, median window 265 characters, **0% title-only** (mention-centered windowing works), but the median window showed only **~2% of the source article.** Guardian made up 90% of documents and PL Scout 9%.
- **A metric bug you forced into the open:** the Scout case looked bad (39% shown), you pushed, and the audit turned out to match sources by *title only*. The Scout reuses identical titles every season, so it had matched last year's edition. The truth was 93.5% of the correct article. Keying is now (title, publication year).
- **Extraction pilot via Haiku subagents** (no API cost), 16 (article, player) pairs with your rule that **blank extractions must be surfaced, never silent**. Result: 6 blanks. Three were correct; one was a precision win (an "Ashley Phillips" article was about the pundit Az Phillips, a name collision that today's window would have shown as evidence); two were misses (Rogers' injury-page pointer, Krafth listed as "Injured (knee, Jun)" in a team-news table). A reworded v2 prompt recovered Rogers and Stroud; Krafth was still missed. **Ultra-terse table rows are an extractor blind spot,** so any extraction must fall back to the mechanical window.
- **The digest pivot (your insight):** per-player extraction is the wrong *form* for list articles (team-news roundups, price lists, bonus/DefCon tables) that carry facts about 20–40 players at once. One digest pass per article produces `{article_type, summary, player_facts[], team_notes[]}`. The Krafth article yielded 40 player facts, including his injury, plus a team note ("Newcastle: 5 defensive players out"). Your stronger proposal, to drop per-player rows entirely and fine-tune article → all-player adjustments, was deliberately *not* adopted: unanchored multi-player outputs are the free-override family that failed in every earlier test.
- **Haiku vs local Gemma A/B:** Gemma blanked less (1 of 16) but its extra recall was poisoned. It extracted a wrong-person Gallagher, garbled the pundit case, and said Krafth was "listed under Subs" when the article lists him injured, which is worse than a blank. Its digests failed to parse (my 700-token cap) and one fragment contained a likely hallucination. Haiku had zero hallucinations found. **Precision beats recall for evidence** (the E8 lesson), so Haiku became the extractor.

### GW2 (deadline 28 August): the walk-forward bug, caught by eyeballing

- **The bug:** the live frame joined each player's *last* training row and used its features as current form. All form features are lagged rolling windows computed *within season*, so once GW1 had been ingested, the last row was the GW1 row, whose lagged features were the season-boundary cold start (all zeros). Every live baseline collapsed: the 90th-percentile P(appear) was 0.13, a hold-squad XI totalled ~10 points, and Saka's 1GW went 4.65 → 0.78 with P(appear) 0.78 → 0.08.
- **How it was caught:** by looking at the numbers before shipping. Nailed starters at 0.08 P(appear) are impossible. A 615-row GPU decode had already run on the broken prompts and was archived as `*_BROKEN_BASELINE_v1.jsonl`.
- **Fix:** `_build_next_week_form_features` appends one synthetic week-(k+1) row per player (identity kept, match stats blank, the *real* next opponent from fixtures) and runs the ordinary feature pipeline over it. The synthetic row's lagged features are then exactly what a training row for week k+1 would carry. Training semantics by construction, with no hand-replicated feature list.
- **Lesson:** GW1 could never have triggered this (no same-season rows existed), so the loop's first live week validated a broken second week. The eyeball gate (compare the baseline distribution to the previous week and spot-check three premiums *before* spending GPU) became mandatory.
- **The week itself:** Watkins → João Pedro (the evidence showed a contract standoff plus zero minutes); João Pedro captained for 9; you kept Bruno, who scored 23 on the bench of our captaincy. **85 vs an average of 79.**

### Card: Haaland ranked 43rd — premium compression, F1–F3, and the F2b win

- **Your catch:** Cherki (14) and Haaland (13) topped GW2 while our adjusted blend ranked Haaland **43rd**, Cherki 27th and Foden 83rd. The top 15 was one-game wonders.
- **Three stacked, measured causes:**
  1. *Classic compressed premiums*: on the E11 holdout, the £8.5–11.4m band (n = 22) realized 5.64 points/week against a classic forecast of 4.07 (−1.56). A pooled ridge regresses extremes, and premium rows are ~2% of the error.
  2. *The adapter made it worse*: its learned global shrink cut premiums to 3.45. The shrink is right on most rows but unconditional; it cut Haaland like a mirage.
  3. *The draft had no captaincy leverage*: the beam is additive, but a captain doubles the best starter (~2.5 points/week for a 7-PPG premium over a 5-PPG alternative).
- **Fixes landed 30 August (all default-off until backtests blessed them):** F1, a premium-rank alarm (flags top premiums ranked below 25); F2, per-band calibration offsets; F3, captaincy leverage in the draft and in transfer evaluation.
- **Backtests (2025-26 GW11-30):** base 1,007; band calibration 987 (−20); leverage 1,007 (±0). **F2 rejected, F3 no effect.**
- **F2b, the prior-season quality blend, adopted (2 September):** early in a season, rolling form features are built on one to five games. F2b blends `points_avg_{1,3,5,8}` toward the player's prior-season per-week mean (joined by `code`), with weight `w = weeks_played / 6`, capped at 1. **Availability features are never blended** (your constraint: an injured player must stay floored and re-rank instantly on return), and a player with no prior season gets no fabricated pedigree. Haaland's GW2 `points_avg_3` went 2.00 → 5.87. Early-season backtests (GW2-8, draft after GW1): 2023-24 **+22**, 2024-25 **+32**, 2025-26 **−3**, net **+51 over 21 weeks.** Adopted for live builds.
- **F2c, the same idea for team-level rates** (goals for/against toward prior-season club rates): 2023-24 +8, 2024-25 −13, 2025-26 −6, net −11. Rejected. Team form is less sticky than player quality, because managers and transfers change club rates fast.
- **The 8-gameweek horizon** (your backlog question): an 8GW label and head on held-out 2025-26 GW26-30 had rank correlation 0.419 vs the 5GW head's 0.417. NULL; ridge signal is exhausted at five weeks.

### Card: E12 — article digests at scale (a flat result after a heroic build)

- **Change:** a router found 2,863 list-type articles across all evidence files. These went out in 115 batches of 25 to Haiku subagents, producing **31,043 player facts**, fanned out into **32,350 per-player mini-documents** with chrono-legal timestamps and team notes attached to named players. Narrative articles kept their windows. Everything else was identical to E11.
- **Orchestration lessons, now encoded in tooling:** agents processing paired batches had a ~45% defect rate (dropped rows from an off-by-one chunked read, scrambled order, malformed lines, "fatigue collapses" that blanked whole articles). Single-batch agents with a mandatory read-back self-check had near-zero defects. A verifier flags >30% empties or any empty fact-bearing title, and a repair script splices rows rather than rerunning batches. One self-inflicted wound: deleting six "stale" files that were actually completed outputs.
- **Result:** 1GW MAE 2.068 vs E11's 2.060. On the digest-bearing rows specifically, 2.006 vs 1.972.
- **Verdict: FLAT.** The *form* of evidence was not the binding constraint.

### Card: E13a — the market line

- **Intuition:** the adapter couldn't condition on price band because price and ownership weren't in the prompt; give it "Market: £X.Xm, owned by Y.Y% of managers."
- **Result:** 1GW MAE 2.059 vs 2.060; premium slice 3.49 vs 3.45. **FLAT.** MAE training gave the market line nothing to do.

### GW3 (deadline 4 September) and the first retrospective

O. Dango → Cherki (City exposure for Coventry at home). Our attack blanked league-wide (Bruno 2, Saka 2, João Pedro 1, Cherki 3), and Mitchell scored 15 on the bench with no legal trigger to bring him on. **38 vs an average of 51.** Cumulative: 161 vs 180.

You asked for a review and stated a preference: *"I personally favor changes [that] could improve things w scaling up either the SFT or RL step."* The retrospective (artifact 3bbe4e95) laid out the 21-experiment ledger and the pattern in it. **Input or capacity scale-ups had gone 0 for 7** (podcasts, digests, market line, DefCon prompting, chip curriculum, G3/G3b, the 8GW head). **Diagnosed fixes had gone 6 for 8** (residual SFT itself, rate labels, walk-forward, F2b, evidence-driven transfers, gates). The recommendation agreed with your instinct to scale but redirected it to the axes never tried: **data regime** (in-season incremental training), **objective** (a decision-weighted loss), and **reward environment** (RL on the forecast layer itself). You chose the last one first.


## 3.7 Era 6 (4 – 18 September 2026): RL on forecasts, the evidence overhaul, and fixture blindness

**What we believed:** the remaining gains would come from attacking the gap between accuracy and decisions directly, either through the reward (G4) or through better evidence selection (E14/E15). Neither paid. The biggest win of the project came instead from a single sentence you said about Bournemouth's striker.

### Card: G4 — reinforcement learning on the forecast layer

- **Intuition:** MAE gives premiums and decision-boundary players ~2% of the gradient. So reward the forecaster for the **realized points of the squad the decision layer picks from its forecasts**. Everything MAE under-weights is exactly what such a reward pays attention to.
- **Design (`docs/rl_forecast_design.md`):** a **per-player marginal reward**. For each player, sample G deltas, swap each into reference forecasts held fixed for everyone else, run the deterministic transfer and lineup decision, and score realized points. The group-relative advantage means players nowhere near a decision boundary get zero gradient, which is correct. Prompts were restricted to the ~40–60 decision-relevant players per week. The policy was initialized from E11 merged into the base, with a fresh LoRA, so TRL's adapter-disabled reference model *is* E11. G = 4, β = 0.04, temperature 0.8, 96-token cap. Training: 102 states, 4,554 prompt rows. Evaluation: 2025-26 GW30-38, with GW35-38 the clean sub-window.
- **v1 → v2:** v1 was stopped at step 162 because ~70% of optimizer steps had zero advantage. Batches of players whose decisions never move under any delta give reward 0 and variance 0, so there is no gradient. KL from E11 was ~1e-4. v2 kept only **boundary-sensitive** players (2,655 rows), trained 2 epochs at learning rate 2e-5, ~1,330 steps, ~42 hours. A reboot on 8 September killed it partway; it resumed from checkpoint.
- **Result (10 September):** decision value GW30-38 was classic 491, E11 480, **G4 487**. Per-week vs E11: 2 wins, **5 ties**, 2 losses, where the pre-registered bar was ≥3 wins. MAE 2.075 (passes), strict JSON 1,024/1,024.
- **Verdict:** **FAILS its gate.**
- **The correction that diagnosed the failure.** You asked, "oh shoot E11 is worse than classic now?" Re-running the *real* gate methodology (an accumulating squad over the same clean GW35-38) gave **classic 267 vs E11 277: E11 wins.** The G4 evaluation proxy had said the opposite (247 vs 231) because its state cache **resets every week to the classic trajectory's squad**. It measured a one-week marginal transfer from someone else's squad and could not see the adapter's real value, which is compounding squad quality over a trajectory (E11's edge came from a different captain in GW36, Semenyo over Bruno, worth 83 vs 75). **G4's reward optimized a metric that inverts the sign of the thing we care about.** Add step-function sparsity (5 of 9 weeks unchanged), ~15 points of weekly noise, bounded deltas and a KL leash, and the null is fully explained.
- **Lesson:** any future forecast-layer RL must reward *multi-week trajectory value* from a self-built squad, not one-week marginal decisions. And check your evaluation proxy against the real metric *before* using it as a reward.

### Card: E14 and E15 — the evidence-selection overhaul (best MAE ever, worse decisions)

- **The diagnosis (your challenge):** "the LM should see Calafiori's offensive contribution / Arsenal clean-sheet odds / the Scout recommending him." You were right that **the Scout's recommendation never reached the model.** There were two bottlenecks. The attach stage capped at 3 documents ranked purely by *mention count*, so all three of Calafiori's GW4 slots went to 25–29k-character match reports while the FPL-analysis pieces never entered the corpus. And the split stage's "scout" title pattern matched almost no real Scout titles ("Scout Selection", "transfer radar", "best FPL captain" all failed).
- **E14 (budget only):** 3 documents × 700 characters instead of 2 × 260. 1GW MAE 2.062. **NULL.**
- **E15 (budget + selection):** `--analysis-first` ranks FPL/Scout-genre titles above match reports; `--max-docs 5`; **multi-mention windowing** (up to three mention passages merged with " … " instead of one window on the first mention); a broadened title taxonomy, with three false positives found and reverted: "deadline day" and "who (is|could|are)" matched transfer live-blogs, and "in fantasy" matched "Mike Dean accused of being 'in fantasy land'". PL Scout's share of documents rose from **3.5% to 19%**, and median window from 265 to 705 characters. On the 27,427-character Arsenal–Chelsea report, the old window showed only "67 min: … replace Calafiori"; the new one also showed "Calafiori has a goal disallowed" and "Calafiori marches infield … belts a right-foot shot."
- **Result:** **the best MAE ever measured**: 1GW 2.059, 3GW 4.864, 5GW 7.797, the first change in five to improve every horizon, plus the best DefCon slice (−0.365). Then the real gate on GW35-38: **E15 264, E11 277, classic 267.** E15 won GW38 big but lost GW36 and GW37 on captaincy and transfer choices.
- **Verdict:** **does not ship.** E11-full stays champion. The broadened taxonomy went behind a flag (`FPL_BROAD_SCOUT_PATTERN`, default off) to keep live decodes in parity with what E11-full trained on.
- **Lesson:** this is the cleanest single demonstration in the project that **MAE and decision value dissociate.** The evidence work was correct as engineering (the model now sees the right documents) and still didn't help decisions.

### Card: F5 clean-sheet features, the alpha sweep, and "the ridge is at its ceiling"

- **Your question:** why do Arsenal defenders rank below Justin and Shaw, given clean-sheet odds and attacking returns?
- **Finding:** `clean_sheets` and `goals_conceded` existed in raw data but were never carried into the feature set. The attacking features were collinear and sign-flipped in the 1GW head (xGI_3 +0.42 vs xGI_5 −0.48; xG_3 −0.27 vs xG_5 +0.34): correlated pairs cancelling into noise, with the subjective FDR integer the second-largest weight.
- **F5** (`clean_sheet_rate_3/5`, `goals_conceded_avg_3/5`, values verified correct): backtest GW2-8 × 3 seasons **407 / 440 / 365 vs 411 / 440 / 406, net −45.** Rejected. A ridge alpha sweep (1 / 10 / 50: 1,257 / 1,255 / 1,239) didn't fix the sign flips either.
- **Then the decomposition you pushed for three times, which showed my framing was wrong twice.** The *classic* model ranked Arsenal defenders correctly *above* Justin (5GW: Calafiori 19.96, Gabriel 19.19, White 18.31 > Mitchell 17.63 > Justin 16.80). The *adapter* flipped part of it via a shrink proportional to the forecast (Calafiori −6.00 or −30%, Gabriel −3.60, White −3.30, Justin −2.40). Only Calafiori ended below Justin.

### Card: the Calafiori case — the adapter was right

- **Your suspicion:** "SFT dropping points for Arsenal is something wrong."
- **Diagnostics:** regressing the adapter's 1GW delta on the classic forecast across all 654 GW4 players gives R² of only **0.194**. About 81% of delta variance is player-specific, so this is not a disguised global shrink. Evidence changes behavior (mean delta −0.330 with evidence vs −0.260 without). Calafiori was the second-largest residual in the set. His prompt contained a Guardian line, "67 min: Double substitution for Arsenal — Hincapie and Zubimendi replace Riccardo Calafiori." The model pinned `delta_minutes` at −20 and `delta_appearance` at −0.25, **both at the schema bound**: a rotation read. It gave Gabriel and White small *positive* minutes deltas.
- **Ground truth:** Calafiori's minutes in GW1-3 were 80 / 90 / **66**; White's were 90 / 90 / 90. **The model was correct.** Buy White or Gabriel, not Calafiori.
- **Tool:** `scripts/explain_player_delta.py` now prints classic vs delta vs final plus the exact evidence text the model read, and flags "MINUTES DELTA AT BOUND → rotation/injury signal." Run it *before* concluding the model is broken.
- **Lesson:** sometimes the human objection uncovers a defect and sometimes it uncovers a correct model. Both outcomes require looking at the evidence the model actually saw.

### Card: team-level evidence — four regex failures

- **Your point:** the press questioned Manchester United's rotation around a midweek European game, and praised Arsenal's defence. SFT should have picked both up.
- **The gap is real:** attachment is by surname, so team-level analysis never reaches the players it is about. A Guardian piece on Arsenal's defensive start mentions Gabriel, White and Saliba **zero** times.
- **Four attempts at keyword/regex team attachment each failed in a new way:** "MUN" matched Bayern "Munich"; match live-blogs swamped the channel with mailbag chatter (Arsenal defenders received a discussion of kit colours); women's and youth articles share club names (Shaw received a WSL report); and transfer-rumour columns and opponent-rotation paragraphs won (Justin received *Chelsea's* rotation news). Parked.
- **Lesson:** **structured data beats mining prose.** The right tool already existed: the digest pipeline's `team_notes`, which are high-precision and were designed for this fan-out.

### GW4 (deadline 12 September) and the settled-data rule

Richarlison → Isak (Richarlison had left the league, a dead slot). Bruno captained again, 2 points. **61 vs an average of 69.**

During the week I narrated a provisional score as final, "59 vs 63, three defenders blanked", and built a post-mortem on it, when **Leeds had not kicked off yet.** You corrected me ("justin and bijol are ok - leeds haven't played till tmrw"). It was the second offence (GW2's mid-week average had read 66 and settled at 79). A note hadn't been enough, so the rule became a script: `scripts/gw_status.py --event N --require-settled` prints per-fixture state and exits 1 until every fixture is finished *and* bonus points are confirmed. It runs first in the weekly ingest.

### Card: fixture blindness → F6, the largest measured win in the project

- **Your catch (GW5 preparation):** Liverpool's defence is good, so Evanilson (Bournemouth, at home to Liverpool) should be discounted. The model had him as its top bench-or-start candidate anyway.
- **The measurement:** across 56,122 historical rows of started players, real 1GW points by opponent leakiness quartile:

| position | toughest quartile | leakiest quartile | ratio |
|---|---|---|---|
| GK | 2.79 | 3.30 | 1.18× |
| DEF | 2.09 | 2.79 | 1.34× |
| MID | 2.49 | 3.11 | 1.25× |
| FWD | 2.86 | 3.66 | 1.28× |

Real points swing 25–34% between the toughest and leakiest opponents. **The forecast moved about 2%** across the same range.

- **Three compounding causes, all verified:**
  1. *The anchor coefficient was effectively zero.* Standardized ridge coefficients on the 1GW head: `opponent_goals_against_avg_3` **+0.0041**, `opponent_goals_against_avg_5` **−0.0163 (wrong sign)**. The model leaned instead on `fixture_difficulty_mean` (−0.4598), FPL's coarse 1–5 FDR integer, which rated Liverpool 4 and Brighton 3 when the real defensive gap was 2.5×.
  2. *The relationship is multiplicative.* A 5-point forward loses far more against a good defence than a 2-point defender does. A plain additive term cannot express that, which is why the raw feature sat at ~zero weight despite being present since day one.
  3. *The prompt suppressed the LLM channel.* The provenance block written in E6 told the adapter that the classic signal "already prices in … team/opponent form, this GW's fixture … adjust only for" other things. The adapter obeyed. On the GW5 decode, corr(delta, opponent goals conceded) was **−0.048** while corr(delta, baseline) was **−0.708**. The LLM channel had collapsed to an unconditional shrink of about −0.45, identical in every fixture quartile.
- **The fix — F6 (`FPL_OPPONENT_INTERACTION=1`):** centre opponent goals-conceded within season (`opp_def_weakness_{3,5}`), then cross it with the player's own output: `form_x_opp_weakness_{3,5}` (points form × weakness) and `xgi_x_opp_weakness_{3,5}` (expected goal involvement × weakness).
- **Result:** 1GW MAE 2.0814 vs 2.1152, **−0.0339, winning 4 of 4 windows.** Decision value **+112 over 5 windows** (−13, +50, +60, −46, +61), the strongest margin in the project. Within-player fixture sensitivity more than doubled: the old anchor captured 19% of the real effect, F6 captures 42%.
- **Lesson:** a feature can be present for months and contribute nothing, because the model's functional form can't use it. And **a prompt is not neutral**: a confident sentence about what the anchor handles can switch a channel off. Any claim in a prompt about what the anchor covers must be *true*.

### Card: the live status gap

While building depth-chart features for your Konsa case, the injury flag for 2026-27 turned out to be **0.0000 flagged across 2,549 rows**, against 19–38% in every historical season. Saliba read "available" with a back injury and zero minutes for four weeks. The official sync had neutralized status, as it had for 2025-26 history. The fix restores the pre-deadline snapshot from our own archived weekly corpora: 2,505 rows filled, 534 changed, flagged rate 0.140. It is now wired into `run_weekly_ingest.sh` with a verification gate that stops if the flagged rate is still zero. Without it, the planned in-season training would have learned from a season in which nobody is ever injured.

### Card: F7 depth chart and F8 finishing regression — two good intuitions that fail as linear features

- **F7 (your Konsa case):** "you cannot tell [this] from the previous goals of the player, you need to go deep into understanding what's going on for the game." Correct: nothing in a player's own history encodes "the man ahead of me is out." Konsa's GW5 prompt mentioned none of Saliba, Mosquera, Gabriel, Timber, Calafiori or White. Built `pos_minutes_share_3`, `pos_rivals_unavailable`, `pos_rivals_minutes_vacated_3` and `pos_unit_size`. **+0.0107 MAE, lost 4 of 4 windows.** `pos_minutes_share_3` has the highest raw correlation with points yet hurts most, because it is collinear with `minutes_avg_3`. Conclusion: a depth chart belongs in the *prompt* as a rendered block, because whether a role actually changes is a judgment over text, which is the LLM's job.
- **F8 (your Calafiori case):** form features are built on actual points, which embed finishing luck that may not persist. Built goals-over-xG, assists-over-xA and involvement-over-expected. **−0.0003 MAE (null); coefficients ≈ 0 and mostly positive**, the opposite of mean reversion. Out-performing xG is confounded with being a good finisher in a good situation; once xGI, ICT and form are in the model, the residual carries nothing. The intuition *is* right for extreme tail events on low-rate players (Mitchell: 4 career goals in 203 appearances, then 2 in one match), which needs a per-player rate-plausibility check, not a linear term.

### E17 launched (18 September), and the GW5 sheet

E17 combined three changes against E11: the F6 anchor, a depth-chart and opponent-record prompt block, and a corrected provenance line (`FPL_PROMPT_V17`) that stops forbidding fixture adjustment. Its prompt gate failed on the first attempt, with `opponent = 0` on all 37,888 rows: the team-name-vs-id bug from Section 1.4. **The gate paid for itself on its first run**; without it we would have trained ~50 hours with the headline feature missing. Prompts ran 32% longer (mean 947 → 1,251 tokens; 0.8% over the cap), making it a ~71-hour run.

For GW5 (deadline 18 September), after several of your pushes:
- **Transfer: Shaw → Konsa** (free). I overrode Konsa's P(appear) from 0.74 to ~0.93: the model averaged in GW1 (0 minutes) and GW2 (11 minutes) as a new signing behind Mosquera, but Mosquera was now injured and Saliba out.
- **You moved Cunha into the XI over Evanilson** (Liverpool's defence makes Bournemouth hard to score on). Saka captain.
- **Result: 61 vs an average of 48, +13**, the best relative week of the season. Your call was the week's best (+8: Cunha 10, Evanilson 2). Two of mine cost points: Konsa over Mitchell (−6: Konsa 1, Mitchell 7), and bench order with Evanilson ahead of Mitchell (−5: João Pedro didn't play, and Mitchell was a legal substitute who would have brought 7 instead of 2).


## 3.8 Era 7 (18 – 29 September 2026): the international break — measurement over capability

**What we believed:** with a 21-day gap to GW6 and no weekly deadline pressure, the break was the one window to spend GPU on *measurement* rather than capability. You asked for "a series of improvements and continuous eval." The plan made two gates mandatory for every run: **decision value on ≥3 windows**, and **a live mechanism**, meaning the adapter must measurably respond to the signal the run was built around.

### Card: E17 verdict — split: ship F6, don't ship the adapter

- **Training:** 71.9 hours, final loss 0.1811, token accuracy 0.9391, strict JSON 1,024/1,024. Indistinguishable from E11-full's fit.
- **Decision value on GW35-38, decomposed:**

| configuration | points | contribution |
|---|---|---|
| classic, old anchor | 247 | — |
| + E11 adapter | 260 | +13 |
| classic, F6 anchor | 270 | **+23 from F6 alone** |
| + E17 adapter | 300 | +30 |

E17 was the first configuration ever to beat classic-only on decision value (300 vs 270).

- **But MAE went the wrong way:** E17's adapter improved its anchor by 0.105 (2.199 → 2.094) against E11's 0.151 (2.211 → 2.060).
- **And the designed mechanism did not engage.** The new `scripts/check_delta_mechanism.py` computes partial correlations of the adapter's 1GW delta with each designed signal, *controlling for the baseline* (raw correlations are contaminated by the baseline-proportional shrink, correlation −0.689). Results: opponent goals conceded **−0.0506**; injured/doubtful team-mates **−0.0328**. Both are zero. The prompt invited the fixture adjustment and the model declined.
- **Verdict:** adopt F6 (well-supported: +23 here, +112 over 5 windows, MAE 4/4); keep E11-full as the deployed adapter; **an outcome without a mechanism is a coincidence.**
- **The leading hypothesis:** F6 had already removed the fixture signal from the residual, leaving nothing for the adapter to learn. The clean test is the F6 anchor with the *original* prompts (E18).
- **A deployment constraint recorded here:** F6 changes the anchor, so the deployed adapter's deltas were learned against the old baselines. F6 and a matching adapter must be deployed together or not at all. Until then the live stack stays old anchor + E11-full.

### Card: the premium-minutes defect — real, significant, and not worth fixing

- **Found while re-checking the 5GW head:** the five-week bias is strongly concentrated by price, and the sign has **flipped** relative to the GW2 premium-compression finding. On the current anchor, players priced £9.5m+ are **over**-predicted.
- **The measurement** (1GW bias = actual − forecast, walk-forward, players averaging >45 minutes, 6 windows over 3 seasons):

| price band | bias | n |
|---|---|---|
| < £6.0m | +0.033 | 9,982 |
| £6.0–7.4m | +0.064 | 1,534 |
| £7.5–9.4m | +0.152 | 572 |
| **£9.5m+** | **−1.094** | 202 |

Over-predicted in 6 of 6 windows; t = −3.49; 95% CI [−1.71, −0.48]; bootstrap P(bias < 0) = 1.000. Not caused by our own changes: with the F2b blend off the figure is −1.101.

- **Root cause isolated: minutes, not scoring.** When a premium plays 60+ minutes (73.3% of weeks), the forecast is exact (5.90 vs 5.91, bias +0.010). The entire error is the 26.7% of weeks they don't (forecast 4.82, actual 0.70, bias −4.119). Premiums start at the same rate as everyone else, but the forecast lost is twice as large, so where the errors cancel for ordinary players they don't for premiums. **It is a captaincy defect**: we captain from this band and the multiplier doubles the error.
- **Six hypotheses tested, all rejected:**
  1. *European rotation (F9 congestion features)*: built correctly (the flagged clubs are exactly 2024-25's European qualifiers), but they moved the premium gap only from −1.129 to −1.110. Then the test that should have come first: premiums start **80.5% without a European game and 79.0% with one.** The causal claim was falsified outright.
  2. *Hot-player regression*: the gap survives a hot/due control in every tercile.
  3. *Price concavity*: actual points keep *rising* at the top of the price range.
  4. *"Premium" as a proxy for "high forecast"*: within the top two forecast deciles the gap sharpens. Premiums forecast at 5.84 actually score 4.74, while non-premiums forecast at 4.18 score 4.41.
  5. *Price momentum*: nothing.
  6. *Bending the price curve (hinge terms)*: the gap widens (−1.21 to −1.27), because extra freedom fits a steeper top slope that doesn't hold out of sample. Dropping price entirely closes 35% of the gap but costs MAE in every window, so price carries real signal.
- **The decisive test — does correcting it win points?** Band calibration, now correctly signed, scored 628 → 620 and 486 → 472: **−22 over two windows.**
- **Verdict:** **real but not actionable; closed.** (Rescored against the noise floor a day later, −22 is −1.04σ: the honest statement is "doesn't help," not "hurts.")
- **Lesson — calibration is not ranking.** Premiums are over-forecast, but at the same forecast level they still out-score the alternatives (4.74 vs 4.41). Shrinking them makes the forecast honest and the squad worse, because it shifts money away from players who are still the best available. A process lesson too: **test the causal claim before building the feature.** A two-minute check would have killed F9 before a line of code was written.

### Card: the GW5 case-study round — decompose before calling luck

At your suggestion the weekly ritual became: rank our forecasts against actual points, take the largest misses in both directions, and investigate 3–5 individually.

- **The big lesson:** I had told you Mitchell's form was luck-inflated, citing 4 career goals in 203 appearances. That was true of his two-goal week. But I let it discount his *whole* output, and that drove both of my GW5 misses. His GW5 return was **7 points from a clean sheet and bonus, with an expected goal involvement of 0.02**, a different and repeatable source the luck argument never touched. **Split a player's points into attacking (testable against xG) and non-attacking (minutes, clean sheets, bonus). Only the first is luck-testable; a defender's floor lives in the second.**
- **Groß:** 7 goal involvements against 2.63 expected (+4.37), so the "lucky" call stood. But he takes maximum bonus in 3 of 5 games, and deep-playmaker BPS is repeatable, so his floor is higher than raw xGI implies.
- **Brobbey:** the best underlying rate in the group (0.69 xGI/90), points 2/2/2/1 and then 17 on genuinely earned chances. We forecast 2.19 because the anchor tracks recent *points*, not underlying output. Generalized, this became **F10** (rank of xGI minus rank of points): +0.228 points/week between the extremes, positive in 5 of 6 windows.
- **Manzambi:** started and scored 13 on a 15% appearance probability. Role-change blindness again, the Konsa case, still unfixed.
- **Calibration where it matters is fine:** of 89 players rated ≥90% to appear, 95.5% appeared. The four who didn't all had status "a" and no pre-deadline news, so they were genuinely unforecastable.

### Card: F11 — the decision-weighted loss, prototyped for free (and E20 cancelled)

- **Intuition:** the one axis the ledger said was never tried is the **objective**. A plain fit spends its effort on players nobody picks: the top 15% by recent form are 15.7% of rows but **41.3% of squared error**. This was queued as E20, a 56-hour adapter run.
- **Change:** weighted least squares in the ridge (`FPL_DECISION_WEIGHTED`), with weights renormalized to keep effective sample size fixed so alpha keeps its meaning. A cheap prototype of the same objective change.
- **The proxy said yes:** on "mean actual points of the 11 highest-forecast players each week", every weighting scheme improved both error and picks. The best implied **+0.69 points per pick per week (~7.6 points/week).**
- **The real squad backtest said no:** +24, 0, −2, −2, +5 = **+25 over 5 windows, 2 of 5**, nearly all from one window.
- **Verdict:** unresolved (+0.75σ). **E20 cancelled.**
- **Lesson — never promote a proxy to a verdict.** The proxy ignores budget, formation, transfer costs and the bench, and those constraints absorb almost all of a pure ranking improvement. It overstated the effect about 30×.

### Card: the noise floor — measuring the instrument

After five nulls in a row, the next step was to measure what the decision backtest can resolve.

- **Estimate:** pooled per-window deltas from experiments independently judged null (F10 [6, 0, −31, 4, 24], F11 [24, 0, −2, −2, 5], band calibration [−8, −14]). n = 12 windows, **sd = 14.9 points per 4-week window.**

| windows | sd of the total | need total above this for 95% |
|---|---|---|
| 3 | 25.9 | 50.7 |
| 5 | 33.4 | 65.5 |
| 8 | 42.3 | 82.8 |
| 12 | 51.8 | 101.4 |

- **Rescoring the ledger:** F6 +112 over 5 windows = **+3.35σ, real.** F11 +25 = +0.75σ. F10 +3 = +0.09σ. Band calibration −22 = −1.04σ. Two of my own earlier claims were corrected. Band calibration doesn't "lose 22 points"; it doesn't help. And E17's +40 *was* probably not noise at 2.68σ, but the decomposition showed the adapter's marginal share (+17 over E11's) was the noisy part.
- **The planning consequence:** to detect an edge of X points per window you need n > (1.96 × 14.9 / X)² windows. F6-sized effects need ~2. A 10-point edge needs ~9. A 5-point edge needs ~34. "Flat" from now on means **unresolved**, not disproven.
- *Two corrections were added on 29 September (Section 3.9):* this 14.9 figure applies to small anchor tweaks, not adapter comparisons; and for anchor-only tests, windows are cheap.

### Card: the attenuation audit and F12 — a discovery method that doesn't generalize

- **Intuition:** F6 was found by comparing the real effect of a signal on next-week points against how much of it the forecast carries. Sweep that over every feature and the next F6 should fall out.
- **Why it fails:** pooled slopes are confounded by quality (better players get more minutes, cost more, face different schedules). Within-player slopes are corrupted for anything autoregressive: a rolling average is high precisely because recent scores were high, and the next score mean-reverts, so 13 of 17 signals flagged as "wrong sign." That was the estimator misbehaving, not the model. **The audit is only licensed for signals the fixture list assigns** (opponent, difficulty, venue, team form), which is why it worked for F6.
- **The one survivor:** the player's own team's attacking form (captured 0.45 marginal / 0.44 within-player). F12 crossed it with the player's xGI and minutes: **+8, −9, −32, +2, −11 = −42 over 5 windows, −1.26σ.** Unresolved, leaning negative.

### The stopping rule (23–24 September)

Seven consecutive anchor experiments had failed to clear the bar, and the last five were not even resolvable (F7, F8, F9, F10, F11, F12, band calibration). The interpretation: F6 worked because it was a *large* defect, the anchor carrying ~19% of an effect worth 25–34% of a player's score. Defects that size appear to be rare, and we may have taken the main one. **So: no more anchor-feature hunting this break.** The real danger was not wasted time but that one result would eventually land at +60 by chance and get shipped. All flags stay in the code, default off.

### Card: E18 — prompt isolation: the v17 blocks were worth nothing

- **Change:** the F6 anchor with the **original v1 prompts**, isolating E17's prompt changes.

| | 1GW MAE | decisions GW35-38 |
|---|---|---|
| E17 (v17 blocks) | 2.0935 | 300 |
| **E18 (v1 prompts)** | **2.0932** | **308** |

- **Verdict:** three independent lines agree the blocks are inert: the mechanism check, MAE and decision value. Dropped. They cost 32% longer prompts and ~12 extra GPU hours.
- **The claim that turned out false:** on the same window, E18 beat classic+F6 308 to 270. I reported that as "+38, +2.55σ — the first solid evidence on the decision metric that the adapter earns its place."
- **A gate bug fixed:** the mechanism check announced "none of the designed signals moved the delta" for E18, when those signals were *absent* from v1 prompts by design. It now separates "signal absent" from "signal present and ignored."

### Card: E19 — the twelve-week holdout overturns the adapter's standing

- **Design:** train through 2025-26 **GW26** instead of GW34, giving a 12-week holdout (GW27-38) = **three independent 4-week decision windows**, at a cost of only 5% of training rows (35,840 vs 37,888). F6 anchor, v1 prompts. Training was healthy: 2,240 steps, loss 0.147, token accuracy 0.939, strict JSON 3,072/3,072.
- **Result:**

| window | E19 | classic+F6 | delta |
|---|---|---|---|
| GW27-30 | 220 | 258 | **−38** |
| GW31-34 | 212 | 234 | **−22** |
| GW35-38 | 339 | 270 | **+69** |
| **total** | **771** | **762** | **+9 (1 of 3 windows, +0.35σ)** |

MAE behaved as always: classic 2.2716, E19 2.1358 (+0.136).

- **Why this matters more than the number:** **GW35-38 is the window on which every adapter from E10 onward had been judged** (E10's sanity check; E11, and through it the E11-full consolidation; E12, E13a, E14, E15, E17, E18). It is the only one of the three where the adapter wins. (E9's large win was on GW2-30, a different, earlier stretch with the old anchor.) E18's "+2.55σ" was a **false positive** from single-window evaluation, and E19 was the run built to catch exactly that. It worked on its first outing.
- **Rules changed:** never judge an adapter on GW35-38 alone; the ≥3-window rule applies to adapters too (E19 shows it costs only 5% of training data); report "unresolved" with a sigma, not "flat" or "wins."
- **A second gate bug fixed:** the mechanism check reported a team-mate-injury signal as present in E19 (partial −0.079, "wrong sign") although E19 has no depth-chart block. The regex was matching injury words in the attached news text. Count patterns are now scoped to their own prompt block.
- **The question the session ended on:** "the honest question is whether the adapter should stay in the live path at all… It costs nothing to run and improves forecast accuracy, but I can no longer claim it improves your squad." Your reply ("I don't know how to decide this… shall we try go harder on each path?") arrived just as that session hit its monthly spend limit, which is where this session picked it up.


## 3.9 Era 8 (29 September – 3 October 2026): what the adapter actually does

**What we asked:** before deciding whether the adapter stays in the live path, find out *what* it contributes, using only predictions already on disk (CPU, no GPU, nothing live touched). Scripts and results are saved in `reports/adapter_bench_2026_09_29/`.

### Finding 1: about 90% of the accuracy gain is a uniform shrink

On E19's 3,072 holdout rows, I fitted, separately for each week and horizon, a straight line predicting the adapter's points delta from the classic forecast (`delta ≈ a + s × baseline`). No labels are used, so this is deployable live. The fitted line is the **shrink component**; what remains is the **player-specific component**.

| | 1GW | 3GW | 5GW |
|---|---|---|---|
| corr(delta, baseline) | −0.650 | −0.561 | −0.544 |
| share of delta variance explained by the line (R²) | 42% | 32% | 30% |
| mean delta | −0.49 | −1.43 | −2.39 |

| 1GW MAE (lower is better) | all rows | evidence present | no evidence | top-10% baselines |
|---|---|---|---|---|
| classic | 2.2716 | 2.2885 | 2.1915 | 3.4575 |
| classic + full adapter delta | **2.1358** | 2.1457 | 2.0890 | **3.2438** |
| classic + shrink component only | 2.1478 | 2.1633 | **2.0746** | 3.2676 |
| classic + player-specific component only | 2.2590 | 2.2703 | 2.2059 | 3.4280 |

The shrink alone recovers 0.124 of the 0.136 MAE gain, about 91%. On rows *without* evidence, the shrink alone beats the full adapter: the player-specific part is noise when there is nothing to read.

**Decision value of the shrink alone: 258 / 233 / 270 vs classic 258 / 234 / 270, i.e. −1 over three windows.** A monotone transform barely changes ranking, so it can't change squads. *The adapter's accuracy advantage is calibration, and calibration is decision-neutral.*

### Finding 2: the adapter's real information is about availability, and it depends on the season phase

Appearance probability: Brier score 0.1727 (classic) → 0.1275 (adapter). Part of that is calibration (classic P(appear) averaged 0.694 against an actual rate of 0.836 on this holdout), but the adapter beats even a recalibration of classic **fitted on the holdout's own answers** (0.1335). What calibration cannot produce is *discrimination*, the ability to separate who plays from who doesn't. That is measured by AUC (0.5 = a coin flip). Among likely starters (classic P ≥ 0.5):

| decode | classic AUC | adapter AUC | gain |
|---|---|---|---|
| E19, 2025-26 GW27-38 (late season) | 0.547 | **0.717** | **+0.170** |
| E9, 2025-26 GW2-30 | 0.645 | 0.658 | +0.013 |
| E7-chrono, 2023-24 GW12-38 | 0.628 | 0.656 | +0.028 |
| E7-chrono, 2024-25 GW12-38 | 0.634 | 0.675 | +0.041 |
| **Live 2026-27 GW2-5 (E11-full)** | 0.673 | **0.673** | **0.000** |

Live evidence coverage is not the cause: 95% of live rows carry evidence, against 83–86% in the training-era sets, and Guardian articles are flowing again. The likelier reading: **the LLM helps when the numbers go blind.** Late-season rotation, dead rubbers and injury crises are where the classic model's P(appear) collapses toward a coin flip (0.547) and pre-deadline team news matters. Early in a season, availability is predictable from the numbers.

*Two caveats discovered on 3 October (Section 3.10) qualify this finding substantially. First, the classic "P(appear)" being beaten here is predicted minutes ÷ 90, a strawman; a logistic classifier on the same features beats the LLM. Second, historical status/news lines are end-of-season snapshots, which are most "accurate", and most leaky, in exactly this late-season window.*

**The optimizer barely listens to this channel.** In the default decision layer, appearance probability enters only through a threshold penalty below P = 0.6. The code itself calls availability-only mode "decision-inert." The LLM's best signal is mostly unused while its shrink, which isn't a decision signal, gets full weight. This was also the finding of 8 July (Section 3.3), rediscovered with better instruments.

### Finding 3: routing availability into points looked great, then faded

The hypothesis was **written down before any backtest of it was run**: route the availability signal into points. For each player, `points_h' = classic_points_h × ratio / mean_week(ratio)`, where `ratio = clip(P_llm / P_classic, 0.6, 1.4)`. Dividing by the week's mean ratio removes the global level shift, so only relative availability information re-ranks players. Call it V3.

| test set | windows | raw adapter (as deployed) | V3 (availability routing) |
|---|---|---|---|
| E19, 2025-26 GW27-38 | 3 | +9 (1/3) | **+52 (3/3)** |
| E9, 2025-26 GW2-25 | 6 | +16 (2/6) | +42 (2/6) |
| E7-chrono, 2023-24 GW12-35 | 6 | −39 (2/6) | +136 (4/6) |
| E7-chrono, 2024-25 GW12-35 | 6 | +53 (4/6) | −65 (3/6, one window −111) |
| **all 21 windows** | **21** | **+39** | **+165 (12/21)** |

V3 was the first adapter-derived configuration to win all three E19 windows. On 18 independent replication windows it netted +113, with 9 wins and 8 losses. **Unresolved, leaning positive**, and its gain tracks the availability signal, which is large only where E19 tested it.

Other variants on E19: de-shrunk points (player-specific component only) +28 (1/3); raw `availability_scaled` −18; evidence-gated deltas −5.

### Finding 4: the raw adapter is worth about zero over 21 windows

Across 21 four-week windows (~84 gameweeks, 3 seasons, 4 adapter generations), the adapter applied as deployed nets **+39 points against classic+F6**: a mean of +1.9 per window, 95% interval roughly −2.4 to +3.3 points per gameweek. *Caveat:* 18 of the 21 windows use older adapters (E7, E9) trained against the pre-F6 anchor and applied on the F6 anchor, so this measures "the adapter approach as built" more than E18/E19 specifically.

### Finding 5: two corrections to our own yardstick

1. **The noise floor depends on the kind of change.** The per-window spread of the deltas was **24.3** for the raw adapter and **39.6** for V3, not the 14.9 measured from small anchor tweaks. An adapter changes the drafted squad far more. E17's "+2.68σ" and E18's "+2.55σ" were overstated by about 1.6×. F6 is unaffected, because it is a small anchor change for which 14.9 applies.
2. **Windows are cheap for anchor-only tests.** A classic backtest costs ~30 seconds of CPU; 54 of them ran in 90 seconds of wall time. The "we can't afford 34 windows" argument behind the stopping rule applies only to GPU-decoded adapters. An anchor change can be judged on ~30 windows across 2022-26 in minutes.

### The recommendation given (29 September)

- **Keep the LLM, change its job.** For GW6, decisions come from classic + F6, the only component with solid decision evidence. This is the shadow-mode fallback your own rule allows when the LLM fails its gate, not dropping the LLM.
- Keep decoding the adapter weekly (~12 GPU minutes, needs your OK) and log it in the two-model ledger, with a **pre-set promotion rule**: if its availability read beats classic's by ≥0.03 AUC among likely starters over a rolling four weeks, switch availability routing on. Given E19, that is most likely in the congested winter and the run-in.
- **Go harder on measurement, not training, for the LLM.** No adapter GPU runs until the availability edge shows up live or a new idea passes the 21-window bench. If it does show up, the run worth funding is an **availability-first adapter** trained on this season's data, since new signings and role changes are exactly where it should shine.
- **Go harder on the classic path, cheaply.** Build a ~30-window bench; re-test F10/F11 properly; try one bigger swing, a gradient-boosted model, because F6 was a missing interaction and that model class finds interactions by itself.

*(Section 3.10 revises this. The promotion rule should compare the adapter with a proper appearance classifier, not minutes ÷ 90. The data defects should be fixed before the bench is built. Expectation decoding replaces the availability-first adapter as the first GPU experiment.)*

### The Cunha → Haaland question, answered with the GW6 frame

You first asked on 4 September. The answer then was "switch once Haaland out-ranks Bruno two weeks running." **That trigger has now fired on the classic model**: GW5 25.4 vs 24.5 over five weeks, GW6 (classic+F6) 28.7 vs 25.9. The adapter blend hid it at GW5 by cutting Haaland 6 points, which is the shrink defect in action. But:

- **Cunha → Haaland is illegal** (midfielder vs forward), and Cunha can't fund him. An exhaustive search of 1–3 transfer routes from your squad (bank £0.3m, exact selling prices) finds one 2-transfer route: **Bruno + Isak → Haaland + a ~£5.1m midfielder** (Belloumi or Janelt). It is worth +0.9 over GW6-10 with a −4 hit in GW6, or **+4.0 if the free transfer is rolled and the move is made free in GW7**, when City host Ipswich.
- **The model's best single move isn't Haaland: Bijol → De Cuyper (+6.8, free).** Bijol has 164 minutes all season; De Cuyper has the best underlying numbers of any defender (0.47 xGI/90), though his 4 goal involvements run ahead of them.
- The margins are small. The stronger reasons for Haaland are captaincy and that 74% of managers own him, so not having him is a big variance bet against the average.
- *Added 3 October:* these numbers come from the live frame, which feeds ownership as a percentage to a model trained on counts (Section 3.10, defect C). That depresses heavily-owned players: by simulation, Haaland's five-week forecast is ~35 rather than ~29, against ~29 rather than ~26 for Bruno. Correcting it widens Haaland's lead and probably makes the Bruno + Isak route more clearly positive, but every player's forecast moves, so re-cost the routes after the units fix rather than trusting this estimate.


## 3.10 Era 9 (3 October 2026): what writing this document uncovered

Reading every file line by line to describe the algorithms exactly (Part II) turned up findings that change the conclusions of Era 8. Each was verified with a CPU check before being written down. This section reports them plainly, because several revise claims made earlier in this document and in the project's memory.

### Finding 6: the adapter is a *median* estimator, and that is the "shrink"

On E19's training set, the 1GW residual label has **mean −0.029 but median −0.300**. FPL residuals are right-skewed: most weeks a player slightly under-performs his expected value, and occasional hauls pull the mean back to zero. The adapter's outputs track the **median**, not the mean:

| E19 eval rows, by classic-forecast quintile | label mean | label median | adapter mean output |
|---|---|---|---|
| lowest (0.95–2.12) | −0.079 | −0.300 | −0.356 |
| 2nd | −0.044 | −0.400 | −0.358 |
| 3rd | −0.002 | −0.300 | −0.383 |
| 4th | −0.077 | −0.400 | −0.523 |
| highest (3.56–8.09) | −0.133 | −0.600 | −0.827 |

**Why it happens:** the adapter is trained with cross-entropy on number tokens and decoded greedily. Greedy decoding returns (approximately) the *most likely* value of the model's predictive distribution, its mode, not its expected value. For a right-skewed outcome the mode sits below the mean, and the gap grows with the size of the forecast.

**What it explains:**

- MAE improves (MAE is minimized by the median) while RMSE gets worse (minimized by the mean). That is exactly E19's evaluation: 1GW MAE 2.27 → 2.14, RMSE 3.04 → 3.06.
- The delta correlates −0.65 to −0.71 with the baseline, for the same reason: the median-to-mean gap grows with the forecast.
- Premiums are cut hardest, because the biggest forecasts have the biggest gap. That is the "Haaland cut like a mirage" problem of GW2 and GW5.
- The shrink is decision-neutral to harmful. Expected-points decisions need means, and captaincy needs the right tail. A mode-seeking forecaster systematically under-rates exactly the players the optimizer should pick.

Every "unconditional shrink" observation since E1 in July is this one mechanism. It also suggests a fix that needs **no retraining**: decode the *expectation* instead of the mode. Sample several completions and average them, or compute the expected value from the token probabilities. That is a decode-time change, testable on E19's existing holdout.

### Finding 7: a plain logistic classifier beats the LLM at the LLM's best job

The classic "P(appear)" is predicted minutes ÷ 90 (§2.3), a crude stand-in. So the LLM's availability advantage (Finding 2) was measured against a strawman. A logistic regression on the anchor's own 76 features, trained on the same cutoffs, gives:

| AUC among likely starters (higher is better) | classic minutes/90 | logistic | LLM | logistic + LLM |
|---|---|---|---|---|
| E19 holdout, late 2025-26 (n = 2,489) | 0.547 | **0.744** | 0.717 | **0.752** |
| Live 2026-27 GW2-5 (n = 881) | 0.673 | **0.699** | 0.673 | **0.716** |

| Brier score among likely starters (lower is better) | classic | logistic | LLM |
|---|---|---|---|
| E19 holdout | 0.142 | **0.086** | 0.106 |
| Live 2026-27 GW2-5 | 0.094 | **0.075** | 0.079 |

**Reading:**

- Most of the LLM's apparent availability edge was the weakness of the baseline it was compared with. A proper classifier, a few minutes of CPU, beats the LLM alone on both sets.
- The LLM still carries **some information the classifier lacks**: combining the two (a simple rank average) adds +0.008 AUC on E19 and **+0.017 live**.
- That small complementary signal is now the most precise statement available of what the fine-tuned LLM contributes.

### Finding 8: four data defects in the foundation

**A. Historical "pre-deadline" status and news are end-of-season snapshots.** For every historical season, the status and news fields come from the end-of-season `players_raw.csv` and are copied onto every week. Across 2019-20 to 2025-26, **not one player has more than one status value in a season.** In 2024-25 Emiliano Martínez is "suspended" for all 38 weeks (3,195 minutes played), Gravenberch "suspended" (3,160), and Saliba "injured" (3,039). Only the live 2026-27 data has real week-by-week values (202 of 667 players change status).

- This *corrects* Section 1.4 and the E10 card. The "real historical values" adopted for 2025-26 in August were this snapshot, not pre-deadline history. Before that, the official backfill had blanked them.
- **What it contaminates:**
  - the anchor's status and news flags (learned on leaky, noisy labels, then applied live to real flags);
  - the "Status / Official news" lines in 13.8% of E19's training prompts (e.g. a GW2 prompt telling the adapter Saliba has "Hamstring injury — Expected back 01 Jun" in a week he played 90 minutes);
  - the F7 depth-chart features.
- **It may also explain part of the late-season availability edge.** An end-of-season snapshot is closest in time to the run-in, so it is most "accurate", and most leaky, in exactly E19's GW27-38 window. The live season, with genuinely pre-deadline status, shows no LLM edge over classic at all.

**B. A player's club is his end-of-season club.** Players who moved mid-season carry their old club's matches into their new club's team-form table. 24–36% of team-weeks in 2022-26 have a contaminated `team_goals_for_avg_3`. For example, Manchester City's first eight weekly goal totals in 2025-26 are recorded as 6, 2, 5, 5, 3, 9, 5, 8; the real figures are 4, 0, 1, 3, 1, 5, 1, 2. This corrupts every team and opponent feature, **including F6's opponent-weakness inputs**, plus the fixture-outlook, congestion and depth-chart prompt blocks. F6 still won +112 with noisy inputs; with clean inputs it might win more. That is untested, and probably the highest-value fix on this list.

**C. Ownership is a manager count in training and a percentage live.** The training table stores vaastav's `selected` (a count, median ~20,000, max 9.5 million) under the name `selected_by_percent`. The live frame fills the same feature with the API's percentage (0–100). So the live anchor sees every player as almost unowned, and the change-in-ownership feature as wildly negative. A simulation on GW5 rows: Haaland 1GW 7.63 → 6.63 and 5GW 35.3 → 28.9; João Pedro 5GW 27.3 → 21.1; B. Fernandes 5GW 28.9 → 25.6. **Every live sheet this season has under-forecast highly-owned players.** Backtests are unaffected, because they use counts consistently. (It is also why E13a's market line read "owned by 6171553.0% of managers.")

**D. The F2b prior-season blend never reached the live walk-forward features.** The synthetic next-week rows are built from the live season alone, so there is no prior season to blend with. Live output is identical with the flag on or off. The anchor was *fitted* on blended features but *fed* unblended ones in GW3–GW5, a train/live mismatch that fades as players pass six appearances.

Several smaller defects were also recorded (Part II §2.12): the backtest's label overlap, all-or-nothing autosubs, the chip program's future-week inflation, surname collisions in evidence matching ("Michael Keane" collecting a Robbie Keane passage), first-publication timestamps on later-fetched live blogs, and the non-standard chat template.

### What this changes

1. **The availability story is weaker than Era 8 stated.** The LLM's late-season edge is partly a weak baseline (Finding 7) and possibly partly a leak (defect A). What survives is a small, live, complementary signal.
2. **The "shrink" has a mechanism and a cheap test.** Expectation decoding (Finding 6) is the first adapter experiment in months aimed at a *diagnosed* defect rather than a new input.
3. **Every anchor verdict was measured on contaminated team and status features.** That includes F6, F7, F12 and the 21-window bench. The comparisons stay internally fair, since both arms share the defects, but magnitudes may move after the fixes.
4. **The live forecasts have been biased against popular players all season** (defect C), and missing F2b for early-season form (defect D). This likely contributed to the GW2 "Haaland 43rd" problem alongside the causes found at the time. It also means the GW6 frame understates Haaland more than Bruno (35 vs 29 rather than 28.7 vs 25.9 over five weeks, by the simulation), which strengthens the case for the Haaland move.


---

# Part IV — The ledger

## 4.1 Every experiment, in one table

Verdict vocabulary: **WIN** = cleared its pre-stated bar on the shipping metric; **ADOPTED** = shipped into the pipeline; **NULL** = no measurable effect; **NEGATIVE** = measurably worse; **UNRESOLVED** = an effect smaller than the instrument can resolve; **FLAT** = no gain on the target metric.

### Pre-E4B (31B, April – July 3)

| ID | Question / change | Key result | Verdict |
|---|---|---|---|
| squad / transfer SFT | Can the LLM choose actions directly? | Format improved; decisions invalid or suboptimal | Abandoned → "LLM feeds an optimizer" |
| direct forecast top-96 | Absolute per-player forecasts | Strict JSON 0 → 1,920/1,920; 1GW MAE 2.67 → 2.37 but RMSE 3.44 → 3.90; 3/5GW worse | Format ✓, prediction ✗ (learned to shrink) |
| residual pilot GW1-10→11 | Deltas vs classic | 3GW RMSE 6.53 vs 6.90; 5GW 8.55 vs 9.85; 1GW 3.42 vs 3.35 | Promising |
| residual GW1-25→26 | Same, more data | 1/3/5GW RMSE 3.71 / 7.69 / 11.60 vs 3.31 / 6.25 / 8.58 | Blew up → clipping mandatory |
| listwise reranking | Rank top 5 of 12 | Value 73.4 (best ckpt) vs 79.9; top-1 0.18 vs 0.30 | NEGATIVE |
| anchored reranking | ≤2 swaps of classic top 5 | 72.9 vs 76.7; top-1 0.125 vs 0.305 | NEGATIVE → pivot to E4B |

### The E4B forecast ladder and gates (July – September)

| ID | Change vs predecessor | Key result | Verdict |
|---|---|---|---|
| E0 | Base E4B, no tuning | Zero deltas; 68% strict JSON | Control |
| E1 | Structured prompt only | 1GW MAE 2.435 vs 2.575; Spearman 0.150 vs 0.165 | Error ✓ rank ✗ |
| E2 | + 2 articles × 260 chars | Top-11 +1.53/wk (t 0.77); usage flat | NULL-ish |
| E3a | Articles × 450 chars | ≈ E2; usage flat | NULL → articles dropped |
| Gate 1 | E3a in backtest | 1,000 vs 1,058 | FAIL |
| E4 | Top-256 pool, fixture outlook | Appear MAE 0.161; gate 1,020 | FAIL |
| E5 | + congestion block | ≈ E4 | NULL |
| E6 | + base anatomy (provenance, decomposition, role) | Top-11 +2.95/wk (t 2.41); gate 1,035, avail_soft 1,058 | Tie (best so far) |
| E7 | + scout evidence (84% coverage) | Gate **1,069** (+11) | **WIN (first)** |
| E7-chrono-2425 | Same recipe, 2024-25 window | **1,314 vs 1,261 (+53)** | **WIN (2/2)** |
| E8 | + podcast transcripts | 1,025 / 1,002 / 1,060 | NEGATIVE |
| E9 | Train on prior seasons only; eval 2025-26 GW2-30 | **1,553 vs 1,471 (+82)**; avail_soft 1,549 | **WIN → ship candidate** |
| E9 DefCon slice | Can text teach an unseen scoring rule? | Bonus weeks: SFT 2.892 vs classic 2.593 | Failed (−0.30) |
| E10 | Ship model, thru 2025-26 GW34 | Sanity 270 vs 268 | ADOPTED (GW1) |
| E11 | Rate labels + DefCon line | 1GW MAE 2.060 vs 2.211; DefCon slice −0.390 | Best adapter; drag accepted |
| E11-full | E11 thru GW38 | Smoke 48/48 strict | ADOPTED (GW2+) |
| E12 | Haiku digests for list articles | 2.068 vs 2.060 | FLAT |
| E13a | + market line (price, ownership) | 2.059 vs 2.060; premium slice 3.49 vs 3.45 | FLAT |
| E14 | 3 docs × 700 chars | 2.062 | NULL |
| E15 | + analysis-first selection, multi-window | **Best MAE 2.059 / 4.864 / 7.797**; decisions 264 vs 277 (E11) vs 267 | NEGATIVE (no ship) |
| E17 | F6 + depth/opponent blocks + v17 provenance | Decisions 300 vs 260 (E11) vs 270 (classic+F6); mechanism partials ≈ 0 | Split: F6 yes, adapter no |
| E18 | F6 + original v1 prompts | 308 vs E17's 300; MAE 2.0932 vs 2.0935 | v17 blocks dropped |
| E19 | Train thru GW26; 3 holdout windows | **−38, −22, +69 = +9 (0.35σ)** | Adapter UNRESOLVED |

### Reinforcement learning (decision layer and forecast layer)

| ID | Change | Key result | Verdict |
|---|---|---|---|
| G1 | Weekly bandit over decision knobs, paired reward | +7 held-out (7W/5L/7T); tie trap | Marginal |
| G2-v2 | K-week plans, deployment-regime states | +47 classic / +27 adjusted (6/6) — inflated by chip-replay bug | Edge real but overstated |
| G2-v2b | Init from E7 merged | +28 adjusted / +3 classic (canned TC) | Worse generalization |
| G2-v2 corrected | Season-aware chips, same adapter | +23 / +20 | Baseline for v3 |
| G2-v3 | Chip-budget curriculum (half-aware) | +23 / +20 | FLAT (frozen for GW1) |
| G3 | transfer_pick + 4× augmentation | +8 / +21 | FLAT |
| G3b | + third epoch, untruncated completions | +10 / +15 | FLAT → G-track closed |
| G4 | GRPO on forecasts, per-player marginal decision reward | 487 vs E11 480 vs classic 491; 2W/5T/2L | FAIL (reward mis-specified) |

### Classic anchor and decision-layer changes (CPU)

| ID | Change | Key result | Verdict |
|---|---|---|---|
| decision knobs | horizon5 / 2 transfers / avail_soft, 3 windows | Worse / worse / −27, +9, +11 | Rejected; ≥3-window rule born |
| LLM avail × avail_soft | Interaction | 1,056 vs 1,031 (+25) | Real but ties classic |
| lookahead-2 | Banking via 2-week valuation | Lost on 3 windows | Rejected |
| oracle test | Perfect information | Banking value exactly 0; +738/season headroom | CLOSED permanently |
| rate-normalized labels | Fix season-end truncation | corr(PPG, 5GW/5) 0.20 → 0.40 | ADOPTED |
| walk-forward live frame | Fix week-2 cold start | P(app) p90 0.13 → normal | ADOPTED |
| F1 | Premium-rank alarm | — | ADOPTED (monitor) |
| F2 | Band calibration (old sign) | 987 vs 1,007 (−20) | Rejected |
| F3 | Captaincy leverage in draft / transfers | 1,007 vs 1,007 | No effect |
| F2b | Prior-season quality blend | +22, +32, −3 = **+51** (3 × 7 weeks) | **ADOPTED** |
| F2c | Prior-season team blend | +8, −13, −6 = −11 | Rejected |
| 8GW head | Longer horizon | Rank corr 0.419 vs 0.417 | NULL |
| DefCon features | Threshold hit rates | Bonus-week MAE 2.496 → 2.494 | NULL |
| DefCon guard | Shrink negative deltas for high hit rates | Net negative, all 6 variants | Rejected |
| F5 | Clean-sheet features | 407/440/365 vs 411/440/406 (−45) | Rejected |
| alpha sweep | Ridge regularization 1 / 10 / 50 | 1,257 / 1,255 / 1,239 | NULL |
| **F6** | **Opponent-weakness interactions** | **MAE −0.0339 (4/4); +112 over 5 windows (+3.35σ)** | **ADOPTED (largest win)** |
| status backfill | Restore live injury flags | Flagged rate 0 → 0.14 | ADOPTED |
| F7 | Depth-chart features | +0.0107 MAE, lost 4/4 | NEGATIVE |
| F8 | Finishing-luck features | −0.0003 MAE, wrong-sign coefficients | NULL |
| F9 | Congestion / European features | Premium gap −1.129 → −1.110; causal claim falsified | NULL |
| band calibration (correct sign) | Fix premium over-forecast | 628→620, 486→472 (−22, −1.04σ) | Not actionable |
| F10 | Hot vs due (rank form) | +3 over 5 windows (0.09σ) | UNRESOLVED |
| F11 | Decision-weighted loss | +25 over 5 windows (0.75σ); proxy said +7.6/wk | UNRESOLVED; E20 cancelled |
| F12 | Team-attack interaction | −42 over 5 windows (−1.26σ) | UNRESOLVED (negative lean) |

### Evidence pipeline (data, not model, changes)

| ID | Change | Key result | Verdict |
|---|---|---|---|
| mention-centered windows | Centre truncation on the player's first mention | Title-only docs 0%; podcast content actually reached | ADOPTED |
| attach merge gate | Coverage must not drop | Caught E8 corpus collapse (26,987 → 8,785 rows) | ADOPTED (gate) |
| audit tool | Track coverage / window size / title-only | 84.3% coverage, ~2% of article shown | ADOPTED (standing metric) |
| Haiku vs Gemma extraction | Precision vs recall | Haiku 0 hallucinations; Gemma wrong facts | Haiku chosen |
| team-context regex | Attach team analysis to players | 4 distinct failure modes | Parked → digests' team_notes |

### Post-E19 analysis (29 September)

| ID | Question | Result | Reading |
|---|---|---|---|
| shrink decomposition | How much of the gain is calibration? | Shrink = 91% of MAE gain; decision −1 over 3 windows | Accuracy gain is decision-neutral |
| availability AUC | Where is the real signal? | +0.17 late 2025-26; +0.01 to +0.04 elsewhere; **0.000 live** | Phase-dependent |
| V3 availability routing | Feed availability into points | +52 (3/3) on E19; +113 over 18 replication windows (9W/8L) | UNRESOLVED (positive lean) |
| raw adapter, 21 windows | Is the deployed approach worth anything? | **+39 total** | ≈ zero |

### Checks run while writing this document (3 October)

| ID | Question | Result | Reading |
|---|---|---|---|
| median check | Why does the adapter shrink? | Labels: mean −0.03, median −0.30; adapter output mean −0.49, tracking the label median by quintile | Greedy decoding returns the mode; it is a median-seeker |
| logistic appearance model | Is the LLM's availability edge real? | Likely starters, E19: classic 0.547 / logistic **0.744** / LLM 0.717 / both 0.752. Live: 0.673 / **0.699** / 0.673 / 0.716 | Mostly a weak baseline; small complementary signal (+0.017 live) |
| status audit | Are historical "pre-deadline" fields real? | 0 players with >1 status per historical season | End-of-season snapshots: leaky |
| club audit | Are team-form features clean? | 24–36% of team-weeks contaminated by mid-season movers | Defect B |
| ownership audit | Same units in training and live? | Counts in training, percentages live; Haaland 5GW 35.3 → 28.9 by simulation | Defect C (live only) |
| live F2b audit | Does the prior blend reach live features? | Identical output with the flag on and off | Defect D (live only) |

## 4.2 The pattern, counted

| category | attempts | paid |
|---|---|---|
| **Input or capacity scale-ups** — more or different text (E2/E3a, E8, E12, E14, E15), more context blocks (E5, E17), market line (E13a), longer horizon (8GW), more RL agency / data / epochs (G2-v3 curriculum, G3, G3b), RL scale-up on forecasts (G4) | ~14 | **0** |
| **Diagnosed defect fixes** — residual + clipping, rate-normalized labels, walk-forward frame, F2b, F6, status backfill, bench-order output, mention-centered windows, settled-data gate, evidence gates | ~10 | **almost all** |
| **Anchor features on intuition alone** — F5, F7, F8, F9, F10, F11, F12, band calibration, F2c, DefCon features | 10 | **0** |

The asymmetry is the most important empirical fact in this document. Every large gain began with someone pointing at a specific player and saying "that's wrong," followed by a measurement that found the general defect behind the anecdote. No gain came from adding more of something.

## 4.3 The live season, decision by decision

| GW | Decision | Whose | Outcome |
|---|---|---|---|
| 1 | Bench order unspecified (Mitchell before Bijol) | system defect | −9 (38 instead of 47) → bench order now an output |
| 1 | Captain Bruno | model | 2 raw points |
| 2 | Watkins → João Pedro (contract standoff + 0 minutes in the evidence) | model + evidence | JP captained for 9 |
| 2 | Keep Bruno (no panic sell) | you | Bruno 23 |
| 3 | O. Dango → Cherki | model | Cherki 3; attack blanked; Mitchell 15 on the bench (no trigger) |
| 4 | Richarlison → Isak (left the league) | model | 61 vs 69 |
| 4 | Mid-week "three defenders blanked" post-mortem | my error | Invalid (Leeds hadn't played) → `gw_status.py` |
| 5 | Shaw → Konsa; Konsa P(app) override to ~0.93 | me | Override right (played 90); points wrong (Konsa 1 vs Mitchell 7, −6) |
| 5 | Start Cunha, bench Evanilson (Liverpool's defence) | **you** | **+8** (Cunha 10, Evanilson 2) |
| 5 | Bench order: Evanilson ahead of Mitchell | me | −5 (JP didn't play; Mitchell would have scored 7) |
| 5 | Captain Saka over Bruno | me | Neutral (both 2) |


---

# Part V — What worked, what didn't, and what is still open

Each item carries an honest **strength-of-evidence** label: *strong* (replicated, or ≥3σ), *moderate* (a clear single result with a mechanism), *weak* (one window or a proxy), or *by construction* (a correctness fix that needs no backtest).

## 5.1 What worked

**1. Decomposing the problem: the optimizer owns legality, the model owns forecasts.** *(Strong.)* Every attempt to have the LLM choose actions directly (squads, transfers, rankings) failed in the spring. Once the LLM's output was restricted to per-player numbers and an exact optimizer handled budget, positions, club limits, hits and chips, invalid decisions disappeared by construction. The decision layer has not produced an illegal recommendation since.

**2. The residual parametrization: bounded, shrunk, clipped deltas.** *(Strong for stability and accuracy; see 5.3 for decisions.)* Training the LLM to output corrections relative to a classic forecast (Δpoints within ±2/±4/±6, Δminutes within ±20, ΔP(appear) within ±0.25, labels multiplied by 0.35 then clipped) turned an unstable task into a stable one. Every E-run converged, every adapter beats classic on MAE, and none has ever "blown up" the way the unbounded residual pilot did at GW26. The same design choice also explains its main limitation: a bounded, shrunk target rewards small, conservative corrections, so most of what the model learns is to shrink.

**3. Completion-only SFT and strict JSON.** *(By construction.)* Format is a solved problem: 100% strict JSON on every evaluation since E1, against 68–76% for the base model. The masking audit pinned completion-only loss with a unit test.

**4. A small model over a big one.** *(Strong.)* Gemma-4-E4B learned everything the 31B model learned, at roughly a tenth of the cost per step, and allowed 21 forecast-adapter training runs plus 8 RL runs between July and September. The 31B model lost to ridge regression on every framing tried. Model scale was never the binding constraint; label noise and the objective were.

**5. The classic anchor, refit weekly.** *(Strong.)* A ridge suite with ~70–76 features, refit on strictly prior data every week in seconds, has been the foundation of every result. It provides the stable numeric prior the LLM corrects and is the reason a walk-forward backtest is possible at all.

**6. Diagnosed fixes to the anchor and labels.** *(Strong.)*
- **F6 opponent interaction:** +112 decision points over 5 windows (+3.35σ), MAE better in 4 of 4 windows. The largest measured win in the project.
- **F2b prior-season blend:** +51 over three early-season windows; fixes cold start without fabricating pedigree for players with no history.
- **Rate-normalized labels:** restored the 5GW head's correlation with reality (0.20 → 0.40) and put elite defenders back in the draft.

**7. Scout evidence, in the right genre.** *(Moderate.)* E7's first gate win (+11) and its chronological replication (+53 on 2024-25) are the clearest sign that *FPL-analysis text* helps where general news did not. The effect is small relative to noise, but it replicated.

**8. The clean-split methodology (E9).** *(Moderate to strong.)* Training only on complete prior seasons and testing on all of the next one matches the real deployment condition and gave the largest held-out test of its time (7,424 rows, +82 over 29 weeks). It is now the template for any ship candidate.

**9. Gates, chains and process scripts.** *(By construction, repeatedly validated.)* Sanity gates stopped three runs that would have trained on broken data (E8's coverage collapse, E17's missing opponent block, the live status gap). The settled-data gate ended mid-week narration. Chains on disk kept the GPU busy across session gaps. The bench-order output, the eyeball gate, the status backfill, the single-instance decode guard and the read-only freeze each exist because of a specific incident, and each has prevented its incident from recurring.

**10. Human judgment, used as a signal.** *(Strong as a discovery method.)* Your single-player objections found the three biggest defects of the season: Haaland 43rd led to F2b; Konsa below his own backups led to the status and depth-chart work; Evanilson unpunished against Liverpool led to F6. Your Cunha-for-Evanilson call was the best decision of GW5. The weekly case-study ritual (rank our misses, investigate 3–5 by hand) has found more than every systematic sweep combined.

**11. Evidence engineering for precision.** *(Moderate.)* Mention-centered windows ended the "title only" failure mode, Haiku digests turned list articles into clean structured facts, and the audit tool made evidence quality a tracked metric. These made the evidence *correct*, even though more correct evidence did not translate into better decisions (E12–E15).

**12. Measuring the instrument.** *(Strong.)* The noise floor, the mechanism check, E19's three-window holdout and the 21-window replication bench changed what the project believes. Without them, E18's false positive would be the deployed belief today.

## 5.2 What didn't work

**1. Letting the LLM override freely.** Free reranking, unbounded residuals, direct action choice and unanchored all-player outputs all failed. Realized FPL points are too noisy for a model to learn unconstrained overrides from.

**2. Scale for its own sake.** 31B over 4B bought nothing. More epochs (G3b), more data per row (wider windows), more rows of RL augmentation (G3) and longer horizons (8GW) all came back flat.

**3. More text, for decisions.** Article packets (E2/E3a), podcast transcripts (E8, actively harmful), digests (E12), wider windows (E14) and better selection (E15) improved accuracy or made evidence more correct, but never improved decisions. The structured status/news line already carries most of the availability signal that text offers, and the rest is either noise or isn't consumed by the decision layer.

**4. More context blocks.** Congestion (E5), the market line (E13a), and the depth-chart and opponent-record blocks (E17) were all ignored by the adapter. The mechanism check proved E17's blocks had zero partial correlation with its outputs.

**5. Reinforcement learning, so far.** G1 was marginal and fell into the tie trap; G2's edge was mostly chip timing and was inflated by a bug; G2-v3, G3 and G3b were flat; G4 optimized a proxy reward that inverted the sign of the real objective. The one durable RL lesson is about evaluation design, not policy capability.

**6. Fixing DefCon through the adapter.** Classic features were collinear, prompt surfacing failed across three adapters, and an inference guard was net-negative. The drag (−0.39 MAE on ~11% of rows) was accepted.

**7. Anchor features on intuition.** Clean sheets (F5), depth chart (F7), finishing luck (F8), congestion (F9), hot-vs-due (F10), decision weighting (F11) and team attack (F12): none cleared the bar. Several had a sound intuition that a linear feature cannot express (F7, F8) or a causal premise that a two-minute check would have falsified (F9).

**8. Calibration corrections.** Band calibration, in both its old and its correctly-signed form, made forecasts more honest and squads no better or worse. Calibration and ranking are different problems.

**9. Planning depth.** Two-week lookahead lost on three windows, and the oracle test proved banking has zero structural value at one transfer per week.

**10. Proxies.** The top-11 proxy overstated F11 roughly 30×, and G4's evaluation proxy inverted the sign of the adapter's true value. Both were caught only by running the real backtest.

**11. Comparing the LLM against a strawman.** For two months the LLM's best claim, availability, was measured against the classic model's predicted-minutes ÷ 90, which is not a probability model. Against a proper logistic classifier, most of the claim disappears.

## 5.3 What is still open

| question | current best answer | what would settle it |
|---|---|---|
| Does the adapter improve decisions? | ≈ 0 (+39 over 21 windows; roughly −2.4 to +3.3 points per gameweek) | More F6-matched holdout windows; or a live ledger kept long enough |
| Does routing the adapter's availability read into points help? | Unresolved, positive lean (+165 over 21 windows, 12 won), but the baseline it beat was minutes ÷ 90 | Repeat with a proper logistic P(appear) as the base, with and without the LLM, on the bench and live |
| Does the LLM know who plays better than the best simple model? | Only slightly: logistic alone 0.744 / 0.699 vs logistic + LLM 0.752 / 0.716 AUC (E19 / live, likely starters) | Weekly live tracking of the *incremental* AUC over the logistic model |
| Is the adapter's "shrink" a decoding artifact? | Very likely: it tracks the label median, not the mean | **Expectation decoding** (average of samples, or expected value from token probabilities) on E19's holdout: does decision value move? |
| How much do the data defects matter? | Unknown: end-of-season status, end-of-season clubs, live ownership units, live F2b | Fix them, rebuild the tables, re-run F6 and the classic baselines |
| Is there another F6-sized anchor defect? | Probably not via linear features; maybe via model class | One gradient-boosted anchor test on a ~30-window bench |
| Would 12B help? | Untested; prior is skeptical (31B didn't) | Only as a paired retrain after an objective change |
| Would in-season incremental training help? | Approved 23 August, never run (the GPU went to E14–E19) | Run only once an availability-first objective exists to train |
| Can team-level news reach players? | Regex failed 4×; the digest `team_notes` route was designed but never run (E16) | Digest team-analysis articles → team notes → a separate prompt line |


---

# Part VI — The surprises

These are the findings that contradicted what we expected at the time. Each is written as *expected → found → why → what it means*, because the gap between expectation and finding is where the learning is.

### 1. A bigger model was worse, not better

- **Expected:** Gemma-31B would out-forecast a ridge regression, and certainly out-forecast a 4B model.
- **Found:** 31B lost to classic on every framing (direct forecasts, residuals, free ranking, anchored ranking). E4B then matched or beat everything 31B had done, at a tenth of the cost.
- **Why:** the task is calibration and extraction over noisy labels, not reasoning. Capacity was never the bottleneck (training loss sat near 0.14–0.18 for every run); label noise was.
- **Means:** for narrow, noisy prediction tasks, spend on iteration speed and data quality, not parameters.

### 2. The base model contributes nothing; fine-tuning owns every effect

- **Expected:** a pre-trained model with football knowledge would bring useful priors.
- **Found:** un-tuned E4B outputs deltas of essentially zero and fails strict JSON a third of the time.
- **Means:** whatever the adapter does, it learned from our data. That makes the null decision result a statement about what *our training signal* can teach, not about the model's world knowledge.

### 3. Format is learned in hours; forecasting skill may never arrive

- **Expected:** formatting would be a nuisance and prediction the real work.
- **Found:** strict JSON went from 0% to 100% in the first spring pilot and has stayed there. Ranking skill above classic has never been reliably demonstrated.
- **Means:** a perfectly formatted, confident output is not evidence of skill. This is worth remembering for any LLM system that "looks right."

### 4. Most of what fine-tuning buys on accuracy is a uniform shrink

- **Expected:** the adapter's MAE gains came from reading news about specific players.
- **Found:** E1, with no text at all, already beat classic on MAE. On E19, a straight-line shrink fitted to the adapter's own outputs recovers 91% of its MAE gain and has zero decision value (−1 over three windows).
- **Why (understood only on 3 October):** the residual labels are right-skewed (mean −0.03, median −0.30). The adapter is trained with cross-entropy on number tokens and decoded greedily, so it returns roughly the most likely residual, which sits near the median and well below the mean. The gap grows with the forecast. The result looks like a proportional shrink, improves MAE (minimized by the median), worsens RMSE (minimized by the mean) and preserves rank order.
- **Means:** accuracy improvements must be decomposed before they are credited to the LLM's "understanding." Ask "would a one-line formula do the same?" Also ask which statistic your decoding returns: greedy decoding gives the mode, and decisions need the mean.

### 5. News articles didn't help, but FPL analysis did

- **Expected:** text is the LLM's comparative advantage, so more articles would mean more lift.
- **Found:** Guardian and PL article packets were null (E2/E3a); Scout analysis converted at the gate (E7, replicated on a second season).
- **Why:** the structured prompt already contained FPL's own status/news line ("knee injury, 75%"), which carries most of what match reports say about availability. Scout articles add *judgment* (captaincy, differentials, price moves) that the numbers don't contain.
- **Means:** text value depends on genre, not volume, and the strongest text signal may already be a structured field.

### 6. Better accuracy repeatedly produced worse decisions

- **Expected:** a more accurate forecaster picks better squads.
- **Found:** E3a (better calibrated, worse squad), E8 (better MAE, −44 vs E7), E15 (best MAE ever, lost the gate), premium band calibration (more honest, no better).
- **Why:** MAE averages over ~650 players, almost none of whom are picked. Decisions depend on the order at the very top, and the captain multiplier doubles errors there. Shrinkage and calibration improve the average and leave the top order unchanged, or perturb it.
- **Means:** the shipping metric must be decision value. MAE is a diagnostic only.

### 7. Planning depth is worth exactly zero; forecast quality is worth 738 points

- **Expected:** smarter transfer planning (banking for a better move next week) would add points.
- **Found:** with perfect information, banking a free transfer never helped at one transfer per week (identical totals on all three windows). Perfect forecasts versus ours: +738 points per season.
- **Means:** all the prize money is in ranking skill, captaincy and chips. This one test redirected the whole decision-layer program.

### 8. The model's own prompt told it not to do its job

- **Expected:** the provenance line ("the classic signal already prices in … this GW's fixture … adjust only for news, congestion and future fixtures") would focus the LLM on what the anchor can't see.
- **Found:** the anchor *couldn't* see the fixture either (coefficient +0.0041), and the adapter obeyed the instruction. Its correlation with opponent strength was −0.048 while its correlation with its own baseline was −0.708.
- **Means:** a prompt is a strong prior, not documentation. Any claim a prompt makes about the rest of the system must be verified, or it becomes a capability defect.

### 9. A feature present since day one contributed nothing for months

- **Expected:** opponent goals-conceded was in the feature set, so the model handled fixtures.
- **Found:** its weight was ~zero (and wrong-signed at the 5-week window). The model leaned on FPL's coarse 1–5 difficulty integer instead.
- **Why:** the effect is multiplicative (a 5-point forward loses more against a good defence than a 2-point defender does), and a linear model can't express that without an interaction term.
- **Means:** "the feature is there" is not "the model uses it." Measure the slope the model carries against the slope in reality. That comparison found F6, and it is valid for schedule-assigned signals.

### 10. The training data has never contained real pre-deadline injury information

- **Expected:** historical status/news fields were real pre-deadline values.
- **Found, in three stages:**
  1. In August, the official-API backfill turned out to neutralize them to "available, no news", so E1–E9 trained with the injury flag blank for 2025-26.
  2. The "real values" adopted for E10 onward turned out on 3 October to be **end-of-season snapshots copied onto every week**. Saliba is "injured" for all of 2024-25, a season in which he played 3,039 minutes.
  3. The live 2026-27 season was blank until our own archived snapshots were restored.
- **Means:** a field called "pre-deadline" is only pre-deadline if it varies week to week. Check per-season *variation*, not just presence. A well-intentioned anti-leakage measure can delete a feature, and a well-intentioned fix can replace it with a leak.

### 11. Week 2 of the live season would have collapsed every forecast

- **Expected:** a pipeline that worked in GW1 would work in GW2.
- **Found:** once GW1 was ingested, every player's "latest row" carried cold-start features, and P(appear) collapsed to ~0.1 for nailed starters.
- **Means:** some bugs cannot appear until the system has run once. The first live week validated a broken second week. Look at the numbers before spending compute.

### 12. A label definition kept the best defenders out of the squad

- **Expected:** five-week labels were straightforward forward sums.
- **Found:** near season end those sums shrink toward zero. About 13% of rows had artificially tiny labels, attenuating the 5-week head and hitting elite players hardest (Gabriel's 5-week rate was 0.54× his own 1-week rate).
- **Means:** check *who* a model excludes, not just its average error.

### 13. The premium bias flipped sign, was about minutes rather than scoring, and correcting it loses points

- **Expected (GW2):** classic under-predicts premiums.
- **Found (September, current anchor):** it *over*-predicts £9.5m+ players by 1.09 points per week, entirely in the 27% of weeks they don't play 60 minutes. When they play, the forecast is exact. Correcting it does not win points.
- **Why:** premiums still out-score cheaper players at the same forecast level, so shrinking them shifts money toward worse picks.
- **Means:** a real, significant (t = −3.49) defect can be not worth fixing. Ask "does fixing it change rank?" before "is it real?"

### 14. A proxy can invert the sign of what you care about

- **Expected:** a week-by-week decision proxy would track the real backtest.
- **Found:** the G4 proxy reset every week to the classic squad, so it measured one-week marginal moves from someone else's team. It said E11 lost to classic (231 vs 247) when the real accumulating backtest said E11 won (277 vs 267). G4 was trained on that proxy as its reward.
- **Means:** validate a proxy against the real metric on known cases *before* optimizing it, and especially before using it as an RL reward.

### 15. Every adapter verdict had been measured on the one window the adapter wins

- **Expected:** GW35-38 was a convenient, representative holdout.
- **Found:** E19's three windows gave −38, −22, +69, and the +69 was GW35-38. Every adapter from E10 onward had been judged there.
- **Means:** a fixed evaluation window can quietly select for whatever happens to work in it. Rotate windows, or use several.

### 16. The adapter was right when we thought it was broken

- **Expected (your suspicion):** the adapter cutting Arsenal defenders was a defect.
- **Found:** for Calafiori, it had read a 67th-minute substitution in a match report, pinned minutes and appearance deltas at their bounds, and was correct (his minutes went 80 → 90 → 66). It gave Gabriel and White small positive minutes deltas.
- **Means:** individual reads can be excellent even when aggregate decision value is ~zero. That is consistent with Finding 2 of Section 3.9: the adapter's value is in availability reads, which the decision layer barely consumes.

### 17. Your single-player objections beat every systematic sweep

- **Expected:** automated audits and feature sweeps would find the defects.
- **Found:** the attenuation audit produced one lead (F12) that failed; feature sweeps went 0 for 10; but "Haaland can't be 43rd", "Konsa is nailed now", "Liverpool's defence is good" each exposed a general defect.
- **Why:** aggregate metrics hid these errors because they were symmetric and cancelled out. A domain expert looking at the top of the distribution sees exactly where decisions are made.
- **Means:** the human-in-the-loop isn't a fallback for when the model fails. It is the most productive debugging tool the project has.

### 18. The LLM's edge appears when the numbers go blind

- **Expected:** if the LLM knows something about availability, it knows it all season.
- **Found:** +0.17 AUC among likely starters late in 2025-26, +0.01 to +0.04 in other backtests, and 0.000 live in GW2-5 of 2026-27.
- **Why (two candidate explanations, not yet separated):**
  1. Late-season rotation, dead rubbers and injury crises make recent-minutes statistics unreliable, which is exactly when pre-deadline team news matters.
  2. The historical "status/news" lines are end-of-season snapshots, which are most accurate (and most leaky) in exactly the late-season window.

  In addition, the baseline was a weak one (minutes ÷ 90): a logistic classifier reaches 0.744 on the same late-season rows.
- **Means:** the LLM's value may be seasonal and conditional, or partly an artifact. Clean status data and a proper baseline are needed to tell which.

### 19. GRPO can learn to say nothing, and greedy decoding finds it

- **Found:** the G2 policy emitted empty completions under greedy decoding on 4 of 6 windows, despite positive training rewards. When every completion in a group is empty, the advantage is zero, so the empty mode is never penalized.
- **Means:** check any GRPO-trained policy under the decoding regime you will deploy (`min_new_tokens` fixes it).

### 20. The pipeline bugs that would have silently corrupted training

A partial list of bugs that produced no error, only wrong data. Each was caught by a gate or by looking at the numbers:

- the attach script *replaced* evidence instead of merging, so coverage fell from 84% to 27%;
- prefix truncation meant podcast evidence showed only cold-open banter;
- club stored as a name in some seasons and a number in others, so there were zero opponent records;
- the Scout audit matched articles by title only, which paired them with last year's edition;
- the "nothing" sentinel required a trailing period, which leaked two-thirds of non-answers into prompts as evidence;
- `pgrep -f` matched the calling shell's own command line, so a chain "verified" itself and never armed (three times);
- old state caches carried `team_id = -1`, so augmentation produced 74 episodes instead of 236.

**Means:** in a pipeline this long, the default failure is silent. Gates that check *counts and distributions* at every stage are the only reliable defence.

### 21. The fine-tuned model is a median estimator, because of how we decode it

- **Expected:** a residual model trained on (shrunk) realized residuals would predict the expected residual, roughly zero on average for an unbiased anchor.
- **Found:** label mean −0.03, label median −0.30, adapter output mean −0.49. By forecast quintile, the adapter tracks the median, not the mean.
- **Why:** greedy decoding of a cross-entropy-trained numeric output returns approximately the mode of the predicted distribution. For right-skewed FPL residuals, the mode is below the mean, more so for bigger forecasts.
- **Means:** this single mechanism explains the "unconditional shrink" (corr −0.65 to −0.71 with the baseline), premiums being cut hardest, MAE improving while RMSE worsens, and the decision neutrality. **Decode the statistic you need.** For expected points that means the expectation, via sampling or the token distribution, not the argmax.

### 22. A plain logistic regression beats the fine-tuned LLM at the LLM's best job

- **Expected:** the LLM's clearest strength, predicting who plays, was beyond what the numbers could do.
- **Found:** the "numbers" it was compared with were predicted minutes ÷ 90, not a probability model. A logistic classifier on the anchor's own features scores 0.744 AUC among likely starters on E19's late-season rows (LLM 0.717) and 0.699 live (LLM 0.673). Combining both adds a little: 0.752 and 0.716.
- **Means:** before crediting a model with a capability, compare it against the **best simple model for that capability**, not against whatever happens to be in the pipeline.

### 23. A player's club was his end-of-season club

- **Expected:** team-form statistics (goals for and against) were clean.
- **Found:** mid-season movers carry their old club's matches into their new club's team table, contaminating 24–36% of team-weeks. Manchester City's first eight 2025-26 weekly goal totals read 6, 2, 5, 5, 3, 9, 5, 8 instead of 4, 0, 1, 3, 1, 5, 1, 2.
- **Means:** F6, the project's biggest win, was measured on noisy opponent statistics. That suggests the true value of opponent strength is larger than measured, and that fixing the data is the cheapest experiment with real upside.

### 24. The live model has been reading ownership in the wrong units all season

- **Found:** "selected by percent" is a count of managers in the training table and a percentage in the live snapshot. The live anchor therefore sees every player as almost unowned, with a huge drop in ownership, and under-forecasts popular players. By simulation, Haaland's five-week forecast falls from 35.3 to 28.9.
- **Means:** backtests cannot catch a defect that exists only in the live path. Live and backtest feature distributions need to be compared directly, column by column.


---

# Part VII — The lessons, as principles

These are the rules the project now runs on. Each one was paid for by a specific mistake, named in brackets.

## A. How to evaluate

1. **Ship on decision value, diagnose with MAE.** The metric that decides shipping is realized squad points from a walk-forward backtest that accumulates a squad over a window. MAE, calibration, Spearman and top-k lift explain *why* something works, never *whether* to ship it. *[E3a, E8, E15, band calibration]*
2. **Use at least three independent windows, and never only the same one.** Single-window totals carry ±35–40 points of noise for decision changes. A window reused for every verdict can quietly select for whatever wins in it. *[avail_soft's −27/+9/+11; E18's false positive on GW35-38]*
3. **Measure the noise floor for the kind of change you are testing.** About 15 points per 4-week window for small anchor tweaks; 24–40 for adapter comparisons. Report results in σ using the right floor, and call anything under ~2σ "unresolved," not "flat" or "wins." *[E17 and E18 sigmas overstated ~1.6×]*
4. **Pre-register the hypothesis, then replicate on independent data.** Write down the variant and the bar before running it; if it wins, re-run it on windows it has never seen. *[V3: 3/3 on E19, then 9W/8L on 18 fresh windows]*
5. **Require a mechanism.** An adapter change must measurably respond to the signal it was built around: the partial correlation of its delta with that signal, controlling for the baseline. **An outcome without a mechanism is a coincidence.** *[E17 won its backtest with both designed signals at ~zero]*
6. **Never promote a proxy to a verdict.** Proxies that ignore budget, formation, transfers or the bench overstate ranking gains, and a proxy that resets state can invert the sign. Validate any proxy against the real metric on known cases first. *[F11's 30× overstatement; G4's inverted reward]*
7. **Test the causal claim before building the feature.** If the story is "premiums miss games after European fixtures," check the start rate with and without a European game first. Two minutes of analysis can save a day of feature engineering. *[F9]*
8. **Decompose before crediting.** Split an accuracy gain into "what a one-line formula would do" (shrink, recalibration) and the remainder. Split a player's points into attacking (luck-testable against xG) and non-attacking (minutes, clean sheets, bonus) before calling anything luck. *[the 91% shrink; the Mitchell misses]*
9. **Ask whether a fix changes rank, not just whether a defect is real.** A real, significant calibration defect can be not worth fixing if correcting it doesn't reorder players. *[the premium-minutes defect]*
10. **Narrate only settled data.** No scoring, ledger entry, average comparison or post-mortem until every fixture is finished and bonus points are confirmed. The rule is a script now, because a note wasn't enough. *[GW2 and GW4]*

## B. How to build with an LLM in the loop

11. **The optimizer owns legality; the LLM owns judgment, expressed as bounded numbers.** Every free-form or unanchored LLM output in this project failed. *[the spring of 2026]*
12. **Residuals need bounds, and bounds shape behavior.** Bounded, shrunk deltas make training stable and also make "shrink everything a bit" the easiest thing to learn. Choose the label transform knowing it is also a prior on behavior. *[GW26 blow-up; the 91% shrink]*
13. **Divide the labor honestly.** The anchor owns arithmetic and anything expressible as a feature, such as fixture interactions and prior-season pedigree. The LLM owns what only text can tell you: a substitution in a match report, a manager's quote, a role change. Don't ask the LLM to fix what a feature can fix, and don't build a feature for what is really a judgment over text. *[F6 vs E17; F7]*
14. **A prompt is a prior, not documentation.** Every claim a prompt makes about the rest of the system must be true, or it switches a channel off. *[the provenance line and fixture blindness]*
15. **Check that the decision layer consumes the signal the model is best at.** The adapter's strongest signal (availability) was routed into a threshold penalty that ignored it, while its weakest-for-decisions output (the points shrink) got full weight. *[8 July and again 29 September]*
16. **Evidence precision beats recall.** A wrong fact is worse than no fact; noisy text actively hurts. *[E8 podcasts; Gemma extraction]*
17. **Structured data beats mining prose.** Before writing a parser, check whether the fact ships as a field. *[four regex team-context failures vs the status field]*
18. **Train/live parity is a correctness property.** Every prompt block, evidence taxonomy and anchor version must be identical between the adapter's training data and the live decode. That is why F6 waited for a matching adapter, and why the market line and broadened Scout pattern are behind default-off flags. *[E13a, E15, F6 sequencing]*
19. **Respect chronology at every layer.** An adapter never adjusts a week inside its own training window. Facts flow down at inference time; outcomes teach upward only. *[the two-model ledger]*

## C. How to run experiments on one GPU box

20. **Gate before spending GPU.** Assert row counts, evidence coverage and prompt-block presence before training; compare the baseline distribution to last week and spot-check premiums before decoding. *[E8, E17, GW2]*
21. **Chain stages on disk; verify by artifact, not process name.** Monitors inform; they never trigger. Make every script executable, launch detached jobs with `setsid nohup … < /dev/null & disown`, and never trust `pgrep -f` (it matches its own caller). *[E6's idle GPU, E7's permission failure, three self-match incidents]*
22. **Assume the box will die.** `save_steps=100`, `oom_score_adj 800` on trainers, never run inference alongside training, and re-arm chains after any reboot (check `uptime -s` against launch times). *[the July power cut; the September reboot]*
23. **One variable per run.** Change only the thing under test, so a null is informative and a win is attributable. When bundling is deliberate (G3), say so up front and accept the attribution cost.
24. **Do the CPU prototype first.** The ridge can carry most objective and feature ideas for free. Two GPU runs (E20 and a congestion adapter) were cancelled on cheap evidence. *[F11, F9]*

## D. How to work with a domain expert

25. **Treat single-player objections as the primary discovery tool.** Each one is a cheap, high-signal pointer to a defect the aggregate metrics are hiding. *[Haaland 43rd, Konsa, Evanilson]*
26. **Look at the evidence the model actually saw before arguing about whether it is wrong.** Sometimes the expert finds a defect; sometimes the model read something the expert didn't. *[Calafiori]*
27. **Score judgment calls honestly, on both sides.** The ledger records your calls and mine with outcomes. Your Cunha call was right; my Konsa and bench-order calls were wrong. That record is what makes the next judgment call better calibrated.
28. **Surface blanks and failures; never let them be silent.** Your rule for the extraction pilot generalizes: any stage that can return "nothing" must report how often it does, and on which cases.

## E. Added after writing this document (3 October)

29. **Decode the statistic you need.** Greedy decoding of a cross-entropy-trained numeric output returns the mode, which for skewed outcomes is not the mean. Expected-points decisions need the mean; captaincy needs the tail. *[The adapter's median-seeking "shrink"]*
30. **Compare a model against the best simple model for the same job, not the incumbent.** The LLM's availability edge was measured against predicted minutes ÷ 90; a logistic classifier erases most of it. *[Finding 7]*
31. **A "pre-deadline" field is only pre-deadline if it varies week to week.** Audit per-season variation of every field that claims to be a point-in-time snapshot. *[End-of-season status and clubs]*
32. **Diff live features against training features, column by column, every week.** Backtests share training's units and cannot see a live-only defect. *[Ownership counts vs percentages; F2b missing live]*
33. **Writing it all down is itself a debugging method.** Describing each algorithm exactly enough for someone else to rebuild it surfaced more defects in one day than the previous two weeks of experiments. Periodic full-pipeline audits deserve a place in the routine.


---

# Part VIII — Where to go from here

## 8.1 The deployment decision for GW6 (deadline 10 October, 10:00 UTC)

**Recommended:**

1. **First, two small live-path fixes (CPU, a few hours):**
   - **Ownership units.** Convert the live percentage to the count units the model was trained on (percentage × total managers / 100, using the API's player total), or rebuild the table in percentages. Defect C has under-forecast popular players in every sheet so far.
   - **The live F2b blend.** Pass the prior season into the walk-forward feature builder so early-season form is blended live as it is in training (defect D).
2. **Decisions from classic + F6** (+112 over 5 windows, the only component with solid decision evidence). The adapter runs in **shadow**: decoded weekly, logged in the two-model ledger, not driving the optimizer. This is the fallback in the 5 July plan, allowed by your load-bearing rule when the LLM fails its gate. It does not drop the LLM.
3. **Re-cost the Haaland routes** after the units fix. The fix raises Haaland's forecast more than Bruno's, so it strengthens the case found on 29 September.

The weekly runbook for GW6:

1. `scripts/run_weekly_ingest.sh 5` (done for GW5): settled gate → sync → status backfill → verification.
2. Build the GW6 frame with `FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1` on the F6 table, with the two fixes above. A side-effect-free script to start from is `reports/adapter_bench_2026_09_29/gw6_forecast.py`.
3. **Eyeball gate:** baseline distribution vs last week; spot-check three premiums. *New:* diff the live feature columns against the training table's units.
4. Sheet from classic+F6: transfers, XI, captain, explicit bench order.
5. *(Needs your OK for ~12 GPU minutes.)* Decode the adapter for the shadow ledger, using E18 for F6 parity and `FPL_LIVE_INCLUDE_MARKET=0`, since E18 was trained without the market line.

**The promotion rule, set in advance:** compare the adapter's availability read with a **proper logistic appearance model**, not minutes ÷ 90. Promote availability routing only if *adding* the adapter to the logistic model improves live AUC among likely starters by ≥ 0.03 over a rolling four weeks *and* a pre-registered routing variant wins on the bench.

## 8.2 Fix the foundation first

The project's most reliable lesson is that diagnosed defects pay and scale-ups don't. The defects found on 3 October are diagnosed defects. In order:

| # | fix | why first | re-measure afterwards |
|---|---|---|---|
| 1 | **Clubs per fixture, not per season** (defect B): take each fixture's team from merged_gw's own club column, mapped through that season's teams file | Corrupts every team and opponent feature, including F6's inputs | F6 decision value on the 5 standard windows; F12 |
| 2 | **Historical status/news** (defect A): neutralize the end-of-season snapshots in training, or reconstruct genuine pre-deadline status for history from archived Scout team-news articles; keep the real live values | The anchor's injury coefficients and 13.8% of prompts were learned from leaky values | The anchor's MAE and decision value; the adapter's availability AUC |
| 3 | **Live ownership units, live F2b** (C, D) | Live-only bias against popular players | The live sheet (Section 8.1) |
| 4 | **Backtest harness:** label embargo for 3GW/5GW (drop or truncate labels reaching week ≥ W), partial autosubs, neutral chip DP, 5-2-3 formation, identical delta clipping live and backtest | Makes the bench measure what live can do | New classic baselines on every standard window (old and new totals won't be comparable) |
| 5 | **Evidence matching:** require first name + surname, or club co-occurrence, for common surnames | "Michael Keane" collects Robbie Keane passages | Evidence precision on a sample |

## 8.3 The research program, in order of expected value per cost

1. **A proper appearance model in the anchor (CPU, a day).** Replace `minutes / 90` with a logistic classifier, which beats the LLM alone. Let the decision layer consume it continuously: either as `E[points] = P(appear) × E[points | plays]`, or through the soft availability weight. Judge on a wide bench.
2. **Expectation decoding for the adapter (GPU decode only, no training).** Decode E19's holdout with sampling (e.g. 8 samples, average) or compute the expected value from the token probabilities. Then re-run the three-window backtest. If the median diagnosis is right, the shrink should mostly vanish, and with it the systematic under-rating of premiums. Pre-register the bar: ≥ +50 over 3 windows, then replicate on a re-decoded older set.
3. **A wide classic bench (CPU, an afternoon, after fixes 1–4).** Thirty or more 4-week windows across 2022-26, with the per-window noise floor measured afresh. First uses: re-test F6 on clean opponent data, F10 and F11 properly, and one larger swing, a **gradient-boosted anchor**. A model-class change shifts squads a lot, so judge it against the adapter-size noise floor.
4. **The live availability tracker (CPU, minutes a week).** Weekly: classic, logistic, adapter, and logistic + adapter AUC among likely starters. This is the low-variance metric on which a null is informative.
5. **An availability-first adapter (GPU, one run, only if 2 or 4 is positive).** Train with availability as the main job, on this season's data, with clean status inputs. Evaluate on a multi-window holdout.
6. **Team notes from digests (E16).** Digest team-analysis articles into `team_notes` attached to every player of the club as a separate prompt line. Single variable.
7. **Reinforcement learning only with a trajectory reward**, from a self-built squad over several weeks, after the RL-cache defects are fixed.
8. **12B only as a paired retrain** after an objective change.
9. **Publishing:** code only, no weights; start from the live repo, with artifacts, reports, logs and data excluded.

## 8.4 What to stop doing

- Adding inputs to the adapter's prompt in the hope it will use them (0 for ~14).
- Judging anything on GW35-38 alone, on a single window, or on a proxy.
- Comparing the LLM against a strawman baseline.
- Anchor features without a measured defect behind them.
- Trusting any field labelled "pre-deadline" without checking that it varies week to week.
- Narrating unsettled weeks (now mechanically prevented).

## 8.5 Questions worth sitting with

You said you want to reflect on this material. These are the questions I would sit with, because the answers change what the project should do next, and they are genuinely yours to answer:

1. **What counts as "the LLM works" for goal #2?** After a fair baseline, the LLM's measurable contribution is a small complementary availability signal (+0.017 AUC live over a logistic model) and occasional excellent individual reads (Calafiori's substitution, Watkins' standoff). Is that the answer to goal #2, a modest yes for a narrow job? Or does goal #2 require a decision gain the squad backtest can detect? Both positions are defensible; they lead to different next steps.
2. **Is "load-bearing" better pursued as a narrower role done well?** The data says the LLM is good at reading specific events and bad at being a general forecaster. A system in which the LLM *flags* events (an injury in a press conference, a substitution pattern, a contract standoff) and the optimizer *uses* them as hard availability inputs might be more load-bearing than one in which it adds small deltas to everything.
3. **How much variance do you want?** Haaland is owned by 74% of managers. Expected-points maximization treats ownership as irrelevant. But if your goal is beating the average or a mini-league, owning or fading highly-owned players is a variance choice, not an expectation choice, and the optimizer currently has no view on it.
4. **How should your own judgment enter the system?** Your calls have been the project's best signal, but they enter as ad-hoc overrides. A structured channel ("Wes: Konsa nailed") that the optimizer consumes and the ledger scores would make your judgment measurable and reusable.
5. **What would make you stop?** A pre-stated condition under which the adapter is retired, or goal #2 is declared answered, protects against continuing by inertia. For example: "no incremental live availability edge over the logistic model by GW20, and no positive expectation-decoding result."


---

# Appendices

## Appendix A — Glossary

| term | meaning |
|---|---|
| **Adapter** | A LoRA fine-tune of Gemma-4-E4B that outputs bounded JSON deltas against the classic forecast. Named E1, E2, … |
| **Anchor / classic** | The ridge-regression forecast suite. "Classic+F6" is the anchor with the F6 opponent-interaction features. |
| **AUC** | Area under the ROC curve: the probability that a randomly chosen player who appeared is ranked above one who didn't. 0.5 = coin flip. Measures discrimination, which calibration cannot change. |
| **avail_soft** | A decision-layer variant that multiplies each starter's points by min(1, P(appear)/0.80), instead of the default threshold penalty below P = 0.6. |
| **availability_scaled** | An LLM application mode that rescales classic points by P_llm / P_classic, clamped to [0.6, 1.4]. |
| **Brier score** | Mean squared error of a probability forecast. Lower is better. Mixes calibration and discrimination. |
| **Chrono adapter / chrono legality** | An adapter trained to an earlier season's cutoff, so it can legally adjust later weeks. The legality map says which adapter may touch which weeks. |
| **Decision value** | Realized FPL points scored by the squad the decision layer builds and manages from a set of forecasts, in a walk-forward backtest. The shipping metric. |
| **DefCon** | Defensive Contribution: +2 points for reaching 10 (DEF) or 12 (MID/FWD) combined defensive actions in a match; introduced 2025-26. |
| **Draft** | The beam-search construction of an initial 15-man squad from forecasts (`build_initial_squad`). Each backtest window starts with one. |
| **Eyeball gate** | Comparing the live baseline distribution to the previous week, and spot-checking premiums, before spending GPU on a decode. |
| **F-number** | A CPU-tested change to the anchor or decision layer (F1–F12). |
| **G-number** | A GRPO reinforcement-learning run (G1–G4). |
| **Gate** | (1) The ship/no-ship decision backtest; (2) a sanity assertion in a pipeline that refuses to proceed on bad data. |
| **GRPO** | Group Relative Policy Optimization: sample a group of completions per prompt, score each with a reward, and push probability toward completions above the group mean. Here via TRL 1.0. |
| **Hit** | −4 points for each transfer beyond the free allowance. |
| **Ledger (season)** | `reports/season_2627_ledger.jsonl`: settled weekly scores, decisions, judgment calls and lessons. |
| **Ledger (two-model)** | The leak-free layering rule: an adapter never trains on the weeks it adjusts; outcomes teach only the layer above. |
| **Mechanism check** | `scripts/check_delta_mechanism.py`: partial correlation of the adapter's delta with a designed signal, controlling for the baseline. |
| **Noise floor** | The standard deviation of decision-value differences between equivalent configurations: ~14.9 per 4-week window for small anchor tweaks, 24–40 for adapter comparisons. |
| **Provenance line** | A prompt sentence describing what the classic forecast already accounts for. The v1 version suppressed the fixture channel. |
| **Rate-normalized labels** | Multi-week labels scaled by horizon / weeks available, fixing season-end truncation. |
| **Residual / delta** | The adapter's correction: Δpoints (1/3/5GW), Δminutes, ΔP(appear). |
| **Shrink (component)** | The part of the adapter's delta explained by a per-week linear function of the baseline. About 91% of its MAE gain on E19. |
| **V3** | Availability routing: classic points × (P_llm/P_classic ratio, clamped and normalized by the week's mean). |
| **Expectation decoding** | Decoding the adapter's *expected* output (average of sampled completions, or the probability-weighted value over number tokens) rather than its single most likely output. Proposed fix for the median-seeking shrink. |
| **Median-seeking (mode-seeking)** | The behavior of a cross-entropy-trained numeric output decoded greedily: it returns roughly the most likely value, which for right-skewed residuals lies below the mean. |
| **Logistic appearance model** | A logistic regression predicting P(minutes > 0) from the anchor's features: the fair baseline for the LLM's availability reads (AUC 0.744 vs the LLM's 0.717 on E19's likely starters). |
| **Walk-forward** | Refit on strictly prior data for each evaluated week. |
| **Window** | A contiguous block of gameweeks (usually 4) for one decision backtest. |

## Appendix B — Where things live

| path | what |
|---|---|
| `src/fpl_ai/dataset.py` | Ingestion normalization, feature engineering, labels, flag-gated feature blocks, live-frame builder |
| `src/fpl_ai/models.py` | Ridge model suite, predictions, band calibration and decision-weighting flags |
| `src/fpl_ai/decision.py` | DecisionWeights, lineup optimizer, squad evaluation, transfer recommendations |
| `src/fpl_ai/backtest.py` | Draft beam search, rolling squad backtest |
| `src/fpl_ai/llm_adjust.py` | Delta parsing, clipping and application modes |
| `src/fpl_ai/grpo_env.py`, `grpo_plan_env.py`, `grpo_forecast_env.py` | G1, G2/G3 and G4 reward environments |
| `scripts/build_residual_player_forecast_split_v2.py` | Builds adapter SFT datasets and prompts |
| `scripts/attach_*_to_corpus.py` | Attach evidence, fixtures, congestion, DefCon, market, depth chart to the corpus |
| `train_gemma_sft.py`, `eval_gemma_responses.py` | Adapter training and batched decoding |
| `train_gemma_grpo*.py` | RL trainers |
| `score_player_forecast_residual_eval.py` | Adapter evaluation (MAE, strict JSON, ranking lift) |
| `scripts/run_weekly_ingest.sh`, `scripts/gw_status.py` | Weekly ingest with the settled gate |
| `scripts/build_live_gw_examples.py`, `scripts/decode_live.sh`, `scripts/recommend_gw2_actions.py`, `scripts/apply_llm_deltas_and_draft.py` | Weekly live pipeline |
| `scripts/check_delta_mechanism.py`, `scripts/explain_player_delta.py`, `scripts/audit_evidence_quality.py`, `scripts/report_premium_calibration.py` | Diagnostics |
| `reports/backtest_*`, `reports/*eval_summary.json` | Experiment results |
| `reports/adapter_bench_2026_09_29/` | The 29 September decomposition and 21-window bench |
| `reports/season_2627_ledger.jsonl` | Season ledger |
| `artifacts/` | All trained adapters |
| `~/fpl_freeze/2026-08-16_gw1_ship/` | Read-only GW1 ship snapshot |
| `docs/` | Plans, experiment logs, session states, this document |

## Appendix C — Every trained model

Final logged training loss and token accuracy are from each run's last `trainer_state.json`. All E4B adapters use LoRA rank 16, alpha 32, dropout 0, via PEFT `target_parameters`.

| artifact | steps | final loss | token acc. | notes |
|---|---|---|---|---|
| 31B squad_v1 / v2_textonly / v3_format_json | 12 each | 6.12 / 1.97 / 2.18 | 0.45–0.70 | April pilots (r16, α32) |
| 31B transfer_choice_v1 | 11 | 2.10 | 0.65 | April pilot |
| 31B player_forecast pilot top2 / top8 / top96 | 24 / 95 / 1,140 | 0.48 / 0.14 / 0.087 | 0.88 / 0.95 / 0.97 | Direct forecasts |
| 31B player_forecast gw1_10_top128_768 | 80 | 1.67 | 0.70 | r4, α8 |
| 31B residual gw1_10 pilot (+ dirty_leakage copy) | 24 | 0.87 / 0.81 | 0.87 / 0.89 | r4, α8 |
| 31B residual gw1_25_top128 | 200 | 0.146 | 0.957 | Blew up at GW26 |
| 31B ranking_value | 640 of 1,000 | 0.298 | 0.877 | Free listwise |
| 31B anchored_ranking_value | 160 of 600 | 0.164 | 0.925 | Stopped at ckpt-160 |
| E4B smoke | 100 | 0.312 | 0.887 | |
| E1 structured / E2 evidence / E3a rich | 1,000 each | 0.163 / 0.167 / 0.163 | 0.933–0.934 | 16k rows |
| E4 / E5 / E6 / E7 | 2,000 each | 0.143 / 0.143 / 0.143 / 0.144 | 0.941–0.942 | 32k rows |
| E7-chrono-2324 / E7-chrono-2425 | 784 / 1,392 | 0.188 / 0.149 | 0.931 / 0.940 | Out-of-window replication and G2 surfaces |
| E8 podcast | 2,000 | 0.143 | 0.942 | Negative |
| E9 clean split | 1,824 | 0.142 | 0.945 | 29,184 rows |
| E10 prelaunch | 2,368 | 0.147 | 0.942 | GW1 ship |
| E11 defcon / E11-full | 2,368 / 2,432 | 0.139 / 0.147 | 0.943 / 0.940 | E11-full live since GW2 |
| E12 / E13a / E14 / E15 | 2,368 each | 0.138 / 0.138 / 0.139 / 0.139 | 0.941–0.944 | Evidence and market variants |
| E17 / E18 | 2,368 each | 0.149 / 0.149 | 0.938 / 0.939 | F6 anchor |
| E19 wide holdout | 2,240 | 0.147 | 0.939 | Trained thru GW26 |
| G1 grpo_decision_v1 | 464 | — | — | Weekly bandit |
| G2 plan v1 / v2 / v2b / v3 | killed ~90 of 384 / 232 / 232 / 232 | — | — | v1 a machinery smoke run; v2 30.6 h, v2b 28.1 h, v3 30.9 h |
| G3 (incl. G3b extension) | 236 + 118 = 354 | — | — | Transfer pick; 32.0 h + 18.3 h |
| G4 forecast v1 / v2 | 100 of 1,138 / 1,326 | — | — | RL on forecasts |

Wall-clock times recorded in the logs: E1–E3a ~10–14 h; E4 23.1 h; E6 30.6 h; E7 ~48 h; E8 50.7 h; E9 45.9 h; E10 52 h; E11-full 58.7 h; E17 71.9 h; G2-v2 30.6 h; G2-v2b 28.1 h; chrono-2324 19.7 h.

## Appendix D — The complete backtest scoreboard

Totals are realized points (`total_actual_points`). Totals are comparable only *within* a group that shares window, anchor and table version.

**2025-26 GW12-30 (the original gate, 19 weeks):**

| config | total |
|---|---|
| classic only (baseline optimizer) | 1,058 |
| avail_soft / horizon5 / horizon5_avail / 2 transfers | 1,031 / 996 / 1,042 / 995 |
| lookahead-2 (schedule / horizon_diff) | 1,002 / 1,058 |
| E3a all / availability / availability_scaled / avail × soft | 1,000 / 1,058 / 1,001 / 1,056 |
| E4 all / availability_scaled / avail × soft | 1,020 / 992 / 1,056 |
| E6 all / availability_scaled / avail × soft | 1,035 / 1,000 / 1,058 |
| **E7 all** / availability_scaled / avail × soft | **1,069** / 1,027 / 1,058 |
| E8 all / availability_scaled / avail × soft | 1,025 / 1,002 / 1,060 |

**2024-25 GW12-30:** classic 1,261; avail_soft 1,270; horizon5 1,241; lookahead-2 1,255 / 1,210; **E7-chrono all 1,314**, avail × soft 1,262, availability_scaled 1,214.

**2023-24 GW12-30:** classic 1,056; avail_soft 1,067; lookahead-2 1,055 / 1,056. **2022-23 GW12-30:** classic 1,166.

**Wide classic baselines:** 2022-23 (33 weeks) 1,898; 2023-24 (37) 2,136; 2024-25 (37) 2,288; 2025-26 GW2-11 538; 2025-26 GW30-38 517.

**2025-26 GW2-30 (E9 gate, 29 weeks):** classic 1,471; **E9 all 1,553**; E9 avail × soft 1,549; E9 availability_scaled 1,414.

**2025-26 GW11-30 premium fixes (old-sign F2/F3):** base 1,007; band calibration 987; leverage 1,007; both 987. Early GW2-8: 409 / 404 / 409 / 404.

**Early-season (GW2-8) anchor tests, by season 2023-24 / 2024-25 / 2025-26:** base 389 / 408 / 409; **F2b 411 / 440 / 406**; F2c 419 / 427 / 400; F5 407 / 440 / 365; alpha 10: 411 / 438 / 406; alpha 50: 389 / 438 / 412.

**2025-26 GW35-38 (4 weeks):** E10 sanity 270 vs classic 268. E11 check 277 vs classic 267; field modes all 277 / availability 267 / availability_scaled 257. E11 277, E15 264. With the F6 table: classic+F6 270, E11-defcon 260, E17 300, E18 308.

**2025-26 GW27-38 (E19, three windows):** classic+F6 258 / 234 / 270; E19 220 / 212 / 339.

**The 29 September bench (classic+F6 anchor; job-local outputs, reproducible from `reports/adapter_bench_2026_09_29/`):**

| set | windows | classic | raw adapter | V3 |
|---|---|---|---|---|
| 2025-26 (E9 decode) | GW2-5 … GW22-25 | 224 / 228 / 150 / 264 / 196 / 217 | 194 / 228 / 198 / 230 / 239 / 206 | 227 / 228 / 224 / 248 / 193 / 201 |
| 2023-24 (E7c decode) | GW12-15 … GW32-35 | 216 / 243 / 234 / 276 / 200 / 259 | 196 / 250 / 213 / 274 / 218 / 238 | 208 / 259 / 245 / 273 / 244 / 335 |
| 2024-25 (E7c decode) | GW12-15 … GW32-35 | 273 / 232 / 233 / 368 / 171 / 225 | 314 / 252 / 231 / 347 / 183 / 228 | 275 / 247 / 224 / 257 / 164 / 270 |
| 2025-26 (E19 decode) | GW27-30 / 31-34 / 35-38 | 258 / 234 / 270 | 220 / 212 / 339 | 259 / 269 / 286 |

## Appendix E — Timeline

| date (2026) | event |
|---|---|
| Apr 13–29 | 31B squad / transfer / direct-forecast pilots |
| May – Jun | 31B residual pilots; listwise and anchored reranking |
| Jun 3 | A residual pilot set aside for a leakage problem |
| Jun 13 / Jul 3 | Project summary; your annotated "two goals" |
| Jul 5 | Season plan approved: E4B, residuals, "LLM load-bearing" |
| Jul 7–8 | E1, E2, E3a; first gate fails (1,000 vs 1,058) |
| Jul 9–10 | Decision-knob sweep; ≥3-window rule; lookahead rejected; oracle test closes planning depth |
| Jul 10–13 | E4, E5, E6 |
| Jul 13–15 | G1 |
| Jul 18 | E7 first gate win (1,069) |
| Jul 20 | E7-chrono-2425 replicates (+53) |
| Jul 18–25 | G2 design (deployment regime, two-model ledger); G2-v2 (+47/+27), v2b |
| Jul 26–29 | Evidence quality review; E8 podcast (negative) |
| Jul 30 | G2-v3 chip fix (half-renewal correction); E9 launched |
| Aug 2 | E9 wins (+82); DefCon generalization fails |
| Aug 6–8 | E10 ship model; status/news neutralization discovered |
| Aug 7 | GPU launch gate |
| Aug 10 | Season confirmed live (GW1 Aug 21) |
| Aug 16 | Ship freeze; publish code only |
| Aug 17–19 | G3 / G3b flat |
| Aug 19 | GW1 squad drafted and entered |
| Aug 21 | Arsenal-defender question → rate-normalized labels; E11 launched |
| Aug 22–24 | Evidence audit, extraction pilots, digest architecture, Haiku vs Gemma; E11 verdict; DefCon trilogy closed |
| Aug 24–26 | E11-full |
| Aug 25 | GW1 settled: 38 vs 50; bench-order fix |
| Aug 27 | Walk-forward bug caught pre-ship; E12 digest backfill; E12 launched |
| Aug 28 | GW2 (85 vs 79); Haaland 43rd → premium compression |
| Aug 30 – Sep 4 | F1–F3; F2b adopted; F2c rejected; E13a; GW3 (38 vs 51); retrospective; G4 launched |
| Sep 8 | Reboot kills E14 and G4 (both resumed) |
| Sep 10 | G4 fails (reward mis-specified); Guardian key restored; F5 rejected; Calafiori case; E15 split built |
| Sep 12 | GW4 (61 vs 69); settled-data gate becomes a script |
| Sep 13 | Team-context regex parked |
| Sep 17 | E15 verdict (best MAE, worse decisions) |
| Sep 17–18 | Fixture blindness → F6; live status gap; F7, F8; E17 launched; GW5 sheet |
| Sep 20 | GW5 retrospective artifact |
| Sep 21 | GW5 settled (61 vs 48); E17 split verdict |
| Sep 21–23 | Premium-minutes defect (6 hypotheses); F9; case studies |
| Sep 23–24 | F10, F11 (E20 cancelled), noise floor, attenuation audit, F12; stopping rule |
| Sep 24 | E18 (prompt blocks inert) |
| Sep 26 | E19 (adapter unresolved) |
| Sep 29 | Main session hits spend limit; shrink decomposition, availability AUC, 21-window bench |
| Oct 3 | This document; writing it uncovers the median-seeking mechanism, the logistic appearance baseline, and data defects A–D (end-of-season status and clubs, live ownership units, live F2b) |
| Oct 10 | GW6 deadline |


