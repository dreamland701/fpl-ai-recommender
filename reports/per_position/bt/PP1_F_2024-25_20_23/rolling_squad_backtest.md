# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 295.97
- Total actual points: 270.00
- Average predicted points: 73.99
- Average actual points: 67.50
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 75.56
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.4 | 4.34 | 14.65 | 25.81 | 1.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.12 | 0.38 | 0.59 | 0.00 | 3.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 15.93 | 25.20 | 0.00 | 90.0 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.70 | 11.78 | 18.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.61 | 11.64 | 18.18 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Timothy Castagne | DEF | 9 | 4.2 | 2.74 | 7.11 | 10.81 | 1.00 | 68.0 | 90.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.80 | 5.08 | 7.99 | 1.00 | 52.9 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.38 | 18.60 | 30.05 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 5.04 | 14.16 | 22.11 | 8.00 | 85.7 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.11 | 0.19 | 0.00 | 0.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 11.07 | 29.48 | 46.83 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.74 | 22.53 | 36.92 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.48 | 15.47 | 25.02 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.41 | 15.27 | 23.72 | 7.00 | 79.7 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.83 | 11.46 | 18.69 | 1.00 | 81.4 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alisson Ramses Becker
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.17
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Alisson Ramses Becker | GK | 12 | 5.4 | 7.96 | 16.90 | 22.65 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.13 | 0.30 | 0.58 | 0.00 | 3.5 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.20 | 12.32 | 18.54 | 6.00 | 80.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.39 | 11.20 | 18.33 | 2.00 | 69.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.65 | 10.14 | 15.88 | 7.00 | 76.6 | 90.0 |
| Bench 2 | Bench | Timothy Castagne | DEF | 9 | 4.2 | 2.49 | 6.67 | 10.25 | 0.00 | 67.7 | 90.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.47 | 4.66 | 7.31 | 1.00 | 50.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 5.34 | 17.52 | 28.27 | 16.00 | 85.2 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.57 | 11.46 | 17.63 | 9.00 | 66.8 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.08 | 0.27 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.28 | 25.84 | 42.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 22.20 | 36.21 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.51 | 16.43 | 26.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 16.09 | 25.16 | 9.00 | 84.7 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.16 | 9.87 | 16.33 | 2.00 | 75.6 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 74.61
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.22) beats the best remaining Bench Boost opportunity (4.79).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.22) beats the best remaining Bench Boost opportunity (4.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.4 | 5.70 | 16.74 | 22.16 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Cieran Slicker | GK | 10 | 3.9 | 0.03 | 0.22 | 0.52 | 0.00 | 3.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.25 | 11.50 | 19.33 | 11.00 | 85.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.60 | 10.98 | 16.91 | 4.00 | 72.4 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.23 | 10.96 | 17.57 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Timothy Castagne | DEF | 9 | 4.2 | 2.52 | 6.07 | 9.93 | 6.00 | 68.1 | 90.0 |
| Bench 3 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.66 | 5.28 | 7.83 | 1.00 | 66.6 | 85.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.20 | 19.53 | 31.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.64 | 17.57 | 28.21 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.09 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.59 | 27.16 | 44.13 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.68 | 34.97 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.59 | 16.03 | 26.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.01 | 14.81 | 23.15 | 2.00 | 75.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.64 | 8.50 | 14.24 | 0.00 | 61.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 79.63
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.79) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.4 | 4.07 | 10.69 | 16.74 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.03 | 0.15 | 0.00 | 3.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.67 | 17.62 | 27.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.46 | 11.11 | 17.46 | 2.00 | 73.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.83 | 10.10 | 16.35 | 2.00 | 83.2 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 9 | 4.2 | 2.58 | 6.57 | 10.48 | 2.00 | 70.3 | 90.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.45 | 4.58 | 7.10 | 4.00 | 63.5 | 87.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 6.72 | 18.42 | 29.87 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.62 | 14.58 | 23.63 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.79 | 26.96 | 43.67 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.00 | 19.10 | 31.75 | 2.00 | 80.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.55 | 16.28 | 26.82 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.78 | 15.36 | 24.39 | 5.00 | 80.1 | 87.0 |
| Bench 3 | Bench | Enzo Fernández | MID | 6 | 4.9 | 0.96 | 4.65 | 8.72 | 2.00 | 27.5 | 90.0 |