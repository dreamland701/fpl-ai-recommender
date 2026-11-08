# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 235.44
- Total actual points: 182.00
- Average predicted points: 58.86
- Average actual points: 45.50
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
- Predicted score: 60.79
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.15 | 15.57 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.83 | 4.48 | 7.06 | 0.00 | 48.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.95 | 14.59 | 23.95 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.69 | 14.33 | 23.72 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.41 | 10.54 | 17.26 | 5.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.25 | 10.56 | 1.00 | 73.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.32 | 6.17 | 10.08 | 5.00 | 74.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.29 | 24.45 | 39.67 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.62 | 10.03 | 16.25 | 9.00 | 79.3 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.71 | 4.30 | 6.51 | 0.00 | 37.3 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.68 | 20.16 | 34.07 | 13.00 | 88.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.63 | 17.20 | 27.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.07 | 12.29 | 19.64 | 2.00 | 78.5 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.19 | 11.55 | 18.34 | 2.00 | 88.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.68 | 11.26 | 18.96 | 1.00 | 80.2 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 58.97
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.77) beats the best remaining Bench Boost opportunity (5.71).
- Transfer: André Onana -> Bernd Leno (projected gain 1.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.77) beats the best remaining Bench Boost opportunity (5.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.72 | 15.73 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.73 | 2.35 | 3.96 | 1.00 | 26.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.56 | 14.65 | 24.10 | 9.00 | 89.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.66 | 13.18 | 21.02 | 8.00 | 89.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.29 | 9.85 | 17.58 | 0.00 | 61.7 | 0.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.21 | 6.60 | 10.56 | 1.00 | 75.6 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.34 | 9.36 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.47 | 10.68 | 17.25 | 2.00 | 81.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 2.76 | 10.30 | 21.44 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.42 | 4.37 | 6.70 | 1.00 | 36.6 | 32.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.15 | 22.07 | 35.80 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.46 | 19.73 | 32.90 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 11.08 | 18.89 | 6.00 | 64.5 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.58 | 10.37 | 17.24 | 14.00 | 68.6 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.98 | 9.36 | 15.37 | 2.00 | 70.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.97
- Actual score: 32.00
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.54 | 10.14 | 16.45 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.77 | 5.02 | 7.90 | 0.00 | 52.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.26 | 14.02 | 23.37 | 5.00 | 83.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.35 | 12.70 | 21.44 | 2.00 | 74.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.30 | 12.52 | 19.30 | 2.00 | 77.9 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.42 | 10.46 | 1.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.40 | 4.30 | 6.94 | 5.00 | 45.6 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.74 | 27.11 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.64 | 10.62 | 17.14 | 1.00 | 76.2 | 85.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.25 | 4.12 | 6.61 | 0.00 | 35.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.40 | 20.38 | 33.49 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.80 | 17.97 | 28.45 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.76 | 13.32 | 21.03 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.45 | 10.37 | 16.99 | 2.00 | 59.3 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.08 | 9.70 | 16.02 | 2.00 | 80.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.71
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.41) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Scott McTominay (projected gain 3.86, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.41) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.76 | 14.65 | 0.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.75 | 2.48 | 4.02 | 0.00 | 24.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.05 | 15.70 | 25.41 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.83 | 13.28 | 21.88 | 1.00 | 81.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.93 | 11.90 | 18.92 | 5.00 | 79.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.55 | 6.96 | 10.99 | 1.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.28 | 9.95 | 1.00 | 67.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.88 | 11.30 | 22.58 | 0.00 | 22.7 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.20 | 9.75 | 15.86 | 5.00 | 69.0 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.21 | 3.09 | 5.13 | 1.00 | 24.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.41 | 21.05 | 36.03 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.17 | 17.37 | 27.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.70 | 12.77 | 20.84 | 1.00 | 80.7 | 90.0 |
| XI | XI | Scott McTominay | MID | 14 | 4.9 | 3.68 | 10.78 | 17.85 | 1.00 | 90.0 | 9.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.09 | 10.03 | 16.21 | 5.00 | 80.8 | 90.0 |