# Returner-pattern calibration (walk-forward classic forecasts, top-256 per week)

Table rows with a fixture 183,920; forecasts available for 38,906. Seasons 2019-20 → 2026-27 GW8.

## All rows with the pattern (realised only)

| slice | n | realised min | appeared | started | points |
|---|---|---|---|---|---|
| isak (injury blank 3 back, two 70+ games since) | 718 | 79.7 ± 2.4 | 0.929 | 0.458 | 2.96 |
| benchblank (unflagged 0-min week 3 back) | 1,333 | 71.0 ± 2.1 | 0.853 | 0.349 | 2.74 |
| anyblank (0-min week 3 back) | 2,423 | 73.7 ± 1.5 | 0.876 | 0.406 | 2.80 |
| nailed (three 70+ games) | 27,693 | 82.2 ± 0.4 | 0.944 | 0.507 | 3.31 |

## Rows with a stored forecast: forecast vs realised

| slice | n | fc min → real | fc P(app) → appeared | fc pts → real pts | Δ pts (real − fc) |
|---|---|---|---|---|---|
| isak (injury blank 3 back, two 70+ games since) | 360 | 60.8 → 78.7 ± 3.0 | 0.665 → 0.944 | 2.41 → 2.78 | +0.36 ± 0.30 |
| benchblank (unflagged 0-min week 3 back) | 543 | 60.5 → 71.1 ± 3.2 | 0.649 → 0.878 | 2.33 → 2.76 | +0.43 ± 0.25 |
| anyblank (0-min week 3 back) | 1,114 | 60.4 → 73.7 ± 2.0 | 0.654 → 0.897 | 2.39 → 2.73 | +0.34 ± 0.17 |
| nailed (three 70+ games) | 15,707 | 76.6 → 81.8 ± 0.4 | 0.823 → 0.950 | 3.13 → 3.34 | +0.21 ± 0.05 |

## The Isak slice by cut

| cut | n | fc min → real | fc P → appeared | fc pts → real | Δ pts |
|---|---|---|---|---|---|
| FWD | 21 | 61.7 → 84.1 ± 5.6 | 0.656 → 1.000 | 3.33 → 4.76 | +1.44 ± 1.32 |
| MID | 132 | 58.8 → 78.4 ± 4.5 | 0.647 → 0.970 | 2.54 → 2.99 | +0.46 ± 0.49 |
| DEF+GK | 207 | 62.0 → 78.4 ± 4.3 | 0.677 → 0.923 | 2.24 → 2.44 | +0.20 ± 0.38 |
| price ≥ 8.0 | 16 | 67.1 → 88.5 ± 2.2 | 0.745 → 1.000 | 3.85 → 5.31 | +1.47 ± 1.60 |
| price < 8.0 | 344 | 60.5 → 78.2 ± 3.1 | 0.661 → 0.942 | 2.35 → 2.66 | +0.31 ± 0.30 |
| 2019-22 | 0 | | | | |
| 2022-25 | 331 | 60.6 → 78.7 ± 3.1 | 0.661 → 0.946 | 2.39 → 2.81 | +0.42 ± 0.31 |
| 2025-27 | 29 | 64.0 → 79.1 ± 9.7 | 0.711 → 0.931 | 2.70 → 2.41 | -0.29 ± 0.89 |
| fc min < 70 | 312 | 57.8 → 76.9 ± 2.9 | 0.643 → 0.949 | 2.23 → 2.66 | +0.42 ± 0.31 |
| fc min ≥ 70 | 48 | 80.3 → 90.4 ± 11.8 | 0.809 → 0.917 | 3.58 → 3.56 | -0.02 ± 0.92 |

Nailed control restricted to the Isak slice's forecast-minutes band (49-72): n 4,901, fc min 66.2 → real 75.7, fc pts 2.69 → 3.05 (+0.37 ± 0.09).

## 2025-27 examples of the Isak slice

