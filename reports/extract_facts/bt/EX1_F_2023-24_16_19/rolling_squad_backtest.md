# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.42
- Total actual points: 190.00
- Average predicted points: 58.10
- Average actual points: 47.50
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
- Predicted score: 61.14
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.15 | 15.57 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.56 | 0.89 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.97 | 14.66 | 24.05 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.73 | 14.40 | 23.84 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.45 | 10.60 | 17.37 | 5.00 | 74.5 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.26 | 10.56 | 1.00 | 73.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.32 | 6.17 | 10.09 | 5.00 | 74.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.31 | 24.54 | 39.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.06 | 16.30 | 9.00 | 79.4 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.71 | 4.29 | 6.50 | 0.00 | 37.3 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.80 | 20.39 | 33.54 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.68 | 17.30 | 27.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.07 | 12.31 | 19.68 | 2.00 | 78.7 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.20 | 11.56 | 18.36 | 2.00 | 88.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.70 | 11.30 | 19.03 | 1.00 | 80.3 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 57.79
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.06) beats the best remaining Bench Boost opportunity (4.81).
- Transfer: Hwang Hee-chan -> Tom Cairney (projected gain 1.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.06) beats the best remaining Bench Boost opportunity (4.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.54 | 8.65 | 14.28 | 10.00 | 84.4 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.29 | 0.42 | 0.00 | 6.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.59 | 14.71 | 24.21 | 9.00 | 89.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.68 | 13.20 | 21.09 | 8.00 | 89.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.31 | 9.92 | 17.70 | 0.00 | 62.0 | 0.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.21 | 6.61 | 10.59 | 1.00 | 75.7 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.35 | 9.37 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.49 | 10.70 | 17.30 | 2.00 | 82.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 2.93 | 10.32 | 19.54 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.43 | 4.38 | 6.73 | 1.00 | 36.8 | 32.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.68 | 20.85 | 33.55 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.49 | 20.04 | 32.92 | 3.00 | 90.0 | 88.0 |
| XI | XI | Tom Cairney | MID | 10 | 4.9 | 3.84 | 10.66 | 17.59 | 2.00 | 76.6 | 75.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.55 | 10.43 | 17.45 | 6.00 | 59.5 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.58 | 10.37 | 17.26 | 14.00 | 68.7 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.80 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.63
- Actual score: 33.00
- Transfer: Tom Cairney -> Dwight McNeil (projected gain 1.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.40 | 10.21 | 16.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.74 | 1.13 | 0.00 | 8.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.30 | 14.08 | 23.49 | 5.00 | 83.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.86 | 13.83 | 23.68 | 2.00 | 73.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.33 | 12.56 | 19.40 | 2.00 | 78.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.43 | 10.47 | 1.00 | 77.8 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.40 | 4.30 | 6.95 | 5.00 | 45.6 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.36 | 25.34 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.63 | 17.16 | 1.00 | 76.4 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.26 | 4.13 | 6.63 | 0.00 | 35.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 20.46 | 33.64 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.86 | 18.07 | 28.65 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.77 | 13.35 | 21.07 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.48 | 10.41 | 17.07 | 2.00 | 59.7 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.09 | 9.73 | 16.06 | 2.00 | 80.8 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.86
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Bruno Guimarães Rodriguez Moura (projected gain 3.17, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.90 | 8.73 | 15.01 | 1.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.75 | 1.24 | 0.00 | 10.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.09 | 15.77 | 25.51 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.85 | 13.31 | 21.95 | 1.00 | 81.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.96 | 11.94 | 18.99 | 5.00 | 79.9 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.56 | 6.97 | 11.01 | 1.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.28 | 9.96 | 1.00 | 67.1 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.25 | 10.44 | 20.53 | 0.00 | 17.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.22 | 9.78 | 15.91 | 5.00 | 69.2 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.21 | 3.09 | 5.13 | 1.00 | 24.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.67 | 19.78 | 32.98 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.46 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.70 | 12.79 | 20.87 | 1.00 | 80.9 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 5.8 | 3.54 | 10.11 | 16.43 | 1.00 | 81.2 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.11 | 10.06 | 16.26 | 5.00 | 81.0 | 90.0 |