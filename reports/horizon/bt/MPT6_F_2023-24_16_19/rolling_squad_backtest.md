# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 231.98
- Total actual points: 164.00
- Average predicted points: 58.00
- Average actual points: 41.00
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
- Predicted score: 60.95
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.20 | 15.34 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.34 | 0.58 | 0.93 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.36 | 23.59 | -1.00 | 90.0 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.48 | 10.79 | 17.52 | 2.00 | 81.8 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.48 | 9.22 | 14.77 | 7.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.55 | 7.44 | 11.86 | 1.00 | 75.1 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.73 | 7.29 | 11.97 | 5.00 | 77.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.35 | 16.70 | 33.05 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.46 | 14.40 | 24.15 | 2.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.82 | 7.15 | 11.26 | 2.00 | 67.6 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.83 | 20.71 | 34.46 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.69 | 17.21 | 27.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.09 | 11.48 | 18.29 | 2.00 | 78.8 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.72 | 11.36 | 19.04 | 1.00 | 80.8 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.22 | 10.95 | 17.56 | 2.00 | 89.2 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.06
- Actual score: 52.00
- Transfer: André Onana -> Bernd Leno (projected gain 3.19, hit 0)
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 9.54 | 15.77 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.25 | 0.46 | 0.00 | 6.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.05 | 11.55 | 18.44 | 7.00 | 84.1 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.26 | 9.86 | 17.33 | 0.00 | 60.9 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.20 | 9.23 | 15.23 | 0.00 | 82.7 | 0.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.00 | 5.71 | 9.61 | 0.00 | 62.2 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.90 | 5.24 | 8.66 | 0.00 | 60.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.64 | 16.94 | 27.87 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.54 | 10.49 | 22.90 | 0.00 | 32.6 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.68 | 7.20 | 11.62 | 2.00 | 67.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.22 | 22.31 | 36.88 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.33 | 18.43 | 29.80 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.87 | 10.38 | 16.69 | 6.00 | 69.9 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.60 | 10.07 | 16.63 | 14.00 | 68.8 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 2.99 | 9.08 | 14.87 | 2.00 | 70.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 54.71
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (1.17) beats the best remaining Bench Boost opportunity (2.80).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (1.17) beats the best remaining Bench Boost opportunity (2.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.55 | 10.16 | 16.62 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.77 | 1.23 | 0.00 | 8.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.75 | 10.99 | 18.76 | 2.00 | 60.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.56 | 10.87 | 17.63 | 2.00 | 87.9 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.42 | 4.84 | 8.38 | 1.00 | 47.8 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.34 | 4.38 | 7.59 | 6.00 | 46.8 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.88 | 3.77 | 7.07 | 1.00 | 34.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.78 | 17.93 | 28.20 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 10.82 | 23.55 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.55 | 7.29 | 11.53 | 8.00 | 74.7 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 20.67 | 34.42 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.12 | 29.22 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.80 | 12.65 | 20.12 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.47 | 9.78 | 16.09 | 2.00 | 59.1 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.20 | 9.30 | 15.95 | 2.00 | 73.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.26
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 2.35, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.11) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.95 | 8.82 | 14.64 | 0.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.80 | 1.36 | 0.00 | 10.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.84 | 13.35 | 22.23 | 1.00 | 81.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.25 | 11.56 | 18.59 | 1.00 | 90.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.45 | 7.61 | 12.53 | 1.00 | 73.4 | 90.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.25 | 6.76 | 10.97 | 1.00 | 72.2 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.13 | 6.63 | 10.82 | 0.00 | 67.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.67 | 14.32 | 22.95 | 2.00 | 75.1 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.51 | 13.07 | 24.49 | 0.00 | 25.1 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.23 | 8.37 | 13.63 | 5.00 | 78.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 21.69 | 36.10 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.72 | 28.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.71 | 12.24 | 20.18 | 1.00 | 80.7 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.10 | 9.77 | 15.74 | 5.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.5 | 3.07 | 9.01 | 14.68 | 0.00 | 54.4 | 0.0 |