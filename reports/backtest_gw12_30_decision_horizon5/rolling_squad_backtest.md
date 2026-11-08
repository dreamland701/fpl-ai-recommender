# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1158.02
- Total actual points: 996.00
- Average predicted points: 60.95
- Average actual points: 52.42
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 169340
- Bank: 100.00 -> 3.30
- Free transfers: 1 -> 2
- Captain: Semenyo
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 62.29
- Actual score: 36.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Mateta, Thiago, O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.31 | 11.92 | 18.46 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 95.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.54 | 12.48 | 20.47 | 14.00 | 79.3 | 90.0 |
| Bench 4 | Autosub In | O'Reilly | DEF | 13 | 4.9 | 4.04 | 11.99 | 19.06 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.60 | 15.64 | 24.41 | 1.00 | 88.7 | 75.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 8.0 | 4.37 | 13.84 | 21.93 | 1.00 | 69.4 | 59.0 |
| Bench 3 | Autosub In | Thiago | FWD | 5 | 6.2 | 4.35 | 12.53 | 19.81 | 4.00 | 84.2 | 90.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 96.6 | 0.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 92.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 4.97 | 15.04 | 23.65 | 6.00 | 85.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 4.78 | 13.63 | 21.89 | 2.00 | 86.5 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.48 | 13.18 | 20.88 | 0.00 | 81.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 3.30 -> 2.30
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.48
- Actual score: 44.00
- Transfer: O'Reilly -> Virgil (projected gain 3.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.75 | 11.08 | 17.59 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 94.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 4.97 | 13.81 | 22.20 | 1.00 | 87.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 93.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.27 | 12.40 | 19.84 | 0.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 12 | 6.0 | 4.02 | 12.04 | 19.96 | 6.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.5 | 2.34 | 9.58 | 19.00 | 0.00 | 37.3 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.22 | 14.59 | 23.27 | 1.00 | 85.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.04 | 13.96 | 21.86 | 13.00 | 80.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.14 | 13.14 | 21.28 | 6.00 | 65.4 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.36 | 15.90 | 25.10 | 1.00 | 82.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 93.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 4.45 | 13.26 | 21.80 | 11.00 | 81.9 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 4.12 | 12.76 | 22.01 | 1.00 | 53.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 2.80 | 9.03 | 15.50 | -2.00 | 47.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 2.30 -> 3.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.33
- Actual score: 40.00
- Transfer: Virgil -> O'Reilly (projected gain 1.30, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.91 | 11.03 | 17.36 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 92.3 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 93.4 | 0.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 4.47 | 12.92 | 20.71 | 14.00 | 82.2 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.1 | 4.45 | 12.82 | 20.43 | 0.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 4.01 | 12.23 | 19.53 | 0.00 | 83.8 | 0.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.4 | 2.13 | 7.72 | 15.40 | 0.00 | 27.3 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.05 | 15.65 | 25.20 | 1.00 | 88.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.78 | 13.23 | 21.01 | 2.00 | 81.1 | 63.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.11 | 12.66 | 21.16 | 2.00 | 67.0 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.27 | 15.47 | 25.56 | 3.00 | 88.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.47 | 15.47 | 24.93 | 2.00 | 85.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.01 | 14.52 | 23.67 | 4.00 | 87.8 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.78 | 14.02 | 23.66 | 4.00 | 73.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.0 | 2.52 | 8.33 | 14.98 | 0.00 | 47.0 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 3.20 -> 4.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.17
- Actual score: 70.00
- Transfer: Gabriel -> Guéhi (projected gain 12.47, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.00 | 11.73 | 18.63 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 93.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 96.1 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.31 | 11.89 | 19.02 | 6.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.55 | 8.26 | 15.61 | 8.00 | 46.5 | 61.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.72 | 8.12 | 13.97 | 6.00 | 50.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.42 | 13.89 | 22.48 | 1.00 | 77.7 | 32.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.32 | 12.74 | 20.67 | 2.00 | 69.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.10 | 12.17 | 19.79 | 2.00 | 67.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.32 | 15.51 | 25.22 | 3.00 | 82.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.29 | 15.27 | 24.54 | 18.00 | 84.5 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.44 | 15.12 | 24.34 | 8.00 | 83.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.63 | 14.43 | 24.17 | 6.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 5.9 | 1.22 | 5.26 | 10.91 | 0.00 | 18.8 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 4.40 -> 1.80
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 58.65
- Actual score: 61.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Caicedo -> Foden (projected gain 7.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.34 | 11.61 | 18.01 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 91.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 94.8 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.15 | 11.81 | 18.95 | 6.00 | 81.4 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.86 | 11.10 | 18.37 | 1.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.1 | 3.36 | 10.73 | 17.91 | 0.00 | 49.6 | 0.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 3.40 | 10.44 | 17.68 | 1.00 | 68.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.55 | 13.78 | 22.21 | 2.00 | 74.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.21 | 12.71 | 20.96 | 2.00 | 67.6 | 62.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.4 | 3.86 | 11.86 | 20.11 | 2.00 | 61.1 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 99.0 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.4 | 5.11 | 15.66 | 24.96 | 11.00 | 72.6 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.30 | 15.02 | 24.64 | 2.00 | 85.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.82 | 14.49 | 23.70 | 6.00 | 83.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.93 | 13.96 | 23.10 | 2.00 | 85.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.80 -> 1.90
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.71
- Actual score: 56.00
- Transfer: Muñoz -> Virgil (projected gain 4.70, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.30 | 17.83 | 7.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.34 | 9.38 | 14.76 | 2.00 | 88.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.24 | 12.82 | 21.00 | 2.00 | 88.2 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.06 | 11.50 | 18.19 | 6.00 | 79.3 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 5.0 | 3.72 | 10.54 | 17.96 | 4.00 | 72.7 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.7 | 3.71 | 10.48 | 17.34 | 0.00 | 74.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.60 | 14.57 | 23.21 | 2.00 | 66.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.72 | 11.78 | 20.11 | 6.00 | 67.8 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.9 | 2.55 | 9.27 | 17.20 | 2.00 | 40.7 | 76.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 94.2 | 45.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 6.22 | 18.57 | 28.95 | 3.00 | 83.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.21 | 14.53 | 23.74 | 10.00 | 84.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.42 | 13.47 | 22.76 | 11.00 | 78.5 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.12 | 13.09 | 22.97 | 0.00 | 72.8 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 1.90 -> 3.00
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.84
- Actual score: 41.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mbeumo -> Rogers (projected gain 3.32, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.58 | 14.89 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 4.14 | 12.83 | 20.64 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.38 | 12.41 | 19.86 | 2.00 | 89.0 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 4.25 | 12.37 | 19.72 | 1.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.26 | 9.57 | 15.42 | 11.00 | 80.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.39 | 12.92 | 20.76 | 5.00 | 79.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.20 | 12.08 | 19.71 | 8.00 | 77.0 | 68.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.8 | 3.40 | 10.28 | 17.03 | 2.00 | 59.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.00 | 18.03 | 28.76 | 2.00 | 86.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.68 | 17.07 | 28.11 | 0.00 | 80.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.23 | 15.41 | 24.86 | 9.00 | 88.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.92 | 14.59 | 23.58 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.1 | 4.87 | 14.23 | 22.73 | 1.00 | 89.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 3.00 -> 1.70
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.31
- Actual score: 31.00
- Transfer: Mateta -> Ekitiké (projected gain 7.10, hit 0)
- Autosub outfielders: O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.81 | 10.83 | 17.14 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 93.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.05 | 12.55 | 19.86 | 3.00 | 94.4 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.19 | 11.88 | 19.67 | 6.00 | 85.7 | 90.0 |
| Bench 2 | Autosub In | O'Reilly | DEF | 13 | 5.3 | 3.55 | 10.48 | 17.04 | 1.00 | 79.2 | 56.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.41 | 10.33 | 16.40 | 6.00 | 86.0 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 4.67 | 13.80 | 21.76 | 2.00 | 68.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.22 | 12.42 | 21.01 | 2.00 | 75.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.19 | 11.47 | 18.43 | 1.00 | 74.1 | 27.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 96.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.3 | 4.49 | 14.17 | 23.25 | 1.00 | 83.0 | 81.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.68 | 14.06 | 22.91 | 0.00 | 82.9 | 0.0 |
| Bench 4 | Bench | B.Fernandes | MID | 14 | 9.2 | 2.81 | 10.35 | 20.36 | 0.00 | 26.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 1.70 -> 4.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.93
- Actual score: 45.00
- Transfer: B.Fernandes -> Cherki (projected gain 11.30, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.70 | 10.61 | 16.86 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 96.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.21 | 11.83 | 19.31 | 1.00 | 87.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.89 | 11.75 | 19.42 | 1.00 | 85.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.12 | 11.36 | 17.55 | 7.00 | 85.8 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.3 | 3.02 | 8.69 | 14.44 | 2.00 | 64.8 | 90.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 4.79 | 13.93 | 21.97 | 0.00 | 75.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.05 | 11.63 | 19.17 | 17.00 | 76.4 | 90.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.2 | 3.13 | 9.66 | 16.06 | 2.00 | 60.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.01 | 17.38 | 28.20 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 93.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.08 | 14.87 | 23.50 | 4.00 | 80.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.4 | 4.94 | 13.83 | 22.19 | 5.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Rice | MID | 1 | 7.2 | 3.04 | 9.88 | 17.36 | 17.00 | 45.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 4.10 -> 3.80
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.16
- Actual score: 51.00
- Transfer: O'Reilly -> Tarkowski (projected gain 6.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.65 | 10.43 | 16.79 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 4.79 | 13.40 | 20.82 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 93.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.98 | 11.76 | 18.21 | 0.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Virgil | DEF | 12 | 5.9 | 3.37 | 10.60 | 17.52 | 6.00 | 83.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.57 | 10.14 | 17.57 | 6.00 | 76.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 92.8 | 81.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 9.1 | 3.20 | 10.64 | 17.70 | 0.00 | 42.6 | 0.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 3.46 | 10.22 | 16.51 | 1.00 | 61.7 | 15.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.84 | 16.56 | 27.11 | 2.00 | 82.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 92.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.15 | 14.96 | 23.22 | 1.00 | 85.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.59 | 13.97 | 22.39 | 3.00 | 77.8 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.36 | 12.95 | 22.17 | 3.00 | 74.6 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 3.80 -> 3.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 55.05
- Actual score: 35.00
- Transfer: Virgil -> J.Timber (projected gain 3.04, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.83 | 10.99 | 17.40 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 94.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 96.3 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.44 | 12.92 | 20.25 | 5.00 | 81.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.02 | 11.71 | 19.20 | 3.00 | 84.6 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.5 | 4.02 | 10.88 | 17.22 | 0.00 | 82.5 | 90.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Ekitiké | FWD | 12 | 9.0 | 3.02 | 9.20 | 16.55 | 2.00 | 22.8 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.2 | 2.63 | 8.62 | 14.70 | 8.00 | 42.9 | 73.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 91.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 4.91 | 14.72 | 24.34 | 1.00 | 75.5 | 45.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.93 | 13.98 | 22.65 | 2.00 | 81.3 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.24 | 12.99 | 21.07 | 1.00 | 60.9 | 45.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 4.24 | 12.70 | 21.42 | 3.00 | 69.7 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 3.40 -> 2.70
- Free transfers: 2 -> 2
- Captain: Thiago
- Vice captain: Semenyo
- Effective captain: Thiago
- Chip used: none
- Predicted score: 57.16
- Actual score: 36.00
- Transfer: Senesi -> Chalobah (projected gain 0.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.10 | 11.58 | 18.16 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 97.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.61 | 13.22 | 20.59 | 1.00 | 83.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.70 | 13.14 | 21.44 | 4.00 | 86.1 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.5 | 4.28 | 12.50 | 19.52 | 4.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.73 | 10.51 | 17.32 | 7.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 3.29 | 9.55 | 16.23 | 6.00 | 53.8 | 90.0 |
| Captain | Captain | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 92.7 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.08 | 12.43 | 20.99 | 1.00 | 51.9 | 31.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.1 | 3.28 | 10.19 | 16.65 | 12.00 | 61.9 | 84.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.46 | 15.60 | 25.18 | 8.00 | 85.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 5.37 | 15.57 | 24.54 | 1.00 | 89.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.06 | 14.30 | 23.04 | 8.00 | 81.8 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.46 | 12.45 | 20.94 | 3.00 | 60.7 | 72.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.92 | 11.77 | 20.45 | 1.00 | 55.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 2.70 -> 2.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.20
- Actual score: 65.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Foden -> B.Fernandes (projected gain 4.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.94 | 11.14 | 17.41 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 100.6 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.6 | 4.44 | 12.44 | 19.64 | 3.00 | 88.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.20 | 12.32 | 20.30 | 2.00 | 84.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.13 | 11.94 | 18.98 | 5.00 | 76.2 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 3.96 | 11.55 | 19.10 | 3.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.88 | 11.28 | 18.40 | 0.00 | 91.5 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 91.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.1 | 4.26 | 11.59 | 18.53 | 10.00 | 72.5 | 45.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 8.9 | 3.84 | 11.21 | 18.63 | 13.00 | 46.1 | 83.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 93.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.12 | 14.98 | 23.65 | 3.00 | 88.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.3 | 4.95 | 13.92 | 21.33 | 10.00 | 70.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.99 | 11.45 | 19.45 | 8.00 | 58.3 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 2.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.21
- Actual score: 63.00
- Transfer: J.Timber -> Gabriel (projected gain 7.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.40 | 11.96 | 18.56 | 7.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 95.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.0 | 5.50 | 15.23 | 23.90 | 6.00 | 84.3 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.30 | 12.33 | 19.86 | 4.00 | 86.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.11 | 12.09 | 19.89 | 2.00 | 84.3 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 3.97 | 11.69 | 19.05 | 3.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.33 | 7.86 | 13.83 | 1.00 | 53.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.98 | 13.47 | 22.27 | 5.00 | 82.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 4.33 | 12.59 | 20.47 | 8.00 | 63.8 | 74.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.31 | 12.53 | 20.21 | 2.00 | 70.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 93.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.42 | 15.61 | 24.72 | 10.00 | 86.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.39 | 15.36 | 24.58 | 5.00 | 85.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 5.09 | 14.96 | 23.25 | 10.00 | 74.7 | 90.0 |
| Bench 3 | Bench | Cherki | MID | 13 | 6.6 | 3.70 | 11.22 | 18.75 | 1.00 | 62.0 | 29.0 |

## GW26

- Train rows: 180267
- Bank: 1.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: bench_boost
- Predicted score: 79.76
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.09) beats the best remaining Bench Boost opportunity (15.15).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Cherki -> Enzo (projected gain 5.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.09) beats the best remaining Bench Boost opportunity (15.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.17 | 12.88 | 19.56 | 3.00 | 112.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 93.9 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 6.40 | 16.55 | 25.50 | 7.00 | 118.7 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 94.1 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.37 | 12.49 | 20.14 | 3.00 | 87.4 | 90.0 |
| Bench 3 | Bench Boost | Tarkowski | DEF | 9 | 5.8 | 3.87 | 11.10 | 18.39 | 1.00 | 80.1 | 90.0 |
| Bench 4 | Bench Boost | Van de Ven | DEF | 18 | 4.5 | 3.60 | 10.41 | 17.06 | 3.00 | 76.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.09 | 14.21 | 22.26 | 10.00 | 74.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.42 | 13.87 | 22.99 | 2.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Ekitiké | FWD | 12 | 8.9 | 4.14 | 11.89 | 18.85 | 2.00 | 70.0 | 87.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 6.26 | 16.30 | 25.59 | 14.00 | 114.2 | 180.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 5.63 | 15.59 | 24.84 | 2.00 | 77.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 92.0 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.8 | 4.94 | 13.88 | 22.42 | 2.00 | 83.1 | 90.0 |

## GW27

- Train rows: 181084
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 69.65
- Actual score: 43.00
- Transfer: Tarkowski -> Virgil (projected gain 5.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 117.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 7.29 | 20.72 | 32.03 | 2.00 | 138.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.16 | 14.70 | 23.49 | 11.00 | 96.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 98.2 | 90.0 |
| Bench 2 | Bench | Chalobah | DEF | 7 | 5.8 | 4.53 | 12.44 | 20.06 | 2.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.25 | 9.78 | 16.11 | 0.00 | 78.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.74 | 15.49 | 24.03 | 7.00 | 83.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.91 | 13.95 | 22.79 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Ekitiké | FWD | 12 | 8.9 | 4.43 | 12.22 | 19.17 | 2.00 | 70.6 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 131.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 96.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 15.08 | 24.47 | 2.00 | 76.9 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 5.34 | 14.63 | 23.20 | 2.00 | 86.4 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.08 | 14.20 | 22.90 | 2.00 | 80.2 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 63.56
- Actual score: 73.00
- Transfer: Ekitiké -> Bowen (projected gain 3.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.78 | 16.70 | 26.68 | 9.00 | 108.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.8 | 3.58 | 11.44 | 19.11 | 1.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.73 | 11.04 | 17.37 | 0.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.40 | 16.09 | 25.22 | 2.00 | 82.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.27 | 14.62 | 23.40 | 6.00 | 81.2 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 4.29 | 13.50 | 21.45 | 7.00 | 84.6 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 108.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 14.94 | 23.96 | 13.00 | 78.3 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.97 | 13.91 | 22.28 | 2.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Enzo | MID | 7 | 6.9 | 4.14 | 12.98 | 21.07 | 1.00 | 80.7 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 2.30 -> 3.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 65.90
- Actual score: 71.00
- Transfer: Enzo -> Wilson (projected gain 1.04, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 94.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.27 | 9.24 | 14.56 | 2.00 | 87.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.81 | 17.27 | 26.97 | 11.00 | 112.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.7 | 3.28 | 10.49 | 17.50 | 2.00 | 79.7 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.35 | 9.70 | 15.17 | -3.00 | 86.1 | 37.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.47 | 15.70 | 24.83 | 19.00 | 81.9 | 84.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 5.02 | 14.68 | 22.59 | 4.00 | 90.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.07 | 14.40 | 22.63 | 2.00 | 84.2 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 101.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 100.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 4.87 | 13.40 | 21.11 | 0.00 | 81.0 | 0.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 4.56 | 12.92 | 20.60 | 1.00 | 81.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 3.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 72.69
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Rogers -> Palmer (projected gain 6.08, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.40 | 9.35 | 14.52 | 6.00 | 88.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.26 | 15.52 | 24.66 | 9.00 | 99.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.13 | 14.63 | 22.87 | 2.00 | 86.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.46 | 12.29 | 19.07 | 2.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Chalobah | DEF | 7 | 5.6 | 3.52 | 10.26 | 16.52 | 2.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 2.08 | 6.66 | 11.08 | 0.00 | 56.8 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 96.1 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.5 | 4.99 | 14.27 | 22.38 | 6.00 | 87.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.00 | 13.79 | 21.33 | 6.00 | 86.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 103.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 97.1 | 90.0 |
| XI | XI | Palmer | MID | 7 | 10.6 | 4.82 | 14.85 | 23.44 | 2.00 | 72.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.54 | 13.53 | 22.43 | 3.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Wilson | MID | 10 | 6.0 | 3.16 | 9.43 | 15.58 | 3.00 | 48.1 | 90.0 |