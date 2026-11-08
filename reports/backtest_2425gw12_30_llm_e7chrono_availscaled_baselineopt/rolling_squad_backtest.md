# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1208.26
- Total actual points: 1214.00
- Average predicted points: 63.59
- Average actual points: 63.89
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.47
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.43 | 9.97 | 16.10 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.7 | 3.33 | 9.13 | 14.81 | 1.00 | 86.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 4.50 | 12.71 | 20.23 | 0.00 | 88.3 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.0 | 4.20 | 11.81 | 19.41 | 0.00 | 71.7 | 0.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.5 | 3.75 | 11.13 | 17.92 | 14.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 3.63 | 10.81 | 17.19 | 2.00 | 87.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.95 | 10.73 | 16.89 | 0.00 | 88.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.8 | 4.38 | 11.98 | 19.12 | 2.00 | 76.1 | 70.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.9 | 3.90 | 11.57 | 18.18 | 2.00 | 76.2 | 85.0 |
| Bench 4 | Bench | Cameron Archer | FWD | -1 | 5.0 | 2.35 | 7.41 | 11.41 | 1.00 | 59.6 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.59 | 18.76 | 29.86 | 13.00 | 89.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.0 | 5.94 | 16.83 | 27.44 | 2.00 | 88.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.14 | 15.50 | 24.79 | 3.00 | 92.1 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.7 | 4.69 | 13.12 | 21.14 | 1.00 | 72.7 | 28.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 4.17 | 11.72 | 18.89 | 2.00 | 73.5 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.36
- Actual score: 66.00
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 1.08, hit 0)
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.84 | 10.71 | 16.96 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.7 | 2.91 | 8.36 | 13.48 | 7.00 | 83.4 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 4.16 | 12.97 | 20.91 | 0.00 | 91.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.30 | 12.14 | 19.55 | 2.00 | 92.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.75 | 11.33 | 18.18 | 6.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | -1 | 4.7 | 3.62 | 10.38 | 16.56 | 2.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.49 | 10.02 | 15.97 | 0.00 | 86.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 6.0 | 4.30 | 11.62 | 18.27 | 2.00 | 81.4 | 78.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.8 | 3.81 | 11.08 | 17.65 | 2.00 | 50.0 | 77.0 |
| Bench 4 | Bench | Cameron Archer | FWD | -1 | 5.0 | 2.35 | 7.35 | 12.28 | 2.00 | 29.5 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.0 | 6.97 | 20.41 | 31.89 | 13.00 | 93.1 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 5.98 | 17.06 | 27.21 | 14.00 | 87.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.14 | 14.64 | 23.89 | 2.00 | 87.3 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.7 | 4.24 | 12.62 | 21.15 | 6.00 | 32.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.91 | 11.62 | 18.84 | 2.00 | 79.6 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.72
- Actual score: 70.00
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 1.43, hit 0)
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.27 | 16.23 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.7 | 3.39 | 8.97 | 14.06 | 0.00 | 86.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.05 | 11.94 | 19.11 | 1.00 | 87.8 | 28.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.97 | 11.82 | 18.85 | 1.00 | 88.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 3.68 | 11.79 | 20.27 | 6.00 | 64.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.42 | 9.99 | 15.97 | 0.00 | 86.2 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | -1 | 4.7 | 3.53 | 9.94 | 15.85 | 6.00 | 85.9 | 90.0 |
| XI | Bench | Danny Welbeck | FWD | -1 | 6.0 | 3.71 | 11.14 | 18.09 | 0.00 | 77.8 | 0.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.7 | 3.81 | 10.79 | 17.42 | 1.00 | 50.3 | 10.0 |
| Bench 4 | Bench | Cameron Archer | FWD | -1 | 5.0 | 2.94 | 7.82 | 12.29 | 2.00 | 70.8 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 7.41 | 21.59 | 33.60 | 18.00 | 79.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 6.60 | 17.96 | 28.23 | 7.00 | 92.3 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.51 | 13.72 | 22.42 | 2.00 | 87.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.3 | 4.82 | 12.05 | 18.07 | 3.00 | 75.9 | 63.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.6 | 3.99 | 11.73 | 19.07 | 1.00 | 72.1 | 23.0 |

