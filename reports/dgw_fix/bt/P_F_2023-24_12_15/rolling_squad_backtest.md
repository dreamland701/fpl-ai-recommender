# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 253.33
- Total actual points: 215.00
- Average predicted points: 63.33
- Average actual points: 53.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.62
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.92 | 10.69 | 17.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.32 | 9.02 | 14.95 | 8.00 | 88.4 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.24 | 16.51 | 26.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.38 | 17.82 | 9.00 | 88.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.10 | 17.72 | 1.00 | 88.2 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.79 | 10.50 | 16.83 | 2.00 | 67.4 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 3.39 | 9.43 | 15.13 | 1.00 | 88.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.76 | 17.00 | 27.13 | 6.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.68 | 12.78 | 2.00 | 70.4 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.77 | 7.32 | 12.09 | 1.00 | 46.2 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.86 | 20.96 | 34.83 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.65 | 16.76 | 27.92 | 2.00 | 89.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 6.02 | 16.28 | 26.49 | 5.00 | 86.4 | 80.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.46 | 15.09 | 23.87 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.90 | 12.68 | 20.09 | 1.00 | 82.0 | 45.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.42
- Actual score: 40.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 3.53, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.91 | 10.65 | 17.15 | 3.00 | 89.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.17 | 9.12 | 15.15 | 9.00 | 88.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.95 | 14.41 | 23.61 | 1.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.53 | 12.48 | 19.38 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 10.80 | 17.42 | 1.00 | 87.9 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 3.03 | 9.08 | 14.67 | 0.00 | 65.2 | 45.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.68 | 7.90 | 12.69 | 1.00 | 70.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.54 | 23.18 | 5.00 | 78.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.98 | 7.81 | 12.65 | 2.00 | 69.5 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.17 | 6.16 | 10.25 | 13.00 | 44.2 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.70 | 22.07 | 36.55 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.53 | 26.63 | 8.00 | 88.1 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.93 | 14.95 | 24.73 | 2.00 | 84.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.49 | 12.10 | 19.29 | 0.00 | 73.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.69 | 11.27 | 17.89 | 2.00 | 85.4 | 74.0 |

## GW14

- Train rows: 113281
- Bank: 1.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.56
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 7.94, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (9.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.78 | 10.33 | 16.65 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.97 | 9.55 | 16.16 | 3.00 | 88.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 13.84 | 23.01 | 12.00 | 86.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.25 | 11.57 | 18.15 | 1.00 | 82.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.26 | 9.37 | 15.42 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 5.0 | 2.90 | 8.12 | 13.51 | 1.00 | 53.9 | 16.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | 8 | 4.6 | 2.41 | 7.19 | 11.99 | 2.00 | 70.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.62 | 13.39 | 22.72 | 11.00 | 69.7 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.84 | 12.79 | 1.00 | 71.3 | 45.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.75 | 7.77 | 13.18 | 4.00 | 62.2 | 33.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.33 | 21.86 | 36.27 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.33 | 17.21 | 27.32 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 5.77 | 15.99 | 20.11 | 5.00 | 90.0 | 77.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.86 | 13.03 | 22.27 | 10.00 | 75.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.11 | 9.25 | 14.96 | 1.00 | 61.3 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.72
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Julián Álvarez (projected gain 3.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.52 | 10.29 | 17.08 | 2.00 | 89.7 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 3.28 | 9.76 | 15.88 | 0.00 | 86.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.42 | 15.11 | 24.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.10 | 11.55 | 18.46 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.65 | 9.80 | 16.00 | 1.00 | 80.9 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 8 | 4.6 | 2.85 | 7.63 | 12.49 | 1.00 | 74.4 | 28.0 |
| Bench 4 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 1.48 | 5.79 | 10.31 | 0.00 | 35.7 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.38 | 13.30 | 22.98 | 1.00 | 78.1 | 89.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.12 | 11.96 | 15.80 | 2.00 | 69.4 | 67.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.16 | 6.47 | 10.52 | 2.00 | 58.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.57 | 21.55 | 36.16 | 3.00 | 90.0 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.26 | 17.28 | 27.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.42 | 15.09 | 25.32 | 2.00 | 89.3 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.79 | 11.48 | 14.78 | 6.00 | 60.4 | 39.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.13 | 8.05 | 13.84 | 8.00 | 48.4 | 90.0 |