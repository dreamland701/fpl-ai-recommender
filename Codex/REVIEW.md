# Why the FPL predictor is underperforming, and what to change

Review date: 2026-10-03. Evidence: current source, historical reports, saved live forecasts, the five-week ledger, current tests, isolated CPU reproductions, and official FPL rule sources.

## Assessment

The central problem is the reliability of the full forecasting and decision process. More SFT examples or longer RL training would currently optimize around inconsistent data, contaminated evaluation inputs, and an incomplete game simulator.

There is real work worth retaining: chronological experiment organization, stable player codes, saved prediction files, explicit bounded residuals, completion-mask tests, a legal-squad search, source-aware evidence retrieval, separate forecast and decision layers, and a live ledger. Several prior reviews already recognized shrinkage, small evaluation samples, availability issues, and the difference between forecast MAE and squad points. My review independently confirms parts of that diagnosis and adds material data and simulator defects.

The order of work should be:

1. Establish correct pre-deadline data and one scoring engine.
2. Establish a trustworthy baseline and paired evaluation.
3. Improve expected points and playing-time forecasts.
4. Give SFT a measurable information advantage from text.
5. Train RL only after it can beat a competent planner in a faithful environment.

This preserves your SFT-plus-RL direction while making it possible to know whether either layer helps.

## What the five live weeks actually say

The saved ledger gives:

| Gameweek | Your score | League average recorded | Difference |
|---|---:|---:|---:|
| 1 | 38 | 50 | -12 |
| 2 | 85 | 79 | +6 |
| 3 | 38 | 51 | -13 |
| 4 | 61 | 69 | -8 |
| 5 | 61 | 48 | +13 |
| Total | **283** | **297** | **-14** |

Source: `reports/season_2627_ledger.jsonl`, independently summed in `analysis/live_analysis.json`. The figures are the ledger's settled results, not independently retrieved account history. The weekly average includes other managers' chip decisions and heterogeneous teams; it is useful context, not a controlled baseline.

You confirmed that you generally followed the recommendations, refining them through discussion. That means the deployed system is the model, optimizer, conversational interpretation, and final entered selection together. The saved GW5 recommendation prefers Bogle, while the ledger records Konsa and a manual Cunha/Evanilson decision. We cannot correctly attribute that week's outcome to the raw model alone.

The ledger describes a nine-point GW1 and five-point GW5 bench-order counterfactual. Those are hindsight comparisons, not proof that a correct expected-value optimizer would have recovered 14 points. Nevertheless, they demonstrate why final bench order and the exact entered lineup must be first-class saved outputs. A good forecast that is not reflected in the entered team has no value.

The five captains produced a recorded raw total of 17 points: 2, 9, 2, 2, 2. That is disappointing, but five realized captain scores are far too noisy to identify a stable captain-selection effect. Likewise, “Konsa played 90 but Mitchell scored more” is not sufficient evidence that the decision was wrong at the deadline. Availability and points conditional on appearing are different uncertainties.

The stronger evidence comes from scoring all saved player forecasts against the completed weeks. This analysis matches by player identity and checks row alignment; it does not simulate an alternative season.

| GW | Matched players | Classic MAE | SFT MAE | Classic RMSE | SFT RMSE | Classic top-11 points | SFT top-11 points |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 595 | 1.626 | 1.523 | 2.649 | 2.672 | 48 | 40 |
| 2 | 616 | 1.233 | 1.146 | 2.136 | 2.160 | 39 | 39 |
| 3 | 652 | 1.097 | 1.052 | 1.951 | 1.993 | 37 | 35 |
| 4 | 654 | 1.215 | 1.162 | 2.184 | 2.233 | 54 | 50 |
| 5 | 659 | 1.125 | 1.109 | 2.145 | 2.201 | 39 | 39 |

**Top-11 here is an unconstrained ranking diagnostic**, not an affordable, position-legal XI, and it excludes captain doubling. It is not a claim that you would have scored the displayed points. All-player MAE also benefits from predicting the many nonparticipants well, so it is not a sufficient deployment objective.

Still, the pattern is informative: lower absolute error coexists with worse squared error and no observed improvement in that ranking diagnostic. The average emitted points delta is about -0.31 to -0.33 each week. Among players with classic appearance probability at least 0.5, GW5 mean prediction error worsens from -0.535 to -1.001 points per player. SFT is frequently making an already low expected-points estimate lower.

