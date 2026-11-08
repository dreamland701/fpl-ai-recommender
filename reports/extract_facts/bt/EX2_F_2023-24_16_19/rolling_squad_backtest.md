# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 231.58
- Total actual points: 199.00
- Average predicted points: 57.89
- Average actual points: 49.75
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
- Predicted score: 61.60
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.33 | 9.24 | 15.64 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.46 | 0.76 | 1.11 | 0.00 | 8.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.01 | 14.72 | 24.12 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.77 | 14.44 | 23.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.50 | 10.66 | 17.42 | 5.00 | 76.1 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.84 | 6.35 | 10.64 | 1.00 | 75.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.25 | 10.16 | 5.00 | 76.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.34 | 24.56 | 39.81 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.12 | 16.34 | 9.00 | 80.6 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.80 | 4.44 | 6.66 | 0.00 | 40.1 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.83 | 20.41 | 33.56 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.70 | 17.34 | 27.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 12.36 | 19.71 | 2.00 | 79.7 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.23 | 11.61 | 18.39 | 2.00 | 89.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.77 | 11.42 | 19.17 | 1.00 | 82.6 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 58.33
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.19) beats the best remaining Bench Boost opportunity (4.98).
- Transfer: Kieran Trippier -> William Saliba (projected gain 2.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.19) beats the best remaining Bench Boost opportunity (4.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.59 | 8.74 | 14.34 | 10.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.49 | 0.62 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.62 | 14.77 | 24.25 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.60 | 13.05 | 21.03 | 8.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.10 | 11.58 | 18.21 | 7.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.27 | 6.69 | 10.64 | 1.00 | 77.2 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.42 | 9.32 | 0.00 | 0.0 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 3.13 | 11.22 | 20.99 | 0.00 | 4.2 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.53 | 10.75 | 17.32 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.50 | 4.49 | 6.83 | 1.00 | 39.1 | 32.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.84 | 21.14 | 33.74 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.46 | 19.99 | 32.85 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.52 | 10.75 | 18.18 | 6.00 | 58.8 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.66 | 10.49 | 17.37 | 14.00 | 71.0 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.04 | 9.43 | 15.45 | 2.00 | 71.8 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.04
- Actual score: 38.00
- Transfer: Hwang Hee-chan -> Pascal Groß (projected gain 2.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.35 | 10.15 | 16.91 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.78 | 1.25 | 0.00 | 9.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.22 | 13.99 | 23.46 | 5.00 | 82.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.25 | 12.44 | 19.32 | 2.00 | 76.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.49 | 10.89 | 17.44 | 2.00 | 86.9 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.36 | 10.45 | 1.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.39 | 4.30 | 7.01 | 5.00 | 46.1 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.58 | 25.51 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.57 | 10.53 | 17.11 | 1.00 | 75.2 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.23 | 4.10 | 6.66 | 0.00 | 35.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.35 | 20.34 | 33.56 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.77 | 17.95 | 28.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.68 | 13.24 | 21.02 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.65 | 11.72 | 19.50 | 7.00 | 78.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.40 | 10.33 | 17.04 | 2.00 | 57.9 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.62
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Bruno Guimarães Rodriguez Moura (projected gain 3.14, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.92 | 8.74 | 14.99 | 1.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.79 | 1.35 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.00 | 15.64 | 25.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.88 | 11.82 | 18.91 | 5.00 | 78.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.17 | 11.36 | 18.09 | 1.00 | 88.9 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.49 | 6.89 | 10.98 | 1.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.29 | 6.25 | 9.98 | 1.00 | 66.8 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.35 | 10.61 | 20.68 | 0.00 | 20.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.15 | 9.68 | 15.85 | 5.00 | 67.9 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.22 | 3.13 | 5.23 | 1.00 | 25.7 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.67 | 19.85 | 33.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.14 | 17.34 | 27.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.63 | 12.70 | 20.83 | 1.00 | 79.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.91 | 11.59 | 19.27 | 2.00 | 79.1 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 5.8 | 3.46 | 10.01 | 16.39 | 1.00 | 79.8 | 90.0 |