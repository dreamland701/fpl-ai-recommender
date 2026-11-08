# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW10
- Simulated weeks: GW11-GW30
- Total predicted points: 1188.94
- Total actual points: 987.00
- Average predicted points: 59.45
- Average actual points: 49.35
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
- Predicted score: 64.38
- Actual score: 27.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.74 | 13.70 | 21.99 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.76 | 10.83 | 17.85 | 2.00 | 98.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.73 | 17.21 | 28.18 | 1.00 | 93.6 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.0 | 5.66 | 15.78 | 25.41 | 0.00 | 92.2 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 5.10 | 14.48 | 23.63 | 1.00 | 95.0 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.75 | 13.93 | 23.04 | 2.00 | 97.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.52 | 13.28 | 21.68 | 6.00 | 81.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.39 | 15.11 | 25.60 | 7.00 | 81.8 | 82.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 4.92 | 14.02 | 21.92 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 4.04 | 11.58 | 18.03 | 1.00 | 84.7 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.12 | 18.71 | 30.95 | 0.00 | 98.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.49 | 16.50 | 25.54 | 7.00 | 82.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.01 | 15.76 | 26.89 | 2.00 | 74.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.12 | 15.33 | 24.28 | 2.00 | 90.7 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 4.97 | 13.76 | 22.22 | 2.00 | 87.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.10
- Actual score: 28.00
- League average score: 0.00
- Transfer: Daniel Muñoz Mejía -> Virgil van Dijk (projected gain 0.82, hit 0)
- Autosub outfielders: Virgil van Dijk, Marc Guéhi, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.60 | 11.33 | 19.24 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.62 | 9.17 | 15.97 | 2.00 | 97.0 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.62 | 15.09 | 25.62 | 0.00 | 92.9 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 3.45 | 12.17 | 21.00 | 0.00 | 98.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.89 | 11.33 | 20.01 | 3.00 | 91.9 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 5.9 | 3.09 | 10.03 | 17.82 | 3.00 | 86.1 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 13 | 5.1 | 3.04 | 9.40 | 16.91 | 5.00 | 55.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.81 | 14.76 | 24.03 | 1.00 | 91.5 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.0 | 3.28 | 12.09 | 19.88 | 1.00 | 68.2 | 59.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 1.89 | 7.77 | 14.25 | 2.00 | 50.0 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 5.62 | 17.18 | 28.63 | 0.00 | 97.7 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 12 | 14.2 | 5.44 | 16.20 | 27.03 | 2.00 | 79.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.89 | 15.50 | 25.67 | 1.00 | 93.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.20 | 13.87 | 22.29 | 6.00 | 88.3 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 3.69 | 11.53 | 18.95 | 0.00 | 84.8 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 54.77
- Actual score: 21.00
- League average score: 0.00
- Transfer: Virgil van Dijk -> Daniel Muñoz Mejía (projected gain 2.00, hit 0)
- Autosub outfielders: Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.91 | 11.39 | 19.17 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.97 | 8.94 | 15.62 | 1.00 | 94.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.77 | 13.13 | 21.21 | 1.00 | 85.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.45 | 12.79 | 21.48 | 2.00 | 95.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.18 | 11.86 | 20.19 | 0.00 | 77.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 3.76 | 11.49 | 19.52 | 0.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.20 | 8.04 | 16.87 | 0.00 | 39.2 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.34 | 14.57 | 24.15 | 1.00 | 90.1 | 54.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.80 | 11.98 | 20.22 | 6.00 | 64.6 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.44 | 8.80 | 15.96 | 1.00 | 62.1 | 10.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.2 | 5.22 | 15.77 | 26.07 | 0.00 | 76.5 | 0.0 |
| Captain | Captain | Declan Rice | MID | 1 | 6.9 | 5.35 | 14.99 | 25.00 | 4.00 | 96.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.62 | 14.49 | 23.59 | 1.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.03 | 11.91 | 21.59 | 1.00 | 54.2 | 90.0 |
| Bench 2 | Autosub In | Moisés Caicedo Corozo | MID | 7 | 6.1 | 2.75 | 8.39 | 14.83 | -2.00 | 51.7 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Bryan Mbeumo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 51.66
- Actual score: 54.00
- League average score: 0.00
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 1.11, hit 0)
- Autosub outfielders: Marc Guéhi, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.87 | 11.36 | 19.19 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.91 | 8.34 | 14.47 | 2.00 | 90.4 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.32 | 12.50 | 21.14 | 0.00 | 94.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.15 | 12.24 | 20.61 | 1.00 | 85.9 | 90.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.02 | 12.11 | 19.93 | 0.00 | 86.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 4.10 | 11.91 | 19.50 | 14.00 | 79.8 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.1 | 3.80 | 11.30 | 18.87 | 14.00 | 74.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.88 | 12.24 | 21.51 | 2.00 | 68.8 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.25 | 12.19 | 20.56 | 2.00 | 78.4 | 63.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.45 | 7.59 | 13.81 | 2.00 | 44.1 | 60.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.0 | 4.95 | 14.54 | 24.76 | 3.00 | 89.6 | 82.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 4.90 | 14.40 | 25.15 | 2.00 | 87.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 4.32 | 13.00 | 23.15 | 4.00 | 72.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 3.94 | 12.09 | 20.65 | 1.00 | 40.7 | 45.0 |
| Bench 3 | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.49 | 8.25 | 15.20 | 0.00 | 49.1 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Antoine Semenyo
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 52.69
- Actual score: 61.00
- League average score: 0.00
- Transfer: Moisés Caicedo Corozo -> Yankuba Minteh (projected gain 3.76, hit 0)
- Autosub outfielders: Marcos Senesi Barón, Micky van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.96 | 12.10 | 19.94 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.30 | 9.48 | 15.75 | 3.00 | 93.6 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.78 | 14.25 | 23.10 | 0.00 | 90.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.41 | 13.15 | 21.04 | 8.00 | 92.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.01 | 12.59 | 20.77 | 6.00 | 89.0 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.63 | 8.40 | 15.15 | 8.00 | 48.6 | 61.0 |
| Bench 4 | Autosub In | Micky van de Ven | DEF | 18 | 4.8 | 2.49 | 7.60 | 13.45 | 6.00 | 53.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.18 | 13.97 | 23.08 | 1.00 | 81.3 | 32.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.87 | 11.79 | 19.32 | 2.00 | 67.5 | 65.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.09 | 8.66 | 14.18 | 0.00 | 59.2 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.06 | 15.35 | 26.16 | 8.00 | 87.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.00 | 15.03 | 24.60 | 3.00 | 81.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.29 | 13.49 | 22.91 | 6.00 | 83.4 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 4.26 | 12.30 | 20.07 | 3.00 | 76.5 | 71.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.1 | 3.81 | 12.18 | 21.50 | 0.00 | 48.8 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 0.30 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.64
- Actual score: 52.00
- League average score: 0.00
- Transfer: Mohamed Salah -> Bruno Borges Fernandes (projected gain 10.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.62 | 12.74 | 20.81 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.60 | 15.74 | 1.00 | 92.6 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.49 | 13.60 | 22.15 | 6.00 | 91.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.56 | 13.59 | 22.05 | 1.00 | 92.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.58 | 10.43 | 17.50 | 1.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.40 | 10.42 | 17.81 | 1.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.1 | 3.00 | 9.78 | 16.71 | 0.00 | 46.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.87 | 11.95 | 20.44 | 2.00 | 64.0 | 80.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.86 | 11.76 | 19.60 | 2.00 | 64.0 | 62.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.64 | 5.72 | 10.49 | 5.00 | 34.0 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.05 | 18.44 | 30.77 | 13.00 | 101.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.18 | 15.94 | 27.00 | 2.00 | 88.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.66 | 14.08 | 23.23 | 6.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.04 | 13.82 | 22.72 | 2.00 | 87.3 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.3 | 3.69 | 11.38 | 18.50 | 2.00 | 71.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.40 -> 2.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.81
- Actual score: 47.00
- League average score: 0.00
- Transfer: Junior Kroupi -> Igor Thiago Nascimento Rodrigues (projected gain 3.99, hit 0)
- Autosub outfielders: Micky van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.06 | 11.99 | 19.43 | 7.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.99 | 9.12 | 15.00 | 2.00 | 90.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.60 | 13.61 | 22.19 | 1.00 | 91.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.62 | 13.44 | 21.62 | 1.00 | 87.2 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.60 | 10.25 | 17.30 | 0.00 | 78.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 10.24 | 17.32 | 4.00 | 73.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.32 | 5.34 | 11.55 | 0.00 | 15.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.71 | 14.05 | 21.81 | 2.00 | 70.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.02 | 12.07 | 20.41 | 6.00 | 70.6 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.19 | 7.84 | 14.50 | 2.00 | 35.8 | 76.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.2 | 6.21 | 18.81 | 30.85 | 1.00 | 95.6 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.97 | 13.53 | 22.08 | 10.00 | 81.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.49 | 13.26 | 21.65 | 11.00 | 79.1 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 14 | 8.3 | 4.13 | 12.66 | 22.02 | 0.00 | 73.2 | 0.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 4.07 | 11.82 | 19.60 | 3.00 | 75.2 | 70.0 |

## GW18

- Train rows: 173897
- Bank: 2.90 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Phil Foden
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 57.15
- Actual score: 42.00
- League average score: 0.00
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 8.37, hit 0)
- Autosub outfielders: Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 12.36 | 20.22 | 2.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.33 | 9.48 | 15.42 | 11.00 | 89.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.76 | 13.49 | 21.51 | 2.00 | 88.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.23 | 12.30 | 19.04 | 2.00 | 91.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.29 | 12.21 | 20.62 | 2.00 | 87.4 | 68.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.02 | 8.93 | 14.57 | 11.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.30 | 4.74 | 9.76 | 0.00 | 13.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.43 | 12.95 | 21.39 | 5.00 | 82.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.23 | 12.15 | 20.19 | 8.00 | 79.4 | 68.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 7.8 | 3.11 | 9.48 | 15.87 | 2.00 | 57.5 | 90.0 |
| Captain | Bench | Bruno Borges Fernandes | MID | 14 | 9.3 | 5.91 | 18.27 | 30.32 | 0.00 | 82.1 | 0.0 |
| Vice Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.83 | 17.79 | 28.58 | 2.00 | 83.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.30 | 15.27 | 24.44 | 9.00 | 88.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.86 | 13.95 | 22.16 | 5.00 | 90.2 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.1 | 3.19 | 10.47 | 17.64 | 1.00 | 68.3 | 45.0 |