| season | GW | player | pos | fc min | real min | fc pts | real pts |
|---|---|---|---|---|---|---|---|
| 2025-26 | 5 | Ezri Konsa Ngoyo | DEF | 68 | 90 | 2.56 | 2 |
| 2025-26 | 5 | Daichi Kamada | MID | 57 | 90 | 2.41 | 2 |
| 2025-26 | 6 | Ethan Ampadu | MID | 68 | 90 | 1.85 | 1 |
| 2025-26 | 6 | Joško Gvardiol | DEF | 72 | 69 | 3.48 | 2 |
| 2025-26 | 7 | Vitalii Mykolenko | DEF | 56 | 90 | 2.27 | 4 |
| 2025-26 | 8 | Ismaïla Sarr | MID | 60 | 90 | 3.32 | 2 |
| 2025-26 | 10 | Trevoh Chalobah | DEF | 65 | 90 | 2.64 | 7 |
| 2025-26 | 10 | Kiernan Dewsbury-Hall | MID | 61 | 82 | 2.23 | 2 |
| 2025-26 | 10 | Murillo Costa dos Santos | DEF | 59 | 90 | 2.20 | 3 |
| 2025-26 | 12 | Joachim Andersen | DEF | 67 | 90 | 2.89 | 10 |
| 2025-26 | 12 | Ryan Gravenberch | MID | 66 | 90 | 3.00 | 1 |
| 2025-26 | 12 | Malo Gusto | DEF | 52 | 23 | 2.81 | 1 |
| 2025-26 | 14 | Alisson Becker | GK | 54 | 90 | 2.33 | 3 |
| 2025-26 | 14 | Tino Livramento | DEF | 55 | 90 | 2.27 | 3 |
| 2025-26 | 28 | Neco Williams | DEF | 68 | 55 | 2.83 | 0 |
| 2025-26 | 28 | Bukayo Saka | MID | 65 | 90 | 4.52 | 2 |
| 2025-26 | 28 | Anthony Gordon | MID | 57 | 85 | 3.12 | 2 |
| 2025-26 | 28 | Djed Spence | DEF | 59 | 0 | 2.01 | 0 |
| 2025-26 | 29 | Reece James | DEF | 64 | 90 | 2.77 | 2 |
| 2025-26 | 29 | Anton Stach | MID | 63 | 90 | 2.89 | 4 |
| 2025-26 | 33 | Matty Cash | DEF | 62 | 90 | 2.50 | 1 |
| 2025-26 | 34 | Nordi Mukiele | DEF | 74 | 90 | 3.35 | 0 |
| 2025-26 | 34 | Daniel Muñoz Mejía | DEF | 66 | 90 | 3.15 | 6 |
| 2025-26 | 34 | Crysencio Summerville | MID | 62 | 90 | 2.85 | 2 |
| 2025-26 | 34 | Robin Roefs | GK | 72 | 90 | 2.67 | 0 |
| 2025-26 | 34 | Lewis Miley | MID | 59 | 90 | 1.82 | 2 |
| 2026-27 | 4 | Andersen | DEF | 78 | 0 | 2.35 | 0 |
| 2026-27 | 4 | Mukiele | DEF | 82 | 90 | 2.88 | 0 |
| 2026-27 | 5 | Gudmundsson | DEF | 64 | 90 | 2.33 | 6 |

## Nailed control by forecast-minutes band (three 70+ games, unflagged)

| forecast minutes | n | fc min → real | fc pts → real | Δ pts |
|---|---|---|---|---|
| < 60 | 1,083 | 49.6 → 73.4 | 2.18 → 3.15 | +0.97 ± 0.20 |
| 60-72 | 4,031 | 67.4 → 76.3 | 2.70 → 3.06 | +0.36 ± 0.10 |
| 72-80 | 5,735 | 76.1 → 80.4 | 2.92 → 3.07 | +0.15 ± 0.08 |
| 80-86 | 2,713 | 82.5 → 83.6 | 3.26 → 3.42 | +0.16 ± 0.12 |
| 86-91 | 795 | 88.2 → 87.1 | 3.84 → 3.83 | −0.01 ± 0.25 |

