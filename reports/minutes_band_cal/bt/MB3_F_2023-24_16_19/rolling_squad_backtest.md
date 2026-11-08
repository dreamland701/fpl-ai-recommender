# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 233.53
- Total actual points: 194.00
- Average predicted points: 58.38
- Average actual points: 48.50
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
- Predicted score: 61.30
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.15 | 15.57 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.28 | 0.47 | 0.82 | 0.00 | 4.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.67 | 24.09 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.72 | 14.38 | 23.83 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.43 | 10.56 | 17.19 | 5.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.76 | 6.20 | 10.36 | 1.00 | 75.3 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.12 | 9.91 | 5.00 | 76.2 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 24.60 | 39.92 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.01 | 16.13 | 9.00 | 80.8 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.66 | 4.21 | 6.45 | 0.00 | 36.4 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.83 | 20.42 | 33.62 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.69 | 17.32 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.08 | 12.30 | 19.57 | 2.00 | 80.4 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.22 | 11.61 | 18.44 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.72 | 11.36 | 19.11 | 1.00 | 80.8 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.92
- Actual score: 61.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.49, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.53 | 8.62 | 14.24 | 10.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.20 | 0.35 | 0.00 | 5.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.60 | 14.74 | 24.25 | 9.00 | 89.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.71 | 13.28 | 21.18 | 8.00 | 89.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.36 | 10.05 | 18.04 | 0.00 | 64.4 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.55 | 10.38 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.33 | 9.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.48 | 14.02 | 25.97 | 0.00 | 31.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.69 | 17.29 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.37 | 4.27 | 6.64 | 1.00 | 35.6 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.22 | 22.20 | 36.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.33 | 18.41 | 29.33 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.96 | 11.23 | 18.15 | 6.00 | 73.4 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.69 | 10.65 | 17.78 | 14.00 | 72.3 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.33 | 10.09 | 16.69 | 1.00 | 81.3 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 54.86
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.67) beats the best remaining Bench Boost opportunity (3.92).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 2.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.67) beats the best remaining Bench Boost opportunity (3.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.39 | 10.18 | 16.86 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.27 | 0.64 | 1.05 | 0.00 | 7.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.30 | 14.08 | 23.50 | 5.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.36 | 12.60 | 19.34 | 2.00 | 80.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.85 | 11.72 | 19.91 | 2.00 | 64.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.39 | 10.31 | 1.00 | 79.3 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.58 | 4.78 | 7.72 | 5.00 | 50.1 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.85 | 27.46 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.60 | 17.01 | 1.00 | 77.7 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.20 | 4.03 | 6.54 | 0.00 | 34.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 20.47 | 33.66 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.05 | 28.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.80 | 13.42 | 21.20 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.65 | 10.89 | 17.86 | 2.00 | 63.7 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.09 | 9.72 | 16.07 | 2.00 | 80.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.45
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.18 | 9.41 | 15.57 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.27 | 0.65 | 1.16 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.11 | 15.81 | 25.58 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.30 | 21.94 | 1.00 | 81.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.96 | 11.91 | 18.82 | 5.00 | 81.4 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.55 | 6.90 | 10.79 | 1.00 | 81.0 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.42 | 6.52 | 10.43 | 1.00 | 70.6 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.46 | 11.03 | 21.05 | 0.00 | 24.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.30 | 10.01 | 16.37 | 5.00 | 72.6 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.15 | 2.98 | 5.03 | 1.00 | 23.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 21.02 | 34.81 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.45 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.71 | 12.82 | 20.92 | 1.00 | 80.7 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.25 | 10.40 | 16.87 | 0.00 | 59.1 | 0.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.10 | 10.05 | 16.25 | 5.00 | 80.9 | 90.0 |