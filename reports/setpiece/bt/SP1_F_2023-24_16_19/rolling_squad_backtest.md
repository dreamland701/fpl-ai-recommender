# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.15
- Total actual points: 189.00
- Average predicted points: 58.04
- Average actual points: 47.25
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
- Predicted score: 61.41
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.14 | 15.57 | 1.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.57 | 0.92 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.17 | 15.44 | 25.49 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.78 | 14.53 | 24.11 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.89 | 17.91 | 5.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.77 | 6.27 | 10.58 | 1.00 | 73.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.32 | 6.17 | 10.10 | 5.00 | 74.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.24 | 24.12 | 38.98 | 0.00 | 90.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.40 | 17.04 | 9.00 | 79.5 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.71 | 4.27 | 6.45 | 0.00 | 37.4 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.76 | 20.18 | 33.26 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.66 | 17.32 | 27.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.87 | 12.02 | 20.30 | 1.00 | 82.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.03 | 12.00 | 19.11 | 2.00 | 78.3 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.18 | 11.52 | 18.21 | 2.00 | 88.2 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.09
- Actual score: 55.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.15, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.14 | 9.76 | 15.81 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.30 | 0.45 | 0.00 | 6.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.66 | 14.91 | 24.55 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.78 | 13.54 | 21.66 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.43 | 10.53 | 18.87 | 0.00 | 63.2 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.21 | 6.61 | 10.61 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.39 | 9.46 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.42 | 13.59 | 25.03 | 0.00 | 31.1 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.54 | 11.07 | 18.06 | 2.00 | 82.3 | 90.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.42 | 4.33 | 6.64 | 1.00 | 36.6 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.17 | 22.02 | 35.77 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.31 | 18.40 | 29.27 | 3.00 | 90.0 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.73 | 11.04 | 18.42 | 14.00 | 69.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.79 | 10.59 | 16.93 | 6.00 | 69.2 | 83.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.96 | 9.32 | 15.29 | 2.00 | 69.6 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 55.02
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.60) beats the best remaining Bench Boost opportunity (3.83).
- Transfer: Anthony Gordon -> James Ward-Prowse (projected gain 0.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.60) beats the best remaining Bench Boost opportunity (3.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.55 | 10.18 | 16.54 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.75 | 1.16 | 0.00 | 8.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.43 | 14.57 | 24.39 | 5.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.42 | 12.77 | 19.76 | 2.00 | 79.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.90 | 12.07 | 20.50 | 2.00 | 62.5 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.43 | 10.49 | 1.00 | 77.7 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.40 | 4.30 | 6.95 | 5.00 | 45.5 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.96 | 25.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.70 | 10.99 | 17.91 | 1.00 | 76.4 | 85.0 |
| Bench 3 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.25 | 4.08 | 6.53 | 0.00 | 35.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.39 | 20.24 | 33.28 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.80 | 17.98 | 28.44 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.93 | 14.04 | 22.34 | 1.00 | 90.0 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.1 | 3.38 | 10.71 | 17.38 | 3.00 | 81.0 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.17 | 9.50 | 16.17 | 2.00 | 72.9 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.64
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hwang Hee-chan -> Morgan Gibbs-White (projected gain 0.76, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.06) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.78 | 14.69 | 0.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.76 | 1.26 | 0.00 | 10.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.21 | 16.18 | 26.26 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.99 | 13.91 | 23.06 | 1.00 | 83.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.04 | 12.25 | 19.59 | 5.00 | 80.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.55 | 6.97 | 11.02 | 1.00 | 79.4 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.33 | 6.31 | 10.00 | 1.00 | 67.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.41 | 10.78 | 20.45 | 0.00 | 23.7 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.27 | 10.16 | 16.68 | 5.00 | 69.4 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.20 | 3.02 | 5.00 | 1.00 | 24.2 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.06 | 20.86 | 34.54 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.20 | 17.51 | 28.04 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.19 | 10.50 | 17.18 | 0.00 | 55.2 | 0.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.0 | 3.00 | 10.33 | 17.51 | 6.00 | 79.9 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 5.7 | 3.17 | 9.96 | 16.14 | 2.00 | 81.5 | 90.0 |