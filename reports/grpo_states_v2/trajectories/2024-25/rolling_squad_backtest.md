# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2209.70
- Total actual points: 2180.00
- Average predicted points: 59.72
- Average actual points: 58.92
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 134294
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.42
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.57 | 10.76 | 17.78 | 10.00 | 93.6 | 90.0 |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.91 | 10.32 | 16.53 | 2.00 | 91.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.60 | 16.03 | 26.17 | 6.00 | 88.6 | 71.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.34 | 14.69 | 24.43 | 6.00 | 96.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 5.06 | 13.34 | 21.38 | 2.00 | 103.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.32 | 12.69 | 20.81 | 6.00 | 99.1 | 90.0 |
| Bench 2 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 3.87 | 10.79 | 17.21 | 4.00 | 97.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.42 | 12.36 | 19.70 | 2.00 | 84.2 | 70.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 3.69 | 10.52 | 17.04 | 9.00 | 86.7 | 78.0 |
| Bench 4 | Bench | Daniel Jebbison | FWD | 3 | 4.5 | 1.70 | 4.88 | 7.79 | 1.00 | 38.4 | 5.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 7.22 | 20.78 | 34.08 | 10.00 | 105.3 | 82.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 6.62 | 19.64 | 32.23 | 6.00 | 93.0 | 87.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 5.99 | 16.02 | 26.78 | 6.00 | 96.0 | 78.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 12 | 7.6 | 5.38 | 14.94 | 23.84 | 6.00 | 92.4 | 71.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.6 | 5.34 | 14.07 | 22.57 | 2.00 | 98.3 | 90.0 |

## GW3

