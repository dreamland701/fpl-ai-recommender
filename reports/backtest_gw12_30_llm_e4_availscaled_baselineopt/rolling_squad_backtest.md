# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1176.85
- Total actual points: 992.00
- Average predicted points: 61.94
- Average actual points: 52.21
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Semenyo
- Vice captain: M.Salah
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 63.97
- Actual score: 48.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Richards, O'Reilly, Raúl.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.45 | 12.31 | 19.07 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.74 | 13.05 | 21.40 | 14.00 | 83.3 | 90.0 |
| Bench 3 | Autosub In | O'Reilly | DEF | 13 | 4.9 | 4.17 | 12.39 | 19.70 | 1.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Richards | DEF | 8 | 4.5 | 4.26 | 11.52 | 18.77 | 6.00 | 86.3 | 82.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.60 | 15.64 | 24.41 | 1.00 | 88.7 | 75.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 4.44 | 12.79 | 20.23 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Autosub In | Raúl | FWD | 10 | 6.2 | 3.98 | 9.91 | 15.27 | 6.00 | 66.8 | 90.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 94.6 | 0.0 |
| Vice Captain | Captain | M.Salah | MID | 12 | 14.2 | 5.80 | 16.25 | 26.06 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 5.08 | 15.35 | 24.15 | 6.00 | 87.1 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.63 | 13.61 | 21.57 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 60.19
- Actual score: 38.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Caicedo -> Anderson (projected gain 2.02, hit 0)
- Autosub outfielders: Raúl.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.92 | 11.57 | 18.38 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 93.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 5.02 | 13.96 | 22.43 | 1.00 | 88.4 | 90.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.5 | 3.28 | 13.42 | 26.60 | 0.00 | 24.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 92.2 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.0 | 4.50 | 12.34 | 19.39 | 4.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Richards | DEF | 8 | 4.5 | 3.94 | 11.25 | 18.52 | 1.00 | 84.5 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.33 | 14.90 | 23.76 | 1.00 | 86.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.27 | 14.59 | 22.84 | 13.00 | 83.2 | 90.0 |
| Bench 2 | Autosub In | Raúl | FWD | 10 | 6.2 | 4.01 | 10.57 | 16.29 | 1.00 | 72.3 | 90.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.54 | 16.42 | 25.91 | 1.00 | 81.9 | 90.0 |
| Captain | Bench | M.Salah | MID | 12 | 14.2 | 5.61 | 16.05 | 25.55 | 0.00 | 80.0 | 0.0 |
| XI | XI | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 92.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 5.08 | 15.75 | 27.16 | 1.00 | 52.8 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 4.52 | 12.57 | 20.64 | 6.00 | 90.5 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 0.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 58.99
- Actual score: 33.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gabriel -> J.Timber (projected gain 3.06, hit 0)
- Autosub outfielders: Richards.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.04 | 11.40 | 17.93 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 91.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.74 | 13.57 | 21.60 | 1.00 | 83.4 | 46.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.1 | 4.60 | 13.24 | 21.10 | 0.00 | 85.5 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 92.4 | 0.0 |
| Bench 2 | Autosub In | Richards | DEF | 8 | 4.6 | 3.76 | 10.56 | 16.98 | 9.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 3.25 | 9.38 | 15.04 | 14.00 | 62.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.10 | 15.81 | 25.46 | 1.00 | 89.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.61 | 14.19 | 23.72 | 2.00 | 66.0 | 90.0 |
| Bench 3 | Bench | Raúl | FWD | 10 | 6.2 | 3.54 | 10.10 | 15.92 | 2.00 | 74.1 | 73.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.59 | 15.79 | 25.46 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.32 | 15.63 | 25.82 | 3.00 | 89.0 | 82.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 5.21 | 15.56 | 26.00 | 1.00 | 26.8 | 45.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 5.13 | 15.05 | 25.39 | 4.00 | 72.8 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 4.50 | 12.64 | 20.79 | 2.00 | 89.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 1.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 58.67
- Actual score: 55.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Senesi -> Guéhi (projected gain 1.42, hit 0)
- Autosub outfielders: Anderson, Richards.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.08 | 11.98 | 19.02 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 92.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 94.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.38 | 13.45 | 22.05 | 3.00 | 68.8 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.56 | 12.58 | 20.12 | 6.00 | 81.7 | 90.0 |
| Bench 3 | Autosub In | Richards | DEF | 8 | 4.6 | 3.77 | 11.17 | 18.16 | 4.00 | 84.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.67 | 14.70 | 23.78 | 1.00 | 81.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.60 | 13.64 | 22.18 | 2.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Raúl | FWD | 10 | 6.2 | 3.27 | 9.20 | 14.77 | 5.00 | 74.2 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.50 | 16.02 | 26.05 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.61 | 15.61 | 25.13 | 8.00 | 85.1 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 4.96 | 15.09 | 25.15 | 0.00 | 61.5 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.78 | 14.91 | 24.96 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.4 | 4.09 | 12.56 | 20.90 | 4.00 | 83.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.90 -> 6.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 60.01
- Actual score: 54.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: M.Salah -> B.Fernandes (projected gain 6.01, hit 0)
- Autosub outfielders: Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.38 | 11.73 | 18.19 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 92.8 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.1 | 4.33 | 13.85 | 23.11 | 0.00 | 63.6 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.85 | 13.63 | 21.35 | 2.00 | 87.0 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.29 | 12.20 | 19.58 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Richards | DEF | 8 | 4.6 | 3.69 | 11.08 | 18.09 | 1.00 | 83.9 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.88 | 14.77 | 23.81 | 2.00 | 79.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.48 | 13.78 | 23.37 | 2.00 | 71.1 | 80.0 |
| Bench 4 | Bench | Raúl | FWD | 10 | 6.2 | 3.45 | 9.95 | 15.62 | 2.00 | 79.0 | 78.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.41 | 15.34 | 25.16 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.98 | 14.96 | 24.47 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 5.04 | 14.26 | 23.59 | 2.00 | 87.7 | 90.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.4 | 4.27 | 12.60 | 20.52 | 3.00 | 85.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 6.00 -> 6.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Semenyo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 56.26
- Actual score: 57.00
- Transfer: Muñoz -> Virgil (projected gain 2.55, hit 0)
- Autosub outfielders: Richards.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.54 | 18.21 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.48 | 14.91 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.23 | 12.96 | 21.41 | 6.00 | 79.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.28 | 12.95 | 21.22 | 2.00 | 89.2 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.25 | 12.02 | 19.01 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | Richards | DEF | 8 | 4.6 | 3.56 | 10.46 | 16.91 | 2.00 | 83.9 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 4.17 | 13.18 | 22.51 | 6.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Raúl | FWD | 10 | 6.3 | 3.48 | 9.87 | 15.89 | 5.00 | 73.4 | 84.0 |
| Bench 4 | Bench | Thiago | FWD | 5 | 7.1 | 3.05 | 9.66 | 15.40 | 2.00 | 46.8 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 92.2 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.32 | 14.84 | 24.25 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.48 | 14.23 | 24.95 | 0.00 | 78.8 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.62 | 14.09 | 23.80 | 11.00 | 82.5 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.76 | 11.68 | 19.48 | 4.00 | 84.0 | 90.0 |

