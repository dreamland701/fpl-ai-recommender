# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 260.38
- Total actual points: 236.00
- Average predicted points: 65.09
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
- Predicted score: 63.35
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.28 | 9.60 | 15.60 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.14 | 9.01 | 14.32 | 9.00 | 94.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.00 | 13.31 | 21.15 | 0.00 | 90.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.50 | 12.05 | 19.21 | 2.00 | 90.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.28 | 11.40 | 18.13 | 1.00 | 98.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.69 | 11.27 | 18.72 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.54 | 10.21 | 16.09 | 6.00 | 90.3 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 3.62 | 9.44 | 14.72 | 13.00 | 63.2 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.76 | 7.68 | 12.55 | 1.00 | 65.2 | 35.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.35 | 6.22 | 9.76 | 1.00 | 41.5 | 54.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.18 | 24.96 | 40.73 | 7.00 | 114.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.63 | 19.86 | 32.80 | 10.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.19 | 14.11 | 22.76 | 19.00 | 100.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.98 | 13.85 | 21.71 | 7.00 | 82.5 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.82 | 10.95 | 17.86 | 5.00 | 65.5 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.81
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.40 | 9.49 | 15.48 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.47 | 8.03 | 13.13 | 3.00 | 83.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.28 | 12.14 | 18.80 | 6.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.18 | 10.67 | 17.67 | 2.00 | 70.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.77 | 10.57 | 17.49 | 2.00 | 86.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.45 | 10.00 | 16.09 | 7.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.04 | 9.35 | 14.92 | 2.00 | 80.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.39 | 11.62 | 17.47 | 1.00 | 75.7 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.37 | 7.07 | 12.07 | 1.00 | 56.9 | 17.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.28 | 6.13 | 9.44 | 1.00 | 46.2 | 7.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.20 | 23.02 | 37.84 | 2.00 | 110.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.43 | 19.24 | 31.76 | 10.00 | 112.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.47 | 15.22 | 23.86 | 9.00 | 91.1 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.69 | 14.03 | 22.75 | 2.00 | 98.1 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.35 | 10.32 | 16.55 | 3.00 | 69.0 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.45
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (10.98).
- Transfer: Jacob Murphy -> Anthony Elanga (projected gain 0.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (10.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.11 | 10.76 | 17.08 | 1.00 | 96.1 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.29 | 9.47 | 15.65 | 1.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.95 | 11.93 | 20.02 | 11.00 | 78.8 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.60 | 11.82 | 18.65 | 4.00 | 93.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.86 | 11.05 | 17.46 | 4.00 | 80.9 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.10 | 10.90 | 17.67 | 8.00 | 91.6 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.3 | 3.63 | 10.57 | 17.55 | 0.00 | 86.1 | 0.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 4.15 | 10.41 | 16.67 | 2.00 | 57.9 | 70.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.47 | 5.27 | 9.21 | 1.00 | 48.0 | 57.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 1.01 | 3.93 | 6.32 | 5.00 | 28.5 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.26 | 24.27 | 39.74 | 3.00 | 106.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.01 | 20.66 | 33.84 | 2.00 | 110.7 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.85 | 14.49 | 22.67 | 2.00 | 76.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.49 | 13.61 | 22.86 | 2.00 | 89.9 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 4.42 | 11.30 | 17.85 | 2.00 | 77.5 | 73.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.76
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.19 | 9.24 | 15.29 | 9.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.68 | 8.47 | 13.88 | 1.00 | 82.9 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.72 | 15.39 | 24.23 | 5.00 | 100.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.73 | 11.97 | 18.93 | 2.00 | 78.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.60 | 10.51 | 16.82 | 1.00 | 91.9 | 78.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.74 | 10.33 | 16.93 | 2.00 | 84.1 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.2 | 1.79 | 6.87 | 12.87 | 9.00 | 31.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 3.50 | 9.50 | 15.68 | 2.00 | 49.5 | 63.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.20 | 6.88 | 11.00 | 2.00 | 36.3 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.09 | 6.81 | 11.56 | 1.00 | 57.5 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.54 | 23.77 | 38.62 | 8.00 | 104.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.70 | 18.22 | 30.68 | 2.00 | 97.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.90 | 14.57 | 24.25 | 7.00 | 100.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.25 | 14.07 | 22.58 | 5.00 | 77.9 | 87.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 2.82 | 9.11 | 14.95 | 2.00 | 55.5 | 90.0 |