## GW19

- Train rows: 174672
- Bank: 2.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 55.55
- Actual score: 46.00
- League average score: 0.00
- Transfer: Bruno Borges Fernandes -> Bukayo Saka (projected gain 6.71, hit 0)
- Autosub outfielders: Yankuba Minteh, Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.60 | 19.13 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.65 | 10.50 | 17.00 | 2.00 | 96.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.29 | 12.37 | 20.21 | 2.00 | 86.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.09 | 12.08 | 18.85 | 3.00 | 94.1 | 90.0 |
| XI | Bench | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.80 | 11.17 | 18.60 | 0.00 | 77.3 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.52 | 10.28 | 16.54 | 6.00 | 89.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.18 | 4.08 | 8.04 | 0.00 | 14.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.23 | 12.55 | 21.29 | 2.00 | 77.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.22 | 11.75 | 19.56 | 1.00 | 77.3 | 27.0 |
| Bench 3 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 7.7 | 2.87 | 8.56 | 14.38 | 9.00 | 63.2 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 6.01 | 18.38 | 30.08 | 3.00 | 87.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 5.36 | 16.14 | 26.85 | 6.00 | 80.3 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.48 | 15.95 | 25.49 | 5.00 | 96.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.61 | 13.45 | 21.37 | 0.00 | 84.6 | 0.0 |
| Bench 2 | Autosub In | Yankuba Minteh | MID | 6 | 6.1 | 3.11 | 9.44 | 15.67 | 4.00 | 63.3 | 57.0 |

