# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 301.78
- Total actual points: 360.00
- Average predicted points: 75.44
- Average actual points: 90.00
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
- Predicted score: 82.63
- Actual score: 126.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.15) beats the best remaining Bench Boost opportunity (15.35).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.15) beats the best remaining Bench Boost opportunity (15.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.81 | 12.16 | 18.66 | 10.00 | 128.3 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.5 | 2.73 | 8.83 | 14.98 | 3.00 | 76.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.43 | 16.87 | 26.28 | 7.00 | 119.5 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.94 | 12.19 | 19.21 | 6.00 | 106.5 | 180.0 |
| Bench 3 | Bench Boost | Antonee Robinson | DEF | 9 | 5.1 | 3.34 | 10.65 | 17.64 | 4.00 | 81.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.21 | 10.47 | 15.96 | 7.00 | 117.8 | 177.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.53 | 10.40 | 16.77 | 1.00 | 75.4 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 4.97 | 12.23 | 18.64 | 9.00 | 118.7 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.35 | 11.88 | 19.17 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.63 | 10.66 | 7.00 | 56.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.49 | 26.38 | 42.88 | 29.00 | 129.9 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.28 | 19.73 | 33.16 | 6.00 | 100.8 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.13 | 16.74 | 27.26 | 2.00 | 94.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.41 | 13.31 | 21.03 | 2.00 | 95.3 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.08 | 12.24 | 20.00 | 2.00 | 84.9 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 85.72
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.70) beats the best remaining Triple Captain opportunity (9.39).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 2.75, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.70) beats the best remaining Triple Captain opportunity (9.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.84 | 11.62 | 18.23 | 3.00 | 109.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.59 | 10.00 | 16.48 | 7.00 | 81.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.29 | 16.36 | 26.53 | 13.00 | 115.8 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.28 | 15.60 | 24.29 | 2.00 | 147.0 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.69 | 11.13 | 18.23 | 2.00 | 85.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.61 | 10.84 | 16.83 | 2.00 | 105.7 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.57 | 8.61 | 14.64 | 0.00 | 68.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.10 | 11.63 | 19.17 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.70 | 9.08 | 14.72 | 0.00 | 66.6 | 0.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.60 | 7.15 | 11.68 | 5.00 | 64.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.32 | 29.91 | 48.97 | 20.00 | 172.4 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.64 | 19.55 | 32.24 | 2.00 | 92.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.53 | 15.53 | 25.48 | 3.00 | 82.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.17 | 15.47 | 23.97 | 5.00 | 90.1 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.61 | 13.36 | 20.08 | 4.00 | 119.7 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.07
- Actual score: 72.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 10.53 | 17.20 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.79 | 10.50 | 17.06 | 1.00 | 97.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.75 | 17.48 | 28.39 | 6.00 | 108.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.68 | 14.11 | 22.57 | 6.00 | 127.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.20 | 17.96 | 1.00 | 86.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.28 | 9.21 | 14.95 | 1.00 | 89.0 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.88 | 8.97 | 15.01 | 9.00 | 76.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.36 | 12.19 | 19.12 | 8.00 | 75.7 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.78 | 7.90 | 12.50 | 1.00 | 69.0 | 18.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.71 | 5.63 | 10.48 | 0.00 | 32.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.31 | 30.54 | 49.75 | 14.00 | 161.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.04 | 18.52 | 30.52 | 2.00 | 93.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.34 | 17.10 | 26.69 | 14.00 | 95.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.52 | 13.19 | 20.55 | 2.00 | 68.6 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.00 | 11.47 | 17.63 | 2.00 | 83.0 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.36
- Actual score: 64.00
- Transfer: Lewis Hall -> Daniel Muñoz (projected gain 1.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.31 | 9.90 | 16.10 | 2.00 | 94.6 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.24 | 9.81 | 16.06 | 6.00 | 82.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.91 | 16.63 | 27.39 | 6.00 | 100.0 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.36 | 12.73 | 20.74 | 7.00 | 108.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.93 | 10.99 | 17.73 | 4.00 | 88.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.39 | 10.16 | 16.52 | 0.00 | 83.3 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.92 | 8.69 | 14.14 | 6.00 | 86.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.85 | 11.11 | 17.46 | 9.00 | 72.3 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.76 | 5.75 | 9.71 | 0.00 | 44.7 | 58.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.95 | 4.84 | 9.01 | 0.00 | 21.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.71 | 30.13 | 49.32 | 6.00 | 141.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.31 | 19.52 | 31.66 | 3.00 | 103.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.12 | 17.96 | 28.36 | 5.00 | 95.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.87 | 18.81 | 10.00 | 62.3 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.52 | 7.76 | 13.70 | 7.00 | 57.8 | 90.0 |