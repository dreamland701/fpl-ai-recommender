# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW10
- Simulated weeks: GW11-GW30
- Total predicted points: 1237.59
- Total actual points: 1066.00
- Average predicted points: 61.88
- Average actual points: 53.30
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Semenyo
- Vice captain: Guéhi
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.68
- Actual score: 42.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Thiago.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.8 | 4.17 | 12.04 | 18.65 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.76 | 10.18 | 16.05 | 2.00 | 98.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.5 | 5.24 | 16.47 | 27.04 | 1.00 | 90.4 | 90.0 |
| Vice Captain | Bench | Guéhi | DEF | 8 | 5.0 | 5.66 | 15.89 | 25.55 | 0.00 | 95.3 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 4.77 | 13.64 | 21.89 | 1.00 | 91.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.50 | 13.48 | 22.56 | 2.00 | 96.3 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.51 | 13.33 | 21.73 | 6.00 | 83.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.95 | 14.22 | 24.27 | 7.00 | 80.1 | 82.0 |
| Bench 3 | Autosub In | Thiago | FWD | 5 | 6.2 | 3.82 | 11.00 | 17.40 | 13.00 | 73.4 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 3.00 | 8.42 | 13.47 | 2.00 | 63.5 | 62.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.06 | 18.22 | 29.32 | 0.00 | 99.2 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.3 | 5.16 | 16.00 | 25.35 | 7.00 | 80.1 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 4.99 | 15.24 | 25.36 | 2.00 | 74.8 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.7 | 4.62 | 14.39 | 22.84 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Kudus | MID | 18 | 6.7 | 4.33 | 12.95 | 21.33 | 0.00 | 80.0 | 0.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 62.99
- Actual score: 41.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 39.00
- Transfer: Kudus -> Caicedo (projected gain 0.80, hit 0)
- Autosub outfielders: Thiago, Guéhi, Isidor.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.31 | 11.92 | 18.46 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 95.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.54 | 12.48 | 20.47 | 14.00 | 79.3 | 90.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.1 | 4.02 | 11.34 | 18.91 | 5.00 | 55.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.60 | 15.64 | 24.41 | 1.00 | 88.7 | 75.0 |
| Bench 2 | Autosub In | Thiago | FWD | 5 | 6.2 | 4.35 | 12.53 | 19.81 | 4.00 | 84.2 | 90.0 |
| Bench 4 | Autosub In | Isidor | FWD | 17 | 5.6 | 2.82 | 7.85 | 12.43 | 2.00 | 59.5 | 63.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 96.6 | 0.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 92.3 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 5.48 | 15.35 | 24.62 | 2.00 | 77.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 4.97 | 15.04 | 23.65 | 6.00 | 85.1 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.48 | 13.18 | 20.88 | 0.00 | 81.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.70
- Actual score: 29.00
- League average score: 35.00
- Transfer: Gabriel -> J.Timber (projected gain 0.35, hit 0)
- Autosub outfielders: Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.75 | 11.08 | 17.59 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 94.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 4.97 | 13.81 | 22.20 | 1.00 | 87.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 93.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.2 | 4.27 | 12.93 | 20.79 | 2.00 | 78.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.44 | 12.78 | 21.17 | 0.00 | 79.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.27 | 12.40 | 19.84 | 0.00 | 85.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.22 | 14.59 | 23.27 | 1.00 | 85.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.04 | 13.96 | 21.86 | 13.00 | 80.2 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.63 | 7.68 | 12.29 | 2.00 | 54.5 | 62.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.36 | 15.90 | 25.10 | 1.00 | 82.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 93.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 5.23 | 14.96 | 23.81 | 0.00 | 74.0 | 0.0 |
| Bench 2 | Autosub In | Semenyo | MID | 4 | 8.0 | 4.12 | 12.76 | 22.01 | 1.00 | 53.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 2.80 | 9.03 | 15.50 | -2.00 | 47.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 1.00 -> 6.30
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 56.64
- Actual score: 54.00
- League average score: 58.00
- Transfer: M.Salah -> B.Fernandes (projected gain 3.06, hit 0)
- Autosub outfielders: Guéhi, Isidor.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.91 | 11.03 | 17.36 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 92.3 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 93.4 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.54 | 12.99 | 20.67 | 1.00 | 80.4 | 46.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 4.47 | 12.92 | 20.71 | 14.00 | 82.2 | 90.0 |
| XI | Bench | Van de Ven | DEF | 18 | 4.8 | 4.01 | 12.23 | 19.53 | 0.00 | 83.8 | 0.0 |
| Bench 2 | Autosub In | Guéhi | DEF | 8 | 5.1 | 3.95 | 11.50 | 18.89 | 14.00 | 77.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.05 | 15.65 | 25.20 | 1.00 | 88.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.11 | 12.66 | 21.16 | 2.00 | 67.0 | 90.0 |
| Bench 4 | Autosub In | Isidor | FWD | 17 | 5.6 | 2.10 | 6.64 | 10.80 | 1.00 | 50.9 | 28.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.27 | 15.47 | 25.56 | 3.00 | 88.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.47 | 15.47 | 24.93 | 2.00 | 85.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.01 | 14.52 | 23.67 | 4.00 | 87.8 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.78 | 14.02 | 23.66 | 4.00 | 73.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.0 | 2.52 | 8.33 | 14.98 | 0.00 | 47.0 | 0.0 |

