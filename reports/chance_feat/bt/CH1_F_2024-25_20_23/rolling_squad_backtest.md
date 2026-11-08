# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.78
- Total actual points: 256.00
- Average predicted points: 70.95
- Average actual points: 64.00
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
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 73.44
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.72 | 17.38 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.07 | 0.63 | 1.01 | 0.00 | 10.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.69 | 23.32 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.70 | 12.94 | 20.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.56 | 19.97 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.91 | 6.02 | 9.42 | 1.00 | 74.5 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.23 | 8.00 | 1.00 | 59.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.73 | 21.42 | 34.13 | 7.00 | 89.7 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.83 | 13.89 | 21.47 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.74 | 45.03 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 21.90 | 36.08 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.65 | 15.62 | 25.15 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.11 | 14.67 | 22.99 | 7.00 | 80.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.74 | 10.95 | 17.90 | 1.00 | 81.1 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.23
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.90 | 10.65 | 17.29 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.30 | 0.73 | 1.24 | 0.00 | 10.6 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.25 | 12.70 | 19.67 | 6.00 | 83.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.46 | 11.56 | 19.07 | 2.00 | 70.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.86 | 11.19 | 18.00 | 7.00 | 81.9 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.15 | 6.16 | 9.91 | 0.00 | 75.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.75 | 8.90 | 1.00 | 68.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.47 | 19.87 | 31.70 | 16.00 | 78.1 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.47 | 10.97 | 17.27 | 9.00 | 65.4 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.23 | 26.05 | 42.62 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.55 | 35.48 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.38 | 16.09 | 25.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 16.01 | 25.13 | 9.00 | 86.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 9.63 | 15.76 | 2.00 | 75.2 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.55
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.46) beats the best remaining Bench Boost opportunity (3.73).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.46) beats the best remaining Bench Boost opportunity (3.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.30 | 11.46 | 18.19 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.30 | 0.70 | 1.18 | 0.00 | 10.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.15 | 12.46 | 20.86 | 11.00 | 79.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 11.99 | 19.38 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.27 | 17.81 | 4.00 | 79.4 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.75 | 9.12 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.23 | 3.71 | 6.39 | 0.00 | 44.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.81 | 21.39 | 34.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.41 | 16.95 | 26.44 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.34 | 43.00 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.40 | 22.03 | 36.46 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.00 | 15.09 | 25.21 | 2.00 | 89.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.81 | 14.86 | 23.22 | 2.00 | 74.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.83 | 9.22 | 15.60 | 0.00 | 64.4 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.56
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.86 | 9.01 | 14.73 | 1.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.19 | 0.60 | 1.12 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.91 | 16.35 | 25.74 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.91 | 18.85 | 2.00 | 77.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.18 | 11.33 | 18.48 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.54 | 2.67 | 4.66 | 6.00 | 40.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.83 | 2.52 | 4.77 | 1.00 | 33.5 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.82 | 20.90 | 33.73 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.37 | 13.55 | 21.50 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 25.73 | 41.71 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.98 | 19.47 | 33.12 | 2.00 | 87.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.28 | 15.90 | 26.38 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.73 | 23.61 | 5.00 | 79.1 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.05 | 5.04 | 9.64 | 2.00 | 28.8 | 90.0 |