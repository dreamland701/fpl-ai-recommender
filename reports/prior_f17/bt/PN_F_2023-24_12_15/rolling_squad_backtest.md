# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.53
- Total actual points: 247.00
- Average predicted points: 65.38
- Average actual points: 61.75
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
- Predicted score: 64.20
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.87 | 10.51 | 16.83 | 2.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.08 | 0.55 | 1.00 | 0.00 | 6.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.19 | 16.88 | 26.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.37 | 11.64 | 18.27 | 9.00 | 89.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.87 | 11.43 | 18.27 | 1.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.88 | 6.40 | 10.75 | 1.00 | 76.1 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.58 | 4.29 | 6.94 | 2.00 | 46.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.26 | 22.47 | 36.57 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.76 | 17.42 | 27.66 | 6.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.94 | 8.11 | 13.50 | 2.00 | 72.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.92 | 21.13 | 34.60 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.51 | 15.96 | 24.87 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.90 | 13.42 | 20.92 | 1.00 | 82.1 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.91 | 13.24 | 21.93 | 2.00 | 84.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.36 | 11.94 | 18.08 | 2.00 | 80.6 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.44
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.46, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.84 | 10.51 | 16.72 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.05 | 0.46 | 0.85 | 0.00 | 4.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.37 | 23.44 | 1.00 | 87.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.51 | 13.03 | 19.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.87 | 11.29 | 18.00 | 1.00 | 88.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.72 | 7.46 | 12.29 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.10 | 5.26 | 8.18 | 5.00 | 52.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.70 | 23.31 | 38.25 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.87 | 16.01 | 24.60 | 5.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.02 | 8.00 | 13.10 | 2.00 | 70.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.80 | 22.11 | 36.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.25 | 13.91 | 22.23 | 2.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.64 | 12.38 | 19.64 | 2.00 | 84.4 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.09 | 12.03 | 19.34 | 0.00 | 64.8 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.25 | 9.62 | 15.54 | 13.00 | 70.9 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.99
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (9.43).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.45, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (9.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.73 | 10.09 | 16.20 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.15 | 0.51 | 0.80 | 0.00 | 3.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.67 | 13.69 | 22.67 | 12.00 | 86.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.29 | 12.00 | 18.74 | 1.00 | 83.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.33 | 9.83 | 15.97 | 2.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.75 | 7.47 | 12.18 | 10.00 | 79.0 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.20 | 6.08 | 9.77 | 1.00 | 58.4 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.18 | 24.76 | 40.83 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.26 | 23.77 | 11.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.15 | 13.40 | 1.00 | 72.6 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.43 | 21.76 | 36.09 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.29 | 17.53 | 27.94 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.76 | 16.53 | 25.94 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.00 | 11.80 | 18.82 | 10.00 | 88.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.19 | 10.54 | 16.79 | 1.00 | 63.3 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.90
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.25 | 9.48 | 15.45 | 0.00 | 85.8 | 0.0 |
| Bench 1 | Bench Boost | Zack Steffen | GK | 13 | 3.9 | 0.00 | 0.30 | 0.68 | 0.00 | 4.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.37 | 15.23 | 24.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.12 | 11.62 | 18.54 | 1.00 | 82.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.71 | 10.06 | 16.56 | 1.00 | 82.2 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.82 | 7.84 | 12.81 | 1.00 | 80.4 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 0.66 | 3.08 | 5.25 | 0.00 | 28.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 24.57 | 40.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.55 | 14.77 | 24.92 | 1.00 | 82.0 | 89.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.27 | 6.97 | 11.37 | 2.00 | 60.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.64 | 21.66 | 36.35 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.22 | 17.56 | 28.27 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.86 | 12.49 | 20.03 | 6.00 | 62.2 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.13 | 10.10 | 15.91 | 2.00 | 61.9 | 90.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.22 | 8.58 | 14.49 | 8.00 | 50.4 | 90.0 |