## GW15

- Train rows: 142975
- Bank: 0.70 -> 1.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 52.98
- Actual score: 72.00
- Transfer: Luis Díaz -> Noni Madueke (projected gain 3.00, hit 0)
- Autosub outfielders: Raúl Jiménez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.62 | 10.44 | 16.53 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 1.13 | 3.59 | 6.16 | 0.00 | 28.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 4.26 | 12.44 | 20.24 | 1.00 | 80.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.77 | 11.18 | 18.33 | 3.00 | 77.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.20 | 9.85 | 15.74 | 1.00 | 86.9 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.31 | 8.95 | 14.28 | 4.00 | 85.0 | 85.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 1.60 | 6.44 | 10.66 | 0.00 | 35.0 | 0.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.9 | 3.59 | 10.54 | 18.07 | 1.00 | 29.5 | 20.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | -1 | 5.6 | 2.84 | 9.25 | 15.52 | 8.00 | 29.2 | 78.0 |
| Bench 3 | Bench | Cameron Archer | FWD | -1 | 5.0 | 2.59 | 7.60 | 12.25 | 2.00 | 70.3 | 72.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 6.63 | 18.43 | 28.57 | 18.00 | 88.5 | 90.0 |
| Vice Captain | Bench | Mohamed Salah | MID | -1 | 13.2 | 4.97 | 15.89 | 25.18 | 0.00 | 57.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 4.14 | 12.62 | 21.60 | 13.00 | 81.2 | 90.0 |
| XI | XI | Noni Madueke | MID | -1 | 6.3 | 4.47 | 12.13 | 19.12 | 1.00 | 62.0 | 4.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.4 | 4.39 | 11.73 | 18.10 | 2.00 | 72.2 | 62.0 |

## GW16

