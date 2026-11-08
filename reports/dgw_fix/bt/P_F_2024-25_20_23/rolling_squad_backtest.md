# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 279.21
- Total actual points: 229.00
- Average predicted points: 69.80
- Average actual points: 57.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.24
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 10.88 | 17.80 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.77 | 8.84 | 17.10 | 4.00 | 84.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.54 | 27.77 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.69 | 12.77 | 20.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.62 | 12.56 | 20.22 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.04 | 12.17 | 20.29 | 2.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.69 | 10.81 | 17.19 | 6.00 | 87.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.13 | 9.39 | 15.51 | 9.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.64 | 7.15 | 11.84 | 1.00 | 64.9 | 35.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.85 | 4.83 | 7.63 | 1.00 | 40.9 | 54.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 28.03 | 55.33 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.48 | 22.39 | 37.14 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.62 | 15.36 | 24.88 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.10 | 14.33 | 22.69 | 7.00 | 80.4 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.85 | 10.87 | 17.60 | 5.00 | 67.2 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.26
- Actual score: 48.00
- Transfer: João Pedro Junqueira de Jesus -> Raúl Jiménez (projected gain 1.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 10.87 | 17.73 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 3.19 | 9.48 | 18.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.27 | 12.28 | 19.08 | 6.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.17 | 11.63 | 19.22 | 2.00 | 86.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.43 | 11.40 | 26.29 | 2.00 | 69.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.92 | 11.22 | 18.17 | 7.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.36 | 10.14 | 16.17 | 2.00 | 80.9 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.43 | 11.51 | 17.66 | 1.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.17 | 6.31 | 10.77 | 1.00 | 57.8 | 17.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.85 | 4.82 | 7.38 | 1.00 | 44.7 | 7.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.29 | 60.47 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 22.05 | 36.51 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.35 | 15.75 | 25.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 15.50 | 24.56 | 9.00 | 86.1 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.53 | 10.59 | 16.87 | 3.00 | 69.9 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 74.09
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.95) beats the best remaining Bench Boost opportunity (11.02).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.95) beats the best remaining Bench Boost opportunity (11.02).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.0 | 3.21 | 11.79 | 17.18 | 2.00 | 86.1 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.29 | 11.48 | 18.21 | 1.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 16.56 | 29.13 | 11.00 | 78.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.79 | 12.42 | 19.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.53 | 12.14 | 19.56 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.89 | 11.20 | 18.53 | 0.00 | 86.5 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 10.95 | 17.22 | 4.00 | 79.6 | 65.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.94 | 9.66 | 15.28 | 2.00 | 56.9 | 70.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.55 | 5.28 | 9.10 | 1.00 | 49.4 | 57.0 |
| Bench 4 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 1.02 | 3.61 | 5.78 | 5.00 | 28.5 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.06 | 35.70 | 61.39 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.86 | 23.03 | 37.78 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.97 | 14.89 | 24.80 | 2.00 | 89.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.81 | 14.35 | 22.48 | 2.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.18 | 9.58 | 15.91 | 2.00 | 65.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.63
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Virgil van Dijk (projected gain 10.50, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.96 | 11.79 | 17.46 | 5.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 2.85 | 9.00 | 14.53 | 1.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.93 | 27.13 | 35.84 | 5.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.27 | 19.28 | 25.62 | 2.00 | 81.8 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.63 | 11.72 | 18.56 | 2.00 | 78.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.22 | 11.59 | 18.93 | 2.00 | 84.7 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.87 | 11.22 | 17.92 | 1.00 | 90.0 | 78.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.37 | 8.86 | 14.45 | 2.00 | 50.7 | 63.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.94 | 6.13 | 10.32 | 1.00 | 59.3 | 59.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.03 | 8.06 | 2.00 | 37.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.37 | 43.70 | 59.67 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.45 | 20.47 | 34.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.32 | 15.82 | 26.05 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.56 | 23.43 | 5.00 | 79.0 | 87.0 |
| Bench 2 | Bench | Jacob Murphy | MID | 15 | 5.1 | 3.62 | 9.00 | 15.27 | 6.00 | 61.7 | 90.0 |