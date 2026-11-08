# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 269.03
- Total actual points: 262.00
- Average predicted points: 67.26
- Average actual points: 65.50
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
- Predicted score: 67.95
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.87 | 8.95 | 14.30 | 4.00 | 83.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.23 | 0.78 | 1.26 | 0.00 | 9.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.89 | 13.07 | 21.21 | 0.00 | 80.6 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.17 | 11.33 | 18.51 | 2.00 | 82.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.02 | 10.96 | 17.89 | 1.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.66 | 8.66 | 1.00 | 63.3 | 90.0 |
| Bench 4 | Bench | James Bree | DEF | 17 | 3.9 | 2.04 | 5.47 | 8.56 | 1.00 | 57.0 | 45.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.21 | 19.86 | 32.13 | 7.00 | 82.6 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.30 | 12.25 | 19.30 | 8.00 | 82.7 | 87.0 |
| Bench 2 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.75 | 7.65 | 12.61 | 1.00 | 69.4 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.74 | 26.14 | 42.97 | 7.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 6.89 | 20.34 | 34.08 | 10.00 | 82.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.19 | 14.75 | 23.05 | 7.00 | 79.7 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.12 | 14.03 | 23.08 | 19.00 | 82.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.82 | 11.03 | 17.97 | 1.00 | 80.0 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.80
- Actual score: 68.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.69 | 7.84 | 13.07 | 1.00 | 82.7 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.26 | 0.80 | 1.26 | 0.00 | 9.6 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.31 | 12.76 | 19.68 | 6.00 | 82.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.56 | 11.84 | 19.63 | 2.00 | 74.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.93 | 11.29 | 18.09 | 7.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.17 | 5.95 | 9.30 | 1.00 | 72.2 | 90.0 |
| Bench 4 | Bench | James Bree | DEF | 17 | 3.9 | 1.74 | 5.14 | 8.17 | 1.00 | 51.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.49 | 19.91 | 31.68 | 16.00 | 80.1 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.58 | 11.29 | 17.93 | 9.00 | 69.6 | 89.0 |
| Bench 2 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.37 | 6.90 | 11.75 | 1.00 | 62.6 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.71 | 24.44 | 40.50 | 2.00 | 82.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.84 | 19.97 | 33.40 | 10.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.86 | 14.53 | 23.92 | 2.00 | 82.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.91 | 14.38 | 22.95 | 9.00 | 78.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.20 | 9.64 | 15.66 | 2.00 | 77.1 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.45
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.84) beats the best remaining Bench Boost opportunity (6.38).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.84) beats the best remaining Bench Boost opportunity (6.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.70 | 7.31 | 12.44 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.37 | 0.77 | 1.36 | 0.00 | 9.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.16 | 12.46 | 20.76 | 11.00 | 81.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.83 | 11.27 | 17.69 | 4.00 | 81.3 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.97 | 10.42 | 17.28 | 8.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.71 | 8.93 | 0.00 | 74.3 | 0.0 |
| Bench 3 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.83 | 5.56 | 8.80 | 1.00 | 66.6 | 85.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.27 | 19.86 | 32.08 | 2.00 | 82.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 5.86 | 15.33 | 24.22 | 12.00 | 82.7 | 82.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.72 | 5.75 | 9.94 | 1.00 | 53.7 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.49 | 24.78 | 40.90 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.75 | 19.58 | 32.57 | 2.00 | 82.7 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.87 | 23.13 | 2.00 | 76.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.46 | 13.55 | 23.16 | 2.00 | 82.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.82 | 8.58 | 14.30 | 0.00 | 65.8 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.83
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.75) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.75) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.40 | 7.25 | 12.53 | 5.00 | 82.4 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.19 | 0.54 | 1.08 | 0.00 | 8.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.34 | 14.71 | 23.54 | 5.00 | 82.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.63 | 11.86 | 18.65 | 2.00 | 79.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.25 | 11.42 | 18.58 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.70 | 5.17 | 8.17 | 4.00 | 64.9 | 87.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.49 | 2.61 | 4.62 | 6.00 | 39.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.25 | 19.31 | 31.64 | 13.00 | 82.7 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.39 | 13.59 | 21.49 | 2.00 | 79.1 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 2.14 | 6.60 | 11.19 | 1.00 | 64.2 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.75 | 24.14 | 39.61 | 8.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.95 | 18.67 | 31.44 | 2.00 | 83.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.52 | 14.72 | 23.49 | 5.00 | 80.9 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.70 | 14.29 | 24.24 | 7.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Enzo Fernández | MID | 6 | 4.9 | 0.91 | 4.14 | 7.94 | 2.00 | 25.6 | 90.0 |