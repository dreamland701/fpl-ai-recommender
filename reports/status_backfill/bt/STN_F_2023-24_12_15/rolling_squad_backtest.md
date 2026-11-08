# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 268.16
- Total actual points: 254.00
- Average predicted points: 67.04
- Average actual points: 63.50
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
- Predicted score: 65.63
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.35 | 16.54 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.29 | 0.76 | 1.22 | 0.00 | 7.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.33 | 16.87 | 26.79 | 1.00 | 95.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.48 | 11.56 | 18.12 | 9.00 | 91.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.31 | 18.08 | 1.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.96 | 6.52 | 10.94 | 1.00 | 78.9 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.61 | 4.42 | 7.15 | 2.00 | 47.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.18 | 22.45 | 36.48 | 16.00 | 97.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.91 | 17.32 | 27.48 | 6.00 | 88.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.94 | 13.23 | 2.00 | 70.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 7.13 | 21.20 | 34.70 | 16.00 | 106.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.85 | 15.86 | 24.71 | 8.00 | 106.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.01 | 13.37 | 20.83 | 1.00 | 85.4 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.26 | 13.17 | 21.83 | 2.00 | 89.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.62 | 11.89 | 18.00 | 2.00 | 84.0 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.55
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.59, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.80 | 10.34 | 16.41 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.17 | 0.67 | 1.16 | 0.00 | 7.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.87 | 14.33 | 23.38 | 1.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.78 | 12.94 | 19.81 | 6.00 | 97.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.16 | 17.79 | 1.00 | 91.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.78 | 7.62 | 12.54 | 1.00 | 81.4 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.20 | 5.39 | 8.40 | 5.00 | 55.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 23.28 | 38.16 | 7.00 | 108.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.00 | 15.92 | 24.44 | 5.00 | 82.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.81 | 12.80 | 2.00 | 68.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.80 | 22.16 | 36.30 | 5.00 | 108.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.64 | 13.84 | 22.14 | 2.00 | 89.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.16 | 12.32 | 19.58 | 2.00 | 90.2 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.20 | 11.99 | 19.29 | 0.00 | 65.8 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.29 | 9.56 | 15.46 | 13.00 | 70.7 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 73.16
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (9.42).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.60, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (9.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.66 | 9.93 | 15.90 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.26 | 0.64 | 8.00 | 6.9 | 67.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.63 | 13.65 | 22.60 | 12.00 | 87.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.43 | 11.92 | 18.62 | 1.00 | 85.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.23 | 9.71 | 15.75 | 2.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.80 | 7.63 | 12.44 | 10.00 | 81.0 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.32 | 6.21 | 9.98 | 1.00 | 61.1 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.21 | 24.67 | 40.62 | 7.00 | 104.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.70 | 14.20 | 23.67 | 11.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.97 | 13.10 | 1.00 | 71.7 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.42 | 21.84 | 36.23 | 5.00 | 108.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.43 | 17.49 | 27.86 | 8.00 | 97.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.27 | 16.45 | 25.84 | 5.00 | 99.3 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.28 | 11.75 | 18.75 | 10.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.50 | 10.49 | 16.76 | 1.00 | 65.5 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.82
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.14 | 9.33 | 15.17 | 0.00 | 85.9 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.09 | 2.60 | 4.36 | 7.00 | 29.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.42 | 15.17 | 24.64 | 1.00 | 96.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.17 | 11.56 | 18.44 | 1.00 | 84.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.66 | 9.95 | 16.37 | 1.00 | 82.7 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.86 | 8.05 | 13.17 | 1.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 0.82 | 3.23 | 5.50 | 0.00 | 32.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.10 | 24.50 | 40.14 | 2.00 | 107.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.65 | 14.73 | 24.88 | 1.00 | 81.4 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.22 | 6.79 | 11.07 | 2.00 | 60.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.65 | 21.76 | 36.51 | 3.00 | 108.4 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.36 | 17.50 | 28.14 | 5.00 | 95.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.95 | 12.42 | 19.96 | 6.00 | 61.8 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.36 | 10.03 | 15.83 | 2.00 | 65.2 | 90.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.28 | 8.52 | 14.42 | 8.00 | 49.1 | 90.0 |