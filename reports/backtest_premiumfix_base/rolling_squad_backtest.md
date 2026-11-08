# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW10
- Simulated weeks: GW11-GW30
- Total predicted points: 1213.81
- Total actual points: 1007.00
- Average predicted points: 60.69
- Average actual points: 50.35
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW10 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW11

- Train rows: 168588
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.82
- Actual score: 27.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.55 | 13.15 | 21.13 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.61 | 10.42 | 17.22 | 2.00 | 98.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.61 | 16.95 | 27.63 | 1.00 | 93.6 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.0 | 5.47 | 15.23 | 24.55 | 0.00 | 92.2 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.95 | 14.07 | 23.00 | 1.00 | 95.0 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.56 | 13.38 | 22.18 | 2.00 | 97.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.33 | 12.74 | 20.82 | 6.00 | 81.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.28 | 14.84 | 25.06 | 7.00 | 81.8 | 82.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 4.81 | 13.76 | 21.37 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.89 | 11.17 | 17.40 | 1.00 | 84.7 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.00 | 18.44 | 30.40 | 0.00 | 98.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.38 | 16.24 | 25.00 | 7.00 | 82.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.01 | 15.76 | 26.89 | 2.00 | 74.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.00 | 15.06 | 23.74 | 2.00 | 90.7 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 4.78 | 13.21 | 21.36 | 2.00 | 87.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bryan Mbeumo
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 63.77
- Actual score: 25.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Daniel Muñoz Mejía -> Nico O'Reilly (projected gain 0.82, hit 0)
- Autosub outfielders: Nico O'Reilly, Marc Guéhi, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.47 | 12.83 | 20.74 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.69 | 10.67 | 17.47 | 2.00 | 97.0 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 5.62 | 16.59 | 27.12 | 0.00 | 92.9 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 4.53 | 13.67 | 22.50 | 0.00 | 98.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.76 | 12.83 | 21.51 | 3.00 | 91.9 | 90.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 4.9 | 4.11 | 12.09 | 19.59 | 1.00 | 82.1 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 13 | 5.1 | 3.91 | 10.90 | 18.41 | 5.00 | 55.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.81 | 16.26 | 25.53 | 1.00 | 91.5 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.0 | 4.27 | 13.59 | 21.38 | 1.00 | 68.2 | 59.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.97 | 9.27 | 15.75 | 2.00 | 50.0 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 6.61 | 18.68 | 30.13 | 0.00 | 97.7 | 0.0 |
| Vice Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 5.89 | 17.00 | 27.17 | 1.00 | 93.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.44 | 16.20 | 27.03 | 2.00 | 79.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.19 | 15.37 | 23.79 | 6.00 | 88.3 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.56 | 13.03 | 20.45 | 0.00 | 84.8 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 1.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 58.13
- Actual score: 24.00
- League average score: 0.00
- Transfer: Nico O'Reilly -> Daniel Muñoz Mejía (projected gain 2.56, hit 0)
- Autosub outfielders: Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.11 | 12.17 | 19.98 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.54 | 10.44 | 17.12 | 1.00 | 94.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.97 | 13.90 | 22.02 | 1.00 | 85.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.65 | 13.56 | 22.29 | 2.00 | 95.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 4.34 | 12.99 | 21.02 | 0.00 | 87.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.38 | 12.63 | 21.00 | 0.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.44 | 9.12 | 17.89 | 0.00 | 39.2 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.58 | 15.64 | 25.17 | 1.00 | 90.1 | 54.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.04 | 13.05 | 21.25 | 6.00 | 64.6 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.02 | 10.30 | 17.46 | 1.00 | 62.1 | 10.0 |
| Captain | Captain | Declan Rice | MID | 1 | 6.9 | 5.59 | 16.06 | 26.02 | 4.00 | 96.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.40 | 15.99 | 25.09 | 1.00 | 83.2 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.2 | 5.22 | 15.77 | 26.07 | 0.00 | 76.5 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.27 | 12.98 | 22.61 | 1.00 | 54.2 | 90.0 |
| Bench 3 | Bench | Moisés Caicedo Corozo | MID | 7 | 6.1 | 2.95 | 9.17 | 15.64 | -2.00 | 51.7 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Declan Rice
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 55.25
- Actual score: 53.00
- League average score: 0.00
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 1.09, hit 0)
- Autosub outfielders: Mohamed Salah, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.05 | 11.86 | 19.58 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.67 | 15.97 | 2.00 | 90.4 | 90.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.48 | 13.44 | 21.43 | 0.00 | 86.5 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.51 | 12.99 | 21.54 | 0.00 | 94.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.33 | 12.73 | 21.01 | 1.00 | 85.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 4.28 | 12.40 | 19.90 | 14.00 | 79.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.98 | 11.80 | 19.27 | 14.00 | 74.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.17 | 12.94 | 22.19 | 2.00 | 68.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.54 | 12.89 | 21.24 | 2.00 | 78.4 | 63.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.91 | 8.93 | 15.31 | 2.00 | 44.1 | 60.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.53 | 15.90 | 26.36 | 2.00 | 87.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.24 | 15.25 | 25.45 | 3.00 | 89.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 4.60 | 13.71 | 23.83 | 4.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Mohamed Salah | MID | 12 | 14.2 | 3.94 | 12.09 | 20.65 | 1.00 | 40.7 | 45.0 |
| Bench 4 | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.67 | 8.74 | 15.60 | 0.00 | 49.1 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Antoine Semenyo
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 55.49
- Actual score: 61.00
- League average score: 0.00
- Transfer: Moisés Caicedo Corozo -> Yankuba Minteh (projected gain 2.93, hit 0)
- Autosub outfielders: Micky van de Ven, Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 12.35 | 20.10 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.71 | 10.59 | 17.25 | 3.00 | 93.6 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.94 | 14.50 | 23.26 | 0.00 | 90.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.57 | 13.39 | 21.20 | 8.00 | 92.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.18 | 12.83 | 20.93 | 6.00 | 89.0 | 90.0 |
| Bench 3 | Autosub In | Micky van de Ven | DEF | 18 | 4.8 | 2.90 | 8.70 | 14.95 | 6.00 | 53.9 | 90.0 |
| Bench 4 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.80 | 8.65 | 15.31 | 8.00 | 48.6 | 61.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.39 | 14.33 | 23.61 | 1.00 | 81.3 | 32.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.08 | 12.15 | 19.85 | 2.00 | 67.5 | 65.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.51 | 9.76 | 15.68 | 0.00 | 59.2 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 16.07 | 26.31 | 8.00 | 87.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.21 | 15.39 | 25.13 | 3.00 | 81.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.50 | 13.85 | 23.44 | 6.00 | 83.4 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 4.43 | 12.54 | 20.23 | 3.00 | 76.5 | 71.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.1 | 3.81 | 12.18 | 21.50 | 0.00 | 48.8 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 0.30 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.56
- Actual score: 52.00
- League average score: 0.00
- Transfer: Mohamed Salah -> Bruno Borges Fernandes (projected gain 8.78, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.69 | 12.78 | 20.72 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.69 | 10.46 | 17.08 | 1.00 | 92.6 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.57 | 13.63 | 22.07 | 6.00 | 91.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 13.62 | 21.96 | 1.00 | 92.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.90 | 11.29 | 18.84 | 1.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.48 | 10.46 | 17.73 | 1.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.1 | 3.08 | 9.81 | 16.63 | 0.00 | 46.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.96 | 12.23 | 21.01 | 2.00 | 64.0 | 80.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.95 | 12.04 | 20.17 | 2.00 | 64.0 | 62.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.96 | 6.58 | 11.83 | 5.00 | 34.0 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.35 | 18.31 | 30.00 | 13.00 | 101.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.49 | 15.81 | 26.23 | 2.00 | 88.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.75 | 14.35 | 23.80 | 6.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.13 | 14.09 | 23.29 | 2.00 | 87.3 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.3 | 3.77 | 11.41 | 18.42 | 2.00 | 71.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.40 -> 2.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.17
- Actual score: 47.00
- League average score: 0.00
- Transfer: Junior Kroupi -> Igor Thiago Nascimento Rodrigues (projected gain 4.47, hit 0)
- Autosub outfielders: Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.04 | 11.92 | 19.24 | 7.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.26 | 9.83 | 16.10 | 2.00 | 90.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.59 | 13.54 | 22.00 | 1.00 | 91.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.60 | 13.37 | 21.44 | 1.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.87 | 10.96 | 18.40 | 0.00 | 78.1 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.69 | 10.17 | 17.13 | 4.00 | 73.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.30 | 5.28 | 11.37 | 0.00 | 15.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.76 | 14.47 | 22.49 | 2.00 | 70.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.08 | 12.48 | 21.10 | 6.00 | 70.6 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.24 | 8.25 | 15.18 | 2.00 | 35.8 | 76.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.2 | 6.22 | 18.37 | 29.80 | 1.00 | 95.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.02 | 13.95 | 22.76 | 10.00 | 81.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.54 | 13.67 | 22.33 | 11.00 | 79.1 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 14 | 8.3 | 4.19 | 13.07 | 22.70 | 0.00 | 73.2 | 0.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 4.06 | 11.75 | 19.42 | 3.00 | 75.2 | 70.0 |

## GW18

- Train rows: 173897
- Bank: 2.90 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Phil Foden
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 57.75
- Actual score: 52.00
- League average score: 0.00
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.81, hit 0)
- Autosub outfielders: Micky van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.20 | 12.29 | 20.10 | 2.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.54 | 10.08 | 16.36 | 11.00 | 89.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.76 | 13.42 | 21.38 | 2.00 | 88.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.44 | 12.90 | 19.98 | 2.00 | 91.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.29 | 12.14 | 20.49 | 2.00 | 87.4 | 68.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.23 | 9.53 | 15.51 | 11.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.30 | 4.67 | 9.63 | 0.00 | 13.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.56 | 13.55 | 22.17 | 5.00 | 82.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.36 | 12.75 | 20.98 | 8.00 | 79.4 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 3.25 | 10.07 | 16.66 | 2.00 | 57.5 | 90.0 |
| Captain | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 5.85 | 17.76 | 29.47 | 0.00 | 82.1 | 0.0 |
| Vice Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.77 | 17.28 | 27.73 | 2.00 | 83.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.43 | 15.86 | 25.22 | 9.00 | 88.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.99 | 14.55 | 22.95 | 5.00 | 90.2 | 90.0 |
| Bench 3 | Bench | Yankuba Minteh | MID | 6 | 6.1 | 3.19 | 10.41 | 17.52 | 1.00 | 68.3 | 45.0 |

