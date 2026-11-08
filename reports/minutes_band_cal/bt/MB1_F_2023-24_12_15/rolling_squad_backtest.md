# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 243.49
- Total actual points: 227.00
- Average predicted points: 60.87
- Average actual points: 56.75
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
- Predicted score: 59.91
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.24 | 8.56 | 14.08 | 2.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.00 | 0.07 | 0.41 | 0.00 | 8.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.61 | 15.08 | 24.33 | 1.00 | 82.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.87 | 10.78 | 17.25 | 2.00 | 70.8 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.92 | 10.37 | 16.41 | 1.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.06 | 6.46 | 11.33 | 1.00 | 71.0 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.81 | 4.93 | 7.96 | 2.00 | 51.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.69 | 20.65 | 34.02 | 16.00 | 82.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.15 | 15.52 | 25.02 | 6.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.17 | 13.66 | 2.00 | 74.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.35 | 19.40 | 32.24 | 16.00 | 82.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 4.89 | 14.06 | 22.25 | 8.00 | 82.4 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.02 | 13.51 | 20.93 | 1.00 | 80.4 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.02 | 13.32 | 21.93 | 2.00 | 82.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.46 | 12.03 | 18.10 | 2.00 | 78.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.43
- Actual score: 49.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.53, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.25 | 8.72 | 14.01 | 3.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.26 | 0.39 | 0.82 | 0.00 | 7.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.36 | 12.70 | 20.98 | 1.00 | 79.8 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.06 | 8.98 | 14.42 | 2.00 | 80.1 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 2.69 | 8.72 | 13.92 | 0.00 | 58.0 | 45.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.33 | 5.91 | 9.20 | 5.00 | 58.2 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.08 | 5.90 | 10.41 | 0.00 | 63.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.16 | 21.65 | 35.77 | 7.00 | 82.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.96 | 16.07 | 24.56 | 5.00 | 78.9 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.06 | 8.06 | 13.23 | 2.00 | 72.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.26 | 20.54 | 33.91 | 5.00 | 82.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.34 | 14.00 | 22.25 | 2.00 | 82.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.73 | 12.48 | 19.70 | 2.00 | 82.4 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.15 | 12.24 | 19.72 | 0.00 | 67.7 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.31 | 9.80 | 15.90 | 13.00 | 73.6 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.77
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.38) beats the best remaining Bench Boost opportunity (7.21).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 7.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.38) beats the best remaining Bench Boost opportunity (7.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.14 | 8.39 | 13.63 | 2.00 | 78.6 | 90.0 |
| Bench 1 | Bench Boost | Denis Franchi | GK | 6 | 3.9 | 0.28 | 0.44 | 0.87 | 0.00 | 6.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.78 | 13.82 | 22.75 | 12.00 | 84.2 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 3.15 | 9.29 | 15.41 | 1.00 | 60.1 | 16.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 2.82 | 8.41 | 13.70 | 6.00 | 78.2 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.42 | 6.74 | 10.79 | 1.00 | 63.8 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.67 | 2.74 | 5.37 | 1.00 | 26.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.62 | 23.13 | 38.35 | 7.00 | 82.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 14.16 | 23.50 | 11.00 | 74.8 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.01 | 8.22 | 13.57 | 1.00 | 74.8 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 6.90 | 20.30 | 33.96 | 5.00 | 82.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.73 | 15.96 | 25.58 | 8.00 | 82.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.18 | 14.92 | 23.56 | 5.00 | 82.5 | 77.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.25 | 10.74 | 17.23 | 1.00 | 66.1 | 24.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.42 | 10.22 | 16.48 | 10.00 | 80.2 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 64.39
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 4.17, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Issa Kaboré replaced Konstantinos Tsimikas.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.33 | 9.52 | 15.30 | 0.00 | 83.4 | 0.0 |
| Bench 1 | Bench | Denis Franchi | GK | 6 | 3.9 | 0.11 | 0.24 | 0.63 | 0.00 | 4.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.81 | 13.67 | 22.55 | 1.00 | 82.6 | 90.0 |
| XI | Bench | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.65 | 10.05 | 16.18 | 0.00 | 72.3 | 0.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.15 | 8.99 | 14.55 | 1.00 | 80.7 | 90.0 |
| Bench 3 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 1.83 | 5.91 | 9.83 | 0.00 | 65.2 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.66 | 3.14 | 5.42 | 0.00 | 28.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.50 | 23.01 | 38.05 | 2.00 | 82.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.64 | 14.91 | 25.01 | 1.00 | 80.0 | 89.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.39 | 7.31 | 11.89 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.12 | 20.27 | 34.42 | 3.00 | 82.6 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.66 | 16.01 | 26.06 | 5.00 | 82.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.92 | 12.66 | 20.42 | 6.00 | 65.0 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.20 | 10.27 | 16.29 | 2.00 | 64.8 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.37 | 9.05 | 15.24 | 8.00 | 54.5 | 90.0 |