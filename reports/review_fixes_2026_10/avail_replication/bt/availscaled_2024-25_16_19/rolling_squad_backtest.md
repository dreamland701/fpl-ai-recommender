# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 258.60
- Total actual points: 251.00
- Average predicted points: 64.65
- Average actual points: 62.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 60.81
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.81 | 10.82 | 17.34 | 6.00 | 91.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.82 | 8.49 | 14.18 | 2.00 | 86.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.51 | 12.76 | 19.68 | 6.00 | 96.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.17 | 11.89 | 20.05 | 1.00 | 67.5 | 78.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.43 | 10.42 | 17.50 | 7.00 | 44.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.61 | 10.41 | 17.62 | 1.00 | 71.7 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.42 | 9.56 | 15.31 | 2.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.90 | 8.23 | 13.72 | 2.00 | 76.3 | 81.0 |
| XI | XI | Cameron Archer | FWD | 17 | 5.0 | 3.07 | 8.15 | 13.16 | 1.00 | 73.0 | 8.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.26 | 0.40 | 0.73 | 0.00 | 2.9 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.44 | 23.99 | 38.56 | 3.00 | 115.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.26 | 21.85 | 36.96 | 5.00 | 100.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.28 | 18.69 | 29.69 | 3.00 | 93.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.35 | 12.72 | 20.20 | 5.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Kevin Schade | MID | 4 | 5.1 | 3.10 | 10.39 | 17.66 | 3.00 | 57.7 | 14.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.64
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.81 | 11.01 | 17.75 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.42 | 7.86 | 13.24 | 0.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.15 | 12.17 | 19.40 | 2.00 | 85.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.69 | 11.12 | 18.58 | 0.00 | 87.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 3.45 | 10.91 | 17.95 | 4.00 | 67.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.31 | 10.04 | 16.65 | 1.00 | 76.2 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 2.91 | 8.61 | 14.38 | 6.00 | 78.3 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.57 | 8.09 | 13.78 | 2.00 | 63.5 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.23 | 7.14 | 12.35 | 1.00 | 30.4 | 45.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.25 | 0.52 | 0.00 | 2.8 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.54 | 23.40 | 37.35 | 3.00 | 105.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.87 | 22.53 | 37.45 | 21.00 | 92.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.35 | 19.28 | 31.38 | 1.00 | 89.0 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.46 | 11.83 | 18.69 | 3.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Kevin Schade | MID | 4 | 5.1 | 2.80 | 9.65 | 16.63 | 2.00 | 27.7 | 80.0 |

## GW18

- Train rows: 145070
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.50
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.67) beats the best remaining Bench Boost opportunity (10.34).
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 4.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.67) beats the best remaining Bench Boost opportunity (10.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.16 | 11.38 | 18.30 | 6.00 | 90.5 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 2.42 | 7.24 | 11.89 | 7.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.72 | 13.30 | 21.36 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.11 | 13.26 | 21.21 | 2.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.79 | 10.28 | 16.89 | 2.00 | 75.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.29 | 9.94 | 16.34 | 2.00 | 81.5 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.29 | 9.31 | 15.06 | 6.00 | 82.8 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 3.19 | 8.41 | 13.67 | 2.00 | 72.4 | 72.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.79 | 7.77 | 13.11 | 0.00 | 34.3 | 0.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.25 | 0.45 | 0.86 | 0.00 | 3.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.57 | 25.60 | 42.19 | 9.00 | 107.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.78 | 23.48 | 37.95 | 10.00 | 113.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.75 | 14.71 | 24.28 | 2.00 | 90.7 | 80.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.61 | 10.92 | 17.81 | 2.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Kevin Schade | MID | 4 | 5.1 | 3.21 | 10.44 | 17.43 | 3.00 | 36.2 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 70.65
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Kevin Schade -> Jacob Murphy (projected gain 3.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.84 | 11.16 | 18.08 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 3.47 | 9.00 | 14.27 | 2.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.35 | 13.06 | 21.66 | 2.00 | 88.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.60 | 13.00 | 20.58 | 15.00 | 79.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 10.69 | 17.30 | 6.00 | 80.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.65 | 10.33 | 16.69 | 6.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 3.09 | 9.23 | 14.82 | 1.00 | 83.4 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.84 | 8.43 | 13.48 | 5.00 | 67.9 | 64.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.03 | 3.60 | 6.30 | 1.00 | 26.3 | 25.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.05 | 0.46 | 0.76 | 0.00 | 5.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.74 | 25.37 | 41.18 | 16.00 | 112.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.89 | 23.04 | 37.97 | 2.00 | 103.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.98 | 14.99 | 25.09 | 0.00 | 83.4 | 63.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.0 | 4.28 | 12.32 | 20.05 | 3.00 | 71.3 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.13 | 11.41 | 18.47 | 1.00 | 81.5 | 90.0 |