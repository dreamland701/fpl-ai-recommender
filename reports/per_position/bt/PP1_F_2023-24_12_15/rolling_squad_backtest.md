# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.17
- Total actual points: 250.00
- Average predicted points: 65.04
- Average actual points: 62.50
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
- Predicted score: 64.97
- Actual score: 79.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 4.42 | 10.92 | 19.00 | 2.00 | 74.3 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.07 | 0.36 | 0.00 | 3.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.02 | 13.40 | 21.56 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.66 | 11.80 | 18.49 | 9.00 | 87.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.76 | 11.38 | 18.27 | 1.00 | 89.1 | 90.0 |
| Bench 2 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 2.93 | 7.38 | 11.55 | 0.00 | 72.1 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.36 | 6.91 | 10.91 | 9.00 | 77.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.17 | 20.18 | 35.26 | 16.00 | 83.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 6.02 | 17.91 | 29.74 | 6.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.93 | 13.47 | 20.77 | 1.00 | 53.2 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.35 | 20.87 | 34.01 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.52 | 15.94 | 24.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.97 | 15.50 | 24.75 | 2.00 | 84.1 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.81 | 13.17 | 20.58 | 1.00 | 78.5 | 45.0 |
| Bench 4 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.16 | 6.63 | 11.39 | 2.00 | 77.5 | 85.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.23
- Actual score: 49.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.72, hit 0)
- Autosub: João Pedro Junqueira de Jesus replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 4.33 | 11.40 | 18.76 | 1.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.14 | 0.16 | 0.32 | 0.00 | 1.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.96 | 14.37 | 21.18 | 6.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.68 | 12.65 | 20.53 | 1.00 | 88.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.93 | 11.74 | 18.54 | 1.00 | 87.6 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.76 | 8.04 | 12.96 | 1.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Jamaal Lascelles | DEF | 15 | 4.1 | 1.80 | 5.94 | 9.48 | 7.00 | 60.1 | 85.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 5.96 | 20.93 | 36.91 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.73 | 14.06 | 24.00 | 5.00 | 82.8 | 90.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.25 | 7.04 | 11.94 | 13.00 | 45.2 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.86 | 21.00 | 34.53 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.79 | 15.29 | 23.79 | 2.00 | 79.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.88 | 12.70 | 19.28 | 2.00 | 87.2 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.50 | 12.59 | 20.19 | 0.00 | 66.1 | 0.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.50 | 7.04 | 11.97 | 0.00 | 75.4 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.23
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.95) beats the best remaining Bench Boost opportunity (7.35).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 10.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.95) beats the best remaining Bench Boost opportunity (7.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.17 | 9.16 | 14.93 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.04 | 0.03 | 0.26 | 0.00 | 1.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.39 | 12.86 | 19.08 | 1.00 | 83.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.35 | 11.25 | 19.07 | 12.00 | 88.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.08 | 9.86 | 15.81 | 2.00 | 76.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.82 | 7.99 | 12.16 | 6.00 | 75.5 | 90.0 |
| Bench 3 | Bench Boost | Jamaal Lascelles | DEF | 15 | 4.1 | 2.30 | 6.23 | 9.80 | 6.00 | 72.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.82 | 24.74 | 40.65 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.69 | 15.33 | 25.44 | 11.00 | 74.1 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.73 | 7.21 | 13.30 | 4.00 | 58.5 | 33.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.49 | 21.10 | 34.88 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.13 | 17.29 | 27.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.98 | 16.76 | 26.48 | 5.00 | 82.9 | 77.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.53 | 10.63 | 16.88 | 1.00 | 67.6 | 24.0 |
| Bench 4 | Bench Boost | Marvelous Nakamba | MID | 12 | 4.4 | 0.88 | 3.23 | 6.12 | 0.00 | 33.9 | 0.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.74
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.79 | 9.91 | 16.74 | 7.00 | 80.2 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.28 | 13.70 | 21.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.06 | 11.47 | 17.52 | 1.00 | 83.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.60 | 9.42 | 15.54 | 1.00 | 81.3 | 90.0 |
| XI | XI | Jamaal Lascelles | DEF | 15 | 4.1 | 3.05 | 8.79 | 12.96 | 1.00 | 79.4 | 89.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.3 | 2.70 | 7.95 | 11.99 | 6.00 | 84.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 7.09 | 24.58 | 40.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.87 | 15.47 | 26.03 | 1.00 | 82.3 | 89.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.49 | 8.03 | 13.59 | 2.00 | 52.3 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 8.22 | 22.23 | 36.38 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.40 | 17.98 | 28.44 | 5.00 | 88.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.26 | 12.49 | 20.45 | 6.00 | 62.0 | 39.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.36 | 8.26 | 13.90 | 8.00 | 51.8 | 90.0 |
| Bench 4 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 0.43 | 2.02 | 4.28 | 0.00 | 24.2 | 0.0 |