- Train rows: 143668
- Bank: 1.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.38
- Actual score: 49.00
- Transfer: Cameron Archer -> João Pedro Junqueira de Jesus (projected gain 3.91, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.57 | 10.30 | 16.35 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.67 | 7.67 | 12.60 | 3.00 | 76.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 4.32 | 12.09 | 19.38 | 7.00 | 54.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 3.29 | 9.71 | 16.25 | 1.00 | 64.9 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | -1 | 4.7 | 2.79 | 8.94 | 14.63 | 6.00 | 85.8 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.27 | 8.93 | 14.41 | -2.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.6 | 2.99 | 8.50 | 13.68 | 6.00 | 64.1 | 62.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.9 | 4.37 | 12.15 | 18.26 | 2.00 | 65.3 | 90.0 |
| XI | Bench | Danny Welbeck | FWD | -1 | 5.9 | 3.17 | 9.82 | 17.06 | 0.00 | 57.9 | 0.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | -1 | 5.5 | 2.76 | 9.11 | 15.12 | 2.00 | 48.9 | 67.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 7.75 | 21.25 | 33.07 | 3.00 | 104.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.2 | 6.96 | 20.95 | 34.44 | 5.00 | 73.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 4.40 | 13.44 | 22.46 | 9.00 | 87.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.5 | 4.72 | 12.18 | 18.70 | 3.00 | 71.1 | 79.0 |
| XI | XI | Noni Madueke | MID | -1 | 6.3 | 3.79 | 11.06 | 18.18 | 6.00 | 25.8 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 1.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.52
- Actual score: 50.00
- Transfer: Virgil van Dijk -> William Saliba (projected gain 1.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.87 | 11.15 | 17.61 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.58 | 7.86 | 12.95 | 9.00 | 76.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.2 | 4.21 | 12.01 | 18.29 | 2.00 | 81.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 3.89 | 11.97 | 19.49 | 0.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.60 | 11.30 | 18.40 | -1.00 | 80.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.96 | 10.53 | 16.87 | 6.00 | 90.5 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.32 | 9.08 | 14.44 | 0.00 | 78.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.9 | 4.50 | 12.01 | 18.43 | 2.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.5 | 3.23 | 8.85 | 14.61 | 0.00 | 65.3 | 28.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.8 | 1.09 | 3.53 | 6.42 | 0.00 | 16.3 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.1 | 7.50 | 21.22 | 33.09 | 3.00 | 99.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.4 | 7.00 | 20.91 | 34.16 | 21.00 | 82.2 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.66 | 13.75 | 22.48 | 2.00 | 90.3 | 90.0 |
| XI | XI | Noni Madueke | MID | -1 | 6.3 | 4.29 | 11.83 | 18.34 | 1.00 | 64.8 | 14.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.5 | 3.54 | 11.15 | 18.18 | 8.00 | 68.2 | 77.0 |

## GW18

- Train rows: 145070
- Bank: 1.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.31
- Actual score: 54.00
- Transfer: Danny Welbeck -> Chris Wood (projected gain 1.22, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 4.03 | 11.25 | 17.91 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 3.08 | 8.86 | 14.17 | 2.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.40 | 11.88 | 18.39 | 7.00 | 83.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.8 | 3.76 | 11.71 | 18.70 | 1.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.6 | 3.57 | 10.64 | 17.41 | 1.00 | 85.9 | 9.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 3.62 | 10.46 | 16.82 | 2.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 1.84 | 6.50 | 12.97 | 6.00 | 24.4 | 86.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 4.17 | 11.68 | 18.47 | 2.00 | 77.6 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.9 | 4.24 | 11.65 | 18.40 | 2.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.5 | 2.47 | 8.51 | 14.33 | 2.00 | 33.6 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.4 | 8.27 | 22.92 | 36.45 | 9.00 | 93.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.2 | 7.18 | 20.60 | 32.60 | 10.00 | 98.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.71 | 13.74 | 22.13 | 3.00 | 89.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.5 | 3.90 | 11.54 | 18.69 | 2.00 | 72.3 | 71.0 |
| XI | Bench | Noni Madueke | MID | -1 | 6.3 | 3.75 | 11.32 | 18.39 | 0.00 | 28.6 | 0.0 |

## GW19

- Train rows: 145775
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.69
- Actual score: 82.00
- Transfer: Justin Kluivert -> Amad Diallo (projected gain 1.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 4.04 | 11.72 | 18.76 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 3.16 | 8.99 | 14.47 | 0.00 | 85.6 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.18 | 12.34 | 19.82 | 2.00 | 83.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.17 | 11.58 | 18.50 | 4.00 | 91.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.65 | 11.17 | 19.02 | 4.00 | 67.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.88 | 10.93 | 17.54 | 6.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.88 | 8.44 | 13.73 | 10.00 | 76.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.8 | 3.84 | 11.59 | 19.18 | 9.00 | 78.7 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.70 | 11.21 | 18.18 | 12.00 | 76.7 | 75.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.5 | 2.95 | 8.48 | 13.49 | 9.00 | 54.3 | 67.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.5 | 8.70 | 24.26 | 38.09 | 16.00 | 103.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 7.02 | 20.73 | 33.72 | 2.00 | 92.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.41 | 13.69 | 22.28 | 7.00 | 86.9 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 4.40 | 12.61 | 19.93 | 2.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Noni Madueke | MID | -1 | 6.3 | 3.15 | 9.49 | 15.93 | 2.00 | 27.9 | 76.0 |

## GW20

- Train rows: 146484
- Bank: 0.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.52
- Actual score: 81.00
- Transfer: Noni Madueke -> Morgan Rogers (projected gain 2.29, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.87 | 11.24 | 18.16 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.16 | 7.16 | 12.51 | 3.00 | 61.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.41 | 12.01 | 19.09 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.99 | 11.71 | 18.99 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.5 | 3.73 | 11.04 | 18.10 | 4.00 | 81.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.04 | 10.93 | 17.09 | 2.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.03 | 8.97 | 14.59 | 1.00 | 78.8 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 4.14 | 12.00 | 19.18 | 8.00 | 78.6 | 87.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.85 | 11.58 | 18.80 | 9.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.5 | 3.47 | 9.22 | 14.36 | 13.00 | 68.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 9.74 | 25.70 | 40.06 | 7.00 | 110.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.80 | 20.23 | 32.61 | 10.00 | 95.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 5.16 | 14.44 | 22.98 | 19.00 | 88.6 | 90.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 5.5 | 5.00 | 13.30 | 20.98 | 0.00 | 86.2 | 0.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 3.78 | 11.82 | 19.07 | 9.00 | 82.0 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.69
- Actual score: 60.00
- Transfer: Joško Gvardiol -> Trent Alexander-Arnold (projected gain 2.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 4.13 | 11.44 | 18.26 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.81 | 8.22 | 13.34 | 1.00 | 77.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 4.27 | 13.05 | 21.12 | 2.00 | 81.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.27 | 12.32 | 19.82 | 7.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.17 | 11.19 | 17.80 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.5 | 3.43 | 10.64 | 17.20 | 1.00 | 59.0 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.80 | 8.47 | 13.79 | 1.00 | 81.5 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.30 | 13.41 | 21.58 | 9.00 | 73.2 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 4.28 | 11.79 | 18.61 | 1.00 | 85.7 | 77.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.6 | 4.33 | 11.35 | 17.40 | 1.00 | 79.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 8.80 | 25.04 | 39.63 | 2.00 | 100.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 7.26 | 20.65 | 33.23 | 10.00 | 103.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 5.84 | 16.75 | 26.32 | 2.00 | 99.1 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.3 | 4.25 | 11.82 | 19.15 | 20.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.5 | 3.34 | 11.15 | 19.58 | 6.00 | 31.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.45
- Actual score: 52.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: William Saliba -> Ola Aina (projected gain 0.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.71 | 10.69 | 17.21 | 1.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.77 | 7.95 | 12.63 | 2.00 | 75.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 4.25 | 12.83 | 20.89 | 11.00 | 82.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.62 | 12.69 | 20.20 | 8.00 | 90.7 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.2 | 4.21 | 11.37 | 17.96 | 4.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.5 | 3.75 | 10.63 | 16.82 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.63 | 8.07 | 13.34 | 1.00 | 80.4 | 73.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.85 | 13.20 | 21.21 | 12.00 | 81.1 | 82.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.7 | 4.64 | 12.19 | 19.05 | 2.00 | 74.5 | 70.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.94 | 11.30 | 18.08 | 2.00 | 78.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.57 | 24.30 | 38.26 | 3.00 | 94.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 7.42 | 20.82 | 33.10 | 2.00 | 103.3 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.57 | 16.10 | 25.79 | 2.00 | 74.6 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 5.11 | 14.16 | 22.26 | 2.00 | 93.1 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.5 | 3.67 | 11.75 | 19.06 | 1.00 | 79.8 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 1.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.81
- Actual score: 51.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Rayan Aït-Nouri -> Lewis Hall (projected gain 1.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.54 | 10.28 | 16.62 | 9.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 2.65 | 8.14 | 13.16 | 2.00 | 82.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 5.02 | 14.13 | 22.23 | 5.00 | 84.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 4.59 | 12.48 | 19.65 | 2.00 | 90.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | -1 | 5.0 | 4.54 | 11.71 | 18.18 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Ola Aina | DEF | -1 | 5.3 | 3.94 | 11.35 | 17.93 | 1.00 | 88.0 | 78.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.96 | 10.77 | 17.14 | 6.00 | 84.8 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 4.96 | 14.75 | 23.47 | 2.00 | 85.0 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.7 | 4.48 | 11.98 | 18.76 | 2.00 | 73.3 | 63.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.70 | 10.69 | 17.07 | 1.00 | 72.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.33 | 23.38 | 36.76 | 8.00 | 91.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.59 | 19.43 | 31.35 | 2.00 | 75.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.65 | 15.77 | 25.22 | 7.00 | 92.1 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.5 | 4.74 | 13.54 | 21.64 | 3.00 | 89.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.5 | 4.03 | 11.19 | 17.89 | 1.00 | 77.3 | 71.0 |

## GW24

- Train rows: 149404
- Bank: 0.90 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cody Gakpo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 85.18
- Actual score: 126.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.73) beats the best remaining Triple Captain opportunity (15.80).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Chris Wood -> Cody Gakpo (projected gain 9.35, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (13.73) beats the best remaining Triple Captain opportunity (15.80).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.61 | 10.63 | 17.20 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.8 | 3.02 | 8.43 | 13.69 | 0.00 | 81.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 7.60 | 19.60 | 29.79 | 7.00 | 102.8 | 98.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 4.00 | 11.99 | 19.41 | 4.00 | 88.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | -1 | 5.1 | 4.21 | 11.61 | 18.03 | 1.00 | 77.2 | 86.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.83 | 11.16 | 17.90 | 6.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.65 | 10.89 | 17.55 | 6.00 | 85.4 | 90.0 |
| Vice Captain | XI | Cody Gakpo | FWD | -1 | 7.5 | 7.89 | 19.40 | 29.34 | 7.00 | 98.1 | 137.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | -1 | 5.7 | 3.34 | 11.26 | 18.59 | 8.00 | 61.4 | 72.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.36 | 10.49 | 16.78 | 1.00 | 77.6 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 10.95 | 28.94 | 45.10 | 29.00 | 142.8 | 177.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.3 | 6.64 | 18.89 | 30.48 | 6.00 | 92.5 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.80 | 16.30 | 25.86 | 2.00 | 89.7 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 4.81 | 13.13 | 20.68 | 2.00 | 90.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 3.95 | 11.50 | 18.42 | 1.00 | 76.2 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 90.28
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.22) beats the best remaining Bench Boost opportunity (14.32).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Pedro Porro -> Andrew Robertson (projected gain 3.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.22) beats the best remaining Bench Boost opportunity (14.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.64 | 10.37 | 17.01 | 7.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | -1 | 4.7 | 1.81 | 6.52 | 11.68 | 0.00 | 58.5 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 8.03 | 20.32 | 30.95 | 13.00 | 124.1 | 128.0 |
| XI | XI | Andrew Robertson | DEF | -1 | 5.9 | 6.06 | 14.36 | 21.02 | 3.00 | 124.7 | 180.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.94 | 11.74 | 18.90 | 2.00 | 87.6 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 4.09 | 11.72 | 18.84 | 1.00 | 66.6 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | -1 | 5.1 | 3.49 | 10.45 | 16.76 | 0.00 | 55.5 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.6 | 8.00 | 20.75 | 31.11 | 0.00 | 113.5 | 0.0 |
| Bench 2 | Bench Boost | Raúl Jiménez | FWD | -1 | 5.6 | 3.65 | 11.79 | 19.28 | 5.00 | 66.7 | 75.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.26 | 9.88 | 16.40 | 1.00 | 45.1 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 11.72 | 30.19 | 46.27 | 20.00 | 174.0 | 180.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.3 | 6.33 | 18.44 | 29.52 | 2.00 | 72.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 5.91 | 14.93 | 22.98 | 4.00 | 99.0 | 180.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 4.48 | 13.24 | 20.96 | 0.00 | 84.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.18 | 12.06 | 19.05 | 3.00 | 66.3 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.79
- Actual score: 81.00
- Transfer: David Raya Martin -> Alisson Ramses Becker (projected gain 0.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.5 | 3.99 | 11.71 | 18.25 | 8.00 | 123.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.7 | 0.76 | 3.35 | 6.47 | 0.00 | 30.5 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 6.21 | 17.73 | 28.04 | 6.00 | 111.2 | 90.0 |
| XI | XI | Andrew Robertson | DEF | -1 | 5.9 | 4.41 | 12.29 | 18.89 | 6.00 | 115.7 | 73.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.60 | 10.88 | 17.70 | 0.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | -1 | 5.1 | 3.20 | 9.60 | 15.83 | 9.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.85 | 8.50 | 13.56 | 1.00 | 65.5 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.6 | 4.34 | 13.79 | 23.60 | 1.00 | 39.9 | 11.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.6 | 4.41 | 12.19 | 19.44 | 2.00 | 62.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.99 | 10.99 | 18.28 | 12.00 | 36.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 10.40 | 29.01 | 45.45 | 14.00 | 150.5 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.2 | 5.84 | 17.63 | 28.54 | 2.00 | 91.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.91 | 16.12 | 25.28 | 14.00 | 88.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 5.30 | 14.65 | 22.26 | 2.00 | 91.9 | 77.0 |
| Bench 2 | Bench | Amad Diallo | MID | -1 | 5.6 | 3.74 | 12.89 | 22.34 | 0.00 | 60.8 | 0.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.27
- Actual score: 56.00
- Transfer: Cody Gakpo -> Chris Wood (projected gain 6.60, hit 0)
- Autosub outfielders: Ola Aina.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.5 | 3.47 | 10.27 | 16.32 | 6.00 | 103.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.6 | 1.19 | 3.37 | 6.18 | 0.00 | 19.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.64 | 16.12 | 25.72 | 6.00 | 79.2 | 76.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.74 | 10.96 | 17.50 | 0.00 | 86.6 | 18.0 |
| XI | Bench | Andrew Robertson | DEF | -1 | 5.9 | 3.73 | 10.58 | 16.50 | 0.00 | 89.2 | 0.0 |
| Bench 2 | Autosub In | Ola Aina | DEF | -1 | 5.4 | 3.37 | 10.34 | 16.92 | 6.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | -1 | 5.0 | 3.24 | 9.95 | 16.17 | 1.00 | 85.3 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 5.73 | 16.84 | 26.79 | 2.00 | 100.3 | 84.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.6 | 4.18 | 11.49 | 18.38 | 1.00 | 78.4 | 18.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 4.12 | 11.42 | 18.31 | 8.00 | 77.1 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.48 | 26.84 | 42.52 | 6.00 | 126.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 6.14 | 17.62 | 27.64 | 5.00 | 91.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.1 | 6.25 | 17.27 | 27.67 | 3.00 | 89.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 4.30 | 11.64 | 18.59 | 7.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Amad Diallo | MID | -1 | 5.5 | 2.69 | 9.03 | 17.60 | 0.00 | 17.1 | 0.0 |

## GW28

- Train rows: 152512
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.73
- Actual score: 68.00
- Transfer: Andrew Robertson -> Virgil van Dijk (projected gain 2.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.5 | 3.93 | 10.39 | 16.26 | 3.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.6 | 1.29 | 3.62 | 6.68 | 9.00 | 20.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.62 | 15.21 | 24.09 | 2.00 | 90.2 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.33 | 11.74 | 18.65 | 2.00 | 99.7 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.66 | 10.68 | 17.23 | 6.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 3.30 | 10.24 | 17.21 | 0.00 | 70.7 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | -1 | 5.0 | 3.39 | 9.30 | 14.87 | 0.00 | 83.2 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.00 | 15.31 | 24.80 | 2.00 | 88.9 | 86.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.6 | 3.77 | 11.25 | 18.50 | 8.00 | 63.4 | 68.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 3.94 | 11.04 | 17.90 | 9.00 | 64.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.00 | 25.33 | 40.00 | 15.00 | 118.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.1 | 6.56 | 17.75 | 27.97 | 1.00 | 90.9 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.0 | 5.87 | 17.01 | 27.12 | 2.00 | 89.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 4.04 | 11.36 | 18.58 | 3.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Amad Diallo | MID | -1 | 5.4 | 0.72 | 3.16 | 6.22 | 0.00 | 14.5 | 0.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 50.92
- Actual score: 23.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 4.22, hit 0)
- Autosub: Robert Sánchez replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | -1 | 5.6 | 1.34 | 5.21 | 8.96 | 0.00 | 38.1 | 0.0 |
| Bench 1 | Autosub In | Robert Sánchez | GK | -1 | 4.5 | 1.19 | 4.11 | 6.88 | 3.00 | 36.1 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.3 | 3.95 | 11.29 | 18.05 | 1.00 | 87.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.85 | 10.99 | 17.66 | 1.00 | 85.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.73 | 10.57 | 17.30 | 7.00 | 81.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 2.44 | 8.54 | 14.29 | 0.00 | 37.8 | 0.0 |
| Bench 4 | Bench | Lewis Hall | DEF | -1 | 4.9 | 0.07 | 3.43 | 8.25 | 0.00 | 6.8 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.27 | 16.00 | 25.64 | 2.00 | 84.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.99 | 11.77 | 18.53 | 1.00 | 79.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.5 | 4.00 | 11.38 | 17.96 | 2.00 | 60.3 | 62.0 |
| Vice Captain | Bench | Mohamed Salah | MID | -1 | 13.8 | 5.65 | 18.01 | 29.21 | 0.00 | 65.7 | 0.0 |
| Captain | Bench | Cole Palmer | MID | -1 | 11.0 | 5.69 | 16.85 | 27.17 | 0.00 | 80.7 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.29 | 15.40 | 24.73 | 6.00 | 90.7 | 90.0 |
| Bench 2 | Bench | Amad Diallo | MID | -1 | 5.4 | 2.36 | 7.08 | 13.09 | 0.00 | 18.0 | 0.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.6 | 1.72 | 6.38 | 10.77 | 0.00 | 36.8 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.19
- Actual score: 34.00
- Transfer: Alisson Ramses Becker -> David Raya Martin (projected gain 3.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.99 | 11.26 | 17.96 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | -1 | 4.5 | 3.04 | 8.06 | 12.80 | 6.00 | 72.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 4.70 | 14.12 | 23.88 | 0.00 | 54.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.29 | 12.11 | 18.93 | 6.00 | 87.3 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 4.23 | 11.88 | 18.58 | 1.00 | 86.8 | 39.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.24 | 9.98 | 16.52 | 1.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | -1 | 4.9 | 0.91 | 2.91 | 5.04 | 0.00 | 22.7 | 0.0 |
| XI | Bench | Chris Wood | FWD | -1 | 7.3 | 5.71 | 15.94 | 25.01 | 0.00 | 80.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.91 | 11.57 | 18.27 | 2.00 | 81.3 | 71.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.5 | 3.28 | 10.44 | 16.92 | 2.00 | 46.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.82 | 23.04 | 38.01 | 3.00 | 80.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 5.86 | 16.67 | 28.77 | 6.00 | 34.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.35 | 15.82 | 25.05 | 8.00 | 91.7 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | -1 | 5.6 | 3.19 | 10.00 | 16.80 | 10.00 | 67.0 | 87.0 |
| Bench 4 | Bench | Amad Diallo | MID | -1 | 5.3 | 0.66 | 3.09 | 6.19 | 0.00 | 17.5 | 0.0 |