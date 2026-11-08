# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.52
- Total actual points: 336.00
- Average predicted points: 91.63
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
- Predicted score: 114.00
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.19) beats the best remaining Bench Boost opportunity (15.00).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.19) beats the best remaining Bench Boost opportunity (15.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.44 | 12.07 | 18.47 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.47 | 0.97 | 1.48 | 0.00 | 13.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.12 | 16.82 | 26.10 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.52 | 10.82 | 17.79 | 4.00 | 85.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.41 | 10.51 | 15.99 | 7.00 | 177.2 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 3.06 | 8.36 | 13.25 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.54 | 6.95 | 11.08 | 1.00 | 80.3 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.84 | 19.99 | 32.97 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.94 | 19.16 | 29.25 | 7.00 | 180.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.47 | 12.10 | 18.44 | 9.00 | 171.2 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.83 | 26.34 | 42.66 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.43 | 19.86 | 33.24 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.08 | 16.78 | 27.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.02 | 13.21 | 20.81 | 2.00 | 89.4 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 3.00 | 7.68 | 12.85 | 4.00 | 67.2 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 116.82
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.40) beats the best remaining Triple Captain opportunity (11.55).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.40) beats the best remaining Triple Captain opportunity (11.55).
- Autosub: Enzo Fernández replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.81 | 11.58 | 18.09 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.22 | 0.71 | 0.00 | 4.6 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.30 | 16.25 | 26.22 | 13.00 | 178.9 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.80 | 11.23 | 18.29 | 2.00 | 88.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.72 | 16.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.41 | 7.20 | 11.76 | 1.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.13 | 4.00 | 7.07 | 0.00 | 44.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.93 | 18.00 | 30.18 | 2.00 | 90.0 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.04 | 13.99 | 23.50 | 0.00 | 119.8 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.84 | 7.29 | 12.24 | 0.00 | 46.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.37 | 29.57 | 48.29 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.70 | 19.47 | 32.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.58 | 15.66 | 25.51 | 3.00 | 84.2 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.66 | 15.20 | 23.47 | 5.00 | 83.2 | 76.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.8 | 2.40 | 7.20 | 11.81 | 1.00 | 64.8 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.47
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.75 | 10.63 | 17.18 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.08 | 0.46 | 1.00 | 0.00 | 4.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.64 | 17.19 | 27.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.74 | 11.24 | 17.93 | 1.00 | 87.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.23 | 9.31 | 15.08 | 1.00 | 88.1 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.52 | 7.47 | 12.07 | 1.00 | 85.7 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.38 | 2.05 | 4.06 | 0.00 | 22.0 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.22 | 18.32 | 30.02 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.38 | 15.76 | 25.35 | 5.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.18 | 4.49 | 8.97 | 0.00 | 19.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.26 | 30.07 | 48.94 | 14.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.22 | 18.62 | 30.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.04 | 16.87 | 26.41 | 14.00 | 88.2 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.22 | 13.14 | 20.38 | 2.00 | 66.1 | 72.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 2.42 | 7.59 | 12.10 | 7.00 | 72.8 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.23
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.45, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.18 | 9.81 | 16.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.38 | 0.88 | 1.50 | 0.00 | 9.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.80 | 16.36 | 27.05 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.83 | 11.05 | 18.03 | 4.00 | 87.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.36 | 10.04 | 16.45 | 0.00 | 81.9 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.89 | 4.02 | 7.29 | 0.00 | 40.9 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.23 | 1.68 | 3.42 | 1.00 | 19.8 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.49 | 17.58 | 28.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.77 | 15.24 | 25.99 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.72 | 4.31 | 8.30 | 0.00 | 17.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.75 | 29.76 | 48.88 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.14 | 19.30 | 31.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.88 | 17.75 | 28.15 | 5.00 | 89.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.78 | 11.78 | 18.79 | 10.00 | 62.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.52 | 8.99 | 14.34 | 3.00 | 73.9 | 89.0 |