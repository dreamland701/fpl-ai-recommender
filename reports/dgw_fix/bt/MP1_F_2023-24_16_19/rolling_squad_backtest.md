# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 233.41
- Total actual points: 186.00
- Average predicted points: 58.35
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
- Predicted score: 61.27
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.12 | 15.54 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.90 | 24.44 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.57 | 14.03 | 23.28 | 4.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.46 | 10.64 | 17.39 | 5.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.76 | 6.20 | 10.47 | 1.00 | 73.4 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.29 | 6.09 | 9.96 | 5.00 | 74.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.41 | 24.77 | 40.21 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.58 | 9.90 | 16.08 | 9.00 | 77.9 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.72 | 4.29 | 6.51 | 0.00 | 37.5 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.26 | 33.38 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.50 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.06 | 12.26 | 19.64 | 2.00 | 78.2 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.19 | 11.52 | 18.30 | 2.00 | 88.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.76 | 11.43 | 19.22 | 1.00 | 81.6 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.19
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.21, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.73 | 15.75 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.06 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.52 | 14.56 | 23.97 | 9.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.81 | 13.51 | 21.52 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.01 | 19.40 | 0.00 | 72.4 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.15 | 6.46 | 10.36 | 1.00 | 74.3 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.46 | 9.54 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.64 | 14.42 | 26.54 | 0.00 | 34.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.39 | 10.46 | 16.94 | 2.00 | 79.7 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.39 | 4.28 | 6.57 | 1.00 | 35.9 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.16 | 22.08 | 35.86 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 18.46 | 29.40 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.81 | 10.84 | 17.45 | 6.00 | 68.6 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.41 | 17.30 | 14.00 | 68.9 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.86 | 9.07 | 14.95 | 2.00 | 67.5 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.47
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.14) beats the best remaining Bench Boost opportunity (3.27).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.14) beats the best remaining Bench Boost opportunity (3.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.56 | 10.19 | 16.53 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.03 | 0.18 | 0.12 | 0.00 | 1.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.23 | 13.92 | 23.26 | 5.00 | 82.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.45 | 12.80 | 19.76 | 2.00 | 80.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.57 | 11.00 | 18.66 | 2.00 | 56.2 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.96 | 6.35 | 10.36 | 1.00 | 77.2 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.24 | 3.95 | 6.42 | 5.00 | 42.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.71 | 27.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.60 | 10.52 | 17.01 | 1.00 | 75.2 | 85.0 |
| Bench 2 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.25 | 4.10 | 6.59 | 0.00 | 35.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.41 | 20.40 | 33.56 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 18.18 | 28.80 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.89 | 13.62 | 21.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.98 | 11.58 | 18.86 | 2.00 | 70.7 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.01 | 9.56 | 15.82 | 2.00 | 79.0 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.47
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.96 | 8.79 | 14.69 | 0.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.19 | 0.37 | 0.48 | 0.00 | 4.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.06 | 15.71 | 25.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.89 | 13.43 | 22.13 | 1.00 | 82.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 12.03 | 19.11 | 5.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.53 | 6.90 | 10.91 | 1.00 | 78.9 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.25 | 6.09 | 9.66 | 1.00 | 65.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.66 | 11.55 | 21.82 | 0.00 | 28.5 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.12 | 9.55 | 15.55 | 5.00 | 66.9 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.09 | 2.83 | 4.73 | 1.00 | 21.7 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.05 | 20.91 | 34.64 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.29 | 17.64 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.73 | 12.88 | 21.02 | 1.00 | 81.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.60 | 11.13 | 17.98 | 0.00 | 66.2 | 0.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.03 | 9.88 | 16.00 | 5.00 | 79.1 | 90.0 |