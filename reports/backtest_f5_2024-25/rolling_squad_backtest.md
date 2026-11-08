# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 402.62
- Total actual points: 440.00
- Average predicted points: 57.52
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
- Predicted score: 54.20
- Actual score: 68.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.60 | 8.94 | 15.00 | 3.00 | 90.5 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.88 | 8.81 | 14.73 | 1.00 | 89.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.08 | 15.08 | 24.75 | 6.00 | 96.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.52 | 13.07 | 21.74 | 6.00 | 70.8 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.75 | 10.16 | 16.86 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.0 | 3.38 | 9.94 | 16.17 | 6.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 3.37 | 9.22 | 15.16 | 0.00 | 83.8 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.61 | 10.68 | 17.24 | 2.00 | 71.8 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.45 | 9.25 | 15.20 | 8.00 | 69.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.61 | 5.04 | 8.18 | 1.00 | 25.8 | 18.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.78 | 17.10 | 28.32 | 6.00 | 76.8 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.57 | 16.05 | 26.79 | 10.00 | 77.1 | 82.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.10 | 15.62 | 26.03 | 17.00 | 91.1 | 82.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.80 | 13.07 | 20.93 | 2.00 | 79.5 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.87 | 11.67 | 19.34 | 2.00 | 63.8 | 89.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.61
- Actual score: 82.00
- League average score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.14 | 8.93 | 14.97 | 3.00 | 91.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.42 | 7.40 | 12.70 | 2.00 | 80.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.97 | 14.71 | 24.01 | 6.00 | 71.7 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.55 | 14.15 | 23.27 | 1.00 | 92.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 11.19 | 17.89 | 2.00 | 81.3 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.81 | 10.98 | 17.48 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.68 | 5.25 | 9.24 | 0.00 | 34.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.99 | 9.48 | 15.51 | 8.00 | 71.9 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.56 | 7.80 | 12.42 | 1.00 | 57.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.50 | 4.81 | 7.95 | 1.00 | 26.7 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 5.75 | 17.30 | 27.98 | 17.00 | 75.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.71 | 16.88 | 27.53 | 6.00 | 79.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.93 | 15.36 | 25.76 | 6.00 | 85.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.21 | 12.76 | 20.56 | 10.00 | 73.3 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 2.99 | 9.86 | 16.40 | 4.00 | 71.5 | 71.0 |

## GW4

