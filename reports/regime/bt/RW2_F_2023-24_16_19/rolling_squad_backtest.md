# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 230.49
- Total actual points: 172.00
- Average predicted points: 57.62
- Average actual points: 43.00
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
- Predicted score: 60.86
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.32 | 9.15 | 15.57 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.31 | 0.63 | 0.00 | 6.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.94 | 14.56 | 23.75 | -1.00 | 90.0 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.50 | 10.62 | 17.03 | 2.00 | 81.9 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.60 | 9.36 | 15.18 | 7.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.53 | 7.81 | 12.20 | 1.00 | 75.7 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.72 | 7.64 | 12.57 | 5.00 | 78.0 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.21 | 24.83 | 40.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.47 | 14.40 | 23.81 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.84 | 7.41 | 11.72 | 2.00 | 67.4 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.85 | 20.81 | 34.10 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.65 | 17.23 | 27.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 12.08 | 19.35 | 2.00 | 80.1 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.24 | 11.50 | 18.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.75 | 11.37 | 19.18 | 1.00 | 82.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.31
- Actual score: 58.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.95, hit 0)
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.49 | 8.48 | 14.09 | 10.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.30 | 0.53 | 0.81 | 0.00 | 6.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.08 | 11.55 | 18.17 | 7.00 | 83.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.20 | 9.87 | 17.38 | 0.00 | 60.1 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.24 | 9.79 | 15.88 | 0.00 | 84.5 | 0.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.02 | 6.36 | 10.51 | 0.00 | 63.2 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.93 | 5.63 | 9.22 | 0.00 | 61.6 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.57 | 16.80 | 27.36 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.48 | 14.43 | 26.31 | 0.00 | 30.2 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.69 | 7.87 | 12.52 | 2.00 | 67.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.09 | 22.10 | 35.89 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.27 | 18.41 | 29.19 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.86 | 10.70 | 17.25 | 6.00 | 71.1 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.58 | 10.19 | 17.05 | 14.00 | 70.7 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.34 | 10.09 | 16.72 | 1.00 | 81.9 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 54.62
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.24) beats the best remaining Bench Boost opportunity (2.89).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 3.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.24) beats the best remaining Bench Boost opportunity (2.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.32 | 9.94 | 16.62 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.27 | 0.73 | 0.99 | 0.00 | 7.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.82 | 11.16 | 18.49 | 2.00 | 59.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.54 | 10.94 | 17.40 | 2.00 | 87.7 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.47 | 5.21 | 8.76 | 1.00 | 49.0 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.39 | 4.44 | 7.77 | 6.00 | 47.6 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.95 | 4.39 | 7.83 | 1.00 | 36.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.78 | 17.86 | 27.98 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.47 | 26.08 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.59 | 7.85 | 12.19 | 8.00 | 75.4 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.31 | 20.44 | 33.56 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.80 | 17.95 | 28.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.82 | 13.31 | 21.02 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.55 | 10.19 | 16.81 | 2.00 | 59.8 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.21 | 9.88 | 16.28 | 2.00 | 82.0 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.70
- Actual score: 29.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.14 | 9.50 | 15.63 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.43 | 0.89 | 1.25 | 0.00 | 9.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.77 | 12.94 | 21.29 | 1.00 | 79.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.16 | 11.40 | 17.98 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.54 | 8.08 | 13.31 | 1.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.15 | 6.67 | 10.78 | 0.00 | 67.8 | 90.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.28 | 6.64 | 10.84 | 1.00 | 72.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.56 | 13.92 | 22.19 | 2.00 | 75.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.28 | 11.25 | 21.22 | 0.00 | 21.4 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.23 | 8.71 | 14.03 | 5.00 | 78.9 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.94 | 20.96 | 34.64 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.15 | 17.38 | 27.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.78 | 12.85 | 20.97 | 1.00 | 81.8 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.26 | 10.25 | 16.63 | 5.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.5 | 3.07 | 9.92 | 16.25 | 0.00 | 56.5 | 0.0 |