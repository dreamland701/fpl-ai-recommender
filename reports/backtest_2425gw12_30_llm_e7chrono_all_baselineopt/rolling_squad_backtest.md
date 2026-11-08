# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 987.52
- Total actual points: 1314.00
- Average predicted points: 51.97
- Average actual points: 69.16
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.04
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 2.86 | 8.76 | 13.77 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.43 | 7.08 | 11.81 | 7.00 | 86.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 3.96 | 10.98 | 17.22 | 0.00 | 88.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 3.38 | 9.79 | 14.67 | 1.00 | 88.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.12 | 9.61 | 15.34 | 14.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 3.00 | 9.40 | 14.91 | 2.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.0 | 3.02 | 9.08 | 14.72 | 0.00 | 71.7 | 0.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.9 | 3.08 | 9.53 | 14.98 | 2.00 | 76.2 | 85.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.8 | 3.21 | 9.40 | 14.59 | 2.00 | 76.1 | 70.0 |
| Bench 4 | Bench | Liam Delap | FWD | -1 | 5.6 | 2.92 | 8.30 | 12.92 | 2.00 | 73.9 | 80.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.02 | 17.27 | 25.46 | 13.00 | 89.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.0 | 4.88 | 13.96 | 22.86 | 2.00 | 88.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.04 | 13.20 | 21.39 | 3.00 | 92.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.7 | 4.29 | 10.62 | 16.54 | 1.00 | 85.1 | 58.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.19 | 9.53 | 14.92 | 2.00 | 73.5 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.20 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.38
- Actual score: 60.00
- Transfer: Trent Alexander-Arnold -> Antonee Robinson (projected gain 0.34, hit 0)
- Autosub outfielders: Rayan Aït-Nouri.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.16 | 8.89 | 13.91 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.64 | 7.41 | 11.65 | 2.00 | 89.9 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 3.36 | 11.57 | 18.51 | 0.00 | 91.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.50 | 11.04 | 17.25 | 2.00 | 92.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.03 | 9.57 | 14.91 | 6.00 | 86.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.04 | 9.07 | 15.11 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.92 | 8.81 | 14.34 | 0.00 | 86.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 6.0 | 3.66 | 9.58 | 15.06 | 2.00 | 81.4 | 78.0 |
| Bench 3 | Bench | Liam Delap | FWD | -1 | 5.6 | 2.73 | 8.07 | 12.79 | 2.00 | 74.3 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | -1 | 5.8 | 2.49 | 7.57 | 11.66 | 2.00 | 50.0 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.0 | 5.97 | 16.41 | 25.89 | 13.00 | 93.1 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 4.86 | 14.01 | 22.25 | 14.00 | 87.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 3.68 | 12.19 | 19.24 | 2.00 | 87.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.04 | 9.13 | 14.55 | 2.00 | 79.6 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.8 | 3.11 | 9.12 | 15.22 | 2.00 | 76.1 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 2.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 47.32
- Actual score: 71.00
- Transfer: Liam Delap -> Matheus Santos Carneiro Da Cunha (projected gain 4.61, hit 0)
- Autosub outfielders: Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.09 | 8.66 | 13.50 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.59 | 7.14 | 11.77 | 7.00 | 86.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.31 | 10.82 | 17.52 | 1.00 | 87.8 | 28.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.85 | 8.78 | 14.34 | 0.00 | 86.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 2.96 | 8.44 | 13.21 | 6.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.23 | 8.30 | 13.16 | 1.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 2.61 | 8.14 | 13.96 | 6.00 | 64.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.0 | 4.29 | 12.85 | 19.37 | 2.00 | 84.8 | 90.0 |
| XI | Bench | Danny Welbeck | FWD | -1 | 6.0 | 2.91 | 9.13 | 15.01 | 0.00 | 77.8 | 0.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | -1 | 5.7 | 2.49 | 7.81 | 12.23 | 1.00 | 50.3 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 6.21 | 17.59 | 27.60 | 18.00 | 79.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 5.30 | 13.96 | 22.23 | 7.00 | 92.3 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 3.96 | 11.98 | 20.69 | 2.00 | 87.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.8 | 3.00 | 9.34 | 14.80 | 2.00 | 78.8 | 70.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | -1 | 5.4 | 2.81 | 7.81 | 12.61 | 8.00 | 72.8 | 86.0 |

## GW15

