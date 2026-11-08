# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 272.45
- Total actual points: 381.00
- Average predicted points: 68.11
- Average actual points: 95.25
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
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 82.43
- Actual score: 161.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.91) beats the best remaining Triple Captain opportunity (12.21).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (11.91) beats the best remaining Triple Captain opportunity (12.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.58 | 17.47 | 25.95 | 10.00 | 176.9 | 180.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.12 | 10.80 | 20.10 | 8.00 | 85.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 7.18 | 14.11 | 22.78 | 7.00 | 165.5 | 177.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 7.64 | 13.42 | 19.91 | 7.00 | 160.3 | 98.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 5.63 | 12.17 | 20.25 | 17.00 | 161.3 | 180.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 2.79 | 11.24 | 17.62 | 2.00 | 82.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.24 | 11.07 | 16.99 | 11.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.0 | 3.21 | 12.69 | 21.46 | 17.00 | 70.6 | 81.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 5.20 | 10.38 | 17.43 | 2.00 | 84.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 3.29 | 7.70 | 11.55 | 7.00 | 66.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.79 | 21.27 | 35.59 | 6.00 | 82.5 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.09 | 16.46 | 29.14 | 29.00 | 152.0 | 177.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.97 | 16.05 | 24.98 | 5.00 | 151.5 | 177.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.63 | 14.54 | 20.42 | 2.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 5.8 | 2.99 | 14.37 | 25.56 | 2.00 | 80.7 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Emiliano Martínez Romero
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 80.37
- Actual score: 107.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.33) beats the best remaining Bench Boost opportunity (13.94).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Jordan Pickford -> Emiliano Martínez Romero (projected gain 7.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.33) beats the best remaining Bench Boost opportunity (13.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 6.90 | 15.49 | 21.96 | 4.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 3.36 | 8.20 | 15.48 | 3.00 | 88.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.70 | 13.72 | 21.77 | 13.00 | 131.5 | 128.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.18 | 11.46 | 18.15 | 6.00 | 84.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.61 | 10.79 | 16.66 | 2.00 | 87.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.65 | 10.28 | 17.94 | 1.00 | 85.3 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.94 | 8.07 | 15.38 | 2.00 | 85.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.0 | 4.90 | 14.40 | 22.93 | 9.00 | 80.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.67 | 11.93 | 17.93 | 2.00 | 83.0 | 90.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.90 | 7.61 | 13.04 | 5.00 | 75.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.58 | 21.21 | 35.53 | 20.00 | 156.0 | 180.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 5.62 | 19.32 | 33.86 | 2.00 | 80.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 6.63 | 15.69 | 24.36 | 13.00 | 129.4 | 79.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.61 | 15.65 | 22.26 | 5.00 | 80.3 | 76.0 |
| Bench 2 | Bench Boost | Amad Diallo | MID | 14 | 5.6 | 3.56 | 10.85 | 15.40 | 0.00 | 78.3 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.10 -> 1.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 51.54
- Actual score: 55.00
- Transfer: Luis Díaz -> Mathys Tel (projected gain 4.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.84 | 12.21 | 18.01 | 3.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.16 | 10.87 | 18.43 | 0.00 | 88.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.06 | 11.73 | 17.09 | 2.00 | 84.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 3.55 | 10.16 | 16.74 | 1.00 | 85.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.42 | 10.12 | 16.55 | 13.00 | 87.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.70 | 9.86 | 15.08 | 1.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 3.41 | 8.87 | 17.99 | 6.00 | 70.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.0 | 4.29 | 13.98 | 17.90 | 5.00 | 86.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.73 | 12.72 | 18.62 | 8.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 3.10 | 8.30 | 14.09 | 1.00 | 75.2 | 18.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 5.19 | 21.59 | 33.62 | 2.00 | 86.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.7 | 4.83 | 17.89 | 28.53 | 14.00 | 86.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.13 | 15.76 | 23.39 | 2.00 | 79.3 | 72.0 |
| XI | XI | Mathys Tel | MID | 18 | 6.0 | 3.61 | 13.46 | 17.00 | 2.00 | 77.0 | 73.0 |
| Bench 4 | Bench | Amad Diallo | MID | 14 | 5.5 | 1.98 | 9.33 | 11.79 | 0.00 | 27.8 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 1.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.11
- Actual score: 58.00
- Transfer: Amad Diallo -> Eberechi Eze (projected gain 5.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.73 | 10.09 | 15.30 | 6.00 | 88.7 | 90.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.51 | 9.24 | 15.90 | 1.00 | 85.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.14 | 12.07 | 16.67 | 7.00 | 83.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.8 | 3.61 | 10.52 | 15.92 | 4.00 | 88.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.32 | 10.30 | 21.65 | 6.00 | 83.7 | 76.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.8 | 2.81 | 8.83 | 15.86 | 2.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.51 | 8.53 | 15.14 | 6.00 | 82.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 3.69 | 15.35 | 23.95 | 2.00 | 79.4 | 84.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.31 | 10.83 | 18.83 | 9.00 | 85.6 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.92 | 6.25 | 11.66 | 0.00 | 44.5 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.61 | 22.06 | 40.61 | 3.00 | 83.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.7 | 7.39 | 18.40 | 26.67 | 6.00 | 85.9 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.7 | 4.09 | 13.47 | 20.64 | 5.00 | 75.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.03 | 12.06 | 20.01 | 10.00 | 69.5 | 90.0 |
| Bench 2 | Bench | Mathys Tel | MID | 18 | 6.0 | 2.78 | 7.83 | 10.54 | 2.00 | 51.0 | 65.0 |