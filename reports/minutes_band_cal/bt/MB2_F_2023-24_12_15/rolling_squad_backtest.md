# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 244.88
- Total actual points: 227.00
- Average predicted points: 61.22
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
- Predicted score: 59.76
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.33 | 8.83 | 14.40 | 2.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.65 | 2.61 | 4.26 | 0.00 | 29.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.70 | 15.35 | 24.65 | 1.00 | 82.7 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.86 | 10.77 | 17.26 | 2.00 | 70.8 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.73 | 10.12 | 16.12 | 1.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.06 | 6.46 | 11.34 | 1.00 | 71.1 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.86 | 5.12 | 8.21 | 2.00 | 53.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.78 | 20.92 | 34.34 | 16.00 | 82.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.24 | 15.79 | 25.34 | 6.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.97 | 8.17 | 13.68 | 2.00 | 74.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.44 | 19.67 | 32.56 | 16.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 4.98 | 14.33 | 22.57 | 8.00 | 82.7 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.82 | 13.27 | 20.65 | 1.00 | 79.2 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.82 | 13.07 | 21.65 | 2.00 | 81.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.27 | 11.79 | 17.82 | 2.00 | 77.5 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.94
- Actual score: 49.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.30, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.32 | 8.91 | 14.33 | 3.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.29 | 1.45 | 2.37 | 0.00 | 17.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.43 | 12.89 | 21.30 | 1.00 | 80.0 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.09 | 9.07 | 14.66 | 2.00 | 79.2 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.1 | 2.50 | 8.19 | 13.12 | 0.00 | 53.3 | 45.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.39 | 6.08 | 9.43 | 5.00 | 59.9 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.88 | 5.38 | 9.61 | 0.00 | 58.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.28 | 38.16 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.77 | 15.83 | 24.26 | 5.00 | 77.8 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.05 | 8.05 | 13.25 | 2.00 | 72.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.33 | 20.72 | 34.22 | 5.00 | 82.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.16 | 13.76 | 21.95 | 2.00 | 81.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.55 | 12.24 | 19.40 | 2.00 | 81.3 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.07 | 11.99 | 19.29 | 0.00 | 64.2 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.30 | 9.79 | 15.92 | 13.00 | 73.7 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.78
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.97) beats the best remaining Bench Boost opportunity (7.87).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 8.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.97) beats the best remaining Bench Boost opportunity (7.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.21 | 8.59 | 13.89 | 2.00 | 78.8 | 90.0 |
| Bench 1 | Bench Boost | Thomas Strakosha | GK | 4 | 3.9 | 0.78 | 1.79 | 2.97 | 0.00 | 16.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.60 | 13.57 | 22.45 | 12.00 | 83.3 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 3.22 | 9.45 | 15.63 | 1.00 | 61.9 | 16.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 2.85 | 8.49 | 13.93 | 6.00 | 77.3 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.48 | 6.91 | 11.00 | 1.00 | 65.6 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.72 | 2.83 | 5.44 | 1.00 | 27.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.69 | 23.33 | 38.61 | 7.00 | 82.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.80 | 14.24 | 23.73 | 11.00 | 73.9 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.00 | 8.21 | 13.56 | 1.00 | 74.9 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 6.97 | 20.50 | 34.22 | 5.00 | 82.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.80 | 16.15 | 25.84 | 8.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.25 | 15.12 | 23.82 | 5.00 | 82.7 | 77.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.24 | 10.73 | 17.22 | 1.00 | 66.1 | 24.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.49 | 10.41 | 16.74 | 10.00 | 80.4 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 64.41
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.57) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.57) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Issa Kaboré replaced Konstantinos Tsimikas.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.15 | 9.25 | 15.00 | 0.00 | 82.4 | 0.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.30 | 0.96 | 1.71 | 0.00 | 11.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.88 | 13.88 | 22.74 | 1.00 | 82.8 | 90.0 |
| XI | Bench | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.62 | 10.04 | 16.18 | 0.00 | 72.2 | 0.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.19 | 9.06 | 14.73 | 1.00 | 79.9 | 90.0 |
| Bench 3 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 1.81 | 5.89 | 9.83 | 0.00 | 65.1 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.71 | 3.23 | 5.50 | 0.00 | 29.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.57 | 23.21 | 38.24 | 2.00 | 82.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.46 | 14.65 | 24.70 | 1.00 | 79.0 | 89.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.46 | 7.49 | 12.11 | 2.00 | 65.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.19 | 20.48 | 34.61 | 3.00 | 82.8 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 5.73 | 16.22 | 26.25 | 5.00 | 82.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.90 | 12.65 | 20.42 | 6.00 | 64.9 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.11 | 10.03 | 15.83 | 2.00 | 61.3 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.2 | 2.45 | 9.23 | 15.46 | 8.00 | 56.5 | 90.0 |