# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 229.43
- Total actual points: 172.00
- Average predicted points: 57.36
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
- Predicted score: 60.78
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.35 | 9.12 | 15.50 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.26 | 0.58 | 0.00 | 6.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.92 | 14.43 | 23.48 | -1.00 | 89.5 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.52 | 10.64 | 17.04 | 2.00 | 82.1 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.68 | 9.36 | 15.28 | 7.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.51 | 7.79 | 12.19 | 1.00 | 76.3 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.69 | 7.53 | 12.52 | 5.00 | 78.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.09 | 24.91 | 40.05 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.48 | 14.54 | 23.86 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.86 | 7.38 | 11.65 | 2.00 | 67.4 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.85 | 20.99 | 34.38 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.65 | 17.18 | 27.56 | 2.00 | 89.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.16 | 11.87 | 19.05 | 2.00 | 81.0 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.76 | 11.38 | 19.20 | 1.00 | 83.9 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.23 | 11.29 | 18.16 | 2.00 | 90.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.79
- Actual score: 58.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 1.13, hit 0)
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.44 | 8.31 | 13.89 | 10.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.28 | 0.54 | 0.79 | 0.00 | 6.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.09 | 11.59 | 18.20 | 7.00 | 83.4 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.17 | 9.94 | 17.29 | 0.00 | 59.5 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.28 | 9.90 | 16.03 | 0.00 | 86.0 | 0.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.04 | 6.35 | 10.51 | 0.00 | 64.4 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.97 | 5.64 | 9.19 | 0.00 | 62.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.49 | 16.70 | 27.27 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.44 | 14.62 | 26.49 | 0.00 | 28.0 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.69 | 7.95 | 12.65 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.93 | 21.80 | 35.53 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 18.38 | 29.06 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.86 | 10.49 | 16.93 | 6.00 | 71.9 | 83.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.36 | 10.08 | 16.70 | 1.00 | 82.4 | 45.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.58 | 10.02 | 16.90 | 14.00 | 72.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 54.78
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.32) beats the best remaining Bench Boost opportunity (2.97).
- Transfer: Abdoulaye Doucouré -> Dwight McNeil (projected gain 3.13, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.32) beats the best remaining Bench Boost opportunity (2.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.22 | 9.67 | 16.34 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.28 | 0.75 | 1.04 | 0.00 | 6.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.88 | 11.03 | 17.89 | 2.00 | 57.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.53 | 10.90 | 17.37 | 2.00 | 87.7 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.49 | 5.23 | 8.83 | 1.00 | 49.6 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 1.00 | 4.59 | 8.15 | 1.00 | 38.4 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.42 | 4.54 | 7.97 | 6.00 | 47.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.79 | 17.35 | 27.39 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.57 | 25.65 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.62 | 7.97 | 12.23 | 8.00 | 76.0 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.19 | 20.32 | 33.43 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.76 | 17.82 | 28.21 | 1.00 | 89.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.84 | 13.21 | 20.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.64 | 10.10 | 16.70 | 2.00 | 60.5 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.32 | 10.02 | 16.43 | 2.00 | 83.2 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.08
- Actual score: 29.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Charlie Taylor replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.12 | 9.52 | 15.60 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.43 | 0.86 | 1.19 | 0.00 | 9.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.73 | 12.64 | 20.76 | 1.00 | 78.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.08 | 11.28 | 17.83 | 1.00 | 89.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.61 | 8.32 | 13.68 | 1.00 | 76.6 | 90.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.30 | 6.63 | 10.81 | 1.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.16 | 6.63 | 10.73 | 0.00 | 68.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.49 | 13.51 | 21.71 | 2.00 | 75.3 | 90.0 |
| Bench 2 | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.07 | 11.21 | 21.22 | 0.00 | 17.8 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.22 | 8.74 | 14.07 | 5.00 | 79.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.80 | 20.79 | 34.41 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.09 | 17.27 | 27.71 | 2.00 | 89.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.86 | 12.89 | 21.04 | 1.00 | 82.8 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.39 | 10.42 | 16.93 | 5.00 | 83.2 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.08 | 9.98 | 16.48 | 0.00 | 58.5 | 0.0 |