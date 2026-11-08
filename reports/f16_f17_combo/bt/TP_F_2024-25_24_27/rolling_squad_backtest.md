# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.45
- Total actual points: 342.00
- Average predicted points: 91.61
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
- Predicted score: 113.66
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.77) beats the best remaining Bench Boost opportunity (14.55).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.77) beats the best remaining Bench Boost opportunity (14.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.82 | 12.50 | 19.14 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Danny Ward | GK | 11 | 3.9 | 0.23 | 0.94 | 1.85 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.19 | 16.66 | 25.76 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.64 | 11.07 | 18.23 | 4.00 | 88.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.62 | 10.67 | 16.19 | 7.00 | 180.0 | 177.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.89 | 7.76 | 12.21 | 1.00 | 86.0 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.44 | 6.64 | 10.58 | 1.00 | 77.9 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.84 | 19.91 | 32.94 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.47 | 18.30 | 27.48 | 7.00 | 171.8 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.30 | 11.59 | 17.42 | 9.00 | 163.5 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.75 | 25.99 | 42.13 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.41 | 19.71 | 33.07 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.10 | 16.74 | 27.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.12 | 13.28 | 20.83 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 3.09 | 7.91 | 13.25 | 4.00 | 69.8 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.04
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.16) beats the best remaining Triple Captain opportunity (11.41).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.16) beats the best remaining Triple Captain opportunity (11.41).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.92 | 11.77 | 18.40 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.00 | 0.47 | 1.11 | 0.00 | 6.7 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.22 | 15.89 | 25.55 | 13.00 | 176.3 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.91 | 11.51 | 18.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.54 | 10.71 | 16.57 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.25 | 6.62 | 10.75 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.94 | 3.47 | 6.25 | 0.00 | 40.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.90 | 17.79 | 29.91 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.59 | 14.79 | 23.22 | 0.00 | 125.0 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.58 | 6.33 | 10.62 | 0.00 | 39.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.14 | 28.97 | 47.31 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.68 | 19.31 | 32.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.59 | 15.64 | 25.55 | 3.00 | 84.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.78 | 15.38 | 23.73 | 5.00 | 86.2 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.51 | 7.45 | 12.23 | 1.00 | 67.8 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.50
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 9.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.86 | 10.85 | 17.53 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.32 | 0.73 | 1.26 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.54 | 16.61 | 26.79 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.87 | 11.56 | 18.45 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.27 | 9.32 | 15.05 | 1.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.36 | 6.87 | 11.04 | 1.00 | 81.2 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.21 | 1.60 | 3.37 | 0.00 | 18.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.20 | 18.10 | 29.66 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.40 | 15.74 | 25.34 | 5.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 0.90 | 3.49 | 7.28 | 0.00 | 11.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.12 | 29.39 | 47.80 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.21 | 18.51 | 30.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.87 | 26.42 | 14.00 | 88.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.33 | 13.31 | 20.62 | 2.00 | 69.1 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.54 | 7.89 | 12.56 | 7.00 | 76.1 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.25
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.59, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.29 | 10.08 | 16.57 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.42 | 0.80 | 1.29 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.68 | 15.79 | 26.04 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.89 | 11.20 | 18.28 | 4.00 | 89.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.48 | 10.40 | 17.08 | 0.00 | 86.0 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.71 | 3.44 | 6.30 | 0.00 | 36.2 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.14 | 1.45 | 3.09 | 1.00 | 17.8 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.49 | 17.47 | 28.72 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.75 | 15.08 | 25.72 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.55 | 3.64 | 7.14 | 0.00 | 12.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.59 | 29.03 | 47.65 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.14 | 19.23 | 31.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.90 | 17.71 | 28.09 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.80 | 11.69 | 18.60 | 10.00 | 63.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.64 | 9.29 | 14.83 | 3.00 | 77.3 | 89.0 |