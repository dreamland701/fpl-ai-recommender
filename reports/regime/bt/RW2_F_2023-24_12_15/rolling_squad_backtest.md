# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 261.00
- Total actual points: 242.00
- Average predicted points: 65.25
- Average actual points: 60.50
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
- Predicted score: 64.10
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.28 | 16.40 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.00 | 0.16 | 0.46 | 0.00 | 9.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.31 | 17.07 | 26.74 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.44 | 11.67 | 18.28 | 9.00 | 88.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.10 | 17.90 | 1.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.99 | 6.03 | 10.57 | 1.00 | 67.3 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.59 | 4.21 | 6.87 | 2.00 | 46.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.09 | 22.81 | 36.63 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.88 | 17.64 | 28.03 | 6.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.97 | 13.33 | 2.00 | 71.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.92 | 21.44 | 35.01 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.50 | 15.81 | 24.53 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.86 | 13.34 | 20.55 | 1.00 | 81.7 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.04 | 13.23 | 21.81 | 2.00 | 84.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.36 | 11.99 | 18.15 | 2.00 | 81.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.54
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.90, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 10.28 | 16.21 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.30 | 0.48 | 0.87 | 0.00 | 8.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.66 | 23.72 | 1.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.45 | 12.78 | 19.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.82 | 11.18 | 17.81 | 1.00 | 89.6 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.90 | 5.41 | 9.76 | 0.00 | 59.7 | 0.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.09 | 5.08 | 7.90 | 5.00 | 53.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.05 | 37.94 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.93 | 16.51 | 25.03 | 5.00 | 82.2 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.99 | 7.77 | 12.73 | 2.00 | 69.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.79 | 22.26 | 36.38 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.27 | 13.57 | 21.57 | 2.00 | 84.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.84 | 12.54 | 19.96 | 2.00 | 86.7 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.06 | 11.60 | 18.77 | 0.00 | 66.0 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.28 | 9.65 | 15.69 | 13.00 | 72.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.56
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.05) beats the best remaining Bench Boost opportunity (6.84).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.05) beats the best remaining Bench Boost opportunity (6.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.65 | 9.78 | 15.60 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Denis Franchi | GK | 6 | 3.9 | 0.31 | 0.51 | 0.89 | 0.00 | 7.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.66 | 13.92 | 22.77 | 12.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.19 | 11.63 | 18.19 | 1.00 | 83.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.26 | 9.76 | 15.82 | 2.00 | 79.1 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.17 | 5.88 | 9.51 | 1.00 | 59.2 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.69 | 2.85 | 5.52 | 1.00 | 28.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 24.44 | 40.25 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.52 | 24.05 | 11.00 | 74.0 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.91 | 13.02 | 1.00 | 72.0 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.46 | 21.93 | 36.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.27 | 17.36 | 27.67 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.80 | 15.91 | 25.03 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.07 | 11.83 | 18.81 | 10.00 | 89.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.30 | 10.55 | 16.81 | 1.00 | 66.5 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.80
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.18 | 9.26 | 14.93 | 0.00 | 84.4 | 0.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.15 | 0.30 | 0.65 | 0.00 | 4.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.30 | 15.08 | 24.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.07 | 11.52 | 18.28 | 1.00 | 83.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.73 | 10.05 | 16.51 | 1.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.69 | 5.42 | 8.83 | 0.00 | 61.5 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.68 | 3.07 | 5.21 | 0.00 | 29.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.96 | 24.47 | 40.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.55 | 14.87 | 24.77 | 1.00 | 83.2 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.16 | 6.65 | 10.86 | 2.00 | 59.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.65 | 21.83 | 36.55 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.19 | 17.25 | 27.66 | 5.00 | 89.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.90 | 12.16 | 19.59 | 6.00 | 64.0 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.10 | 9.75 | 15.47 | 2.00 | 63.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 2.26 | 8.68 | 14.67 | 8.00 | 52.2 | 90.0 |