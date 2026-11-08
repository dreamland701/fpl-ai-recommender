# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 250.89
- Total actual points: 216.00
- Average predicted points: 62.72
- Average actual points: 54.00
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
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.89
- Actual score: 39.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.71, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.59 | 16.78 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.26 | 9.55 | 15.90 | 3.00 | 86.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.42 | 23.49 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.82 | 13.04 | 19.97 | 6.00 | 98.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.14 | 17.76 | 1.00 | 91.1 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 5.1 | 2.90 | 9.42 | 15.00 | 0.00 | 65.1 | 45.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.04 | 8.87 | 14.37 | 2.00 | 78.4 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 7 | 6.8 | 4.10 | 11.78 | 18.71 | 2.00 | 81.7 | 68.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.83 | 12.83 | 2.00 | 68.6 | 90.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.40 | 7.64 | 12.29 | 1.00 | 39.1 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.71 | 21.95 | 35.97 | 5.00 | 106.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 6.07 | 16.96 | 26.86 | 8.00 | 94.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.89 | 14.80 | 24.58 | 2.00 | 84.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.59 | 12.97 | 20.80 | 0.00 | 74.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.23 | 12.48 | 19.83 | 2.00 | 91.7 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: wildcard
- Predicted score: 60.29
- Actual score: 67.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +14.96 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 10.14 | 16.22 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.95 | 9.74 | 16.31 | 3.00 | 90.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.65 | 13.69 | 22.64 | 12.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.41 | 11.88 | 18.55 | 1.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.20 | 11.85 | 19.47 | 13.00 | 80.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.20 | 9.64 | 15.65 | 2.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 2.73 | 9.03 | 15.30 | 2.00 | 80.6 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 4.61 | 12.53 | 19.77 | 2.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.84 | 8.57 | 14.42 | 1.00 | 77.4 | 59.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.98 | 13.12 | 1.00 | 71.7 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.32 | 21.61 | 35.87 | 5.00 | 106.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.47 | 17.60 | 28.02 | 8.00 | 99.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 6.30 | 16.54 | 25.95 | 5.00 | 100.1 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 3.80 | 12.71 | 21.33 | 2.00 | 84.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 4.26 | 11.71 | 18.68 | 10.00 | 92.7 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.73
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.45 | 10.30 | 17.10 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 3.20 | 9.49 | 15.41 | 0.00 | 87.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.47 | 15.31 | 24.83 | 1.00 | 98.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.75 | 13.12 | 21.98 | 12.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.17 | 11.59 | 18.47 | 1.00 | 84.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.2 | 3.63 | 9.89 | 16.27 | 1.00 | 82.1 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.11 | 9.23 | 15.63 | 1.00 | 77.5 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 4.07 | 10.76 | 17.96 | 3.00 | 60.4 | 23.0 |
| Bench 3 | Bench Boost | Chiedozie Ogbene | FWD | 12 | 4.9 | 2.31 | 7.60 | 12.81 | 1.00 | 73.9 | 28.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.17 | 6.68 | 10.90 | 2.00 | 59.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.58 | 21.57 | 36.24 | 3.00 | 106.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.41 | 17.63 | 28.32 | 5.00 | 96.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.12 | 12.44 | 20.86 | 0.00 | 82.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.90 | 12.30 | 19.77 | 6.00 | 60.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.81 | 11.15 | 17.54 | 2.00 | 75.2 | 90.0 |