Availability has a more encouraging signal. In that likely-player subset, the Brier score improves in GW2–5, including 0.108 to 0.087 in GW5; it worsens slightly in GW1. This supports investigating text for playing-time information. It does not establish that multiplying all point forecasts by an availability ratio is calibrated or optimal.

## Data defects are more urgent than model capacity

### Ownership has incompatible units

The historical normalizer renames `selected` to `selected_by_percent`, but historical `selected` is a number of squads. It never divides by the historical number of entries. In the 2025-26 table, this supposed percentage has median **19,545** and maximum **9,515,178**. Over 96% of rows exceed 100.

Live inference uses the official API's actual percentage. It also calculates ownership change as a percentage minus the historical count. This is a fundamental distribution mismatch, not a small seasonal drift. Clipping features to the observed training range cannot reconcile two different units.

The problem reaches SFT: the first checked E13a training example says `owned by 6072.0% of managers`. This compromises interpretation of the market-feature ablation; a weak result there does not show that properly normalized market information is useless.

Fix ownership semantics explicitly. If a trustworthy historical denominator is unavailable, mark the percentage unknown and omit it from comparable experiments. Preserve counts as counts if useful, with the appropriate season/time normalization. Do not silently clip all historical ownership to 100 or fabricate a denominator.

### Historical status/news are not consistently historical snapshots

The 2019-20 through 2025-26 raw merged files lack a status column. The normalizer merges status and news from a single `players_raw.csv` lookup across all weeks, then shifts them by one row. Shifting a season-level snapshot does not turn it into information known at each historical deadline.

The old seasons' 19–38% flagged rates are therefore not a trustworthy target for the live injury-flag rate. A weekly guard that expects live flags to resemble that distribution may enforce a contaminated historical reference. The current-season backfill from archived corpora is a useful recovery step, but its timestamp meaning must also be explicit: a pre-GW-k snapshot should not be inadvertently shifted again into GW-k+1.

Club identity is also overwritten preferentially from the season player lookup. That requires auditing players who transferred between Premier League clubs midseason. Availability, team, position, price, ownership, fixtures, and text must all be indexed by when the fact was known.

### Multiweek labels cross the training boundary

`_training_frame_for_week` admits origins before the evaluation week, but a label at week t includes t through t+2 or t+4. Before 2025-26 GW27, the selected training set includes **1,634 three-week targets** and **3,248 five-week targets** that reach into GW27 or later.

For example, Haaland's week-26 three-week target is 11 = week-26's 5 + week-27's 6 + week-28's 0. That target is present in training before predicting GW27. The corpus exporter repeats the same origin-only cutoff. The SFT split builder also accepts training completions whose multiweek outcomes cross its holdout boundary.

This contaminates long-horizon evaluation and the baselines used in downstream SFT/RL. **It does not mean the one-week label itself leaks through that same mechanism**, and it does not prove how many points were gained or lost because of it.

I tested a partial repair in memory: purge immature 3GW/5GW targets and rerun three four-week classic backtests. Forecasts changed, but realized totals remained exactly **258, 234, 270** in both arms. That is a useful limit on the finding: the integrity defect is confirmed, but this diagnostic did not show a realized-points change in those windows. Other defects remained in both arms.

Use label-end and label-available timestamps, separately for each target. A multi-output SFT completion needs either a maturity mask per field or a cutoff early enough that every supervised field is known. For week W, with contiguous weekly windows, the condition is `t + horizon - 1 < W`; real settlement times are preferable to arithmetic when fixtures are rearranged.

### Full-season preprocessing also sees the future

F6 centers opponent weakness with a mean over the whole season before splitting; F12 uses the same pattern for team attack. Future rows can therefore change an earlier feature. This is a weaker and more indirect leak than seeing a target, but it violates the same contract. Fit preprocessing inside the training fold or compute a truly lagged expanding reference.

Final historical fixture calendars are another known source of hindsight. The fixture attachment script explicitly acknowledges using the final schedule. For chip timing, the timing of rearrangement announcements is central, so calling this bias minor is not justified without measurement.

### The early-season prior disappears during live recomputation

The prior blend requires both the previous season and the current season. The live helper intentionally slices raw history down to the current season before invoking the feature builder. Its resulting current-only form then overwrites the historical feature join. The result is that the intended prior blend has no previous-season lookup, even with `FPL_PRIOR_BLEND=1`.