- Train rows: 135569
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.87
- Actual score: 36.00
- League average score: 0.00
- Transfer: Yankuba Minteh -> Antoine Semenyo (projected gain 2.90, hit 0)
- Autosub outfielders: Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.57 | 8.68 | 14.64 | 2.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 1.96 | 6.81 | 11.89 | 2.00 | 78.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.50 | 13.44 | 22.36 | 1.00 | 70.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.08 | 13.06 | 21.56 | 2.00 | 86.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 11.53 | 19.00 | 1.00 | 78.7 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.66 | 10.96 | 17.70 | 5.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.60 | 4.82 | 8.61 | 2.00 | 27.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.81 | 10.77 | 16.98 | 0.00 | 70.0 | 0.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.6 | 2.52 | 7.89 | 12.86 | 8.00 | 64.0 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.07 | 5.68 | 9.17 | 0.00 | 40.4 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.40 | 19.13 | 31.51 | 2.00 | 86.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.85 | 17.27 | 28.27 | 7.00 | 79.4 | 85.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.22 | 16.67 | 27.15 | 3.00 | 81.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.31 | 12.49 | 20.13 | 1.00 | 82.6 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.20 | 12.00 | 19.96 | 2.00 | 67.8 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.82
- Actual score: 54.00
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Danny Welbeck (projected gain 1.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.67 | 8.58 | 14.51 | 3.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.50 | 7.00 | 12.15 | 2.00 | 78.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.42 | 13.09 | 21.72 | 11.00 | 71.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.29 | 13.05 | 21.63 | 2.00 | 85.6 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.32 | 10.22 | 16.93 | 1.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.82 | 9.52 | 16.27 | 1.00 | 61.1 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.09 | 6.78 | 11.44 | 2.00 | 54.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.51 | 10.71 | 16.65 | 6.00 | 63.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.91 | 8.73 | 14.33 | 2.00 | 68.5 | 82.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.03 | 5.46 | 8.60 | 1.00 | 41.6 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.32 | 19.39 | 31.29 | 6.00 | 79.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.07 | 15.89 | 26.60 | 4.00 | 74.7 | 45.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.07 | 15.75 | 26.65 | 8.00 | 81.2 | 63.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.38 | 12.75 | 20.44 | 3.00 | 71.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.53 | 11.61 | 18.74 | 2.00 | 76.4 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.76
- Actual score: 76.00
- League average score: 0.00
- Transfer: William Saliba -> Noussair Mazraoui (projected gain 0.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.95 | 8.69 | 14.71 | 2.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.34 | 6.91 | 11.83 | 2.00 | 81.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.84 | 13.84 | 23.18 | 1.00 | 83.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.30 | 12.89 | 21.24 | 5.00 | 88.6 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.94 | 10.90 | 17.58 | 0.00 | 83.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.41 | 10.69 | 17.71 | 9.00 | 73.8 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.44 | 7.55 | 12.36 | 8.00 | 68.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.58 | 11.17 | 18.15 | 2.00 | 73.2 | 80.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.49 | 8.48 | 13.76 | 1.00 | 65.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.30 | 6.34 | 9.69 | 1.00 | 51.7 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.06 | 20.73 | 34.35 | 10.00 | 90.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.50 | 16.07 | 26.67 | 3.00 | 72.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.05 | 15.89 | 26.62 | 25.00 | 78.5 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.11 | 12.27 | 20.21 | 2.00 | 77.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.95 | 10.56 | 17.28 | 7.00 | 67.9 | 88.0 |

## GW7

- Train rows: 137553
- Bank: 1.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 64.20
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.06).
- League average score: 0.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 2.81, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.32 | 18.43 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.74 | 8.53 | 14.20 | 2.00 | 85.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.29 | 13.06 | 22.02 | 8.00 | 80.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.11 | 12.19 | 20.46 | 1.00 | 84.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.82 | 11.25 | 18.63 | 1.00 | 77.9 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.96 | 9.43 | 15.74 | 1.00 | 80.8 | 45.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.77 | 8.29 | 13.43 | 1.00 | 78.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.00 | 11.49 | 18.84 | 8.00 | 70.3 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.91 | 8.59 | 14.48 | 2.00 | 75.8 | 73.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.41 | 4.81 | 7.61 | 7.00 | 35.3 | 63.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.6 | 6.87 | 20.71 | 33.78 | 6.00 | 104.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.56 | 19.24 | 32.35 | 3.00 | 83.1 | 72.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.03 | 17.30 | 27.74 | 16.00 | 73.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.24 | 11.89 | 18.96 | 2.00 | 71.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 3.64 | 11.59 | 19.06 | 2.00 | 72.1 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 69.17
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.58) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Eberechi Eze -> Bryan Mbeumo (projected gain 4.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 11.42 | 18.85 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 2.58 | 8.17 | 13.66 | 4.00 | 83.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.75 | 13.94 | 23.33 | 2.00 | 87.2 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.14 | 11.91 | 19.59 | 2.00 | 83.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.94 | 11.42 | 18.51 | 10.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.82 | 8.40 | 14.30 | 1.00 | 68.7 | 1.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 9 | 4.4 | 2.45 | 7.03 | 11.58 | -2.00 | 72.7 | 63.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.30 | 12.39 | 20.19 | 9.00 | 83.2 | 80.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.7 | 3.01 | 8.63 | 14.08 | 6.00 | 65.2 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.73 | 7.15 | 11.42 | 9.00 | 51.2 | 67.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.7 | 6.68 | 20.55 | 32.90 | 2.00 | 93.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.66 | 19.80 | 32.61 | 0.00 | 89.4 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 6.19 | 18.31 | 30.66 | 12.00 | 75.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.4 | 5.05 | 15.52 | 25.00 | 2.00 | 87.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.46 | 10.96 | 17.70 | 2.00 | 77.6 | 90.0 |