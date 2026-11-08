# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 237.25
- Total actual points: 186.00
- Average predicted points: 59.31
- Average actual points: 46.50
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
- Predicted score: 61.48
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.29 | 9.11 | 15.47 | 1.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.87 | 4.66 | 7.42 | 0.00 | 49.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.99 | 14.68 | 24.11 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.76 | 14.48 | 23.97 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.42 | 10.55 | 17.28 | 5.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.81 | 6.39 | 10.85 | 1.00 | 74.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.13 | 10.02 | 5.00 | 74.5 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.34 | 24.57 | 39.90 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.03 | 16.24 | 9.00 | 79.0 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.70 | 4.26 | 6.43 | 0.00 | 37.2 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.94 | 20.73 | 34.11 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.70 | 17.37 | 28.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.10 | 12.36 | 19.74 | 2.00 | 78.6 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.25 | 11.63 | 18.44 | 2.00 | 88.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.73 | 11.37 | 19.12 | 1.00 | 80.4 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.24
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.09, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.68 | 15.64 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.78 | 2.53 | 4.33 | 1.00 | 27.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.64 | 14.83 | 24.39 | 9.00 | 89.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.69 | 13.25 | 21.13 | 8.00 | 89.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.26 | 9.80 | 17.54 | 0.00 | 60.8 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.56 | 10.51 | 1.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.49 | 9.67 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.53 | 14.10 | 26.05 | 0.00 | 32.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.67 | 17.24 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.41 | 4.32 | 6.63 | 1.00 | 36.5 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.34 | 22.52 | 36.57 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.35 | 18.46 | 29.41 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.89 | 11.02 | 17.69 | 6.00 | 69.7 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.44 | 17.36 | 14.00 | 68.5 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.99 | 9.34 | 15.34 | 2.00 | 70.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 58.52
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (8.34).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.22, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (8.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.54 | 10.11 | 16.38 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.82 | 5.21 | 8.27 | 0.00 | 53.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.33 | 14.17 | 23.64 | 5.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.35 | 12.61 | 19.46 | 2.00 | 78.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.76 | 11.51 | 19.47 | 2.00 | 60.3 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.38 | 10.39 | 1.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.44 | 4.44 | 7.25 | 5.00 | 46.4 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.62 | 27.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.58 | 17.08 | 1.00 | 76.0 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.24 | 4.07 | 6.52 | 0.00 | 35.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.57 | 20.80 | 34.20 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.09 | 28.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.81 | 13.45 | 21.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.48 | 10.41 | 17.07 | 2.00 | 59.0 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.08 | 9.69 | 16.00 | 2.00 | 80.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.01
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.71 | 14.55 | 0.00 | 83.7 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.80 | 2.68 | 4.42 | 0.00 | 25.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.14 | 15.89 | 25.72 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.83 | 13.30 | 21.93 | 1.00 | 81.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.94 | 11.92 | 18.95 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.54 | 6.92 | 10.92 | 1.00 | 79.2 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.37 | 6.42 | 10.24 | 1.00 | 67.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.49 | 11.07 | 21.06 | 0.00 | 25.2 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.20 | 9.74 | 15.84 | 5.00 | 68.9 | 90.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.19 | 3.03 | 5.02 | 1.00 | 24.1 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.22 | 21.34 | 35.34 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.48 | 28.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.71 | 12.82 | 20.91 | 1.00 | 80.5 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.10 | 10.03 | 16.20 | 5.00 | 80.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.07 | 9.94 | 16.13 | 0.00 | 54.1 | 0.0 |