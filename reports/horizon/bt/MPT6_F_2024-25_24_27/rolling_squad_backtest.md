# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 365.16
- Total actual points: 336.00
- Average predicted points: 91.29
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
- Predicted score: 112.05
- Actual score: 118.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.96) beats the best remaining Bench Boost opportunity (14.42).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.96) beats the best remaining Bench Boost opportunity (14.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 14.22 | 20.67 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.01 | 0.49 | 0.88 | 0.00 | 7.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.16 | 25.75 | 34.01 | 7.00 | 180.0 | 98.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 12.08 | 17.57 | 7.00 | 176.2 | 177.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.45 | 10.79 | 17.96 | 4.00 | 83.3 | 90.0 |
| Bench 3 | Bench Boost | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 2.53 | 9.78 | 14.48 | 1.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.01 | 8.32 | 13.49 | 1.00 | 89.1 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.44 | 26.98 | 34.76 | 7.00 | 171.5 | 137.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.93 | 33.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.50 | 13.97 | 20.21 | 9.00 | 171.3 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.79 | 42.64 | 59.17 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.36 | 19.97 | 33.69 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.52 | 26.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.04 | 12.67 | 20.00 | 2.00 | 89.3 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.25 | 10.04 | 2.00 | 74.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 118.77
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.77) beats the best remaining Triple Captain opportunity (11.56).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.77) beats the best remaining Triple Captain opportunity (11.56).
- Autosub: Jan Bednarek replaced Ezri Konsa Ngoyo.
- Autosub: Boubakary Soumaré replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.78 | 11.12 | 17.51 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.59 | 0.92 | 0.00 | 6.8 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.19 | 19.76 | 24.47 | 13.00 | 176.0 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.74 | 11.21 | 18.51 | 2.00 | 86.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.26 | 15.99 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 3.63 | 7.32 | 9.07 | 0.00 | 126.6 | 0.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.07 | 11.66 | 1.00 | 84.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.84 | 18.18 | 24.54 | 2.00 | 89.5 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.96 | 16.88 | 19.95 | 0.00 | 135.2 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.16 | 7.13 | 11.62 | 0.00 | 55.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.39 | 38.22 | 47.58 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.78 | 32.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.51 | 15.32 | 25.14 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.69 | 14.35 | 22.22 | 5.00 | 83.6 | 76.0 |
| Bench 4 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.13 | 6.41 | 10.62 | 2.00 | 77.0 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.31
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 23.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.45 | 17.14 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.77 | 1.15 | 0.00 | 6.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 16.90 | 22.24 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.71 | 11.26 | 18.22 | 1.00 | 86.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.20 | 9.15 | 14.94 | 1.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.47 | 7.50 | 12.20 | 1.00 | 84.3 | 11.0 |
| Bench 4 | Bench | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 0.84 | 2.93 | 4.29 | 2.00 | 32.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.15 | 18.05 | 24.07 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.32 | 15.39 | 25.14 | 5.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.43 | 4.84 | 9.20 | 0.00 | 26.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.32 | 30.40 | 40.05 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.15 | 18.68 | 31.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 16.29 | 26.02 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.21 | 12.35 | 19.07 | 2.00 | 65.6 | 72.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.48 | 6.78 | 11.04 | 2.00 | 76.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.03
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Ezri Konsa Ngoyo replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.25 | 9.85 | 16.15 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.57 | 0.89 | 0.00 | 5.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.86 | 10.97 | 21.96 | 6.00 | 90.0 | 76.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.42 | 10.20 | 16.69 | 0.00 | 83.5 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.84 | 8.61 | 14.02 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Ezri Konsa Ngoyo | DEF | 2 | 4.4 | 2.13 | 4.10 | 8.13 | 0.00 | 68.4 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.89 | 3.89 | 7.06 | 0.00 | 40.9 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.84 | 15.34 | 25.82 | 2.00 | 90.0 | 84.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 11.84 | 23.56 | 0.00 | 90.0 | 0.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.66 | 3.98 | 7.75 | 0.00 | 16.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.88 | 20.27 | 40.32 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.35 | 31.88 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.98 | 17.49 | 27.99 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.83 | 11.48 | 18.06 | 10.00 | 63.8 | 90.0 |
| XI | XI | Boubakary Soumaré | MID | 11 | 4.4 | 2.51 | 6.83 | 11.06 | 2.00 | 76.7 | 60.0 |