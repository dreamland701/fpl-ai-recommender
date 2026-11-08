# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 361.84
- Total actual points: 342.00
- Average predicted points: 90.46
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
- Predicted score: 112.70
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.52) beats the best remaining Bench Boost opportunity (14.23).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.52) beats the best remaining Bench Boost opportunity (14.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 8.12 | 13.10 | 20.18 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Danny Ward | GK | 11 | 3.9 | 0.31 | 0.96 | 1.82 | 0.00 | 12.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.03 | 16.70 | 26.01 | 7.00 | 178.3 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.42 | 10.62 | 17.61 | 4.00 | 82.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.15 | 10.21 | 15.58 | 7.00 | 171.7 | 177.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.74 | 7.57 | 12.10 | 1.00 | 85.9 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.31 | 6.43 | 10.37 | 1.00 | 76.3 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.94 | 20.39 | 33.80 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 12.18 | 19.53 | 29.60 | 7.00 | 176.1 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.64 | 12.29 | 18.73 | 9.00 | 173.8 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.42 | 25.79 | 41.94 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.18 | 19.29 | 32.54 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.00 | 16.46 | 26.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 3.82 | 12.70 | 20.08 | 2.00 | 87.6 | 90.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 3.04 | 7.96 | 13.46 | 4.00 | 66.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 115.23
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (22.65) beats the best remaining Triple Captain opportunity (11.12).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (22.65) beats the best remaining Triple Captain opportunity (11.12).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.06 | 12.34 | 19.42 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.03 | 0.47 | 1.01 | 0.00 | 9.3 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 9.92 | 15.79 | 25.62 | 13.00 | 171.6 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.67 | 10.96 | 17.97 | 2.00 | 85.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.29 | 10.12 | 15.73 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.16 | 6.51 | 10.70 | 1.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.28 | 4.28 | 7.28 | 0.00 | 49.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.04 | 18.46 | 31.12 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 9.46 | 15.58 | 24.17 | 0.00 | 138.5 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.13 | 7.80 | 12.81 | 0.00 | 54.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 19.62 | 28.51 | 46.71 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.61 | 19.16 | 31.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.36 | 15.17 | 24.94 | 3.00 | 81.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.44 | 14.61 | 22.65 | 5.00 | 81.7 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.53 | 7.52 | 12.25 | 1.00 | 67.6 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.03
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.02 | 11.43 | 18.58 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.24 | 0.51 | 0.78 | 0.00 | 6.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.50 | 16.73 | 27.15 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.62 | 10.96 | 17.59 | 1.00 | 85.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.01 | 8.72 | 14.18 | 1.00 | 85.2 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.26 | 6.77 | 11.03 | 1.00 | 82.7 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.56 | 2.46 | 4.51 | 0.00 | 27.1 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.31 | 18.73 | 30.88 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.50 | 16.16 | 26.17 | 5.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.37 | 4.83 | 9.31 | 0.00 | 25.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.77 | 28.67 | 46.79 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.02 | 18.03 | 29.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.98 | 16.69 | 26.06 | 14.00 | 89.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.03 | 12.69 | 19.81 | 2.00 | 63.9 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.50 | 7.75 | 12.42 | 7.00 | 75.0 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.88
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.65, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.56 | 10.81 | 17.60 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.33 | 0.58 | 0.81 | 0.00 | 6.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.72 | 16.00 | 26.30 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.75 | 10.75 | 17.39 | 4.00 | 87.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.27 | 9.74 | 15.84 | 0.00 | 81.5 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.71 | 3.57 | 6.51 | 0.00 | 38.7 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.16 | 1.53 | 3.14 | 1.00 | 18.4 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.68 | 18.13 | 29.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.12 | 16.18 | 27.39 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.62 | 4.06 | 7.86 | 0.00 | 15.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.30 | 28.33 | 46.45 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.05 | 18.96 | 30.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.90 | 17.61 | 27.76 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.67 | 11.48 | 18.24 | 10.00 | 62.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.59 | 9.06 | 14.31 | 3.00 | 77.7 | 89.0 |