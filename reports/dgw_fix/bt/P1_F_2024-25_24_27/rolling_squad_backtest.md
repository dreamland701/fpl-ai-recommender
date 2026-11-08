# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 367.91
- Total actual points: 364.00
- Average predicted points: 91.98
- Average actual points: 91.00
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
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 110.72
- Actual score: 126.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.54) beats the best remaining Bench Boost opportunity (18.77).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.54) beats the best remaining Bench Boost opportunity (18.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.50 | 12.18 | 18.69 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 2.89 | 8.80 | 14.93 | 3.00 | 79.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.13 | 16.84 | 26.21 | 7.00 | 180.0 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 7.41 | 12.22 | 19.25 | 6.00 | 157.7 | 180.0 |
| Bench 3 | Bench Boost | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.61 | 17.59 | 4.00 | 82.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 10.51 | 16.04 | 7.00 | 176.1 | 177.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.60 | 10.42 | 16.81 | 1.00 | 76.2 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.58 | 12.27 | 18.74 | 9.00 | 172.9 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.27 | 11.82 | 19.07 | 2.00 | 76.0 | 90.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.52 | 6.66 | 10.73 | 7.00 | 58.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.78 | 26.31 | 42.77 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.34 | 19.69 | 33.17 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.76 | 27.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.06 | 13.33 | 21.06 | 2.00 | 89.7 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.01 | 12.20 | 19.92 | 2.00 | 83.8 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 124.19
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.00) beats the best remaining Triple Captain opportunity (11.69).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 2.82, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.00) beats the best remaining Triple Captain opportunity (11.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.85 | 11.65 | 18.28 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.60 | 9.97 | 16.44 | 7.00 | 82.1 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.35 | 16.32 | 26.46 | 13.00 | 179.5 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 10.21 | 15.63 | 24.33 | 2.00 | 180.0 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.09 | 18.18 | 2.00 | 86.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.58 | 10.88 | 16.92 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.75 | 8.63 | 14.68 | 0.00 | 71.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.98 | 11.57 | 19.07 | 2.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.68 | 9.11 | 14.82 | 0.00 | 66.6 | 0.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.63 | 7.18 | 11.75 | 5.00 | 65.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.63 | 29.85 | 48.87 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.74 | 19.52 | 32.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.52 | 15.54 | 25.50 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.78 | 15.48 | 23.99 | 5.00 | 85.5 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.59 | 13.38 | 20.12 | 4.00 | 173.8 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.85
- Actual score: 72.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.70 | 10.52 | 17.11 | 1.00 | 90.0 | 90.0 |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.50 | 17.16 | 2.00 | 85.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.77 | 17.45 | 28.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.71 | 14.14 | 22.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.17 | 17.91 | 1.00 | 86.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.18 | 9.24 | 15.04 | 1.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.93 | 8.99 | 15.05 | 9.00 | 76.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.17 | 12.13 | 19.02 | 8.00 | 73.7 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.79 | 7.93 | 12.58 | 1.00 | 69.8 | 18.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.69 | 5.65 | 10.57 | 0.00 | 32.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.46 | 30.47 | 49.65 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.13 | 18.45 | 30.54 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.16 | 17.12 | 26.71 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.24 | 13.20 | 20.58 | 2.00 | 66.3 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.12 | 11.48 | 17.67 | 2.00 | 85.0 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.15
- Actual score: 68.00
- Transfer: Lewis Hall -> Daniel Muñoz (projected gain 1.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.24 | 9.92 | 16.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.27 | 9.78 | 16.02 | 6.00 | 82.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 16.61 | 27.32 | 6.00 | 90.0 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.34 | 12.76 | 20.79 | 7.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.83 | 11.02 | 17.85 | 4.00 | 87.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.13 | 16.47 | 0.00 | 83.3 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.82 | 8.72 | 14.22 | 6.00 | 85.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.74 | 11.06 | 17.38 | 9.00 | 70.9 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.77 | 5.77 | 9.78 | 0.00 | 45.3 | 58.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.94 | 4.85 | 9.09 | 0.00 | 22.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.89 | 30.06 | 49.22 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.41 | 31.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.99 | 17.98 | 28.39 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.88 | 18.84 | 10.00 | 64.1 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.70 | 7.77 | 13.74 | 7.00 | 60.6 | 90.0 |