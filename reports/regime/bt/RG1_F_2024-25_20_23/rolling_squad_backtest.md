# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.75
- Total actual points: 256.00
- Average predicted points: 70.94
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
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.76 | 17.44 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.13 | 0.78 | 1.23 | 0.00 | 8.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.45 | 14.81 | 23.56 | 0.00 | 89.6 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.70 | 12.95 | 20.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.54 | 12.55 | 19.97 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.92 | 6.10 | 9.59 | 1.00 | 76.0 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.20 | 7.96 | 1.00 | 60.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.74 | 21.45 | 34.19 | 7.00 | 89.4 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.78 | 13.68 | 21.07 | 8.00 | 89.3 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.31 | 27.93 | 45.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 21.98 | 36.24 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.62 | 15.56 | 25.05 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.12 | 14.72 | 23.07 | 7.00 | 80.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.70 | 10.78 | 17.59 | 1.00 | 79.7 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.33
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.69 | 17.35 | 2.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.36 | 0.88 | 1.48 | 0.00 | 8.3 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.26 | 12.73 | 19.73 | 6.00 | 83.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.50 | 11.75 | 19.46 | 2.00 | 71.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.86 | 11.23 | 18.08 | 7.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.18 | 6.28 | 10.14 | 0.00 | 77.0 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.07 | 5.73 | 8.87 | 1.00 | 69.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.48 | 19.95 | 31.87 | 16.00 | 78.2 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.43 | 10.86 | 17.09 | 9.00 | 64.8 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.29 | 26.31 | 43.15 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.59 | 35.55 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.36 | 16.07 | 25.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.45 | 16.04 | 25.18 | 9.00 | 85.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.15 | 9.51 | 15.54 | 2.00 | 74.0 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.47
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.52) beats the best remaining Bench Boost opportunity (3.82).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.52) beats the best remaining Bench Boost opportunity (3.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.30 | 11.45 | 18.14 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.36 | 0.85 | 1.42 | 0.00 | 8.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.18 | 12.61 | 21.16 | 11.00 | 81.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.01 | 19.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.29 | 17.85 | 4.00 | 79.8 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.91 | 5.72 | 9.09 | 0.00 | 73.8 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.26 | 3.85 | 6.66 | 0.00 | 45.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.78 | 21.32 | 33.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.34 | 16.67 | 25.92 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.10 | 26.66 | 43.62 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.30 | 21.20 | 34.79 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.98 | 15.05 | 25.15 | 2.00 | 89.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.93 | 23.36 | 2.00 | 74.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.70 | 8.26 | 13.68 | 0.00 | 60.2 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.52
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.87 | 9.07 | 14.81 | 1.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.24 | 0.74 | 1.35 | 0.00 | 7.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.95 | 16.47 | 25.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.90 | 18.82 | 2.00 | 78.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.18 | 11.39 | 18.60 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.54 | 2.67 | 4.68 | 6.00 | 41.6 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.85 | 2.63 | 5.00 | 1.00 | 35.1 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.79 | 20.80 | 33.55 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.32 | 13.39 | 21.22 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.40 | 26.06 | 42.34 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.89 | 18.66 | 31.51 | 2.00 | 85.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.25 | 15.82 | 26.22 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.75 | 23.66 | 5.00 | 79.4 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.94 | 4.12 | 7.81 | 2.00 | 25.1 | 90.0 |