# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 234.72
- Total actual points: 203.00
- Average predicted points: 58.68
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
- Predicted score: 61.31
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.30 | 9.14 | 15.52 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.60 | 1.03 | 0.00 | 4.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.66 | 24.08 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.73 | 14.38 | 23.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.44 | 10.60 | 17.36 | 5.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.22 | 10.47 | 1.00 | 73.9 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.33 | 6.13 | 9.99 | 5.00 | 74.8 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 24.56 | 39.86 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.04 | 16.26 | 9.00 | 79.4 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.69 | 4.33 | 6.64 | 0.00 | 36.9 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.84 | 20.42 | 33.61 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.67 | 17.31 | 28.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.08 | 12.34 | 19.78 | 2.00 | 78.6 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.22 | 11.61 | 18.48 | 2.00 | 89.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.73 | 11.41 | 19.24 | 1.00 | 80.9 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.21
- Actual score: 68.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 2.19, hit 0)
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.55 | 8.61 | 14.17 | 10.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.34 | 0.57 | 0.00 | 6.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.60 | 14.75 | 24.28 | 9.00 | 89.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.69 | 13.32 | 21.32 | 8.00 | 89.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.07 | 11.46 | 18.04 | 7.00 | 84.3 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.21 | 6.55 | 10.45 | 1.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.30 | 9.26 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.62 | 14.60 | 27.03 | 0.00 | 34.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.66 | 17.24 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.41 | 4.34 | 6.69 | 1.00 | 36.3 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.22 | 22.20 | 36.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.32 | 18.40 | 29.32 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.86 | 10.97 | 17.65 | 6.00 | 69.8 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.59 | 10.41 | 17.33 | 14.00 | 68.8 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.99 | 9.34 | 15.33 | 2.00 | 70.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 55.06
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.60) beats the best remaining Bench Boost opportunity (3.83).
- Transfer: Hwang Hee-chan -> Pascal Groß (projected gain 2.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.60) beats the best remaining Bench Boost opportunity (3.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.41 | 10.16 | 16.77 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.78 | 1.26 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.31 | 14.06 | 23.44 | 5.00 | 83.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.34 | 12.59 | 19.47 | 2.00 | 78.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.56 | 10.89 | 17.30 | 2.00 | 88.0 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.38 | 10.34 | 1.00 | 77.9 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.42 | 4.25 | 6.79 | 5.00 | 46.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 15.27 | 28.07 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.57 | 17.06 | 1.00 | 76.2 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.25 | 4.08 | 6.53 | 0.00 | 35.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.46 | 20.44 | 33.57 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.03 | 28.56 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.79 | 13.42 | 21.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.74 | 11.83 | 19.53 | 7.00 | 80.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.53 | 11.03 | 18.43 | 2.00 | 60.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.13
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Bruno Guimarães Rodriguez Moura (projected gain 0.87, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.19 | 9.39 | 15.49 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.31 | 0.79 | 1.36 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.11 | 15.82 | 25.61 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.94 | 11.91 | 18.94 | 5.00 | 79.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.26 | 11.41 | 18.03 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.56 | 6.92 | 10.88 | 1.00 | 79.6 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.27 | 9.93 | 1.00 | 67.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.61 | 11.69 | 22.21 | 0.00 | 27.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.21 | 9.73 | 15.81 | 5.00 | 69.0 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.22 | 3.05 | 5.00 | 1.00 | 24.7 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 20.99 | 34.73 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.21 | 17.44 | 27.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.71 | 12.81 | 20.89 | 1.00 | 80.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.01 | 11.74 | 19.37 | 2.00 | 80.7 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 5.8 | 3.55 | 10.12 | 16.46 | 1.00 | 81.3 | 90.0 |