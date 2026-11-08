# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 287.94
- Total actual points: 256.00
- Average predicted points: 71.99
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
- Predicted score: 74.72
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.73 | 17.43 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.09 | 0.22 | 0.00 | 4.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.52 | 14.69 | 23.32 | 0.00 | 90.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.81 | 12.94 | 20.61 | 2.00 | 90.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.77 | 12.74 | 20.26 | 1.00 | 98.4 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.92 | 5.98 | 9.38 | 1.00 | 75.4 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.84 | 5.09 | 7.76 | 1.00 | 58.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 8.08 | 21.76 | 34.68 | 7.00 | 95.1 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 5.26 | 14.00 | 21.62 | 8.00 | 99.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.19 | 0.58 | 1.03 | 0.00 | 5.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.83 | 45.19 | 7.00 | 114.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.39 | 22.12 | 36.44 | 10.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.72 | 15.58 | 25.09 | 19.00 | 100.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.25 | 14.65 | 22.97 | 7.00 | 82.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.72 | 10.90 | 17.84 | 1.00 | 80.3 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.01
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.65 | 17.32 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.37 | 0.65 | 0.00 | 5.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.50 | 12.76 | 19.77 | 6.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.46 | 11.53 | 19.05 | 2.00 | 70.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.92 | 11.36 | 18.29 | 7.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.17 | 6.17 | 9.94 | 0.00 | 76.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.13 | 5.73 | 8.87 | 1.00 | 69.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.68 | 20.14 | 32.17 | 16.00 | 81.4 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.53 | 11.04 | 17.44 | 9.00 | 66.4 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.08 | 0.54 | 0.93 | 0.00 | 5.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.26 | 26.06 | 42.65 | 2.00 | 110.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.31 | 21.74 | 35.79 | 10.00 | 112.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.06 | 25.94 | 2.00 | 98.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.75 | 16.01 | 25.13 | 9.00 | 91.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.11 | 9.61 | 15.75 | 2.00 | 73.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.64
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.06) beats the best remaining Bench Boost opportunity (3.26).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.06) beats the best remaining Bench Boost opportunity (3.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.36 | 11.45 | 18.18 | 1.00 | 96.1 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.02 | 0.27 | 0.59 | 0.00 | 4.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 12.39 | 20.78 | 11.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 12.05 | 19.50 | 8.00 | 91.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.96 | 11.31 | 17.87 | 4.00 | 80.9 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.93 | 5.73 | 9.09 | 0.00 | 72.9 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.11 | 3.40 | 5.95 | 0.00 | 41.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.99 | 21.65 | 34.54 | 2.00 | 97.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.78 | 17.21 | 26.81 | 12.00 | 110.3 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.42 | 0.80 | 0.00 | 4.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.47 | 43.21 | 3.00 | 106.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.68 | 22.54 | 36.84 | 2.00 | 110.7 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.99 | 15.07 | 25.20 | 2.00 | 89.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.98 | 14.86 | 23.25 | 2.00 | 76.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.16 | 9.42 | 15.50 | 0.00 | 71.6 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 76.57
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.86 | 9.03 | 14.78 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.11 | 0.23 | 0.51 | 0.00 | 2.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.07 | 16.38 | 25.79 | 5.00 | 100.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.72 | 11.94 | 18.89 | 2.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.16 | 11.47 | 18.71 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.38 | 2.27 | 4.04 | 6.00 | 36.4 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.64 | 2.09 | 4.13 | 1.00 | 29.3 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.85 | 21.11 | 34.06 | 13.00 | 99.7 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.53 | 13.71 | 21.80 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.25 | 0.54 | 0.00 | 3.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.89 | 41.96 | 8.00 | 104.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.29 | 19.98 | 33.53 | 2.00 | 97.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.42 | 16.00 | 26.55 | 7.00 | 100.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.76 | 23.67 | 5.00 | 77.9 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.29 | 5.00 | 9.21 | 2.00 | 33.6 | 90.0 |