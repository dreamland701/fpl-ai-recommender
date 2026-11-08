# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 284.93
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
- Predicted score: 73.62
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 10.90 | 17.56 | 3.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.13 | 0.77 | 1.27 | 0.00 | 7.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.46 | 14.64 | 23.18 | 0.00 | 89.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.67 | 12.76 | 20.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.46 | 12.13 | 19.53 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.93 | 5.90 | 9.22 | 1.00 | 75.4 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.83 | 5.07 | 7.71 | 1.00 | 60.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.83 | 21.30 | 34.07 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.86 | 13.76 | 20.98 | 8.00 | 89.9 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 27.88 | 45.56 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.96 | 35.99 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.59 | 15.26 | 24.55 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.21 | 14.73 | 23.11 | 7.00 | 82.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.80 | 10.99 | 18.07 | 1.00 | 81.8 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.73
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.87 | 10.67 | 17.28 | 2.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.35 | 0.91 | 1.50 | 0.00 | 8.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.36 | 12.73 | 19.66 | 6.00 | 86.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.54 | 11.68 | 19.30 | 2.00 | 72.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.90 | 11.06 | 18.02 | 7.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.19 | 6.19 | 9.93 | 0.00 | 76.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.06 | 5.61 | 8.55 | 1.00 | 69.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.62 | 20.24 | 32.42 | 16.00 | 80.6 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.52 | 10.83 | 16.86 | 9.00 | 66.3 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.24 | 26.20 | 43.07 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.32 | 21.87 | 35.86 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.52 | 15.98 | 25.11 | 9.00 | 87.9 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.38 | 15.97 | 25.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.23 | 9.76 | 16.06 | 2.00 | 75.5 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.70
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.47) beats the best remaining Bench Boost opportunity (3.75).
- Transfer: David Raya Martin -> Matz Sels (projected gain 0.98, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.47) beats the best remaining Bench Boost opportunity (3.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.25 | 11.22 | 17.76 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.35 | 0.85 | 1.39 | 0.00 | 7.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.13 | 12.44 | 20.86 | 11.00 | 81.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.58 | 12.25 | 19.70 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.85 | 11.26 | 17.67 | 4.00 | 82.5 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.90 | 5.57 | 8.67 | 0.00 | 73.8 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.23 | 3.77 | 6.61 | 0.00 | 45.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.90 | 21.79 | 34.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.24 | 16.44 | 25.59 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.09 | 26.74 | 43.71 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.27 | 21.36 | 34.93 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.03 | 15.09 | 25.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.92 | 14.77 | 23.02 | 2.00 | 76.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.86 | 8.59 | 14.20 | 0.00 | 62.5 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.88
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.38) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.38) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.94 | 9.11 | 14.68 | 1.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.23 | 0.74 | 1.31 | 0.00 | 7.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.98 | 16.43 | 25.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.76 | 12.17 | 19.12 | 2.00 | 80.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.16 | 11.44 | 18.72 | 2.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.81 | 2.53 | 4.86 | 1.00 | 34.3 | 3.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.53 | 2.43 | 4.24 | 6.00 | 40.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.86 | 21.15 | 34.15 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.42 | 13.34 | 21.02 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.38 | 26.25 | 42.47 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.86 | 18.83 | 31.63 | 2.00 | 83.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.18 | 15.59 | 26.05 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.53 | 14.65 | 23.59 | 5.00 | 79.9 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.04 | 4.36 | 8.27 | 2.00 | 26.3 | 90.0 |