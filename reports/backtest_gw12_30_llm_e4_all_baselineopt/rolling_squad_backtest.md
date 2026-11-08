# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 901.37
- Total actual points: 1020.00
- Average predicted points: 47.44
- Average actual points: 53.68
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
- Predicted score: 50.10
- Actual score: 33.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Woltemade, Ballard, Keane.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.51 | 9.52 | 15.16 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.97 | 14.16 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 4.25 | 12.16 | 20.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.18 | 10.31 | 16.71 | 0.00 | 75.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 10.28 | 16.87 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Autosub In | Keane | DEF | 9 | 4.5 | 3.00 | 9.78 | 16.00 | 9.00 | 87.0 | 90.0 |
| Bench 3 | Autosub In | Ballard | DEF | 17 | 4.6 | 3.06 | 9.07 | 15.26 | 1.00 | 80.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.30 | 12.64 | 19.01 | 1.00 | 88.7 | 75.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 3.85 | 11.33 | 18.51 | 4.00 | 86.2 | 90.0 |
| Bench 2 | Autosub In | Woltemade | FWD | 15 | 7.5 | 3.17 | 10.91 | 18.76 | 2.00 | 67.2 | 84.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 5.33 | 15.44 | 24.67 | 0.00 | 94.6 | 0.0 |
| Vice Captain | Captain | M.Salah | MID | 12 | 14.2 | 4.58 | 13.45 | 21.62 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 4.45 | 13.25 | 20.64 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.97 | 12.24 | 19.25 | 6.00 | 87.1 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 3.58 | 12.08 | 19.18 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 44.64
- Actual score: 36.00
- Transfer: Gabriel -> Muñoz (projected gain 3.25, hit 0)
- Autosub outfielders: Keane.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.15 | 9.28 | 15.29 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.81 | 8.43 | 12.38 | 1.00 | 93.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 3.97 | 11.11 | 17.60 | 1.00 | 88.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.23 | 10.50 | 17.10 | 2.00 | 92.2 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.17 | 9.10 | 14.24 | 0.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 2.92 | 8.80 | 14.91 | 3.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Keane | DEF | 9 | 4.5 | 2.95 | 7.92 | 12.60 | 2.00 | 65.5 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.12 | 12.29 | 18.97 | 1.00 | 86.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 3.94 | 11.56 | 20.16 | 13.00 | 83.2 | 90.0 |
| XI | XI | Woltemade | FWD | 15 | 7.4 | 3.03 | 8.99 | 14.93 | 7.00 | 74.1 | 89.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.16 | 13.50 | 23.30 | 1.00 | 81.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.15 | 13.50 | 24.47 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.13 | 12.86 | 22.51 | 0.00 | 80.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 3.42 | 11.76 | 20.61 | 1.00 | 52.8 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 6.1 | 2.50 | 7.93 | 14.30 | -2.00 | 62.2 | 37.0 |

## GW14

