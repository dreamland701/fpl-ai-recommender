# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 402.31
- Total actual points: 440.00
- Average predicted points: 57.47
- Average actual points: 62.86
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 134294
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.12
- Actual score: 68.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.88 | 8.94 | 14.89 | 1.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.60 | 8.80 | 14.83 | 3.00 | 89.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.08 | 14.95 | 24.59 | 6.00 | 95.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.51 | 13.25 | 21.95 | 6.00 | 72.5 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.72 | 10.26 | 16.95 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 3.36 | 10.03 | 16.26 | 6.00 | 82.2 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 3.36 | 9.21 | 15.14 | 0.00 | 83.7 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.63 | 10.48 | 17.04 | 2.00 | 69.9 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.43 | 9.43 | 15.38 | 8.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.61 | 4.94 | 8.05 | 1.00 | 25.1 | 18.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.75 | 17.28 | 28.48 | 6.00 | 78.8 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.55 | 16.22 | 26.94 | 10.00 | 79.0 | 82.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.13 | 15.61 | 26.07 | 17.00 | 90.7 | 82.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.82 | 12.98 | 20.85 | 2.00 | 78.5 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.87 | 11.64 | 19.32 | 2.00 | 63.6 | 89.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.50
- Actual score: 82.00
- League average score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.12 | 8.84 | 14.84 | 3.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.42 | 7.60 | 12.93 | 2.00 | 82.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.96 | 14.87 | 24.21 | 6.00 | 73.3 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.54 | 14.14 | 23.25 | 1.00 | 92.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.80 | 11.18 | 17.89 | 2.00 | 81.3 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.78 | 11.06 | 17.55 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.68 | 5.25 | 9.25 | 0.00 | 34.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.98 | 9.48 | 15.49 | 8.00 | 71.9 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.57 | 7.70 | 12.32 | 1.00 | 56.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.50 | 4.73 | 7.85 | 1.00 | 26.1 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 5.73 | 17.45 | 28.14 | 17.00 | 76.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.68 | 17.01 | 27.65 | 6.00 | 81.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.96 | 15.35 | 25.77 | 6.00 | 84.9 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.23 | 12.72 | 20.52 | 10.00 | 72.6 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.00 | 9.78 | 16.31 | 4.00 | 70.7 | 71.0 |

## GW4

