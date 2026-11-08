# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 917.63
- Total actual points: 1025.00
- Average predicted points: 48.30
- Average actual points: 53.95
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: M.Salah
- Vice captain: Semenyo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 49.78
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Muñoz, Van de Ven, Flemming.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.81 | 10.92 | 16.86 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.27 | 13.46 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 3.55 | 12.16 | 20.18 | 0.00 | 70.1 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 10.28 | 17.17 | 3.00 | 90.0 | 90.0 |
| XI | XI | Lacroix | DEF | 8 | 5.0 | 3.74 | 10.15 | 15.45 | 11.00 | 86.6 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.18 | 10.01 | 16.41 | 0.00 | 93.4 | 90.0 |
| Bench 2 | Autosub In | Muñoz | DEF | 8 | 5.7 | 3.34 | 9.18 | 15.37 | 14.00 | 83.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 3.87 | 12.84 | 20.93 | 1.00 | 76.4 | 59.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 3.85 | 11.33 | 17.41 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Autosub In | Flemming | FWD | 3 | 5.3 | 2.46 | 6.65 | 10.68 | 2.00 | 72.2 | 71.0 |
| Vice Captain | Bench | Semenyo | MID | 4 | 8.1 | 4.63 | 14.34 | 22.77 | 0.00 | 76.6 | 0.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.2 | 5.28 | 14.15 | 23.32 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 4.45 | 13.65 | 20.64 | 1.00 | 91.3 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 3.58 | 12.08 | 19.18 | 0.00 | 84.9 | 0.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.97 | 11.84 | 18.55 | 6.00 | 87.1 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 46.82
- Actual score: 37.00
- Transfer: Gabriel -> J.Timber (projected gain 2.69, hit 0)
- Autosub outfielders: Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.15 | 9.28 | 14.19 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.81 | 8.43 | 12.38 | 1.00 | 92.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.93 | 12.20 | 20.60 | 2.00 | 92.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.2 | 3.47 | 11.93 | 19.79 | 2.00 | 82.9 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 3.57 | 9.81 | 16.20 | 1.00 | 88.4 | 90.0 |
| XI | XI | Lacroix | DEF | 8 | 5.0 | 3.14 | 9.45 | 15.49 | 3.00 | 85.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.17 | 9.10 | 13.94 | 0.00 | 86.9 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 3.94 | 11.16 | 17.36 | 13.00 | 83.2 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.04 | 9.94 | 15.98 | 6.00 | 46.4 | 90.0 |
| Bench 4 | Bench | Flemming | FWD | 3 | 5.3 | 1.61 | 5.87 | 9.81 | 6.00 | 42.5 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.86 | 14.90 | 23.30 | 1.00 | 84.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.85 | 14.90 | 24.17 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.83 | 13.96 | 22.81 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Autosub In | Semenyo | MID | 4 | 8.0 | 3.02 | 9.36 | 16.41 | 1.00 | 34.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 2.50 | 7.93 | 14.30 | -2.00 | 62.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Mbeumo
- Effective captain: Rice
- Chip used: none
- Predicted score: 44.29
- Actual score: 45.00
- Transfer: Van de Ven -> O'Reilly (projected gain 2.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.21 | 9.23 | 14.46 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 12.64 | 2.00 | 91.3 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 3.57 | 11.92 | 19.41 | 14.00 | 85.2 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.1 | 3.55 | 11.12 | 17.83 | 0.00 | 85.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.34 | 9.49 | 14.87 | 1.00 | 83.4 | 46.0 |
| XI | XI | Lacroix | DEF | 8 | 5.0 | 3.08 | 9.20 | 15.01 | 8.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 2.95 | 9.06 | 15.02 | 0.00 | 73.4 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 3.65 | 11.65 | 19.20 | 1.00 | 68.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.78 | 11.03 | 19.61 | 2.00 | 84.1 | 63.0 |
| Bench 3 | Bench | Flemming | FWD | 3 | 5.3 | 2.63 | 7.23 | 11.15 | 1.00 | 77.9 | 58.0 |
| Captain | Captain | Rice | MID | 1 | 7.0 | 4.47 | 14.27 | 23.96 | 3.00 | 89.0 | 82.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.6 | 4.27 | 13.17 | 20.43 | 2.00 | 87.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 3.78 | 11.22 | 18.86 | 4.00 | 79.8 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.12 | 10.01 | 16.97 | 1.00 | 55.8 | 45.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 6.0 | 2.32 | 7.13 | 12.18 | 0.00 | 62.0 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.37
- Actual score: 61.00
- Transfer: Lacroix -> Guéhi (projected gain 4.50, hit 0)
- Autosub outfielders: Flemming, Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.30 | 10.43 | 16.63 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.76 | 13.77 | 3.00 | 91.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.44 | 12.92 | 20.63 | 8.00 | 94.1 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 4.07 | 12.21 | 19.32 | 0.00 | 92.5 | 0.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 3.51 | 10.19 | 15.82 | 6.00 | 81.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.97 | 8.99 | 14.09 | 3.00 | 76.8 | 90.0 |
| Bench 3 | Autosub In | Senesi | DEF | 4 | 5.0 | 1.65 | 5.36 | 10.51 | 8.00 | 30.5 | 61.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.52 | 11.44 | 19.37 | 2.00 | 76.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 3.40 | 11.07 | 18.79 | 2.00 | 75.1 | 90.0 |
| Bench 2 | Autosub In | Flemming | FWD | 3 | 5.3 | 2.08 | 6.54 | 10.34 | 5.00 | 60.9 | 4.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.94 | 14.02 | 23.14 | 8.00 | 85.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.03 | 13.23 | 23.07 | 6.00 | 85.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.12 | 12.21 | 19.92 | 3.00 | 85.0 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 3.13 | 9.46 | 15.43 | 0.00 | 61.5 | 0.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 5.9 | 0.82 | 3.76 | 8.11 | 0.00 | 11.8 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 5.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 45.93
- Actual score: 52.00
- Transfer: M.Salah -> B.Fernandes (projected gain 6.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.84 | 10.01 | 15.21 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.20 | 8.45 | 12.84 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.86 | 11.41 | 17.85 | 1.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.75 | 10.05 | 15.71 | 2.00 | 87.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 2.90 | 9.24 | 14.98 | 1.00 | 76.3 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 3.05 | 8.01 | 12.95 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Muñoz | DEF | 8 | 6.1 | 2.16 | 7.33 | 12.01 | 0.00 | 32.6 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 3.65 | 12.78 | 21.11 | 2.00 | 73.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.11 | 9.31 | 15.76 | 2.00 | 56.6 | 62.0 |
| Bench 2 | Bench | Flemming | FWD | 3 | 5.3 | 2.64 | 7.15 | 11.53 | 1.00 | 63.0 | 28.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 4.75 | 13.72 | 22.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 4.50 | 13.62 | 23.34 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 3.82 | 11.89 | 18.90 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 10.46 | 17.50 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 5.8 | 1.11 | 4.30 | 8.65 | 0.00 | 18.4 | 0.0 |

## GW17

- Train rows: 173127
- Bank: 5.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 46.81
- Actual score: 56.00
- Transfer: Caicedo -> Foden (projected gain 8.65, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 9.40 | 14.73 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.84 | 8.18 | 12.06 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.80 | 11.28 | 17.67 | 1.00 | 89.1 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 3.36 | 9.90 | 15.29 | 6.00 | 83.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 2.95 | 9.59 | 16.16 | 6.00 | 79.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.12 | 8.64 | 14.46 | 4.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.0 | 1.05 | 4.68 | 9.75 | 0.00 | 13.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.30 | 11.57 | 17.91 | 2.00 | 55.8 | 90.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.9 | 2.35 | 7.77 | 14.00 | 2.00 | 57.7 | 76.0 |
| Bench 3 | Bench | Flemming | FWD | 3 | 5.3 | 2.04 | 6.43 | 10.68 | 1.00 | 31.7 | 64.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 5.12 | 16.27 | 24.45 | 3.00 | 85.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 5.09 | 15.99 | 25.73 | 1.00 | 92.2 | 45.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.27 | 21.76 | 11.00 | 82.5 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.11 | 12.23 | 18.94 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 3.72 | 11.29 | 21.27 | 0.00 | 78.8 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 2.10 -> 4.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.97
- Actual score: 38.00
- Transfer: Mbeumo -> Wilson (projected gain 3.45, hit 0)
- Autosub outfielders: Mateta, Flemming.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.37 | 9.53 | 14.47 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 7.98 | 12.09 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 9.96 | 15.69 | 2.00 | 90.5 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 3.15 | 9.07 | 14.22 | 1.00 | 85.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.04 | 9.03 | 15.24 | 2.00 | 88.9 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 2.96 | 8.77 | 14.20 | 0.00 | 65.5 | 0.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.01 | 3.48 | 7.40 | 0.00 | 10.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.59 | 11.92 | 18.76 | 5.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.8 | 2.90 | 8.78 | 14.93 | 2.00 | 70.5 | 90.0 |
| Bench 3 | Autosub In | Flemming | FWD | 3 | 5.3 | 2.36 | 6.77 | 11.00 | 1.00 | 62.6 | 2.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.00 | 15.23 | 23.96 | 2.00 | 87.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.27 | 23.51 | 0.00 | 84.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 12.81 | 20.36 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.29 | 21.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.7 | 3.57 | 12.13 | 19.95 | 5.00 | 77.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 4.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 44.94
- Actual score: 43.00
- Transfer: Flemming -> Ekitiké (projected gain 4.54, hit 0)
- Autosub outfielders: J.Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.21 | 9.13 | 13.94 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.12 | 8.75 | 13.57 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.43 | 9.91 | 15.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 3.05 | 8.88 | 14.94 | 1.00 | 83.2 | 56.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 2.65 | 8.85 | 13.96 | 3.00 | 74.4 | 90.0 |
| Bench 3 | Autosub In | J.Timber | DEF | 1 | 6.5 | 2.34 | 7.25 | 11.87 | 9.00 | 29.3 | 82.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.06 | 3.65 | 6.78 | 0.00 | 10.5 | 0.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 4.07 | 12.80 | 20.76 | 2.00 | 75.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.42 | 11.22 | 19.61 | 2.00 | 80.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 3.01 | 8.55 | 13.38 | 9.00 | 74.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 15.39 | 27.34 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.75 | 19.84 | 5.00 | 94.2 | 90.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.66 | 21.91 | 0.00 | 84.9 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.95 | 11.37 | 17.92 | 2.00 | 87.1 | 84.0 |
| Bench 2 | Bench | B.Fernandes | MID | 14 | 9.2 | 2.51 | 8.45 | 15.66 | 0.00 | 17.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.90 -> 3.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.02
- Actual score: 43.00
- Transfer: B.Fernandes -> Cherki (projected gain 5.18, hit 0)
- Autosub outfielders: O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.10 | 9.01 | 14.46 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.16 | 12.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.33 | 10.34 | 16.01 | 2.00 | 94.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.13 | 9.27 | 15.48 | 3.00 | 72.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 2.89 | 8.35 | 14.32 | 1.00 | 86.8 | 90.0 |
| Bench 2 | Autosub In | O'Reilly | DEF | 13 | 5.3 | 2.62 | 7.39 | 12.14 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.8 | 1.07 | 4.14 | 7.84 | 0.00 | 16.0 | 0.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 3.79 | 11.13 | 17.47 | 0.00 | 74.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.35 | 10.33 | 16.97 | 17.00 | 81.4 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 3.29 | 9.18 | 15.05 | 2.00 | 80.9 | 86.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 14.48 | 23.60 | 2.00 | 86.8 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.98 | 12.47 | 22.30 | 4.00 | 83.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.03 | 12.14 | 19.79 | 6.00 | 83.9 | 84.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 12.02 | 19.33 | 1.00 | 92.4 | 90.0 |
| Bench 3 | Bench | Rice | MID | 1 | 7.2 | 1.94 | 6.78 | 12.36 | 17.00 | 29.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 3.30 -> 3.50
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 46.40
- Actual score: 59.00
- Transfer: Muñoz -> Tarkowski (projected gain 3.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.05 | 8.53 | 13.69 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 12.38 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 3.79 | 11.50 | 18.12 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 10.00 | 16.42 | 6.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.97 | 8.28 | 13.68 | 6.00 | 78.1 | 90.0 |
| Bench 2 | Bench | O'Reilly | DEF | 13 | 5.3 | 2.83 | 7.78 | 12.29 | 1.00 | 79.3 | 17.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.67 | 7.64 | 13.17 | 6.00 | 81.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 11.17 | 17.55 | 12.00 | 91.8 | 81.0 |
| Bench 4 | Bench | Ekitiké | FWD | 12 | 9.1 | 2.40 | 9.04 | 15.00 | 0.00 | 30.6 | 0.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.28 | 8.96 | 15.12 | 2.00 | 76.9 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.84 | 14.26 | 22.51 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.09 | 19.59 | 6.00 | 91.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.86 | 11.95 | 21.07 | 3.00 | 79.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.05 | 11.46 | 17.92 | 1.00 | 84.3 | 17.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.91 | 10.40 | 17.00 | 9.00 | 83.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 3.50 -> 2.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Watkins
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 43.81
- Actual score: 37.00
- Transfer: Mateta -> Watkins (projected gain 3.81, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.23 | 9.29 | 14.80 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.86 | 7.97 | 12.70 | 5.00 | 92.3 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.18 | 9.99 | 16.33 | 8.00 | 90.2 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.36 | 9.56 | 15.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.24 | 9.42 | 14.55 | 5.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.8 | 2.92 | 8.31 | 13.50 | 3.00 | 86.6 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.3 | 1.85 | 5.69 | 9.26 | -1.00 | 36.0 | 45.0 |
| Vice Captain | XI | Watkins | FWD | 2 | 8.7 | 4.04 | 12.08 | 18.45 | 2.00 | 80.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.96 | 11.95 | 20.28 | 2.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Ekitiké | FWD | 12 | 9.0 | 2.62 | 8.10 | 14.25 | 2.00 | 36.8 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.12 | 12.93 | 20.65 | 2.00 | 90.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 3.44 | 11.40 | 19.52 | 3.00 | 76.7 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 11.32 | 19.34 | 1.00 | 74.5 | 45.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 3.44 | 11.29 | 18.97 | 1.00 | 70.9 | 45.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.77 | 10.83 | 17.01 | 2.00 | 86.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 2.40 -> 1.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 44.19
- Actual score: 44.00
- Transfer: Senesi -> Chalobah (projected gain 1.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.40 | 9.98 | 15.66 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.51 | 13.30 | 5.00 | 94.6 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.5 | 3.48 | 10.60 | 16.52 | 4.00 | 90.5 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.40 | 9.94 | 16.44 | 4.00 | 87.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.01 | 9.22 | 14.59 | 1.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 2.49 | 7.25 | 11.93 | 6.00 | 41.8 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.2 | 2.02 | 6.15 | 9.82 | 6.00 | 44.7 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.38 | 11.23 | 19.29 | 1.00 | 50.9 | 31.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.96 | 10.88 | 17.34 | 2.00 | 91.7 | 90.0 |
| Bench 2 | Bench | Watkins | FWD | 2 | 8.8 | 3.19 | 9.63 | 15.38 | 8.00 | 76.9 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.26 | 12.60 | 19.88 | 8.00 | 87.3 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.3 | 4.17 | 12.57 | 19.44 | 1.00 | 89.9 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.08 | 12.01 | 19.20 | 10.00 | 83.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 3.56 | 10.55 | 17.84 | 3.00 | 59.7 | 72.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.22 | 10.07 | 17.45 | 1.00 | 54.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 1.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 45.88
- Actual score: 60.00
- Transfer: Foden -> Rogers (projected gain 4.93, hit 0)
- Autosub outfielders: Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.24 | 9.34 | 14.81 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 9.02 | 14.68 | 1.00 | 96.6 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.6 | 3.54 | 10.54 | 16.24 | 3.00 | 89.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.40 | 10.42 | 17.00 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.2 | 2.96 | 8.55 | 13.80 | 3.00 | 81.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.03 | 8.44 | 13.78 | 5.00 | 81.2 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.1 | 2.49 | 7.15 | 11.68 | 1.00 | 74.9 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.43 | 11.43 | 17.88 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Watkins | FWD | 2 | 8.8 | 3.80 | 10.75 | 17.10 | 0.00 | 78.7 | 0.0 |
| Bench 2 | Autosub In | Ekitiké | FWD | 12 | 8.9 | 3.24 | 10.11 | 16.63 | 13.00 | 61.1 | 83.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 4.40 | 14.98 | 25.24 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 4.86 | 13.92 | 22.15 | 7.00 | 92.1 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.00 | 12.11 | 19.46 | 2.00 | 89.7 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.02 | 11.48 | 17.85 | 3.00 | 88.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.29 | 9.55 | 16.15 | 8.00 | 47.3 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 2.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Semenyo
- Effective captain: Rogers
- Chip used: none
- Predicted score: 47.65
- Actual score: 57.00
- Transfer: Cherki -> Enzo (projected gain 1.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.90 | 10.96 | 16.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.59 | 13.44 | 1.00 | 93.9 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 3.50 | 11.13 | 17.46 | 4.00 | 87.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.90 | 10.96 | 17.66 | 6.00 | 79.5 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.41 | 10.29 | 16.79 | 2.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 2.97 | 8.29 | 13.45 | 3.00 | 82.0 | 90.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 5.0 | 2.03 | 6.62 | 10.61 | 2.00 | 77.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.28 | 12.27 | 20.77 | 5.00 | 85.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 3.81 | 11.33 | 19.11 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Watkins | FWD | 2 | 8.8 | 1.87 | 6.41 | 11.18 | 2.00 | 20.6 | 85.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.39 | 14.19 | 22.15 | 2.00 | 92.2 | 90.0 |
| Captain | Captain | Rogers | MID | 2 | 7.7 | 4.92 | 14.01 | 22.02 | 10.00 | 87.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.19 | 12.46 | 20.18 | 5.00 | 87.1 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 4.03 | 11.94 | 19.83 | 2.00 | 82.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.42 | 11.09 | 17.83 | 2.00 | 85.4 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 2.50 -> 3.70
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: bench_boost
- Predicted score: 60.95
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.85) beats the best remaining Bench Boost opportunity (11.43).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Watkins -> João Pedro (projected gain 3.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.85) beats the best remaining Bench Boost opportunity (11.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.08 | 15.16 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.02 | 12.43 | 1.00 | 92.9 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 3.57 | 11.29 | 17.64 | 3.00 | 88.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.24 | 10.20 | 15.37 | 3.00 | 127.3 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.60 | 9.82 | 15.51 | 7.00 | 74.1 | 90.0 |
| Bench 3 | Bench Boost | Tarkowski | DEF | 9 | 5.8 | 2.87 | 8.60 | 14.39 | 1.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | O'Reilly | DEF | 13 | 5.0 | 2.81 | 7.42 | 11.09 | 13.00 | 81.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 12.87 | 21.29 | 2.00 | 86.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.99 | 12.01 | 17.96 | 10.00 | 73.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.74 | 10.19 | 15.75 | 2.00 | 77.0 | 87.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 4.76 | 13.40 | 21.19 | 14.00 | 113.2 | 180.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.15 | 12.45 | 19.74 | 2.00 | 91.0 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.48 | 12.23 | 19.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.8 | 3.94 | 11.08 | 17.72 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Bench Boost | Wilson | MID | 10 | 6.1 | 3.19 | 10.26 | 16.47 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 3.70 -> 3.60
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 52.78
- Actual score: 46.00
- Transfer: Tarkowski -> Virgil (projected gain 2.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 11.05 | 16.80 | 3.00 | 116.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.93 | 12.69 | 2.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.12 | 12.20 | 18.87 | 3.00 | 99.5 | 56.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.06 | 11.30 | 18.39 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.63 | 11.05 | 17.37 | 2.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Chalobah | DEF | 7 | 5.8 | 3.33 | 9.14 | 14.46 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 4.9 | 2.96 | 8.24 | 12.01 | 17.00 | 80.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.44 | 13.19 | 22.63 | 7.00 | 85.6 | 79.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.93 | 11.12 | 16.97 | 2.00 | 77.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 10.45 | 17.59 | 2.00 | 85.8 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 5.75 | 16.88 | 26.72 | 4.00 | 130.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 4.97 | 14.44 | 21.88 | 4.00 | 94.0 | 86.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.70 | 18.40 | 2.00 | 83.2 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 4.14 | 11.63 | 17.90 | 2.00 | 87.4 | 90.0 |
| Bench 4 | Bench | Wilson | MID | 10 | 6.0 | 2.88 | 9.20 | 15.49 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 3.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rice
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 49.55
- Actual score: 84.00
- Transfer: Rogers -> B.Fernandes (projected gain 3.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.47 | 14.63 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 11.96 | 0.00 | 89.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.32 | 11.44 | 16.56 | 6.00 | 90.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.59 | 11.13 | 16.86 | 8.00 | 88.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.82 | 10.69 | 17.59 | 7.00 | 89.0 | 90.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 4.9 | 3.23 | 9.37 | 14.15 | 6.00 | 81.6 | 69.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.8 | 2.68 | 8.14 | 13.51 | 1.00 | 87.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.47 | 13.32 | 22.20 | 6.00 | 84.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.20 | 13.29 | 20.62 | 2.00 | 81.6 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 8.9 | 3.55 | 10.80 | 16.15 | 15.00 | 76.5 | 75.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.6 | 4.72 | 14.32 | 23.37 | 5.00 | 97.6 | 75.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.8 | 4.80 | 13.94 | 22.96 | 13.00 | 82.3 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 4.59 | 13.41 | 21.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.02 | 11.62 | 17.84 | 12.00 | 87.6 | 71.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 3.74 | 11.28 | 17.87 | 1.00 | 83.7 | 85.0 |

## GW29

- Train rows: 182721
- Bank: 1.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 52.56
- Actual score: 72.00
- Transfer: J.Timber -> Gabriel (projected gain 3.07, hit 0)
- Autosub outfielders: Enzo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.72 | 9.46 | 14.20 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.14 | 12.96 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.51 | 13.27 | 20.97 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 11.66 | 18.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.88 | 10.50 | 15.85 | 1.00 | 90.8 | 90.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.7 | 2.48 | 8.19 | 14.20 | 2.00 | 83.7 | 90.0 |
| Bench 2 | Bench | O'Reilly | DEF | 13 | 5.0 | 2.93 | 7.81 | 12.26 | 0.00 | 46.4 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.27 | 13.00 | 20.33 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.80 | 17.83 | 2.00 | 86.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.78 | 10.97 | 16.56 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.93 | 15.91 | 24.44 | 7.00 | 97.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 3.95 | 12.78 | 20.40 | 3.00 | 99.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 4.45 | 12.74 | 20.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 3.87 | 10.50 | 16.51 | 0.00 | 84.0 | 0.0 |
| Bench 3 | Autosub In | Enzo | MID | 7 | 6.8 | 2.92 | 9.99 | 16.75 | 4.00 | 78.7 | 78.0 |

## GW30

- Train rows: 183541
- Bank: 0.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: Semenyo
- Effective captain: João Pedro
- Chip used: triple_captain
- Predicted score: 58.94
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Wilson -> Anderson (projected gain 0.90, hit 0)
- Chip used: Triple Captain on João Pedro. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 9.62 | 14.92 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 8.15 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 11.63 | 17.67 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 3.76 | 11.52 | 18.66 | 9.00 | 96.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.56 | 9.09 | 13.47 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Chalobah | DEF | 7 | 5.6 | 3.02 | 8.76 | 13.92 | 2.00 | 83.6 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.1 | 1.87 | 5.29 | 8.69 | 2.00 | 26.9 | 90.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.6 | 5.88 | 16.46 | 24.82 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 4.02 | 12.07 | 18.47 | 1.00 | 74.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.00 | 10.39 | 16.33 | 6.00 | 87.3 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.2 | 5.65 | 15.55 | 23.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 4.83 | 14.44 | 22.97 | 10.00 | 94.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.04 | 11.23 | 18.43 | 3.00 | 83.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.69 | 11.05 | 17.50 | 2.00 | 89.1 | 87.0 |
| Bench 2 | Bench | Enzo | MID | 7 | 6.7 | 3.26 | 10.22 | 16.09 | 2.00 | 74.5 | 90.0 |