# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.91
- Total actual points: 256.00
- Average predicted points: 70.98
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
- Predicted score: 73.48
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.87 | 17.66 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.18 | 0.74 | 1.24 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.39 | 14.58 | 23.19 | 0.00 | 88.1 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.73 | 13.11 | 20.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.62 | 12.70 | 20.07 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.82 | 5.68 | 8.92 | 1.00 | 75.1 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.77 | 4.88 | 7.36 | 1.00 | 60.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.75 | 21.74 | 34.47 | 7.00 | 89.9 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.80 | 13.72 | 21.25 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.24 | 27.70 | 44.95 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.38 | 21.83 | 36.04 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.73 | 15.74 | 25.31 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.14 | 14.87 | 23.22 | 7.00 | 81.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.71 | 10.84 | 17.80 | 1.00 | 81.4 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.26
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.94 | 10.85 | 17.63 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.50 | 1.08 | 1.64 | 0.00 | 10.8 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.26 | 12.71 | 19.78 | 6.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.42 | 11.56 | 19.10 | 2.00 | 70.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.85 | 11.20 | 18.07 | 7.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.06 | 5.84 | 9.42 | 0.00 | 76.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.97 | 5.41 | 8.29 | 1.00 | 69.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.48 | 19.96 | 31.99 | 16.00 | 78.5 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.52 | 11.13 | 17.45 | 9.00 | 66.8 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.20 | 25.91 | 42.56 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.35 | 21.55 | 35.48 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.46 | 16.13 | 26.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.43 | 15.99 | 25.19 | 9.00 | 86.3 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.16 | 9.64 | 15.77 | 2.00 | 75.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.27
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.26) beats the best remaining Bench Boost opportunity (3.53).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.26) beats the best remaining Bench Boost opportunity (3.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.37 | 11.37 | 18.07 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.24 | 0.80 | 1.41 | 0.00 | 10.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 12.44 | 20.86 | 11.00 | 79.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.61 | 12.15 | 19.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.40 | 17.99 | 4.00 | 80.1 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.88 | 5.40 | 8.58 | 0.00 | 73.2 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.15 | 3.52 | 6.03 | 0.00 | 45.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.83 | 21.51 | 34.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.48 | 16.86 | 26.29 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.99 | 26.32 | 42.98 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.26 | 21.02 | 34.57 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.06 | 15.28 | 25.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.97 | 23.41 | 2.00 | 75.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.69 | 8.21 | 13.72 | 0.00 | 62.3 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.90
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.83 | 9.01 | 14.66 | 1.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.33 | 0.72 | 1.29 | 0.00 | 8.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.96 | 16.35 | 25.68 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.72 | 12.00 | 18.99 | 2.00 | 77.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.18 | 11.38 | 18.59 | 2.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.49 | 2.51 | 4.29 | 6.00 | 40.5 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.76 | 2.34 | 4.42 | 1.00 | 34.4 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.91 | 21.11 | 34.01 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.36 | 13.61 | 21.56 | 2.00 | 78.6 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.37 | 25.82 | 41.76 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.94 | 18.55 | 31.39 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.30 | 15.88 | 26.42 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.60 | 14.89 | 23.85 | 5.00 | 79.2 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 1.01 | 4.13 | 7.96 | 2.00 | 26.6 | 90.0 |