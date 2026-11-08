# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.39
- Total actual points: 336.00
- Average predicted points: 91.60
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
- Predicted score: 112.73
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (14.31).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.53) beats the best remaining Bench Boost opportunity (14.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.46 | 12.12 | 18.58 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.62 | 1.12 | 0.00 | 4.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.22 | 16.99 | 26.50 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.44 | 10.65 | 17.64 | 4.00 | 84.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.39 | 10.54 | 16.11 | 7.00 | 178.3 | 177.0 |
| Bench 2 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.99 | 8.25 | 13.17 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.49 | 6.89 | 11.12 | 1.00 | 80.0 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.71 | 19.68 | 32.61 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.43 | 18.38 | 27.70 | 7.00 | 169.0 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.41 | 11.99 | 18.24 | 9.00 | 168.6 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.92 | 26.52 | 43.19 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.35 | 19.72 | 33.23 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.05 | 16.72 | 27.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.00 | 13.19 | 20.81 | 2.00 | 89.4 | 90.0 |
| Bench 3 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.87 | 7.39 | 12.49 | 4.00 | 63.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.66
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.48) beats the best remaining Triple Captain opportunity (11.59).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.48) beats the best remaining Triple Captain opportunity (11.59).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.79 | 11.51 | 18.03 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.30 | 0.73 | 1.18 | 0.00 | 4.5 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.26 | 16.27 | 26.44 | 13.00 | 178.8 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.10 | 18.18 | 2.00 | 87.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.49 | 10.69 | 16.65 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.34 | 7.10 | 11.70 | 1.00 | 86.3 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.45 | 4.72 | 7.99 | 0.00 | 53.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.77 | 17.59 | 29.66 | 2.00 | 89.4 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.95 | 14.81 | 22.88 | 0.00 | 132.6 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.12 | 7.78 | 12.72 | 0.00 | 53.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.46 | 29.71 | 48.71 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.73 | 19.51 | 32.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.52 | 15.56 | 25.54 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.66 | 15.22 | 23.58 | 5.00 | 83.7 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.40 | 7.11 | 11.52 | 1.00 | 64.5 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.10
- Actual score: 74.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.72 | 10.54 | 17.08 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.47 | 0.95 | 1.44 | 0.00 | 4.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.65 | 17.23 | 28.00 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.69 | 11.13 | 17.86 | 1.00 | 87.7 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.19 | 9.24 | 15.04 | 1.00 | 88.6 | 90.0 |
| XI | XI | Jan Bednarek | DEF | 17 | 4.0 | 2.44 | 7.33 | 11.96 | 1.00 | 86.0 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.67 | 2.72 | 4.92 | 0.00 | 29.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.06 | 17.88 | 29.44 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.23 | 15.34 | 24.79 | 5.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.37 | 4.81 | 9.22 | 0.00 | 25.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.35 | 30.26 | 49.36 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.14 | 18.45 | 30.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.11 | 17.02 | 26.55 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.17 | 13.03 | 20.30 | 2.00 | 65.5 | 72.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 2.35 | 7.38 | 11.80 | 7.00 | 70.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.90
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.49, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.26 | 9.94 | 16.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.28 | 0.66 | 1.04 | 0.00 | 3.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.88 | 16.52 | 27.22 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.90 | 11.19 | 18.13 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.40 | 10.10 | 16.43 | 0.00 | 84.7 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.90 | 4.07 | 7.32 | 0.00 | 42.4 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.21 | 1.70 | 3.45 | 1.00 | 19.7 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.45 | 17.38 | 28.45 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.73 | 14.99 | 25.43 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.61 | 3.97 | 7.69 | 0.00 | 15.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.88 | 30.02 | 49.20 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.40 | 31.68 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.97 | 17.92 | 28.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.77 | 11.67 | 18.49 | 10.00 | 63.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.57 | 9.03 | 14.23 | 3.00 | 75.4 | 89.0 |