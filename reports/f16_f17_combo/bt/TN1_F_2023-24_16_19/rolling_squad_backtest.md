# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.65
- Total actual points: 203.00
- Average predicted points: 58.16
- Average actual points: 50.75
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
- Predicted score: 61.83
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.34 | 9.24 | 15.66 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.17 | 0.33 | 1.00 | 2.1 | 3.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.03 | 14.74 | 24.17 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.76 | 14.44 | 23.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.49 | 10.66 | 17.40 | 5.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.83 | 6.33 | 10.61 | 1.00 | 75.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.24 | 10.14 | 5.00 | 76.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.38 | 24.62 | 39.93 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.12 | 16.34 | 9.00 | 80.5 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.81 | 4.46 | 6.70 | 0.00 | 40.2 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.86 | 20.46 | 33.65 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.72 | 17.37 | 28.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.13 | 12.39 | 19.77 | 2.00 | 79.9 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.26 | 11.66 | 18.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.80 | 11.48 | 19.25 | 1.00 | 83.1 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.25
- Actual score: 68.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 2.73, hit 0)
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.59 | 8.72 | 14.32 | 10.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.06 | 1.05 | 1.70 | 0.00 | 14.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.64 | 14.80 | 24.30 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.62 | 13.11 | 21.10 | 8.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.10 | 11.57 | 18.20 | 7.00 | 85.3 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.26 | 6.68 | 10.62 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.41 | 9.30 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.46 | 14.42 | 26.89 | 0.00 | 31.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.53 | 10.75 | 17.31 | 2.00 | 83.0 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.50 | 4.49 | 6.83 | 1.00 | 39.0 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.25 | 22.23 | 36.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.36 | 18.45 | 29.34 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.74 | 11.21 | 18.42 | 6.00 | 67.0 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.67 | 10.52 | 17.41 | 14.00 | 71.1 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.04 | 9.43 | 15.44 | 2.00 | 71.6 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.06
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.69) beats the best remaining Bench Boost opportunity (3.92).
- Transfer: Hwang Hee-chan -> Pascal Groß (projected gain 2.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.69) beats the best remaining Bench Boost opportunity (3.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.33 | 10.12 | 16.86 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Remi Matthews | GK | 8 | 3.9 | 0.48 | 1.03 | 1.61 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.22 | 13.99 | 23.47 | 5.00 | 82.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.26 | 12.48 | 19.38 | 2.00 | 76.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.49 | 10.86 | 17.41 | 2.00 | 86.6 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.92 | 6.33 | 10.41 | 1.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.38 | 4.29 | 6.99 | 5.00 | 45.9 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.68 | 27.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.57 | 10.52 | 17.09 | 1.00 | 74.9 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.22 | 4.09 | 6.65 | 0.00 | 35.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.35 | 20.35 | 33.57 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.94 | 28.55 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.71 | 13.29 | 21.13 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.64 | 11.71 | 19.49 | 7.00 | 78.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.39 | 10.32 | 17.03 | 2.00 | 57.5 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.52
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.11 | 9.34 | 15.55 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.27 | 1.00 | 1.60 | 0.00 | 11.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.00 | 15.67 | 25.50 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.87 | 11.82 | 18.92 | 5.00 | 78.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.17 | 11.35 | 18.08 | 1.00 | 88.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.48 | 6.86 | 10.94 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.28 | 6.23 | 9.96 | 1.00 | 66.7 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.55 | 11.24 | 21.32 | 0.00 | 26.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.13 | 9.65 | 15.82 | 5.00 | 67.6 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.22 | 3.12 | 5.23 | 1.00 | 25.6 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.00 | 20.88 | 34.72 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.13 | 17.34 | 27.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.63 | 12.72 | 20.87 | 1.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.91 | 11.61 | 19.30 | 2.00 | 78.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.00 | 9.82 | 16.04 | 0.00 | 53.1 | 0.0 |