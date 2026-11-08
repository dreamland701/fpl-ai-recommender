# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.71
- Total actual points: 231.00
- Average predicted points: 65.18
- Average actual points: 57.75
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
- Predicted score: 63.15
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.82 | 10.34 | 16.52 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.00 | 0.15 | 0.46 | 0.00 | 9.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.36 | 17.49 | 27.91 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.34 | 11.55 | 18.11 | 9.00 | 88.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.80 | 11.14 | 17.77 | 1.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.92 | 6.48 | 10.87 | 1.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.96 | 6.11 | 10.67 | 1.00 | 67.3 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.18 | 22.02 | 35.62 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.75 | 17.44 | 27.78 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.85 | 7.73 | 12.84 | 2.00 | 71.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.86 | 20.88 | 34.17 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.47 | 15.84 | 24.69 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.96 | 13.61 | 22.65 | 2.00 | 84.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.83 | 13.05 | 20.22 | 1.00 | 81.2 | 45.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.61 | 11.57 | 18.84 | 2.00 | 72.6 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.12
- Actual score: 48.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.21, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.80 | 10.33 | 16.38 | 3.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.31 | 0.46 | 0.86 | 0.00 | 8.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.09 | 15.07 | 24.73 | 1.00 | 89.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.46 | 12.83 | 19.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.82 | 11.07 | 17.61 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.75 | 7.55 | 12.41 | 1.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.85 | 5.22 | 9.31 | 0.00 | 58.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.57 | 22.58 | 36.81 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.86 | 16.09 | 24.85 | 5.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.95 | 7.66 | 12.52 | 2.00 | 69.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.73 | 21.86 | 35.83 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.31 | 14.30 | 23.02 | 2.00 | 84.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.72 | 12.80 | 20.42 | 2.00 | 84.9 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.05 | 11.93 | 19.21 | 0.00 | 64.0 | 0.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.13 | 11.10 | 18.19 | 7.00 | 74.9 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.19
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.70) beats the best remaining Bench Boost opportunity (7.96).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.70) beats the best remaining Bench Boost opportunity (7.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.69 | 9.91 | 15.87 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Denis Franchi | GK | 6 | 3.9 | 0.33 | 0.52 | 0.92 | 0.00 | 7.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.85 | 14.44 | 24.05 | 12.00 | 88.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.24 | 11.78 | 18.36 | 1.00 | 82.3 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.27 | 9.62 | 15.58 | 2.00 | 77.6 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.79 | 7.60 | 12.38 | 10.00 | 79.8 | 90.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.69 | 2.68 | 5.18 | 1.00 | 27.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.08 | 24.22 | 39.71 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 14.29 | 23.93 | 11.00 | 73.1 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.84 | 12.85 | 1.00 | 71.1 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.36 | 21.53 | 35.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.30 | 17.59 | 27.94 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.82 | 16.92 | 26.73 | 5.00 | 90.0 | 77.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 3.76 | 11.36 | 19.05 | 2.00 | 80.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.26 | 10.95 | 17.57 | 1.00 | 63.5 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.24
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.92) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.92) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.21 | 9.32 | 15.15 | 0.00 | 84.9 | 0.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.16 | 0.34 | 0.71 | 0.00 | 4.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.54 | 15.89 | 25.96 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.08 | 11.45 | 18.21 | 1.00 | 82.2 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.66 | 9.84 | 16.16 | 1.00 | 81.3 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.86 | 7.99 | 13.05 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.72 | 5.55 | 9.16 | 0.00 | 61.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.92 | 23.90 | 38.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.52 | 14.72 | 24.95 | 1.00 | 81.4 | 89.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.19 | 6.63 | 10.78 | 2.00 | 58.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.58 | 21.46 | 36.03 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.19 | 17.54 | 28.11 | 5.00 | 89.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.92 | 12.93 | 20.94 | 6.00 | 62.5 | 39.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 2.94 | 9.76 | 16.71 | 3.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.32 | 9.03 | 15.36 | 8.00 | 50.8 | 90.0 |