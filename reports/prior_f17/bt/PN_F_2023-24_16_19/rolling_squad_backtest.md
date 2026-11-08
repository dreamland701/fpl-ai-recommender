# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.18
- Total actual points: 156.00
- Average predicted points: 59.80
- Average actual points: 39.00
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
- Predicted score: 61.03
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.20 | 8.88 | 15.11 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.79 | 4.31 | 6.75 | 0.00 | 46.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.00 | 14.77 | 24.29 | -1.00 | 90.0 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.51 | 10.65 | 17.18 | 2.00 | 82.4 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.51 | 9.35 | 15.06 | 7.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.77 | 7.78 | 12.77 | 5.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.49 | 7.59 | 11.85 | 1.00 | 73.9 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.34 | 24.63 | 40.03 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.35 | 24.00 | 2.00 | 87.2 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.87 | 7.65 | 12.13 | 2.00 | 68.7 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.81 | 20.36 | 33.53 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.70 | 17.40 | 28.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 12.44 | 19.89 | 2.00 | 79.6 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.26 | 11.69 | 18.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.75 | 11.41 | 19.17 | 1.00 | 81.4 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.27
- Actual score: 52.00
- Transfer: André Onana -> Bernd Leno (projected gain 1.46, hit 0)
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.16 | 9.84 | 15.95 | 3.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.69 | 2.18 | 3.66 | 1.00 | 24.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.07 | 11.57 | 18.30 | 7.00 | 84.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.27 | 9.89 | 17.71 | 0.00 | 61.2 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.23 | 9.65 | 15.62 | 0.00 | 83.4 | 0.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.02 | 6.43 | 10.63 | 0.00 | 62.7 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.82 | 5.37 | 8.86 | 0.00 | 59.5 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.68 | 16.98 | 27.68 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.53 | 14.13 | 26.09 | 0.00 | 32.4 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.73 | 7.95 | 12.64 | 2.00 | 68.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.21 | 22.17 | 36.00 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 18.47 | 29.46 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.90 | 11.08 | 17.79 | 6.00 | 70.8 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.63 | 10.50 | 17.42 | 14.00 | 69.7 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.03 | 9.46 | 15.52 | 2.00 | 71.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 59.14
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (8.18).
- Transfer: Hwang Hee-chan -> Dwight McNeil (projected gain 0.14, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (8.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.58 | 10.28 | 16.70 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.73 | 4.85 | 7.58 | 0.00 | 50.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.58 | 19.59 | 2.00 | 61.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.58 | 11.03 | 17.60 | 2.00 | 88.4 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.46 | 5.25 | 8.81 | 1.00 | 48.7 | 90.0 |
| Bench 2 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.28 | 4.09 | 7.15 | 6.00 | 45.7 | 90.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.89 | 4.08 | 7.32 | 1.00 | 34.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.82 | 18.59 | 28.98 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.53 | 26.91 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.60 | 7.87 | 12.38 | 8.00 | 75.8 | 89.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.44 | 20.47 | 33.69 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 18.12 | 28.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.83 | 13.49 | 21.30 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.48 | 10.43 | 17.11 | 2.00 | 59.6 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.11 | 9.77 | 16.13 | 2.00 | 81.2 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.74
- Actual score: 25.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.13) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Vitalii Mykolenko -> Gabriel dos Santos Magalhães (projected gain 2.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.13) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.98 | 8.87 | 14.86 | 0.00 | 84.6 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.70 | 2.31 | 3.73 | 0.00 | 23.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.86 | 13.44 | 22.19 | 1.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.27 | 11.55 | 18.33 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.74 | 10.24 | 16.43 | 1.00 | 88.1 | 90.0 |
| Bench 4 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.16 | 6.84 | 11.05 | 0.00 | 68.5 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.18 | 6.41 | 10.47 | 1.00 | 70.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.71 | 14.59 | 23.20 | 2.00 | 76.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.50 | 11.12 | 21.15 | 0.00 | 24.6 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.28 | 8.80 | 14.20 | 5.00 | 79.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.11 | 21.04 | 34.88 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.52 | 28.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.73 | 12.91 | 21.06 | 1.00 | 81.4 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.11 | 10.08 | 16.30 | 5.00 | 81.2 | 90.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.5 | 3.08 | 9.93 | 16.10 | 0.00 | 54.6 | 0.0 |