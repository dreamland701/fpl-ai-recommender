# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 263.88
- Total actual points: 247.00
- Average predicted points: 65.97
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
- Predicted score: 64.62
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.09 | 16.10 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.31 | 0.53 | 0.77 | 0.00 | 9.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.13 | 16.64 | 26.53 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.65 | 11.89 | 18.69 | 9.00 | 89.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.17 | 17.81 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.81 | 6.34 | 10.67 | 1.00 | 78.4 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.51 | 4.17 | 6.80 | 2.00 | 49.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.42 | 22.72 | 36.90 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.63 | 16.94 | 26.95 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.77 | 7.69 | 12.88 | 2.00 | 73.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.95 | 21.18 | 34.66 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.45 | 15.60 | 24.30 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.12 | 13.60 | 21.23 | 1.00 | 82.0 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.95 | 13.45 | 22.08 | 2.00 | 83.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.30 | 11.64 | 17.71 | 2.00 | 81.3 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.26
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.10, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.94 | 10.21 | 16.13 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.20 | 0.32 | 0.61 | 0.00 | 8.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.95 | 14.48 | 23.59 | 1.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.55 | 13.19 | 20.18 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 4.04 | 11.30 | 17.82 | 1.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.64 | 7.17 | 11.87 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.98 | 4.77 | 7.54 | 5.00 | 55.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.89 | 23.86 | 38.88 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.79 | 15.64 | 24.05 | 5.00 | 81.1 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.81 | 7.20 | 11.96 | 2.00 | 71.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.83 | 22.33 | 36.46 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.35 | 14.26 | 22.60 | 2.00 | 83.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.60 | 12.25 | 19.35 | 2.00 | 84.2 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.18 | 11.91 | 19.06 | 0.00 | 64.3 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.26 | 9.70 | 15.66 | 13.00 | 70.9 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 72.35
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.31) beats the best remaining Triple Captain opportunity (9.40).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.94, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.31) beats the best remaining Triple Captain opportunity (9.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.63 | 9.61 | 15.51 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.18 | 0.20 | 0.54 | 0.00 | 7.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.69 | 13.72 | 22.72 | 12.00 | 86.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.33 | 12.00 | 18.90 | 1.00 | 83.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.31 | 9.67 | 15.69 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.83 | 7.30 | 11.90 | 10.00 | 81.1 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 2.28 | 5.96 | 9.52 | 1.00 | 60.3 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.31 | 25.12 | 41.26 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.63 | 13.60 | 23.05 | 11.00 | 74.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 7.71 | 12.64 | 1.00 | 72.5 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.40 | 21.66 | 36.07 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.35 | 17.58 | 28.14 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.97 | 16.89 | 26.35 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.01 | 11.84 | 18.89 | 10.00 | 88.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.13 | 10.41 | 16.54 | 1.00 | 62.9 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.64
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.19 | 9.18 | 14.88 | 0.00 | 85.8 | 0.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 9 | 3.9 | 0.23 | 0.51 | 0.60 | 0.00 | 6.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.37 | 15.07 | 24.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.35 | 11.93 | 18.98 | 1.00 | 82.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.66 | 9.70 | 16.17 | 1.00 | 82.6 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.69 | 7.32 | 12.23 | 1.00 | 83.3 | 90.0 |
| Bench 4 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 0.68 | 3.24 | 5.23 | 0.00 | 30.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.20 | 25.02 | 40.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.76 | 24.59 | 1.00 | 81.9 | 89.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.19 | 6.79 | 10.79 | 2.00 | 60.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.76 | 21.76 | 36.50 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.46 | 17.90 | 28.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.89 | 12.65 | 20.16 | 6.00 | 61.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.13 | 9.96 | 15.94 | 2.00 | 62.1 | 90.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.17 | 8.33 | 14.12 | 8.00 | 50.4 | 90.0 |