## GW18

- Train rows: 173897
- Bank: 6.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 59.77
- Actual score: 50.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mbeumo -> Foden (projected gain 6.99, hit 0)
- Autosub outfielders: Anderson, Raúl.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.58 | 14.89 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 4.66 | 13.04 | 20.63 | 0.00 | 87.5 | 0.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 4.39 | 12.77 | 20.36 | 1.00 | 85.6 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.38 | 12.41 | 19.86 | 2.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Richards | DEF | 8 | 4.6 | 3.69 | 10.64 | 17.19 | 0.00 | 85.6 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.59 | 13.50 | 21.70 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.44 | 12.79 | 20.87 | 8.00 | 82.0 | 68.0 |
| Bench 3 | Autosub In | Raúl | FWD | 10 | 6.3 | 3.83 | 10.18 | 16.27 | 9.00 | 77.7 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.12 | 18.40 | 29.36 | 2.00 | 87.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.94 | 17.83 | 29.38 | 0.00 | 84.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.28 | 15.57 | 25.11 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.92 | 14.59 | 23.58 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Anderson | MID | 16 | 5.4 | 3.84 | 11.63 | 19.21 | 3.00 | 85.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 5.40 -> 3.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.67
- Actual score: 37.00
- Transfer: Anderson -> Rogers (projected gain 3.07, hit 0)
- Autosub outfielders: Raúl, O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.05 | 17.50 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 89.0 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.28 | 12.13 | 20.09 | 6.00 | 84.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.07 | 11.98 | 20.16 | 9.00 | 61.3 | 82.0 |
| Bench 3 | Autosub In | O'Reilly | DEF | 13 | 5.3 | 3.71 | 10.96 | 17.82 | 1.00 | 83.2 | 56.0 |
| Bench 4 | Bench | Richards | DEF | 8 | 4.6 | 2.95 | 8.75 | 15.63 | 0.00 | 28.6 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.52 | 13.31 | 22.52 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.49 | 12.30 | 19.78 | 1.00 | 80.1 | 27.0 |
| Bench 2 | Autosub In | Raúl | FWD | 10 | 6.3 | 3.91 | 10.67 | 17.07 | 2.00 | 80.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 94.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.3 | 4.64 | 14.63 | 24.00 | 1.00 | 85.0 | 81.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.83 | 14.52 | 23.66 | 0.00 | 84.9 | 0.0 |
| XI | Bench | B.Fernandes | MID | 14 | 9.2 | 3.93 | 14.49 | 28.51 | 0.00 | 25.3 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 3.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.95
- Actual score: 55.00
- Transfer: Raúl -> Ekitiké (projected gain 4.04, hit 0)
- Autosub outfielders: O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 10.72 | 17.03 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.26 | 12.51 | 21.09 | 3.00 | 72.9 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.25 | 11.95 | 19.51 | 1.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | O'Reilly | DEF | 13 | 5.3 | 3.44 | 9.90 | 16.45 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Richards | DEF | 8 | 4.5 | 1.19 | 4.53 | 8.98 | 0.00 | 31.0 | 0.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 5.13 | 14.94 | 23.55 | 0.00 | 74.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.29 | 12.32 | 20.30 | 17.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.69 | 11.39 | 18.93 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.14 | 17.75 | 28.80 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 92.4 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.4 | 5.10 | 14.29 | 22.92 | 5.00 | 85.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 4.07 | 13.22 | 23.23 | 17.00 | 61.2 | 90.0 |
| Bench 3 | Bench | B.Fernandes | MID | 14 | 9.1 | 3.01 | 11.41 | 22.21 | 0.00 | 15.7 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.28
- Actual score: 49.00
- Transfer: B.Fernandes -> Cherki (projected gain 3.61, hit 0)
- Autosub outfielders: João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.73 | 10.65 | 17.15 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.33 | 12.72 | 20.55 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Virgil | DEF | 12 | 5.9 | 3.48 | 10.94 | 18.08 | 6.00 | 85.4 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 3.57 | 9.96 | 16.21 | 1.00 | 79.3 | 17.0 |
| Bench 4 | Bench | Richards | DEF | 8 | 4.5 | 0.77 | 2.43 | 6.09 | 0.00 | 15.3 | 0.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 4.41 | 14.70 | 24.44 | 0.00 | 59.6 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 91.8 | 81.0 |
| Bench 2 | Autosub In | João Pedro | FWD | 7 | 7.2 | 4.02 | 11.86 | 19.16 | 1.00 | 71.7 | 15.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.03 | 17.10 | 27.99 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.26 | 15.27 | 23.71 | 1.00 | 87.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.85 | 14.77 | 23.68 | 3.00 | 81.8 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.68 | 13.88 | 23.78 | 3.00 | 79.6 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 2.90 -> 3.10
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.11
- Actual score: 32.00
- Transfer: Virgil -> Tarkowski (projected gain 1.53, hit 0)
- Autosub outfielders: O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.10 | 17.58 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 93.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.59 | 13.35 | 20.93 | 5.00 | 84.4 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| Bench 3 | Autosub In | O'Reilly | DEF | 13 | 5.3 | 2.85 | 9.09 | 15.38 | -1.00 | 65.0 | 45.0 |
| Bench 4 | Bench | Richards | DEF | 8 | 4.4 | 0.59 | 2.51 | 5.79 | 2.00 | 14.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 89.0 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 4.22 | 12.87 | 23.17 | 2.00 | 17.8 | 90.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 3.63 | 11.87 | 20.25 | 8.00 | 58.9 | 73.0 |
| Captain | Captain | Foden | MID | 13 | 8.8 | 5.26 | 15.77 | 26.08 | 1.00 | 74.5 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.93 | 15.11 | 24.50 | 1.00 | 59.9 | 45.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.10 | 14.44 | 23.40 | 2.00 | 84.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 4.68 | 14.01 | 23.63 | 3.00 | 76.7 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 3.10 -> 2.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.43
- Actual score: 41.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Richards -> Senesi (projected gain 0.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.19 | 11.83 | 18.54 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.76 | 13.65 | 21.26 | 1.00 | 85.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.75 | 13.27 | 21.66 | 4.00 | 87.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.35 | 12.25 | 19.36 | 3.00 | 88.6 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 8 | 5.3 | 4.06 | 11.79 | 20.03 | 6.00 | 35.8 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.2 | 3.05 | 8.90 | 15.04 | 6.00 | 67.7 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.14 | 15.66 | 26.45 | 1.00 | 40.9 | 31.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 91.7 | 90.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.1 | 3.81 | 11.82 | 19.32 | 12.00 | 50.9 | 84.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.57 | 15.93 | 25.71 | 8.00 | 87.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 5.37 | 15.57 | 24.54 | 1.00 | 89.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.22 | 14.77 | 23.80 | 8.00 | 84.8 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.19 | 14.48 | 24.35 | 3.00 | 59.7 | 72.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 4.75 | 14.25 | 24.75 | 1.00 | 54.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 2.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.43
- Actual score: 64.00
- Transfer: João Pedro -> Woltemade (projected gain 0.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 11.50 | 17.98 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 96.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.37 | 12.65 | 20.10 | 5.00 | 81.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.50 | 12.64 | 19.85 | 8.00 | 91.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.29 | 12.58 | 20.74 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 5.1 | 3.13 | 9.36 | 15.34 | 1.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Guéhi | DEF | 8 | 5.2 | 2.79 | 8.15 | 13.47 | 3.00 | 56.4 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.11 | 14.93 | 24.81 | 13.00 | 45.1 | 83.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Woltemade | FWD | 15 | 7.2 | 3.64 | 11.55 | 19.21 | 1.00 | 60.0 | 17.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.17 | 15.13 | 23.89 | 3.00 | 88.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 4.73 | 13.57 | 23.05 | 8.00 | 57.3 | 68.0 |
| XI | XI | Foden | MID | 13 | 8.6 | 4.02 | 13.47 | 23.53 | 1.00 | 62.1 | 2.0 |

## GW25

- Train rows: 179450
- Bank: 2.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.90
- Actual score: 52.00
- Transfer: Foden -> B.Fernandes (projected gain 2.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.50 | 12.21 | 18.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 93.9 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.71 | 12.83 | 20.44 | 6.00 | 79.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.42 | 12.49 | 20.23 | 2.00 | 88.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.20 | 12.37 | 20.17 | 3.00 | 82.0 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.20 | 12.34 | 20.32 | 2.00 | 86.3 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.0 | 2.79 | 8.84 | 14.45 | 2.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 5 | 7.2 | 4.11 | 13.91 | 23.00 | 5.00 | 85.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.75 | 13.81 | 22.28 | 2.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Woltemade | FWD | 15 | 7.1 | 3.18 | 9.89 | 17.57 | 1.00 | 28.7 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 5.46 | 16.04 | 24.93 | 10.00 | 79.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.47 | 15.77 | 24.98 | 10.00 | 87.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.4 | 5.50 | 15.68 | 25.10 | 5.00 | 87.1 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.29 | 13.01 | 21.74 | 1.00 | 72.0 | 29.0 |

## GW26

- Train rows: 180267
- Bank: 1.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: J.Timber
- Effective captain: Rice
- Chip used: triple_captain
- Predicted score: 76.45
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.57) beats the best remaining Triple Captain opportunity (7.76).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Woltemade -> João Pedro (projected gain 2.92, hit 0)
- Chip used: Triple Captain on Rice. Optimizer chose Triple Captain here because the current estimated captain upside (10.57) beats the best remaining Triple Captain opportunity (7.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 6.24 | 15.56 | 23.63 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 92.9 | 90.0 |
| Vice Captain | XI | J.Timber | DEF | 1 | 6.4 | 6.72 | 16.67 | 25.27 | 3.00 | 127.3 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 93.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.23 | 12.03 | 19.85 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.8 | 4.04 | 11.60 | 19.22 | 1.00 | 83.1 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.0 | 3.40 | 9.24 | 14.07 | 13.00 | 81.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.46 | 15.24 | 23.87 | 10.00 | 79.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.51 | 14.17 | 23.48 | 2.00 | 86.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.57 | 13.11 | 20.79 | 2.00 | 77.0 | 87.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.55 | 19.64 | 30.83 | 14.00 | 103.2 | 180.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 5.96 | 16.50 | 26.29 | 2.00 | 76.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 91.0 | 90.0 |
| Bench 2 | Bench | Cherki | MID | 13 | 6.6 | 4.48 | 12.42 | 20.65 | 1.00 | 63.2 | 19.0 |

## GW27

- Train rows: 181084
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 68.58
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: O'Reilly -> Virgil (projected gain 3.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 105.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 105.5 | 56.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.16 | 14.70 | 23.49 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.8 | 4.10 | 11.35 | 18.75 | 5.00 | 62.9 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.8 | 3.79 | 10.73 | 17.96 | 1.00 | 81.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.93 | 15.99 | 24.81 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.07 | 14.40 | 23.53 | 2.00 | 84.8 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.88 | 13.47 | 21.12 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 120.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.61 | 15.97 | 25.90 | 2.00 | 75.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.31 | 14.84 | 23.93 | 2.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Cherki | MID | 13 | 6.5 | 3.54 | 10.60 | 17.97 | 1.00 | 56.7 | 32.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 63.30
- Actual score: 69.00
- Transfer: B.Fernandes -> Mbeumo (projected gain 3.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.53 | 12.97 | 20.77 | 8.00 | 88.1 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 4.8 | 4.15 | 11.25 | 18.20 | 4.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.23 | 9.64 | 16.04 | 3.00 | 81.2 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.57 | 16.62 | 26.04 | 2.00 | 81.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.44 | 15.10 | 24.18 | 6.00 | 84.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.91 | 13.57 | 20.91 | 15.00 | 76.5 | 75.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 101.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.6 | 5.16 | 14.54 | 22.51 | 2.00 | 70.1 | 85.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.14 | 14.37 | 23.01 | 2.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Cherki | MID | 13 | 6.5 | 2.98 | 9.62 | 16.54 | 3.00 | 27.2 | 87.0 |

## GW29

- Train rows: 182721
- Bank: 1.20 -> 1.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 64.72
- Actual score: 64.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Cherki -> Wilson (projected gain 0.58, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.30 | 9.34 | 14.71 | 2.00 | 88.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.40 | 13.00 | 91.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 4.9 | 3.92 | 11.23 | 17.81 | 11.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.7 | 4.09 | 11.03 | 17.15 | 15.00 | 85.4 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.7 | 5.65 | 16.22 | 25.65 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.18 | 14.70 | 23.11 | 2.00 | 86.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.13 | 14.66 | 22.70 | 2.00 | 80.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 97.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 96.1 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 5.08 | 14.74 | 22.90 | 1.00 | 71.9 | 76.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 5.03 | 13.84 | 21.81 | 0.00 | 84.0 | 0.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 4.71 | 13.35 | 21.29 | 1.00 | 84.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 1.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: bench_boost
- Predicted score: 79.15
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.36) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Wilson -> Szoboszlai (projected gain 0.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.36) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.44 | 14.67 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.18 | 14.78 | 23.11 | 2.00 | 87.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 5.06 | 14.37 | 22.48 | 1.00 | 91.2 | 37.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.51 | 12.41 | 19.27 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench Boost | Tarkowski | DEF | 9 | 5.7 | 3.64 | 11.13 | 17.56 | 0.00 | 88.8 | 0.0 |
| Bench 4 | Bench Boost | Senesi | DEF | 4 | 4.9 | 3.19 | 8.97 | 13.84 | 10.00 | 72.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 5.48 | 15.83 | 24.72 | 1.00 | 74.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.05 | 13.93 | 21.55 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 96.0 | 74.0 |
| XI | XI | Mbeumo | MID | 14 | 8.7 | 5.03 | 14.37 | 22.80 | 2.00 | 67.4 | 74.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.74 | 14.13 | 23.44 | 3.00 | 83.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 12 | 6.9 | 4.62 | 12.92 | 19.86 | 11.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Rogers | MID | 2 | 7.6 | 4.09 | 12.52 | 20.28 | 2.00 | 83.9 | 90.0 |