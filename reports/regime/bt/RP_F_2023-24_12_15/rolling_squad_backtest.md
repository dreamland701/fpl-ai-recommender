# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 260.42
- Total actual points: 242.00
- Average predicted points: 65.10
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
- Predicted score: 63.85
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.79 | 10.20 | 16.24 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Marek Rodák | GK | 10 | 3.9 | 0.08 | 0.64 | 1.25 | 0.00 | 7.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.20 | 16.86 | 26.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.32 | 11.46 | 17.96 | 9.00 | 89.5 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.83 | 11.29 | 18.07 | 1.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.02 | 6.36 | 11.14 | 1.00 | 69.2 | 86.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 1.65 | 4.53 | 7.37 | 2.00 | 48.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.24 | 22.32 | 36.24 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.67 | 17.05 | 26.97 | 6.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.82 | 7.65 | 12.69 | 2.00 | 69.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 7.03 | 21.54 | 35.33 | 16.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.48 | 15.88 | 24.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.85 | 13.24 | 20.60 | 1.00 | 81.9 | 45.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.89 | 13.17 | 21.83 | 2.00 | 83.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.30 | 11.76 | 17.78 | 2.00 | 80.1 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.22
- Actual score: 54.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.94, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.77 | 10.20 | 16.11 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Marek Rodák | GK | 10 | 3.9 | 0.49 | 0.93 | 1.51 | 0.00 | 5.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.35 | 23.44 | 1.00 | 88.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.47 | 12.90 | 19.77 | 6.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.81 | 11.07 | 17.64 | 1.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.93 | 5.56 | 9.95 | 0.00 | 60.0 | 0.0 |
| Bench 3 | Bench | George Baldock | DEF | 17 | 3.8 | 2.17 | 5.49 | 8.61 | 5.00 | 55.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.71 | 23.26 | 38.13 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.80 | 15.75 | 24.13 | 5.00 | 80.1 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.50 | 12.22 | 2.00 | 67.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.9 | 6.90 | 22.52 | 36.96 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.24 | 13.88 | 22.21 | 2.00 | 84.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.62 | 12.34 | 19.60 | 2.00 | 83.9 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.07 | 12.01 | 19.33 | 0.00 | 64.8 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.20 | 9.46 | 15.30 | 13.00 | 70.3 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.39
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.86) beats the best remaining Bench Boost opportunity (6.57).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 9.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.86) beats the best remaining Bench Boost opportunity (6.57).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.66 | 9.77 | 15.59 | 2.00 | 83.4 | 90.0 |
| Bench 1 | Bench Boost | Marek Rodák | GK | 10 | 3.9 | 0.00 | 0.46 | 0.87 | 0.00 | 5.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.67 | 13.65 | 22.62 | 12.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.25 | 11.87 | 18.54 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.27 | 9.65 | 15.67 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench Boost | George Baldock | DEF | 17 | 3.8 | 2.25 | 6.28 | 10.13 | 1.00 | 60.5 | 24.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.77 | 3.00 | 5.76 | 1.00 | 28.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.17 | 24.66 | 40.62 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.71 | 13.99 | 23.29 | 11.00 | 72.7 | 90.0 |
| Bench 2 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.64 | 12.49 | 1.00 | 69.6 | 45.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.53 | 22.13 | 36.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.25 | 17.36 | 27.62 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.76 | 16.54 | 26.00 | 5.00 | 90.0 | 77.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 3.94 | 11.66 | 18.60 | 10.00 | 88.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.15 | 10.46 | 16.70 | 1.00 | 62.4 | 24.0 |

## GW15

- Train rows: 114034
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.95
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.18 | 9.19 | 14.88 | 0.00 | 82.2 | 0.0 |
| Bench 1 | Bench | Marek Rodák | GK | 10 | 3.9 | 0.34 | 0.65 | 1.05 | 0.00 | 2.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.37 | 15.19 | 24.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.08 | 11.48 | 18.30 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.66 | 9.89 | 16.28 | 1.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.78 | 5.80 | 9.63 | 0.00 | 63.2 | 90.0 |
| Bench 4 | Bench | George Baldock | DEF | 17 | 3.8 | 0.75 | 3.36 | 5.75 | 0.00 | 30.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.06 | 24.55 | 40.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.47 | 14.49 | 24.43 | 1.00 | 80.9 | 89.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.13 | 6.46 | 10.45 | 2.00 | 57.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.0 | 7.73 | 21.98 | 36.91 | 3.00 | 90.0 | 66.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 6.18 | 17.41 | 27.97 | 5.00 | 89.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.85 | 12.48 | 20.06 | 6.00 | 61.7 | 39.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.9 | 3.10 | 10.03 | 15.83 | 2.00 | 61.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 2.16 | 8.40 | 14.20 | 8.00 | 49.5 | 90.0 |