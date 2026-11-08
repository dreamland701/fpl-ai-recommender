# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 273.22
- Total actual points: 251.00
- Average predicted points: 68.30
- Average actual points: 62.75
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
- Predicted score: 64.69
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.45 | 16.64 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.9 | 0.30 | 0.50 | 0.96 | 0.00 | 2.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.26 | 16.95 | 26.84 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.38 | 11.63 | 18.16 | 9.00 | 89.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.39 | 18.16 | 1.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.00 | 6.64 | 11.07 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.71 | 4.57 | 7.30 | 2.00 | 49.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.40 | 21.23 | 34.80 | 16.00 | 83.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.79 | 17.37 | 27.49 | 6.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.99 | 8.09 | 13.36 | 2.00 | 74.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.96 | 21.20 | 34.65 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.49 | 15.86 | 24.66 | 8.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 5.82 | 14.86 | 21.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.95 | 13.49 | 20.93 | 1.00 | 83.3 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.90 | 13.13 | 21.68 | 2.00 | 84.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.46
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 7.03, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.86 | 10.44 | 16.50 | 3.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.9 | 0.00 | 0.12 | 0.44 | 0.00 | 1.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.41 | 23.45 | 1.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.50 | 12.96 | 19.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.89 | 11.23 | 17.84 | 1.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.84 | 7.74 | 12.66 | 1.00 | 81.9 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.19 | 5.46 | 8.45 | 5.00 | 54.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.21 | 23.10 | 39.17 | 7.00 | 88.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.89 | 15.97 | 24.50 | 5.00 | 81.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.07 | 7.98 | 12.96 | 2.00 | 71.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.82 | 22.14 | 36.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.95 | 14.90 | 22.93 | 2.00 | 90.0 | 74.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.28 | 13.86 | 22.10 | 2.00 | 85.1 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.60 | 11.92 | 20.54 | 0.00 | 53.4 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.27 | 9.62 | 15.50 | 13.00 | 71.2 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 81.76
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.94) beats the best remaining Bench Boost opportunity (11.37).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 5.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.94) beats the best remaining Bench Boost opportunity (11.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.75 | 10.02 | 15.99 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.9 | 1.90 | 3.62 | 5.66 | 1.00 | 28.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.94 | 15.92 | 26.32 | 12.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.32 | 11.97 | 18.64 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.36 | 9.82 | 15.86 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.87 | 7.75 | 12.56 | 10.00 | 81.8 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.27 | 6.26 | 10.01 | 1.00 | 60.0 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 9.41 | 26.85 | 44.25 | 7.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.4 | 2.90 | 14.25 | 26.86 | 11.00 | 42.9 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.06 | 13.17 | 1.00 | 72.8 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 8.64 | 24.00 | 39.81 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 7.49 | 19.68 | 31.48 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.94 | 18.57 | 29.35 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 5.17 | 13.93 | 22.34 | 10.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.42 | 12.71 | 20.41 | 1.00 | 80.4 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.30
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.89) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhin Kelleher replaced Alphonse Areola.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.14 | 9.24 | 15.16 | 0.00 | 83.8 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.9 | 1.24 | 3.42 | 5.25 | 6.00 | 34.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.25 | 15.03 | 24.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.01 | 11.45 | 18.38 | 1.00 | 81.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.61 | 9.87 | 16.36 | 1.00 | 80.4 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.81 | 7.97 | 13.17 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.64 | 3.17 | 5.52 | 0.00 | 28.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.89 | 24.27 | 39.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.50 | 14.70 | 24.90 | 1.00 | 81.4 | 89.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.15 | 6.71 | 11.06 | 2.00 | 58.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.52 | 21.57 | 36.32 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.06 | 17.31 | 28.00 | 5.00 | 87.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.75 | 12.30 | 19.92 | 6.00 | 60.3 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.00 | 9.89 | 15.73 | 2.00 | 59.1 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.17 | 8.48 | 14.48 | 8.00 | 50.5 | 90.0 |