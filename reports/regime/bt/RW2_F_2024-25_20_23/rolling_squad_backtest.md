# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 284.92
- Total actual points: 256.00
- Average predicted points: 71.23
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
- Predicted score: 73.66
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.79 | 10.88 | 17.54 | 3.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.07 | 0.57 | 0.92 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.45 | 14.58 | 23.04 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.68 | 12.77 | 20.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.48 | 12.18 | 19.62 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.93 | 5.88 | 9.18 | 1.00 | 74.1 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.83 | 5.08 | 7.71 | 1.00 | 58.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.82 | 21.31 | 34.09 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.90 | 13.92 | 21.28 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.26 | 27.77 | 45.35 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.94 | 35.95 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.61 | 15.34 | 24.70 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.21 | 14.72 | 23.09 | 7.00 | 82.9 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.83 | 11.13 | 18.33 | 1.00 | 83.0 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.74
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.86 | 10.65 | 17.28 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.29 | 0.69 | 1.14 | 0.00 | 10.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.36 | 12.72 | 19.64 | 6.00 | 86.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.52 | 11.61 | 19.15 | 2.00 | 71.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.91 | 11.11 | 18.10 | 7.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.19 | 6.17 | 9.87 | 0.00 | 75.1 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.07 | 5.63 | 8.59 | 1.00 | 68.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.62 | 20.24 | 32.43 | 16.00 | 80.5 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.56 | 11.02 | 17.21 | 9.00 | 67.3 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.04 | 42.75 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.33 | 21.89 | 35.90 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.07 | 25.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.52 | 15.97 | 25.10 | 9.00 | 88.2 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.26 | 9.88 | 16.31 | 2.00 | 76.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.67
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.43) beats the best remaining Bench Boost opportunity (3.70).
- Transfer: David Raya Martin -> Matz Sels (projected gain 0.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.43) beats the best remaining Bench Boost opportunity (3.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.23 | 11.19 | 17.74 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.28 | 0.64 | 1.03 | 0.00 | 9.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.12 | 12.40 | 20.74 | 11.00 | 79.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.59 | 12.29 | 19.77 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.85 | 11.28 | 17.71 | 4.00 | 82.1 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.63 | 8.75 | 0.00 | 72.6 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.23 | 3.75 | 6.56 | 0.00 | 43.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.92 | 21.90 | 34.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.29 | 16.65 | 26.00 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.05 | 26.53 | 43.30 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.27 | 21.35 | 34.90 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.05 | 15.17 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.92 | 14.77 | 23.03 | 2.00 | 77.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.87 | 8.64 | 14.32 | 0.00 | 64.0 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.84
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.34) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.34) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.92 | 9.06 | 14.64 | 1.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.17 | 0.52 | 0.95 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.96 | 16.35 | 25.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.76 | 12.20 | 19.17 | 2.00 | 79.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.17 | 11.48 | 18.78 | 2.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.82 | 2.51 | 4.80 | 1.00 | 33.0 | 3.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.49 | 4.32 | 6.00 | 39.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.89 | 21.27 | 34.36 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.47 | 13.56 | 21.43 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.34 | 26.03 | 42.02 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.86 | 18.82 | 31.60 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.20 | 15.68 | 26.21 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.54 | 14.68 | 23.63 | 5.00 | 79.8 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.05 | 4.42 | 8.40 | 2.00 | 27.6 | 90.0 |