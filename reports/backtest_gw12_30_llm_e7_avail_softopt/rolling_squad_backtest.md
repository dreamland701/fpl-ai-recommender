# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1156.02
- Total actual points: 1058.00
- Average predicted points: 60.84
- Average actual points: 55.68
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
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Mateta, Thiago, O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.31 | 11.92 | 18.46 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.54 | 12.48 | 20.47 | 14.00 | 83.3 | 90.0 |
| Bench 4 | Autosub In | O'Reilly | DEF | 13 | 4.9 | 4.04 | 11.99 | 19.06 | 1.00 | 84.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.60 | 15.64 | 24.41 | 1.00 | 68.7 | 75.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 8.0 | 4.37 | 13.84 | 21.93 | 1.00 | 76.4 | 59.0 |
| Bench 3 | Autosub In | Thiago | FWD | 5 | 6.2 | 4.35 | 12.53 | 19.81 | 4.00 | 86.2 | 90.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 76.6 | 0.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 4.97 | 15.04 | 23.65 | 6.00 | 87.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 4.78 | 13.63 | 21.89 | 2.00 | 87.5 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.48 | 13.18 | 20.88 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 3.30 -> 3.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.80
- Actual score: 43.00
- Transfer: O'Reilly -> Guéhi (projected gain 0.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.75 | 11.08 | 17.59 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 92.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 4.97 | 13.81 | 22.20 | 1.00 | 88.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 92.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.44 | 12.78 | 21.17 | 0.00 | 83.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.27 | 12.40 | 19.84 | 0.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.5 | 2.34 | 9.58 | 19.00 | 0.00 | 24.3 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.22 | 14.59 | 23.27 | 1.00 | 65.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.04 | 13.96 | 21.86 | 13.00 | 83.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.14 | 13.14 | 21.28 | 6.00 | 64.4 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.36 | 15.90 | 25.10 | 1.00 | 84.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 92.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 4.45 | 13.26 | 21.80 | 11.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Semenyo | MID | 4 | 8.0 | 4.12 | 12.76 | 22.01 | 1.00 | 34.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 2.80 | 9.03 | 15.50 | -2.00 | 62.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 3.20 -> 3.30
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.41
- Actual score: 55.00
- Transfer: Gabriel -> J.Timber (projected gain 0.87, hit 0)
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.91 | 11.03 | 17.36 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 91.3 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 92.4 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.54 | 12.99 | 20.67 | 1.00 | 83.4 | 46.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 4.47 | 12.92 | 20.71 | 14.00 | 85.2 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 4.01 | 12.23 | 19.53 | 0.00 | 85.8 | 0.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.1 | 3.95 | 11.50 | 18.89 | 14.00 | 82.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.05 | 15.65 | 25.20 | 1.00 | 87.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.78 | 13.23 | 21.01 | 2.00 | 84.1 | 63.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.11 | 12.66 | 21.16 | 2.00 | 66.0 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.27 | 15.47 | 25.56 | 3.00 | 89.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.47 | 15.47 | 24.93 | 2.00 | 87.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.01 | 14.52 | 23.67 | 4.00 | 88.8 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.78 | 14.02 | 23.66 | 4.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 6.0 | 2.52 | 8.33 | 14.98 | 0.00 | 34.0 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 3.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.82
- Actual score: 77.00
- Transfer: Caicedo -> Foden (projected gain 2.20, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.00 | 11.73 | 18.63 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 92.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 94.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 12.19 | 19.99 | 3.00 | 68.8 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 5.0 | 2.55 | 8.26 | 15.61 | 8.00 | 61.5 | 61.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.72 | 8.12 | 13.97 | 6.00 | 33.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.42 | 13.89 | 22.48 | 1.00 | 81.7 | 32.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.32 | 12.74 | 20.67 | 2.00 | 76.5 | 65.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 6.7 | 4.10 | 12.17 | 19.79 | 2.00 | 75.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.32 | 15.51 | 25.22 | 3.00 | 85.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.29 | 15.27 | 24.54 | 18.00 | 86.5 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.44 | 15.12 | 24.34 | 8.00 | 85.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.63 | 14.43 | 24.17 | 6.00 | 85.4 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.1 | 5.09 | 14.13 | 22.29 | 12.00 | 87.6 | 68.0 |

## GW16

- Train rows: 172367
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 59.80
- Actual score: 62.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Muñoz -> Cucurella (projected gain 1.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.34 | 11.61 | 18.01 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.75 | 13.35 | 20.91 | 2.00 | 87.0 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 4.41 | 12.91 | 20.61 | 6.00 | 89.4 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.7 | 3.86 | 11.10 | 18.37 | 1.00 | 57.3 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 5.0 | 3.40 | 10.44 | 17.68 | 1.00 | 67.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.55 | 13.78 | 22.21 | 2.00 | 79.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.21 | 12.71 | 20.96 | 2.00 | 66.6 | 62.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.4 | 3.86 | 11.86 | 20.11 | 2.00 | 71.1 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 96.0 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.4 | 5.11 | 15.66 | 24.96 | 11.00 | 78.6 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.30 | 15.02 | 24.64 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.82 | 14.49 | 23.70 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.93 | 13.96 | 23.10 | 2.00 | 84.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.09
- Actual score: 53.00
- Transfer: Senesi -> Virgil (projected gain 1.04, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.30 | 17.83 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.34 | 9.38 | 14.76 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.24 | 12.82 | 21.00 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 4.21 | 12.62 | 20.37 | 1.00 | 88.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 3.95 | 12.09 | 19.96 | 6.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.7 | 3.71 | 10.48 | 17.34 | 0.00 | 79.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.60 | 14.57 | 23.21 | 2.00 | 65.8 | 90.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.3 | 3.72 | 11.78 | 20.11 | 6.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.9 | 2.55 | 9.27 | 17.20 | 2.00 | 57.7 | 76.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 92.2 | 45.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 6.22 | 18.57 | 28.95 | 3.00 | 86.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.21 | 14.53 | 23.74 | 10.00 | 86.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.42 | 13.47 | 22.76 | 11.00 | 82.5 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.12 | 13.09 | 22.97 | 0.00 | 78.8 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.74
- Actual score: 42.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mbeumo -> Rogers (projected gain 3.25, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.58 | 14.89 | 11.00 | 89.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| Bench 2 | Bench | J.Timber | DEF | 1 | 6.5 | 4.56 | 12.77 | 20.20 | 0.00 | 65.5 | 0.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.38 | 12.41 | 19.86 | 2.00 | 89.0 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 4.15 | 11.61 | 19.14 | 2.00 | 86.5 | 68.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.26 | 9.57 | 15.42 | 11.00 | 83.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.39 | 12.92 | 20.76 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.20 | 12.08 | 19.71 | 8.00 | 76.0 | 68.0 |
| Bench 3 | Autosub In | Mateta | FWD | 8 | 7.8 | 3.40 | 10.28 | 17.03 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.00 | 18.03 | 28.76 | 2.00 | 66.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.68 | 17.07 | 28.11 | 0.00 | 79.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.23 | 15.41 | 24.86 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.92 | 14.59 | 23.58 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.1 | 4.87 | 14.23 | 22.73 | 1.00 | 89.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 1.20 -> 4.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.14
- Actual score: 42.00
- Transfer: B.Fernandes -> Wilson (projected gain 4.36, hit 0)
- Autosub outfielders: Mateta, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.81 | 10.83 | 17.14 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.19 | 11.88 | 19.67 | 6.00 | 65.7 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.6 | 3.41 | 10.33 | 16.40 | 6.00 | 87.0 | 90.0 |
| XI | Bench | Cucurella | DEF | 7 | 6.2 | 3.61 | 10.29 | 16.79 | 0.00 | 79.2 | 0.0 |
| Bench 4 | Bench | J.Timber | DEF | 1 | 6.5 | 3.04 | 8.95 | 15.07 | 9.00 | 29.3 | 82.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.22 | 12.42 | 21.01 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.19 | 11.47 | 18.43 | 1.00 | 73.1 | 27.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.7 | 3.51 | 9.95 | 16.28 | 9.00 | 74.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 94.2 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.95 | 14.27 | 22.72 | 2.00 | 86.1 | 84.0 |
| XI | XI | Rogers | MID | 2 | 7.3 | 4.49 | 14.17 | 23.25 | 1.00 | 85.0 | 81.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.68 | 14.06 | 22.91 | 0.00 | 84.9 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 4.60 -> 5.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.62
- Actual score: 51.00
- Transfer: Rice -> Cherki (projected gain 4.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.70 | 10.61 | 16.86 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.21 | 11.83 | 19.31 | 1.00 | 88.1 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.12 | 11.36 | 17.55 | 7.00 | 65.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.73 | 10.97 | 18.48 | 3.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Cucurella | DEF | 7 | 6.2 | 1.72 | 6.46 | 11.78 | 0.00 | 27.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.05 | 11.63 | 19.17 | 17.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Mateta | FWD | 8 | 7.7 | 3.49 | 10.38 | 16.75 | 2.00 | 80.9 | 86.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 3.13 | 9.66 | 16.06 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.01 | 17.38 | 28.20 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 92.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.08 | 14.87 | 23.50 | 4.00 | 83.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.4 | 4.94 | 13.83 | 22.19 | 5.00 | 81.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.63 | 13.24 | 21.29 | 6.00 | 83.9 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 5.10 -> 5.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.12
- Actual score: 57.00
- Transfer: Cucurella -> Tarkowski (projected gain 3.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.65 | 10.43 | 16.79 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 4.79 | 13.40 | 20.82 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.98 | 11.76 | 18.21 | 0.00 | 90.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 11.68 | 18.88 | 6.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Virgil | DEF | 12 | 5.9 | 3.37 | 10.60 | 17.52 | 6.00 | 85.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 91.8 | 81.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 3.46 | 10.22 | 16.51 | 1.00 | 71.7 | 15.0 |
| Bench 2 | Bench | Mateta | FWD | 8 | 7.6 | 3.48 | 9.96 | 16.22 | 2.00 | 76.9 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.84 | 16.56 | 27.11 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.15 | 14.96 | 23.22 | 1.00 | 87.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.59 | 13.97 | 22.39 | 3.00 | 81.8 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.91 | 13.90 | 22.30 | 9.00 | 86.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 5.60 -> 4.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 56.20
- Actual score: 35.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: João Pedro -> Watkins (projected gain 0.51, hit 0)
- Autosub outfielders: Cherki.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.83 | 10.99 | 17.40 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 92.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.44 | 12.92 | 20.25 | 5.00 | 84.4 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.24 | 11.42 | 18.18 | 2.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 4.02 | 10.88 | 17.22 | 0.00 | 85.5 | 90.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 88.0 | 90.0 |
| XI | XI | Watkins | FWD | 2 | 8.7 | 4.64 | 13.18 | 20.35 | 2.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.6 | 3.19 | 9.33 | 15.11 | 2.00 | 70.6 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 4.91 | 14.72 | 24.34 | 1.00 | 74.5 | 45.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.93 | 13.98 | 22.65 | 2.00 | 80.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.77 | 13.43 | 21.81 | 2.00 | 67.2 | 87.0 |
| Bench 2 | Autosub In | Cherki | MID | 13 | 6.8 | 4.24 | 12.99 | 21.07 | 1.00 | 59.9 | 45.0 |

## GW23

- Train rows: 177836
- Bank: 4.10 -> 1.90
- Free transfers: 2 -> 2
- Captain: Thiago
- Vice captain: Semenyo
- Effective captain: Thiago
- Chip used: none
- Predicted score: 56.69
- Actual score: 57.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Van de Ven -> Gabriel (projected gain 3.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.10 | 11.58 | 18.16 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.8 | 4.99 | 14.17 | 21.21 | 1.00 | 82.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.61 | 13.22 | 20.59 | 1.00 | 85.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.70 | 13.14 | 21.44 | 4.00 | 87.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.73 | 10.94 | 17.52 | 9.00 | 85.8 | 90.0 |
| Bench 4 | Bench | Guéhi | DEF | 8 | 5.3 | 3.29 | 9.55 | 16.23 | 6.00 | 41.8 | 90.0 |
| Captain | Captain | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 91.7 | 90.0 |
| XI | XI | Watkins | FWD | 2 | 8.8 | 3.79 | 11.53 | 18.28 | 8.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.6 | 3.53 | 9.92 | 15.71 | 2.00 | 78.5 | 84.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.46 | 15.60 | 25.18 | 8.00 | 87.3 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.06 | 14.30 | 23.04 | 8.00 | 84.8 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.68 | 13.11 | 21.50 | 10.00 | 83.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.46 | 12.45 | 20.94 | 3.00 | 59.7 | 72.0 |
| Bench 2 | Bench | Foden | MID | 13 | 8.7 | 3.92 | 11.77 | 20.45 | 1.00 | 54.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.58
- Actual score: 58.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Foden -> B.Fernandes (projected gain 2.41, hit 0)
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.94 | 11.14 | 17.41 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 96.6 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.9 | 4.60 | 13.17 | 20.59 | 8.00 | 80.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.69 | 13.10 | 20.69 | 4.00 | 91.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.20 | 12.32 | 20.30 | 2.00 | 86.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.13 | 11.94 | 18.98 | 5.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Guéhi | DEF | 8 | 5.2 | 3.96 | 11.55 | 19.10 | 3.00 | 81.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Watkins | FWD | 2 | 8.8 | 4.30 | 12.25 | 19.90 | 0.00 | 78.7 | 0.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.5 | 3.35 | 9.57 | 15.25 | 0.00 | 78.2 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.3 | 4.95 | 13.92 | 21.33 | 10.00 | 77.7 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.60 | 13.31 | 21.36 | 2.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Cherki | MID | 13 | 6.7 | 3.99 | 11.45 | 19.45 | 8.00 | 69.3 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 1.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.49
- Actual score: 54.00
- Transfer: Cherki -> Enzo (projected gain 1.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.40 | 11.96 | 18.56 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 93.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.0 | 5.50 | 15.23 | 23.90 | 6.00 | 86.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.47 | 13.07 | 20.59 | 0.00 | 91.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.11 | 12.09 | 19.89 | 2.00 | 86.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.40 | 11.96 | 19.06 | 6.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 3.97 | 11.69 | 19.05 | 3.00 | 57.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.98 | 13.47 | 22.27 | 5.00 | 62.3 | 90.0 |
| Bench 3 | Bench | Watkins | FWD | 2 | 8.8 | 2.37 | 7.71 | 13.98 | 2.00 | 50.6 | 85.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.5 | 2.10 | 6.34 | 11.20 | 0.00 | 25.4 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.42 | 15.61 | 24.72 | 10.00 | 87.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 5.09 | 14.96 | 23.25 | 10.00 | 79.7 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 4.53 | 12.94 | 21.33 | 2.00 | 82.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 4.22 | 12.19 | 19.33 | 2.00 | 85.4 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 1.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Semenyo
- Effective captain: Gabriel
- Chip used: bench_boost
- Predicted score: 78.21
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.54) beats the best remaining Bench Boost opportunity (14.62).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Mateta -> João Pedro (projected gain 2.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.54) beats the best remaining Bench Boost opportunity (14.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.17 | 12.88 | 19.56 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 6.40 | 16.55 | 25.50 | 7.00 | 112.7 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 92.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.44 | 13.50 | 20.47 | 3.00 | 127.3 | 180.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.19 | 12.64 | 20.13 | 17.00 | 90.5 | 90.0 |
| Bench 3 | Bench Boost | Tarkowski | DEF | 9 | 5.8 | 3.87 | 11.10 | 18.39 | 1.00 | 83.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.09 | 14.21 | 22.26 | 10.00 | 73.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.42 | 13.87 | 22.99 | 2.00 | 86.3 | 90.0 |
| Bench 4 | Bench Boost | Watkins | FWD | 2 | 8.7 | 3.30 | 9.72 | 16.32 | 2.00 | 68.6 | 73.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 5.63 | 15.59 | 24.84 | 2.00 | 81.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.8 | 4.94 | 13.88 | 22.42 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Bench Boost | Wilson | MID | 10 | 6.1 | 3.89 | 12.06 | 19.37 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 1.10 -> 5.20
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Semenyo
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 68.43
- Actual score: 42.00
- Transfer: Watkins -> Mané (projected gain 0.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 111.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 7.29 | 20.72 | 32.03 | 2.00 | 124.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 107.5 | 56.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.16 | 14.70 | 23.49 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 95.2 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.8 | 3.58 | 10.13 | 16.96 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.74 | 15.49 | 24.03 | 7.00 | 85.6 | 79.0 |
| XI | XI | Mané | FWD | 20 | 4.6 | 5.13 | 14.18 | 21.57 | 2.00 | 111.8 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 7.0 | 4.91 | 13.95 | 22.79 | 2.00 | 85.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 15.08 | 24.47 | 2.00 | 81.9 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 5.34 | 14.63 | 23.20 | 2.00 | 87.4 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.08 | 14.20 | 22.90 | 2.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Wilson | MID | 10 | 6.0 | 3.38 | 10.40 | 17.39 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 5.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 61.94
- Actual score: 77.00
- Transfer: Enzo -> Palmer (projected gain 1.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.78 | 16.70 | 26.68 | 9.00 | 101.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| Bench 2 | Bench | J.Timber | DEF | 1 | 6.4 | 4.49 | 12.83 | 20.56 | 8.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.05 | 9.11 | 15.15 | 3.00 | 81.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.40 | 16.09 | 25.22 | 2.00 | 62.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.27 | 14.62 | 23.40 | 6.00 | 84.2 | 90.0 |
| Bench 3 | Bench | Mané | FWD | 20 | 4.6 | 4.07 | 11.56 | 18.28 | 2.00 | 96.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 89.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.30 | 14.94 | 23.96 | 13.00 | 82.3 | 90.0 |
| XI | XI | Palmer | MID | 7 | 10.6 | 4.60 | 13.96 | 22.63 | 1.00 | 77.2 | 85.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.97 | 13.91 | 22.28 | 2.00 | 85.9 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.52 | 13.02 | 20.44 | 12.00 | 87.6 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 64.75
- Actual score: 86.00
- Transfer: Rogers -> Mbeumo (projected gain 0.65, hit 0)
- Autosub outfielders: Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.27 | 9.24 | 14.56 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.81 | 17.27 | 26.97 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.40 | 13.00 | 91.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.96 | 10.68 | 16.61 | 15.00 | 85.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.47 | 15.70 | 24.83 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.07 | 14.40 | 22.63 | 2.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Mané | FWD | 20 | 4.6 | 3.79 | 10.68 | 16.69 | 2.00 | 92.4 | 69.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 100.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 4.67 | 13.57 | 21.08 | 1.00 | 78.9 | 76.0 |
| Bench 2 | Autosub In | Palmer | MID | 7 | 10.6 | 4.35 | 13.54 | 21.66 | 9.00 | 76.0 | 84.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 4.87 | 13.40 | 21.11 | 0.00 | 80.0 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 0.50 -> 1.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 72.91
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Wilson -> Anderson (projected gain 0.49, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.40 | 9.35 | 14.52 | 6.00 | 88.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.26 | 15.52 | 24.66 | 9.00 | 79.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.13 | 14.63 | 22.87 | 2.00 | 87.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 5.06 | 14.37 | 22.48 | 1.00 | 71.2 | 37.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 4.46 | 12.29 | 19.07 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.64 | 11.13 | 17.56 | 0.00 | 88.8 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.00 | 13.79 | 21.33 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Mané | FWD | 20 | 4.6 | 2.34 | 7.10 | 11.76 | 1.00 | 73.4 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 77.1 | 90.0 |
| XI | XI | Palmer | MID | 7 | 10.6 | 4.82 | 14.85 | 23.44 | 2.00 | 71.0 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 4.55 | 13.00 | 20.63 | 2.00 | 67.4 | 74.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 4.59 | 12.65 | 19.90 | 2.00 | 89.1 | 87.0 |