## GW19

- Train rows: 174672
- Bank: 2.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 56.49
- Actual score: 46.00
- League average score: 0.00
- Transfer: Bruno Borges Fernandes -> Bukayo Saka (projected gain 6.38, hit 0)
- Autosub outfielders: Yankuba Minteh, Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.54 | 19.04 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.84 | 11.00 | 17.81 | 2.00 | 96.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.28 | 12.58 | 19.65 | 3.00 | 94.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.29 | 12.31 | 20.13 | 2.00 | 86.5 | 90.0 |
| XI | Bench | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.80 | 11.10 | 18.52 | 0.00 | 77.3 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.71 | 10.79 | 17.35 | 6.00 | 89.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.18 | 4.02 | 7.95 | 0.00 | 14.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.40 | 13.05 | 22.06 | 2.00 | 77.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.39 | 12.26 | 20.33 | 1.00 | 77.3 | 27.0 |
| Bench 3 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 7.7 | 3.04 | 9.07 | 15.15 | 9.00 | 63.2 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 5.97 | 17.98 | 29.38 | 3.00 | 87.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.65 | 16.46 | 26.26 | 5.00 | 96.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.32 | 15.74 | 26.14 | 6.00 | 80.3 | 82.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.78 | 13.95 | 22.14 | 0.00 | 84.6 | 0.0 |
| Bench 2 | Autosub In | Yankuba Minteh | MID | 6 | 6.1 | 3.11 | 9.38 | 15.58 | 4.00 | 63.3 | 57.0 |

