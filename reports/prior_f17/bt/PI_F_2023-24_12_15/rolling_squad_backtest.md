# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 264.43
- Total actual points: 244.00
- Average predicted points: 66.11
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
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.21
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.82 | 10.35 | 16.58 | 2.00 | 89.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.38 | 0.79 | 1.19 | 0.00 | 8.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.21 | 16.90 | 26.84 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.33 | 11.54 | 18.12 | 9.00 | 88.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.27 | 18.01 | 1.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.93 | 6.52 | 10.94 | 1.00 | 77.0 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.63 | 4.47 | 7.24 | 2.00 | 47.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.28 | 22.46 | 36.51 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.76 | 17.35 | 27.52 | 6.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.89 | 13.13 | 2.00 | 71.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 7.05 | 21.48 | 35.15 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.52 | 15.94 | 24.81 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.88 | 13.33 | 20.76 | 1.00 | 81.7 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.91 | 13.22 | 21.91 | 2.00 | 83.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.36 | 11.91 | 17.99 | 2.00 | 79.8 | 90.0 |

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
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.60, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.33 | 16.43 | 3.00 | 87.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.26 | 0.58 | 0.96 | 0.00 | 6.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.35 | 23.40 | 1.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.45 | 12.91 | 19.80 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.12 | 17.70 | 1.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.77 | 7.61 | 12.52 | 1.00 | 80.2 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.15 | 5.43 | 8.48 | 5.00 | 53.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.28 | 38.19 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.86 | 15.96 | 24.50 | 5.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.96 | 7.81 | 12.84 | 2.00 | 70.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.92 | 22.44 | 36.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.25 | 13.89 | 22.21 | 2.00 | 83.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.61 | 12.33 | 19.60 | 2.00 | 83.6 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.12 | 12.10 | 19.44 | 0.00 | 64.1 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.25 | 9.58 | 15.46 | 13.00 | 70.0 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.95
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.16) beats the best remaining Bench Boost opportunity (9.56).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.16) beats the best remaining Bench Boost opportunity (9.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.68 | 9.91 | 15.91 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 9 | 3.9 | 0.22 | 0.52 | 0.86 | 0.00 | 6.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 13.67 | 22.62 | 12.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.24 | 11.88 | 18.59 | 1.00 | 82.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.28 | 9.65 | 15.64 | 2.00 | 77.7 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.80 | 7.62 | 12.42 | 10.00 | 80.0 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.24 | 6.25 | 10.05 | 1.00 | 59.4 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.16 | 24.66 | 40.64 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.23 | 23.72 | 11.00 | 73.0 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.96 | 13.15 | 1.00 | 72.2 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.57 | 22.15 | 36.72 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.32 | 17.57 | 27.98 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.76 | 16.52 | 25.95 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.99 | 11.77 | 18.75 | 10.00 | 87.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.17 | 10.53 | 16.83 | 1.00 | 62.2 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.84
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.02) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.02) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.20 | 9.31 | 15.17 | 0.00 | 85.5 | 0.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.23 | 0.45 | 0.77 | 0.00 | 6.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.37 | 15.18 | 24.67 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.06 | 11.50 | 18.37 | 1.00 | 82.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.67 | 9.89 | 16.26 | 1.00 | 81.5 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.88 | 8.05 | 13.15 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.72 | 3.26 | 5.57 | 0.00 | 29.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.02 | 24.48 | 40.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.56 | 14.78 | 24.94 | 1.00 | 81.4 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.20 | 6.78 | 11.11 | 2.00 | 60.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.79 | 22.08 | 37.00 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.24 | 17.58 | 28.27 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.87 | 12.51 | 20.08 | 6.00 | 61.3 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.13 | 10.08 | 15.87 | 2.00 | 61.1 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.20 | 8.53 | 14.46 | 8.00 | 49.6 | 90.0 |