## GW15

- Train rows: 171608
- Bank: 6.30 -> 4.10
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.61
- Actual score: 77.00
- League average score: 49.00
- Transfer: Caicedo -> Foden (projected gain 6.17, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.00 | 11.73 | 18.63 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 93.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 96.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 12.19 | 19.99 | 3.00 | 69.8 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.55 | 8.26 | 15.61 | 8.00 | 46.5 | 61.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.72 | 8.12 | 13.97 | 6.00 | 50.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.42 | 13.89 | 22.48 | 1.00 | 77.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.10 | 12.17 | 19.79 | 2.00 | 67.1 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 1.63 | 5.75 | 9.93 | 1.00 | 42.1 | 55.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.32 | 15.51 | 25.22 | 3.00 | 82.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.29 | 15.27 | 24.54 | 18.00 | 84.5 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.44 | 15.12 | 24.34 | 8.00 | 83.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.63 | 14.43 | 24.17 | 6.00 | 82.4 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.1 | 5.09 | 14.13 | 22.29 | 12.00 | 88.6 | 68.0 |

## GW16

- Train rows: 172367
- Bank: 4.10 -> 2.60
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 59.44
- Actual score: 62.00
- League average score: 60.00
- Transfer: Van de Ven -> Cucurella (projected gain 1.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.34 | 11.61 | 18.01 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 91.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 94.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.75 | 13.35 | 20.91 | 2.00 | 85.0 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 4.41 | 12.91 | 20.61 | 6.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Muñoz | DEF | 8 | 6.1 | 3.36 | 10.73 | 17.91 | 0.00 | 49.6 | 0.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 3.40 | 10.44 | 17.68 | 1.00 | 68.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.55 | 13.78 | 22.21 | 2.00 | 74.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.86 | 11.86 | 20.11 | 2.00 | 61.1 | 80.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.51 | 7.02 | 11.34 | 0.00 | 51.9 | 20.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 99.0 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.4 | 5.11 | 15.66 | 24.96 | 11.00 | 72.6 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.30 | 15.02 | 24.64 | 2.00 | 85.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.82 | 14.49 | 23.70 | 6.00 | 83.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.93 | 13.96 | 23.10 | 2.00 | 85.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 2.60 -> 2.70
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.09
- Actual score: 53.00
- League average score: 66.00
- Transfer: Muñoz -> Virgil (projected gain 1.16, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.30 | 17.83 | 7.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.34 | 9.38 | 14.76 | 2.00 | 88.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.24 | 12.82 | 21.00 | 2.00 | 88.2 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 4.21 | 12.62 | 20.37 | 1.00 | 87.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 3.95 | 12.09 | 19.96 | 6.00 | 74.8 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 3.72 | 10.54 | 17.96 | 4.00 | 72.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.60 | 14.57 | 23.21 | 2.00 | 66.8 | 90.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.3 | 3.72 | 11.78 | 20.11 | 6.00 | 67.8 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.5 | 1.99 | 6.09 | 10.19 | 1.00 | 38.9 | 18.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 94.2 | 45.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 6.22 | 18.57 | 28.95 | 3.00 | 83.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.21 | 14.53 | 23.74 | 10.00 | 84.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.42 | 13.47 | 22.76 | 11.00 | 78.5 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.12 | 13.09 | 22.97 | 0.00 | 72.8 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 2.70 -> 3.80
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 59.15
- Actual score: 42.00
- League average score: 44.00
- Transfer: Mbeumo -> Rogers (projected gain 2.74, hit 0)
- Autosub outfielders: Cucurella, Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.58 | 14.89 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| Bench 3 | Autosub In | Senesi | DEF | 4 | 4.9 | 4.14 | 12.83 | 20.64 | 2.00 | 89.9 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 4.56 | 12.77 | 20.20 | 0.00 | 85.5 | 0.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.38 | 12.41 | 19.86 | 2.00 | 89.0 | 90.0 |
| Bench 2 | Autosub In | Cucurella | DEF | 7 | 6.2 | 4.15 | 11.61 | 19.14 | 2.00 | 84.5 | 68.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.39 | 12.92 | 20.76 | 5.00 | 79.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.20 | 12.08 | 19.71 | 8.00 | 77.0 | 68.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.5 | 2.11 | 5.75 | 9.23 | 1.00 | 35.9 | 22.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.00 | 18.03 | 28.76 | 2.00 | 86.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.68 | 17.07 | 28.11 | 0.00 | 80.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.23 | 15.41 | 24.86 | 9.00 | 88.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.92 | 14.59 | 23.58 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.1 | 4.87 | 14.23 | 22.73 | 1.00 | 89.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 3.80 -> 7.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.58
- Actual score: 39.00
- League average score: 40.00
- Transfer: B.Fernandes -> Wilson (projected gain 4.06, hit 0)
- Autosub outfielders: J.Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.81 | 10.83 | 17.14 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 93.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.05 | 12.55 | 19.86 | 3.00 | 94.4 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.19 | 11.88 | 19.67 | 6.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Cucurella | DEF | 7 | 6.2 | 3.61 | 10.29 | 16.79 | 0.00 | 74.2 | 0.0 |
| Bench 3 | Autosub In | J.Timber | DEF | 1 | 6.5 | 3.04 | 8.95 | 15.07 | 9.00 | 45.3 | 82.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.22 | 12.42 | 21.01 | 2.00 | 75.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.19 | 11.47 | 18.43 | 1.00 | 74.1 | 27.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.4 | 1.46 | 4.90 | 8.56 | 1.00 | 30.4 | 32.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 96.2 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.95 | 14.27 | 22.72 | 2.00 | 88.1 | 84.0 |
| XI | XI | Rogers | MID | 2 | 7.3 | 4.49 | 14.17 | 23.25 | 1.00 | 83.0 | 81.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.68 | 14.06 | 22.91 | 0.00 | 82.9 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 7.20 -> 7.70
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.39
- Actual score: 45.00
- League average score: 42.00
- Transfer: Rice -> Cherki (projected gain 5.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.70 | 10.61 | 16.86 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 96.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.21 | 11.83 | 19.31 | 1.00 | 87.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.89 | 11.75 | 19.42 | 1.00 | 85.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.73 | 10.97 | 18.48 | 3.00 | 63.9 | 90.0 |
| Bench 4 | Bench | Cucurella | DEF | 7 | 6.2 | 1.72 | 6.46 | 11.78 | 0.00 | 41.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.05 | 11.63 | 19.17 | 17.00 | 76.4 | 90.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 3.13 | 9.66 | 16.06 | 2.00 | 60.3 | 61.0 |
| Bench 3 | Bench | Isidor | FWD | 17 | 5.4 | 1.74 | 5.05 | 8.46 | 0.00 | 35.1 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.01 | 17.38 | 28.20 | 2.00 | 84.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 93.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.08 | 14.87 | 23.50 | 4.00 | 80.0 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.4 | 4.94 | 13.83 | 22.19 | 5.00 | 82.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.63 | 13.24 | 21.29 | 6.00 | 80.9 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 7.70 -> 8.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.71
- Actual score: 63.00
- League average score: 48.00
- Transfer: Cucurella -> Tarkowski (projected gain 3.30, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.65 | 10.43 | 16.79 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 4.79 | 13.40 | 20.82 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 93.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.97 | 11.68 | 18.88 | 6.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Virgil | DEF | 12 | 5.9 | 3.37 | 10.60 | 17.52 | 6.00 | 83.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.57 | 10.14 | 17.57 | 6.00 | 76.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 92.8 | 81.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 3.46 | 10.22 | 16.51 | 1.00 | 61.7 | 15.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.3 | 0.81 | 3.28 | 5.91 | 0.00 | 20.5 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.84 | 16.56 | 27.11 | 2.00 | 82.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 92.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.15 | 14.96 | 23.22 | 1.00 | 85.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.59 | 13.97 | 22.39 | 3.00 | 77.8 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.91 | 13.90 | 22.30 | 9.00 | 84.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 8.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 60.95
- Actual score: 35.00
- League average score: 40.00
- Transfer: João Pedro -> Haaland (projected gain 11.86, hit 0)
- Autosub outfielders: Virgil.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.83 | 10.99 | 17.40 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 94.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 96.3 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.44 | 12.92 | 20.25 | 5.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 4.02 | 11.71 | 19.20 | 3.00 | 84.6 | 90.0 |
| Bench 2 | Autosub In | Virgil | DEF | 12 | 5.9 | 4.24 | 11.42 | 18.18 | 2.00 | 85.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 7.31 | 21.09 | 33.29 | 2.00 | 97.5 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.3 | 0.87 | 2.65 | 4.48 | 0.00 | 15.8 | 0.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 91.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 4.91 | 14.72 | 24.34 | 1.00 | 75.5 | 45.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.93 | 13.98 | 22.65 | 2.00 | 81.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.77 | 13.43 | 21.81 | 2.00 | 87.2 | 87.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.24 | 12.99 | 21.07 | 1.00 | 60.9 | 45.0 |

## GW23

- Train rows: 177836
- Bank: 0.30 -> 1.70
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Thiago
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.81
- Actual score: 43.00
- League average score: 44.00
- Transfer: Foden -> Rice (projected gain 3.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.10 | 11.58 | 18.16 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 97.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.61 | 13.22 | 20.59 | 1.00 | 83.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.70 | 13.14 | 21.44 | 4.00 | 86.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.31 | 12.13 | 19.16 | 3.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 12 | 5.9 | 3.73 | 10.94 | 17.52 | 9.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 3.29 | 9.55 | 16.23 | 6.00 | 53.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 7.25 | 19.86 | 31.58 | 1.00 | 89.7 | 17.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 92.7 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.2 | 0.66 | 2.03 | 3.83 | 1.00 | 7.6 | 15.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.46 | 15.60 | 25.18 | 8.00 | 85.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 5.37 | 15.57 | 24.54 | 1.00 | 89.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.06 | 14.30 | 23.04 | 8.00 | 81.8 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.68 | 13.11 | 21.50 | 10.00 | 79.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.46 | 12.45 | 20.94 | 3.00 | 60.7 | 72.0 |

## GW24

- Train rows: 178639
- Bank: 1.70 -> 1.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 60.14
- Actual score: 54.00
- League average score: 55.00
- Transfer: J.Timber -> Gabriel (projected gain 1.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.94 | 11.14 | 17.41 | 6.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 100.6 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.9 | 4.60 | 13.17 | 20.59 | 8.00 | 75.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.69 | 13.10 | 20.69 | 4.00 | 92.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.50 | 12.64 | 19.85 | 8.00 | 92.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.20 | 12.32 | 20.30 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.2 | 3.96 | 11.55 | 19.10 | 3.00 | 76.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.1 | 6.10 | 17.78 | 29.12 | 5.00 | 66.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 91.0 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.2 | 1.31 | 3.17 | 5.15 | 1.00 | 16.3 | 10.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 93.1 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.12 | 14.98 | 23.65 | 3.00 | 88.7 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.60 | 13.31 | 21.36 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Cherki | MID | 13 | 6.7 | 3.99 | 11.45 | 19.45 | 8.00 | 58.3 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 1.10 -> 2.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Semenyo
- Effective captain: Haaland
- Chip used: none
- Predicted score: 59.52
- Actual score: 62.00
- League average score: 58.00
- Transfer: Tarkowski -> Mukiele (projected gain 0.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.40 | 11.96 | 18.56 | 7.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 95.9 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.0 | 5.50 | 15.23 | 23.90 | 6.00 | 84.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.47 | 13.07 | 20.59 | 0.00 | 92.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.38 | 12.36 | 20.02 | 2.00 | 88.6 | 90.0 |
| XI | XI | Mukiele | DEF | 17 | 4.5 | 4.15 | 12.35 | 20.11 | 1.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.2 | 3.97 | 11.69 | 19.05 | 3.00 | 77.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 15.0 | 5.96 | 18.27 | 30.02 | 11.00 | 79.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.98 | 13.47 | 22.27 | 5.00 | 82.3 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.2 | 0.63 | 2.83 | 5.16 | 1.00 | 18.2 | 5.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 93.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.42 | 15.61 | 24.72 | 10.00 | 86.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.39 | 15.36 | 24.58 | 5.00 | 85.1 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 4.22 | 12.19 | 19.33 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Cherki | MID | 13 | 6.6 | 3.70 | 11.22 | 18.75 | 1.00 | 62.0 | 29.0 |

## GW26

- Train rows: 180267
- Bank: 2.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Gabriel
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 79.87
- Actual score: 94.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.85) beats the best remaining Bench Boost opportunity (15.34).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- League average score: 58.00
- Transfer: Isidor -> João Pedro (projected gain 3.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.85) beats the best remaining Bench Boost opportunity (15.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.17 | 12.88 | 19.56 | 3.00 | 112.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 93.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 6.40 | 16.55 | 25.50 | 7.00 | 118.7 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 94.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.19 | 12.64 | 20.13 | 17.00 | 91.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.09 | 11.65 | 19.22 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Mukiele | DEF | 17 | 4.6 | 4.01 | 11.12 | 18.07 | 2.00 | 78.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 13 | 14.9 | 6.69 | 19.19 | 30.88 | 5.00 | 85.3 | 45.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.09 | 14.21 | 22.26 | 10.00 | 74.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.42 | 13.87 | 22.99 | 2.00 | 84.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 6.26 | 16.30 | 25.59 | 14.00 | 114.2 | 180.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 92.0 | 90.0 |
| Bench 3 | Bench Boost | Wilson | MID | 10 | 6.1 | 3.89 | 12.06 | 19.37 | 2.00 | 84.7 | 71.0 |
| Bench 4 | Bench Boost | Cherki | MID | 13 | 6.6 | 3.47 | 9.61 | 15.97 | 1.00 | 49.2 | 19.0 |

## GW27

- Train rows: 181084
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 69.78
- Actual score: 50.00
- League average score: 45.00
- Transfer: Cherki -> Anderson (projected gain 0.79, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 117.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 7.29 | 20.72 | 32.03 | 2.00 | 138.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.16 | 14.70 | 23.49 | 11.00 | 96.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 98.2 | 90.0 |
| Bench 2 | Bench | Mukiele | DEF | 17 | 4.6 | 4.31 | 11.80 | 18.91 | 1.00 | 84.1 | 11.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 3.97 | 11.00 | 18.16 | 5.00 | 82.9 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 14.9 | 6.33 | 17.92 | 28.51 | 6.00 | 80.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.74 | 15.49 | 24.03 | 7.00 | 83.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.91 | 13.95 | 22.79 | 2.00 | 82.8 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 131.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 96.0 | 86.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.08 | 14.20 | 22.90 | 2.00 | 80.2 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 4.44 | 12.48 | 20.20 | 5.00 | 87.6 | 76.0 |
| Bench 4 | Bench | Wilson | MID | 10 | 6.0 | 3.38 | 10.40 | 17.39 | 8.00 | 69.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.20 -> 1.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rice
- Effective captain: Rice
- Chip used: none
- Predicted score: 65.40
- Actual score: 66.00
- League average score: 53.00
- Transfer: Mukiele -> Hill (projected gain 0.07, hit 0)
- Autosub outfielders: Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 95.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.78 | 16.70 | 26.68 | 9.00 | 108.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Hill | DEF | 4 | 4.0 | 4.31 | 12.14 | 19.26 | 2.00 | 91.9 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 4.8 | 4.06 | 11.02 | 17.82 | 4.00 | 84.9 | 90.0 |
| Captain | Bench | Haaland | FWD | 13 | 14.8 | 6.57 | 19.15 | 30.42 | 0.00 | 89.4 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.40 | 16.09 | 25.22 | 2.00 | 82.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.27 | 14.62 | 23.40 | 6.00 | 81.2 | 90.0 |
| Vice Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 108.6 | 75.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.97 | 13.91 | 22.28 | 2.00 | 82.9 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.52 | 13.02 | 20.44 | 12.00 | 86.6 | 71.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.4 | 4.34 | 12.50 | 20.08 | 1.00 | 82.7 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 65.05
- Actual score: 72.00
- League average score: 54.00
- Transfer: Rogers -> Mbeumo (projected gain 0.65, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 94.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.27 | 9.24 | 14.56 | 2.00 | 87.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.81 | 17.27 | 26.97 | 11.00 | 112.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 3.92 | 11.23 | 17.81 | 11.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Hill | DEF | 4 | 4.1 | 3.71 | 10.96 | 17.51 | 8.00 | 87.6 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 14.8 | 5.25 | 15.70 | 25.25 | 2.00 | 51.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.47 | 15.70 | 24.83 | 19.00 | 81.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.07 | 14.40 | 22.63 | 2.00 | 84.2 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 101.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 100.1 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 4.67 | 13.57 | 21.08 | 1.00 | 72.9 | 76.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 4.87 | 13.40 | 21.11 | 0.00 | 81.0 | 0.0 |
| Bench 3 | Bench | Anderson | MID | 16 | 5.4 | 3.84 | 11.90 | 18.97 | 12.00 | 83.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 71.08
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 43.00
- Transfer: Wilson -> Summerville (projected gain 0.06, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.40 | 9.35 | 14.52 | 6.00 | 88.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 5.26 | 15.52 | 24.66 | 9.00 | 99.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.13 | 14.63 | 22.87 | 2.00 | 86.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.46 | 12.29 | 19.07 | 2.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.9 | 4.26 | 11.96 | 18.45 | 10.00 | 92.0 | 90.0 |
| Bench 4 | Bench | Hill | DEF | 4 | 4.1 | 4.10 | 11.44 | 18.09 | 8.00 | 86.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 96.1 | 90.0 |
| XI | XI | Haaland | FWD | 13 | 14.7 | 5.39 | 16.28 | 26.50 | 2.00 | 67.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.00 | 13.79 | 21.33 | 6.00 | 86.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 103.0 | 74.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.54 | 13.53 | 22.43 | 3.00 | 80.0 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 4.55 | 13.00 | 20.63 | 2.00 | 68.4 | 74.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 4.59 | 12.65 | 19.90 | 2.00 | 88.1 | 87.0 |
| Bench 2 | Bench | Summerville | MID | 19 | 5.7 | 4.36 | 12.55 | 19.59 | 0.00 | 86.2 | 0.0 |