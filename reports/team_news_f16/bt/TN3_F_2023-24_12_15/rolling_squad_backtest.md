# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.32
- Total actual points: 254.00
- Average predicted points: 65.33
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
- Predicted score: 64.59
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.45 | 16.64 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.16 | 0.51 | 0.86 | 0.00 | 2.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.26 | 16.97 | 26.88 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.40 | 11.64 | 18.20 | 9.00 | 89.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.39 | 18.15 | 1.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.99 | 6.62 | 11.04 | 1.00 | 78.6 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.72 | 4.59 | 7.34 | 2.00 | 49.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.32 | 22.50 | 36.52 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.79 | 17.38 | 27.54 | 6.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.99 | 8.09 | 13.38 | 2.00 | 74.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.97 | 21.22 | 34.72 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.51 | 15.90 | 24.74 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.95 | 13.46 | 20.92 | 1.00 | 83.2 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.91 | 13.20 | 21.86 | 2.00 | 84.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.38 | 11.94 | 18.03 | 2.00 | 80.8 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.15
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.49, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.87 | 10.44 | 16.50 | 3.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.05 | 0.43 | 0.82 | 0.00 | 1.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.96 | 14.42 | 23.45 | 1.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.52 | 13.00 | 19.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.24 | 17.85 | 1.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.84 | 7.72 | 12.64 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.20 | 5.48 | 8.49 | 5.00 | 55.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.54 | 23.41 | 38.68 | 7.00 | 49.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.88 | 15.96 | 24.46 | 5.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.07 | 7.97 | 12.96 | 2.00 | 71.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.83 | 22.18 | 36.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.26 | 13.88 | 22.15 | 2.00 | 84.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.65 | 12.37 | 19.62 | 2.00 | 84.8 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.94 | 12.20 | 19.88 | 0.00 | 33.4 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.27 | 9.62 | 15.51 | 13.00 | 71.1 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.15
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (9.48).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.21) beats the best remaining Triple Captain opportunity (9.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.75 | 10.02 | 15.99 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.00 | 0.03 | 0.30 | 8.00 | 1.7 | 67.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.72 | 13.73 | 22.67 | 12.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.31 | 11.98 | 18.65 | 1.00 | 83.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.35 | 9.79 | 15.82 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.87 | 7.74 | 12.54 | 10.00 | 81.7 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.27 | 6.27 | 10.03 | 1.00 | 60.1 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.21 | 24.70 | 40.63 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.63 | 14.39 | 24.28 | 11.00 | 38.3 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.05 | 13.18 | 1.00 | 72.7 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.47 | 21.87 | 36.24 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.32 | 17.56 | 27.92 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.76 | 16.47 | 25.84 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.01 | 11.81 | 18.80 | 10.00 | 88.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.21 | 10.54 | 16.78 | 1.00 | 63.9 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.43
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.13 | 9.21 | 15.11 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 1.09 | 2.59 | 4.46 | 7.00 | 31.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.25 | 15.03 | 24.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.01 | 11.43 | 18.35 | 1.00 | 80.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.59 | 9.83 | 16.31 | 1.00 | 80.1 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.79 | 7.94 | 13.12 | 1.00 | 80.2 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 0.63 | 3.13 | 5.46 | 0.00 | 28.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.91 | 24.29 | 39.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.46 | 14.61 | 24.78 | 1.00 | 80.3 | 89.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.14 | 6.68 | 11.02 | 2.00 | 58.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.55 | 21.60 | 36.40 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.08 | 17.34 | 28.05 | 5.00 | 87.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.74 | 12.29 | 19.88 | 6.00 | 60.0 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.00 | 9.89 | 15.72 | 2.00 | 59.0 | 90.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.16 | 8.46 | 14.42 | 8.00 | 50.2 | 90.0 |