The isolated GW6 reproduction changes `points_avg_3` for **420 of 667 players** when prior-season context is supplied to the same builder. Bruno Fernandes changes from 2.000 to 2.697; Haaland from 8.000 to 7.773. These are feature values, not point forecasts, and restoring them does not by itself establish improved outcomes. The important result is demonstrated train/live inconsistency.

The historical first-week representation is also unrealistic: 690 GW1 rows in 2025-26 have a zero pre-deadline price because price was blindly shifted. Live GW1 has actual launch prices and sometimes inherited previous-season form. Evaluation needs explicit preseason features and early-season folds; late-season validation is not a substitute.

## Why SFT is not yet providing the intended edge

Your current SFT trainer optimizes token cross-entropy over numeric JSON completions. It does **not** directly minimize point MAE, despite language in some design notes. Targets are rounded, clipped residuals, typically `clip(0.35 × (realized − baseline))`. Completion masking is tested and is worth retaining. The central issue is what those completions teach.

FPL outcomes have substantial zeros, two-pointers, and occasional large hauls. Predicting the conditional mean is appropriate for maximizing expected team points. Absolute-error selection rewards behavior closer to a conditional median, and greedy numeric token decoding is not an estimator of the predictive mean. Clipping large positive residuals also removes much of the magnitude information about hauls. The resulting model can reduce aggregate MAE by shrinking strong forecasts without improving the decisions that matter.

The E19 mechanism check supports this interpretation:

| Predictor, E19 saved evaluation rows | 1GW MAE | 1GW RMSE | Mean error, predicted minus actual |
|---|---:|---:|---:|
| Classic | 2.2716 | 3.0423 | +0.0388 |
| Full SFT | 2.1358 | 3.0593 | -0.4508 |
| Per-week linear shrink component only | 2.1478 | 3.0753 | -0.4508 |
| Player-specific remainder only | 2.2590 | 3.0260 | +0.0388 |

Approximately 91% of the absolute-error improvement is reproduced by the linear shrink component. That decomposition is fitted to saved adapter outputs, not to outcomes, but it is still descriptive and post hoc. It is not a calibrated deployable challenger. Nor does it prove that the model ignores text: a text ablation is required for that causal claim. The player-specific remainder and availability improvements are reasons to investigate more carefully rather than abandon the LLM.

A more promising SFT role is extracting information the numerical model lacks: available/unavailable/uncertain, expected role, return timing, likely starter or substitute, penalty/set-piece duties, and which teammates' absences change a player's opportunity. Each claim needs player and club resolution, evidence span, source, publication/update time, and an explicit unknown state. Predicting match results from retrospective prose is a much less reliable training objective.

Feed these extracted facts into a calibrated playing-time/points model. Keep direct residual SFT as an ablation. Require it to beat a simple numeric residual calibrator using the same inputs and folds. It should also survive evidence removal, shuffled evidence within the same deadline, and identity masking controls before claiming incremental text value.

The SFT pool is another mismatch: E11-full trains on 256 players per week, but live decoding covers roughly the whole player universe. Inclusion depends on baseline rank, and applying shrinkage only to the historical top-256 can change rankings around that cutoff. Training and evaluation should cover the same decision universe: the owned squad, legitimate transfer candidates, cheap bench options, returners, and newly registered players.

## Why RL is not yet solving your intended strategy problem

The G2/G3 plan environment has several limitations that change the meaning of its results.

**It exposes future information.** Its opening prompt includes squad projections and the best outside player from each future cached week. Those forecasts were computed at those later weeks using intervening results. An opening plan cannot legally know them. Live inference instead constructs pseudo-future weeks from current horizon sums. That is a fundamentally different observation process.

**It measures against a weak comparator.** The default sequential baseline spends no chips. A policy can gain simply by consuming an available chip. In the same current environment, the fixed rule “BB first opportunity, TC next opportunity, repeat next half” earns +13 on classic states and +15 on adjusted states without a trained model. This does not beat every reported RL result, but it shows why positive reward alone does not demonstrate learned strategic value.

**It cannot spend banked transfers as intended.** The recommender is always called with a maximum of one transfer. Starting with one FT and refreshing each week means the policy cannot learn the core benefit of accumulating transfers to make a coordinated double/triple move. G3 chooses among only three proposals from a restricted deterministic pool. Wildcard and Free Hit are absent from the plan action space.

