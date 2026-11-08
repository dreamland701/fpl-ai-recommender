# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.68
- Total actual points: 256.00
- Average predicted points: 70.92
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
- Predicted score: 73.60
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.75 | 17.44 | 3.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.65 | 1.09 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.52 | 15.18 | 24.27 | 0.00 | 89.7 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.67 | 12.79 | 20.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.49 | 12.30 | 19.47 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.90 | 6.00 | 9.38 | 1.00 | 74.4 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.19 | 7.92 | 1.00 | 58.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.76 | 21.54 | 34.39 | 7.00 | 89.8 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.84 | 13.97 | 21.57 | 8.00 | 89.8 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.26 | 27.66 | 44.92 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.47 | 22.28 | 36.79 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.71 | 15.89 | 25.68 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.13 | 14.75 | 23.14 | 7.00 | 80.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.76 | 11.01 | 18.01 | 1.00 | 80.7 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.31
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.70 | 17.39 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.40 | 0.92 | 1.49 | 0.00 | 10.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.21 | 12.50 | 19.31 | 6.00 | 83.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.55 | 12.05 | 20.01 | 2.00 | 71.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.80 | 10.92 | 17.49 | 7.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.15 | 6.15 | 9.88 | 0.00 | 75.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.73 | 8.87 | 1.00 | 68.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.49 | 19.96 | 31.94 | 16.00 | 78.2 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.48 | 11.08 | 17.46 | 9.00 | 65.2 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.19 | 25.85 | 42.30 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.43 | 21.96 | 36.21 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.43 | 16.32 | 26.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.45 | 16.01 | 25.15 | 9.00 | 85.7 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.20 | 9.70 | 15.90 | 2.00 | 74.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.34
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.66).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.30 | 11.47 | 18.21 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.79 | 1.41 | 0.00 | 9.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.23 | 12.93 | 21.75 | 11.00 | 81.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.46 | 11.71 | 18.86 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.79 | 11.16 | 17.60 | 4.00 | 79.2 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.77 | 9.15 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.24 | 3.75 | 6.47 | 0.00 | 44.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.82 | 21.48 | 34.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.42 | 16.98 | 26.42 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.99 | 26.15 | 42.71 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.56 | 35.41 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.04 | 15.28 | 25.60 | 2.00 | 89.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.88 | 23.29 | 2.00 | 74.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.73 | 8.36 | 13.88 | 0.00 | 61.3 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.43
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.85 | 9.03 | 14.77 | 1.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.33 | 0.77 | 1.35 | 0.00 | 7.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.99 | 16.73 | 26.48 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.59 | 11.75 | 18.54 | 2.00 | 77.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.13 | 11.10 | 18.05 | 2.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.72 | 4.75 | 6.00 | 40.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.84 | 2.55 | 4.83 | 1.00 | 33.6 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.85 | 21.05 | 34.07 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.38 | 13.60 | 21.52 | 2.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.58 | 41.50 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.95 | 19.02 | 32.10 | 2.00 | 85.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.32 | 16.12 | 26.82 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.53 | 14.85 | 23.86 | 5.00 | 79.1 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.97 | 4.24 | 8.06 | 2.00 | 26.0 | 90.0 |