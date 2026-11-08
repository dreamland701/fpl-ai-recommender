# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 246.68
- Total actual points: 246.00
- Average predicted points: 61.67
- Average actual points: 61.50
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.66
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.16 | 15.29 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.15 | 8.93 | 14.59 | 9.00 | 83.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.60 | 23.98 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.57 | 13.76 | 22.94 | 4.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.47 | 10.76 | 17.50 | 2.00 | 81.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.64 | 10.22 | 16.69 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.46 | 9.91 | 16.39 | 5.00 | 75.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.58 | 9.60 | 15.57 | 9.00 | 77.9 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.23 | 8.71 | 14.23 | 2.00 | 59.1 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.06 | 11.12 | 2.00 | 66.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.50 | 34.17 | 13.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.41 | 28.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.88 | 14.37 | 24.12 | 17.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.76 | 11.44 | 19.17 | 1.00 | 81.6 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.19 | 10.84 | 17.40 | 2.00 | 88.4 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 58.63
- Actual score: 60.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.04, hit 0)
- Autosub: Abdoulaye Doucouré replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.55 | 15.79 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.48 | 8.38 | 13.83 | 10.00 | 83.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.52 | 13.96 | 22.96 | 9.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.81 | 12.72 | 20.46 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.05 | 11.55 | 18.44 | 7.00 | 83.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.19 | 19.42 | 0.00 | 72.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.38 | 10.17 | 16.65 | 6.00 | 82.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.39 | 9.91 | 16.25 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.37 | 8.13 | 13.29 | 1.00 | 52.8 | 30.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.63 | 7.07 | 11.41 | 2.00 | 66.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 7.16 | 22.15 | 36.66 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.6 | 7.24 | 19.37 | 31.86 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 18.46 | 29.86 | 3.00 | 90.0 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.08 | 16.65 | 14.00 | 68.9 | 90.0 |
| Bench 2 | Autosub In | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.21 | 9.52 | 15.93 | 1.00 | 78.6 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.96
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.72) beats the best remaining Triple Captain opportunity (8.14).
- Transfer: Abdoulaye Doucouré -> Hwang Hee-chan (projected gain 0.08, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.72) beats the best remaining Triple Captain opportunity (8.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.56 | 10.20 | 16.68 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.35 | 9.83 | 16.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.23 | 13.36 | 22.13 | 5.00 | 82.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.45 | 11.84 | 18.30 | 2.00 | 80.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.55 | 10.87 | 17.64 | 2.00 | 87.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.57 | 10.48 | 17.93 | 2.00 | 56.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.19 | 10.14 | 16.79 | 2.00 | 82.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.60 | 9.97 | 16.24 | 1.00 | 75.2 | 85.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.54 | 7.45 | 12.73 | 2.00 | 41.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.53 | 7.23 | 11.43 | 8.00 | 74.2 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.41 | 20.59 | 34.31 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 18.24 | 29.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.81 | 16.78 | 26.62 | 7.00 | 85.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.89 | 12.86 | 20.44 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Hwang Hee-chan | MID | 20 | 5.8 | 3.08 | 8.98 | 15.48 | 2.00 | 70.9 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 70.42
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.16 | 9.28 | 15.49 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.96 | 8.85 | 14.69 | 0.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.06 | 15.33 | 24.91 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.89 | 13.49 | 22.45 | 1.00 | 82.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.30 | 11.69 | 18.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 11.37 | 18.37 | 5.00 | 80.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.50 | 10.54 | 17.19 | 7.00 | 83.6 | 90.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.12 | 9.04 | 14.85 | 5.00 | 66.9 | 90.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.10 | 8.42 | 13.50 | 16.00 | 63.0 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.21 | 8.31 | 13.53 | 5.00 | 78.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.05 | 21.54 | 35.90 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.29 | 17.91 | 29.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.03 | 17.86 | 29.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 10.38 | 16.82 | 0.00 | 66.2 | 0.0 |
| Bench 2 | Bench Boost | Hwang Hee-chan | MID | 20 | 5.7 | 3.12 | 8.81 | 14.30 | 14.00 | 74.8 | 45.0 |