# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.65
- Total actual points: 256.00
- Average predicted points: 70.91
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
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 10.81 | 17.47 | 3.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.07 | 0.63 | 1.10 | 0.00 | 10.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.43 | 14.61 | 23.12 | 0.00 | 88.3 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.69 | 12.98 | 20.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.58 | 12.36 | 19.54 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.78 | 5.63 | 8.79 | 1.00 | 71.3 | 81.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.79 | 4.93 | 7.49 | 1.00 | 57.3 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.83 | 21.80 | 34.81 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.86 | 13.86 | 21.36 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.01 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.19 | 27.31 | 44.23 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 21.87 | 36.01 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.65 | 15.49 | 24.86 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.19 | 14.80 | 23.13 | 7.00 | 83.2 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.80 | 11.03 | 17.97 | 1.00 | 82.6 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.41
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.97 | 10.76 | 17.45 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.37 | 0.89 | 1.48 | 0.00 | 10.1 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.14 | 12.18 | 18.70 | 6.00 | 80.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.00 | 11.65 | 18.77 | 7.00 | 86.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.46 | 11.49 | 18.93 | 2.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.02 | 5.75 | 9.21 | 0.00 | 71.9 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.99 | 5.43 | 8.36 | 1.00 | 66.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.58 | 20.31 | 32.53 | 16.00 | 81.2 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.50 | 10.99 | 17.27 | 9.00 | 66.1 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.17 | 25.79 | 42.15 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.34 | 21.40 | 35.17 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.49 | 16.09 | 25.22 | 9.00 | 87.9 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.36 | 15.93 | 25.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.24 | 9.73 | 15.88 | 2.00 | 76.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.10
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.12) beats the best remaining Bench Boost opportunity (3.37).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.12) beats the best remaining Bench Boost opportunity (3.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.36 | 11.59 | 18.43 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.76 | 1.38 | 0.00 | 9.1 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.65 | 12.39 | 20.09 | 8.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.12 | 12.30 | 20.57 | 11.00 | 78.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.72 | 10.79 | 16.89 | 4.00 | 76.3 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.81 | 5.40 | 8.53 | 0.00 | 70.0 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.12 | 3.38 | 5.84 | 0.00 | 41.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.85 | 21.56 | 34.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.42 | 16.88 | 26.28 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.98 | 26.16 | 42.70 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.25 | 20.94 | 34.31 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.88 | 14.99 | 23.43 | 2.00 | 76.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.96 | 14.87 | 24.78 | 2.00 | 88.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.78 | 8.48 | 14.06 | 0.00 | 63.6 | 0.0 |

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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.94 | 9.22 | 15.13 | 1.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.30 | 0.73 | 1.33 | 0.00 | 7.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 16.13 | 25.33 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.32 | 11.78 | 19.27 | 2.00 | 88.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.51 | 11.35 | 17.79 | 2.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.45 | 2.44 | 4.27 | 6.00 | 38.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.74 | 2.25 | 4.31 | 1.00 | 31.2 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.85 | 20.93 | 33.79 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.42 | 13.64 | 21.65 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.58 | 41.48 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.86 | 18.47 | 31.17 | 2.00 | 83.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.26 | 15.73 | 26.04 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.57 | 14.87 | 23.84 | 5.00 | 81.2 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.04 | 4.40 | 8.33 | 2.00 | 28.7 | 90.0 |