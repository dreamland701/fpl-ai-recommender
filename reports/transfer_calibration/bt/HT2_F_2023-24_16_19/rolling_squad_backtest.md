# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 236.67
- Total actual points: 186.00
- Average predicted points: 59.17
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
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.15 | 15.57 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.83 | 4.48 | 7.06 | 0.00 | 48.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.67 | 24.09 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.72 | 14.38 | 23.83 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.44 | 10.59 | 17.34 | 5.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.77 | 6.23 | 10.52 | 1.00 | 73.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.15 | 10.06 | 5.00 | 74.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 24.60 | 39.92 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 10.04 | 16.28 | 9.00 | 79.2 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.71 | 4.31 | 6.53 | 0.00 | 37.4 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.83 | 20.42 | 33.62 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.69 | 17.32 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.09 | 12.33 | 19.73 | 2.00 | 78.8 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.22 | 11.61 | 18.44 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.72 | 11.36 | 19.11 | 1.00 | 80.8 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 1
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.29
- Actual score: 54.00
- Transfer: André Onana, Hwang Hee-chan -> Abdoulaye Doucouré, Bernd Leno (projected gain 1.83, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.73 | 15.74 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.73 | 2.34 | 3.95 | 1.00 | 26.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.60 | 14.74 | 24.25 | 9.00 | 89.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.71 | 13.28 | 21.18 | 8.00 | 89.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.26 | 9.81 | 17.56 | 0.00 | 60.9 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.58 | 10.55 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.33 | 9.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.54 | 14.11 | 26.04 | 0.00 | 32.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.69 | 17.29 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.42 | 4.37 | 6.72 | 1.00 | 36.6 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.22 | 22.20 | 36.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.33 | 18.41 | 29.33 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.87 | 10.99 | 17.66 | 6.00 | 69.9 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.41 | 17.29 | 14.00 | 68.8 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.33 | 10.09 | 16.69 | 1.00 | 81.3 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.20 -> 0.40
- Free transfers: 1 -> 1
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 58.13
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.76) beats the best remaining Triple Captain opportunity (8.19).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 3.10, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.76) beats the best remaining Triple Captain opportunity (8.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.55 | 10.16 | 16.48 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.77 | 5.02 | 7.89 | 0.00 | 52.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.30 | 14.08 | 23.50 | 5.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.36 | 12.62 | 19.47 | 2.00 | 78.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.75 | 11.48 | 19.42 | 2.00 | 60.4 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.40 | 10.44 | 1.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.39 | 4.28 | 6.92 | 5.00 | 45.5 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.61 | 26.97 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.61 | 17.14 | 1.00 | 76.1 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.25 | 4.13 | 6.62 | 0.00 | 35.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 20.47 | 33.66 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.05 | 28.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.80 | 13.42 | 21.20 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.47 | 10.39 | 17.05 | 2.00 | 59.1 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.09 | 9.72 | 16.07 | 2.00 | 80.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.30
- Free transfers: 1 -> 1
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.94
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.82) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> André Onana (projected gain 0.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.82) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.18 | 9.41 | 15.57 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.74 | 2.47 | 4.01 | 0.00 | 24.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.11 | 15.81 | 25.58 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.30 | 21.94 | 1.00 | 81.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.95 | 11.95 | 19.00 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.55 | 6.94 | 10.97 | 1.00 | 79.3 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.27 | 9.94 | 1.00 | 67.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.51 | 11.13 | 21.13 | 0.00 | 25.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.21 | 9.76 | 15.88 | 5.00 | 69.0 | 90.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.20 | 3.08 | 5.12 | 1.00 | 24.2 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 21.02 | 34.81 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.45 | 28.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.71 | 12.82 | 20.92 | 1.00 | 80.7 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.10 | 10.05 | 16.25 | 5.00 | 80.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.07 | 9.91 | 16.08 | 0.00 | 54.4 | 0.0 |