- Train rows: 135569
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.79
- Actual score: 36.00
- League average score: 0.00
- Transfer: Yankuba Minteh -> Antoine Semenyo (projected gain 2.88, hit 0)
- Autosub outfielders: Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.55 | 8.58 | 14.50 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 1.96 | 6.96 | 12.07 | 2.00 | 79.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.49 | 13.59 | 22.53 | 1.00 | 71.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.07 | 13.06 | 21.55 | 2.00 | 86.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 11.49 | 18.96 | 1.00 | 78.4 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.97 | 17.67 | 5.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.61 | 4.83 | 8.62 | 2.00 | 27.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.80 | 10.70 | 16.89 | 0.00 | 69.4 | 0.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.6 | 2.53 | 7.81 | 12.79 | 8.00 | 63.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.06 | 5.66 | 9.14 | 0.00 | 40.2 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.38 | 19.25 | 31.64 | 2.00 | 87.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.83 | 17.29 | 28.27 | 7.00 | 79.8 | 85.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.25 | 16.62 | 27.11 | 3.00 | 80.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.31 | 12.36 | 19.97 | 1.00 | 81.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.21 | 11.90 | 19.84 | 2.00 | 66.8 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.77
- Actual score: 54.00
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Danny Welbeck (projected gain 1.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.66 | 8.51 | 14.42 | 3.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.49 | 7.14 | 12.31 | 2.00 | 79.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.41 | 13.18 | 21.80 | 11.00 | 72.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.28 | 13.04 | 21.64 | 2.00 | 85.5 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.30 | 10.24 | 16.92 | 1.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.82 | 9.45 | 16.13 | 1.00 | 60.5 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.09 | 6.75 | 11.40 | 2.00 | 54.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.50 | 10.67 | 16.51 | 6.00 | 63.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.93 | 8.66 | 14.30 | 2.00 | 68.0 | 82.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.03 | 5.46 | 8.64 | 1.00 | 42.0 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.31 | 19.44 | 31.30 | 6.00 | 79.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.05 | 15.92 | 26.56 | 4.00 | 75.2 | 45.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.07 | 15.71 | 26.59 | 8.00 | 80.4 | 63.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.40 | 12.67 | 20.36 | 3.00 | 70.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.54 | 11.48 | 18.61 | 2.00 | 75.3 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.70
- Actual score: 76.00
- League average score: 0.00
- Transfer: William Saliba -> Noussair Mazraoui (projected gain 0.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.94 | 8.66 | 14.66 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.32 | 6.97 | 11.80 | 2.00 | 81.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.83 | 13.91 | 23.21 | 1.00 | 84.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.29 | 12.84 | 21.15 | 5.00 | 88.0 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.93 | 10.98 | 17.70 | 0.00 | 84.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.42 | 10.65 | 17.66 | 9.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.44 | 7.48 | 12.23 | 8.00 | 67.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.58 | 11.15 | 18.11 | 2.00 | 73.2 | 80.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.51 | 8.40 | 13.68 | 1.00 | 65.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.30 | 6.32 | 9.71 | 1.00 | 51.9 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.04 | 20.77 | 34.32 | 10.00 | 91.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.49 | 16.09 | 26.63 | 3.00 | 72.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.05 | 15.90 | 26.66 | 25.00 | 78.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.11 | 12.23 | 20.15 | 2.00 | 76.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.98 | 10.50 | 17.32 | 7.00 | 67.9 | 88.0 |

## GW7

- Train rows: 137553
- Bank: 1.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 64.21
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.05).
- League average score: 0.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.37 | 18.53 | 2.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.73 | 8.50 | 14.17 | 2.00 | 85.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.27 | 13.08 | 21.96 | 8.00 | 80.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.10 | 12.18 | 20.38 | 1.00 | 83.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.83 | 11.17 | 18.56 | 1.00 | 77.2 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.94 | 9.48 | 15.75 | 1.00 | 80.8 | 45.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.76 | 8.26 | 13.35 | 1.00 | 77.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.01 | 11.52 | 19.01 | 8.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.92 | 8.56 | 14.44 | 2.00 | 75.2 | 73.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.40 | 4.77 | 7.52 | 7.00 | 34.7 | 63.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.6 | 6.87 | 20.73 | 33.89 | 6.00 | 104.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.56 | 19.24 | 32.27 | 3.00 | 82.8 | 72.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.04 | 17.35 | 27.88 | 16.00 | 74.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.26 | 11.83 | 18.95 | 2.00 | 70.7 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 3.65 | 11.58 | 19.12 | 2.00 | 72.1 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 69.22
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Eberechi Eze -> Bryan Mbeumo (projected gain 4.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 11.42 | 18.84 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 2.58 | 8.18 | 13.75 | 4.00 | 84.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.74 | 13.97 | 23.34 | 2.00 | 87.4 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.14 | 11.93 | 19.63 | 2.00 | 84.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.95 | 11.37 | 18.47 | 10.00 | 82.0 | 90.0 |
| Bench 2 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.80 | 8.43 | 14.25 | 1.00 | 68.6 | 1.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 9 | 4.4 | 2.45 | 7.05 | 11.65 | -2.00 | 73.0 | 63.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.31 | 12.40 | 20.23 | 9.00 | 83.9 | 80.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.7 | 3.01 | 8.64 | 14.13 | 6.00 | 65.2 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.73 | 7.12 | 11.32 | 9.00 | 50.7 | 67.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.7 | 6.69 | 20.53 | 32.92 | 2.00 | 94.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.68 | 19.78 | 32.62 | 0.00 | 89.7 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 6.19 | 18.34 | 30.73 | 12.00 | 75.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.4 | 5.07 | 15.49 | 25.05 | 2.00 | 87.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.48 | 10.90 | 17.69 | 2.00 | 77.2 | 90.0 |