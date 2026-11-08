# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.48
- Total actual points: 203.00
- Average predicted points: 58.12
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
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.46 | 0.78 | 1.14 | 0.00 | 8.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.03 | 14.75 | 24.17 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.76 | 14.44 | 23.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.49 | 10.66 | 17.40 | 5.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.83 | 6.33 | 10.61 | 1.00 | 75.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.24 | 10.14 | 5.00 | 76.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.38 | 24.62 | 39.93 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.12 | 16.35 | 9.00 | 80.5 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.81 | 4.47 | 6.70 | 0.00 | 40.2 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.86 | 20.46 | 33.65 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.72 | 17.37 | 28.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.13 | 12.39 | 19.77 | 2.00 | 79.9 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.26 | 11.66 | 18.48 | 2.00 | 90.0 | 90.0 |
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
- Transfer: Kieran Trippier -> William Saliba (projected gain 3.83, hit 0)
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.59 | 8.72 | 14.32 | 10.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.50 | 0.65 | 0.00 | 10.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.64 | 14.80 | 24.30 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.62 | 13.10 | 21.08 | 8.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.11 | 11.57 | 18.20 | 7.00 | 85.3 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.26 | 6.68 | 10.62 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.41 | 9.32 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.46 | 14.42 | 26.88 | 0.00 | 17.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.53 | 10.75 | 17.31 | 2.00 | 83.0 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.50 | 4.49 | 6.83 | 1.00 | 39.0 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.25 | 22.23 | 36.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.36 | 18.45 | 29.35 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.74 | 11.21 | 18.42 | 6.00 | 36.9 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.67 | 10.53 | 17.41 | 14.00 | 71.1 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.04 | 9.44 | 15.44 | 2.00 | 71.6 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 53.89
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.55) beats the best remaining Bench Boost opportunity (3.76).
- Transfer: Hwang Hee-chan -> Pascal Groß (projected gain 2.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.55) beats the best remaining Bench Boost opportunity (3.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.33 | 10.11 | 16.84 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.77 | 1.24 | 0.00 | 9.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.21 | 13.98 | 23.46 | 5.00 | 82.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.26 | 12.47 | 19.36 | 2.00 | 76.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.48 | 10.85 | 17.39 | 2.00 | 86.6 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.92 | 6.32 | 10.40 | 1.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.38 | 4.28 | 6.97 | 5.00 | 45.9 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.68 | 27.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.56 | 10.51 | 17.07 | 1.00 | 74.9 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.22 | 4.08 | 6.63 | 0.00 | 35.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.35 | 20.34 | 33.56 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.93 | 28.53 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.71 | 13.29 | 21.12 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.64 | 11.70 | 19.47 | 7.00 | 78.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.39 | 10.31 | 17.02 | 2.00 | 57.5 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.50
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.11 | 9.33 | 15.53 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.78 | 1.34 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.00 | 15.66 | 25.48 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.87 | 11.82 | 18.90 | 5.00 | 78.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.17 | 11.34 | 18.06 | 1.00 | 88.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.48 | 6.85 | 10.92 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.28 | 6.23 | 9.95 | 1.00 | 66.6 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.54 | 11.23 | 21.29 | 0.00 | 26.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.13 | 9.65 | 15.81 | 5.00 | 67.6 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.21 | 3.12 | 5.21 | 1.00 | 25.6 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.00 | 20.87 | 34.70 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.13 | 17.33 | 27.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.63 | 12.71 | 20.86 | 1.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.91 | 11.60 | 19.29 | 2.00 | 78.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.00 | 9.82 | 16.02 | 0.00 | 53.0 | 0.0 |