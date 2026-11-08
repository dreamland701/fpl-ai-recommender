# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 233.48
- Total actual points: 186.00
- Average predicted points: 58.37
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
- Predicted score: 61.31
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.12 | 15.52 | 1.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.62 | 1.01 | 0.00 | 5.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.67 | 24.08 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.72 | 14.37 | 23.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.44 | 10.59 | 17.35 | 5.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.76 | 6.22 | 10.49 | 1.00 | 73.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.12 | 9.99 | 5.00 | 74.5 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 24.56 | 39.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.02 | 16.25 | 9.00 | 79.1 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.72 | 4.35 | 6.61 | 0.00 | 37.5 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.83 | 20.42 | 33.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.69 | 17.32 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.09 | 12.34 | 19.75 | 2.00 | 78.8 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.23 | 11.62 | 18.47 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.73 | 11.42 | 19.24 | 1.00 | 81.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.96
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.09, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.67 | 15.64 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.36 | 0.56 | 0.00 | 6.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.60 | 14.76 | 24.29 | 9.00 | 89.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.71 | 13.33 | 21.29 | 8.00 | 89.7 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.23 | 9.54 | 17.03 | 0.00 | 60.1 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.54 | 10.46 | 1.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.28 | 9.24 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.58 | 14.48 | 26.81 | 0.00 | 33.7 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.66 | 17.22 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.42 | 4.33 | 6.65 | 1.00 | 36.5 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.23 | 22.21 | 36.06 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.33 | 18.40 | 29.32 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.86 | 10.96 | 17.62 | 6.00 | 69.8 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.42 | 17.32 | 14.00 | 68.8 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.98 | 9.33 | 15.33 | 2.00 | 70.2 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.71
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.59) beats the best remaining Bench Boost opportunity (3.82).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.59) beats the best remaining Bench Boost opportunity (3.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.54 | 10.13 | 16.43 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.80 | 1.25 | 0.00 | 8.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.29 | 14.05 | 23.44 | 5.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.35 | 12.59 | 19.43 | 2.00 | 78.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.75 | 11.46 | 19.36 | 2.00 | 60.3 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.36 | 10.36 | 1.00 | 77.5 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.39 | 4.23 | 6.81 | 5.00 | 45.3 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 15.12 | 28.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.56 | 17.05 | 1.00 | 75.9 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.25 | 4.07 | 6.52 | 0.00 | 35.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 20.43 | 33.59 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.84 | 18.02 | 28.55 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.81 | 13.43 | 21.24 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.57 | 11.33 | 18.96 | 2.00 | 61.8 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.08 | 9.69 | 16.00 | 2.00 | 80.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.50
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Bruno Guimarães Rodriguez Moura (projected gain 0.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.94 | 8.70 | 14.54 | 0.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.80 | 1.36 | 0.00 | 10.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.11 | 15.82 | 25.62 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.30 | 21.92 | 1.00 | 81.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.95 | 11.91 | 18.92 | 5.00 | 79.5 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.54 | 6.90 | 10.89 | 1.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.32 | 6.27 | 9.93 | 1.00 | 67.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.56 | 11.59 | 22.06 | 0.00 | 26.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.21 | 9.72 | 15.80 | 5.00 | 68.8 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.20 | 3.03 | 5.03 | 1.00 | 24.1 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 20.99 | 34.74 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.21 | 17.43 | 27.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.70 | 12.81 | 20.90 | 1.00 | 80.7 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 5.8 | 3.55 | 10.12 | 16.47 | 1.00 | 81.2 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.10 | 10.03 | 16.22 | 5.00 | 80.8 | 90.0 |