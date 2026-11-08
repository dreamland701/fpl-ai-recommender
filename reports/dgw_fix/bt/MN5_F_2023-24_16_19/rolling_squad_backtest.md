# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.85
- Total actual points: 187.00
- Average predicted points: 59.96
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
- Predicted score: 62.05
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.26 | 9.12 | 15.54 | 1.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.07 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.90 | 24.44 | -1.00 | 95.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.03 | 23.28 | 4.00 | 89.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.63 | 10.64 | 17.39 | 5.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.20 | 10.47 | 1.00 | 74.5 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.09 | 9.96 | 5.00 | 75.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 24.77 | 40.21 | 0.00 | 110.8 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.63 | 9.90 | 16.08 | 9.00 | 78.1 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.74 | 4.29 | 6.51 | 0.00 | 37.6 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.70 | 20.26 | 33.38 | 13.00 | 93.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.84 | 17.50 | 28.27 | 2.00 | 97.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.30 | 12.26 | 19.64 | 2.00 | 81.2 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.41 | 11.52 | 18.30 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.83 | 11.43 | 19.22 | 1.00 | 81.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.05
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 2.63, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.14 | 9.73 | 15.75 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.56 | 23.97 | 9.00 | 91.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.23 | 13.51 | 21.52 | 8.00 | 98.5 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.41 | 11.01 | 19.40 | 0.00 | 68.0 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.17 | 6.46 | 10.36 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.44 | 5.46 | 9.54 | 0.00 | 55.3 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 3.83 | 14.42 | 26.54 | 0.00 | 22.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.48 | 10.46 | 16.94 | 2.00 | 80.1 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.47 | 4.28 | 6.57 | 1.00 | 37.4 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.21 | 22.08 | 35.86 | 3.00 | 110.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.42 | 18.46 | 29.40 | 3.00 | 100.2 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.94 | 10.84 | 17.45 | 6.00 | 70.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.64 | 10.41 | 17.30 | 14.00 | 68.3 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.86 | 9.07 | 14.95 | 2.00 | 66.7 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.64
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.20, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.68) beats the best remaining Triple Captain opportunity (8.09).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.65 | 10.19 | 16.53 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 5.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.27 | 13.92 | 23.26 | 5.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.82 | 12.80 | 19.76 | 2.00 | 87.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.81 | 11.00 | 18.66 | 2.00 | 59.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.35 | 10.36 | 1.00 | 78.6 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.27 | 3.95 | 6.42 | 5.00 | 42.8 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.14 | 14.71 | 27.12 | 0.00 | 28.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.72 | 10.52 | 17.01 | 1.00 | 77.1 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.27 | 4.10 | 6.59 | 0.00 | 36.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.37 | 20.40 | 33.56 | 7.00 | 96.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.91 | 18.18 | 28.80 | 1.00 | 97.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 5.16 | 13.62 | 21.50 | 1.00 | 99.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.02 | 11.58 | 18.86 | 2.00 | 69.4 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.04 | 9.56 | 15.82 | 2.00 | 79.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.11
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> André Onana (projected gain 1.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.09 | 9.37 | 15.52 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.18 | 0.26 | 0.42 | 0.00 | 5.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.26 | 15.71 | 25.42 | 8.00 | 98.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.43 | 22.13 | 1.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.14 | 12.03 | 19.11 | 5.00 | 83.6 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.54 | 6.90 | 10.91 | 1.00 | 79.9 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.26 | 6.09 | 9.66 | 1.00 | 65.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 2.88 | 11.55 | 21.82 | 0.00 | 18.4 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.19 | 9.55 | 15.55 | 5.00 | 67.9 | 90.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.11 | 2.83 | 4.73 | 1.00 | 21.9 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.95 | 20.91 | 34.64 | 3.00 | 104.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.28 | 17.64 | 28.27 | 2.00 | 96.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.81 | 12.88 | 21.02 | 1.00 | 82.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 11.13 | 17.98 | 0.00 | 66.2 | 0.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.05 | 9.88 | 16.00 | 5.00 | 79.0 | 90.0 |