4th game back (injury blank 4 back, three 70+ since): n 289, 70.7 → 81.8 min, +0.21 ± 0.35 pts. Isak slice with the last
two games averaging ≥ 75 min (his 78/76): n 358, 60.9 → 78.9 min, appeared 0.947, +0.37 ± 0.30 pts.

## Reading

1. **P(appear) is predicted minutes / 90** (`models.py`, per-fixture mode), not a probability; Isak's 0.72 is his
   65-minute forecast restated. 94.7% of players with his pattern appeared. The optimizer uses the points forecasts, not
   this column, so it does not drive the recommendation.
2. **The minutes forecast is too low for his pattern by ~18 min** (61 → 79, ± 3). About 8 of those are the injury blank
   sitting in the 3/5/8-week rolling windows (`returner_counterfactual.py`: 65 → 73 min when GW6 is filled with 78);
   the rest is the ridge's general shrinkage, which under-forecasts every nailed player in the 60-72 band by ~9 min.
3. **In points the pattern is under-forecast by +0.37 ± 0.30 per GW, the same as any nailed player forecast at 60-72
   minutes (+0.36 ± 0.10).** Players forecast at 86+ minutes (Thiago, N.Jackson) are calibrated (−0.01 ± 0.25). Applied:
   Isak 20.3 + ~1.8 ≈ 22.1 over GW9-13 vs Thiago 21.5 / Jackson 21.4 → a coin flip, slight lean to Isak, inside noise.
4. **Injury blank vs benching blank**: same forecast (60.8 / 60.5 min), realised 78.7 vs 71.1 min, but points +0.36 vs
   +0.43: the model cannot tell them apart and that costs ~8 minutes of accuracy, not points. A fix (availability-
   conditional rolling windows, or a "flagged blank in window" feature, F18) is cheap to test on the 21-window bench but
   its decision value is likely small; the bigger systematic lever is the minutes-band under-forecast itself.

## Decomposition of the GW9-13 gap (`forecast_decomposition.py Isak Thiago N.Jackson`, same fit and snapshot)

| family (features) | Isak | Thiago | N.Jackson | Isak − Thiago | Isak − Jackson |
|---|---|---|---|---|---|
| availability (16) | +4.16 | +5.85 | +4.84 | −1.68 | −0.68 |
| points form (19) | +1.74 | +3.13 | +2.48 | −1.38 | −0.74 |
| xG form (11) | +0.83 | +1.94 | +0.83 | −1.11 | 0.00 |
| fixtures / F6 (20) | −0.16 | +0.25 | +0.09 | −0.41 | −0.24 |
| market (7) | +7.85 | +4.49 | +7.31 | +3.36 | +0.54 |
| total (intercept 5.87) | 20.31 | 21.53 | 21.42 | −1.22 | −1.12 |

Largest single features vs Thiago: expected_assists_avg_5 −3.18 (0.01 vs 0.23 per game), defensive_contribution_avg_3
−1.88 (0.7 vs 7.7; Brentford's forward presses, a work-rate proxy that gives forwards no points), creativity_avg_5
−1.59, expected_goal_involvements_avg_3 −1.57 (0.26 vs 0.58: the GW6 zero sits in Isak's 3-game average), minutes_avg_3
−1.09 (51 vs 90); in Isak's favour points_avg_8 +1.86 (6.4 vs 2.9), price +1.73, expected_goals_avg_5 +1.54 (0.40 vs
0.30). Vs Jackson the market term is Jackson's one-week ownership jump (selected_change_1 8.9 vs 3.0: −2.46) against
Isak's price (+3.07). So Isak's finishing and his season (51 pts in 7 starts, xGI/90 0.70, second only to Haaland) ARE
credited; the gap is minutes plus a creativity/pressing profile the ridge rewards in Thiago. Flag-off re-forecasts
(FPL_PRIOR_BLEND=0, FPL_OPPONENT_INTERACTION=0) are NOT valid counterfactuals at forecast time: those flags act when the
table is built, and the outputs were identical.
