# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 401.63
- Total actual points: 438.00
- Average predicted points: 57.38
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
- Predicted score: 54.13
- Actual score: 68.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.88 | 8.97 | 14.94 | 1.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.59 | 8.75 | 14.72 | 3.00 | 89.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.07 | 14.90 | 24.49 | 6.00 | 95.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.52 | 13.28 | 22.02 | 6.00 | 72.4 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.73 | 10.30 | 17.03 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.0 | 3.36 | 10.06 | 16.30 | 6.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 3.36 | 9.19 | 15.10 | 0.00 | 83.8 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.63 | 10.54 | 17.15 | 2.00 | 69.7 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.43 | 9.46 | 15.43 | 8.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.61 | 4.94 | 8.07 | 1.00 | 25.0 | 18.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.75 | 17.27 | 28.47 | 6.00 | 78.9 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.54 | 16.19 | 26.89 | 10.00 | 79.1 | 82.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.12 | 15.59 | 26.02 | 17.00 | 90.8 | 82.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.82 | 12.97 | 20.83 | 2.00 | 78.5 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.87 | 11.59 | 19.22 | 2.00 | 63.8 | 89.0 |

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
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.11 | 8.82 | 14.78 | 3.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.42 | 7.60 | 12.94 | 2.00 | 82.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.96 | 14.87 | 24.19 | 6.00 | 73.4 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.53 | 14.13 | 23.22 | 1.00 | 93.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 11.20 | 17.91 | 2.00 | 81.2 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.78 | 11.07 | 17.57 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.68 | 5.24 | 9.23 | 0.00 | 34.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.99 | 9.49 | 15.52 | 8.00 | 71.8 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.57 | 7.71 | 12.34 | 1.00 | 56.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.50 | 4.75 | 7.89 | 1.00 | 25.9 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 5.73 | 17.44 | 28.13 | 17.00 | 76.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.68 | 17.00 | 27.62 | 6.00 | 81.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.96 | 15.34 | 25.75 | 6.00 | 85.0 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.23 | 12.71 | 20.52 | 10.00 | 72.6 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.00 | 9.75 | 16.26 | 4.00 | 70.8 | 71.0 |

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
- Transfer: Yankuba Minteh -> Antoine Semenyo (projected gain 2.89, hit 0)
- Autosub outfielders: Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.55 | 8.55 | 14.43 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 1.96 | 6.97 | 12.08 | 2.00 | 79.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.49 | 13.59 | 22.54 | 1.00 | 71.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.07 | 13.06 | 21.54 | 2.00 | 86.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 11.49 | 18.96 | 1.00 | 78.4 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.96 | 17.67 | 5.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.60 | 4.82 | 8.61 | 2.00 | 27.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.80 | 10.70 | 16.90 | 0.00 | 69.3 | 0.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.6 | 2.53 | 7.78 | 12.71 | 8.00 | 63.4 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.07 | 5.69 | 9.19 | 0.00 | 40.0 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.38 | 19.25 | 31.63 | 2.00 | 87.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.83 | 17.29 | 28.27 | 7.00 | 79.8 | 85.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.25 | 16.61 | 27.11 | 3.00 | 80.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.31 | 12.37 | 19.98 | 1.00 | 81.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.21 | 11.89 | 19.82 | 2.00 | 66.8 | 90.0 |

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
- Transfer: João Pedro Junqueira de Jesus -> Danny Welbeck (projected gain 1.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.66 | 8.47 | 14.36 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.49 | 7.15 | 12.30 | 2.00 | 80.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.41 | 13.19 | 21.79 | 11.00 | 72.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.28 | 13.02 | 21.62 | 2.00 | 85.4 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.30 | 10.26 | 16.94 | 1.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.82 | 9.47 | 16.15 | 1.00 | 60.6 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.09 | 6.75 | 11.41 | 2.00 | 54.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.50 | 10.67 | 16.55 | 6.00 | 63.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.94 | 8.66 | 14.25 | 2.00 | 68.4 | 82.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.03 | 5.49 | 8.70 | 1.00 | 41.7 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.31 | 19.43 | 31.29 | 6.00 | 79.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.05 | 15.92 | 26.56 | 4.00 | 75.2 | 45.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.07 | 15.70 | 26.58 | 8.00 | 80.4 | 63.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.40 | 12.66 | 20.34 | 3.00 | 70.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.54 | 11.44 | 18.47 | 2.00 | 76.0 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.71
- Actual score: 76.00
- League average score: 0.00
- Transfer: William Saliba -> Noussair Mazraoui (projected gain 0.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.94 | 8.63 | 14.58 | 2.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.32 | 6.97 | 11.79 | 2.00 | 81.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.83 | 13.90 | 23.19 | 1.00 | 84.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.29 | 12.83 | 21.12 | 5.00 | 88.0 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.93 | 10.96 | 17.68 | 0.00 | 84.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.42 | 10.66 | 17.67 | 9.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.44 | 7.48 | 12.24 | 8.00 | 67.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.58 | 11.16 | 18.12 | 2.00 | 73.2 | 80.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.51 | 8.39 | 13.60 | 1.00 | 65.5 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.30 | 6.35 | 9.77 | 1.00 | 51.6 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.05 | 20.77 | 34.30 | 10.00 | 91.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.49 | 16.08 | 26.60 | 3.00 | 72.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.05 | 15.90 | 26.65 | 25.00 | 78.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.12 | 12.22 | 20.12 | 2.00 | 76.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.98 | 10.50 | 17.22 | 7.00 | 68.6 | 88.0 |

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
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 2.94, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.39 | 18.56 | 2.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.73 | 8.47 | 14.12 | 2.00 | 85.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.27 | 13.06 | 21.93 | 8.00 | 80.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.10 | 12.19 | 20.38 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.83 | 11.16 | 18.57 | 1.00 | 77.0 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.94 | 9.48 | 15.75 | 1.00 | 80.9 | 45.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.76 | 8.27 | 13.39 | 1.00 | 77.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.01 | 11.55 | 19.05 | 8.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.91 | 8.48 | 14.32 | 2.00 | 75.3 | 73.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.40 | 4.81 | 7.59 | 7.00 | 34.6 | 63.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.6 | 6.87 | 20.73 | 33.87 | 6.00 | 104.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.56 | 19.24 | 32.26 | 3.00 | 82.9 | 72.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.04 | 17.34 | 27.86 | 16.00 | 74.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.26 | 11.80 | 18.81 | 2.00 | 71.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 3.65 | 11.56 | 19.07 | 2.00 | 72.2 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 68.52
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.83) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Cameron Archer -> Raúl Jiménez (projected gain 1.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.83) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 11.43 | 18.87 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 2.58 | 8.14 | 13.68 | 4.00 | 84.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.74 | 13.95 | 23.31 | 2.00 | 87.5 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.14 | 11.92 | 19.64 | 2.00 | 83.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.95 | 11.38 | 18.49 | 10.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.80 | 8.43 | 14.26 | 1.00 | 68.4 | 1.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 9 | 4.4 | 2.45 | 7.07 | 11.69 | -2.00 | 72.9 | 63.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.31 | 12.41 | 20.23 | 9.00 | 84.0 | 80.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.6 | 3.77 | 10.46 | 16.25 | 7.00 | 62.8 | 90.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.7 | 3.00 | 8.58 | 14.07 | 6.00 | 65.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.7 | 6.69 | 20.53 | 32.92 | 2.00 | 94.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.68 | 19.78 | 32.58 | 0.00 | 89.9 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 6.19 | 18.34 | 30.71 | 12.00 | 75.8 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.8 | 3.36 | 10.76 | 18.09 | 2.00 | 70.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.46 | 10.76 | 17.52 | 2.00 | 77.0 | 90.0 |