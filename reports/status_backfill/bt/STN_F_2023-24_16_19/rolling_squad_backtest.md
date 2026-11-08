# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.17
- Total actual points: 187.00
- Average predicted points: 59.79
- Average actual points: 46.75
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
- Predicted score: 62.03
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.15 | 15.57 | 1.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.35 | 0.69 | 0.00 | 6.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.67 | 24.09 | -1.00 | 93.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.83 | 14.38 | 23.83 | 4.00 | 92.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.61 | 10.59 | 17.34 | 5.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.79 | 6.23 | 10.52 | 1.00 | 74.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.33 | 6.15 | 10.06 | 5.00 | 75.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.28 | 24.60 | 39.92 | 0.00 | 109.3 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.04 | 16.28 | 9.00 | 79.3 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.75 | 4.31 | 6.53 | 0.00 | 37.7 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.77 | 20.42 | 33.62 | 13.00 | 95.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.77 | 17.32 | 28.00 | 2.00 | 95.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.32 | 12.33 | 19.73 | 2.00 | 81.8 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.44 | 11.61 | 18.44 | 2.00 | 91.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.81 | 11.36 | 19.11 | 1.00 | 80.4 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.77
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.10, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.14 | 9.73 | 15.74 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.32 | 0.56 | 0.86 | 0.00 | 6.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.76 | 14.74 | 24.25 | 9.00 | 93.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.13 | 13.28 | 21.18 | 8.00 | 96.4 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 2.93 | 9.81 | 17.56 | 0.00 | 57.3 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.22 | 6.58 | 10.55 | 1.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.38 | 5.33 | 9.34 | 0.00 | 54.1 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 3.71 | 14.11 | 26.04 | 0.00 | 19.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.56 | 10.69 | 17.29 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.50 | 4.37 | 6.72 | 1.00 | 38.2 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.25 | 22.20 | 36.05 | 3.00 | 111.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.40 | 18.41 | 29.33 | 3.00 | 99.8 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.00 | 10.99 | 17.66 | 6.00 | 71.4 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.64 | 10.41 | 17.29 | 14.00 | 68.3 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.98 | 9.37 | 15.40 | 2.00 | 69.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.35
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.71) beats the best remaining Triple Captain opportunity (8.12).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.20, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.71) beats the best remaining Triple Captain opportunity (8.12).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.64 | 10.16 | 16.48 | 1.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.29 | 0.75 | 0.99 | 0.00 | 7.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.34 | 14.08 | 23.50 | 5.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.74 | 12.62 | 19.47 | 2.00 | 85.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.00 | 11.48 | 19.42 | 2.00 | 63.9 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.00 | 6.40 | 10.44 | 1.00 | 79.1 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.40 | 4.28 | 6.92 | 5.00 | 45.8 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.10 | 14.61 | 26.97 | 0.00 | 27.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.75 | 10.61 | 17.14 | 1.00 | 77.9 | 85.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.28 | 4.13 | 6.62 | 0.00 | 36.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.40 | 20.47 | 33.66 | 7.00 | 97.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.87 | 18.05 | 28.62 | 1.00 | 96.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.08 | 13.42 | 21.20 | 1.00 | 97.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.54 | 10.39 | 17.05 | 2.00 | 58.9 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.11 | 9.72 | 16.07 | 2.00 | 80.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.02
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> André Onana (projected gain 0.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.11 | 9.41 | 15.57 | 1.00 | 91.8 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.43 | 0.92 | 1.32 | 0.00 | 9.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.30 | 15.81 | 25.58 | 8.00 | 99.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.79 | 13.30 | 21.94 | 1.00 | 81.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.11 | 11.95 | 19.00 | 5.00 | 82.9 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.56 | 6.94 | 10.97 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.27 | 9.94 | 1.00 | 67.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 2.72 | 11.13 | 21.13 | 0.00 | 14.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.28 | 9.76 | 15.88 | 5.00 | 69.8 | 90.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.21 | 3.08 | 5.12 | 1.00 | 24.2 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.99 | 21.02 | 34.81 | 3.00 | 105.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.20 | 17.45 | 28.00 | 2.00 | 94.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.79 | 12.82 | 20.92 | 1.00 | 82.2 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.11 | 10.05 | 16.25 | 5.00 | 80.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.11 | 9.91 | 16.08 | 0.00 | 55.2 | 0.0 |