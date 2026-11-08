# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 367.88
- Total actual points: 335.00
- Average predicted points: 91.97
- Average actual points: 83.75
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
- Predicted score: 112.26
- Actual score: 118.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.87) beats the best remaining Bench Boost opportunity (14.37).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.87) beats the best remaining Bench Boost opportunity (14.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.50 | 14.33 | 20.83 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.00 | 0.04 | 0.00 | 0.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.13 | 25.70 | 33.93 | 7.00 | 180.0 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 12.07 | 17.56 | 7.00 | 176.1 | 177.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.70 | 17.81 | 4.00 | 82.5 | 90.0 |
| Bench 3 | Bench Boost | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 2.49 | 9.64 | 14.30 | 1.00 | 77.1 | 90.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.00 | 8.30 | 13.45 | 1.00 | 88.9 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.64 | 27.40 | 35.29 | 7.00 | 175.9 | 137.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.83 | 20.08 | 33.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.58 | 14.09 | 20.37 | 9.00 | 172.9 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.78 | 42.65 | 59.19 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.34 | 19.91 | 33.62 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.51 | 26.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.06 | 12.71 | 20.06 | 2.00 | 89.7 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.26 | 6.17 | 9.91 | 2.00 | 73.8 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 120.92
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (24.00) beats the best remaining Triple Captain opportunity (11.69).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (24.00) beats the best remaining Triple Captain opportunity (11.69).
- Autosub: Jan Bednarek replaced Ezri Konsa Ngoyo.
- Autosub: Boubakary Soumaré replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.85 | 11.28 | 17.74 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.35 | 20.01 | 24.76 | 13.00 | 179.5 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.15 | 18.41 | 2.00 | 86.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.58 | 10.45 | 16.29 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 4.60 | 8.98 | 10.98 | 0.00 | 147.9 | 0.0 |
| Bench 3 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.34 | 7.01 | 11.58 | 1.00 | 84.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.81 | 18.11 | 24.47 | 2.00 | 88.8 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.09 | 17.06 | 20.13 | 0.00 | 138.1 | 0.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.68 | 8.46 | 13.64 | 0.00 | 66.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.63 | 38.60 | 48.05 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.74 | 19.80 | 32.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.52 | 15.32 | 25.13 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.78 | 14.58 | 22.54 | 5.00 | 85.5 | 76.0 |
| Bench 4 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.10 | 6.32 | 10.48 | 2.00 | 76.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.69
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.70 | 10.40 | 17.07 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.77 | 17.25 | 22.67 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.25 | 18.20 | 1.00 | 86.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.18 | 9.10 | 14.86 | 1.00 | 87.2 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.44 | 7.43 | 12.09 | 1.00 | 83.8 | 11.0 |
| Bench 4 | Bench | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 1.15 | 3.74 | 5.28 | 2.00 | 39.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.12 | 17.95 | 23.97 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.34 | 15.44 | 25.23 | 5.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.69 | 5.52 | 10.23 | 0.00 | 32.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.46 | 30.75 | 40.50 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.13 | 18.65 | 31.21 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.16 | 16.40 | 26.20 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.24 | 12.43 | 19.16 | 2.00 | 66.3 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.44 | 6.67 | 10.87 | 2.00 | 75.7 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.01
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Ezri Konsa Ngoyo replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.24 | 9.83 | 16.10 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 11.08 | 22.14 | 6.00 | 90.0 | 76.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.19 | 16.67 | 0.00 | 83.3 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.82 | 8.56 | 13.95 | 6.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 1.35 | 5.07 | 8.85 | 0.00 | 51.0 | 0.0 |
| Bench 2 | Autosub In | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 2.06 | 3.97 | 7.90 | 0.00 | 66.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.82 | 15.29 | 25.75 | 2.00 | 90.0 | 84.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 11.82 | 23.56 | 0.00 | 90.0 | 0.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.94 | 4.70 | 8.85 | 0.00 | 22.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.89 | 20.32 | 40.41 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.33 | 31.87 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.99 | 17.52 | 28.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.51 | 18.09 | 10.00 | 64.1 | 90.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.46 | 6.70 | 10.87 | 2.00 | 75.6 | 60.0 |