## GW20

- Train rows: 175452
- Bank: 1.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 54.89
- Actual score: 47.00
- League average score: 0.00
- Transfer: Yankuba Minteh -> Harry Wilson (projected gain 4.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.73 | 11.33 | 18.87 | 1.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.40 | 10.26 | 16.89 | 1.00 | 92.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.77 | 13.77 | 22.10 | 2.00 | 96.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.32 | 12.11 | 19.06 | 7.00 | 89.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.90 | 11.28 | 18.58 | 1.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.2 | 1.77 | 6.64 | 12.06 | 0.00 | 41.5 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 1.19 | 4.14 | 7.56 | 0.00 | 16.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.24 | 12.43 | 20.82 | 17.00 | 78.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.7 | 3.58 | 10.50 | 16.79 | 2.00 | 75.8 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.22 | 10.05 | 16.97 | 2.00 | 61.3 | 61.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 5.96 | 17.79 | 29.43 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.52 | 16.50 | 26.68 | 1.00 | 94.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.87 | 14.92 | 24.59 | 4.00 | 75.8 | 23.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.80 | 14.12 | 22.95 | 6.00 | 83.7 | 84.0 |
| Bench 2 | Bench | Declan Rice | MID | 1 | 7.2 | 2.98 | 9.71 | 17.01 | 17.00 | 46.8 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 57.39
- Actual score: 54.00
- League average score: 0.00
- Transfer: Marcos Senesi Barón -> James Tarkowski (projected gain 3.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.34 | 18.67 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.62 | 10.38 | 16.97 | 3.00 | 93.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.6 | 4.92 | 13.15 | 20.15 | 4.00 | 90.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.59 | 13.00 | 20.75 | 6.00 | 92.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 3.97 | 11.96 | 18.62 | 0.00 | 93.4 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 1.65 | 5.59 | 10.71 | -3.00 | 30.6 | 21.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 0.83 | 2.74 | 4.98 | 0.00 | 11.6 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.48 | 15.08 | 24.45 | 12.00 | 96.3 | 81.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.61 | 10.97 | 18.18 | 1.00 | 64.4 | 15.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.39 | 9.77 | 15.89 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.72 | 16.65 | 27.48 | 2.00 | 81.8 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.47 | 15.78 | 25.54 | 6.00 | 94.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 5.07 | 14.76 | 23.88 | 9.00 | 86.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.52 | 13.65 | 22.73 | 3.00 | 57.4 | 77.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.45 | 13.04 | 22.07 | 3.00 | 75.7 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Antoine Semenyo
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 55.82
- Actual score: 35.00
- League average score: 0.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 2.87, hit 0)
- Autosub outfielders: Marc Cucurella Saseta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.96 | 11.74 | 19.38 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 10.32 | 17.03 | 5.00 | 96.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.83 | 13.83 | 22.25 | 0.00 | 96.2 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.24 | 12.50 | 19.59 | 8.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.18 | 11.55 | 18.53 | 0.00 | 85.3 | 90.0 |
| Bench 3 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.1 | 1.62 | 5.30 | 10.16 | 5.00 | 31.6 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 0.93 | 3.14 | 5.60 | 0.00 | 11.1 | 0.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.33 | 14.91 | 23.68 | 2.00 | 92.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.34 | 12.73 | 20.08 | 3.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.45 | 9.93 | 16.11 | 2.00 | 72.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.23 | 15.81 | 25.80 | 2.00 | 92.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.87 | 14.93 | 25.07 | 1.00 | 76.0 | 45.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.85 | 13.89 | 22.81 | 2.00 | 88.3 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.37 | 13.37 | 22.94 | 1.00 | 60.7 | 33.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.29 | 12.59 | 21.20 | 3.00 | 70.9 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 56.89
- Actual score: 59.00
- League average score: 0.00
- Transfer: Daniel Muñoz Mejía -> Marcos Senesi Barón (projected gain 3.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.33 | 12.62 | 20.56 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.67 | 10.69 | 17.52 | 5.00 | 99.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.48 | 12.47 | 19.31 | 3.00 | 88.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.55 | 12.43 | 20.28 | 4.00 | 83.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.90 | 11.03 | 18.11 | 7.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.3 | 3.39 | 9.43 | 16.18 | 6.00 | 54.6 | 90.0 |
| Bench 4 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 2.82 | 8.59 | 14.13 | 4.00 | 62.5 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.56 | 15.46 | 24.88 | 2.00 | 95.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.34 | 12.30 | 19.37 | 12.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.64 | 10.41 | 16.71 | 2.00 | 74.5 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.55 | 15.97 | 25.04 | 1.00 | 93.7 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.6 | 5.65 | 15.91 | 25.75 | 8.00 | 87.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.73 | 13.42 | 22.21 | 10.00 | 80.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.14 | 12.84 | 22.14 | 2.00 | 52.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 4.03 | 11.98 | 20.84 | 1.00 | 56.0 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Morgan Rogers
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.09
- Actual score: 57.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Phil Foden -> Morgan Rogers (projected gain 5.19, hit 0)
- Autosub outfielders: James Tarkowski, Marc Cucurella Saseta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.10 | 12.01 | 19.68 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.73 | 10.99 | 18.16 | 1.00 | 102.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.53 | 12.53 | 19.50 | 8.00 | 92.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.05 | 11.82 | 19.67 | 3.00 | 78.5 | 90.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.98 | 11.71 | 19.42 | 0.00 | 93.0 | 0.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.8 | 3.86 | 11.29 | 18.37 | 2.00 | 81.6 | 90.0 |
| Bench 3 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.78 | 10.32 | 15.88 | 7.00 | 75.5 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.89 | 14.97 | 23.97 | 2.00 | 93.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.21 | 12.31 | 19.87 | 8.00 | 82.5 | 80.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 3.42 | 10.03 | 16.37 | 0.00 | 73.2 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.91 | 16.98 | 27.62 | 7.00 | 95.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.77 | 16.44 | 26.36 | 2.00 | 91.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.35 | 15.66 | 24.67 | 3.00 | 92.8 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.1 | 4.67 | 14.29 | 23.60 | 0.00 | 72.0 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.73 | 13.90 | 22.71 | 2.00 | 90.9 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 1.90 -> 2.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Declan Rice
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 57.38
- Actual score: 53.00
- League average score: 0.00
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 3.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.57 | 12.86 | 20.85 | 7.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.69 | 10.45 | 17.28 | 1.00 | 97.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.34 | 11.93 | 19.12 | 2.00 | 88.3 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 4.01 | 11.78 | 19.38 | 3.00 | 78.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.07 | 11.62 | 18.82 | 2.00 | 82.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.16 | 11.61 | 17.90 | 4.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 2.49 | 8.26 | 14.46 | 1.00 | 56.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.28 | 14.04 | 22.98 | 5.00 | 84.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.06 | 11.39 | 18.79 | 2.00 | 76.5 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 1.96 | 6.42 | 11.57 | 0.00 | 37.4 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 5.74 | 16.86 | 27.64 | 2.00 | 95.8 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.60 | 16.05 | 25.84 | 5.00 | 88.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.34 | 15.83 | 25.41 | 10.00 | 88.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.5 | 5.24 | 15.06 | 22.98 | 10.00 | 76.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.26 | 12.51 | 20.20 | 2.00 | 83.7 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 2.40 -> 1.10
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: bench_boost
- Predicted score: 77.21
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.31) beats the best remaining Bench Boost opportunity (13.95).
- League average score: 0.00
- Transfer: James Tarkowski -> Gabriel dos Santos Magalhães (projected gain 5.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.31) beats the best remaining Bench Boost opportunity (13.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.48 | 13.87 | 22.14 | 3.00 | 113.4 | 180.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.50 | 10.49 | 17.24 | 1.00 | 96.0 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.62 | 17.05 | 26.92 | 7.00 | 118.9 | 180.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.79 | 13.60 | 21.58 | 7.00 | 94.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.50 | 12.33 | 19.18 | 1.00 | 81.1 | 45.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.12 | 11.41 | 18.67 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 3.76 | 11.01 | 18.21 | 3.00 | 79.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.61 | 14.43 | 23.84 | 2.00 | 87.1 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.7 | 4.00 | 11.24 | 18.71 | 5.00 | 77.2 | 89.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.5 | 1.93 | 5.36 | 10.06 | 0.00 | 24.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.80 | 16.71 | 27.42 | 14.00 | 93.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.5 | 6.48 | 16.63 | 26.46 | 14.00 | 114.5 | 180.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.7 | 5.62 | 16.01 | 25.85 | 2.00 | 79.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.36 | 15.87 | 25.62 | 2.00 | 93.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.01 | 12.58 | 20.61 | 2.00 | 86.6 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 68.11
- Actual score: 39.00
- League average score: 0.00
- Transfer: Jean-Philippe Mateta -> João Pedro Junqueira de Jesus (projected gain 6.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.31 | 15.19 | 24.23 | 3.00 | 119.1 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.79 | 16.02 | 2.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.28 | 20.83 | 32.55 | 2.00 | 139.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 5.06 | 14.37 | 22.61 | 2.00 | 99.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.97 | 11.09 | 18.30 | 5.00 | 84.7 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.90 | 10.19 | 16.68 | 0.00 | 58.5 | 0.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.32 | 9.91 | 16.50 | 0.00 | 80.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.83 | 16.17 | 26.00 | 7.00 | 85.6 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.08 | 14.69 | 24.19 | 2.00 | 85.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.19 | 12.51 | 20.62 | 4.00 | 82.2 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.5 | 7.10 | 20.36 | 31.98 | 4.00 | 129.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 6.20 | 17.63 | 28.81 | 4.00 | 98.7 | 86.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.44 | 15.91 | 26.59 | 2.00 | 79.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.35 | 15.16 | 24.81 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Harry Wilson | MID | 10 | 6.0 | 3.61 | 11.04 | 18.80 | 8.00 | 71.3 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 64.91
- Actual score: 78.00
- League average score: 0.00
- Transfer: Marc Cucurella Saseta -> Virgil van Dijk (projected gain 3.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.38 | 12.56 | 20.60 | 3.00 | 97.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.55 | 10.22 | 16.61 | 0.00 | 92.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.89 | 16.98 | 27.29 | 9.00 | 110.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.49 | 14.99 | 24.10 | 7.00 | 91.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.69 | 13.77 | 22.11 | 6.00 | 93.1 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.35 | 11.84 | 19.19 | 4.00 | 88.2 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.84 | 11.26 | 17.70 | 0.00 | 92.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.51 | 16.61 | 26.69 | 2.00 | 85.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.40 | 15.20 | 24.76 | 6.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 4.41 | 13.97 | 22.36 | 7.00 | 87.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.07 | 17.77 | 28.86 | 8.00 | 92.5 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.13 | 17.75 | 28.31 | 5.00 | 107.2 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.41 | 15.83 | 26.51 | 13.00 | 81.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.25 | 14.79 | 23.98 | 2.00 | 86.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.55 | 13.31 | 21.27 | 12.00 | 87.8 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 66.12
- Actual score: 71.00
- League average score: 0.00
- Transfer: Morgan Rogers -> Bryan Mbeumo (projected gain 0.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.09 | 12.56 | 20.71 | 7.00 | 97.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.41 | 9.93 | 16.28 | 2.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.67 | 17.12 | 27.43 | 11.00 | 112.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.65 | 15.87 | 25.39 | 1.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.99 | 14.23 | 22.76 | 1.00 | 94.6 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.07 | 11.61 | 18.66 | 11.00 | 91.2 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.47 | 9.94 | 15.74 | -3.00 | 87.9 | 37.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.59 | 16.47 | 27.13 | 19.00 | 84.3 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.08 | 14.95 | 24.20 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.98 | 14.69 | 23.41 | 4.00 | 90.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.86 | 19.59 | 31.44 | 7.00 | 103.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 6.04 | 17.83 | 29.53 | 8.00 | 93.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 5.29 | 16.17 | 26.06 | 3.00 | 98.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.01 | 14.60 | 23.47 | 1.00 | 76.3 | 76.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 5.9 | 4.92 | 13.79 | 22.20 | 0.00 | 82.3 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 73.56
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Micky van de Ven -> James Hill (projected gain 0.10, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.29 | 12.53 | 20.55 | 7.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.60 | 10.34 | 16.81 | 6.00 | 91.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.34 | 15.37 | 24.88 | 2.00 | 89.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.21 | 15.35 | 25.54 | 9.00 | 98.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.52 | 12.95 | 21.01 | 2.00 | 90.5 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.26 | 12.02 | 19.38 | 10.00 | 92.4 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.1 | 4.24 | 11.85 | 19.47 | 8.00 | 88.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.96 | 19.66 | 32.02 | 2.00 | 98.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.33 | 14.79 | 23.77 | 6.00 | 89.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.97 | 14.51 | 23.70 | 6.00 | 87.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 7.00 | 20.09 | 32.01 | 2.00 | 105.6 | 74.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.56 | 19.61 | 31.92 | 10.00 | 100.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.72 | 13.87 | 23.03 | 2.00 | 71.0 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.66 | 13.79 | 23.35 | 3.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Harry Wilson | MID | 10 | 6.0 | 3.27 | 9.89 | 16.67 | 3.00 | 49.9 | 90.0 |