## GW20

- Train rows: 175452
- Bank: 1.10 -> 2.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 54.76
- Actual score: 47.00
- League average score: 0.00
- Transfer: Declan Rice -> Harry Wilson (projected gain 4.50, hit 0)
- Autosub outfielders: João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 11.38 | 18.93 | 1.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.24 | 9.84 | 16.22 | 1.00 | 92.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.79 | 13.82 | 22.15 | 2.00 | 96.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.16 | 11.69 | 18.39 | 7.00 | 89.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.75 | 10.85 | 17.91 | 1.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.2 | 1.79 | 6.68 | 12.12 | 0.00 | 41.5 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 1.21 | 4.18 | 7.62 | 0.00 | 16.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.06 | 12.07 | 20.26 | 17.00 | 78.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.7 | 3.41 | 10.15 | 16.23 | 2.00 | 75.8 | 86.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.04 | 9.69 | 16.41 | 2.00 | 61.3 | 61.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 6.06 | 17.98 | 29.85 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.35 | 16.14 | 26.12 | 1.00 | 94.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.97 | 15.11 | 25.01 | 4.00 | 75.8 | 23.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.83 | 14.16 | 23.01 | 6.00 | 83.7 | 84.0 |
| XI | Bench | Yankuba Minteh | MID | 6 | 6.0 | 3.57 | 9.82 | 16.26 | 0.00 | 62.1 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 2.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 55.99
- Actual score: 64.00
- League average score: 0.00
- Transfer: Yankuba Minteh -> Bruno Guimarães Rodriguez Moura (projected gain 3.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.31 | 18.62 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.48 | 9.99 | 16.35 | 3.00 | 93.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.3 | 4.59 | 12.97 | 20.70 | 6.00 | 92.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 3.83 | 11.58 | 17.99 | 0.00 | 93.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.47 | 9.58 | 16.56 | 6.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 1.64 | 5.56 | 10.65 | -3.00 | 30.6 | 21.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 0.82 | 2.71 | 4.93 | 0.00 | 11.6 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.45 | 14.85 | 24.22 | 12.00 | 96.3 | 81.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.57 | 10.74 | 17.95 | 1.00 | 64.4 | 15.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.35 | 9.54 | 15.65 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.70 | 16.68 | 27.52 | 2.00 | 81.8 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.44 | 15.55 | 25.31 | 6.00 | 94.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 5.06 | 14.73 | 23.83 | 9.00 | 86.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.3 | 4.50 | 13.68 | 22.78 | 3.00 | 57.4 | 77.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.80 | 13.27 | 21.61 | 11.00 | 89.2 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 1.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Guimarães Rodriguez Moura
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Guimarães Rodriguez Moura
- Chip used: none
- Predicted score: 56.73
- Actual score: 33.00
- League average score: 0.00
- Transfer: Daniel Muñoz Mejía -> Gabriel dos Santos Magalhães (projected gain 3.65, hit 0)
- Autosub outfielders: Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.93 | 11.68 | 19.22 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.22 | 9.97 | 16.42 | 5.00 | 96.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.3 | 4.79 | 13.78 | 22.09 | 0.00 | 96.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 4.65 | 13.29 | 20.14 | 8.00 | 73.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.04 | 11.19 | 17.93 | 0.00 | 85.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.73 | 11.11 | 17.96 | 3.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 1.59 | 5.24 | 10.00 | 5.00 | 31.6 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.34 | 14.79 | 23.61 | 2.00 | 92.6 | 90.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.45 | 9.82 | 16.04 | 2.00 | 72.7 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 2.82 | 9.27 | 16.04 | 8.00 | 45.9 | 73.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.24 | 15.70 | 25.72 | 2.00 | 92.8 | 90.0 |
| Captain | Captain | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.1 | 5.59 | 15.53 | 24.96 | 3.00 | 96.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.75 | 14.82 | 24.94 | 1.00 | 76.0 | 45.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.8 | 4.81 | 13.83 | 22.65 | 2.00 | 88.3 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.25 | 13.26 | 22.81 | 1.00 | 60.7 | 33.0 |

## GW23

- Train rows: 177836
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 56.73
- Actual score: 49.00
- League average score: 0.00
- Transfer: Marc Cucurella Saseta -> James Tarkowski (projected gain 1.93, hit 0)
- Autosub outfielders: Jean-Philippe Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.28 | 12.52 | 20.32 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.54 | 10.34 | 16.92 | 5.00 | 99.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.08 | 14.66 | 22.27 | 1.00 | 81.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.50 | 12.33 | 20.03 | 4.00 | 83.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.35 | 12.12 | 18.71 | 3.00 | 88.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.77 | 10.68 | 17.50 | 7.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.3 | 3.35 | 9.32 | 15.94 | 6.00 | 54.6 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.50 | 15.50 | 24.96 | 2.00 | 95.5 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 3.32 | 10.72 | 17.93 | 12.00 | 63.8 | 84.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 7.6 | 3.58 | 10.45 | 16.79 | 2.00 | 74.5 | 84.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.6 | 5.59 | 15.95 | 25.83 | 8.00 | 87.1 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.28 | 15.60 | 25.11 | 0.00 | 92.4 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.68 | 13.32 | 21.97 | 10.00 | 80.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.11 | 12.64 | 21.70 | 2.00 | 52.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 4.01 | 11.78 | 20.40 | 1.00 | 56.0 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Morgan Rogers
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 57.33
- Actual score: 55.00
- League average score: 0.00
- Transfer: Phil Foden -> Morgan Rogers (projected gain 5.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.05 | 11.83 | 19.38 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.60 | 10.62 | 17.53 | 1.00 | 102.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.80 | 13.99 | 22.45 | 8.00 | 79.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.40 | 12.16 | 18.87 | 8.00 | 92.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.01 | 11.65 | 19.38 | 3.00 | 78.5 | 90.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.85 | 11.33 | 18.79 | 0.00 | 93.0 | 0.0 |
| Bench 2 | Bench | James Tarkowski | DEF | 9 | 5.8 | 3.81 | 11.11 | 18.08 | 2.00 | 81.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.92 | 15.12 | 24.20 | 2.00 | 93.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 4.40 | 12.27 | 20.17 | 10.00 | 74.9 | 45.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 3.45 | 10.18 | 16.60 | 0.00 | 73.2 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.94 | 17.12 | 27.85 | 7.00 | 95.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.80 | 16.58 | 26.59 | 2.00 | 91.7 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.1 | 4.53 | 13.91 | 22.67 | 0.00 | 72.0 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.68 | 13.73 | 22.42 | 2.00 | 90.9 | 90.0 |
| Bench 4 | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.3 | 3.10 | 10.21 | 18.36 | 0.00 | 50.4 | 0.0 |

## GW25

- Train rows: 179450
- Bank: 1.90 -> 4.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.40
- Actual score: 54.00
- League average score: 0.00
- Transfer: Bukayo Saka -> Declan Rice (projected gain 7.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.49 | 12.59 | 20.53 | 7.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.55 | 10.06 | 16.57 | 1.00 | 97.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.0 | 5.74 | 15.84 | 25.24 | 6.00 | 86.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.19 | 11.54 | 18.41 | 2.00 | 88.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.92 | 11.51 | 19.06 | 3.00 | 78.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.98 | 11.35 | 18.50 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 2.35 | 7.87 | 13.76 | 1.00 | 56.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.39 | 14.23 | 23.31 | 5.00 | 84.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.65 | 13.20 | 21.06 | 8.00 | 66.8 | 74.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 2.07 | 6.62 | 11.91 | 0.00 | 37.4 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 5.85 | 17.06 | 27.98 | 2.00 | 95.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.71 | 16.25 | 26.17 | 5.00 | 88.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.45 | 16.02 | 25.75 | 10.00 | 88.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.18 | 12.24 | 19.88 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 2.41 | 8.38 | 15.84 | 11.00 | 28.6 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 4.50 -> 1.90
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: bench_boost
- Predicted score: 77.34
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.93) beats the best remaining Bench Boost opportunity (13.74).
- League average score: 0.00
- Transfer: Bruno Guimarães Rodriguez Moura -> Bruno Borges Fernandes (projected gain 4.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.93) beats the best remaining Bench Boost opportunity (13.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.36 | 13.59 | 21.81 | 3.00 | 113.4 | 180.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.36 | 10.09 | 16.48 | 1.00 | 96.0 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.66 | 17.19 | 27.21 | 7.00 | 118.9 | 180.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.68 | 13.32 | 21.25 | 7.00 | 94.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.98 | 11.01 | 17.92 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Bench Boost | James Tarkowski | DEF | 9 | 5.8 | 3.87 | 10.95 | 18.08 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 3.61 | 10.61 | 17.45 | 3.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.31 | 14.81 | 23.43 | 10.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.66 | 14.57 | 24.14 | 2.00 | 87.1 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.5 | 1.98 | 5.50 | 10.36 | 0.00 | 24.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.8 | 5.85 | 16.85 | 27.72 | 14.00 | 93.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.5 | 6.53 | 16.78 | 26.75 | 14.00 | 114.5 | 180.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.41 | 16.01 | 25.92 | 2.00 | 93.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.7 | 5.53 | 15.27 | 24.84 | 2.00 | 79.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 3.90 | 12.30 | 20.28 | 2.00 | 86.6 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 1.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Declan Rice
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 69.10
- Actual score: 37.00
- League average score: 0.00
- Transfer: Harry Wilson -> Enzo Fernández (projected gain 4.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.17 | 14.95 | 23.90 | 3.00 | 119.1 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.14 | 9.32 | 15.19 | 2.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 7.32 | 20.97 | 32.75 | 2.00 | 139.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.92 | 14.13 | 22.28 | 2.00 | 99.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.81 | 10.63 | 17.47 | 5.00 | 84.7 | 90.0 |
| Bench 2 | Bench | James Tarkowski | DEF | 9 | 5.8 | 3.70 | 10.50 | 17.34 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.16 | 9.45 | 15.67 | 0.00 | 80.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.87 | 16.31 | 26.19 | 7.00 | 85.6 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.12 | 14.83 | 24.38 | 2.00 | 85.5 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 1.70 | 4.98 | 9.26 | 0.00 | 16.3 | 0.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.5 | 7.13 | 20.50 | 32.17 | 4.00 | 129.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.9 | 6.23 | 17.77 | 29.00 | 4.00 | 98.7 | 86.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 5.49 | 15.46 | 25.13 | 2.00 | 88.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.32 | 15.39 | 26.01 | 2.00 | 79.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 5.39 | 15.30 | 25.01 | 2.00 | 84.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 63.98
- Actual score: 67.00
- League average score: 0.00
- Transfer: James Tarkowski -> Virgil van Dijk (projected gain 3.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.26 | 12.34 | 20.21 | 3.00 | 97.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.67 | 15.69 | 0.00 | 92.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.88 | 17.04 | 27.16 | 9.00 | 110.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.37 | 14.77 | 23.71 | 7.00 | 91.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.57 | 13.55 | 21.72 | 6.00 | 93.1 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.17 | 11.28 | 18.27 | 4.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.66 | 10.70 | 16.77 | 0.00 | 92.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.49 | 16.68 | 26.57 | 2.00 | 85.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.39 | 15.26 | 24.64 | 6.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.5 | 0.93 | 3.84 | 7.08 | 0.00 | 16.6 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.05 | 17.83 | 28.74 | 8.00 | 92.5 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 6.11 | 17.81 | 28.19 | 5.00 | 107.2 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 5.25 | 15.45 | 26.27 | 13.00 | 81.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.23 | 14.86 | 23.86 | 2.00 | 86.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.9 | 4.25 | 13.54 | 22.06 | 1.00 | 83.2 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 65.38
- Actual score: 71.00
- League average score: 0.00
- Transfer: Jean-Philippe Mateta -> Jarrod Bowen (projected gain 3.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 12.32 | 20.23 | 7.00 | 97.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.20 | 9.33 | 15.28 | 2.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 17.01 | 27.06 | 11.00 | 112.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.56 | 15.63 | 24.90 | 1.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.90 | 13.99 | 22.28 | 1.00 | 94.6 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.85 | 11.01 | 17.67 | 11.00 | 91.2 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.26 | 9.34 | 14.74 | -3.00 | 87.9 | 37.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.58 | 16.35 | 26.76 | 19.00 | 84.3 | 84.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.06 | 14.84 | 23.83 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.96 | 14.58 | 23.04 | 4.00 | 90.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.84 | 19.48 | 31.08 | 7.00 | 103.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 5.99 | 17.75 | 29.61 | 8.00 | 93.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 5.27 | 16.05 | 25.70 | 3.00 | 98.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.72 | 13.52 | 21.90 | 1.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Enzo Fernández | MID | 7 | 6.8 | 3.57 | 11.45 | 18.99 | 4.00 | 75.4 | 78.0 |

## GW30

- Train rows: 183541
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 72.46
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.95) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Morgan Rogers -> Crysencio Summerville (projected gain 0.83, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.95) beats the best remaining Triple Captain opportunity (0.00).
- Autosub outfielders: Enzo Fernández.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.16 | 12.17 | 20.02 | 7.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.73 | 15.82 | 6.00 | 91.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.22 | 15.02 | 24.34 | 2.00 | 89.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.16 | 14.95 | 24.86 | 9.00 | 98.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.39 | 12.60 | 20.48 | 2.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.02 | 11.41 | 18.39 | 10.00 | 92.4 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 2.05 | 6.64 | 11.39 | 0.00 | 59.7 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.90 | 19.26 | 31.34 | 2.00 | 98.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.28 | 14.39 | 23.08 | 6.00 | 89.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.92 | 14.11 | 23.02 | 6.00 | 87.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.54 | 19.72 | 32.23 | 10.00 | 100.6 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 6.95 | 19.69 | 31.33 | 2.00 | 105.6 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.61 | 13.39 | 22.67 | 3.00 | 81.3 | 90.0 |
| XI | Bench | Crysencio Summerville | MID | 19 | 5.7 | 4.43 | 12.94 | 20.79 | 0.00 | 89.6 | 0.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 7 | 6.7 | 4.07 | 12.11 | 19.86 | 2.00 | 78.4 | 90.0 |