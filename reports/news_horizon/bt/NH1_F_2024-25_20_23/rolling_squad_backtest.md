# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.59
- Total actual points: 256.00
- Average predicted points: 70.90
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
- Predicted score: 73.38
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.75 | 17.38 | 3.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.08 | 0.68 | 1.19 | 0.00 | 9.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.40 | 14.68 | 23.36 | 0.00 | 87.4 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.69 | 12.94 | 20.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.54 | 12.57 | 20.00 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.91 | 6.03 | 9.42 | 1.00 | 74.6 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.84 | 5.21 | 8.04 | 1.00 | 58.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.71 | 21.41 | 34.16 | 7.00 | 89.3 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.82 | 13.88 | 21.47 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.25 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.26 | 27.73 | 45.06 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 21.91 | 36.07 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.66 | 15.63 | 25.14 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.11 | 14.67 | 23.00 | 7.00 | 80.6 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.75 | 10.96 | 17.90 | 1.00 | 81.2 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.28
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 10.68 | 17.29 | 2.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.38 | 0.94 | 1.59 | 0.00 | 9.7 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.25 | 12.71 | 19.68 | 6.00 | 83.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.47 | 11.58 | 19.09 | 2.00 | 70.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.87 | 11.22 | 18.02 | 7.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.17 | 6.18 | 9.89 | 0.00 | 75.8 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.06 | 5.74 | 8.94 | 1.00 | 67.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.46 | 19.88 | 31.75 | 16.00 | 77.8 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.50 | 11.00 | 17.29 | 9.00 | 66.0 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.11 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.04 | 42.66 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.57 | 35.47 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.38 | 16.10 | 25.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.42 | 16.00 | 25.16 | 9.00 | 85.7 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.22 | 9.66 | 15.75 | 2.00 | 75.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.41
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.66).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.32 | 11.47 | 18.18 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.81 | 1.49 | 0.00 | 8.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.17 | 12.48 | 20.86 | 11.00 | 79.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.00 | 19.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.29 | 17.83 | 4.00 | 79.4 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.91 | 5.75 | 9.15 | 0.00 | 72.3 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.27 | 3.74 | 6.36 | 0.00 | 45.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.79 | 21.40 | 34.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.40 | 16.94 | 26.44 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.02 | 26.34 | 43.03 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.35 | 21.75 | 35.98 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.02 | 15.12 | 25.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.81 | 14.87 | 23.25 | 2.00 | 74.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.79 | 8.95 | 15.12 | 0.00 | 63.4 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.51
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.88 | 9.04 | 14.73 | 1.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.31 | 0.78 | 1.43 | 0.00 | 7.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.90 | 16.34 | 25.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.61 | 11.92 | 18.87 | 2.00 | 77.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.19 | 11.35 | 18.50 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.68 | 4.66 | 6.00 | 40.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.87 | 2.55 | 4.73 | 1.00 | 34.3 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.81 | 20.90 | 33.74 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.38 | 13.57 | 21.53 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.30 | 25.72 | 41.73 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.96 | 19.21 | 32.63 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.29 | 15.92 | 26.38 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.52 | 14.75 | 23.61 | 5.00 | 79.4 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.05 | 4.79 | 9.14 | 2.00 | 28.5 | 90.0 |