# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1158.29
- Total actual points: 1001.00
- Average predicted points: 60.96
- Average actual points: 52.68
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
- Predicted score: 64.23
- Actual score: 35.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Van de Ven, O'Reilly, Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.45 | 12.31 | 19.07 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.94 | 13.93 | 23.23 | 5.00 | 41.1 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Autosub In | O'Reilly | DEF | 13 | 4.9 | 4.17 | 12.39 | 19.70 | 1.00 | 84.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 5.66 | 15.79 | 24.66 | 1.00 | 87.7 | 75.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 4.44 | 12.79 | 20.23 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Autosub In | Welbeck | FWD | 6 | 6.5 | 3.89 | 11.10 | 17.52 | 8.00 | 70.3 | 90.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 6.63 | 18.34 | 28.77 | 0.00 | 76.6 | 0.0 |
| Vice Captain | Captain | M.Salah | MID | 12 | 14.2 | 5.80 | 16.25 | 26.06 | 2.00 | 81.3 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 5.08 | 15.35 | 24.15 | 6.00 | 87.1 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.63 | 13.61 | 21.57 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: João Pedro
- Effective captain: Rice
- Chip used: none
- Predicted score: 56.76
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: M.Salah -> B.Fernandes (projected gain 2.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.92 | 11.57 | 18.38 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 92.1 | 90.0 |
| Bench 4 | Bench | Gabriel | DEF | 1 | 6.5 | 3.28 | 13.42 | 26.60 | 0.00 | 53.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 92.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.64 | 13.36 | 22.13 | 0.00 | 83.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.36 | 12.66 | 20.25 | 0.00 | 86.9 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.0 | 4.50 | 12.34 | 19.39 | 4.00 | 83.1 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.5 | 5.33 | 14.90 | 23.76 | 1.00 | 86.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.27 | 14.59 | 22.84 | 13.00 | 83.2 | 90.0 |
| XI | XI | Welbeck | FWD | 6 | 6.5 | 3.92 | 11.62 | 18.43 | 2.00 | 81.7 | 64.0 |
| Captain | Captain | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 92.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 8.0 | 5.08 | 15.75 | 27.16 | 1.00 | 36.8 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 4.60 | 13.69 | 22.52 | 11.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.1 | 3.70 | 11.96 | 20.52 | -2.00 | 62.2 | 37.0 |
| Bench 2 | Bench | Mbeumo | MID | 14 | 8.6 | 3.91 | 11.59 | 18.29 | 1.00 | 62.9 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 5.40 -> 5.50
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.48
- Actual score: 40.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gabriel -> J.Timber (projected gain 1.72, hit 0)
- Autosub outfielders: Welbeck, Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.04 | 11.40 | 17.93 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 91.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.74 | 13.57 | 21.60 | 1.00 | 83.4 | 46.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.1 | 4.60 | 13.24 | 21.10 | 0.00 | 85.5 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 92.4 | 0.0 |
| XI | Bench | Van de Ven | DEF | 18 | 4.8 | 4.09 | 12.49 | 19.95 | 0.00 | 85.8 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.19 | 12.17 | 19.99 | 14.00 | 82.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.10 | 15.81 | 25.46 | 1.00 | 87.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.61 | 14.19 | 23.72 | 2.00 | 75.0 | 90.0 |
| Bench 2 | Autosub In | Welbeck | FWD | 6 | 6.6 | 3.91 | 11.97 | 19.62 | 1.00 | 73.4 | 23.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.59 | 15.79 | 25.46 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.32 | 15.63 | 25.82 | 3.00 | 87.0 | 82.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.06 | 14.67 | 23.91 | 4.00 | 88.8 | 90.0 |
| Bench 3 | Bench | Caicedo | MID | 7 | 6.0 | 3.34 | 11.04 | 19.85 | 0.00 | 62.0 | 0.0 |
| Bench 4 | Autosub In | Semenyo | MID | 4 | 7.9 | 3.32 | 9.74 | 16.44 | 4.00 | 53.8 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 5.50 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.65
- Actual score: 71.00
- Transfer: Rice -> Saka (projected gain 5.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.08 | 11.98 | 19.02 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 76.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.38 | 13.45 | 22.05 | 3.00 | 76.8 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.56 | 12.58 | 20.12 | 6.00 | 81.7 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.39 | 10.98 | 20.75 | 8.00 | 60.5 | 61.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.8 | 1.76 | 5.24 | 9.01 | 6.00 | 33.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.67 | 14.70 | 23.78 | 1.00 | 81.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.60 | 13.64 | 22.18 | 2.00 | 75.1 | 90.0 |
| Bench 2 | Bench | Welbeck | FWD | 6 | 6.6 | 2.07 | 6.08 | 10.27 | 2.00 | 34.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.1 | 5.11 | 16.23 | 26.53 | 4.00 | 45.9 | 78.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.50 | 16.02 | 26.05 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.61 | 15.61 | 25.13 | 8.00 | 85.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 8.9 | 5.40 | 15.60 | 25.06 | 18.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 5.9 | 1.22 | 5.26 | 10.91 | 0.00 | 18.8 | 0.0 |

## GW16

- Train rows: 172367
- Bank: 2.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Saka
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 60.44
- Actual score: 61.00
- Transfer: Welbeck -> Mateta (projected gain 2.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.38 | 11.73 | 18.19 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 92.8 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.29 | 12.20 | 19.58 | 6.00 | 84.4 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 4.09 | 11.75 | 19.44 | 1.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Senesi | DEF | 4 | 5.0 | 3.76 | 11.54 | 19.54 | 1.00 | 76.3 | 90.0 |
| Bench 3 | Bench | J.Timber | DEF | 1 | 6.4 | 3.49 | 9.81 | 15.37 | 2.00 | 65.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.88 | 14.77 | 23.81 | 2.00 | 79.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.72 | 14.24 | 23.47 | 2.00 | 55.6 | 62.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.48 | 13.78 | 23.37 | 2.00 | 71.1 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.1 | 5.84 | 16.39 | 26.18 | 11.00 | 78.8 | 90.0 |
| XI | XI | Mbeumo | MID | 14 | 8.5 | 5.41 | 15.34 | 25.16 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 4.98 | 14.96 | 24.47 | 6.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Caicedo | MID | 7 | 5.8 | 1.11 | 4.30 | 8.65 | 0.00 | 18.4 | 0.0 |

## GW17

- Train rows: 173127
- Bank: 0.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Saka
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 58.22
- Actual score: 47.00
- Transfer: Caicedo -> Wilson (projected gain 2.74, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.54 | 18.21 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.48 | 14.91 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.23 | 12.96 | 21.41 | 6.00 | 79.8 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 4.25 | 12.02 | 19.01 | 6.00 | 83.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.04 | 11.45 | 19.52 | 4.00 | 78.7 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.7 | 3.97 | 11.24 | 18.60 | 0.00 | 79.6 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 4.17 | 13.18 | 22.51 | 6.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.9 | 3.56 | 12.98 | 24.08 | 2.00 | 56.7 | 76.0 |
| Bench 4 | Bench | Thiago | FWD | 5 | 7.1 | 3.05 | 9.66 | 15.40 | 2.00 | 46.8 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 93.2 | 45.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.2 | 5.67 | 16.30 | 26.48 | 3.00 | 79.4 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.32 | 14.84 | 24.25 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.48 | 14.23 | 24.95 | 0.00 | 78.8 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.4 | 4.92 | 13.79 | 21.28 | 2.00 | 85.7 | 83.0 |

## GW18

- Train rows: 173897
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 60.90
- Actual score: 47.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mbeumo -> Foden (projected gain 5.86, hit 0)
- Autosub outfielders: Senesi, Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.58 | 14.89 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| XI | Bench | J.Timber | DEF | 1 | 6.5 | 4.66 | 13.04 | 20.63 | 0.00 | 87.5 | 0.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 4.14 | 12.83 | 20.64 | 2.00 | 89.9 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.3 | 4.39 | 12.77 | 20.36 | 1.00 | 85.6 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.41 | 10.00 | 16.11 | 11.00 | 83.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.59 | 13.50 | 21.70 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.44 | 12.79 | 20.87 | 8.00 | 82.0 | 68.0 |
| Bench 3 | Autosub In | Mateta | FWD | 8 | 7.8 | 4.01 | 12.14 | 20.12 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.12 | 18.40 | 29.36 | 2.00 | 87.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.94 | 17.83 | 29.38 | 0.00 | 84.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.28 | 15.57 | 25.11 | 9.00 | 87.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 5.56 | 15.45 | 24.79 | 7.00 | 81.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.7 | 4.86 | 14.50 | 23.45 | 5.00 | 77.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.50 -> 0.90
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Saka
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.74
- Actual score: 39.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mateta -> Woltemade (projected gain 1.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.05 | 17.50 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.05 | 12.55 | 19.86 | 3.00 | 92.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.07 | 11.98 | 20.16 | 9.00 | 60.3 | 82.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 5.3 | 3.71 | 10.96 | 17.82 | 1.00 | 83.2 | 56.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.48 | 10.54 | 16.74 | 6.00 | 87.0 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.52 | 13.31 | 22.52 | 2.00 | 80.3 | 90.0 |
| XI | XI | Woltemade | FWD | 15 | 7.3 | 4.21 | 12.39 | 20.91 | 1.00 | 69.4 | 10.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.49 | 12.30 | 19.78 | 1.00 | 80.1 | 27.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.3 | 5.50 | 15.93 | 25.91 | 6.00 | 81.9 | 82.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 94.2 | 90.0 |
| Bench 2 | Bench | B.Fernandes | MID | 14 | 9.2 | 3.93 | 14.49 | 28.51 | 0.00 | 18.3 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 5.00 | 14.41 | 22.96 | 2.00 | 89.1 | 84.0 |

## GW20

- Train rows: 175452
- Bank: 0.90 -> 3.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.25
- Actual score: 50.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: B.Fernandes -> Cherki (projected gain 3.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 10.72 | 17.03 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 76.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.26 | 12.51 | 21.09 | 3.00 | 72.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.97 | 12.00 | 19.83 | 1.00 | 86.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.20 | 11.60 | 17.92 | 7.00 | 86.8 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 13 | 5.3 | 3.44 | 9.90 | 16.45 | 2.00 | 73.8 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.29 | 12.32 | 20.30 | 17.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Woltemade | FWD | 15 | 7.4 | 3.85 | 11.76 | 19.51 | 1.00 | 60.4 | 12.0 |
| Bench 3 | Bench | João Pedro | FWD | 7 | 7.2 | 3.69 | 11.39 | 18.93 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.14 | 17.75 | 28.80 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 73.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.31 | 15.54 | 24.56 | 4.00 | 83.0 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 5.24 | 15.19 | 24.53 | 4.00 | 79.3 | 23.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.84 | 13.83 | 22.23 | 6.00 | 83.9 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 3.30 -> 3.00
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 59.91
- Actual score: 58.00
- Transfer: O'Reilly -> Tarkowski (projected gain 1.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.73 | 10.65 | 17.15 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 4.79 | 13.40 | 20.82 | 4.00 | 90.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.33 | 12.72 | 20.55 | 6.00 | 78.1 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.98 | 11.76 | 18.21 | 0.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 3.78 | 10.73 | 18.61 | 6.00 | 81.2 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 91.8 | 81.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 4.02 | 11.86 | 19.16 | 1.00 | 71.7 | 15.0 |
| Bench 4 | Bench | Woltemade | FWD | 15 | 7.4 | 2.60 | 8.37 | 14.13 | 5.00 | 38.0 | 74.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.03 | 17.10 | 27.99 | 2.00 | 85.6 | 72.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 5.32 | 15.59 | 25.65 | 3.00 | 66.6 | 77.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.26 | 15.27 | 23.71 | 1.00 | 87.3 | 17.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 5.02 | 14.19 | 22.77 | 9.00 | 86.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 3.00 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bruno G.
- Vice captain: Semenyo
- Effective captain: Bruno G.
- Chip used: none
- Predicted score: 57.37
- Actual score: 36.00
- Transfer: Foden -> Bruno G. (projected gain 3.15, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.10 | 17.58 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 74.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 76.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.59 | 13.35 | 20.93 | 5.00 | 84.4 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.8 | 4.11 | 11.96 | 19.61 | 3.00 | 86.6 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.15 | 11.23 | 17.79 | 0.00 | 85.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Woltemade | FWD | 15 | 7.3 | 2.14 | 6.50 | 10.62 | 2.00 | 35.8 | 66.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.2 | 1.75 | 5.72 | 9.77 | 8.00 | 28.9 | 73.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.93 | 15.11 | 24.50 | 1.00 | 59.9 | 45.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 5.05 | 15.06 | 24.99 | 1.00 | 41.7 | 33.0 |
| Captain | Captain | Bruno G. | MID | 15 | 7.1 | 5.37 | 14.88 | 23.72 | 3.00 | 92.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 4.82 | 13.57 | 22.03 | 2.00 | 88.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 4.70 -> 2.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.35
- Actual score: 49.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: João Pedro -> Ekitiké (projected gain 3.89, hit 0)
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.19 | 11.83 | 18.54 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.76 | 13.65 | 21.26 | 1.00 | 85.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.80 | 13.41 | 21.89 | 4.00 | 87.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.35 | 12.25 | 19.36 | 3.00 | 88.6 | 90.0 |
| Bench 2 | Autosub In | Guéhi | DEF | 8 | 5.3 | 4.06 | 11.79 | 20.03 | 6.00 | 36.8 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.81 | 10.73 | 17.69 | 7.00 | 87.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.14 | 15.66 | 26.45 | 1.00 | 34.9 | 31.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 91.7 | 90.0 |
| Bench 3 | Bench | Woltemade | FWD | 15 | 7.3 | 4.06 | 11.73 | 19.06 | 1.00 | 36.2 | 28.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.57 | 15.93 | 25.71 | 8.00 | 87.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 5.13 | 15.42 | 25.88 | 2.00 | 31.9 | 90.0 |
| XI | Bench | Bruno G. | MID | 15 | 7.2 | 5.19 | 15.03 | 24.09 | 0.00 | 89.4 | 0.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.19 | 14.48 | 24.35 | 3.00 | 41.7 | 72.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.89 | 13.71 | 22.47 | 10.00 | 83.6 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 2.90 -> 5.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 58.03
- Actual score: 65.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Saka -> Rogers (projected gain 3.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 11.50 | 17.98 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 99.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.37 | 12.65 | 20.10 | 5.00 | 81.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.50 | 12.64 | 19.85 | 8.00 | 91.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.29 | 12.58 | 20.74 | 2.00 | 86.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.19 | 12.23 | 20.23 | 3.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.88 | 11.28 | 18.40 | 0.00 | 90.5 | 0.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.11 | 14.93 | 24.81 | 13.00 | 60.1 | 83.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Woltemade | FWD | 15 | 7.2 | 3.64 | 11.55 | 19.21 | 1.00 | 30.0 | 17.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 89.0 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 4.73 | 13.57 | 23.05 | 8.00 | 46.3 | 68.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.60 | 13.31 | 21.36 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Bruno G. | MID | 15 | 7.3 | 3.90 | 12.60 | 22.33 | 0.00 | 62.4 | 0.0 |

## GW25

- Train rows: 179450
- Bank: 5.30 -> 4.10
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.87
- Actual score: 48.00
- Transfer: Tarkowski -> Gabriel (projected gain 3.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.50 | 12.21 | 18.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 93.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.0 | 5.62 | 15.56 | 24.41 | 6.00 | 86.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.71 | 12.83 | 20.44 | 6.00 | 79.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.42 | 12.49 | 20.23 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.20 | 12.37 | 20.17 | 3.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.88 | 9.72 | 17.09 | 1.00 | 66.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.11 | 13.91 | 23.00 | 5.00 | 85.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.75 | 13.81 | 22.28 | 2.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Woltemade | FWD | 15 | 7.1 | 2.27 | 7.06 | 12.55 | 1.00 | 29.7 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.53 | 15.93 | 25.24 | 10.00 | 87.2 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.29 | 13.01 | 21.74 | 1.00 | 72.0 | 29.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 4.36 | 12.59 | 19.97 | 2.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Bruno G. | MID | 15 | 7.2 | 2.22 | 7.82 | 14.87 | 11.00 | 26.2 | 90.0 |

## GW26

- Train rows: 180267
- Bank: 4.10 -> 6.90
- Free transfers: 2 -> 2
- Captain: J.Timber
- Vice captain: Semenyo
- Effective captain: J.Timber
- Chip used: bench_boost
- Predicted score: 73.81
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.41) beats the best remaining Bench Boost opportunity (12.16).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Gabriel -> H.Bueno (projected gain 2.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.41) beats the best remaining Bench Boost opportunity (12.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 92.9 | 90.0 |
| Bench 1 | Bench Boost | Raya | GK | 1 | 5.9 | 3.35 | 8.34 | 12.67 | 3.00 | 92.4 | 180.0 |
| Captain | Captain | J.Timber | DEF | 1 | 6.4 | 6.72 | 16.67 | 25.27 | 3.00 | 127.3 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 74.1 | 90.0 |
| XI | XI | H.Bueno | DEF | 20 | 4.3 | 5.42 | 12.85 | 19.44 | 8.00 | 125.2 | 149.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.23 | 12.03 | 19.85 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Bench Boost | Van de Ven | DEF | 18 | 4.5 | 3.81 | 11.02 | 18.07 | 3.00 | 81.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.51 | 14.17 | 23.48 | 2.00 | 86.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.57 | 13.11 | 20.79 | 2.00 | 77.0 | 87.0 |
| Bench 4 | Bench Boost | Woltemade | FWD | 15 | 7.0 | 2.17 | 6.87 | 11.53 | 1.00 | 38.2 | 2.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Bruno G. | MID | 15 | 7.1 | 4.38 | 13.68 | 23.29 | 3.00 | 70.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.48 | 12.42 | 20.65 | 1.00 | 62.2 | 19.0 |
| Bench 2 | Bench Boost | Wilson | MID | 10 | 6.1 | 3.97 | 12.31 | 19.78 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 6.90 -> 5.90
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 63.34
- Actual score: 43.00
- Transfer: Cherki -> Rice (projected gain 11.98, hit 0)
- Autosub outfielders: Thiago.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 116.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 99.5 | 56.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 95.2 | 90.0 |
| XI | XI | H.Bueno | DEF | 20 | 4.3 | 4.36 | 11.93 | 18.65 | 4.00 | 109.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.10 | 11.35 | 18.75 | 5.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.44 | 10.34 | 17.04 | 0.00 | 82.4 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.88 | 13.47 | 21.12 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Autosub In | Thiago | FWD | 5 | 7.0 | 3.57 | 10.16 | 16.60 | 2.00 | 62.8 | 90.0 |
| Bench 4 | Bench | Woltemade | FWD | 15 | 6.9 | 1.29 | 5.25 | 9.07 | 1.00 | 24.8 | 59.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 111.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.31 | 14.84 | 23.93 | 2.00 | 83.2 | 90.0 |
| XI | Bench | Bruno G. | MID | 15 | 7.0 | 4.34 | 13.53 | 22.05 | 0.00 | 80.8 | 0.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 3.73 | 11.48 | 19.18 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 5.90 -> 3.80
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 60.52
- Actual score: 91.00
- Transfer: Rogers -> B.Fernandes (projected gain 3.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.53 | 12.97 | 20.77 | 8.00 | 88.1 | 90.0 |
| XI | XI | H.Bueno | DEF | 20 | 4.3 | 4.09 | 11.46 | 18.06 | 6.00 | 99.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 4.15 | 11.25 | 18.20 | 4.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.73 | 11.04 | 17.37 | 0.00 | 89.7 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.44 | 15.10 | 24.18 | 6.00 | 84.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.91 | 13.57 | 20.91 | 15.00 | 76.5 | 75.0 |
| Bench 4 | Bench | Woltemade | FWD | 15 | 6.9 | 2.49 | 6.95 | 10.93 | 1.00 | 46.8 | 55.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 97.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 90.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.60 | 15.80 | 25.34 | 13.00 | 82.3 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 4.56 | 13.16 | 20.65 | 12.00 | 87.6 | 71.0 |
| Bench 2 | Bench | Bruno G. | MID | 15 | 6.9 | 3.87 | 12.18 | 20.83 | 0.00 | 58.6 | 0.0 |

## GW29

- Train rows: 182721
- Bank: 3.80 -> 2.90
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: B.Fernandes
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 62.80
- Actual score: 76.00
- Transfer: Woltemade -> João Pedro (projected gain 6.38, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.30 | 9.34 | 14.71 | 2.00 | 88.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.40 | 13.00 | 91.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| XI | XI | H.Bueno | DEF | 20 | 4.3 | 4.13 | 11.47 | 17.69 | 1.00 | 95.5 | 11.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.92 | 11.23 | 17.81 | 11.00 | 89.3 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.5 | 3.42 | 9.90 | 15.49 | -3.00 | 87.1 | 37.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.65 | 16.22 | 25.65 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.18 | 14.70 | 23.11 | 2.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Ekitiké | FWD | 12 | 8.9 | 3.33 | 9.51 | 14.73 | 2.00 | 54.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 100.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 80.1 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 5.03 | 13.84 | 21.81 | 0.00 | 84.0 | 0.0 |
| Bench 4 | Bench | Bruno G. | MID | 15 | 6.9 | 1.86 | 6.05 | 10.70 | 0.00 | 24.4 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 2.90 -> 1.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 72.63
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Senesi -> Virgil (projected gain 2.82, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.40 | 9.35 | 14.52 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.18 | 14.78 | 23.11 | 2.00 | 87.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 5.06 | 14.37 | 22.48 | 1.00 | 90.2 | 37.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.51 | 12.41 | 19.27 | 2.00 | 87.8 | 90.0 |
| Bench 2 | Bench | H.Bueno | DEF | 20 | 4.3 | 2.42 | 7.68 | 12.50 | 1.00 | 57.5 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 2.08 | 6.66 | 11.08 | 0.00 | 56.8 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 5.48 | 15.83 | 24.72 | 1.00 | 80.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.05 | 13.93 | 21.55 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 94.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.74 | 14.13 | 23.44 | 3.00 | 83.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 4.11 | 12.25 | 20.25 | 3.00 | 61.1 | 90.0 |
| Bench 4 | Bench | Bruno G. | MID | 15 | 6.8 | 0.52 | 2.97 | 6.51 | 0.00 | 3.6 | 0.0 |