- Train rows: 142975
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 44.41
- Actual score: 66.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 2.55, hit 0)
- Autosub outfielders: Danny Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.04 | 9.12 | 14.69 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.64 | 6.97 | 11.37 | 1.00 | 86.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 3.27 | 10.01 | 16.48 | 1.00 | 80.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 2.92 | 9.05 | 15.03 | 3.00 | 77.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 2.74 | 8.35 | 12.82 | 1.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 1.56 | 8.20 | 13.81 | 0.00 | 35.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.9 | 2.80 | 7.36 | 11.43 | 4.00 | 85.0 | 85.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.05 | 11.69 | 17.99 | 1.00 | 87.1 | 90.0 |
| Bench 2 | Autosub In | Danny Welbeck | FWD | -1 | 5.9 | 2.37 | 5.93 | 10.11 | 1.00 | 29.5 | 20.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.6 | 1.63 | 5.01 | 8.29 | 8.00 | 29.2 | 78.0 |
| Vice Captain | Bench | Mohamed Salah | MID | -1 | 13.2 | 4.99 | 18.36 | 29.42 | 0.00 | 57.8 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 5.03 | 14.43 | 22.57 | 18.00 | 88.5 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 3.69 | 10.88 | 16.43 | 2.00 | 89.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 3.21 | 10.21 | 17.40 | 13.00 | 81.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 3.64 | 9.60 | 14.77 | 2.00 | 79.7 | 90.0 |

## GW16

