# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 249.80
- Total actual points: 214.00
- Average predicted points: 62.45
- Average actual points: 53.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.41
- Actual score: 65.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 4.07 | 9.12 | 15.54 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.7 | 3.62 | 9.02 | 14.62 | 9.00 | 87.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.35 | 14.90 | 24.44 | -1.00 | 86.6 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.68 | 14.03 | 23.28 | 4.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.56 | 10.64 | 17.39 | 5.00 | 86.6 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.5 | 2.63 | 10.55 | 17.00 | 2.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 4.11 | 10.45 | 16.93 | 2.00 | 84.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.89 | 9.90 | 16.08 | 9.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.53 | 7.46 | 11.69 | 2.00 | 74.4 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.58 | 7.40 | 11.73 | 2.00 | 65.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.73 | 20.26 | 33.38 | 13.00 | 74.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 4.10 | 17.50 | 28.27 | 2.00 | 86.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 5.03 | 14.63 | 24.47 | 17.00 | 80.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.24 | 12.26 | 19.64 | 2.00 | 85.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.90 | 11.43 | 19.22 | 1.00 | 82.9 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.02
- Actual score: 53.00
- Transfer: Cole Palmer -> Abdoulaye Doucouré (projected gain 0.43, hit 0)
- Autosub: Abdoulaye Doucouré replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.24 | 9.73 | 15.75 | 3.00 | 88.4 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.17 | 8.53 | 14.10 | 10.00 | 84.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.33 | 14.56 | 23.97 | 9.00 | 88.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.90 | 13.51 | 21.52 | 8.00 | 84.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.03 | 11.49 | 18.15 | 7.00 | 85.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 4.08 | 11.01 | 19.40 | 0.00 | 68.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 4.12 | 10.45 | 16.85 | 6.00 | 84.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.44 | 10.46 | 16.94 | 2.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.24 | 7.84 | 12.02 | 0.00 | 67.9 | 22.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.75 | 7.69 | 12.22 | 2.00 | 70.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.97 | 22.08 | 35.86 | 3.00 | 86.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.55 | 20.31 | 32.94 | 2.00 | 85.3 | 87.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 7.29 | 18.46 | 29.40 | 3.00 | 86.8 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.76 | 10.84 | 17.45 | 6.00 | 78.0 | 83.0 |
| Bench 2 | Autosub In | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.75 | 9.82 | 16.28 | 1.00 | 85.8 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.78
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (9.91).
- Transfer: Abdoulaye Doucouré -> Cole Palmer (projected gain 2.71, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (9.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.59 | 10.19 | 16.53 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.40 | 10.10 | 16.74 | 2.00 | 89.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.90 | 13.92 | 23.26 | 5.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.48 | 12.80 | 19.76 | 2.00 | 85.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.60 | 11.00 | 18.66 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.5 | 1.92 | 10.95 | 17.46 | 2.00 | 85.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.56 | 10.36 | 16.93 | 2.00 | 84.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.88 | 10.52 | 17.01 | 1.00 | 83.0 | 85.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 1.89 | 7.65 | 12.03 | 8.00 | 79.3 | 89.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 0.03 | 4.38 | 8.08 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.80 | 20.40 | 33.56 | 7.00 | 86.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 3.49 | 18.18 | 28.80 | 1.00 | 83.4 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 6.39 | 17.38 | 27.43 | 7.00 | 86.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 3.18 | 13.62 | 21.50 | 1.00 | 85.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 5.32 | 11.58 | 18.86 | 2.00 | 78.0 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 69.59
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 4.31 | 9.37 | 15.52 | 1.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.7 | 2.82 | 8.79 | 14.69 | 0.00 | 83.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 3.97 | 15.71 | 25.42 | 8.00 | 88.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.52 | 13.43 | 22.13 | 1.00 | 78.4 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.4 | 3.49 | 12.03 | 19.11 | 5.00 | 86.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.88 | 11.58 | 18.33 | 1.00 | 85.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.90 | 10.49 | 17.11 | 7.00 | 85.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.56 | 9.55 | 15.55 | 5.00 | 78.6 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 4.13 | 8.60 | 13.87 | 5.00 | 84.9 | 85.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 2.32 | 3.89 | 6.68 | 5.00 | 51.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.2 | 6.20 | 20.91 | 34.64 | 3.00 | 88.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.80 | 17.92 | 29.31 | 5.00 | 85.3 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.35 | 17.64 | 28.27 | 2.00 | 84.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 5.29 | 12.88 | 21.02 | 1.00 | 83.6 | 90.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.6 | 2.69 | 11.13 | 17.98 | 0.00 | 75.2 | 0.0 |