- Train rows: 170850
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 44.19
- Actual score: 41.00
- Transfer: Caicedo -> Anderson (projected gain 1.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.21 | 9.23 | 14.46 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 12.64 | 2.00 | 91.3 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 3.35 | 10.96 | 17.52 | 0.00 | 92.4 | 0.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 3.27 | 9.82 | 15.21 | 14.00 | 62.2 | 90.0 |
| XI | Bench | Keane | DEF | 9 | 4.5 | 3.05 | 9.29 | 16.06 | 0.00 | 83.0 | 0.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.8 | 2.91 | 9.03 | 14.13 | 0.00 | 85.8 | 0.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 2.49 | 7.51 | 12.03 | 4.00 | 83.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 3.95 | 12.65 | 19.90 | 1.00 | 89.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.41 | 11.36 | 20.06 | 2.00 | 66.0 | 90.0 |
| XI | XI | Woltemade | FWD | 15 | 7.4 | 3.85 | 11.08 | 17.89 | 5.00 | 83.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.17 | 12.87 | 21.16 | 3.00 | 89.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.27 | 12.87 | 20.43 | 2.00 | 87.1 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.60 | 11.34 | 19.09 | 2.00 | 89.0 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 3.78 | 11.22 | 19.26 | 4.00 | 72.8 | 90.0 |
| Bench 2 | Bench | M.Salah | MID | 12 | 14.2 | 3.12 | 9.71 | 16.97 | 1.00 | 26.8 | 45.0 |

## GW15

- Train rows: 171608
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 44.46
- Actual score: 53.00
- Transfer: Keane -> Guéhi (projected gain 3.97, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.30 | 10.43 | 16.33 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.06 | 12.37 | 3.00 | 91.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.44 | 11.12 | 17.13 | 8.00 | 94.1 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 4.07 | 11.11 | 18.22 | 0.00 | 92.5 | 0.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 2.82 | 9.23 | 16.11 | 1.00 | 84.7 | 90.0 |
| Bench 3 | Autosub In | Senesi | DEF | 4 | 5.0 | 2.35 | 7.16 | 13.31 | 8.00 | 61.5 | 61.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.8 | 2.12 | 6.72 | 11.57 | 6.00 | 39.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.62 | 12.49 | 21.28 | 1.00 | 81.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 3.40 | 11.07 | 18.09 | 2.00 | 75.1 | 90.0 |
| XI | XI | Woltemade | FWD | 15 | 7.4 | 3.96 | 10.20 | 16.74 | 2.00 | 85.2 | 73.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.03 | 13.23 | 23.07 | 6.00 | 85.4 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.24 | 12.32 | 20.04 | 8.00 | 85.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.12 | 12.21 | 19.52 | 3.00 | 85.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.22 | 10.92 | 18.61 | 4.00 | 83.6 | 90.0 |
| Bench 2 | Bench | M.Salah | MID | 12 | 14.1 | 3.13 | 9.46 | 15.83 | 0.00 | 61.5 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 0.90 -> 6.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 45.66
- Actual score: 53.00
- Transfer: M.Salah -> B.Fernandes (projected gain 3.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.84 | 10.31 | 15.91 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.20 | 8.45 | 13.24 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.86 | 11.71 | 18.25 | 1.00 | 92.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.16 | 9.70 | 16.17 | 1.00 | 81.3 | 90.0 |
| Bench 3 | Bench | Muñoz | DEF | 8 | 6.1 | 2.86 | 9.43 | 15.51 | 0.00 | 63.6 | 0.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 5.0 | 2.60 | 9.24 | 15.68 | 1.00 | 76.3 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 3.02 | 9.07 | 14.45 | 8.00 | 85.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 3.65 | 11.78 | 20.71 | 2.00 | 79.8 | 90.0 |
| XI | XI | Woltemade | FWD | 15 | 7.5 | 3.34 | 10.92 | 17.71 | 0.00 | 77.8 | 74.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.4 | 3.26 | 10.86 | 18.71 | 2.00 | 71.1 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 4.75 | 13.72 | 22.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 4.10 | 12.22 | 20.24 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 3.82 | 12.19 | 22.10 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 11.56 | 21.70 | 2.00 | 87.7 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.43 | 10.71 | 17.48 | 3.00 | 85.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 6.00 -> 4.80
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Semenyo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 43.77
- Actual score: 53.00
- Transfer: Senesi -> Cucurella (projected gain 0.68, hit 0)
- Autosub outfielders: Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 9.40 | 14.73 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.84 | 7.88 | 12.76 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.80 | 11.28 | 17.67 | 1.00 | 89.1 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 3.11 | 9.62 | 14.67 | 1.00 | 88.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.11 | 9.28 | 15.44 | 0.00 | 79.6 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 3.01 | 9.25 | 15.04 | 9.00 | 87.0 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.0 | 1.45 | 5.38 | 11.55 | 0.00 | 19.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.30 | 11.57 | 17.51 | 2.00 | 46.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.12 | 10.78 | 18.71 | 6.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Woltemade | FWD | 15 | 7.5 | 2.87 | 8.41 | 14.19 | 13.00 | 69.3 | 72.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.2 | 4.69 | 14.69 | 24.33 | 1.00 | 92.2 | 45.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.27 | 21.76 | 11.00 | 82.5 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 4.11 | 12.23 | 19.64 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 3.72 | 11.99 | 21.97 | 0.00 | 78.8 | 0.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.4 | 3.00 | 10.08 | 17.34 | 4.00 | 84.0 | 90.0 |

## GW18

- Train rows: 173897
- Bank: 4.80 -> 4.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.01
- Actual score: 53.00
- Transfer: Mbeumo -> Foden (projected gain 4.98, hit 0)
- Autosub outfielders: Woltemade, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.37 | 10.23 | 16.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 7.98 | 12.49 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 11.36 | 17.29 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cucurella | DEF | 7 | 6.2 | 3.05 | 8.61 | 13.84 | 2.00 | 86.5 | 68.0 |
| XI | Bench | Ballard | DEF | 17 | 4.6 | 2.99 | 7.67 | 12.82 | 0.00 | 86.3 | 0.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.6 | 2.46 | 7.27 | 12.12 | 11.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.31 | 4.18 | 8.50 | 0.00 | 10.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.59 | 11.92 | 19.06 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.40 | 10.98 | 18.41 | 8.00 | 82.0 | 68.0 |
| Bench 2 | Autosub In | Woltemade | FWD | 15 | 7.3 | 2.76 | 9.35 | 17.29 | 2.00 | 70.4 | 67.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.97 | 26.71 | 0.00 | 84.0 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.60 | 14.03 | 22.76 | 2.00 | 87.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 12.81 | 20.76 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.29 | 19.58 | 5.00 | 90.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.12 | 10.17 | 17.31 | 3.00 | 85.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 4.10 -> 3.00
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 44.55
- Actual score: 34.00
- Transfer: B.Fernandes -> Saka (projected gain 3.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.21 | 9.53 | 14.64 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.12 | 8.45 | 13.57 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.43 | 10.31 | 16.69 | 2.00 | 89.0 | 90.0 |
| XI | Bench | Cucurella | DEF | 7 | 6.2 | 3.01 | 8.79 | 14.09 | 0.00 | 80.2 | 0.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 2.61 | 8.13 | 13.10 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.7 | 2.13 | 5.86 | 9.65 | 0.00 | 60.1 | 0.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.06 | 3.65 | 6.78 | 0.00 | 10.5 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.42 | 11.22 | 19.61 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.39 | 10.27 | 17.23 | 1.00 | 80.1 | 27.0 |
| Bench 2 | Bench | Woltemade | FWD | 15 | 7.3 | 3.05 | 9.25 | 16.34 | 1.00 | 69.4 | 10.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 15.79 | 27.34 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 13.15 | 20.54 | 5.00 | 94.2 | 90.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.96 | 21.91 | 0.00 | 84.9 | 0.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 4.10 | 12.96 | 23.29 | 6.00 | 81.9 | 82.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.23 | 9.69 | 16.20 | 4.00 | 85.4 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 3.00 -> 3.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 42.95
- Actual score: 61.00
- Transfer: Muñoz -> Tarkowski (projected gain 6.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.10 | 9.31 | 14.46 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.86 | 14.26 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.33 | 11.04 | 17.01 | 2.00 | 94.3 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.5 | 3.33 | 9.82 | 15.15 | 2.00 | 90.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.42 | 9.46 | 14.55 | 7.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Cucurella | DEF | 7 | 6.2 | 1.12 | 4.56 | 8.38 | 0.00 | 27.2 | 0.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.7 | 1.32 | 3.76 | 7.95 | 1.00 | 20.0 | 24.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.35 | 10.33 | 18.07 | 17.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 2.73 | 8.36 | 13.96 | 2.00 | 70.3 | 61.0 |
| Bench 2 | Bench | Woltemade | FWD | 15 | 7.4 | 2.60 | 7.54 | 12.37 | 1.00 | 61.4 | 12.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 14.78 | 23.60 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 13.22 | 20.63 | 1.00 | 92.4 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.88 | 11.65 | 18.34 | 4.00 | 72.3 | 23.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.04 | 9.69 | 15.82 | 4.00 | 87.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 2.64 | 8.48 | 14.46 | 17.00 | 61.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 3.30 -> 3.00
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.73
- Actual score: 53.00
- Transfer: Woltemade -> Bowen (projected gain 2.31, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.05 | 8.53 | 14.09 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 12.38 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 3.79 | 10.50 | 16.32 | 4.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 10.40 | 17.12 | 6.00 | 92.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 2.98 | 8.36 | 13.21 | 0.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 1.27 | 4.74 | 9.41 | 1.00 | 28.7 | 78.0 |
| Bench 4 | Bench | Cucurella | DEF | 7 | 6.1 | 1.00 | 3.70 | 7.54 | -3.00 | 17.4 | 21.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 11.57 | 17.55 | 12.00 | 91.8 | 81.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.39 | 10.96 | 17.75 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 2.96 | 8.72 | 14.21 | 1.00 | 71.7 | 15.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.84 | 14.26 | 25.71 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.49 | 19.59 | 6.00 | 91.6 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.86 | 11.95 | 21.07 | 3.00 | 79.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.82 | 11.37 | 19.54 | 3.00 | 66.6 | 77.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.37 | 9.99 | 15.29 | 7.00 | 88.0 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 3.00 -> 3.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 42.72
- Actual score: 37.00
- Transfer: Cucurella -> Pedro Porro (projected gain 2.02, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.23 | 9.99 | 15.90 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.46 | 7.27 | 11.30 | 5.00 | 93.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.36 | 11.26 | 20.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.18 | 10.29 | 16.63 | 8.00 | 90.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.29 | 9.66 | 14.72 | 4.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.5 | 2.92 | 7.78 | 12.22 | 0.00 | 85.5 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 1.47 | 4.89 | 8.01 | 4.00 | 34.9 | 90.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.0 | 3.96 | 11.25 | 17.88 | 2.00 | 89.0 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.44 | 10.42 | 15.69 | 3.00 | 85.4 | 90.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 2.43 | 7.32 | 12.40 | 8.00 | 58.9 | 73.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.12 | 13.33 | 20.95 | 2.00 | 90.5 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 12.72 | 22.44 | 1.00 | 74.5 | 45.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.47 | 11.42 | 19.70 | 1.00 | 57.7 | 33.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 3.44 | 11.10 | 20.22 | 3.00 | 76.7 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.21 | 10.30 | 17.96 | 5.00 | 87.3 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 3.90 -> 4.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 43.56
- Actual score: 54.00
- Transfer: Guéhi -> Senesi (projected gain 2.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.40 | 9.98 | 15.66 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.91 | 14.00 | 5.00 | 94.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.40 | 10.34 | 17.44 | 4.00 | 87.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.51 | 10.33 | 15.96 | 3.00 | 88.6 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 3.13 | 9.31 | 15.42 | 7.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.2 | 3.02 | 7.73 | 12.41 | 1.00 | 65.7 | 45.0 |
| Bench 3 | Bench | Ballard | DEF | 17 | 4.6 | 2.58 | 7.18 | 11.05 | 2.00 | 78.7 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.7 | 3.84 | 11.14 | 17.81 | 12.00 | 84.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.96 | 10.88 | 17.34 | 2.00 | 91.7 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.1 | 2.48 | 8.69 | 14.35 | 12.00 | 50.9 | 84.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.26 | 13.30 | 23.38 | 8.00 | 87.3 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.3 | 4.17 | 13.27 | 20.14 | 1.00 | 89.9 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.26 | 10.91 | 18.60 | 2.00 | 47.9 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.22 | 10.77 | 19.25 | 1.00 | 54.6 | 29.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.14 | 9.95 | 16.32 | 5.00 | 87.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 4.40 -> 5.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 44.95
- Actual score: 71.00
- Transfer: Foden -> Rogers (projected gain 2.98, hit 0)
- Autosub outfielders: Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.24 | 9.34 | 14.81 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.72 | 13.68 | 1.00 | 96.6 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.30 | 9.64 | 14.65 | 8.00 | 91.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.10 | 8.72 | 14.60 | 2.00 | 86.4 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 3.18 | 8.45 | 12.28 | 9.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 2.63 | 7.94 | 14.06 | 0.00 | 74.3 | 0.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.88 | 7.68 | 13.40 | 0.00 | 90.5 | 0.0 |
| Bench 2 | Autosub In | Bowen | FWD | 19 | 7.6 | 3.27 | 10.96 | 18.26 | 8.00 | 84.8 | 80.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.43 | 10.73 | 16.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.1 | 3.46 | 9.99 | 16.23 | 10.00 | 78.5 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 4.86 | 13.92 | 21.85 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 4.40 | 13.88 | 23.44 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Saka | MID | 1 | 10.1 | 3.60 | 12.24 | 20.05 | 0.00 | 67.7 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.02 | 12.18 | 19.25 | 3.00 | 88.7 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.48 | 10.41 | 16.58 | 7.00 | 88.6 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 5.30 -> 5.80
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Semenyo
- Effective captain: Rogers
- Chip used: none
- Predicted score: 45.05
- Actual score: 64.00
- Transfer: Saka -> B.Fernandes (projected gain 2.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.60 | 10.96 | 16.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.59 | 13.44 | 1.00 | 93.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.58 | 10.46 | 16.52 | 2.00 | 88.6 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 2.87 | 8.97 | 14.11 | 1.00 | 82.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.01 | 8.59 | 13.99 | 2.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 1.83 | 6.16 | 10.73 | 1.00 | 42.5 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 1.60 | 5.34 | 9.55 | 0.00 | 30.3 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.28 | 12.27 | 20.47 | 5.00 | 85.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.53 | 10.99 | 18.17 | 8.00 | 62.8 | 74.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.37 | 10.26 | 17.49 | 2.00 | 81.7 | 90.0 |
| Captain | Captain | Rogers | MID | 2 | 7.7 | 4.62 | 14.31 | 23.42 | 10.00 | 87.2 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.39 | 14.19 | 24.95 | 2.00 | 92.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 4.19 | 12.76 | 20.18 | 5.00 | 87.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 3.99 | 12.56 | 21.75 | 10.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Anderson | MID | 16 | 5.3 | 3.24 | 10.21 | 17.91 | 4.00 | 85.4 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 5.80 -> 3.20
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: bench_boost
- Predicted score: 59.99
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (9.75).
- Transfer: Van de Ven -> Gabriel (projected gain 5.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.64) beats the best remaining Bench Boost opportunity (9.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.48 | 15.86 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.42 | 12.43 | 1.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 5.20 | 14.25 | 21.10 | 7.00 | 138.7 | 180.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.17 | 9.70 | 15.49 | 1.00 | 83.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 2.99 | 8.65 | 14.22 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench Boost | Ballard | DEF | 17 | 4.6 | 2.28 | 6.48 | 10.04 | 4.00 | 67.6 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.2 | 1.14 | 3.98 | 7.20 | 0.00 | 18.4 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 12.47 | 21.99 | 2.00 | 86.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.99 | 11.31 | 17.66 | 10.00 | 79.3 | 90.0 |
| Bench 2 | Bench Boost | Bowen | FWD | 19 | 7.7 | 3.23 | 9.53 | 16.37 | 5.00 | 80.0 | 89.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 4.33 | 13.99 | 22.14 | 2.00 | 76.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 5.16 | 13.40 | 21.19 | 14.00 | 103.2 | 180.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.88 | 13.33 | 21.33 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.15 | 12.45 | 19.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.41 | 10.40 | 17.43 | 5.00 | 84.7 | 90.0 |

## GW27

- Train rows: 181084
- Bank: 3.20 -> 2.50
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Gabriel
- Effective captain: Rice
- Chip used: none
- Predicted score: 53.29
- Actual score: 50.00
- Transfer: Pedro Porro -> Virgil (projected gain 4.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 11.75 | 17.10 | 3.00 | 105.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.93 | 12.69 | 2.00 | 89.7 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 5.29 | 16.72 | 26.03 | 2.00 | 118.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.06 | 11.70 | 18.09 | 11.00 | 94.6 | 90.0 |
| XI | XI | Ballard | DEF | 17 | 4.6 | 3.00 | 8.32 | 12.60 | 4.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.97 | 7.50 | 12.86 | 5.00 | 62.9 | 90.0 |
| Bench 4 | Bench | Tarkowski | DEF | 9 | 5.8 | 2.68 | 7.33 | 12.46 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.44 | 12.19 | 18.73 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 11.55 | 21.49 | 2.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Bowen | FWD | 19 | 7.7 | 3.26 | 10.48 | 17.90 | 4.00 | 82.7 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 5.75 | 16.88 | 26.72 | 4.00 | 120.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.97 | 14.14 | 21.58 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 4.10 | 11.58 | 19.07 | 2.00 | 75.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.30 | 18.40 | 2.00 | 83.2 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.94 | 11.28 | 19.10 | 5.00 | 88.6 | 76.0 |

## GW28

- Train rows: 181902
- Bank: 2.50 -> 3.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 49.78
- Actual score: 70.00
- Transfer: Tarkowski -> Guéhi (projected gain 2.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.47 | 14.63 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 13.36 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 4.48 | 12.70 | 20.68 | 9.00 | 101.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 3.82 | 10.69 | 17.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 13 | 5.2 | 3.32 | 9.74 | 15.86 | 6.00 | 90.7 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.96 | 7.52 | 11.92 | 4.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 2.44 | 7.02 | 11.15 | 4.00 | 83.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.20 | 13.29 | 20.62 | 2.00 | 81.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.17 | 12.32 | 19.40 | 6.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Bowen | FWD | 19 | 7.6 | 3.49 | 11.90 | 20.25 | 7.00 | 86.6 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.0 | 4.99 | 14.81 | 23.19 | 8.00 | 90.4 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.6 | 4.72 | 14.32 | 23.37 | 5.00 | 101.6 | 75.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 3.97 | 11.51 | 20.78 | 2.00 | 84.9 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.84 | 11.30 | 18.68 | 1.00 | 85.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 3.80 | 10.94 | 17.96 | 13.00 | 58.3 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 3.00 -> 2.20
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 52.29
- Actual score: 71.00
- Transfer: Senesi -> Tarkowski (projected gain 0.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.42 | 9.46 | 14.20 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.14 | 12.96 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.51 | 13.27 | 20.97 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 12.66 | 19.61 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 13 | 5.2 | 3.88 | 10.20 | 15.85 | 1.00 | 90.8 | 90.0 |
| Bench 2 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.26 | 9.08 | 14.31 | 15.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 3.01 | 8.73 | 13.55 | 9.00 | 87.1 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.27 | 13.00 | 20.73 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.80 | 18.23 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.6 | 3.62 | 10.68 | 16.59 | 4.00 | 90.1 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.93 | 15.11 | 23.54 | 7.00 | 97.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 4.45 | 14.04 | 22.18 | 8.00 | 90.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 4.35 | 12.78 | 20.40 | 3.00 | 96.1 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 3.66 | 11.92 | 19.30 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Anderson | MID | 16 | 5.4 | 3.24 | 10.50 | 17.97 | 12.00 | 85.4 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 2.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 58.67
- Actual score: 54.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Rice -> Mbeumo (projected gain 1.77, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.95) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.44 | 8.62 | 12.82 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 7.85 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 11.63 | 17.27 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 3.76 | 11.52 | 18.66 | 9.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.04 | 9.73 | 15.26 | 0.00 | 88.8 | 0.0 |
| XI | XI | Guéhi | DEF | 13 | 5.2 | 3.26 | 8.69 | 13.77 | 2.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Ballard | DEF | 17 | 4.6 | 2.90 | 7.66 | 12.33 | 4.00 | 89.9 | 63.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.88 | 17.86 | 27.92 | 2.00 | 94.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.00 | 11.79 | 19.43 | 6.00 | 87.3 | 90.0 |
| XI | XI | Bowen | FWD | 19 | 7.5 | 3.99 | 11.37 | 18.08 | 6.00 | 88.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 5.13 | 15.84 | 24.07 | 10.00 | 94.1 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 5.95 | 15.55 | 23.96 | 2.00 | 96.0 | 74.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 3.65 | 12.00 | 19.33 | 2.00 | 67.4 | 74.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.69 | 11.35 | 17.50 | 2.00 | 89.1 | 87.0 |
| Bench 2 | Bench | Rogers | MID | 2 | 7.6 | 3.21 | 10.98 | 18.21 | 2.00 | 83.9 | 90.0 |