**The environment and real scoring differ.** G2/G3 and G4 omit automatic substitutions. The general backtest includes them, but its implementation has a partial-team failure. The RL cap is two FTs, and its historical chip logic grants two half-season copies even to seasons before that rule existed. Current FPL has five saved transfers and two chip sets; season-specific rules are required. [Official current changes](https://www.premierleague.com/en/news/4679873) and [transfer rules](https://www.premierleague.com/en/news/2174907).

**Episode independence is overstated.** Overlapping training windows are correlated, and evaluation resets squad/bank/FT to cached trajectories at window boundaries while carrying chip availability. Six-week slicing of GW12–30 also drops GW30. Window outcomes sharing a season and chip budget are not independent replications of full-season strategy.

**Plan parsing hides noncompliance.** Multiple newline-separated action objects are accepted by extracting the first object and padding the rest with defaults. The saved v3 responses exhibit that style. “Zero unparseable” therefore does not imply a valid six-week plan. Some apparent long-term behavior is the fallback policy.

G4 adds further difficulties. The design calls for scoring the whole adjusted pool, but the implementation changes one player's delta in an otherwise classic pool. Decision boundaries differ when every player's forecast is adjusted at deployment. It also scores without autosubs despite the design describing autosubs, and trains a forecaster without giving it the squad/bank context on which its reward depends. The same player prompt can therefore receive incompatible preferences in different portfolio states. Its boundary filter checks realized reward changes, not just whether the selected action changes, so outcome ties affect which training examples are admitted.

The way forward is a weekly decision policy over validated legal candidate plans, with observations available at that deadline, an exact persistent squad state, and a competent deterministic planner as the opponent. Learn transferable choices such as when to bank, which multi-transfer plan to choose, or when a chip has high opportunity value. Do not expect RL to repair corrupted forecast inputs or a restricted action space.

## The classical forecast and optimizer need a stronger contract

The classic suite is four pooled ridge regressions. Position is carried as metadata but is absent from the active numerical feature list. The model can infer some position differences indirectly; it does not explicitly represent different FPL scoring rules for goals, clean sheets, and defensive contributions.

Appearance probability is derived from expected minutes divided by 90 times fixture count. That is not `P(minutes > 0)`. A guaranteed 30-minute substitute has appearance probability 1, not one-third. In double gameweeks, average participation per fixture is not the probability of appearing at least once. A 180-minute cap for all rows also allows single-fixture predictions above 90 minutes.

Build an explicit minutes distribution: no appearance, cameo, start under 60, start at least 60, with a fixture-level treatment for doubles. Model attacking events, clean sheets, save points, cards, defensive-contribution thresholds, and bonus or start with a strong expected-points regressor plus a calibrated availability model. Include position and era explicitly. Historical points include different scoring systems; official 2026-27 BPS changes make this especially relevant. [Official update](https://www.premierleague.com/en/news/4679873).

Separate modeling skill from optimization skill. The objective should be expected **fielded** points plus captain duplication, less hits, over the planned horizon, with the value of remaining transfers, chips, and budget represented. The current draft gives substantial value to all 15 players and has different backup-GK settings in live and historical paths. The weekly transfer scorer mixes multiweek starter points with a single-week captain term and chooses the future-value XI using only this week's starting lineup.

For fixed expected points and basic legal constraints, an exact MILP/CP-SAT or equivalent small exhaustive solver is an appropriate benchmark. RL should earn its place by beating it on uncertainty, sequential decisions, or terminal resource value. Simply choosing players from different clubs is already a hard constraint; it need not be learned by an LLM.

## What I would do immediately

Freeze new GPU experiment launches while the data and simulator repairs are implemented. Keep current artifacts as a historical record. Do not automatically switch to a new E-series adapter or a classic-only strategy solely on this review; the clean deployment comparison has not been run.

For the next deadline, produce one immutable packet from the actual current squad: snapshot timestamps, player IDs, purchase/selling prices, bank, FTs, remaining chips, frozen model/config hashes, predictions, uncertainty, transfer alternatives, starting XI, ordered outfield bench, bench GK, captain, vice, and every conversational override. Run the corrected numerical path and the existing stack side by side. Surface disagreements with evidence before choosing the final team.

The implementation sequence, experiments, acceptance criteria, and stop rules are in [PLAN.md](PLAN.md). The key decision is to spend the next effort on making the comparison trustworthy. Once that is done, the useful parts of SFT and RL can be improved with evidence instead of another round of small-window wins.
