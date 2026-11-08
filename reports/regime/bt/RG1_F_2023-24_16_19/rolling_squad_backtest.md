# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.61
- Total actual points: 196.00
- Average predicted points: 58.15
- Average actual points: 49.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.28
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.08 | 15.42 | 1.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.86 | 4.59 | 7.23 | 0.00 | 45.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.00 | 14.72 | 24.20 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.80 | 14.66 | 24.32 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.48 | 10.73 | 17.60 | 5.00 | 75.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.50 | 9.37 | 15.15 | 7.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.54 | 7.75 | 12.11 | 1.00 | 75.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.36 | 24.63 | 39.98 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.74 | 7.18 | 11.28 | 2.00 | 65.8 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 1.67 | 5.68 | 8.60 | 1.00 | 42.3 | 57.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.90 | 20.69 | 34.13 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.66 | 17.20 | 27.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.07 | 12.30 | 19.67 | 2.00 | 79.4 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.20 | 11.55 | 18.33 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.67 | 11.18 | 18.78 | 1.00 | 80.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.59
- Actual score: 59.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.71, hit 0)
- Autosub: Cameron Archer replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.52 | 8.57 | 14.12 | 10.00 | 81.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.76 | 2.44 | 4.11 | 1.00 | 23.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 15.04 | 24.79 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.76 | 13.45 | 21.49 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.27 | 9.83 | 17.60 | 0.00 | 61.9 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.20 | 9.60 | 15.58 | 0.00 | 83.9 | 0.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.89 | 5.59 | 9.22 | 0.00 | 61.4 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.54 | 14.13 | 26.08 | 0.00 | 33.7 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.60 | 7.48 | 11.78 | 2.00 | 65.6 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 0.00 | 4.93 | 8.28 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.29 | 22.46 | 36.52 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.30 | 18.31 | 29.15 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.85 | 10.96 | 17.62 | 6.00 | 70.3 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.57 | 10.32 | 17.13 | 14.00 | 68.6 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.31 | 10.03 | 16.58 | 1.00 | 81.4 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.21
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.63) beats the best remaining Bench Boost opportunity (4.70).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 3.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.63) beats the best remaining Bench Boost opportunity (4.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.37 | 10.08 | 16.67 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.80 | 5.11 | 8.02 | 0.00 | 50.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.40 | 14.43 | 24.14 | 5.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.43 | 12.87 | 19.92 | 2.00 | 78.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.75 | 11.48 | 19.43 | 2.00 | 61.5 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.33 | 4.26 | 7.43 | 6.00 | 47.7 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.88 | 4.07 | 7.36 | 1.00 | 35.2 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.58 | 26.92 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.48 | 7.41 | 11.56 | 8.00 | 72.8 | 89.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.6 | 1.58 | 4.47 | 7.14 | 1.00 | 27.6 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.55 | 20.81 | 34.29 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.83 | 17.99 | 28.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.76 | 13.28 | 20.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.46 | 10.37 | 17.01 | 2.00 | 58.9 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.05 | 9.60 | 15.84 | 2.00 | 80.3 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.53
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.21) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.21) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Vitalii Mykolenko replaced Cole Palmer.
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.17 | 9.36 | 15.46 | 1.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.77 | 2.56 | 4.14 | 0.00 | 22.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.22 | 16.19 | 26.27 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.86 | 13.36 | 22.06 | 1.00 | 82.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 12.08 | 19.24 | 5.00 | 80.2 | 90.0 |
| Bench 2 | Autosub In | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.44 | 7.74 | 12.78 | 1.00 | 74.5 | 90.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.24 | 6.61 | 10.80 | 1.00 | 72.7 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.52 | 11.13 | 21.14 | 0.00 | 25.8 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.15 | 8.33 | 13.36 | 5.00 | 76.7 | 85.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 2.05 | 5.45 | 8.59 | 5.00 | 40.0 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.21 | 21.40 | 35.51 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.19 | 17.39 | 27.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.69 | 12.75 | 20.79 | 1.00 | 80.3 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.06 | 9.91 | 15.99 | 5.00 | 80.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.04 | 9.81 | 15.90 | 0.00 | 53.8 | 0.0 |