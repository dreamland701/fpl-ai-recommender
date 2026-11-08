# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 401.73
- Total actual points: 438.00
- Average predicted points: 57.39
- Average actual points: 62.57
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
- Predicted score: 54.17
- Actual score: 68.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.88 | 8.98 | 14.97 | 1.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.59 | 8.71 | 14.63 | 3.00 | 90.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.07 | 14.87 | 24.41 | 6.00 | 95.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.53 | 13.33 | 22.11 | 6.00 | 72.5 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.73 | 10.33 | 17.09 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.0 | 3.37 | 10.07 | 16.34 | 6.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 3.36 | 9.17 | 15.06 | 0.00 | 83.8 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.64 | 10.59 | 17.25 | 2.00 | 69.5 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.43 | 9.47 | 15.47 | 8.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.61 | 4.95 | 8.08 | 1.00 | 25.0 | 18.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.76 | 17.28 | 28.47 | 6.00 | 79.1 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.55 | 16.19 | 26.86 | 10.00 | 79.3 | 82.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.12 | 15.57 | 25.98 | 17.00 | 90.9 | 82.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.82 | 12.98 | 20.83 | 2.00 | 78.6 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.87 | 11.57 | 19.15 | 2.00 | 63.8 | 89.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.51
- Actual score: 82.00
- League average score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.11 | 8.80 | 14.74 | 3.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.42 | 7.60 | 12.94 | 2.00 | 82.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.96 | 14.87 | 24.19 | 6.00 | 73.6 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.53 | 14.12 | 23.20 | 1.00 | 93.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 11.21 | 17.94 | 2.00 | 81.1 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.78 | 11.07 | 17.58 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.68 | 5.23 | 9.21 | 0.00 | 34.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.99 | 9.50 | 15.54 | 8.00 | 71.8 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.58 | 7.72 | 12.36 | 1.00 | 56.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.50 | 4.77 | 7.92 | 1.00 | 25.8 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 5.73 | 17.45 | 28.14 | 17.00 | 77.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.68 | 16.99 | 27.60 | 6.00 | 81.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.96 | 15.34 | 25.74 | 6.00 | 85.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.24 | 12.72 | 20.52 | 10.00 | 72.6 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.00 | 9.74 | 16.22 | 4.00 | 70.9 | 71.0 |

## GW4

