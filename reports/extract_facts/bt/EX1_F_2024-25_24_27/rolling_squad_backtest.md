# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 373.85
- Total actual points: 336.00
- Average predicted points: 93.46
- Average actual points: 84.00
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
- Predicted score: 116.90
- Actual score: 122.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.85) beats the best remaining Bench Boost opportunity (15.20).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.85) beats the best remaining Bench Boost opportunity (15.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.37 | 12.03 | 18.45 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.35 | 0.78 | 1.32 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.22 | 17.82 | 28.62 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.49 | 10.78 | 17.81 | 4.00 | 83.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.35 | 10.48 | 15.98 | 7.00 | 175.6 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.01 | 8.30 | 13.23 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench Boost | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 2.94 | 8.22 | 13.09 | 0.00 | 77.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.79 | 19.94 | 32.94 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 12.34 | 19.22 | 29.93 | 7.00 | 180.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.39 | 12.06 | 18.39 | 9.00 | 169.5 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 17.89 | 27.31 | 45.15 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.40 | 19.83 | 33.27 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.76 | 27.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.98 | 13.16 | 20.75 | 2.00 | 88.2 | 90.0 |
| Bench 4 | Bench Boost | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.43 | 6.75 | 11.35 | 7.00 | 63.7 | 89.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 121.39
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.54) beats the best remaining Triple Captain opportunity (12.20).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.54) beats the best remaining Triple Captain opportunity (12.20).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.81 | 11.59 | 18.16 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.40 | 0.92 | 0.00 | 9.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.26 | 16.23 | 26.25 | 13.00 | 177.0 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.76 | 11.20 | 18.32 | 2.00 | 87.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.51 | 10.75 | 16.72 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.13 | 11.73 | 1.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 1.18 | 3.63 | 6.54 | 0.00 | 33.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.88 | 17.94 | 30.17 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.07 | 14.35 | 23.42 | 0.00 | 122.1 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.22 | 8.07 | 13.18 | 0.00 | 56.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 21.52 | 30.87 | 50.87 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 7.31 | 20.82 | 34.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.16 | 16.37 | 25.87 | 5.00 | 90.0 | 76.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.59 | 25.49 | 3.00 | 83.3 | 90.0 |
| XI | XI | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.54 | 6.75 | 10.66 | 3.00 | 62.5 | 75.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.43
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.74 | 10.61 | 17.23 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.22 | 0.66 | 1.22 | 0.00 | 9.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.65 | 17.20 | 27.88 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.71 | 11.20 | 17.94 | 1.00 | 86.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.22 | 9.32 | 15.14 | 1.00 | 87.9 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.48 | 7.40 | 12.05 | 1.00 | 84.5 | 11.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 1.14 | 3.08 | 5.37 | 0.00 | 24.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.18 | 18.26 | 30.01 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.32 | 15.68 | 25.30 | 5.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.51 | 5.20 | 9.83 | 0.00 | 27.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.33 | 30.18 | 49.09 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.19 | 18.57 | 30.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 17.00 | 26.45 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.17 | 13.07 | 20.35 | 2.00 | 65.0 | 72.0 |
| Bench 2 | Bench | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.21 | 6.28 | 9.92 | -2.00 | 55.9 | 16.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.13
- Actual score: 44.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.27 | 9.98 | 16.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.37 | 0.87 | 1.39 | 0.00 | 8.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.88 | 16.52 | 27.13 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.20 | 18.10 | 4.00 | 89.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.43 | 10.17 | 16.50 | 0.00 | 83.6 | 18.0 |
| XI | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.92 | 4.09 | 7.31 | 0.00 | 41.5 | 0.0 |
| Bench 3 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 0.39 | 1.53 | 3.13 | 0.00 | 13.5 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.55 | 17.69 | 28.90 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.85 | 15.38 | 26.03 | 2.00 | 90.0 | 84.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.72 | 4.32 | 8.25 | 0.00 | 17.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.40 | 31.33 | 51.62 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.73 | 20.77 | 34.26 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.97 | 17.92 | 28.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.83 | 11.88 | 18.78 | 10.00 | 63.7 | 90.0 |
| Bench 4 | Bench | Myles Lewis-Skelly | MID | 1 | 4.5 | 0.00 | 0.39 | 1.94 | 0.00 | 6.1 | 0.0 |