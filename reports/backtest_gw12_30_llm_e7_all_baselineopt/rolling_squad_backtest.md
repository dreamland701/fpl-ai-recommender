# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 911.47
- Total actual points: 1069.00
- Average predicted points: 47.97
- Average actual points: 56.26
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 48.88
- Actual score: 39.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Van de Ven, Van Hecke, Isidor.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.51 | 10.92 | 17.26 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.67 | 13.46 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 4.25 | 12.16 | 20.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 10.98 | 17.87 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.18 | 10.71 | 17.11 | 0.00 | 93.4 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 3.64 | 10.18 | 16.07 | 14.00 | 83.3 | 90.0 |
| Bench 3 | Autosub In | Van Hecke | DEF | 6 | 4.4 | 2.88 | 8.76 | 13.84 | 2.00 | 86.0 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 3.57 | 12.84 | 20.93 | 1.00 | 76.4 | 59.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 3.55 | 11.33 | 18.81 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Autosub In | Isidor | FWD | 17 | 5.6 | 2.52 | 6.85 | 11.23 | 2.00 | 70.5 | 63.0 |
| Vice Captain | Bench | Semenyo | MID | 4 | 8.1 | 4.63 | 14.34 | 22.77 | 0.00 | 76.6 | 0.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.2 | 4.98 | 14.15 | 23.02 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 4.45 | 13.95 | 20.94 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.97 | 12.94 | 22.05 | 6.00 | 87.1 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 3.58 | 12.08 | 19.18 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 47.10
- Actual score: 40.00
- Transfer: Gabriel -> J.Timber (projected gain 4.22, hit 0)
- Autosub outfielders: Van Hecke.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.15 | 9.68 | 15.59 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.51 | 7.73 | 12.08 | 1.00 | 92.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.2 | 3.47 | 11.93 | 19.79 | 2.00 | 82.9 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.47 | 11.20 | 17.84 | 0.00 | 86.9 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 3.97 | 10.41 | 16.60 | 1.00 | 88.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.23 | 10.10 | 16.80 | 2.00 | 92.2 | 90.0 |
| Bench 2 | Autosub In | Van Hecke | DEF | 6 | 4.4 | 2.75 | 7.77 | 12.97 | 6.00 | 84.4 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.44 | 12.04 | 19.78 | 6.00 | 64.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 3.94 | 10.46 | 15.96 | 13.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.43 | 6.38 | 10.09 | 2.00 | 66.5 | 62.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.86 | 14.90 | 23.70 | 1.00 | 84.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.85 | 14.90 | 24.87 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.83 | 13.96 | 22.81 | 0.00 | 80.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 3.02 | 9.66 | 16.41 | 1.00 | 34.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 2.50 | 7.93 | 12.90 | -2.00 | 62.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.41
- Actual score: 55.00
- Transfer: Caicedo -> Bruno G. (projected gain 2.18, hit 0)
- Autosub outfielders: Van Hecke.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.21 | 9.23 | 14.46 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 12.64 | 2.00 | 91.3 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 3.57 | 11.92 | 18.71 | 14.00 | 85.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.34 | 9.49 | 14.87 | 1.00 | 83.4 | 46.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 2.95 | 9.06 | 15.02 | 0.00 | 92.4 | 0.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 2.91 | 9.03 | 14.03 | 0.00 | 85.8 | 0.0 |
| Bench 3 | Autosub In | Van Hecke | DEF | 6 | 4.4 | 2.53 | 7.75 | 12.43 | 12.00 | 85.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 3.95 | 12.65 | 19.90 | 1.00 | 87.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.78 | 11.03 | 19.61 | 2.00 | 84.1 | 63.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 1.70 | 5.04 | 8.40 | 1.00 | 36.9 | 28.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.47 | 14.27 | 23.96 | 3.00 | 89.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.97 | 14.27 | 22.53 | 2.00 | 87.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 3.78 | 11.92 | 22.06 | 4.00 | 79.8 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 6.6 | 3.30 | 11.13 | 18.96 | 7.00 | 85.5 | 45.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.12 | 10.01 | 16.97 | 1.00 | 55.8 | 45.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.06
- Actual score: 62.00
- Transfer: J.Timber -> Virgil (projected gain 1.82, hit 0)
- Autosub outfielders: Senesi, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.30 | 10.43 | 16.63 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.46 | 12.37 | 3.00 | 91.0 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 4.07 | 12.21 | 19.02 | 0.00 | 92.5 | 0.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 3.47 | 10.81 | 17.24 | 2.00 | 89.2 | 90.0 |
| XI | XI | Van Hecke | DEF | 6 | 4.4 | 2.77 | 7.97 | 12.76 | 5.00 | 89.1 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.12 | 7.02 | 11.87 | 6.00 | 33.7 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 5.0 | 2.35 | 6.76 | 12.61 | 8.00 | 61.5 | 61.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.52 | 11.44 | 18.67 | 2.00 | 76.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 3.40 | 11.07 | 17.39 | 2.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 1.43 | 4.45 | 7.83 | 1.00 | 31.1 | 55.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.94 | 14.02 | 22.14 | 8.00 | 85.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.03 | 13.23 | 23.07 | 6.00 | 85.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.12 | 12.91 | 20.62 | 3.00 | 85.0 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 3.13 | 10.16 | 17.93 | 0.00 | 61.5 | 0.0 |
| XI | XI | Bruno G. | MID | 15 | 6.7 | 3.37 | 10.06 | 16.85 | 10.00 | 76.3 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.40 -> 5.50
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 46.39
- Actual score: 51.00
- Transfer: M.Salah -> B.Fernandes (projected gain 8.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.54 | 10.01 | 15.91 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.20 | 8.45 | 12.84 | 1.00 | 90.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 3.55 | 11.00 | 17.46 | 6.00 | 89.4 | 90.0 |
| Bench 2 | Bench | Muñoz | DEF | 8 | 6.1 | 2.86 | 9.43 | 15.51 | 0.00 | 63.6 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 2.86 | 8.60 | 14.37 | 1.00 | 57.3 | 90.0 |
| XI | XI | Van Hecke | DEF | 6 | 4.5 | 2.92 | 8.05 | 12.58 | 1.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.60 | 7.84 | 12.88 | 1.00 | 67.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 3.65 | 12.78 | 21.11 | 2.00 | 79.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.41 | 11.41 | 18.56 | 2.00 | 66.6 | 62.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.01 | 5.92 | 9.44 | 0.00 | 41.9 | 20.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 5.45 | 16.72 | 27.22 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 4.50 | 13.62 | 22.64 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 3.82 | 12.19 | 22.40 | 6.00 | 85.4 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 6.8 | 3.29 | 10.79 | 17.45 | 1.00 | 82.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 10.46 | 17.50 | 2.00 | 84.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.50 -> 6.30
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Semenyo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 46.04
- Actual score: 43.00
- Transfer: Muñoz -> Guéhi (projected gain 3.88, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 9.80 | 15.43 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.84 | 8.18 | 12.76 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.80 | 11.98 | 20.77 | 1.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.44 | 11.82 | 18.90 | 2.00 | 89.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.12 | 9.34 | 15.86 | 4.00 | 78.7 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.11 | 9.28 | 15.14 | 0.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Van Hecke | DEF | 6 | 4.5 | 3.03 | 8.24 | 13.07 | 0.00 | 86.9 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.70 | 12.97 | 21.01 | 2.00 | 65.8 | 90.0 |
| Bench 3 | Autosub In | Mateta | FWD | 8 | 7.9 | 2.35 | 7.77 | 14.00 | 2.00 | 57.7 | 76.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.5 | 1.69 | 4.99 | 8.69 | 1.00 | 28.9 | 18.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.2 | 5.09 | 15.29 | 24.63 | 1.00 | 92.2 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 4.81 | 13.33 | 21.74 | 10.00 | 86.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.27 | 21.76 | 11.00 | 82.5 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 3.42 | 11.69 | 21.57 | 0.00 | 78.8 | 0.0 |
| XI | XI | Bruno G. | MID | 15 | 7.0 | 3.36 | 10.96 | 18.44 | 2.00 | 80.2 | 90.0 |

## GW18

- Train rows: 173897
- Bank: 6.30 -> 5.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.60
- Actual score: 46.00
- Transfer: Mbeumo -> Foden (projected gain 7.05, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.37 | 9.53 | 14.87 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.28 | 12.49 | 11.00 | 89.9 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.88 | 11.21 | 17.46 | 2.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 10.66 | 16.19 | 2.00 | 90.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.04 | 9.73 | 15.14 | 2.00 | 88.9 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.6 | 2.46 | 7.27 | 12.12 | 11.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.6 | 1.63 | 5.67 | 9.91 | 3.00 | 28.8 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.89 | 11.92 | 18.76 | 5.00 | 83.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 2.90 | 8.78 | 14.93 | 2.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Isidor | FWD | 17 | 5.5 | 1.71 | 4.45 | 7.03 | 1.00 | 24.9 | 22.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.27 | 23.91 | 0.00 | 79.0 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.60 | 14.03 | 22.76 | 2.00 | 66.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.59 | 21.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 12.11 | 19.66 | 9.00 | 89.3 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 7.0 | 3.04 | 10.21 | 16.74 | 2.00 | 84.3 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 5.60 -> 4.50
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Saka
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.16
- Actual score: 51.00
- Transfer: B.Fernandes -> Saka (projected gain 5.62, hit 0)
- Autosub outfielders: Virgil.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.21 | 9.83 | 16.04 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.12 | 8.75 | 13.17 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.43 | 9.91 | 15.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 2.95 | 9.55 | 14.66 | 3.00 | 92.4 | 90.0 |
| XI | XI | Van Hecke | DEF | 6 | 4.6 | 2.88 | 8.90 | 13.63 | 0.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.61 | 8.13 | 13.10 | 6.00 | 87.0 | 90.0 |
| Bench 2 | Autosub In | Virgil | DEF | 12 | 5.9 | 2.69 | 8.08 | 13.67 | 6.00 | 65.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.42 | 11.22 | 18.91 | 2.00 | 80.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 3.01 | 8.95 | 14.78 | 9.00 | 74.5 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.4 | 1.46 | 4.90 | 8.56 | 1.00 | 30.4 | 32.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 15.39 | 27.04 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.3 | 4.80 | 13.66 | 22.19 | 6.00 | 81.9 | 82.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.96 | 21.91 | 0.00 | 84.9 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.45 | 19.84 | 5.00 | 94.2 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 7.0 | 3.30 | 10.24 | 16.70 | 10.00 | 85.0 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 4.50 -> 5.90
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 44.68
- Actual score: 55.00
- Transfer: Rice -> Wilson (projected gain 3.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.10 | 9.01 | 14.46 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.86 | 13.86 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.03 | 9.74 | 15.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.41 | 9.43 | 15.01 | 1.00 | 88.1 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.9 | 2.89 | 8.35 | 14.02 | 1.00 | 65.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.02 | 8.06 | 12.45 | 7.00 | 65.8 | 90.0 |
| Bench 3 | Bench | Van Hecke | DEF | 6 | 4.5 | 2.74 | 7.79 | 12.81 | 6.00 | 79.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.35 | 10.03 | 16.67 | 17.00 | 81.4 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 2.99 | 9.18 | 14.75 | 2.00 | 80.9 | 86.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.4 | 1.14 | 3.25 | 5.86 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 14.08 | 22.30 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 13.22 | 21.03 | 1.00 | 92.4 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.03 | 12.14 | 19.79 | 6.00 | 83.9 | 84.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.88 | 11.65 | 18.34 | 4.00 | 79.3 | 23.0 |
| XI | XI | Bruno G. | MID | 15 | 7.0 | 3.74 | 10.80 | 17.76 | 10.00 | 86.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 5.90 -> 5.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.77
- Actual score: 64.00
- Transfer: Van de Ven -> Thiaw (projected gain 2.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.05 | 9.23 | 15.79 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 13.08 | 3.00 | 90.8 | 90.0 |
| XI | XI | Thiaw | DEF | 15 | 5.0 | 3.90 | 10.95 | 17.83 | -1.00 | 90.7 | 45.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 9.70 | 15.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 2.87 | 9.00 | 14.92 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.8 | 2.67 | 7.64 | 13.47 | 6.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Van Hecke | DEF | 6 | 4.5 | 2.43 | 7.51 | 11.49 | 3.00 | 89.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 10.47 | 16.85 | 12.00 | 91.8 | 81.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 2.98 | 8.96 | 15.12 | 2.00 | 76.9 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.3 | 0.81 | 3.28 | 5.91 | 0.00 | 20.5 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.84 | 14.26 | 22.91 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.09 | 19.19 | 6.00 | 91.6 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 7.0 | 4.06 | 11.90 | 19.77 | 11.00 | 87.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.52 | 11.07 | 18.44 | 3.00 | 43.6 | 77.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.91 | 10.80 | 16.60 | 9.00 | 86.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 5.40 -> 4.20
- Free transfers: 2 -> 2
- Captain: Bruno G.
- Vice captain: Semenyo
- Effective captain: Bruno G.
- Chip used: none
- Predicted score: 45.15
- Actual score: 36.00
- Transfer: Thiaw -> J.Timber (projected gain 3.97, hit 0)
- Autosub outfielders: Van Hecke.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.23 | 9.59 | 14.80 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.46 | 7.27 | 11.30 | 5.00 | 92.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.54 | 11.92 | 18.75 | 5.00 | 84.4 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.06 | 9.56 | 15.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.44 | 8.82 | 13.58 | 2.00 | 87.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 2.92 | 8.31 | 13.50 | 3.00 | 86.6 | 90.0 |
| Bench 2 | Autosub In | Van Hecke | DEF | 6 | 4.5 | 2.85 | 8.00 | 12.34 | 6.00 | 85.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.96 | 11.95 | 18.58 | 2.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.6 | 2.39 | 7.83 | 12.61 | 2.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.3 | 0.87 | 2.65 | 4.48 | 0.00 | 15.8 | 0.0 |
| Captain | Captain | Bruno G. | MID | 15 | 7.1 | 4.87 | 13.88 | 22.72 | 3.00 | 92.3 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 4.12 | 12.63 | 19.95 | 2.00 | 90.5 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.47 | 11.72 | 20.00 | 1.00 | 57.7 | 33.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 11.32 | 19.34 | 1.00 | 74.5 | 45.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.77 | 10.83 | 17.31 | 2.00 | 67.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 4.20 -> 1.70
- Free transfers: 2 -> 2
- Captain: Bruno G.
- Vice captain: Semenyo
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 43.76
- Actual score: 59.00
- Transfer: Isidor -> Bowen (projected gain 2.36, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.40 | 9.98 | 15.66 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.21 | 12.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.31 | 10.02 | 15.09 | 1.00 | 85.2 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.13 | 9.24 | 14.52 | 9.00 | 85.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 2.81 | 8.93 | 13.86 | 3.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 2.49 | 7.25 | 11.93 | 6.00 | 41.8 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.5 | 2.40 | 6.75 | 10.95 | 1.00 | 83.8 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.54 | 11.14 | 17.81 | 12.00 | 84.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.96 | 10.88 | 17.34 | 2.00 | 91.7 | 90.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.6 | 3.03 | 8.92 | 14.41 | 2.00 | 78.5 | 84.0 |
| Vice Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.26 | 13.30 | 20.88 | 8.00 | 87.3 | 90.0 |
| Captain | Bench | Bruno G. | MID | 15 | 7.2 | 4.39 | 12.93 | 20.59 | 0.00 | 89.4 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.08 | 12.01 | 19.20 | 10.00 | 83.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.26 | 10.91 | 18.60 | 2.00 | 47.9 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.22 | 10.07 | 17.45 | 1.00 | 54.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.70 -> 1.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 44.05
- Actual score: 55.00
- Transfer: Bruno G. -> Rogers (projected gain 5.24, hit 0)
- Autosub outfielders: Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.24 | 9.34 | 14.81 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 9.02 | 14.68 | 1.00 | 96.6 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.39 | 9.90 | 15.19 | 4.00 | 91.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.30 | 9.64 | 14.65 | 8.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 2.96 | 8.55 | 13.80 | 3.00 | 81.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.03 | 8.44 | 13.38 | 5.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.5 | 2.52 | 6.98 | 11.88 | 2.00 | 81.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.43 | 11.43 | 17.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.27 | 10.56 | 17.16 | 8.00 | 84.8 | 80.0 |
| Bench 2 | Bench | Mateta | FWD | 8 | 7.5 | 2.85 | 7.97 | 12.35 | 0.00 | 78.2 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 4.86 | 13.62 | 21.15 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 4.40 | 13.18 | 21.04 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Saka | MID | 1 | 10.1 | 3.60 | 12.24 | 20.05 | 0.00 | 67.7 | 0.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 3.70 | 11.81 | 18.46 | 2.00 | 89.7 | 90.0 |
| Bench 3 | Autosub In | Foden | MID | 13 | 8.6 | 2.64 | 9.07 | 16.76 | 1.00 | 62.1 | 2.0 |

## GW25

- Train rows: 179450
- Bank: 1.30 -> 3.90
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Rice
- Effective captain: Rogers
- Chip used: none
- Predicted score: 45.80
- Actual score: 54.00
- Transfer: Saka -> Rice (projected gain 6.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.60 | 10.56 | 16.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.59 | 13.44 | 1.00 | 93.9 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.90 | 10.96 | 17.66 | 6.00 | 79.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.27 | 9.87 | 15.09 | 0.00 | 91.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.18 | 9.06 | 14.42 | 2.00 | 88.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 2.97 | 8.29 | 13.75 | 3.00 | 57.0 | 90.0 |
| Bench 2 | Bench | Van Hecke | DEF | 6 | 4.5 | 2.49 | 6.79 | 10.81 | 0.00 | 78.6 | 0.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.37 | 10.26 | 16.49 | 2.00 | 81.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 2.98 | 10.17 | 16.57 | 5.00 | 62.3 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.5 | 1.70 | 5.84 | 10.10 | 0.00 | 25.4 | 0.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.4 | 4.89 | 14.16 | 22.98 | 5.00 | 87.1 | 90.0 |
| Captain | Captain | Rogers | MID | 2 | 7.7 | 4.92 | 14.01 | 22.72 | 10.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.39 | 12.49 | 20.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.42 | 10.69 | 17.13 | 2.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.4 | 1.00 | 5.02 | 10.64 | 0.00 | 14.7 | 0.0 |

## GW26

- Train rows: 180267
- Bank: 3.90 -> 2.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: bench_boost
- Predicted score: 57.00
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.18) beats the best remaining Bench Boost opportunity (8.19).
- Transfer: Foden -> B.Fernandes (projected gain 4.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.18) beats the best remaining Bench Boost opportunity (8.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.48 | 16.56 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.42 | 13.13 | 1.00 | 92.9 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.24 | 10.90 | 16.07 | 3.00 | 127.3 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.00 | 10.42 | 16.51 | 7.00 | 92.1 | 90.0 |
| Bench 2 | Bench Boost | Virgil | DEF | 12 | 5.9 | 2.69 | 8.94 | 14.53 | 17.00 | 90.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 2.99 | 8.25 | 13.52 | 2.00 | 85.7 | 90.0 |
| Bench 4 | Bench Boost | Van Hecke | DEF | 6 | 4.5 | 0.91 | 3.61 | 6.57 | 5.00 | 27.0 | 60.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 12.87 | 21.59 | 2.00 | 86.3 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.23 | 9.13 | 14.97 | 5.00 | 80.0 | 89.0 |
| Bench 3 | Bench Boost | Mateta | FWD | 8 | 7.5 | 1.60 | 3.99 | 7.44 | 0.00 | 18.2 | 0.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.45 | 14.15 | 21.84 | 2.00 | 91.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 4.88 | 14.03 | 24.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 4.33 | 13.29 | 23.84 | 2.00 | 81.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 4.76 | 12.30 | 19.59 | 14.00 | 94.2 | 180.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.19 | 10.96 | 17.87 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 2.50 -> 2.40
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: B.Fernandes
- Effective captain: Rice
- Chip used: none
- Predicted score: 53.57
- Actual score: 48.00
- Transfer: Mateta -> João Pedro (projected gain 5.79, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 11.45 | 17.10 | 3.00 | 111.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.93 | 12.69 | 2.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.82 | 13.70 | 19.67 | 3.00 | 107.5 | 56.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.06 | 11.30 | 18.09 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.63 | 11.05 | 16.67 | 2.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.8 | 2.97 | 7.90 | 12.86 | 5.00 | 85.9 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.5 | 1.63 | 5.39 | 8.97 | 9.00 | 47.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.44 | 13.59 | 21.93 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 10.45 | 16.89 | 2.00 | 85.8 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.26 | 9.38 | 15.40 | 4.00 | 77.7 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 5.75 | 16.88 | 26.72 | 4.00 | 119.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.67 | 13.74 | 20.68 | 4.00 | 94.0 | 86.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.8 | 5.20 | 13.68 | 22.87 | 2.00 | 81.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.70 | 18.00 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Wilson | MID | 10 | 6.0 | 2.88 | 9.20 | 15.49 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 2.40 -> 4.60
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rice
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 50.39
- Actual score: 90.00
- Transfer: Rogers -> Rayan (projected gain 1.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.47 | 14.63 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 12.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.59 | 11.83 | 18.26 | 8.00 | 88.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.12 | 11.29 | 18.09 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.32 | 10.04 | 15.46 | 6.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.96 | 8.22 | 13.32 | 4.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.4 | 2.73 | 7.30 | 11.44 | 4.00 | 74.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.20 | 13.99 | 20.62 | 2.00 | 62.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.47 | 13.02 | 20.50 | 6.00 | 84.2 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.49 | 11.90 | 18.85 | 7.00 | 86.6 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.6 | 5.12 | 15.02 | 23.37 | 5.00 | 102.6 | 75.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.8 | 5.20 | 13.94 | 22.96 | 13.00 | 82.3 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 4.59 | 13.41 | 21.59 | 8.00 | 89.4 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 3.62 | 10.92 | 17.14 | 12.00 | 87.6 | 71.0 |
| Bench 2 | Bench | Rayan | MID | 4 | 5.5 | 3.41 | 9.85 | 16.04 | 2.00 | 80.5 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 4.60 -> 3.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 53.10
- Actual score: 73.00
- Transfer: J.Timber -> Gabriel (projected gain 4.17, hit 0)
- Autosub outfielders: Rayan.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.42 | 9.46 | 14.50 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.47 | 7.44 | 12.26 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.81 | 14.07 | 20.97 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 11.66 | 18.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.88 | 10.50 | 15.85 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.9 | 2.92 | 9.03 | 14.41 | 11.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.4 | 2.36 | 7.16 | 11.50 | 2.00 | 83.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.27 | 13.00 | 20.33 | 19.00 | 84.9 | 84.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.92 | 12.68 | 20.99 | 4.00 | 90.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.50 | 17.83 | 2.00 | 86.2 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.93 | 15.91 | 24.04 | 7.00 | 100.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 4.45 | 14.04 | 21.78 | 8.00 | 90.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 4.35 | 13.68 | 21.40 | 3.00 | 96.1 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 3.87 | 10.50 | 16.51 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Autosub In | Rayan | MID | 4 | 5.6 | 3.17 | 8.97 | 14.17 | 3.00 | 83.2 | 73.0 |

## GW30

- Train rows: 183541
- Bank: 3.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: Semenyo
- Effective captain: João Pedro
- Chip used: triple_captain
- Predicted score: 58.56
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Wilson -> Mbeumo (projected gain 3.19, hit 0)
- Chip used: Triple Captain on João Pedro. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.44 | 8.62 | 12.82 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 8.15 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 11.63 | 17.67 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 3.76 | 11.52 | 18.66 | 9.00 | 79.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.56 | 9.09 | 13.77 | 2.00 | 87.8 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.9 | 3.16 | 8.46 | 13.05 | 10.00 | 91.0 | 90.0 |
| Bench 4 | Bench | Van Hecke | DEF | 6 | 4.4 | 2.47 | 7.63 | 11.34 | 9.00 | 85.8 | 90.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.6 | 5.88 | 15.76 | 23.72 | 2.00 | 94.1 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.5 | 3.99 | 12.07 | 21.18 | 6.00 | 88.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.00 | 10.69 | 16.03 | 6.00 | 87.3 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.2 | 5.65 | 15.55 | 23.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 4.83 | 14.44 | 22.97 | 10.00 | 77.1 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 3.65 | 11.60 | 18.63 | 2.00 | 67.4 | 74.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.04 | 10.93 | 18.13 | 3.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Rayan | MID | 4 | 5.6 | 3.03 | 8.87 | 14.04 | 3.00 | 76.7 | 86.0 |