- Train rows: 134921
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.59
- Actual score: 65.00
- Transfer: Bernardo Veiga de Carvalho e Silva -> Antoine Semenyo (projected gain 3.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.18 | 11.73 | 18.97 | 2.00 | 100.6 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.92 | 8.38 | 13.71 | 2.00 | 76.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.85 | 14.87 | 24.53 | 6.00 | 73.4 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.55 | 13.93 | 22.66 | 1.00 | 98.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.52 | 12.92 | 21.10 | 2.00 | 100.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.43 | 10.29 | 17.02 | 2.00 | 75.7 | 87.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 2.59 | 8.70 | 13.87 | 1.00 | 80.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.5 | 3.68 | 11.89 | 18.44 | 2.00 | 83.4 | 84.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.11 | 9.01 | 14.37 | 1.00 | 62.4 | 90.0 |
| Bench 4 | Bench | Daniel Jebbison | FWD | 3 | 4.5 | 1.54 | 4.60 | 7.22 | 0.00 | 29.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 6.32 | 19.35 | 31.88 | 17.00 | 89.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.83 | 17.71 | 29.06 | 6.00 | 90.8 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.24 | 14.12 | 23.25 | 1.00 | 78.5 | 81.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 5.56 | 13.81 | 22.62 | 6.00 | 93.2 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 12 | 7.6 | 4.11 | 12.70 | 20.41 | 3.00 | 66.3 | 75.0 |

## GW4

- Train rows: 135569
- Bank: 1.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.32
- Actual score: 38.00
- Transfer: Daniel Jebbison -> João Pedro Junqueira de Jesus (projected gain 6.16, hit 0)
- Autosub: Joško Gvardiol replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.90 | 9.45 | 15.70 | 9.00 | 79.0 | 90.0 |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.90 | 8.45 | 13.85 | 7.00 | 77.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.81 | 14.59 | 23.71 | 1.00 | 80.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.34 | 11.46 | 18.87 | 2.00 | 78.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.46 | 10.92 | 18.23 | 5.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.0 | 3.18 | 9.87 | 16.74 | 1.00 | 66.4 | 45.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 3.47 | 9.42 | 14.77 | 6.00 | 80.5 | 73.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 6.45 | 15.89 | 24.01 | 0.00 | 108.9 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.6 | 4.44 | 11.49 | 17.85 | 2.00 | 73.5 | 84.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.66 | 8.06 | 13.21 | 8.00 | 62.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 8.17 | 24.17 | 38.86 | 2.00 | 124.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.0 | 4.75 | 15.47 | 26.03 | 7.00 | 67.3 | 85.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.81 | 13.14 | 20.98 | 1.00 | 89.5 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.56 | 12.20 | 20.25 | 2.00 | 72.7 | 79.0 |
| Bench 3 | Bench | Diogo Teixeira da Silva | MID | 12 | 7.6 | 3.04 | 10.44 | 17.34 | 1.00 | 53.2 | 59.0 |

## GW5

- Train rows: 136228
- Bank: 0.10 -> 2.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dwight McNeil
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.68
- Actual score: 62.00
- Transfer: Diogo Teixeira da Silva -> Dwight McNeil (projected gain 3.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.29 | 10.50 | 17.60 | 4.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.54 | 8.45 | 14.08 | 0.00 | 81.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.59 | 13.27 | 21.88 | 11.00 | 75.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.32 | 12.52 | 20.51 | 2.00 | 87.6 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.63 | 11.29 | 18.84 | 1.00 | 90.2 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 2.94 | 8.65 | 13.95 | 6.00 | 68.9 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 2.43 | 8.65 | 15.01 | 1.00 | 55.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.53 | 11.13 | 18.07 | 2.00 | 87.3 | 82.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.6 | 3.11 | 9.84 | 15.41 | 6.00 | 61.3 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 0.55 | 4.08 | 7.32 | 1.00 | 2.8 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.75 | 20.69 | 33.55 | 6.00 | 87.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.0 | 4.66 | 15.60 | 26.14 | 4.00 | 74.7 | 45.0 |
| Vice Captain | XI | Dwight McNeil | MID | 8 | 5.4 | 4.96 | 13.56 | 22.50 | 2.00 | 97.8 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.16 | 11.94 | 20.18 | 12.00 | 75.3 | 87.0 |
| Bench 2 | Bench | Antoine Semenyo | MID | 3 | 5.5 | 2.92 | 10.62 | 17.15 | 2.00 | 71.3 | 69.0 |

## GW6

- Train rows: 136889
- Bank: 2.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.96
- Actual score: 53.00
- Transfer: João Pedro Junqueira de Jesus -> Nicolas Jackson (projected gain 5.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.50 | 12.17 | 19.78 | 1.00 | 101.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.76 | 8.57 | 14.27 | 2.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.37 | 13.99 | 23.81 | 1.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.19 | 11.50 | 19.03 | 0.00 | 91.1 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 3.84 | 10.68 | 16.95 | 0.00 | 87.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.31 | 10.54 | 17.85 | 5.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 2.91 | 9.54 | 16.11 | 9.00 | 65.9 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 5.81 | 15.88 | 24.68 | 5.00 | 97.2 | 78.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 5.6 | 3.20 | 10.31 | 16.79 | 2.00 | 69.7 | 80.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.92 | 7.55 | 12.34 | 1.00 | 56.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.6 | 7.11 | 19.54 | 33.64 | 10.00 | 83.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.0 | 7.12 | 19.29 | 31.09 | 3.00 | 99.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.57 | 13.82 | 23.02 | 3.00 | 82.5 | 76.0 |
| XI | XI | Dwight McNeil | MID | 8 | 5.4 | 4.16 | 12.06 | 20.32 | 15.00 | 87.0 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 4.86 | 11.91 | 19.03 | 7.00 | 81.7 | 88.0 |

## GW7

- Train rows: 137553
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.56
- Actual score: 52.00
- Transfer: Jamie Vardy -> Liam Delap (projected gain 0.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.03 | 11.25 | 17.99 | 2.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.74 | 8.06 | 13.48 | 0.00 | 80.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.04 | 12.39 | 20.78 | 8.00 | 76.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.85 | 11.28 | 18.75 | 1.00 | 80.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.92 | 11.00 | 17.99 | 1.00 | 80.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.76 | 10.52 | 17.22 | 2.00 | 80.0 | 90.0 |
| Bench 4 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 2.92 | 9.21 | 14.97 | 1.00 | 81.2 | 45.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 4.03 | 13.28 | 20.24 | 2.00 | 60.3 | 80.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.6 | 3.41 | 10.20 | 16.53 | 8.00 | 65.6 | 90.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 3.66 | 9.98 | 15.91 | 6.00 | 81.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.40 | 19.45 | 32.80 | 3.00 | 79.9 | 72.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 6.00 | 17.17 | 27.83 | 16.00 | 71.1 | 90.0 |
| XI | XI | Dwight McNeil | MID | 8 | 5.5 | 4.79 | 14.36 | 23.34 | 2.00 | 95.3 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.36 | 13.37 | 21.71 | 10.00 | 72.7 | 84.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 4.00 | 10.45 | 16.87 | 2.00 | 64.4 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.54
- Actual score: 63.00
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 1.20, hit 0)
- Autosub: Liam Delap replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.77 | 11.08 | 18.04 | 1.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.69 | 8.02 | 13.35 | 2.00 | 80.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.43 | 13.31 | 22.19 | 2.00 | 86.4 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.16 | 11.52 | 18.83 | 2.00 | 86.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.11 | 11.17 | 18.07 | 10.00 | 83.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.45 | 10.19 | 16.86 | -3.00 | 83.6 | 29.0 |
| Bench 4 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 2.26 | 6.82 | 11.87 | 1.00 | 61.3 | 1.0 |
| Bench 3 | Bench | Nicolas Jackson | FWD | 6 | 7.8 | 2.98 | 11.22 | 18.20 | 6.00 | 53.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.6 | 3.85 | 11.11 | 17.93 | 9.00 | 78.9 | 80.0 |
| Bench 2 | Autosub In | Liam Delap | FWD | 10 | 5.6 | 3.44 | 9.52 | 15.50 | 2.00 | 77.4 | 78.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 10.0 | 6.52 | 19.34 | 32.20 | 0.00 | 86.6 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 5.86 | 18.41 | 30.78 | 12.00 | 76.1 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.86 | 13.43 | 22.03 | 4.00 | 80.6 | 45.0 |
| XI | XI | Dwight McNeil | MID | 8 | 5.5 | 4.44 | 12.93 | 20.56 | 6.00 | 82.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 3.59 | 10.65 | 17.06 | 6.00 | 75.9 | 82.0 |

## GW9

- Train rows: 138886
- Bank: 0.40 -> 2.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.72
- Actual score: 74.00
- Transfer: Bukayo Saka -> Bryan Mbeumo (projected gain 8.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.01 | 9.87 | 16.34 | 0.00 | 83.1 | 90.0 |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.18 | 8.48 | 13.91 | 6.00 | 81.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 5.68 | 14.20 | 22.39 | 9.00 | 103.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 3.93 | 12.60 | 20.88 | 1.00 | 81.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.98 | 11.59 | 18.83 | 2.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 1.88 | 5.75 | 10.43 | 2.00 | 43.7 | 83.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.0 | 1.08 | 5.24 | 9.99 | 0.00 | 36.4 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 4.22 | 12.55 | 20.61 | 9.00 | 74.5 | 77.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 4.18 | 10.95 | 18.09 | 7.00 | 70.4 | 72.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.93 | 8.70 | 14.39 | 5.00 | 65.7 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 6.52 | 19.96 | 32.79 | 10.00 | 98.1 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.6 | 6.31 | 17.54 | 27.46 | 15.00 | 104.0 | 90.0 |
| XI | XI | Dwight McNeil | MID | 8 | 5.6 | 4.27 | 12.37 | 20.01 | 2.00 | 84.0 | 85.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.70 | 11.70 | 19.56 | 2.00 | 59.9 | 61.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.22 | 11.54 | 18.29 | 1.00 | 83.1 | 56.0 |

## GW10

- Train rows: 139556
- Bank: 2.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.79
- Actual score: 50.00
- Transfer: Morgan Rogers -> Jarrod Bowen (projected gain 3.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.24 | 9.93 | 16.41 | 3.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.82 | 8.32 | 13.57 | 2.00 | 82.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.46 | 12.72 | 20.97 | 2.00 | 85.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.59 | 11.08 | 17.90 | 7.00 | 76.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.50 | 10.23 | 16.71 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 2.46 | 7.60 | 12.52 | 2.00 | 66.4 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.0 | 1.50 | 5.22 | 9.60 | 2.00 | 32.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 3.91 | 12.63 | 21.15 | 1.00 | 71.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.18 | 10.89 | 17.75 | 5.00 | 70.8 | 90.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.79 | 7.74 | 13.31 | 2.00 | 50.0 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 7.17 | 20.39 | 33.74 | 9.00 | 100.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 6.28 | 18.33 | 28.47 | 3.00 | 104.1 | 86.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.45 | 13.51 | 22.04 | 2.00 | 92.3 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.22 | 10.68 | 18.14 | 6.00 | 52.7 | 8.0 |
| XI | XI | Dwight McNeil | MID | 8 | 5.6 | 3.63 | 10.26 | 16.80 | 2.00 | 68.1 | 90.0 |

## GW11

- Train rows: 140230
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.00
- Actual score: 51.00
- Transfer: Dwight McNeil -> Antoine Semenyo (projected gain 1.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.11 | 9.29 | 15.29 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.81 | 8.50 | 13.98 | 1.00 | 83.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.50 | 12.98 | 21.29 | 1.00 | 92.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.11 | 11.92 | 19.53 | 1.00 | 82.0 | 24.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.04 | 10.81 | 17.58 | 4.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Noussair Mazraoui | DEF | 14 | 4.5 | 3.31 | 8.79 | 14.04 | 8.00 | 78.9 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 2.63 | 8.07 | 13.27 | 2.00 | 64.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.67 | 11.37 | 18.58 | 2.00 | 77.6 | 90.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 3.57 | 11.27 | 19.29 | 2.00 | 71.5 | 87.0 |
| Bench 4 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.15 | 7.62 | 12.76 | 11.00 | 52.9 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 7.58 | 21.88 | 35.38 | 14.00 | 110.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.09 | 15.85 | 25.35 | 5.00 | 91.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 3.93 | 12.08 | 19.36 | 3.00 | 81.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 4.18 | 11.36 | 18.16 | 2.00 | 84.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.64 | 10.27 | 17.48 | 1.00 | 45.7 | 6.0 |

## GW12

- Train rows: 140908
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Virgil van Dijk
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.47
- Actual score: 74.00
- Transfer: William Saliba -> Virgil van Dijk (projected gain 3.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.09 | 16.40 | 6.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.05 | 8.52 | 14.08 | 1.00 | 85.7 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 12.66 | 20.25 | 1.00 | 100.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.24 | 12.14 | 19.92 | 0.00 | 87.3 | 90.0 |
| XI | XI | Noussair Mazraoui | DEF | 14 | 4.5 | 3.92 | 10.41 | 16.29 | 2.00 | 89.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.16 | 9.71 | 16.26 | 14.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 12 | 6.9 | 1.97 | 6.91 | 13.10 | 0.00 | 34.1 | 0.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.8 | 4.59 | 12.56 | 20.53 | 12.00 | 80.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.88 | 11.85 | 18.76 | 2.00 | 79.9 | 85.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.96 | 9.09 | 14.84 | 2.00 | 61.5 | 80.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 8.11 | 22.21 | 36.23 | 13.00 | 114.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.22 | 14.58 | 23.92 | 3.00 | 86.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 3.74 | 11.95 | 19.55 | 7.00 | 82.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.27 | 9.49 | 15.22 | 1.00 | 68.0 | 90.0 |
| Bench 3 | Bench | James Maddison | MID | 18 | 7.5 | 2.10 | 7.88 | 13.90 | 16.00 | 33.1 | 88.0 |

## GW13

- Train rows: 141592
- Bank: 0.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.19
- Actual score: 60.00
- Transfer: Trent Alexander-Arnold -> Gabriel dos Santos Magalhães (projected gain 2.28, hit 0)
- Autosub: Noussair Mazraoui replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.72 | 17.27 | 2.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.24 | 7.51 | 12.73 | 0.00 | 85.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.90 | 13.32 | 21.36 | 2.00 | 103.4 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.1 | 3.38 | 11.35 | 19.03 | 0.00 | 83.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.22 | 18.02 | 6.00 | 84.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 3.99 | 11.11 | 17.71 | 9.00 | 89.0 | 45.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.5 | 3.05 | 8.89 | 14.09 | 1.00 | 77.7 | 55.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 7.9 | 4.96 | 14.03 | 22.48 | 6.00 | 84.6 | 70.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.70 | 10.31 | 16.79 | 2.00 | 70.2 | 78.0 |
| Bench 3 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.96 | 9.23 | 14.75 | 2.00 | 62.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 8.18 | 24.26 | 38.49 | 13.00 | 107.5 | 83.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.30 | 14.72 | 24.60 | 2.00 | 92.1 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 4.53 | 12.90 | 21.27 | 2.00 | 78.2 | 84.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 3.46 | 11.15 | 18.92 | 2.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 3 | 5.6 | 2.87 | 8.79 | 14.88 | 0.00 | 61.5 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 1.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Nicolas Jackson
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.63
- Actual score: 61.00
- Transfer: Antoine Semenyo -> Brennan Johnson (projected gain 2.35, hit 0)
- Autosub: Joško Gvardiol replaced Gabriel dos Santos Magalhães.
- Autosub: Noussair Mazraoui replaced Nicolas Jackson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.99 | 16.25 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.30 | 4.67 | 8.46 | 0.00 | 49.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.29 | 12.68 | 20.52 | 1.00 | 97.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.06 | 11.75 | 18.85 | 1.00 | 87.9 | 28.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 3.72 | 10.67 | 17.20 | 0.00 | 76.5 | 0.0 |
| Bench 3 | Autosub In | Joško Gvardiol | DEF | 13 | 6.1 | 2.28 | 7.97 | 14.04 | 6.00 | 45.4 | 90.0 |
| Bench 4 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.6 | 2.18 | 7.33 | 12.40 | 1.00 | 65.0 | 90.0 |
| Vice Captain | Bench | Nicolas Jackson | FWD | 6 | 7.9 | 6.14 | 16.48 | 25.45 | 0.00 | 96.8 | 0.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.44 | 9.63 | 15.42 | 2.00 | 70.6 | 78.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 5 | 5.7 | 3.01 | 9.48 | 15.74 | 0.00 | 66.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 8.06 | 24.30 | 39.01 | 18.00 | 114.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.44 | 12.04 | 20.18 | 2.00 | 87.3 | 90.0 |
| XI | XI | Brennan Johnson | MID | 18 | 6.7 | 3.97 | 11.74 | 19.20 | 2.00 | 71.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.36 | 11.09 | 19.90 | 2.00 | 66.9 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.51 | 10.85 | 17.77 | 2.00 | 64.6 | 79.0 |

## GW15

- Train rows: 142975
- Bank: -0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Matheus Santos Carneiro Da Cunha
- Chip used: none
- Predicted score: 49.74
- Actual score: 44.00
- Transfer: Nicolas Jackson -> Matheus Santos Carneiro Da Cunha (projected gain 5.09, hit 0)
- Autosub: Noussair Mazraoui replaced Virgil van Dijk.
- Autosub: Danny Welbeck replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.92 | 17.63 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.4 | 0.97 | 3.72 | 7.05 | 0.00 | 34.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.98 | 11.32 | 19.05 | 1.00 | 80.6 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.86 | 9.88 | 16.74 | 0.00 | 66.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.94 | 9.34 | 15.99 | 3.00 | 67.9 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.6 | 2.82 | 8.15 | 13.10 | 1.00 | 74.3 | 24.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 2.18 | 7.30 | 12.47 | 0.00 | 40.6 | 0.0 |
| Vice Captain | Captain | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.58 | 13.21 | 21.32 | 1.00 | 80.1 | 90.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 2.83 | 8.01 | 13.07 | 1.00 | 58.5 | 80.0 |
| Bench 4 | Autosub In | Danny Welbeck | FWD | 5 | 5.7 | 1.84 | 5.65 | 10.44 | 1.00 | 30.7 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 12.8 | 7.38 | 23.33 | 38.89 | 0.00 | 91.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.28 | 12.41 | 20.04 | 12.00 | 83.2 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.51 | 10.47 | 17.83 | 4.00 | 72.7 | 11.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.15 | 10.38 | 18.72 | 13.00 | 67.6 | 90.0 |
| XI | XI | Brennan Johnson | MID | 18 | 6.7 | 3.08 | 10.31 | 17.03 | 4.00 | 70.1 | 52.0 |

## GW16

- Train rows: 143668
- Bank: 0.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: William Saliba
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.73
- Actual score: 71.00
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 4.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 10.66 | 17.07 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.4 | 0.96 | 2.99 | 5.83 | 1.00 | 21.8 | 90.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.2 | 4.51 | 12.76 | 19.68 | 6.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.18 | 11.65 | 19.31 | 6.00 | 87.4 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.16 | 9.62 | 16.15 | 7.00 | 64.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.93 | 8.44 | 14.28 | 1.00 | 57.7 | 90.0 |
| Bench 4 | Bench | Noussair Mazraoui | DEF | 14 | 4.6 | 1.74 | 6.01 | 10.32 | 2.00 | 46.4 | 77.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.16 | 12.40 | 20.22 | 9.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.65 | 8.07 | 13.36 | 1.00 | 56.1 | 83.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.6 | 1.93 | 6.14 | 11.03 | 0.00 | 35.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 7.26 | 21.85 | 36.96 | 5.00 | 91.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.81 | 12.33 | 21.37 | 9.00 | 81.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.07 | 12.01 | 20.06 | 2.00 | 84.1 | 90.0 |
| XI | XI | Brennan Johnson | MID | 18 | 6.7 | 3.46 | 10.09 | 17.30 | 0.00 | 65.7 | 45.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.18 | 9.07 | 15.63 | 15.00 | 43.9 | 76.0 |

## GW17

- Train rows: 144369
- Bank: 0.90 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antonee Robinson
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.02
- Actual score: 76.00
- Transfer: Noussair Mazraoui -> Antonee Robinson (projected gain 5.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.70 | 10.68 | 17.22 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.4 | 1.71 | 5.52 | 9.45 | 0.00 | 54.1 | 0.0 |
| Vice Captain | XI | Antonee Robinson | DEF | 9 | 4.8 | 5.34 | 13.32 | 21.06 | 6.00 | 112.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.93 | 11.52 | 18.37 | 2.00 | 80.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.62 | 10.89 | 18.19 | 0.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.91 | 9.80 | 16.57 | -1.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.00 | 9.09 | 15.08 | 1.00 | 69.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.36 | 12.24 | 20.54 | 9.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.69 | 8.09 | 13.29 | 0.00 | 58.3 | 0.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.6 | 0.84 | 3.33 | 6.74 | 0.00 | 13.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 6.87 | 22.53 | 37.45 | 21.00 | 93.7 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.75 | 14.09 | 23.52 | 2.00 | 92.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.33 | 12.96 | 21.14 | 6.00 | 81.8 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.5 | 3.36 | 11.29 | 18.84 | 6.00 | 61.9 | 57.0 |
| Bench 3 | Bench | Brennan Johnson | MID | 18 | 6.6 | 2.07 | 8.07 | 13.81 | 4.00 | 51.1 | 32.0 |

## GW18

- Train rows: 145070
- Bank: 0.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.32
- Actual score: 61.00
- Transfer: Brennan Johnson -> Morgan Rogers (projected gain 2.62, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.09 | 11.19 | 17.99 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.4 | 1.01 | 3.11 | 5.56 | 0.00 | 24.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.57 | 12.86 | 20.66 | 7.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 9 | 4.8 | 2.93 | 9.57 | 15.28 | 1.00 | 76.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.97 | 9.54 | 16.01 | 1.00 | 78.3 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.14 | 9.51 | 15.63 | 2.00 | 78.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.47 | 9.42 | 15.47 | 2.00 | 68.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.30 | 12.51 | 21.16 | 12.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Liam Delap | FWD | 10 | 5.6 | 1.36 | 5.10 | 8.86 | 2.00 | 34.9 | 79.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 0.53 | 2.51 | 5.33 | 0.00 | 9.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 9.57 | 25.60 | 42.19 | 9.00 | 109.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.87 | 14.28 | 23.66 | 3.00 | 89.7 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 7.6 | 3.93 | 12.20 | 20.18 | 0.00 | 75.9 | 26.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 4.19 | 12.10 | 19.77 | 2.00 | 88.7 | 68.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.64 | 12.07 | 20.22 | 8.00 | 78.1 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 1.70 -> 2.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.48
- Actual score: 78.00
- Transfer: James Maddison -> Anthony Gordon (projected gain 4.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 11.05 | 17.89 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.08 | 3.04 | 5.11 | 0.00 | 22.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.17 | 12.54 | 20.79 | 2.00 | 85.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.01 | 11.64 | 18.72 | 4.00 | 93.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.66 | 10.09 | 16.33 | 6.00 | 75.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.49 | 9.89 | 15.96 | 6.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.5 | 2.43 | 7.82 | 13.68 | 4.00 | 50.4 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.39 | 15.22 | 25.17 | 1.00 | 95.3 | 45.0 |
| Bench 2 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.49 | 7.46 | 12.20 | 11.00 | 58.9 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 0.40 | 2.31 | 4.60 | 0.00 | 11.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.74 | 25.37 | 41.18 | 16.00 | 113.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.20 | 14.46 | 23.14 | 6.00 | 83.8 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.01 | 13.40 | 21.97 | 7.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.4 | 4.26 | 12.93 | 20.90 | 1.00 | 76.1 | 59.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 4.00 | 11.36 | 18.10 | 11.00 | 77.1 | 90.0 |

## GW20

- Train rows: 146484
- Bank: 2.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.09
- Actual score: 63.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Ollie Watkins (projected gain 5.82, hit 0)
- Autosub: Pedro Porro replaced Morgan Rogers.
- Autosub: Liam Delap replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.67 | 10.73 | 17.43 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 0.75 | 2.11 | 3.73 | 0.00 | 12.8 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.77 | 12.74 | 20.26 | 1.00 | 98.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.97 | 12.07 | 20.02 | 2.00 | 85.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 10.54 | 16.78 | 2.00 | 81.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.79 | 10.43 | 16.76 | 1.00 | 79.4 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.5 | 3.00 | 9.35 | 15.82 | 4.00 | 73.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 5.47 | 14.11 | 22.61 | 2.00 | 79.1 | 90.0 |
| Bench 3 | Autosub In | Liam Delap | FWD | 10 | 5.6 | 2.80 | 8.42 | 13.94 | 8.00 | 64.6 | 87.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 0.35 | 2.18 | 4.11 | 0.00 | 10.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 10.27 | 27.83 | 45.19 | 7.00 | 114.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.6 | 5.72 | 15.58 | 25.09 | 19.00 | 100.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.25 | 14.65 | 22.97 | 7.00 | 82.5 | 77.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.4 | 4.03 | 10.87 | 17.92 | 0.00 | 66.9 | 0.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.4 | 3.08 | 10.14 | 17.19 | 0.00 | 61.4 | 0.0 |

## GW21

- Train rows: 147195
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Anthony Gordon
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.82
- Actual score: 39.00
- Transfer: Liam Delap -> Raúl Jiménez (projected gain 3.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 10.65 | 17.32 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 0.46 | 1.74 | 3.15 | 0.00 | 10.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.09 | 11.45 | 18.89 | 2.00 | 86.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.92 | 11.36 | 18.29 | 7.00 | 82.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.46 | 10.10 | 16.42 | 1.00 | 80.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.33 | 10.00 | 16.29 | 2.00 | 79.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 3.12 | 9.93 | 16.49 | 1.00 | 79.5 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.62 | 12.22 | 18.38 | 1.00 | 75.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 3.77 | 11.67 | 18.82 | 8.00 | 61.2 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 0.75 | 2.21 | 4.01 | 1.00 | 10.9 | 12.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.26 | 26.06 | 42.65 | 2.00 | 110.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.06 | 25.94 | 2.00 | 98.1 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.4 | 5.75 | 16.01 | 25.13 | 9.00 | 91.1 | 77.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.4 | 2.43 | 7.96 | 13.41 | 6.00 | 46.4 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | 19 | 7.4 | 2.31 | 7.51 | 12.89 | 0.00 | 36.8 | 0.0 |

## GW22

- Train rows: 147919
- Bank: -0.00 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.97
- Actual score: 44.00
- Transfer: Jarrod Bowen -> Amad Diallo (projected gain 3.95, hit 0)
- Autosub: Pedro Porro replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.55 | 10.21 | 16.85 | 1.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 0.67 | 1.94 | 3.51 | 7.00 | 9.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.51 | 12.05 | 19.50 | 8.00 | 91.6 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.2 | 3.81 | 11.07 | 18.34 | 0.00 | 86.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.70 | 10.25 | 17.11 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.4 | 3.55 | 10.24 | 16.74 | 1.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.60 | 10.15 | 16.59 | 6.00 | 79.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 3.77 | 11.92 | 19.95 | 8.00 | 70.4 | 79.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.07 | 10.19 | 16.33 | 2.00 | 57.9 | 70.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 0.96 | 3.13 | 5.37 | 2.00 | 16.1 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 9.03 | 26.47 | 43.21 | 3.00 | 106.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.99 | 15.07 | 25.20 | 2.00 | 89.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.98 | 14.86 | 23.25 | 2.00 | 76.7 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.93 | 14.04 | 22.24 | 2.00 | 97.5 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | 2 | 5.4 | 2.84 | 9.79 | 16.23 | 1.00 | 70.6 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 1.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.14
- Actual score: 61.00
- Transfer: William Saliba -> Trent Alexander-Arnold (projected gain 6.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.40 | 9.85 | 16.28 | 9.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.90 | 5.28 | 8.40 | 8.00 | 44.1 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.07 | 16.38 | 25.79 | 5.00 | 100.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.31 | 11.54 | 18.38 | 2.00 | 82.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.16 | 11.47 | 18.71 | 2.00 | 84.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.73 | 10.00 | 16.42 | 6.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.36 | 9.85 | 16.48 | 8.00 | 78.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 4.96 | 13.18 | 21.68 | 5.00 | 71.1 | 65.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.7 | 3.35 | 9.12 | 15.08 | 2.00 | 49.5 | 63.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 1.85 | 5.00 | 7.97 | 2.00 | 35.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 9.29 | 25.89 | 41.96 | 8.00 | 104.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.42 | 16.00 | 26.55 | 7.00 | 100.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.76 | 23.67 | 5.00 | 77.9 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.19 | 12.31 | 20.17 | 3.00 | 81.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 3.81 | 10.14 | 16.41 | 1.00 | 75.0 | 71.0 |

## GW24

- Train rows: 149404
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.63
- Actual score: 86.00
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 3.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.73 | 8.80 | 14.93 | 3.00 | 77.1 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.74 | 5.82 | 9.61 | 0.00 | 56.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.43 | 16.84 | 26.21 | 7.00 | 119.8 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.94 | 12.22 | 19.25 | 6.00 | 106.3 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.34 | 10.61 | 17.59 | 4.00 | 82.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.34 | 10.47 | 17.35 | 0.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.4 | 3.13 | 9.63 | 16.05 | 6.00 | 76.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 4.07 | 12.12 | 20.29 | 1.00 | 57.9 | 45.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 1.60 | 7.09 | 12.30 | 8.00 | 30.8 | 72.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 1.98 | 5.86 | 9.09 | 1.00 | 49.0 | 72.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 9.48 | 26.31 | 42.77 | 29.00 | 130.3 | 177.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 6.14 | 16.76 | 27.28 | 2.00 | 93.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.41 | 13.33 | 21.06 | 2.00 | 95.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.16 | 12.74 | 21.49 | 1.00 | 71.4 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.08 | 12.20 | 19.92 | 2.00 | 85.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.40 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 83.73
- Actual score: 123.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.04) beats the best remaining Triple Captain opportunity (13.04).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Anthony Gordon -> Morgan Rogers (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (15.04) beats the best remaining Triple Captain opportunity (13.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.97 | 16.44 | 7.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.01 | 3.43 | 5.97 | 11.00 | 27.6 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 6.30 | 16.32 | 26.46 | 13.00 | 116.0 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 6.29 | 15.63 | 24.33 | 2.00 | 146.8 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.69 | 11.09 | 18.18 | 2.00 | 86.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.46 | 10.41 | 16.78 | 6.00 | 80.3 | 86.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.43 | 9.93 | 16.49 | 6.00 | 81.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 5.73 | 14.44 | 22.98 | 15.00 | 98.7 | 180.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 2.67 | 8.98 | 14.95 | 5.00 | 47.0 | 75.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 5 | 5.5 | 2.17 | 5.76 | 8.99 | 8.00 | 49.6 | 83.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 11.31 | 29.85 | 48.87 | 20.00 | 172.9 | 180.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.54 | 15.54 | 25.50 | 3.00 | 82.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 6.17 | 15.48 | 23.99 | 5.00 | 89.9 | 76.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 5.61 | 13.38 | 20.12 | 4.00 | 119.5 | 180.0 |
| Bench 2 | Bench | Amad Diallo | MID | 14 | 5.5 | 3.26 | 10.56 | 17.80 | 0.00 | 64.4 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 2.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.27
- Actual score: 69.00
- Transfer: Danny Welbeck -> Chris Wood (projected gain 5.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.50 | 17.16 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.84 | 6.16 | 10.16 | 1.00 | 56.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 5.75 | 17.45 | 28.32 | 6.00 | 109.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.68 | 14.14 | 22.62 | 6.00 | 127.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.19 | 11.24 | 18.48 | 1.00 | 88.8 | 25.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.70 | 11.17 | 17.91 | 1.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.45 | 10.71 | 17.19 | 1.00 | 81.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 5.43 | 16.16 | 25.64 | 2.00 | 100.4 | 76.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 5.29 | 15.71 | 25.43 | 5.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 3.29 | 9.77 | 15.82 | 2.00 | 55.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 10.29 | 30.47 | 49.65 | 14.00 | 162.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 6.35 | 17.12 | 26.71 | 14.00 | 95.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.51 | 13.20 | 20.58 | 2.00 | 68.4 | 72.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.99 | 11.48 | 17.67 | 2.00 | 82.8 | 77.0 |
| Bench 4 | Bench | Amad Diallo | MID | 14 | 5.5 | 0.26 | 4.26 | 9.17 | 0.00 | 7.9 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.79
- Actual score: 61.00
- Transfer: Amad Diallo -> Marco Asensio (projected gain 3.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.23 | 9.78 | 16.02 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.89 | 6.11 | 10.06 | 11.00 | 57.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.3 | 5.92 | 16.61 | 27.32 | 6.00 | 100.3 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.36 | 12.76 | 20.79 | 7.00 | 108.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.37 | 10.40 | 17.03 | 7.00 | 78.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 3.39 | 10.13 | 16.47 | 0.00 | 83.8 | 18.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.4 | 2.70 | 8.66 | 14.70 | 2.00 | 62.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.81 | 15.34 | 26.03 | 2.00 | 94.0 | 84.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 4.32 | 13.54 | 22.62 | 5.00 | 81.7 | 67.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 3.20 | 9.21 | 15.54 | 1.00 | 64.2 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 10.70 | 30.06 | 49.22 | 6.00 | 142.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.13 | 17.98 | 28.39 | 5.00 | 95.4 | 90.0 |
| XI | XI | Marco Asensio | MID | 2 | 6.0 | 4.01 | 12.81 | 21.26 | 1.00 | 87.5 | 22.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.88 | 18.84 | 10.00 | 62.1 | 90.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.52 | 7.77 | 13.74 | 7.00 | 57.7 | 90.0 |

## GW28

- Train rows: 152512
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.19
- Actual score: 69.00
- Transfer: Marco Asensio -> Ismaïla Sarr (projected gain 1.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.89 | 17.64 | 3.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.48 | 7.69 | 12.64 | 3.00 | 71.5 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 6.33 | 16.56 | 26.74 | 2.00 | 97.3 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.83 | 13.02 | 21.08 | 2.00 | 102.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.78 | 11.05 | 18.09 | 2.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.58 | 10.67 | 17.59 | 1.00 | 81.4 | 86.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 9 | 4.9 | 2.45 | 7.72 | 13.30 | 0.00 | 57.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.1 | 4.94 | 15.29 | 25.53 | 2.00 | 91.8 | 86.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 4.45 | 13.19 | 22.15 | 9.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 2.58 | 7.54 | 13.09 | 8.00 | 43.4 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 10.66 | 29.04 | 47.45 | 15.00 | 127.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.08 | 17.53 | 28.20 | 2.00 | 90.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.66 | 13.93 | 22.67 | 5.00 | 86.8 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.5 | 4.49 | 11.18 | 18.01 | 11.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 3.55 | 9.88 | 16.66 | 3.00 | 83.2 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 63.28
- Actual score: 22.00
- Transfer: Antonee Robinson -> Ola Aina (projected gain 4.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.54 | 17.22 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.80 | 8.11 | 13.25 | 0.00 | 78.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 5.30 | 13.73 | 21.36 | 1.00 | 111.1 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.01 | 13.55 | 23.12 | 0.00 | 70.2 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.95 | 12.97 | 20.08 | 1.00 | 105.8 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.56 | 17.24 | 0.00 | 83.6 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 2.90 | 10.26 | 17.80 | 0.00 | 74.8 | 0.0 |
| Vice Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.85 | 19.00 | 29.90 | 2.00 | 109.3 | 79.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.9 | 3.63 | 12.31 | 21.12 | 0.00 | 59.3 | 0.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.5 | 3.11 | 9.49 | 15.17 | 2.00 | 56.7 | 62.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.1 | 8.15 | 26.62 | 45.14 | 0.00 | 101.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 5.92 | 17.03 | 27.47 | 6.00 | 101.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 6.03 | 16.73 | 26.20 | 2.00 | 108.2 | 78.0 |
| Bench 2 | Bench | Ismaïla Sarr | MID | 7 | 5.5 | 2.96 | 9.87 | 16.87 | 0.00 | 51.2 | 0.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.75 | 9.51 | 16.27 | 0.00 | 64.3 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ismaïla Sarr
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.53
- Actual score: 36.00
- Transfer: Trent Alexander-Arnold -> Gabriel dos Santos Magalhães (projected gain 5.14, hit 0)
- Autosub: Raúl Jiménez replaced Justin Kluivert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.58 | 12.73 | 20.11 | 2.00 | 107.1 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.01 | 5.69 | 9.81 | 6.00 | 42.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 4.34 | 12.51 | 20.20 | 1.00 | 95.6 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 11.20 | 17.85 | 6.00 | 82.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.08 | 9.17 | 14.81 | 1.00 | 73.7 | 39.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.71 | 8.49 | 14.87 | 8.00 | 59.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.17 | 7.01 | 12.10 | 0.00 | 50.8 | 2.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.56 | 9.75 | 17.18 | 0.00 | 42.6 | 25.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.1 | 2.09 | 8.14 | 14.76 | 0.00 | 30.5 | 0.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | 9 | 5.5 | 2.09 | 7.58 | 12.65 | 2.00 | 47.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.47 | 23.09 | 39.29 | 3.00 | 86.3 | 90.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 6.0 | 4.62 | 13.48 | 22.12 | 0.00 | 70.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 4.38 | 13.35 | 22.55 | 8.00 | 76.4 | 90.0 |
| Vice Captain | XI | Ismaïla Sarr | MID | 7 | 5.6 | 5.11 | 12.07 | 19.30 | 2.00 | 66.1 | 90.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.5 | 1.48 | 5.99 | 10.82 | 10.00 | 40.2 | 87.0 |

## GW31

- Train rows: 154881
- Bank: 0.90 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.63
- Actual score: 36.00
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 7.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.60 | 18.36 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.56 | 7.76 | 12.61 | 6.00 | 69.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.84 | 13.42 | 21.26 | 2.00 | 105.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.16 | 12.15 | 19.05 | 9.00 | 91.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.94 | 11.61 | 19.07 | 1.00 | 89.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.73 | 7.44 | 12.54 | 1.00 | 46.3 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.3 | 1.57 | 6.19 | 11.17 | 0.00 | 48.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 3.18 | 10.29 | 17.70 | 2.00 | 50.1 | 61.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.4 | 2.41 | 7.66 | 12.76 | 1.00 | 58.6 | 14.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.54 | 6.11 | 12.46 | 0.00 | 19.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.40 | 24.68 | 40.64 | 2.00 | 108.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.8 | 4.90 | 14.80 | 24.56 | 3.00 | 89.1 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.6 | 3.27 | 10.71 | 16.82 | 2.00 | 55.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 3.46 | 10.29 | 16.65 | 9.00 | 80.0 | 90.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.0 | 0.72 | 5.20 | 10.36 | 0.00 | 6.8 | 0.0 |

## GW32

- Train rows: 155673
- Bank: 0.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jacob Murphy
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.51
- Actual score: 68.00
- Transfer: Justin Kluivert -> Jacob Murphy (projected gain 7.65, hit 0)
- Autosub: Raúl Jiménez replaced Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.93 | 11.34 | 18.23 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.80 | 8.24 | 13.48 | 4.00 | 73.7 | 70.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.23 | 12.37 | 19.87 | 1.00 | 97.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 3.93 | 11.65 | 18.37 | 2.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.76 | 11.06 | 18.18 | 9.00 | 83.6 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.83 | 8.60 | 14.25 | 0.00 | 65.0 | 0.0 |
| Bench 4 | Bench | Ola Aina | DEF | 16 | 5.2 | 0.66 | 3.50 | 7.35 | 0.00 | 21.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 3.91 | 10.98 | 18.50 | 7.00 | 59.5 | 24.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | 9 | 5.4 | 2.16 | 6.64 | 11.50 | 1.00 | 40.4 | 33.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.0 | 1.46 | 5.65 | 11.04 | 2.00 | 16.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.16 | 24.40 | 40.51 | 6.00 | 108.3 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 4.36 | 14.13 | 23.74 | 2.00 | 88.9 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 6.16 | 13.84 | 20.64 | 19.00 | 114.2 | 138.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.93 | 12.65 | 20.20 | 6.00 | 89.1 | 84.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.6 | 4.16 | 12.00 | 19.07 | 7.00 | 89.2 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 1.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 79.58
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.90) beats the best remaining Bench Boost opportunity (8.06).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 10.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.90) beats the best remaining Bench Boost opportunity (8.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 5.77 | 13.72 | 21.23 | 7.00 | 128.8 | 180.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.3 | 4.09 | 9.67 | 15.36 | 0.00 | 98.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 6.41 | 15.25 | 23.37 | 7.00 | 130.9 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 6.08 | 14.81 | 22.93 | 7.00 | 130.3 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.48 | 12.21 | 19.94 | 7.00 | 92.7 | 90.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 1.54 | 5.10 | 9.01 | 5.00 | 33.0 | 90.0 |
| Bench 4 | Bench Boost | Ola Aina | DEF | 16 | 5.2 | 0.63 | 2.94 | 6.36 | 0.00 | 18.5 | 0.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.7 | 7.56 | 17.99 | 27.83 | 4.00 | 127.9 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 5.02 | 13.04 | 21.00 | 12.00 | 86.9 | 96.0 |
| Bench 2 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.3 | 2.04 | 6.65 | 11.27 | 2.00 | 43.6 | 83.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.20 | 23.28 | 38.67 | 3.00 | 105.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.05 | 14.85 | 22.85 | 7.00 | 124.8 | 166.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.6 | 5.46 | 13.95 | 21.79 | 3.00 | 129.8 | 117.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.59 | 13.58 | 22.69 | 18.00 | 81.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.47 | 11.06 | 18.35 | 2.00 | 71.9 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.66
- Actual score: 34.00
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 7.76, hit 0)
- Autosub: Ola Aina replaced William Saliba.
- Autosub: Raúl Jiménez replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 4.01 | 12.66 | 20.48 | 0.00 | 101.2 | 0.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 0.79 | 4.11 | 8.10 | 0.00 | 20.9 | 0.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.5 | 4.47 | 14.10 | 22.65 | 0.00 | 102.1 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.1 | 4.08 | 13.21 | 21.71 | 0.00 | 100.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.86 | 13.02 | 20.72 | 2.00 | 94.2 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.61 | 8.06 | 13.31 | 0.00 | 65.1 | 0.0 |
| Bench 4 | Autosub In | Ola Aina | DEF | 16 | 5.2 | 0.87 | 2.97 | 6.08 | 1.00 | 18.0 | 74.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.6 | 7.60 | 19.59 | 31.14 | 6.00 | 104.9 | 76.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.7 | 4.98 | 15.75 | 25.22 | 0.00 | 84.6 | 0.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | 9 | 5.3 | 3.40 | 8.74 | 13.74 | 1.00 | 66.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 8.55 | 23.11 | 37.30 | 8.00 | 113.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 7.47 | 20.70 | 32.76 | 2.00 | 130.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.30 | 13.59 | 22.25 | 6.00 | 81.1 | 66.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.6 | 4.12 | 13.09 | 21.26 | 0.00 | 81.6 | 0.0 |
| XI | Bench | Ismaïla Sarr | MID | 7 | 5.6 | 3.67 | 11.56 | 19.28 | 0.00 | 83.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.41
- Actual score: 42.00
- Transfer: Ismaïla Sarr -> Sandro Tonali (projected gain 4.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.44 | 7.49 | 13.15 | 1.00 | 57.4 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 1.30 | 4.35 | 7.95 | 6.00 | 29.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.22 | 10.36 | 17.56 | 6.00 | 79.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.03 | 9.24 | 16.05 | 8.00 | 67.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 2.86 | 8.76 | 15.44 | 1.00 | 59.4 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 2.05 | 6.34 | 10.57 | 1.00 | 50.7 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.3 | 1.82 | 5.24 | 9.22 | 0.00 | 31.3 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.6 | 6.42 | 17.61 | 28.25 | 9.00 | 83.0 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 2.73 | 9.51 | 16.95 | 2.00 | 38.6 | 82.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.3 | 2.02 | 6.50 | 10.77 | 2.00 | 48.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.52 | 22.32 | 36.64 | 2.00 | 105.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 6.15 | 17.65 | 28.26 | 5.00 | 95.1 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.11 | 11.84 | 19.77 | 1.00 | 60.4 | 55.0 |
| XI | XI | Sandro Tonali | MID | 15 | 5.5 | 3.67 | 10.25 | 16.77 | 2.00 | 82.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.72 | 8.57 | 15.10 | 3.00 | 46.3 | 90.0 |

## GW36

- Train rows: 158871
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.23
- Actual score: 41.00
- Transfer: Pedro Porro -> Rayan Aït-Nouri (projected gain 3.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.06 | 9.55 | 15.87 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.64 | 7.15 | 11.57 | 6.00 | 54.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 5.06 | 13.39 | 21.09 | 6.00 | 98.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.70 | 11.39 | 18.87 | 1.00 | 87.5 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.1 | 4.32 | 11.35 | 18.49 | 1.00 | 80.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 3.29 | 10.54 | 17.65 | 1.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.2 | 3.03 | 7.64 | 12.25 | 0.00 | 65.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.6 | 5.59 | 16.83 | 28.09 | 2.00 | 83.6 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.39 | 12.08 | 19.76 | 1.00 | 65.6 | 6.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | 9 | 5.3 | 2.95 | 8.05 | 12.84 | 9.00 | 63.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.00 | 21.13 | 35.17 | 2.00 | 99.1 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.91 | 18.55 | 29.08 | 6.00 | 101.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 3.73 | 11.72 | 19.18 | 6.00 | 74.2 | 88.0 |
| Bench 4 | Bench | Jacob Murphy | MID | 15 | 5.2 | 2.62 | 9.69 | 16.80 | 5.00 | 49.5 | 90.0 |
| XI | XI | Sandro Tonali | MID | 15 | 5.5 | 3.18 | 9.49 | 15.70 | 11.00 | 77.6 | 90.0 |

## GW37

- Train rows: 159672
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.50
- Actual score: 48.00
- Transfer: Omar Marmoush -> Yoane Wissa (projected gain 2.22, hit 0)
- Autosub: Sandro Tonali replaced Virgil van Dijk.
- Autosub: Raúl Jiménez replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.97 | 9.10 | 15.18 | 7.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.66 | 7.69 | 12.17 | 1.00 | 61.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 12.06 | 19.33 | 2.00 | 79.5 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.5 | 3.82 | 11.33 | 18.64 | 0.00 | 89.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 3.31 | 10.30 | 17.45 | 1.00 | 81.6 | 45.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.1 | 3.63 | 9.64 | 16.07 | 0.00 | 73.4 | 90.0 |
| Bench 4 | Bench | Ola Aina | DEF | 16 | 5.2 | 2.68 | 7.38 | 11.59 | 2.00 | 68.3 | 90.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.34 | 16.66 | 27.65 | 0.00 | 78.6 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.8 | 4.21 | 12.49 | 19.71 | 10.00 | 73.7 | 90.0 |
| Bench 3 | Autosub In | Raúl Jiménez | FWD | 9 | 5.3 | 2.85 | 8.01 | 13.12 | 9.00 | 66.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.18 | 20.94 | 34.98 | 2.00 | 102.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.65 | 16.79 | 26.91 | 5.00 | 91.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.69 | 12.65 | 19.97 | 6.00 | 79.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.53 | 11.42 | 18.78 | 2.00 | 69.5 | 62.0 |
| Bench 2 | Autosub In | Sandro Tonali | MID | 15 | 5.5 | 3.25 | 10.37 | 17.00 | 2.00 | 76.7 | 90.0 |

## GW38

- Train rows: 160473
- Bank: 1.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.58
- Actual score: 54.00
- Transfer: Ola Aina -> Milos Kerkez (projected gain 3.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.47 | 11.77 | 18.77 | 2.00 | 101.4 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.3 | 2.99 | 8.39 | 13.28 | 7.00 | 72.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.63 | 13.19 | 21.27 | 8.00 | 93.5 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.3 | 4.29 | 11.21 | 17.62 | 6.00 | 91.6 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.1 | 3.36 | 9.71 | 15.77 | 2.00 | 76.0 | 64.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.5 | 2.79 | 8.23 | 14.23 | 1.00 | 56.2 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.4 | 2.55 | 8.04 | 14.09 | 0.00 | 61.4 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.8 | 4.88 | 14.87 | 23.54 | 1.00 | 86.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.4 | 2.88 | 10.41 | 19.09 | 2.00 | 29.6 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.3 | 2.46 | 7.83 | 13.18 | 2.00 | 69.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.84 | 20.91 | 34.85 | 10.00 | 109.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.66 | 17.58 | 28.40 | 8.00 | 96.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.7 | 4.55 | 13.44 | 21.41 | 1.00 | 85.0 | 83.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.60 | 10.70 | 17.60 | 2.00 | 67.9 | 69.0 |
| XI | XI | Sandro Tonali | MID | 15 | 5.5 | 3.58 | 10.58 | 17.59 | 2.00 | 82.6 | 90.0 |