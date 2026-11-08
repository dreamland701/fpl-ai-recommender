# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 300.92
- Total actual points: 358.00
- Average predicted points: 75.23
- Average actual points: 89.50
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 84.65
- Actual score: 125.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.08) beats the best remaining Bench Boost opportunity (15.86).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.08) beats the best remaining Bench Boost opportunity (15.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.96 | 12.51 | 19.21 | 10.00 | 131.4 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 2.85 | 8.71 | 14.24 | 8.00 | 82.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.54 | 16.86 | 26.19 | 7.00 | 117.9 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.95 | 12.13 | 19.11 | 6.00 | 104.7 | 180.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 4.33 | 10.80 | 16.50 | 7.00 | 120.6 | 177.0 |
| Bench 3 | Bench Boost | Antonee Robinson | DEF | 9 | 5.1 | 3.39 | 10.62 | 17.62 | 4.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Lewis Hall | DEF | 15 | 5.1 | 3.57 | 10.51 | 16.93 | 1.00 | 75.7 | 86.0 |
| XI | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 5.04 | 12.50 | 19.08 | 9.00 | 120.9 | 114.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.15 | 11.67 | 18.78 | 2.00 | 74.8 | 90.0 |
| Bench 4 | Bench Boost | Jamie Vardy | FWD | 11 | 5.4 | 3.16 | 8.85 | 14.43 | 1.00 | 66.5 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.78 | 26.36 | 43.00 | 29.00 | 131.4 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.89 | 19.86 | 33.09 | 6.00 | 100.3 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.95 | 16.74 | 27.19 | 2.00 | 94.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.87 | 14.01 | 21.98 | 2.00 | 94.5 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.42 | 12.70 | 20.61 | 2.00 | 86.4 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 85.46
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (9.28).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 2.81, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.72) beats the best remaining Triple Captain opportunity (9.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.09 | 12.13 | 18.95 | 3.00 | 111.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.07 | 9.31 | 15.19 | 3.00 | 85.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.33 | 16.75 | 26.93 | 13.00 | 117.6 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 6.33 | 15.87 | 24.63 | 2.00 | 148.0 | 180.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.83 | 11.28 | 17.50 | 2.00 | 107.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.65 | 10.98 | 18.01 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.1 | 2.50 | 8.48 | 14.45 | 0.00 | 67.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.91 | 11.79 | 19.08 | 2.00 | 71.9 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 2.99 | 9.63 | 15.52 | 0.00 | 67.4 | 0.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.4 | 2.29 | 7.51 | 12.55 | 2.00 | 61.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 11.35 | 30.63 | 49.75 | 20.00 | 175.8 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.56 | 19.49 | 32.28 | 2.00 | 95.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.38 | 15.86 | 25.67 | 3.00 | 83.2 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.64 | 15.38 | 23.61 | 5.00 | 90.4 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.68 | 13.58 | 20.41 | 4.00 | 120.7 | 180.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.89
- Actual score: 71.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.94 | 10.85 | 17.59 | 1.00 | 99.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.85 | 8.97 | 14.91 | 0.00 | 87.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.62 | 16.96 | 27.71 | 6.00 | 106.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.55 | 13.76 | 22.10 | 6.00 | 123.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.86 | 11.32 | 18.20 | 1.00 | 89.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.39 | 9.51 | 15.42 | 1.00 | 90.4 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 5.0 | 2.81 | 8.82 | 14.83 | 9.00 | 74.3 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.33 | 12.27 | 19.23 | 8.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.4 | 2.95 | 8.57 | 13.79 | 2.00 | 69.6 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.77 | 5.87 | 10.82 | 0.00 | 32.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 10.12 | 29.68 | 48.76 | 14.00 | 160.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.1 | 6.04 | 18.46 | 30.67 | 2.00 | 95.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.33 | 17.15 | 26.87 | 14.00 | 98.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.56 | 13.65 | 21.07 | 2.00 | 69.6 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.01 | 11.44 | 17.71 | 2.00 | 83.6 | 77.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.92
- Actual score: 64.00
- Transfer: Lewis Hall -> Daniel Muñoz (projected gain 2.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.46 | 10.18 | 16.55 | 2.00 | 95.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.68 | 8.40 | 14.18 | 6.00 | 87.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.40 | 16.12 | 26.50 | 6.00 | 99.4 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.10 | 12.40 | 20.23 | 7.00 | 106.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.92 | 11.06 | 17.96 | 4.00 | 90.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.58 | 10.52 | 17.10 | 0.00 | 87.5 | 18.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.01 | 8.90 | 14.48 | 6.00 | 86.9 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.93 | 11.03 | 17.46 | 9.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.4 | 2.99 | 8.71 | 13.96 | 2.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 1.07 | 4.83 | 9.16 | 0.00 | 21.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.67 | 28.45 | 47.19 | 6.00 | 143.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.07 | 19.33 | 31.53 | 3.00 | 103.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.27 | 17.98 | 28.56 | 5.00 | 97.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.85 | 11.82 | 18.87 | 10.00 | 63.6 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.62 | 8.04 | 14.09 | 7.00 | 59.5 | 90.0 |