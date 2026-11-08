# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 270.92
- Total actual points: 264.00
- Average predicted points: 67.73
- Average actual points: 66.00
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
- Predicted score: 69.15
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.33 | 9.44 | 15.60 | 3.00 | 80.8 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.28 | 0.88 | 1.39 | 0.00 | 10.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.01 | 13.36 | 21.44 | 0.00 | 81.1 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.29 | 11.63 | 18.74 | 2.00 | 83.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.14 | 11.25 | 18.12 | 1.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Nathan Wood-Gordon | DEF | 17 | 4.0 | 2.16 | 6.08 | 9.66 | 1.00 | 75.9 | 45.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 5.83 | 8.87 | 1.00 | 65.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.33 | 20.15 | 32.37 | 7.00 | 83.1 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.42 | 12.54 | 19.54 | 8.00 | 83.2 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.06 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.86 | 26.44 | 43.20 | 7.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.00 | 20.63 | 34.32 | 10.00 | 83.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.02 | 14.48 | 22.71 | 7.00 | 78.4 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.24 | 14.32 | 23.32 | 19.00 | 83.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.65 | 10.76 | 17.63 | 1.00 | 78.7 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.88
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.50 | 9.38 | 15.50 | 2.00 | 79.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.31 | 0.91 | 1.39 | 0.00 | 10.6 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.16 | 12.50 | 19.38 | 6.00 | 81.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.57 | 11.87 | 19.66 | 2.00 | 74.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.77 | 11.03 | 17.78 | 7.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.19 | 5.98 | 9.32 | 1.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Nathan Wood-Gordon | DEF | 17 | 4.0 | 1.83 | 5.44 | 8.73 | 0.00 | 66.1 | 7.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.48 | 19.95 | 31.86 | 16.00 | 79.2 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.59 | 11.33 | 17.95 | 9.00 | 69.9 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.82 | 24.74 | 40.76 | 2.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.96 | 20.27 | 33.65 | 10.00 | 83.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.98 | 14.83 | 24.18 | 2.00 | 83.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.03 | 14.68 | 23.21 | 9.00 | 79.3 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.19 | 9.68 | 15.83 | 2.00 | 76.2 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.01
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.68) beats the best remaining Bench Boost opportunity (3.93).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.68) beats the best remaining Bench Boost opportunity (3.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.21 | 8.94 | 14.98 | 1.00 | 79.9 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.42 | 0.87 | 1.48 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.15 | 12.50 | 20.90 | 11.00 | 80.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.31 | 17.84 | 4.00 | 80.3 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.10 | 10.71 | 17.52 | 8.00 | 83.2 | 90.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.75 | 9.07 | 0.00 | 73.3 | 0.0 |
| Bench 3 | Bench Boost | Nathan Wood-Gordon | DEF | 17 | 4.0 | 1.34 | 4.77 | 7.98 | 0.00 | 54.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.40 | 20.14 | 32.32 | 2.00 | 83.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 5.99 | 15.61 | 24.46 | 12.00 | 83.2 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.62 | 25.06 | 41.14 | 3.00 | 83.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.29 | 21.18 | 34.75 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.90 | 23.28 | 2.00 | 75.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.59 | 13.84 | 23.40 | 2.00 | 83.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.73 | 8.37 | 13.89 | 0.00 | 61.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 72.88
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.89) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.07 | 8.57 | 14.42 | 9.00 | 79.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.24 | 0.64 | 1.20 | 0.00 | 9.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.47 | 14.99 | 23.77 | 5.00 | 83.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.88 | 18.78 | 2.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.09 | 11.20 | 18.32 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Nathan Wood-Gordon | DEF | 17 | 4.0 | 0.83 | 2.89 | 5.20 | 0.00 | 33.0 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.54 | 2.71 | 4.75 | 6.00 | 40.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.39 | 19.59 | 31.86 | 13.00 | 83.2 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.38 | 13.61 | 21.61 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.89 | 24.42 | 39.83 | 8.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.89 | 18.64 | 31.47 | 2.00 | 84.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.51 | 14.74 | 23.61 | 5.00 | 80.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.84 | 14.57 | 24.46 | 7.00 | 83.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.96 | 4.22 | 8.02 | 2.00 | 26.5 | 90.0 |