- Train rows: 143668
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 46.37
- Actual score: 52.00
- Transfer: Raúl Jiménez -> Chris Wood (projected gain 3.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 2.96 | 8.57 | 13.43 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.10 | 7.00 | 12.09 | 2.00 | 82.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 2.93 | 8.38 | 13.48 | 7.00 | 54.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 2.98 | 8.21 | 13.18 | 6.00 | 64.1 | 62.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 4.7 | 2.11 | 7.36 | 13.07 | 6.00 | 85.8 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.9 | 2.73 | 6.94 | 11.38 | -2.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.40 | 6.37 | 10.44 | 1.00 | 64.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.45 | 11.04 | 16.78 | 9.00 | 82.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.5 | 3.25 | 9.66 | 15.23 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 2.17 | 6.62 | 11.09 | 0.00 | 57.9 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 6.75 | 18.75 | 28.47 | 3.00 | 104.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.2 | 5.01 | 15.77 | 25.60 | 5.00 | 73.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 3.51 | 12.06 | 20.59 | 9.00 | 87.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 3.17 | 10.09 | 16.02 | 2.00 | 81.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 2.88 | 9.01 | 14.64 | 2.00 | 85.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 47.22
- Actual score: 67.00
- Transfer: Virgil van Dijk -> William Saliba (projected gain 1.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.15 | 9.10 | 14.26 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.33 | 6.92 | 11.31 | 0.00 | 84.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.2 | 3.28 | 9.84 | 14.37 | 2.00 | 81.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 2.86 | 8.94 | 14.67 | -1.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | -1 | 6.1 | 2.81 | 8.33 | 13.78 | 0.00 | 87.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 2.96 | 8.23 | 13.77 | 6.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.9 | 2.38 | 7.38 | 11.41 | 0.00 | 78.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.75 | 10.70 | 16.95 | 9.00 | 86.2 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.07 | 8.93 | 14.26 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.8 | 1.09 | 3.58 | 6.87 | 0.00 | 16.3 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.1 | 6.30 | 20.12 | 30.59 | 3.00 | 99.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.4 | 5.78 | 16.25 | 27.08 | 21.00 | 82.2 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 3.36 | 11.05 | 17.78 | 2.00 | 90.3 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.7 | 3.20 | 9.22 | 14.66 | 3.00 | 85.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.21 | 9.10 | 14.32 | 14.00 | 83.0 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.01
- Actual score: 64.00
- Transfer: Alex Iwobi -> Amad Diallo (projected gain 2.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.25 | 9.62 | 15.24 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.26 | 6.89 | 10.96 | 7.00 | 83.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.8 | 3.08 | 9.57 | 15.01 | 1.00 | 87.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.41 | 9.47 | 14.20 | 7.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.29 | 9.21 | 14.95 | 1.00 | 85.9 | 9.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | -1 | 6.1 | 2.97 | 8.61 | 13.60 | 2.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 1.22 | 4.04 | 7.76 | 6.00 | 24.4 | 86.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.82 | 10.99 | 18.16 | 12.00 | 87.7 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.18 | 9.00 | 14.37 | 2.00 | 77.6 | 86.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.7 | 1.13 | 3.95 | 6.94 | 0.00 | 16.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.4 | 7.17 | 18.92 | 30.45 | 9.00 | 93.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.2 | 6.08 | 16.60 | 26.60 | 10.00 | 98.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 3.41 | 12.74 | 21.73 | 3.00 | 89.5 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.3 | 3.45 | 11.10 | 17.34 | 2.00 | 79.7 | 78.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 3.68 | 11.02 | 17.63 | 2.00 | 85.7 | 68.0 |

## GW19

- Train rows: 145775
- Bank: 0.80 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.34
- Actual score: 78.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 0.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.29 | 10.00 | 16.27 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.4 | 2.91 | 7.91 | 13.07 | 2.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.30 | 10.12 | 16.57 | 2.00 | 83.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 3.37 | 9.98 | 16.20 | 4.00 | 91.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.07 | 9.12 | 14.96 | 6.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | -1 | 5.5 | 2.67 | 8.00 | 13.88 | 4.00 | 67.1 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.40 | 6.33 | 9.82 | 10.00 | 76.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.77 | 11.51 | 18.45 | 1.00 | 90.9 | 45.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.8 | 3.03 | 9.37 | 16.35 | 9.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | -1 | 6.6 | 2.86 | 9.06 | 14.88 | 12.00 | 76.7 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.5 | 7.40 | 20.26 | 32.09 | 16.00 | 103.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 5.62 | 16.73 | 27.72 | 2.00 | 92.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 3.52 | 12.21 | 19.42 | 7.00 | 86.9 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 3.36 | 10.22 | 16.44 | 2.00 | 82.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.21 | 10.04 | 16.67 | 11.00 | 79.6 | 90.0 |

## GW20

- Train rows: 146484
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.33
- Actual score: 85.00
- Transfer: Joško Gvardiol -> Ola Aina (projected gain 0.81, hit 0)
- Autosub outfielders: Pedro Porro, Amad Diallo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.23 | 10.02 | 15.87 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.65 | 7.19 | 11.27 | 2.00 | 85.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 3.91 | 10.91 | 16.99 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.22 | 10.10 | 15.67 | 2.00 | 83.7 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.1 | 3.19 | 9.67 | 14.91 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.5 | 3.02 | 9.24 | 14.61 | 4.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.49 | 6.75 | 10.83 | 1.00 | 78.8 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.25 | 11.00 | 18.31 | 0.00 | 79.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.09 | 9.68 | 15.89 | 9.00 | 83.3 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.21 | 9.64 | 14.95 | 8.00 | 78.6 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 8.74 | 21.70 | 34.06 | 7.00 | 110.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 5.80 | 16.23 | 26.61 | 10.00 | 95.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.01 | 12.09 | 21.05 | 19.00 | 88.6 | 90.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 5.5 | 3.95 | 10.66 | 16.27 | 0.00 | 86.2 | 0.0 |
| Bench 3 | Autosub In | Amad Diallo | MID | -1 | 5.4 | 2.98 | 10.07 | 15.93 | 9.00 | 82.0 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 1.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.22
- Actual score: 61.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Cody Gakpo (projected gain 2.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.35 | 10.10 | 16.19 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.81 | 7.33 | 11.40 | 7.00 | 85.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.43 | 11.09 | 17.61 | 7.00 | 88.0 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.2 | 3.14 | 10.16 | 15.88 | 2.00 | 85.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.29 | 9.42 | 14.54 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.5 | 2.48 | 9.08 | 15.25 | 1.00 | 59.0 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.45 | 6.90 | 10.52 | 1.00 | 81.5 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 3.31 | 11.30 | 17.62 | 9.00 | 73.2 | 89.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.3 | 3.71 | 11.05 | 16.83 | 2.00 | 81.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.74 | 10.21 | 15.92 | 1.00 | 85.7 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 7.80 | 21.04 | 33.63 | 2.00 | 100.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.16 | 16.65 | 27.23 | 10.00 | 103.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 4.84 | 13.35 | 21.32 | 2.00 | 99.1 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.3 | 3.66 | 9.80 | 15.72 | 20.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Morgan Rogers | MID | -1 | 5.5 | 1.92 | 6.99 | 13.09 | 6.00 | 31.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.31
- Actual score: 51.00
- Transfer: William Saliba -> Trent Alexander-Arnold (projected gain 1.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.03 | 8.86 | 14.45 | 1.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.46 | 7.59 | 11.62 | 6.00 | 85.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.32 | 11.03 | 17.36 | 11.00 | 82.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.32 | 9.99 | 15.60 | 8.00 | 90.7 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.2 | 3.67 | 9.61 | 14.79 | 4.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.03 | 8.79 | 13.69 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.26 | 6.33 | 9.85 | 1.00 | 80.4 | 73.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 3.80 | 10.45 | 16.01 | 2.00 | 80.3 | 86.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 3.39 | 9.68 | 15.44 | 12.00 | 81.1 | 82.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.02 | 9.20 | 15.34 | 2.00 | 78.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 7.27 | 20.30 | 32.26 | 3.00 | 94.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.22 | 17.42 | 27.80 | 2.00 | 103.3 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 3.97 | 12.10 | 19.79 | 2.00 | 74.6 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 4.01 | 11.66 | 17.56 | 2.00 | 93.1 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.5 | 2.92 | 9.55 | 15.36 | 1.00 | 79.8 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.81
- Actual score: 80.00
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 0.85, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 2.93 | 8.56 | 13.60 | 9.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.73 | 7.79 | 12.10 | 1.00 | 84.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 3.91 | 10.74 | 16.27 | 5.00 | 84.3 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.3 | 3.20 | 10.14 | 15.74 | 1.00 | 88.0 | 78.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 3.23 | 9.22 | 15.00 | 6.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.99 | 8.48 | 13.65 | 2.00 | 90.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 1.64 | 5.43 | 8.41 | 2.00 | 67.6 | 86.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 3.80 | 12.08 | 21.02 | 2.00 | 85.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 3.53 | 10.36 | 15.63 | 16.00 | 78.1 | 67.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 2.95 | 8.56 | 13.51 | 1.00 | 72.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 6.83 | 19.38 | 30.76 | 8.00 | 91.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 4.99 | 15.43 | 25.35 | 2.00 | 75.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 4.35 | 12.37 | 19.52 | 7.00 | 92.1 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.5 | 3.74 | 10.94 | 17.24 | 3.00 | 89.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.5 | 3.45 | 9.90 | 15.47 | 13.00 | 87.0 | 87.0 |

## GW24

- Train rows: 149404
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.04
- Actual score: 140.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.01) beats the best remaining Triple Captain opportunity (12.37).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Lewis Hall (projected gain 0.64, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (11.01) beats the best remaining Triple Captain opportunity (12.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.03 | 9.21 | 15.15 | 3.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.67 | 6.90 | 10.89 | 6.00 | 84.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 4.81 | 12.28 | 18.75 | 7.00 | 102.8 | 98.0 |
| XI | XI | Lewis Hall | DEF | -1 | 5.1 | 3.28 | 9.58 | 14.55 | 1.00 | 77.2 | 86.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.07 | 9.39 | 14.64 | 6.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.96 | 8.76 | 14.21 | 4.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 2.34 | 6.25 | 9.37 | 7.00 | 77.8 | 72.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.5 | 5.01 | 12.53 | 19.34 | 7.00 | 98.1 | 137.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 3.01 | 9.69 | 16.01 | 17.00 | 64.5 | 81.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 2.69 | 8.35 | 12.82 | 1.00 | 77.6 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.23 | 22.52 | 35.73 | 29.00 | 142.8 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 5.04 | 14.89 | 24.48 | 6.00 | 92.5 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 4.80 | 13.70 | 21.36 | 2.00 | 89.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.6 | 3.49 | 11.41 | 17.70 | 2.00 | 85.6 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 3.81 | 10.63 | 16.98 | 2.00 | 90.3 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.60 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 72.46
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.42) beats the best remaining Bench Boost opportunity (12.66).
- Transfer: Rayan Aït-Nouri -> James Tarkowski (projected gain 2.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.42) beats the best remaining Bench Boost opportunity (12.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.02 | 8.64 | 14.16 | 7.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | -1 | 4.5 | 2.76 | 7.86 | 11.89 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.93 | 15.24 | 22.62 | 13.00 | 124.1 | 128.0 |
| XI | XI | James Tarkowski | DEF | -1 | 4.8 | 3.89 | 10.85 | 15.68 | 2.00 | 119.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.20 | 10.32 | 16.71 | 2.00 | 87.6 | 90.0 |
| Bench 2 | Bench Boost | Ola Aina | DEF | -1 | 5.4 | 2.94 | 8.60 | 13.54 | 1.00 | 66.6 | 90.0 |
| Bench 3 | Bench Boost | Lewis Hall | DEF | -1 | 5.1 | 2.46 | 7.76 | 12.24 | 0.00 | 55.5 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.6 | 5.04 | 14.33 | 20.33 | 0.00 | 113.5 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 4.26 | 11.45 | 18.63 | 9.00 | 71.2 | 90.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 2.15 | 6.43 | 10.73 | 1.00 | 45.1 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 10.30 | 25.88 | 39.80 | 20.00 | 174.0 | 180.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.3 | 4.83 | 14.44 | 23.52 | 2.00 | 72.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.06 | 12.30 | 19.77 | 3.00 | 66.3 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 3.53 | 11.12 | 17.69 | 0.00 | 84.9 | 0.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.8 | 3.80 | 10.93 | 19.78 | 5.00 | 74.6 | 76.0 |

## GW26

- Train rows: 150945
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.09
- Actual score: 63.00
- Transfer: Amad Diallo -> Anthony Elanga (projected gain 3.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.21 | 9.09 | 14.32 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.67 | 7.80 | 12.04 | 6.00 | 85.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.11 | 14.33 | 22.44 | 6.00 | 111.2 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.03 | 9.36 | 15.44 | 0.00 | 84.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 2.87 | 8.53 | 13.31 | 1.00 | 65.5 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | -1 | 5.1 | 2.68 | 7.55 | 12.75 | 9.00 | 79.8 | 90.0 |
| Bench 4 | Bench | James Tarkowski | DEF | -1 | 4.8 | 2.47 | 7.07 | 11.41 | 1.00 | 90.2 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 4.27 | 12.85 | 20.09 | 5.00 | 93.2 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.6 | 2.87 | 9.40 | 15.71 | 1.00 | 39.9 | 11.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 2.60 | 7.16 | 11.74 | 12.00 | 36.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.50 | 25.01 | 39.45 | 14.00 | 150.5 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.2 | 4.84 | 15.63 | 24.84 | 2.00 | 91.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.85 | 13.56 | 23.22 | 14.00 | 88.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.9 | 4.36 | 12.93 | 20.53 | 2.00 | 76.4 | 72.0 |
| XI | XI | Anthony Elanga | MID | -1 | 5.3 | 3.69 | 10.84 | 17.13 | 2.00 | 85.6 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.80 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.43
- Actual score: 62.00
- Transfer: Cody Gakpo -> Yoane Wissa (projected gain 1.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 2.51 | 8.60 | 13.89 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.48 | 7.04 | 11.26 | 2.00 | 85.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 4.04 | 12.12 | 19.72 | 6.00 | 79.2 | 76.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.07 | 9.43 | 14.63 | 0.00 | 86.6 | 18.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 2.84 | 9.14 | 14.74 | 6.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | -1 | 5.0 | 2.73 | 8.33 | 12.95 | 1.00 | 85.3 | 90.0 |
| Bench 4 | Bench | James Tarkowski | DEF | -1 | 4.8 | 2.53 | 7.13 | 11.59 | 2.00 | 88.0 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 4.73 | 14.44 | 22.29 | 2.00 | 100.3 | 84.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.3 | 3.64 | 10.12 | 15.63 | 9.00 | 82.1 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 3.13 | 8.46 | 13.61 | 8.00 | 77.1 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.28 | 22.84 | 36.52 | 6.00 | 126.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.04 | 14.92 | 23.14 | 5.00 | 91.7 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.1 | 4.75 | 13.27 | 21.67 | 3.00 | 89.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.0 | 3.98 | 11.81 | 18.52 | 10.00 | 77.8 | 90.0 |
| XI | XI | Anthony Elanga | MID | -1 | 5.3 | 3.25 | 10.00 | 16.22 | 3.00 | 86.0 | 61.0 |

## GW28

- Train rows: 152512
- Bank: 2.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.48
- Actual score: 64.00
- Transfer: James Tarkowski -> Joško Gvardiol (projected gain 1.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.16 | 9.06 | 14.60 | 3.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.5 | 2.84 | 8.12 | 13.39 | 10.00 | 83.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 4.02 | 11.21 | 18.09 | 2.00 | 90.2 | 88.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.10 | 9.62 | 14.96 | 2.00 | 85.3 | 90.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 3.03 | 8.97 | 14.26 | 6.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.54 | 7.81 | 13.10 | 0.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Lewis Hall | DEF | -1 | 5.0 | 2.44 | 6.50 | 10.63 | 0.00 | 83.2 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 3.60 | 11.31 | 18.80 | 2.00 | 88.9 | 86.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.4 | 3.43 | 10.22 | 15.62 | 2.00 | 85.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 3.01 | 8.83 | 14.54 | 9.00 | 64.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 7.60 | 21.33 | 34.00 | 15.00 | 118.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.0 | 4.87 | 14.21 | 22.82 | 2.00 | 89.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.1 | 4.96 | 13.75 | 21.97 | 1.00 | 90.9 | 72.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.0 | 4.10 | 12.36 | 18.83 | 5.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Anthony Elanga | MID | -1 | 5.3 | 2.86 | 8.41 | 14.05 | 3.00 | 76.1 | 79.0 |

## GW29

- Train rows: 153301
- Bank: 1.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.73
- Actual score: 52.00
- Transfer: Lewis Hall -> Marc Cucurella Saseta (projected gain 0.43, hit 0)
- Autosub outfielders: Anthony Elanga, Ola Aina.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.16 | 9.04 | 14.29 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.6 | 1.47 | 6.23 | 10.83 | 0.00 | 37.5 | 0.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 2.51 | 10.39 | 17.65 | 0.00 | 37.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.13 | 9.35 | 14.61 | 1.00 | 85.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | -1 | 5.2 | 2.92 | 8.98 | 14.65 | 2.00 | 90.7 | 90.0 |
| Bench 3 | Autosub In | Ola Aina | DEF | -1 | 5.3 | 2.91 | 8.67 | 13.76 | 1.00 | 87.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.03 | 8.59 | 13.76 | 7.00 | 81.8 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 4.06 | 13.67 | 21.21 | 2.00 | 84.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.22 | 10.17 | 15.74 | 1.00 | 79.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.5 | 3.16 | 10.06 | 16.52 | 8.00 | 81.1 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.8 | 5.65 | 20.42 | 33.61 | 0.00 | 65.7 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | -1 | 11.0 | 4.31 | 13.71 | 21.60 | 0.00 | 80.7 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 4.19 | 12.80 | 20.63 | 6.00 | 90.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.1 | 4.22 | 12.77 | 20.21 | 2.00 | 89.7 | 78.0 |
| Bench 2 | Autosub In | Anthony Elanga | MID | -1 | 5.3 | 3.12 | 8.67 | 14.03 | 16.00 | 78.5 | 66.0 |

## GW30

- Train rows: 154090
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.53
- Actual score: 52.00
- Transfer: Anthony Elanga -> Mikel Merino (projected gain 0.58, hit 0)
- Autosub outfielders: Mikel Merino, Ola Aina, Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.29 | 10.16 | 14.86 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | -1 | 4.6 | 1.90 | 5.90 | 9.86 | 2.00 | 37.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.80 | 10.86 | 15.54 | 6.00 | 87.3 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 3.18 | 10.35 | 17.31 | 0.00 | 54.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | -1 | 5.2 | 3.25 | 9.40 | 14.73 | 5.00 | 85.8 | 90.0 |
| Bench 4 | Autosub In | Antonee Robinson | DEF | -1 | 5.0 | 2.74 | 8.36 | 13.50 | 1.00 | 81.9 | 90.0 |
| Bench 3 | Autosub In | Ola Aina | DEF | -1 | 5.4 | 3.04 | 8.23 | 12.49 | 1.00 | 86.8 | 39.0 |
| XI | Bench | Chris Wood | FWD | -1 | 7.3 | 4.32 | 12.83 | 19.61 | 0.00 | 80.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.09 | 9.53 | 15.05 | 2.00 | 81.3 | 71.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.5 | 3.18 | 9.48 | 14.92 | 5.00 | 85.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 6.19 | 19.90 | 33.86 | 3.00 | 80.0 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | -1 | 6.2 | 4.40 | 14.04 | 21.36 | 0.00 | 86.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 4.15 | 13.42 | 20.45 | 8.00 | 91.7 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 10.9 | 3.48 | 11.08 | 18.93 | 6.00 | 34.0 | 90.0 |
| Bench 2 | Autosub In | Mikel Merino | MID | -1 | 6.0 | 3.05 | 8.68 | 13.63 | 10.00 | 77.0 | 90.0 |