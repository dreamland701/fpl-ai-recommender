# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 403.06
- Total actual points: 427.00
- Average predicted points: 57.58
- Average actual points: 61.00
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
- Predicted score: 54.65
- Actual score: 66.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.05 | 9.41 | 15.73 | 1.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.50 | 8.54 | 14.38 | 3.00 | 89.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.04 | 14.91 | 24.65 | 6.00 | 96.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.50 | 13.18 | 21.73 | 6.00 | 71.4 | 71.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.52 | 10.50 | 17.04 | 6.00 | 83.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.68 | 10.13 | 16.73 | 2.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 3.42 | 9.36 | 15.40 | 0.00 | 84.8 | 0.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.67 | 10.61 | 17.24 | 2.00 | 70.6 | 70.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.31 | 9.09 | 14.81 | 8.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.69 | 5.19 | 8.41 | 1.00 | 26.0 | 18.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.90 | 17.71 | 29.21 | 6.00 | 80.2 | 87.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.52 | 16.10 | 26.64 | 10.00 | 77.6 | 82.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.08 | 15.51 | 25.97 | 17.00 | 90.0 | 82.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 5.04 | 13.60 | 21.84 | 2.00 | 81.0 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.75 | 11.30 | 18.74 | 2.00 | 63.3 | 89.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 52.99
- Actual score: 71.00
- League average score: 0.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.09 | 8.76 | 14.71 | 3.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.0 | 2.73 | 8.47 | 14.33 | 2.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.87 | 14.61 | 23.77 | 6.00 | 72.1 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.44 | 13.87 | 22.81 | 1.00 | 92.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.90 | 11.39 | 18.06 | 2.00 | 84.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 11.18 | 17.84 | 2.00 | 81.1 | 87.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.71 | 5.33 | 9.38 | 0.00 | 36.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.07 | 9.73 | 15.84 | 8.00 | 73.6 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.69 | 8.06 | 12.87 | 1.00 | 58.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.51 | 4.77 | 7.90 | 1.00 | 26.1 | 45.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 5.79 | 17.30 | 28.10 | 6.00 | 83.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.5 | 5.61 | 17.10 | 27.58 | 17.00 | 75.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 5.12 | 15.84 | 26.50 | 6.00 | 87.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 7.0 | 4.41 | 13.25 | 21.39 | 10.00 | 76.3 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.5 | 3.09 | 10.06 | 16.70 | 4.00 | 72.6 | 71.0 |

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
- Transfer: Yankuba Minteh -> Antoine Semenyo (projected gain 3.04, hit 0)
- Autosub outfielders: Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.52 | 8.47 | 14.32 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.19 | 7.64 | 13.18 | 2.00 | 82.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.44 | 13.45 | 22.29 | 1.00 | 70.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.11 | 13.17 | 21.71 | 2.00 | 86.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.88 | 11.46 | 18.89 | 1.00 | 78.2 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.68 | 11.07 | 17.86 | 5.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 9 | 4.5 | 1.62 | 4.88 | 8.69 | 2.00 | 28.0 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.78 | 10.63 | 16.78 | 0.00 | 69.5 | 0.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.6 | 2.61 | 8.05 | 13.14 | 8.00 | 64.2 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.05 | 5.63 | 9.11 | 0.00 | 40.2 | 61.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.30 | 19.04 | 31.27 | 2.00 | 86.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.86 | 17.38 | 28.42 | 7.00 | 80.3 | 85.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.29 | 16.74 | 27.29 | 3.00 | 80.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.35 | 12.50 | 20.21 | 1.00 | 82.7 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.28 | 12.11 | 20.20 | 2.00 | 68.4 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.67
- Actual score: 54.00
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Danny Welbeck (projected gain 1.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.61 | 8.36 | 14.18 | 3.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.59 | 7.44 | 12.80 | 2.00 | 81.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.41 | 13.16 | 21.75 | 11.00 | 71.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.26 | 12.98 | 21.54 | 2.00 | 85.2 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.32 | 10.30 | 17.02 | 1.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.85 | 9.53 | 16.24 | 1.00 | 61.0 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.06 | 6.65 | 11.24 | 2.00 | 53.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.45 | 10.53 | 16.27 | 6.00 | 62.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 2.98 | 8.83 | 14.57 | 2.00 | 69.2 | 82.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.04 | 5.51 | 8.72 | 1.00 | 42.3 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.28 | 19.33 | 31.09 | 6.00 | 79.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.06 | 15.95 | 26.62 | 4.00 | 75.4 | 45.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.07 | 15.71 | 26.58 | 8.00 | 80.6 | 63.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.43 | 12.74 | 20.50 | 3.00 | 71.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.53 | 11.47 | 18.60 | 2.00 | 75.5 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.62
- Actual score: 76.00
- League average score: 0.00
- Transfer: William Saliba -> Noussair Mazraoui (projected gain 0.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.94 | 8.65 | 14.65 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 4.9 | 2.38 | 7.16 | 12.11 | 2.00 | 82.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.82 | 13.92 | 23.21 | 1.00 | 84.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.29 | 12.83 | 21.12 | 5.00 | 87.9 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 3.92 | 10.96 | 17.68 | 0.00 | 84.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.41 | 10.63 | 17.63 | 9.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.43 | 7.45 | 12.18 | 8.00 | 67.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.57 | 11.14 | 18.08 | 2.00 | 73.1 | 80.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.50 | 8.39 | 13.67 | 1.00 | 65.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.31 | 6.35 | 9.75 | 1.00 | 51.9 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.02 | 20.71 | 34.21 | 10.00 | 90.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.48 | 16.07 | 26.60 | 3.00 | 72.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.01 | 15.81 | 26.52 | 25.00 | 77.5 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 4.16 | 12.38 | 20.41 | 2.00 | 77.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.98 | 10.52 | 17.35 | 7.00 | 67.9 | 88.0 |

## GW7

- Train rows: 137553
- Bank: 1.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 64.18
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (8.04).
- League average score: 0.00
- Transfer: Jordan Pickford -> David Raya Martin (projected gain 2.94, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (8.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.38 | 18.54 | 2.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.72 | 8.46 | 14.10 | 2.00 | 85.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.28 | 13.09 | 21.99 | 8.00 | 80.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.10 | 12.19 | 20.39 | 1.00 | 83.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.83 | 11.17 | 18.56 | 1.00 | 77.1 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.6 | 2.97 | 9.56 | 15.89 | 1.00 | 81.4 | 45.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 9 | 4.4 | 2.76 | 8.27 | 13.36 | 1.00 | 77.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.00 | 11.49 | 18.98 | 8.00 | 70.9 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.7 | 2.91 | 8.53 | 14.40 | 2.00 | 75.1 | 73.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.40 | 4.78 | 7.52 | 7.00 | 34.7 | 63.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.6 | 6.85 | 20.68 | 33.81 | 6.00 | 104.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.55 | 19.21 | 32.24 | 3.00 | 82.8 | 72.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 6.02 | 17.30 | 27.80 | 16.00 | 74.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.26 | 11.83 | 18.94 | 2.00 | 70.7 | 90.0 |
| XI | XI | Eberechi Eze | MID | 7 | 6.9 | 3.66 | 11.62 | 19.17 | 2.00 | 72.1 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 69.14
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.57) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Eberechi Eze -> Bryan Mbeumo (projected gain 4.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.57) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 11.41 | 18.83 | 1.00 | 89.8 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 2.59 | 8.19 | 13.75 | 4.00 | 84.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.75 | 13.98 | 23.36 | 2.00 | 87.5 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.16 | 11.99 | 19.74 | 2.00 | 84.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.95 | 11.37 | 18.48 | 10.00 | 81.9 | 90.0 |
| Bench 2 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.6 | 2.81 | 8.46 | 14.31 | 1.00 | 68.8 | 1.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 9 | 4.4 | 2.46 | 7.09 | 11.72 | -2.00 | 73.3 | 63.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.31 | 12.40 | 20.23 | 9.00 | 83.8 | 80.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.7 | 2.99 | 8.58 | 14.03 | 6.00 | 64.8 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 2.71 | 7.07 | 11.24 | 9.00 | 50.5 | 67.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 10.7 | 6.65 | 20.44 | 32.78 | 2.00 | 93.7 | 90.0 |
| Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.67 | 19.74 | 32.55 | 0.00 | 89.4 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 6.17 | 18.29 | 30.64 | 12.00 | 75.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.4 | 5.06 | 15.46 | 25.02 | 2.00 | 87.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.48 | 10.90 | 17.68 | 2.00 | 77.2 | 90.0 |