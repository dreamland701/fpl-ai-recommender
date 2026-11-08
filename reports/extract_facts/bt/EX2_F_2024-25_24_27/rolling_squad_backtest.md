# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 372.61
- Total actual points: 336.00
- Average predicted points: 93.15
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
- Predicted score: 116.93
- Actual score: 122.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (14.86).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (14.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 12.08 | 18.47 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.13 | 0.62 | 0.97 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 11.20 | 17.81 | 28.58 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.54 | 10.85 | 17.84 | 4.00 | 85.2 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.41 | 10.52 | 16.00 | 7.00 | 177.3 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.06 | 8.37 | 13.27 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 2.97 | 8.27 | 13.11 | 0.00 | 78.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.83 | 19.98 | 32.94 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 12.35 | 19.22 | 29.90 | 7.00 | 180.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.46 | 12.10 | 18.41 | 9.00 | 171.2 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 17.88 | 27.29 | 45.10 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.43 | 19.86 | 33.25 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.08 | 16.78 | 27.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.02 | 13.22 | 20.78 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench Boost | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.25 | 6.44 | 10.95 | 7.00 | 57.8 | 89.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 121.04
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.43) beats the best remaining Triple Captain opportunity (12.13).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.43) beats the best remaining Triple Captain opportunity (12.13).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.82 | 11.60 | 18.13 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.25 | 0.56 | 0.97 | 0.00 | 7.8 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.34 | 16.29 | 26.28 | 13.00 | 179.4 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.81 | 11.26 | 18.35 | 2.00 | 88.2 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.51 | 10.75 | 16.68 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.41 | 7.21 | 11.77 | 1.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 1.27 | 3.77 | 6.63 | 0.00 | 35.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.92 | 17.98 | 30.18 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 7.88 | 14.49 | 23.93 | 0.00 | 116.7 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.86 | 7.31 | 12.28 | 0.00 | 46.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 21.41 | 30.78 | 50.74 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 7.22 | 20.67 | 34.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.16 | 16.37 | 25.83 | 5.00 | 90.0 | 76.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.57 | 15.63 | 25.48 | 3.00 | 84.2 | 90.0 |
| XI | XI | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.59 | 6.82 | 10.70 | 3.00 | 64.0 | 75.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.52
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.76 | 10.65 | 17.22 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.52 | 0.95 | 1.29 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.65 | 17.21 | 27.87 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.75 | 11.26 | 17.97 | 1.00 | 87.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.24 | 9.35 | 15.13 | 1.00 | 88.3 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.53 | 7.48 | 12.09 | 1.00 | 85.8 | 11.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 1.16 | 3.10 | 5.45 | 0.00 | 25.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.22 | 18.32 | 30.02 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.37 | 15.73 | 25.32 | 5.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.19 | 4.51 | 9.01 | 0.00 | 19.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.26 | 30.07 | 48.95 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.22 | 18.62 | 30.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 16.87 | 26.39 | 14.00 | 88.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.21 | 13.13 | 20.36 | 2.00 | 66.2 | 72.0 |
| Bench 2 | Bench | Myles Lewis-Skelly | MID | 1 | 4.5 | 2.26 | 6.36 | 9.96 | -2.00 | 57.5 | 16.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.11
- Actual score: 44.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.19 | 9.83 | 16.18 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.46 | 0.84 | 0.00 | 6.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.80 | 16.37 | 27.07 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.84 | 11.07 | 18.06 | 4.00 | 87.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.37 | 10.05 | 16.48 | 0.00 | 82.1 | 18.0 |
| XI | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.90 | 4.05 | 7.34 | 0.00 | 41.2 | 0.0 |
| Bench 3 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.3 | 0.43 | 1.57 | 3.25 | 0.00 | 14.8 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.48 | 17.57 | 28.87 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.77 | 15.23 | 25.97 | 2.00 | 90.0 | 84.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.73 | 4.31 | 8.32 | 0.00 | 17.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.23 | 31.04 | 51.41 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.62 | 20.59 | 34.17 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.89 | 17.76 | 28.17 | 5.00 | 89.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.78 | 11.77 | 18.77 | 10.00 | 62.6 | 90.0 |
| Bench 4 | Bench | Myles Lewis-Skelly | MID | 1 | 4.5 | 0.00 | 0.64 | 2.29 | 0.00 | 9.6 | 0.0 |