# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 287.89
- Total actual points: 236.00
- Average predicted points: 71.97
- Average actual points: 59.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 146484
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.49
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.71 | 10.85 | 17.61 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.48 | 9.96 | 15.83 | 9.00 | 95.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.52 | 14.69 | 23.32 | 0.00 | 91.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.81 | 12.94 | 20.61 | 2.00 | 93.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.77 | 12.74 | 20.26 | 1.00 | 98.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.13 | 12.58 | 20.86 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.86 | 11.13 | 17.54 | 6.00 | 92.3 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.06 | 10.56 | 16.48 | 13.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 3.07 | 8.58 | 14.04 | 1.00 | 48.2 | 35.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.63 | 6.98 | 11.01 | 1.00 | 29.5 | 54.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.83 | 45.19 | 7.00 | 113.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.39 | 22.12 | 36.44 | 10.00 | 104.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.72 | 15.58 | 25.09 | 19.00 | 100.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.54 | 15.45 | 24.22 | 7.00 | 86.5 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 4.31 | 12.38 | 20.18 | 5.00 | 73.5 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.28
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.90 | 10.87 | 17.68 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.85 | 9.22 | 15.06 | 3.00 | 85.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.67 | 13.26 | 20.54 | 6.00 | 92.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.68 | 12.26 | 20.27 | 2.00 | 75.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.26 | 11.93 | 19.68 | 2.00 | 89.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.97 | 11.49 | 18.49 | 7.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.50 | 10.75 | 17.14 | 2.00 | 82.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.95 | 13.09 | 19.70 | 1.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.66 | 7.99 | 13.70 | 1.00 | 46.9 | 17.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.57 | 6.96 | 10.76 | 1.00 | 33.2 | 7.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.26 | 26.06 | 42.65 | 2.00 | 109.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.31 | 21.74 | 35.79 | 10.00 | 111.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.06 | 25.94 | 2.00 | 97.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.75 | 16.01 | 25.13 | 9.00 | 90.1 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.86 | 11.83 | 18.96 | 3.00 | 75.0 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 77.88
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.07) beats the best remaining Bench Boost opportunity (11.77).
- Transfer: Jacob Murphy -> Anthony Elanga (projected gain 0.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.07) beats the best remaining Bench Boost opportunity (11.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.36 | 11.45 | 18.18 | 1.00 | 98.1 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.62 | 10.43 | 17.21 | 1.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.34 | 13.10 | 21.96 | 11.00 | 82.8 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.85 | 12.48 | 19.71 | 4.00 | 96.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.22 | 12.06 | 19.07 | 4.00 | 85.9 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 12.05 | 19.50 | 8.00 | 90.6 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.3 | 3.97 | 11.53 | 19.11 | 0.00 | 90.1 | 0.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.64 | 11.62 | 18.61 | 2.00 | 65.9 | 70.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.47 | 5.27 | 9.21 | 1.00 | 48.0 | 57.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 1.01 | 3.93 | 6.32 | 5.00 | 28.5 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.47 | 43.21 | 3.00 | 103.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.68 | 22.54 | 36.84 | 2.00 | 109.7 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.33 | 15.90 | 24.88 | 2.00 | 75.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.99 | 15.07 | 25.20 | 2.00 | 69.9 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 4.83 | 12.35 | 19.50 | 2.00 | 83.5 | 73.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.24
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.51 | 10.17 | 16.80 | 9.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.95 | 9.32 | 15.27 | 1.00 | 85.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.07 | 16.38 | 25.79 | 5.00 | 99.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 5.15 | 13.04 | 20.62 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.16 | 11.47 | 18.71 | 2.00 | 84.1 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.92 | 11.42 | 18.26 | 1.00 | 92.9 | 78.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.2 | 1.78 | 7.33 | 14.11 | 9.00 | 16.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 3.96 | 10.78 | 17.82 | 2.00 | 58.5 | 63.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.28 | 7.51 | 12.82 | 1.00 | 56.5 | 59.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.31 | 7.43 | 12.06 | 2.00 | 25.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.89 | 41.96 | 8.00 | 103.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.29 | 19.98 | 33.53 | 2.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.42 | 16.00 | 26.55 | 7.00 | 98.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.76 | 15.44 | 24.77 | 5.00 | 76.9 | 87.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 3.12 | 10.13 | 16.65 | 2.00 | 43.5 | 90.0 |