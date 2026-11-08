# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 915.18
- Total actual points: 1035.00
- Average predicted points: 48.17
- Average actual points: 54.47
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
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 51.54
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Van de Ven, Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.81 | 10.92 | 16.86 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.27 | 12.76 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 4.25 | 12.16 | 20.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 9.88 | 16.57 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.18 | 9.31 | 15.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 3.34 | 9.18 | 15.47 | 14.00 | 83.3 | 90.0 |
| Bench 3 | Autosub In | Ballard | DEF | 17 | 4.6 | 3.06 | 8.37 | 13.46 | 1.00 | 80.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.30 | 12.64 | 19.41 | 1.00 | 88.7 | 75.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 3.85 | 11.33 | 18.81 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.52 | 6.85 | 11.23 | 2.00 | 70.5 | 63.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 5.33 | 15.74 | 24.67 | 0.00 | 94.6 | 0.0 |
| Vice Captain | Captain | M.Salah | MID | 12 | 14.2 | 4.98 | 14.15 | 23.32 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 4.75 | 13.65 | 20.94 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.97 | 12.54 | 19.65 | 6.00 | 87.1 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.86 | 11.12 | 18.20 | 11.00 | 79.7 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 46.96
- Actual score: 29.00
- Transfer: Gabriel -> Guéhi (projected gain 0.83, hit 0)
- Autosub outfielders: Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.15 | 9.28 | 14.59 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.81 | 8.43 | 13.08 | 1.00 | 92.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.23 | 10.10 | 16.90 | 2.00 | 92.2 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 3.57 | 9.81 | 16.20 | 1.00 | 88.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.24 | 9.68 | 15.57 | 0.00 | 83.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.17 | 9.10 | 14.74 | 0.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 2.62 | 7.40 | 11.41 | 3.00 | 81.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.12 | 11.59 | 18.27 | 1.00 | 84.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 3.94 | 10.46 | 16.36 | 13.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.43 | 7.08 | 10.79 | 2.00 | 66.5 | 62.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.86 | 14.90 | 23.70 | 1.00 | 84.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.85 | 14.90 | 24.87 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.13 | 11.46 | 18.71 | 0.00 | 80.0 | 0.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.83 | 11.16 | 18.77 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Autosub In | Semenyo | MID | 4 | 8.0 | 3.02 | 9.36 | 16.71 | 1.00 | 34.8 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 1.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.21
- Actual score: 42.00
- Transfer: Guéhi -> J.Timber (projected gain 1.30, hit 0)
- Autosub outfielders: Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.21 | 9.63 | 14.76 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 14.04 | 2.00 | 91.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.34 | 9.49 | 14.87 | 1.00 | 83.4 | 46.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 3.27 | 9.42 | 15.61 | 14.00 | 85.2 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 3.35 | 9.16 | 15.02 | 0.00 | 92.4 | 0.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 2.91 | 8.63 | 14.43 | 0.00 | 85.8 | 0.0 |
| Bench 3 | Autosub In | Ballard | DEF | 17 | 4.6 | 2.49 | 7.11 | 12.03 | 4.00 | 83.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 3.95 | 12.65 | 19.90 | 1.00 | 89.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.41 | 11.36 | 19.66 | 2.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 1.70 | 5.34 | 8.40 | 1.00 | 37.9 | 28.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.47 | 13.87 | 23.96 | 3.00 | 89.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.97 | 13.87 | 23.23 | 2.00 | 87.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 3.78 | 11.92 | 22.36 | 4.00 | 79.8 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 3.12 | 9.31 | 15.57 | 1.00 | 55.8 | 45.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.36 | 9.20 | 14.93 | 2.00 | 82.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 44.47
- Actual score: 51.00
- Transfer: Senesi -> Guéhi (projected gain 2.60, hit 0)
- Autosub outfielders: Ballard, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.76 | 13.47 | 3.00 | 91.0 | 90.0 |
| XI | XI | Raya | GK | 1 | 5.9 | 3.00 | 8.33 | 13.53 | 2.00 | 87.7 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 4.07 | 11.11 | 17.82 | 0.00 | 92.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.74 | 10.42 | 16.73 | 8.00 | 94.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.97 | 8.99 | 14.89 | 3.00 | 76.8 | 90.0 |
| Bench 2 | Autosub In | Ballard | DEF | 17 | 4.6 | 2.42 | 7.83 | 12.91 | 1.00 | 84.7 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 2.12 | 6.72 | 11.17 | 6.00 | 64.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.62 | 11.09 | 18.48 | 1.00 | 81.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 3.40 | 10.67 | 18.79 | 2.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 1.43 | 5.15 | 8.93 | 1.00 | 31.1 | 55.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.94 | 13.72 | 22.44 | 8.00 | 85.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.12 | 12.51 | 20.22 | 3.00 | 85.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 3.33 | 11.13 | 19.17 | 6.00 | 62.4 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.21 | 10.33 | 17.06 | 3.00 | 81.7 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 3.13 | 10.16 | 17.93 | 0.00 | 61.5 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 0.10 -> 5.20
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 47.44
- Actual score: 56.00
- Transfer: M.Salah -> B.Fernandes (projected gain 8.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.84 | 10.31 | 15.91 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.20 | 8.45 | 12.84 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.86 | 11.71 | 18.25 | 1.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 3.75 | 10.75 | 16.41 | 2.00 | 87.0 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 3.02 | 9.07 | 13.75 | 8.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Muñoz | DEF | 8 | 6.1 | 2.56 | 8.03 | 13.41 | 0.00 | 32.6 | 0.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.7 | 2.86 | 7.90 | 13.37 | 1.00 | 81.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 3.65 | 11.08 | 17.91 | 2.00 | 73.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.26 | 10.86 | 18.31 | 2.00 | 71.1 | 80.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.6 | 2.31 | 5.92 | 9.44 | 0.00 | 64.9 | 20.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 5.15 | 15.72 | 24.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 4.80 | 13.92 | 23.34 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 3.82 | 12.19 | 22.40 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 11.86 | 21.30 | 2.00 | 84.7 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 3.20 | 9.88 | 15.89 | 3.00 | 81.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.20 -> 5.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Semenyo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 44.30
- Actual score: 56.00
- Transfer: Muñoz -> Cucurella (projected gain 1.87, hit 0)
- Autosub outfielders: Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 9.80 | 15.13 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.84 | 8.18 | 13.06 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.80 | 11.98 | 20.47 | 1.00 | 89.1 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 3.11 | 9.62 | 15.37 | 1.00 | 88.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 2.95 | 8.89 | 14.86 | 6.00 | 79.8 | 90.0 |
| Bench 2 | Autosub In | Ballard | DEF | 17 | 4.6 | 2.71 | 7.85 | 12.64 | 9.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.7 | 2.41 | 7.18 | 12.34 | 0.00 | 79.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.30 | 11.57 | 18.21 | 2.00 | 46.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.12 | 10.08 | 17.61 | 6.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.5 | 1.69 | 4.99 | 8.69 | 1.00 | 27.9 | 18.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.2 | 5.09 | 16.69 | 28.43 | 1.00 | 93.2 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 4.11 | 12.23 | 19.64 | 10.00 | 86.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 11.87 | 21.76 | 11.00 | 82.5 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 3.42 | 11.69 | 21.97 | 0.00 | 78.8 | 0.0 |
| XI | XI | Enzo | MID | 7 | 6.6 | 3.20 | 10.96 | 18.35 | 1.00 | 83.3 | 36.0 |

## GW18

- Train rows: 173897
- Bank: 5.00 -> 4.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.68
- Actual score: 59.00
- Transfer: Mbeumo -> Foden (projected gain 7.51, hit 0)
- Autosub outfielders: Enzo, Van de Ven, Isidor.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.28 | 12.49 | 11.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 2.97 | 8.13 | 12.87 | 2.00 | 90.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 10.66 | 16.69 | 2.00 | 90.5 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 3.36 | 9.37 | 15.20 | 0.00 | 87.5 | 0.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 3.05 | 8.61 | 14.14 | 2.00 | 86.5 | 68.0 |
| XI | Bench | Ballard | DEF | 17 | 4.6 | 2.99 | 7.67 | 12.32 | 0.00 | 86.3 | 0.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.6 | 2.46 | 7.27 | 11.42 | 11.00 | 83.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.59 | 11.92 | 19.76 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.40 | 10.68 | 18.41 | 8.00 | 76.0 | 68.0 |
| Bench 4 | Autosub In | Isidor | FWD | 17 | 5.5 | 1.71 | 4.75 | 7.73 | 1.00 | 25.9 | 22.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.00 | 15.93 | 24.66 | 2.00 | 87.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.97 | 23.21 | 0.00 | 79.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 12.81 | 20.76 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 11.59 | 18.58 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Enzo | MID | 7 | 6.5 | 2.97 | 9.13 | 14.75 | 1.00 | 71.9 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 4.30 -> 2.50
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 42.97
- Actual score: 34.00
- Transfer: João Pedro -> Ekitiké (projected gain 1.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.12 | 9.15 | 14.97 | 2.00 | 92.9 | 90.0 |
| XI | XI | Raya | GK | 1 | 6.0 | 3.21 | 9.13 | 14.64 | 2.00 | 87.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.43 | 9.91 | 15.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 2.91 | 8.83 | 13.80 | 6.00 | 87.0 | 90.0 |
| XI | Bench | Cucurella | DEF | 7 | 6.2 | 2.71 | 8.09 | 13.39 | 0.00 | 73.2 | 0.0 |
| Bench 2 | Bench | J.Timber | DEF | 1 | 6.5 | 2.34 | 7.55 | 12.97 | 9.00 | 32.3 | 82.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.7 | 1.83 | 5.86 | 11.05 | 0.00 | 60.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.42 | 11.22 | 19.61 | 2.00 | 80.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 3.37 | 10.40 | 16.66 | 2.00 | 48.6 | 90.0 |
| Bench 4 | Bench | Isidor | FWD | 17 | 5.4 | 1.46 | 4.90 | 8.56 | 1.00 | 30.4 | 32.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 15.79 | 27.34 | 3.00 | 89.4 | 90.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.66 | 21.91 | 0.00 | 84.9 | 0.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.05 | 19.54 | 5.00 | 94.2 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.5 | 3.26 | 10.17 | 16.66 | 9.00 | 81.5 | 90.0 |
| XI | Bench | B.Fernandes | MID | 14 | 9.2 | 2.51 | 9.15 | 18.46 | 0.00 | 24.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 2.50 -> 5.80
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 43.58
- Actual score: 70.00
- Transfer: B.Fernandes -> Wilson (projected gain 5.31, hit 0)
- Autosub outfielders: Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.10 | 9.01 | 14.46 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.86 | 13.86 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.33 | 10.34 | 16.81 | 2.00 | 94.3 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.42 | 9.46 | 14.55 | 7.00 | 86.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.73 | 7.47 | 13.48 | 3.00 | 72.9 | 90.0 |
| Bench 3 | Bench | Cucurella | DEF | 7 | 6.2 | 1.12 | 4.56 | 8.38 | 0.00 | 27.2 | 0.0 |
| Bench 4 | Autosub In | Ballard | DEF | 17 | 4.7 | 1.02 | 3.06 | 5.85 | 1.00 | 20.0 | 24.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 3.79 | 11.13 | 17.47 | 0.00 | 80.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.35 | 10.33 | 16.97 | 17.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Isidor | FWD | 17 | 5.4 | 1.14 | 3.65 | 6.16 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 14.78 | 23.30 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 13.92 | 21.73 | 1.00 | 92.4 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.03 | 12.14 | 19.79 | 6.00 | 83.9 | 84.0 |
| XI | XI | Enzo | MID | 7 | 6.4 | 3.07 | 9.92 | 16.85 | 11.00 | 83.7 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 2.64 | 8.88 | 15.46 | 17.00 | 61.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 5.80 -> 2.50
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 44.93
- Actual score: 55.00
- Transfer: Isidor -> Watkins (projected gain 2.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.05 | 9.23 | 15.09 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 13.08 | 3.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 9.70 | 15.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 2.98 | 8.36 | 13.21 | 0.00 | 90.5 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 2.97 | 8.28 | 13.78 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 1.27 | 4.74 | 9.41 | 1.00 | 28.7 | 78.0 |
| Bench 4 | Bench | Cucurella | DEF | 7 | 6.1 | 1.00 | 3.70 | 7.14 | -3.00 | 17.4 | 21.0 |
| XI | XI | Watkins | FWD | 2 | 8.6 | 3.96 | 11.14 | 17.59 | 2.00 | 79.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 10.47 | 17.15 | 12.00 | 91.8 | 81.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 9.1 | 2.40 | 8.64 | 14.30 | 0.00 | 27.6 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.54 | 16.36 | 25.01 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.09 | 19.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.56 | 11.95 | 20.67 | 3.00 | 79.6 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.91 | 11.10 | 18.00 | 9.00 | 86.3 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.4 | 3.62 | 10.45 | 16.49 | 1.00 | 89.8 | 64.0 |

## GW22

- Train rows: 177037
- Bank: 2.50 -> 2.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Watkins
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 43.60
- Actual score: 39.00
- Transfer: Cucurella -> Tarkowski (projected gain 4.03, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.23 | 9.59 | 14.80 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.86 | 7.97 | 12.70 | 5.00 | 92.3 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.18 | 11.69 | 19.43 | 8.00 | 90.2 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.36 | 9.86 | 15.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.24 | 9.42 | 15.25 | 5.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.5 | 2.92 | 7.78 | 12.22 | 0.00 | 85.5 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 2.17 | 6.29 | 10.11 | 4.00 | 66.9 | 90.0 |
| Vice Captain | XI | Watkins | FWD | 2 | 8.7 | 4.04 | 12.08 | 18.45 | 2.00 | 80.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.96 | 11.95 | 20.28 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Ekitiké | FWD | 12 | 9.0 | 2.62 | 7.70 | 12.85 | 2.00 | 17.8 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.12 | 12.63 | 20.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 3.44 | 11.40 | 19.52 | 3.00 | 68.7 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 11.32 | 19.34 | 1.00 | 80.5 | 45.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.77 | 10.83 | 17.71 | 2.00 | 88.2 | 87.0 |
| XI | XI | Enzo | MID | 7 | 6.4 | 3.23 | 9.27 | 14.95 | 6.00 | 79.5 | 84.0 |

## GW23

- Train rows: 177836
- Bank: 2.90 -> 3.30
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Thiago
- Effective captain: Rice
- Chip used: none
- Predicted score: 44.75
- Actual score: 53.00
- Transfer: Ballard -> Dorgu (projected gain 2.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.40 | 9.98 | 15.26 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.91 | 14.30 | 5.00 | 94.6 | 90.0 |
| XI | XI | Dorgu | DEF | 14 | 4.2 | 3.15 | 9.96 | 15.86 | 8.00 | 84.0 | 80.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.40 | 9.94 | 16.44 | 4.00 | 87.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.31 | 9.32 | 14.59 | 1.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.73 | 7.51 | 12.32 | 7.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Guéhi | DEF | 8 | 5.3 | 2.49 | 7.25 | 11.93 | 6.00 | 34.8 | 90.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 4.36 | 11.78 | 18.34 | 2.00 | 91.7 | 90.0 |
| XI | XI | Watkins | FWD | 2 | 8.8 | 3.19 | 10.33 | 16.08 | 8.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 8.9 | 2.98 | 9.13 | 15.89 | 1.00 | 33.9 | 31.0 |
| Captain | Captain | Rice | MID | 1 | 7.3 | 4.87 | 13.97 | 22.94 | 1.00 | 89.9 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.26 | 12.60 | 20.18 | 8.00 | 87.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 3.38 | 10.61 | 16.80 | 10.00 | 59.6 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.22 | 10.07 | 17.15 | 1.00 | 54.6 | 29.0 |
| XI | XI | Enzo | MID | 7 | 6.5 | 3.34 | 9.96 | 16.03 | 8.00 | 81.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 3.30 -> 4.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 45.58
- Actual score: 60.00
- Transfer: Foden -> Rogers (projected gain 3.13, hit 0)
- Autosub outfielders: Ekitiké, Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.24 | 9.34 | 14.11 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.72 | 13.98 | 1.00 | 96.6 | 90.0 |
| XI | Bench | Dorgu | DEF | 14 | 4.3 | 3.29 | 8.85 | 13.83 | 0.00 | 59.9 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.10 | 8.72 | 15.30 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.2 | 2.96 | 8.55 | 14.10 | 3.00 | 56.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 3.03 | 8.44 | 13.88 | 5.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.88 | 7.68 | 12.60 | 0.00 | 90.5 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.43 | 11.73 | 18.28 | 2.00 | 89.0 | 90.0 |
| XI | Bench | Watkins | FWD | 2 | 8.8 | 3.80 | 11.15 | 18.90 | 0.00 | 78.7 | 0.0 |
| Bench 2 | Autosub In | Ekitiké | FWD | 12 | 8.9 | 3.24 | 9.41 | 15.23 | 13.00 | 61.1 | 83.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 4.86 | 14.32 | 22.55 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 4.40 | 12.48 | 19.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 3.70 | 11.81 | 19.46 | 2.00 | 88.7 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.02 | 11.48 | 18.65 | 3.00 | 88.7 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.6 | 3.83 | 10.47 | 17.46 | 8.00 | 80.2 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 4.20 -> 3.50
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Rice
- Effective captain: Rogers
- Chip used: none
- Predicted score: 47.22
- Actual score: 56.00
- Transfer: J.Timber -> Gabriel (projected gain 3.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.60 | 10.56 | 16.26 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.29 | 13.14 | 1.00 | 93.9 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.0 | 4.30 | 11.63 | 18.80 | 6.00 | 86.3 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.01 | 8.89 | 14.79 | 2.00 | 86.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 2.97 | 8.69 | 14.05 | 3.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Dorgu | DEF | 14 | 4.4 | 2.34 | 7.01 | 12.10 | 0.00 | 58.2 | 0.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 1.83 | 6.16 | 11.13 | 1.00 | 66.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.28 | 11.87 | 20.77 | 5.00 | 85.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 3.51 | 11.33 | 18.01 | 2.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Watkins | FWD | 2 | 8.8 | 1.87 | 6.41 | 11.88 | 2.00 | 30.6 | 85.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.39 | 14.89 | 23.95 | 2.00 | 92.2 | 90.0 |
| Captain | Captain | Rogers | MID | 2 | 7.7 | 4.92 | 14.31 | 23.02 | 10.00 | 87.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.4 | 4.89 | 14.16 | 22.98 | 5.00 | 87.1 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.7 | 4.03 | 11.94 | 19.83 | 2.00 | 82.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.42 | 10.69 | 16.73 | 2.00 | 85.4 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 3.50 -> 2.00
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: bench_boost
- Predicted score: 61.75
- Actual score: 86.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.34) beats the best remaining Bench Boost opportunity (11.98).
- Transfer: Dorgu -> Virgil (projected gain 1.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.34) beats the best remaining Bench Boost opportunity (11.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.08 | 15.16 | 3.00 | 104.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.57 | 7.72 | 11.73 | 1.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 5.20 | 12.85 | 19.50 | 7.00 | 108.7 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.00 | 10.42 | 16.51 | 7.00 | 92.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.09 | 9.64 | 14.53 | 17.00 | 90.5 | 90.0 |
| Bench 2 | Bench Boost | Van de Ven | DEF | 18 | 4.5 | 3.00 | 8.51 | 13.86 | 3.00 | 81.7 | 90.0 |
| Bench 3 | Bench Boost | Tarkowski | DEF | 9 | 5.8 | 2.87 | 7.90 | 13.39 | 1.00 | 83.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 12.47 | 21.59 | 2.00 | 86.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.74 | 10.49 | 17.15 | 2.00 | 77.0 | 87.0 |
| Bench 4 | Bench Boost | Watkins | FWD | 2 | 8.7 | 2.80 | 8.42 | 13.72 | 2.00 | 68.6 | 73.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.88 | 13.73 | 21.03 | 14.00 | 90.7 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 5.16 | 13.70 | 21.59 | 14.00 | 113.2 | 180.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.15 | 12.05 | 19.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.8 | 3.94 | 11.08 | 18.42 | 2.00 | 85.1 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.19 | 10.96 | 17.87 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 2.00 -> 3.10
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Gabriel
- Effective captain: Rice
- Chip used: none
- Predicted score: 56.04
- Actual score: 45.00
- Transfer: Watkins -> João Pedro (projected gain 4.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 11.05 | 16.00 | 3.00 | 107.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.93 | 12.69 | 2.00 | 89.7 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.29 | 16.72 | 26.03 | 2.00 | 118.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.06 | 11.30 | 18.49 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.93 | 11.05 | 16.37 | 2.00 | 95.2 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 2.45 | 7.78 | 13.61 | 0.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.8 | 2.68 | 7.63 | 12.46 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.74 | 13.19 | 22.93 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 11.85 | 21.49 | 2.00 | 85.8 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.93 | 11.12 | 17.67 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 6.15 | 16.88 | 26.72 | 4.00 | 119.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.97 | 13.44 | 20.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 4.84 | 13.33 | 21.40 | 2.00 | 87.4 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.70 | 18.80 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 6.0 | 2.88 | 9.20 | 14.79 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 3.10 -> 4.30
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 49.96
- Actual score: 69.00
- Transfer: Tarkowski -> Truffert (projected gain 0.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.07 | 14.63 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 13.06 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 4.48 | 12.70 | 20.68 | 9.00 | 97.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.82 | 10.69 | 17.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.32 | 10.04 | 16.16 | 6.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Truffert | DEF | 4 | 4.5 | 3.14 | 9.08 | 13.96 | 4.00 | 85.6 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 2.73 | 7.84 | 12.37 | 0.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.20 | 14.69 | 23.42 | 2.00 | 85.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.17 | 11.62 | 18.40 | 6.00 | 84.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.95 | 10.80 | 17.95 | 15.00 | 76.5 | 75.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 5.12 | 15.42 | 24.37 | 5.00 | 107.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 4.59 | 13.41 | 21.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | Enzo | MID | 7 | 6.9 | 3.74 | 11.98 | 19.67 | 1.00 | 83.7 | 85.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 5.9 | 3.62 | 10.92 | 18.54 | 12.00 | 87.6 | 71.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 3.97 | 10.81 | 17.28 | 2.00 | 85.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 4.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 52.26
- Actual score: 69.00
- Transfer: Enzo -> B.Fernandes (projected gain 3.30, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.42 | 9.46 | 14.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.14 | 12.96 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.51 | 13.27 | 20.97 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 12.66 | 19.61 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.48 | 9.80 | 15.15 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Truffert | DEF | 4 | 4.5 | 3.05 | 8.94 | 13.79 | 8.00 | 88.2 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 2.85 | 8.40 | 12.97 | -3.00 | 87.1 | 37.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.27 | 13.00 | 20.73 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.80 | 18.23 | 2.00 | 86.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 3.78 | 11.67 | 17.96 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.93 | 15.11 | 23.54 | 7.00 | 97.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 4.45 | 14.04 | 22.58 | 8.00 | 90.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 4.35 | 12.78 | 20.40 | 3.00 | 96.1 | 90.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 3.66 | 10.82 | 19.00 | 1.00 | 84.6 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 3.87 | 10.80 | 16.51 | 0.00 | 84.0 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 1.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: João Pedro
- Vice captain: Semenyo
- Effective captain: João Pedro
- Chip used: triple_captain
- Predicted score: 56.92
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.48) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Wilson -> Szoboszlai (projected gain 0.79, hit 0)
- Chip used: Triple Captain on João Pedro. Optimizer chose Triple Captain here because the current estimated captain upside (5.48) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.44 | 8.92 | 13.22 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 8.15 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 11.63 | 17.77 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 3.76 | 11.52 | 18.66 | 9.00 | 96.3 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.26 | 8.69 | 13.87 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Truffert | DEF | 4 | 4.6 | 2.82 | 7.41 | 11.49 | 11.00 | 85.9 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 1.38 | 4.66 | 7.88 | 0.00 | 36.8 | 0.0 |
| Captain | Captain | João Pedro | FWD | 7 | 7.6 | 5.48 | 14.86 | 23.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 4.02 | 11.67 | 18.07 | 1.00 | 74.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.00 | 11.09 | 17.03 | 6.00 | 87.3 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 5.13 | 15.84 | 24.87 | 10.00 | 94.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.2 | 5.25 | 15.55 | 23.96 | 2.00 | 83.0 | 74.0 |
| XI | XI | Szoboszlai | MID | 12 | 6.9 | 3.98 | 11.32 | 18.14 | 11.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 2 | 7.6 | 3.21 | 10.58 | 16.81 | 2.00 | 83.9 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 3.64 | 10.23 | 17.43 | 3.00 | 83.0 | 90.0 |