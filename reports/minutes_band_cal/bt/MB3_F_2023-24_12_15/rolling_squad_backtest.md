# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.74
- Total actual points: 236.00
- Average predicted points: 65.43
- Average actual points: 59.00
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
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.05
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.35 | 16.54 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.52 | 1.03 | 0.00 | 7.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.20 | 16.87 | 26.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.35 | 11.56 | 18.12 | 9.00 | 88.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.31 | 18.08 | 1.00 | 88.5 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.06 | 6.46 | 11.33 | 1.00 | 71.0 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.81 | 4.93 | 7.96 | 2.00 | 51.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.28 | 22.45 | 36.48 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.74 | 17.32 | 27.48 | 6.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.17 | 13.66 | 2.00 | 74.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.94 | 21.20 | 34.70 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.48 | 15.86 | 24.71 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.89 | 13.37 | 20.83 | 1.00 | 81.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.89 | 13.17 | 21.83 | 2.00 | 83.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.34 | 11.89 | 18.00 | 2.00 | 80.0 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.43
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.38, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.81 | 10.34 | 16.41 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.25 | 0.55 | 1.02 | 0.00 | 6.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.33 | 23.38 | 1.00 | 87.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.48 | 12.94 | 19.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.16 | 17.79 | 1.00 | 88.1 | 90.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.33 | 5.91 | 9.20 | 5.00 | 58.2 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.08 | 5.90 | 10.41 | 0.00 | 63.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.28 | 38.16 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.84 | 15.92 | 24.44 | 5.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.06 | 8.06 | 13.23 | 2.00 | 72.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.81 | 22.16 | 36.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 13.84 | 22.14 | 2.00 | 83.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.62 | 12.32 | 19.58 | 2.00 | 83.9 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.15 | 12.24 | 19.72 | 0.00 | 67.7 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.31 | 9.80 | 15.90 | 13.00 | 73.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.83
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (6.85).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.38, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (6.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 9.93 | 15.90 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.32 | 0.69 | 0.00 | 5.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.67 | 13.65 | 22.60 | 12.00 | 85.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.26 | 11.92 | 18.62 | 1.00 | 82.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.29 | 9.67 | 15.57 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.42 | 6.74 | 10.79 | 1.00 | 63.8 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.67 | 2.74 | 5.37 | 1.00 | 26.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.18 | 24.67 | 40.62 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 14.16 | 23.50 | 11.00 | 74.8 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.01 | 8.22 | 13.57 | 1.00 | 74.8 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.45 | 21.84 | 36.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.29 | 17.49 | 27.86 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.73 | 16.45 | 25.84 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.97 | 11.75 | 18.75 | 10.00 | 87.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.25 | 10.74 | 17.23 | 1.00 | 66.1 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.42
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.04) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.04) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.33 | 15.17 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.24 | 0.33 | 0.66 | 0.00 | 3.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.36 | 15.17 | 24.64 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.10 | 11.56 | 18.44 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.68 | 9.95 | 16.37 | 1.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.83 | 5.91 | 9.83 | 0.00 | 65.2 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.66 | 3.14 | 5.42 | 0.00 | 28.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 24.50 | 40.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.53 | 14.73 | 24.88 | 1.00 | 81.5 | 89.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.39 | 7.31 | 11.89 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.67 | 21.76 | 36.51 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.21 | 17.50 | 28.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.92 | 12.66 | 20.42 | 6.00 | 65.0 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.20 | 10.27 | 16.29 | 2.00 | 64.8 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.37 | 9.05 | 15.24 | 8.00 | 54.5 | 90.0 |