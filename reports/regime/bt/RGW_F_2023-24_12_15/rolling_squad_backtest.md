# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.53
- Total actual points: 242.00
- Average predicted points: 65.13
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
- Predicted score: 63.95
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.76 | 10.17 | 16.18 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.11 | 0.56 | 0.97 | 0.00 | 2.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.30 | 17.05 | 26.71 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.42 | 11.58 | 18.11 | 9.00 | 89.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.82 | 11.07 | 17.85 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.01 | 6.12 | 10.76 | 1.00 | 68.7 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.61 | 4.29 | 7.04 | 2.00 | 48.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.06 | 22.71 | 36.46 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.82 | 17.39 | 27.56 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.85 | 7.68 | 12.80 | 2.00 | 69.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 7.01 | 21.78 | 35.63 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.50 | 15.84 | 24.58 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.04 | 13.24 | 21.81 | 2.00 | 84.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.83 | 13.23 | 20.35 | 1.00 | 81.8 | 45.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.33 | 11.88 | 17.94 | 2.00 | 81.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.52
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.21, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.72 | 10.18 | 16.00 | 3.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.10 | 0.45 | 0.78 | 0.00 | 1.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.67 | 23.74 | 1.00 | 89.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.44 | 12.74 | 19.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.79 | 11.08 | 17.64 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.93 | 5.56 | 10.03 | 0.00 | 60.8 | 0.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.10 | 5.16 | 8.07 | 5.00 | 54.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.07 | 37.97 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.89 | 16.35 | 24.72 | 5.00 | 81.8 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.92 | 7.46 | 12.17 | 2.00 | 67.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.88 | 22.61 | 37.03 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.28 | 13.61 | 21.65 | 2.00 | 84.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.84 | 12.56 | 19.98 | 2.00 | 86.6 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.06 | 11.63 | 18.81 | 0.00 | 66.5 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.25 | 9.57 | 15.54 | 13.00 | 72.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.32
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (6.61).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (6.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.63 | 9.67 | 15.37 | 2.00 | 82.8 | 90.0 |
| Bench 1 | Bench Boost | Zack Steffen | GK | 13 | 3.9 | 0.19 | 0.53 | 0.80 | 0.00 | 0.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.65 | 13.91 | 22.75 | 12.00 | 87.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.17 | 11.56 | 18.08 | 1.00 | 84.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.23 | 9.70 | 15.71 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.18 | 5.94 | 9.62 | 1.00 | 60.5 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.72 | 2.99 | 5.77 | 1.00 | 29.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.04 | 24.47 | 40.30 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.73 | 14.33 | 23.69 | 11.00 | 73.6 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.81 | 7.59 | 12.43 | 1.00 | 70.3 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.53 | 22.22 | 36.97 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.25 | 17.25 | 27.46 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.82 | 16.00 | 25.18 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.05 | 11.75 | 18.66 | 10.00 | 89.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.29 | 10.52 | 16.74 | 1.00 | 66.3 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.75
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.98) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.98) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.16 | 9.16 | 14.72 | 0.00 | 81.7 | 0.0 |
| Bench 1 | Bench | Zack Steffen | GK | 13 | 3.9 | 0.00 | 0.30 | 0.68 | 0.00 | 1.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.30 | 15.09 | 24.43 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.05 | 11.42 | 18.12 | 1.00 | 84.1 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.71 | 9.98 | 16.40 | 1.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.71 | 5.52 | 9.03 | 0.00 | 63.0 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.70 | 3.18 | 5.42 | 0.00 | 30.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.98 | 24.55 | 40.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.65 | 24.35 | 1.00 | 82.5 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.08 | 6.33 | 10.27 | 2.00 | 57.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.70 | 22.06 | 36.96 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.17 | 17.17 | 27.51 | 5.00 | 89.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.91 | 12.21 | 19.69 | 6.00 | 64.2 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.10 | 9.74 | 15.46 | 2.00 | 64.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 2.23 | 8.58 | 14.47 | 8.00 | 51.7 | 90.0 |