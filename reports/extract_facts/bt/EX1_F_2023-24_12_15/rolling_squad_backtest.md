# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 272.46
- Total actual points: 244.00
- Average predicted points: 68.11
- Average actual points: 61.00
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
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.17
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.37 | 16.56 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.25 | 0.70 | 1.21 | 0.00 | 6.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.22 | 16.86 | 26.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.34 | 11.55 | 18.10 | 9.00 | 88.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.32 | 18.10 | 1.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.94 | 6.55 | 10.98 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.61 | 4.40 | 7.13 | 2.00 | 46.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.22 | 20.96 | 34.53 | 16.00 | 79.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.76 | 17.32 | 27.45 | 6.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.95 | 13.22 | 2.00 | 71.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.95 | 21.19 | 34.65 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.46 | 15.83 | 24.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 5.83 | 14.90 | 21.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.90 | 13.41 | 20.86 | 1.00 | 82.1 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.88 | 13.11 | 21.66 | 2.00 | 83.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.47
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 7.20, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.81 | 10.36 | 16.42 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.19 | 0.48 | 0.88 | 0.00 | 6.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.94 | 14.34 | 23.39 | 1.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.46 | 12.90 | 19.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.84 | 11.17 | 17.80 | 1.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.78 | 7.65 | 12.58 | 1.00 | 80.3 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.13 | 5.37 | 8.37 | 5.00 | 53.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.31 | 22.94 | 38.75 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.87 | 15.94 | 24.51 | 5.00 | 80.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.98 | 7.83 | 12.81 | 2.00 | 69.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.81 | 22.13 | 36.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.97 | 14.95 | 22.99 | 2.00 | 90.0 | 74.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.26 | 13.84 | 22.09 | 2.00 | 84.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.66 | 11.68 | 20.05 | 0.00 | 55.4 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.23 | 9.56 | 15.46 | 13.00 | 70.4 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 80.15
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.27) beats the best remaining Bench Boost opportunity (9.35).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 11.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.27) beats the best remaining Bench Boost opportunity (9.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.70 | 9.94 | 15.92 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.30 | 0.57 | 1.05 | 0.00 | 6.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.95 | 15.94 | 26.36 | 12.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.28 | 11.92 | 18.62 | 1.00 | 82.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.31 | 9.74 | 15.80 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.81 | 7.66 | 12.48 | 10.00 | 80.2 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.23 | 6.20 | 9.96 | 1.00 | 59.1 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 9.43 | 26.92 | 44.35 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 3.00 | 14.08 | 26.39 | 11.00 | 45.6 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.98 | 13.11 | 1.00 | 71.5 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 8.68 | 24.06 | 39.90 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 7.51 | 19.71 | 31.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.97 | 18.64 | 29.43 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 5.19 | 13.96 | 22.39 | 10.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.42 | 12.75 | 20.48 | 1.00 | 80.6 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.66
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.01) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.01) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.35 | 15.19 | 0.00 | 85.2 | 0.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.27 | 0.53 | 0.92 | 0.00 | 5.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.36 | 15.16 | 24.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.11 | 11.58 | 18.45 | 1.00 | 82.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.70 | 9.98 | 16.41 | 1.00 | 81.9 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.89 | 8.07 | 13.20 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.72 | 3.26 | 5.55 | 0.00 | 29.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.01 | 24.47 | 40.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.58 | 14.83 | 24.99 | 1.00 | 82.9 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.23 | 6.80 | 11.09 | 2.00 | 59.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.64 | 21.73 | 36.41 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.18 | 17.46 | 28.07 | 5.00 | 89.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.83 | 12.42 | 19.98 | 6.00 | 61.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.10 | 10.04 | 15.83 | 2.00 | 61.4 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.21 | 8.54 | 14.47 | 8.00 | 50.3 | 90.0 |