- Train rows: 135569
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.81
- Actual score: 36.00
- League average score: 0.00
- Transfer: Yankuba Minteh -> Antoine Semenyo (projected gain 2.90, hit 0)
- Autosub outfielders: Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.55 | 8.52 | 14.38 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 1.95 | 6.96 | 12.07 | 2.00 | 79.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.49 | 13.60 | 22.55 | 1.00 | 71.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.07 | 13.06 | 21.54 | 2.00 | 86.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 11.49 | 18.96 | 1.00 | 78.4 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.96 | 17.66 | 5.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.60 | 4.82 | 8.60 | 2.00 | 27.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.81 | 10.71 | 16.92 | 0.00 | 69.4 | 0.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.6 | 2.53 | 7.76 | 12.66 | 8.00 | 63.6 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.07 | 5.70 | 9.23 | 0.00 | 39.8 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.38 | 19.25 | 31.63 | 2.00 | 87.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.83 | 17.29 | 28.27 | 7.00 | 79.8 | 85.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.25 | 16.61 | 27.10 | 3.00 | 80.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.31 | 12.38 | 19.99 | 1.00 | 81.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.21 | 11.89 | 19.82 | 2.00 | 66.8 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.80
- Actual score: 54.00
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Danny Welbeck (projected gain 1.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.66 | 8.46 | 14.31 | 3.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.49 | 7.14 | 12.27 | 2.00 | 80.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.42 | 13.20 | 21.80 | 11.00 | 72.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.28 | 13.01 | 21.61 | 2.00 | 85.4 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.31 | 10.27 | 16.96 | 1.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.83 | 9.49 | 16.18 | 1.00 | 60.5 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.09 | 6.75 | 11.42 | 2.00 | 53.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.50 | 10.69 | 16.60 | 6.00 | 62.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.94 | 8.66 | 14.22 | 2.00 | 68.7 | 82.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.04 | 5.51 | 8.77 | 1.00 | 41.6 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.32 | 19.44 | 31.30 | 6.00 | 79.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.05 | 15.93 | 26.57 | 4.00 | 75.2 | 45.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.07 | 15.70 | 26.58 | 8.00 | 80.5 | 63.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.40 | 12.66 | 20.33 | 3.00 | 70.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.54 | 11.41 | 18.36 | 2.00 | 76.5 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.74
- Actual score: 76.00
- League average score: 0.00
- Transfer: William Saliba -> Noussair Mazraoui (projected gain 0.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.94 | 8.60 | 14.52 | 2.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.31 | 6.95 | 11.76 | 2.00 | 81.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.83 | 13.91 | 23.19 | 1.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.29 | 12.82 | 21.10 | 5.00 | 88.0 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.93 | 10.96 | 17.68 | 0.00 | 84.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.42 | 10.67 | 17.69 | 9.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.44 | 7.47 | 12.23 | 8.00 | 67.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.59 | 11.18 | 18.15 | 2.00 | 73.3 | 80.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.51 | 8.37 | 13.53 | 1.00 | 65.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.30 | 6.37 | 9.81 | 1.00 | 51.2 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.05 | 20.77 | 34.29 | 10.00 | 91.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.49 | 16.07 | 26.57 | 3.00 | 72.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.05 | 15.90 | 26.65 | 25.00 | 78.3 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.12 | 12.22 | 20.10 | 2.00 | 76.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.98 | 10.48 | 17.12 | 7.00 | 69.1 | 88.0 |

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
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 2.96, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.39 | 18.57 | 2.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.73 | 8.45 | 14.07 | 2.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.27 | 13.06 | 21.92 | 8.00 | 80.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.09 | 12.18 | 20.36 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.83 | 11.17 | 18.60 | 1.00 | 76.9 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.93 | 9.46 | 15.72 | 1.00 | 80.9 | 45.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.75 | 8.26 | 13.40 | 1.00 | 77.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.02 | 11.57 | 19.08 | 8.00 | 71.1 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.90 | 8.44 | 14.24 | 2.00 | 75.4 | 73.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.40 | 4.84 | 7.65 | 7.00 | 34.4 | 63.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.6 | 6.87 | 20.73 | 33.86 | 6.00 | 104.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.56 | 19.24 | 32.24 | 3.00 | 82.9 | 72.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.03 | 17.33 | 27.83 | 16.00 | 74.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.25 | 11.76 | 18.69 | 2.00 | 71.9 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 3.65 | 11.55 | 19.04 | 2.00 | 72.2 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 68.50
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.82) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Cameron Archer -> Raúl Jiménez (projected gain 1.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.82) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 11.44 | 18.88 | 1.00 | 89.8 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 2.58 | 8.13 | 13.65 | 4.00 | 84.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.72 | 13.93 | 23.27 | 2.00 | 87.5 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.14 | 11.92 | 19.63 | 2.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.95 | 11.39 | 18.53 | 10.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.79 | 8.43 | 14.27 | 1.00 | 68.3 | 1.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 9 | 4.4 | 2.45 | 7.08 | 11.72 | -2.00 | 72.8 | 63.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.31 | 12.41 | 20.22 | 9.00 | 84.0 | 80.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 3.77 | 10.48 | 16.28 | 7.00 | 62.7 | 90.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.7 | 3.00 | 8.57 | 14.06 | 6.00 | 65.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.7 | 6.69 | 20.54 | 32.93 | 2.00 | 94.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.67 | 19.76 | 32.54 | 0.00 | 90.1 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 6.19 | 18.34 | 30.71 | 12.00 | 75.9 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 3.36 | 10.76 | 18.09 | 2.00 | 70.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.46 | 10.72 | 17.45 | 2.00 | 77.2 | 90.0 |