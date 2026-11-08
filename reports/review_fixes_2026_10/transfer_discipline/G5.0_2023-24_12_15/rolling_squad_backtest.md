# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 248.64
- Total actual points: 198.00
- Average predicted points: 62.16
- Average actual points: 49.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.97
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.88 | 10.57 | 16.88 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.66 | 10.03 | 16.28 | 4.00 | 83.0 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.37 | 16.95 | 26.88 | 1.00 | 96.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.49 | 11.58 | 18.15 | 9.00 | 92.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.28 | 18.05 | 1.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.2 | 3.80 | 10.54 | 16.82 | 2.00 | 69.8 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.81 | 10.09 | 16.10 | 1.00 | 81.7 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 3.85 | 11.24 | 17.99 | 5.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 3.71 | 9.77 | 15.15 | 1.00 | 61.2 | 9.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.83 | 13.07 | 2.00 | 69.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.06 | 21.03 | 34.47 | 16.00 | 104.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.73 | 16.87 | 27.95 | 2.00 | 91.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 5.98 | 15.93 | 25.98 | 5.00 | 87.8 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.83 | 15.81 | 24.64 | 8.00 | 106.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 13.38 | 20.86 | 1.00 | 85.6 | 45.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.58
- Actual score: 37.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Matty Cash replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.59 | 16.78 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.26 | 9.55 | 15.90 | 3.00 | 86.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.42 | 23.49 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.82 | 13.04 | 19.97 | 6.00 | 98.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.14 | 17.76 | 1.00 | 91.1 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 5.1 | 2.90 | 9.42 | 15.00 | 0.00 | 65.1 | 45.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.04 | 8.87 | 14.37 | 2.00 | 78.4 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 4.10 | 11.78 | 18.71 | 2.00 | 81.7 | 68.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.83 | 12.83 | 2.00 | 68.6 | 90.0 |
| Bench 3 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.40 | 7.64 | 12.29 | 1.00 | 39.1 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.71 | 21.95 | 35.97 | 5.00 | 106.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.07 | 16.96 | 26.86 | 8.00 | 94.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.89 | 14.80 | 24.58 | 2.00 | 84.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.59 | 12.97 | 20.80 | 0.00 | 74.5 | 0.0 |
| Bench 4 | Bench | Kaoru Mitoma | MID | 5 | 6.5 | 1.62 | 6.65 | 12.13 | 0.00 | 27.1 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.86
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.32) beats the best remaining Triple Captain opportunity (9.30).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 8.39, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.32) beats the best remaining Triple Captain opportunity (9.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 10.14 | 16.22 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.00 | 9.12 | 15.22 | 6.00 | 85.5 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.65 | 13.69 | 22.64 | 12.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.41 | 11.88 | 18.55 | 1.00 | 85.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.20 | 9.64 | 15.65 | 2.00 | 78.0 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 2.97 | 8.58 | 14.33 | 1.00 | 55.7 | 16.0 |
| Bench 2 | Bench | Fabian Schär | DEF | 15 | 5.2 | 2.78 | 8.27 | 13.59 | 6.00 | 75.9 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 3.71 | 10.67 | 16.76 | 5.00 | 65.1 | 71.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.98 | 13.12 | 1.00 | 71.7 | 45.0 |
| Bench 3 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.01 | 6.11 | 10.62 | 1.00 | 30.1 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.32 | 21.61 | 35.87 | 5.00 | 106.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.47 | 17.60 | 28.02 | 8.00 | 99.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 6.30 | 16.54 | 25.95 | 5.00 | 100.1 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.55 | 12.91 | 22.39 | 10.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Kaoru Mitoma | MID | 5 | 6.5 | 1.47 | 5.45 | 10.79 | 1.00 | 16.4 | 33.0 |

## GW15

- Train rows: 114034
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.24
- Actual score: 32.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.91) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nicolas Jackson -> Julián Álvarez (projected gain 5.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.91) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.20 | 9.49 | 15.41 | 0.00 | 87.3 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 2.62 | 8.15 | 13.86 | 0.00 | 74.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.47 | 15.31 | 24.83 | 1.00 | 98.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.17 | 11.59 | 18.47 | 1.00 | 84.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.63 | 9.89 | 16.27 | 1.00 | 82.1 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.10 | 8.76 | 14.28 | 1.00 | 78.0 | 90.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 1.34 | 5.60 | 10.11 | 0.00 | 33.4 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.29 | 12.63 | 20.77 | 2.00 | 73.2 | 67.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.17 | 6.68 | 10.90 | 2.00 | 59.6 | 90.0 |
| Bench 3 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 1.77 | 5.82 | 10.42 | 0.00 | 24.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.58 | 21.57 | 36.24 | 3.00 | 106.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.41 | 17.63 | 28.32 | 5.00 | 96.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.43 | 15.47 | 26.20 | 2.00 | 90.7 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.90 | 12.30 | 19.77 | 6.00 | 60.7 | 39.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 2.56 | 7.48 | 12.97 | 5.00 | 37.3 | 90.0 |