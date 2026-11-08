# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 301.42
- Total actual points: 359.00
- Average predicted points: 75.36
- Average actual points: 89.75
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 82.56
- Actual score: 126.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.13) beats the best remaining Bench Boost opportunity (15.33).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.13) beats the best remaining Bench Boost opportunity (15.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.82 | 12.18 | 18.69 | 10.00 | 176.9 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 2.73 | 8.80 | 14.93 | 3.00 | 78.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.43 | 16.84 | 26.21 | 7.00 | 160.3 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.94 | 12.22 | 19.25 | 6.00 | 147.6 | 180.0 |
| Bench 3 | Bench Boost | Antonee Robinson | DEF | 9 | 5.1 | 3.34 | 10.61 | 17.59 | 4.00 | 85.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.20 | 10.51 | 16.04 | 7.00 | 165.5 | 177.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.53 | 10.42 | 16.81 | 1.00 | 78.4 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 4.96 | 12.27 | 18.74 | 9.00 | 150.8 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.35 | 11.82 | 19.07 | 2.00 | 84.6 | 90.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.66 | 10.73 | 7.00 | 66.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.48 | 26.31 | 42.77 | 29.00 | 152.0 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.24 | 19.69 | 33.17 | 6.00 | 82.5 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 16.76 | 27.28 | 2.00 | 85.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.41 | 13.33 | 21.06 | 2.00 | 80.7 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.08 | 12.20 | 19.92 | 2.00 | 84.7 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 85.64
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.69) beats the best remaining Triple Captain opportunity (9.31).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 2.82, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.69) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.84 | 11.65 | 18.28 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.97 | 16.44 | 7.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.30 | 16.32 | 26.46 | 13.00 | 131.5 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.29 | 15.63 | 24.33 | 2.00 | 154.6 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.69 | 11.09 | 18.18 | 2.00 | 84.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.60 | 10.88 | 16.92 | 2.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.57 | 8.63 | 14.68 | 0.00 | 60.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.09 | 11.57 | 19.07 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.68 | 9.11 | 14.82 | 0.00 | 47.7 | 0.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.60 | 7.18 | 11.75 | 5.00 | 75.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.31 | 29.85 | 48.87 | 20.00 | 156.0 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.58 | 19.52 | 32.25 | 2.00 | 80.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.54 | 25.50 | 3.00 | 87.2 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.17 | 15.48 | 23.99 | 5.00 | 80.3 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.61 | 13.38 | 20.12 | 4.00 | 167.4 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.97
- Actual score: 71.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.79 | 10.52 | 17.11 | 1.00 | 85.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.50 | 17.16 | 2.00 | 87.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.75 | 17.45 | 28.32 | 6.00 | 70.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.68 | 14.14 | 22.62 | 6.00 | 84.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.17 | 17.91 | 1.00 | 86.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.28 | 9.24 | 15.04 | 1.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.88 | 8.99 | 15.05 | 9.00 | 85.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.35 | 12.13 | 19.02 | 8.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.77 | 7.93 | 12.58 | 1.00 | 75.2 | 18.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.70 | 5.65 | 10.57 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.29 | 30.47 | 49.65 | 14.00 | 86.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 5.98 | 18.45 | 30.54 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.35 | 17.12 | 26.71 | 14.00 | 84.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.51 | 13.20 | 20.58 | 2.00 | 79.3 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.99 | 11.48 | 17.67 | 2.00 | 85.1 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.25
- Actual score: 64.00
- Transfer: Lewis Hall -> Daniel Muñoz (projected gain 1.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.31 | 9.92 | 16.16 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.23 | 9.78 | 16.02 | 6.00 | 87.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 16.61 | 27.32 | 6.00 | 83.7 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.36 | 12.76 | 20.79 | 7.00 | 83.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.91 | 11.02 | 17.85 | 4.00 | 88.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.39 | 10.13 | 16.47 | 0.00 | 84.5 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.91 | 8.72 | 14.22 | 6.00 | 82.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.84 | 11.06 | 17.38 | 9.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.76 | 5.77 | 9.78 | 0.00 | 44.5 | 58.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.94 | 4.85 | 9.09 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.70 | 30.06 | 49.22 | 6.00 | 85.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.23 | 19.41 | 31.69 | 3.00 | 83.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.13 | 17.98 | 28.39 | 5.00 | 87.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.88 | 18.84 | 10.00 | 69.5 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.52 | 7.77 | 13.74 | 7.00 | 62.6 | 90.0 |