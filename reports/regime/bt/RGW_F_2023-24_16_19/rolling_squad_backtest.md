# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 229.76
- Total actual points: 196.00
- Average predicted points: 57.44
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
- Predicted score: 61.05
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.31 | 9.12 | 15.48 | 1.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.40 | 0.71 | 1.11 | 0.00 | 4.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.95 | 14.59 | 23.82 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.71 | 14.56 | 24.25 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.43 | 10.51 | 17.19 | 5.00 | 75.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.60 | 9.41 | 15.28 | 7.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.51 | 7.75 | 12.10 | 1.00 | 76.4 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.23 | 24.88 | 40.15 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.77 | 7.12 | 11.17 | 2.00 | 65.7 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 1.68 | 5.76 | 8.69 | 1.00 | 43.7 | 57.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.92 | 21.08 | 34.62 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.63 | 17.14 | 27.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 12.05 | 19.30 | 2.00 | 80.6 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.22 | 11.45 | 18.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.71 | 11.22 | 18.90 | 1.00 | 82.1 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.09
- Actual score: 59.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.94, hit 0)
- Autosub: Cameron Archer replaced Vitalii Mykolenko.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.50 | 8.47 | 14.05 | 10.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.08 | 0.61 | 1.06 | 0.00 | 5.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.60 | 14.79 | 24.64 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.77 | 13.12 | 21.02 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.20 | 9.88 | 17.42 | 0.00 | 61.1 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.23 | 9.75 | 15.81 | 0.00 | 85.5 | 0.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.92 | 5.60 | 9.16 | 0.00 | 62.2 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.49 | 14.48 | 26.41 | 0.00 | 31.4 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.62 | 7.56 | 11.92 | 2.00 | 65.9 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 0.00 | 5.08 | 8.57 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.16 | 22.36 | 36.38 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.25 | 18.33 | 29.03 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.85 | 10.68 | 17.21 | 6.00 | 71.4 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.56 | 10.11 | 16.91 | 14.00 | 70.5 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.33 | 10.04 | 16.63 | 1.00 | 81.9 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 52.76
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.07) beats the best remaining Bench Boost opportunity (2.71).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 3.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.07) beats the best remaining Bench Boost opportunity (2.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.31 | 9.88 | 16.50 | 2.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.12 | 0.74 | 1.23 | 0.00 | 8.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.38 | 14.15 | 24.01 | 5.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.48 | 12.46 | 19.32 | 2.00 | 80.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.81 | 11.14 | 18.47 | 2.00 | 60.3 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.95 | 4.38 | 7.83 | 1.00 | 37.7 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.38 | 4.38 | 7.68 | 6.00 | 48.4 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.46 | 26.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.52 | 7.56 | 11.64 | 8.00 | 73.5 | 89.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.6 | 1.72 | 4.82 | 7.83 | 1.00 | 29.3 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.40 | 20.78 | 34.19 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.79 | 17.90 | 28.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.79 | 13.18 | 20.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.54 | 10.17 | 16.78 | 2.00 | 59.5 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.18 | 9.77 | 16.07 | 2.00 | 81.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.87
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Vitalii Mykolenko replaced Cole Palmer.
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.14 | 9.49 | 15.59 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.46 | 1.03 | 1.59 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.25 | 16.32 | 26.60 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.79 | 12.99 | 21.37 | 1.00 | 80.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.97 | 11.85 | 18.84 | 5.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.53 | 8.04 | 13.23 | 1.00 | 76.0 | 90.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.27 | 6.58 | 10.75 | 1.00 | 72.8 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.29 | 11.28 | 21.29 | 0.00 | 22.2 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.15 | 8.39 | 13.45 | 5.00 | 77.3 | 85.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.6 | 2.18 | 5.71 | 9.08 | 5.00 | 41.4 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.03 | 21.34 | 35.34 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.13 | 17.33 | 27.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.77 | 12.80 | 20.87 | 1.00 | 81.3 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.23 | 10.12 | 16.39 | 5.00 | 81.5 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.04 | 9.84 | 16.09 | 0.00 | 55.9 | 0.0 |