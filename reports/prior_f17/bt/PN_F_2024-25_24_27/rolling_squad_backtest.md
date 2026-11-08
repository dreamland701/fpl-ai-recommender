# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 367.12
- Total actual points: 342.00
- Average predicted points: 91.78
- Average actual points: 85.50
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
- Predicted score: 113.13
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.80) beats the best remaining Bench Boost opportunity (14.62).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.80) beats the best remaining Bench Boost opportunity (14.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.48 | 12.13 | 18.59 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 6 | 3.9 | 0.39 | 0.86 | 1.45 | 0.00 | 8.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.19 | 16.87 | 26.24 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.47 | 10.77 | 17.83 | 4.00 | 84.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.44 | 10.56 | 16.10 | 7.00 | 177.6 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.94 | 8.06 | 12.83 | 1.00 | 87.9 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.43 | 6.69 | 10.76 | 1.00 | 77.7 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.95 | 33.13 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.48 | 18.46 | 27.85 | 7.00 | 172.4 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.57 | 12.27 | 18.74 | 9.00 | 172.9 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.77 | 26.25 | 42.69 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.36 | 19.79 | 33.36 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.09 | 16.85 | 27.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.06 | 13.31 | 21.00 | 2.00 | 89.8 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.93 | 7.63 | 12.93 | 4.00 | 65.2 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.56
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.36) beats the best remaining Triple Captain opportunity (11.53).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.36) beats the best remaining Triple Captain opportunity (11.53).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.79 | 11.53 | 18.08 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.15 | 0.60 | 1.03 | 0.00 | 6.9 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.19 | 16.12 | 26.12 | 13.00 | 176.3 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.76 | 11.21 | 18.37 | 2.00 | 87.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.51 | 10.73 | 16.70 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.29 | 6.89 | 11.31 | 1.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.37 | 4.46 | 7.53 | 0.00 | 51.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.85 | 17.90 | 30.23 | 2.00 | 89.8 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.01 | 14.88 | 22.99 | 0.00 | 136.5 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.17 | 7.97 | 13.07 | 0.00 | 55.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.33 | 29.49 | 48.30 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.54 | 32.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.54 | 15.65 | 25.69 | 3.00 | 83.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.70 | 15.32 | 23.74 | 5.00 | 84.1 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.47 | 7.36 | 11.97 | 1.00 | 66.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.26
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.58 | 17.19 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.07 | 0.59 | 1.00 | 0.00 | 8.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.60 | 17.04 | 27.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.24 | 18.03 | 1.00 | 87.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.22 | 9.31 | 15.15 | 1.00 | 88.0 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.40 | 7.14 | 11.60 | 1.00 | 83.0 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.60 | 2.47 | 4.49 | 0.00 | 27.7 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.16 | 18.26 | 30.11 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.35 | 15.78 | 25.56 | 5.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.44 | 5.08 | 9.71 | 0.00 | 26.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.28 | 30.04 | 48.98 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.15 | 18.53 | 30.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.14 | 17.11 | 26.71 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.23 | 13.19 | 20.55 | 2.00 | 66.3 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.42 | 7.65 | 12.28 | 7.00 | 72.5 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.17
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.11, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.97 | 16.24 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 6 | 3.9 | 0.51 | 0.87 | 1.37 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.83 | 16.37 | 26.93 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.83 | 10.90 | 17.58 | 4.00 | 86.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.44 | 10.23 | 16.64 | 0.00 | 84.2 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.75 | 6.72 | 0.00 | 39.3 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.13 | 1.44 | 2.98 | 1.00 | 17.6 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.56 | 17.75 | 29.10 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.87 | 15.47 | 26.25 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.68 | 4.27 | 8.23 | 0.00 | 16.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.84 | 29.88 | 48.97 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.21 | 19.48 | 31.83 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.00 | 18.02 | 28.47 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.88 | 18.82 | 10.00 | 64.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.64 | 9.27 | 14.66 | 3.00 | 76.9 | 89.0 |