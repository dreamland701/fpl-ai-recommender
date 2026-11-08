# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 366.26
- Total actual points: 342.00
- Average predicted points: 91.57
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
- Predicted score: 112.47
- Actual score: 120.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.34) beats the best remaining Bench Boost opportunity (14.06).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.34) beats the best remaining Bench Boost opportunity (14.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.70 | 12.40 | 19.06 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.43 | 0.83 | 0.00 | 7.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.14 | 16.62 | 25.75 | 7.00 | 180.0 | 98.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.56 | 10.94 | 18.12 | 4.00 | 86.5 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.52 | 10.59 | 16.13 | 7.00 | 180.0 | 177.0 |
| Bench 3 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 2.85 | 7.70 | 12.18 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 2.39 | 6.56 | 10.53 | 1.00 | 76.3 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.78 | 19.84 | 32.91 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | 12 | 7.6 | 11.41 | 18.27 | 27.47 | 7.00 | 170.2 | 137.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.25 | 11.56 | 17.42 | 9.00 | 162.3 | 114.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 16.69 | 25.95 | 42.11 | 29.00 | 180.0 | 177.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.35 | 19.63 | 33.04 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.07 | 16.70 | 27.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.08 | 13.22 | 20.80 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.8 | 2.99 | 7.74 | 13.10 | 4.00 | 67.0 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 117.28
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (23.21) beats the best remaining Triple Captain opportunity (11.44).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (23.21) beats the best remaining Triple Captain opportunity (11.44).
- Autosub: Jan Bednarek replaced Cody Gakpo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.89 | 11.71 | 18.37 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.53 | 0.87 | 0.00 | 7.0 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.11 | 15.81 | 25.50 | 13.00 | 173.3 | 128.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.84 | 11.39 | 18.66 | 2.00 | 89.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.53 | 10.68 | 16.57 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 6.55 | 10.71 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 1.34 | 4.38 | 7.39 | 0.00 | 50.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.84 | 17.72 | 29.87 | 2.00 | 89.2 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | 12 | 7.6 | 8.96 | 14.71 | 22.64 | 0.00 | 134.7 | 0.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.02 | 7.31 | 11.85 | 0.00 | 50.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 20.19 | 29.01 | 47.40 | 20.00 | 180.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.74 | 19.40 | 32.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.53 | 15.57 | 25.53 | 3.00 | 83.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.74 | 15.33 | 23.72 | 5.00 | 85.2 | 76.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.8 | 2.54 | 7.50 | 12.19 | 1.00 | 68.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.27
- Actual score: 80.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 8.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.81 | 10.76 | 17.47 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.73 | 1.11 | 0.00 | 7.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.53 | 16.59 | 26.79 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.80 | 11.44 | 18.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.23 | 9.26 | 15.02 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.31 | 6.81 | 11.01 | 1.00 | 80.0 | 11.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.57 | 2.44 | 4.45 | 0.00 | 26.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.14 | 18.01 | 29.61 | 13.00 | 90.0 | 86.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.34 | 15.65 | 25.30 | 5.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.28 | 4.37 | 8.41 | 0.00 | 21.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.19 | 29.50 | 47.95 | 14.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.15 | 18.41 | 30.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.13 | 17.00 | 26.49 | 14.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.27 | 13.23 | 20.59 | 2.00 | 67.6 | 72.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 2.48 | 7.78 | 12.48 | 7.00 | 74.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.25
- Actual score: 48.00
- Transfer: Vitalii Mykolenko -> Daniel Muñoz (projected gain 2.56, hit 0)
- Autosub: Taylor Harwood-Bellis replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.35 | 10.19 | 16.59 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.19 | 0.43 | 0.73 | 0.00 | 5.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.77 | 15.95 | 26.11 | 6.00 | 90.0 | 76.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.96 | 11.31 | 18.30 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.53 | 10.49 | 17.07 | 0.00 | 87.2 | 18.0 |
| Bench 2 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.74 | 3.49 | 6.27 | 0.00 | 36.7 | 0.0 |
| Bench 4 | Autosub In | Taylor Harwood-Bellis | DEF | 17 | 4.0 | 0.11 | 1.41 | 2.95 | 1.00 | 16.9 | 45.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.55 | 17.59 | 28.74 | 0.00 | 90.0 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.84 | 15.25 | 25.80 | 2.00 | 90.0 | 84.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.54 | 3.63 | 7.03 | 0.00 | 11.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.74 | 29.31 | 47.86 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.22 | 19.36 | 31.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.99 | 17.88 | 28.18 | 5.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.85 | 11.80 | 18.61 | 10.00 | 64.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.71 | 9.42 | 14.89 | 3.00 | 79.0 | 89.0 |