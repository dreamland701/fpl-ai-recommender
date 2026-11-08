# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 238.29
- Total actual points: 165.00
- Average predicted points: 59.57
- Average actual points: 41.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.94
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.16 | 15.29 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.79 | 4.13 | 6.31 | 0.00 | 47.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.07 | 14.60 | 23.98 | -1.00 | 90.0 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.47 | 10.76 | 17.50 | 2.00 | 81.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.37 | 8.95 | 14.37 | 7.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.51 | 7.34 | 11.72 | 1.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.69 | 7.17 | 11.79 | 5.00 | 76.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.41 | 16.81 | 33.30 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.44 | 14.33 | 24.07 | 2.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.79 | 7.06 | 11.12 | 2.00 | 66.8 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.50 | 34.17 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.41 | 28.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.76 | 11.44 | 19.17 | 1.00 | 81.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.06 | 11.42 | 18.19 | 2.00 | 78.2 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.19 | 10.84 | 17.40 | 2.00 | 88.4 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.33
- Actual score: 52.00
- Transfer: André Onana -> Bernd Leno (projected gain 2.89, hit 0)
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.55 | 15.79 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.56 | 1.72 | 2.93 | 1.00 | 22.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.05 | 11.55 | 18.44 | 7.00 | 83.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.19 | 19.42 | 0.00 | 72.4 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.10 | 8.96 | 14.81 | 0.00 | 80.3 | 0.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.49 | 6.98 | 11.58 | 0.00 | 73.1 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.40 | 6.54 | 10.69 | 0.00 | 72.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.71 | 17.13 | 28.19 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.64 | 10.69 | 23.34 | 0.00 | 34.8 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.63 | 7.07 | 11.41 | 2.00 | 66.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.16 | 22.15 | 36.66 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 18.46 | 29.86 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.81 | 10.22 | 16.44 | 6.00 | 68.6 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.08 | 16.65 | 14.00 | 68.9 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.86 | 8.76 | 14.37 | 2.00 | 67.5 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 59.36
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (8.14).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (8.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.56 | 10.20 | 16.68 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.71 | 4.39 | 6.98 | 0.00 | 51.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.55 | 10.87 | 17.64 | 2.00 | 87.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.57 | 10.48 | 17.93 | 2.00 | 56.2 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 1.18 | 4.57 | 8.32 | 1.00 | 41.0 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.23 | 4.38 | 7.66 | 1.00 | 43.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.15 | 3.91 | 6.86 | 6.00 | 42.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.89 | 18.21 | 28.65 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 10.91 | 23.72 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.53 | 7.23 | 11.43 | 8.00 | 74.2 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.41 | 20.59 | 34.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 18.24 | 29.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.89 | 12.86 | 20.44 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.98 | 11.11 | 18.14 | 2.00 | 70.7 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.08 | 8.98 | 15.48 | 2.00 | 70.9 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.66
- Actual score: 34.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.96 | 8.85 | 14.69 | 0.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.55 | 1.71 | 2.91 | 0.00 | 20.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.89 | 13.49 | 22.45 | 1.00 | 82.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.30 | 11.69 | 18.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.35 | 7.35 | 12.14 | 1.00 | 71.3 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.20 | 6.63 | 10.76 | 1.00 | 71.1 | 90.0 |
| Bench 4 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.06 | 6.45 | 10.55 | 0.00 | 66.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.63 | 14.24 | 22.84 | 2.00 | 74.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.66 | 13.50 | 25.24 | 0.00 | 28.5 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.21 | 8.31 | 13.53 | 5.00 | 78.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.05 | 21.54 | 35.90 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.29 | 17.91 | 29.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.73 | 12.31 | 20.30 | 1.00 | 81.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.60 | 10.38 | 16.82 | 0.00 | 66.2 | 0.0 |
| Bench 2 | Bench Boost | Hwang Hee-chan | MID | 20 | 5.7 | 3.12 | 8.81 | 14.30 | 14.00 | 74.8 | 45.0 |