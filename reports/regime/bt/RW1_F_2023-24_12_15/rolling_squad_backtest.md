# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.59
- Total actual points: 242.00
- Average predicted points: 65.15
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
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.11
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.76 | 10.23 | 16.34 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.37 | 17.25 | 26.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.53 | 11.75 | 18.41 | 9.00 | 88.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 10.95 | 17.76 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.99 | 5.89 | 10.35 | 1.00 | 67.1 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.58 | 4.07 | 6.74 | 2.00 | 46.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.90 | 22.96 | 36.68 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.98 | 17.93 | 28.56 | 6.00 | 88.9 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.94 | 8.04 | 13.49 | 2.00 | 71.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.91 | 21.57 | 35.27 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.52 | 15.77 | 24.35 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.85 | 13.38 | 20.46 | 1.00 | 81.8 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.22 | 13.33 | 21.90 | 2.00 | 85.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.35 | 12.04 | 18.19 | 2.00 | 81.9 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.70
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 5.08, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.69 | 10.21 | 16.07 | 3.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.90 | 24.08 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.42 | 12.64 | 19.50 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.80 | 11.18 | 17.82 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.91 | 5.36 | 9.81 | 0.00 | 60.2 | 0.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.05 | 4.84 | 7.54 | 5.00 | 53.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.69 | 22.77 | 37.80 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.99 | 17.02 | 25.48 | 5.00 | 83.8 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 3.03 | 7.73 | 12.74 | 2.00 | 70.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.74 | 22.29 | 36.37 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.31 | 13.32 | 21.07 | 2.00 | 84.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.01 | 12.68 | 20.21 | 2.00 | 88.8 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.10 | 11.40 | 18.53 | 0.00 | 67.6 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.33 | 9.74 | 15.94 | 13.00 | 74.7 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.02
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (6.31).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (6.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.62 | 9.64 | 15.37 | 2.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.64 | 14.10 | 22.92 | 12.00 | 86.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.14 | 11.39 | 17.88 | 1.00 | 84.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.23 | 9.81 | 15.94 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.11 | 5.61 | 9.16 | 1.00 | 59.4 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.64 | 2.80 | 5.50 | 1.00 | 28.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.89 | 24.15 | 39.89 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 14.77 | 24.38 | 11.00 | 75.0 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.87 | 7.82 | 12.94 | 1.00 | 72.6 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.47 | 21.87 | 36.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.28 | 17.22 | 27.57 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.85 | 15.43 | 24.36 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.19 | 11.96 | 18.87 | 10.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.44 | 10.63 | 16.88 | 1.00 | 69.8 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.76
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.90) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.90) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.15 | 9.19 | 14.74 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.25 | 14.95 | 24.23 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.07 | 11.46 | 18.16 | 1.00 | 83.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.78 | 10.13 | 16.64 | 1.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.64 | 5.21 | 8.40 | 0.00 | 61.6 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.66 | 2.99 | 5.04 | 0.00 | 29.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.90 | 24.38 | 39.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.54 | 15.04 | 24.76 | 1.00 | 84.6 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.11 | 6.53 | 10.70 | 2.00 | 59.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.62 | 21.75 | 36.46 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.20 | 17.06 | 27.32 | 5.00 | 89.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.01 | 12.07 | 19.48 | 6.00 | 66.3 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.11 | 9.54 | 15.19 | 2.00 | 66.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 2.30 | 8.80 | 14.85 | 8.00 | 53.9 | 90.0 |