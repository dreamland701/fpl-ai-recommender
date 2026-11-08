# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.27
- Total actual points: 339.00
- Average predicted points: 91.57
- Average actual points: 84.75
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
- Predicted score: 112.52
- Actual score: 117.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.30) beats the best remaining Bench Boost opportunity (13.99).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.30) beats the best remaining Bench Boost opportunity (13.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.37 | 12.02 | 18.45 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.35 | 0.79 | 1.32 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.08 | 16.80 | 26.10 | 7.00 | 179.8 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.47 | 10.74 | 17.75 | 4.00 | 83.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.34 | 10.46 | 15.98 | 7.00 | 175.5 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.01 | 8.28 | 13.20 | 1.00 | 89.0 | 90.0 |
| Bench 3 | Bench Boost | Dean Huijsen | DEF | 3 | 4.4 | 2.54 | 8.14 | 13.40 | 0.00 | 80.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.80 | 19.94 | 32.97 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.86 | 19.07 | 29.08 | 7.00 | 180.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.40 | 12.06 | 18.42 | 9.00 | 169.5 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.79 | 26.31 | 42.64 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.40 | 19.82 | 33.26 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.76 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.97 | 13.15 | 20.78 | 2.00 | 88.2 | 90.0 |
| Bench 4 | Bench Boost | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.55 | 10.55 | 2.00 | 74.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.76
- Actual score: 95.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.46) beats the best remaining Triple Captain opportunity (11.58).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.46) beats the best remaining Triple Captain opportunity (11.58).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.80 | 11.57 | 18.13 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.41 | 0.93 | 0.00 | 9.3 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.22 | 16.20 | 26.20 | 13.00 | 176.4 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.75 | 11.17 | 18.26 | 2.00 | 86.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.50 | 10.72 | 16.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 3.14 | 8.45 | 13.67 | 2.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 7.12 | 11.71 | 1.00 | 84.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.89 | 17.95 | 30.17 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.23 | 14.10 | 23.44 | 0.00 | 125.6 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.21 | 8.06 | 13.15 | 0.00 | 55.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.43 | 29.62 | 48.37 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.76 | 19.58 | 32.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.62 | 25.53 | 3.00 | 83.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.63 | 15.16 | 23.48 | 5.00 | 82.4 | 76.0 |
| Bench 4 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.13 | 6.58 | 10.90 | 2.00 | 77.0 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.52
- Actual score: 75.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.73 | 10.59 | 17.19 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.22 | 0.66 | 1.22 | 0.00 | 9.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.63 | 17.17 | 27.83 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.18 | 17.90 | 1.00 | 86.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.21 | 9.29 | 15.09 | 1.00 | 87.6 | 90.0 |
| XI | XI | Dean Huijsen | DEF | 3 | 4.4 | 2.63 | 7.72 | 12.53 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.47 | 7.39 | 12.02 | 1.00 | 84.3 | 11.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.18 | 18.26 | 30.01 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.33 | 15.70 | 25.34 | 5.00 | 86.3 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.50 | 5.19 | 9.81 | 0.00 | 27.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.32 | 30.16 | 49.05 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.18 | 18.56 | 30.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 17.00 | 26.46 | 14.00 | 89.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.17 | 13.08 | 20.37 | 2.00 | 65.0 | 72.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.48 | 6.99 | 11.33 | 2.00 | 76.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.47
- Actual score: 52.00
- Transfer: Dean Huijsen -> Daniel Muñoz (projected gain 4.22, hit 0)
- Autosub: Boubakary Soumaré replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.95 | 16.19 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.37 | 0.87 | 1.40 | 0.00 | 8.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.88 | 16.51 | 27.12 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.90 | 11.18 | 18.07 | 4.00 | 89.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.42 | 10.15 | 16.48 | 0.00 | 83.5 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.84 | 8.75 | 14.26 | 6.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.91 | 4.07 | 7.26 | 0.00 | 41.3 | 0.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.55 | 17.69 | 28.90 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.85 | 15.39 | 26.05 | 2.00 | 90.0 | 84.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.72 | 4.32 | 8.25 | 0.00 | 17.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.89 | 30.00 | 49.04 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.22 | 19.44 | 31.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.96 | 17.90 | 28.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.83 | 11.88 | 18.81 | 10.00 | 63.8 | 90.0 |
| Bench 2 | Autosub In | Boubakary Soumaré | MID | 11 | 4.4 | 2.51 | 6.98 | 11.32 | 2.00 | 76.6 | 60.0 |