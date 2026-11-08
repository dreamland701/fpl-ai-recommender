# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 363.16
- Total actual points: 327.00
- Average predicted points: 90.79
- Average actual points: 81.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 149404
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cody Gakpo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 112.62
- Actual score: 113.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.38) beats the best remaining Bench Boost opportunity (10.76).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.38) beats the best remaining Bench Boost opportunity (10.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 10.22 | 15.22 | 23.39 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.9 | 0.07 | 0.08 | 0.18 | 0.00 | 1.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.89 | 17.23 | 26.27 | 7.00 | 180.0 | 98.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.19 | 10.72 | 17.34 | 0.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.41 | 10.10 | 15.42 | 7.00 | 178.2 | 177.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 2.34 | 5.64 | 8.58 | 1.00 | 67.5 | 90.0 |
| Bench 4 | Bench Boost | Jannik Vestergaard | DEF | 11 | 3.9 | 1.80 | 5.11 | 8.17 | 0.00 | 75.2 | 59.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.27 | 18.47 | 27.38 | 7.00 | 180.0 | 137.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.80 | 18.06 | 29.45 | 2.00 | 87.5 | 90.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.87 | 11.97 | 18.45 | 9.00 | 150.4 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.83 | 26.41 | 43.17 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.59 | 20.33 | 34.13 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.25 | 17.26 | 28.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.21 | 12.12 | 19.66 | 2.00 | 83.3 | 90.0 |
| Bench 3 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.06 | 6.08 | 9.98 | 2.00 | 73.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 115.76
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.91) beats the best remaining Triple Captain opportunity (11.84).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.91) beats the best remaining Triple Captain opportunity (11.84).
- Autosub: Boubakary Soumaré replaced Amad Diallo.
- Autosub: Jacob Greaves replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.27 | 14.49 | 23.49 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.9 | 0.00 | 0.03 | 0.15 | 0.00 | 1.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 8.98 | 14.82 | 24.03 | 13.00 | 179.9 | 128.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.55 | 11.46 | 17.78 | 6.00 | 88.6 | 86.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.00 | 9.77 | 14.81 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 1.52 | 5.12 | 8.05 | 1.00 | 68.4 | 90.0 |
| Bench 4 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 0.48 | 2.83 | 5.01 | 0.00 | 53.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.42 | 16.74 | 27.72 | 2.00 | 85.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.58 | 15.05 | 22.69 | 0.00 | 150.2 | 0.0 |
| XI | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.92 | 9.87 | 16.25 | 0.00 | 58.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.88 | 30.32 | 49.56 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.70 | 32.49 | 2.00 | 87.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 16.44 | 27.12 | 3.00 | 82.4 | 90.0 |
| XI | Bench | Amad Diallo | MID | 14 | 5.6 | 3.57 | 10.78 | 18.52 | 0.00 | 68.4 | 0.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.08 | 6.31 | 10.65 | 2.00 | 76.7 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.53
- Actual score: 73.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.66 | 13.36 | 21.47 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.9 | 0.03 | 0.11 | 0.26 | 0.00 | 2.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.71 | 16.72 | 26.57 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.62 | 11.88 | 18.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.06 | 8.33 | 13.35 | 1.00 | 85.6 | 90.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.24 | 5.51 | 8.97 | 0.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 1.00 | 2.98 | 5.12 | 1.00 | 43.4 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.24 | 17.64 | 28.86 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.00 | 14.96 | 24.17 | 5.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.92 | 6.28 | 11.02 | 0.00 | 25.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.55 | 30.75 | 49.74 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.07 | 18.59 | 30.80 | 2.00 | 88.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.47 | 18.31 | 28.31 | 14.00 | 86.8 | 90.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.36 | 6.73 | 11.06 | 2.00 | 76.3 | 90.0 |
| Bench 4 | Bench | Amad Diallo | MID | 14 | 5.5 | 0.35 | 3.81 | 9.26 | 0.00 | 16.2 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.25
- Actual score: 47.00
- Transfer: Amad Diallo -> Antoine Semenyo (projected gain 6.72, hit 0)
- Autosub: Jacob Greaves replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.20 | 13.01 | 21.06 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.71 | 15.11 | 25.10 | 6.00 | 90.0 | 76.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.53 | 10.17 | 16.64 | 7.00 | 85.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.65 | 8.04 | 12.82 | 6.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 1.93 | 5.20 | 8.50 | 1.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Jannik Vestergaard | DEF | 11 | 3.9 | 1.41 | 4.09 | 6.77 | -1.00 | 55.2 | 86.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.48 | 17.11 | 27.99 | 0.00 | 88.2 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.80 | 15.81 | 26.11 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.92 | 5.18 | 9.02 | 0.00 | 15.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.15 | 30.98 | 49.99 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.16 | 19.80 | 32.10 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.15 | 18.63 | 29.20 | 5.00 | 89.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.91 | 11.82 | 18.84 | 1.00 | 77.4 | 90.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.37 | 6.70 | 11.12 | 2.00 | 76.1 | 60.0 |