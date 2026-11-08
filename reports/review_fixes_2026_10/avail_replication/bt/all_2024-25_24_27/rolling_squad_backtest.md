# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 244.60
- Total actual points: 362.00
- Average predicted points: 61.15
- Average actual points: 90.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.92
- Actual score: 127.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.66) beats the best remaining Bench Boost opportunity (13.28).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.66) beats the best remaining Bench Boost opportunity (13.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 9.18 | 14.09 | 10.00 | 108.1 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 2.23 | 7.60 | 13.23 | 3.00 | 78.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.93 | 12.84 | 20.21 | 7.00 | 107.8 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.60 | 9.51 | 14.34 | 7.00 | 137.7 | 177.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 2.84 | 9.17 | 14.75 | 0.00 | 87.1 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 2.83 | 9.02 | 14.31 | 1.00 | 74.2 | 86.0 |
| Bench 3 | Bench Boost | Daniel Muñoz | DEF | 7 | 4.8 | 2.71 | 8.52 | 14.26 | 11.00 | 80.4 | 90.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 4.36 | 11.07 | 17.64 | 9.00 | 138.8 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.55 | 10.12 | 16.47 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.22 | 6.46 | 10.63 | 7.00 | 67.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.28 | 23.91 | 39.67 | 29.00 | 150.3 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 5.64 | 15.69 | 27.17 | 6.00 | 99.1 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.14 | 14.16 | 22.78 | 2.00 | 93.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.61 | 12.03 | 18.46 | 2.00 | 97.1 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.1 | 2.96 | 9.58 | 16.71 | 2.00 | 82.4 | 86.0 |

## GW25

- Train rows: 150166
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.38
- Actual score: 102.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.69) beats the best remaining Triple Captain opportunity (7.19).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Lewis Hall -> Antonee Robinson (projected gain 1.77, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (12.69) beats the best remaining Triple Captain opportunity (7.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.09 | 8.57 | 14.14 | 7.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.54 | 7.65 | 12.28 | 3.00 | 108.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.30 | 14.02 | 22.36 | 13.00 | 115.0 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 2.99 | 9.79 | 16.18 | 2.00 | 87.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 2.89 | 8.90 | 14.01 | 1.00 | 86.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 2.56 | 8.51 | 14.18 | 6.00 | 82.3 | 86.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.50 | 8.08 | 12.62 | 2.00 | 104.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.49 | 10.37 | 16.47 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.98 | 7.21 | 11.42 | 0.00 | 67.7 | 0.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.20 | 6.18 | 10.35 | 5.00 | 71.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.01 | 25.85 | 42.87 | 20.00 | 171.9 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.08 | 15.52 | 26.25 | 2.00 | 73.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.17 | 12.88 | 22.49 | 5.00 | 88.9 | 76.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.94 | 11.54 | 19.50 | 3.00 | 62.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.1 | 2.85 | 9.51 | 15.57 | 1.00 | 82.5 | 71.0 |

## GW26

- Train rows: 150945
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.77
- Actual score: 67.00
- Transfer: Bruno Guimarães Rodriguez Moura -> Alexis Mac Allister (projected gain 3.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.09 | 9.22 | 14.71 | 1.00 | 95.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.08 | 8.80 | 14.26 | 2.00 | 87.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.65 | 14.05 | 22.72 | 6.00 | 108.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 2.85 | 9.01 | 14.69 | 1.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.8 | 2.61 | 8.62 | 13.58 | 13.00 | 84.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 2.70 | 8.17 | 12.81 | 1.00 | 67.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.78 | 7.94 | 12.84 | 1.00 | 89.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.65 | 10.93 | 16.92 | 8.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.73 | 10.88 | 1.00 | 74.0 | 18.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.60 | 4.35 | 7.87 | 0.00 | 48.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.39 | 26.47 | 43.65 | 14.00 | 151.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 4.98 | 16.45 | 26.84 | 2.00 | 92.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.35 | 14.72 | 24.91 | 14.00 | 96.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.31 | 12.10 | 19.18 | 2.00 | 76.4 | 72.0 |
| XI | XI | Alexis Mac Allister | MID | 12 | 6.2 | 3.63 | 11.79 | 18.53 | 3.00 | 110.4 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.53
- Actual score: 66.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 2.81 | 8.52 | 13.76 | 2.00 | 93.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.43 | 8.38 | 13.92 | 6.00 | 84.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.32 | 12.61 | 21.32 | 6.00 | 80.3 | 76.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 2.77 | 9.10 | 14.53 | 7.00 | 82.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 2.79 | 8.83 | 13.97 | 0.00 | 85.8 | 18.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.21 | 8.62 | 13.75 | 4.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.51 | 7.62 | 11.92 | 6.00 | 87.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.44 | 9.96 | 15.38 | 9.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.84 | 4.45 | 8.99 | 0.00 | 20.8 | 0.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.36 | 4.27 | 7.28 | 0.00 | 34.7 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.50 | 26.06 | 43.22 | 6.00 | 131.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 5.73 | 15.41 | 25.69 | 3.00 | 104.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.03 | 15.28 | 23.89 | 5.00 | 94.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.34 | 10.38 | 16.44 | 10.00 | 69.1 | 90.0 |
| XI | XI | Alexis Mac Allister | MID | 12 | 6.2 | 3.08 | 8.82 | 14.67 | 8.00 | 89.2 | 86.0 |