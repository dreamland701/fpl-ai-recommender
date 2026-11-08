# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 286.48
- Total actual points: 256.00
- Average predicted points: 71.62
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
- Predicted score: 73.96
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.83 | 10.98 | 17.63 | 3.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.09 | 0.56 | 0.97 | 0.00 | 9.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.48 | 14.49 | 22.82 | 0.00 | 87.8 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.61 | 12.54 | 20.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.43 | 11.85 | 19.31 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.97 | 5.80 | 9.06 | 1.00 | 74.0 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.82 | 5.01 | 7.61 | 1.00 | 59.3 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.90 | 21.15 | 33.95 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.94 | 14.03 | 21.30 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.30 | 27.66 | 45.40 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 21.98 | 35.83 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.63 | 15.22 | 24.46 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.26 | 14.67 | 23.07 | 7.00 | 83.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.87 | 11.12 | 18.40 | 1.00 | 84.2 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.29
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.61 | 17.21 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.29 | 0.70 | 1.16 | 0.00 | 9.7 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.44 | 12.77 | 19.67 | 6.00 | 88.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.62 | 11.67 | 19.27 | 2.00 | 71.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.96 | 11.02 | 18.14 | 7.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.22 | 6.16 | 9.86 | 0.00 | 74.9 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.06 | 5.54 | 8.40 | 1.00 | 68.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.69 | 20.37 | 32.75 | 16.00 | 82.4 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.70 | 11.23 | 17.38 | 9.00 | 68.5 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.24 | 25.92 | 42.60 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.34 | 22.14 | 36.25 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.45 | 16.08 | 25.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.55 | 15.91 | 25.02 | 9.00 | 89.4 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.25 | 9.90 | 16.46 | 2.00 | 77.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.94
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.69).
- Transfer: David Raya Martin -> Matz Sels (projected gain 0.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.15 | 10.96 | 17.32 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.28 | 0.66 | 1.02 | 0.00 | 9.4 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.65 | 12.54 | 20.06 | 8.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.12 | 12.36 | 20.73 | 11.00 | 79.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.92 | 11.35 | 17.68 | 4.00 | 84.6 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.91 | 5.55 | 8.51 | 0.00 | 72.9 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.22 | 3.72 | 6.60 | 0.00 | 42.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.97 | 22.11 | 35.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.18 | 16.50 | 25.89 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.08 | 26.57 | 43.39 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.29 | 21.54 | 35.19 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.09 | 15.19 | 25.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.06 | 14.76 | 22.83 | 2.00 | 78.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.95 | 8.78 | 14.56 | 0.00 | 65.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 76.29
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.34) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.34) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.99 | 9.15 | 14.59 | 1.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.17 | 0.52 | 0.92 | 0.00 | 8.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.00 | 16.43 | 25.56 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.88 | 12.48 | 19.45 | 2.00 | 80.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.18 | 11.60 | 19.01 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.82 | 2.51 | 4.81 | 1.00 | 32.1 | 3.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.54 | 2.38 | 4.07 | 6.00 | 38.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.91 | 21.42 | 34.71 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.65 | 13.81 | 21.69 | 2.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.34 | 26.21 | 42.16 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.87 | 19.02 | 31.89 | 2.00 | 83.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.13 | 15.42 | 25.90 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.57 | 14.60 | 23.56 | 5.00 | 80.0 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.10 | 4.52 | 8.62 | 2.00 | 28.1 | 90.0 |