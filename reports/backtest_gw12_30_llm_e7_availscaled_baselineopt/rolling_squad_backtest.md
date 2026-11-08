# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1173.31
- Total actual points: 1027.00
- Average predicted points: 61.75
- Average actual points: 54.05
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: M.Salah
- Vice captain: Mbeumo
- Effective captain: M.Salah
- Chip used: none
- Predicted score: 60.90
- Actual score: 42.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Thiago, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.45 | 12.31 | 19.07 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.61 | 10.07 | 15.86 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 5.45 | 16.16 | 26.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.94 | 13.93 | 23.23 | 5.00 | 36.1 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 4.38 | 13.21 | 21.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.77 | 13.08 | 21.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.74 | 13.05 | 21.40 | 14.00 | 83.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.0 | 4.82 | 15.27 | 24.21 | 1.00 | 76.4 | 59.0 |
| Bench 2 | Autosub In | Thiago | FWD | 5 | 6.2 | 4.44 | 12.79 | 20.23 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Calvert-Lewin | FWD | 11 | 5.5 | 3.08 | 9.33 | 15.84 | 1.00 | 60.3 | 19.0 |
| Captain | Captain | M.Salah | MID | 12 | 14.2 | 5.80 | 16.25 | 26.06 | 2.00 | 81.3 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.4 | 5.75 | 16.15 | 25.24 | 1.00 | 91.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 5.08 | 15.35 | 24.15 | 6.00 | 87.1 | 90.0 |
| XI | XI | Gakpo | MID | 12 | 7.6 | 4.66 | 13.91 | 22.98 | 2.00 | 64.0 | 90.0 |
| XI | Bench | Caicedo | MID | 7 | 6.0 | 4.63 | 13.61 | 21.57 | 0.00 | 84.9 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: M.Salah
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 59.06
- Actual score: 57.00
- Transfer: Caicedo -> O.Dango (projected gain 0.07, hit 0)
- Autosub outfielders: O.Dango.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.92 | 11.57 | 18.38 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.31 | 9.73 | 15.28 | 1.00 | 92.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 5.02 | 13.96 | 22.43 | 1.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Gabriel | DEF | 1 | 6.5 | 3.28 | 13.42 | 26.60 | 0.00 | 24.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.43 | 13.40 | 22.00 | 2.00 | 92.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.64 | 13.36 | 22.13 | 0.00 | 83.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 4.36 | 12.66 | 20.25 | 0.00 | 86.9 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.71 | 14.94 | 24.20 | 6.00 | 64.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 5.27 | 14.59 | 22.84 | 13.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Calvert-Lewin | FWD | 11 | 5.5 | 0.99 | 3.82 | 6.64 | 7.00 | 26.3 | 45.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.54 | 16.42 | 25.91 | 1.00 | 84.9 | 90.0 |
| Captain | Bench | M.Salah | MID | 12 | 14.2 | 5.61 | 16.05 | 25.55 | 0.00 | 80.0 | 0.0 |
| XI | XI | Rice | MID | 1 | 6.9 | 5.35 | 15.90 | 25.87 | 4.00 | 92.2 | 90.0 |
| XI | XI | Gakpo | MID | 12 | 7.5 | 4.60 | 13.17 | 20.98 | 14.00 | 63.7 | 90.0 |
| Bench 2 | Autosub In | O.Dango | MID | 5 | 6.0 | 4.31 | 11.75 | 18.50 | 12.00 | 44.9 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 58.72
- Actual score: 49.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gabriel -> J.Timber (projected gain 1.16, hit 0)
- Autosub outfielders: O.Dango.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.04 | 11.40 | 17.93 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.49 | 9.62 | 15.14 | 2.00 | 91.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.74 | 13.57 | 21.60 | 1.00 | 83.4 | 46.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 4.62 | 13.34 | 21.39 | 14.00 | 85.2 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 4.55 | 13.06 | 21.02 | 0.00 | 92.4 | 0.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 4.09 | 12.49 | 19.95 | 0.00 | 85.8 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.19 | 12.17 | 19.99 | 14.00 | 82.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 5.10 | 15.81 | 25.46 | 1.00 | 87.4 | 30.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.94 | 13.67 | 21.71 | 2.00 | 84.1 | 63.0 |
| Bench 4 | Bench | Calvert-Lewin | FWD | 11 | 5.5 | 2.85 | 8.31 | 13.64 | 9.00 | 36.1 | 85.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.59 | 15.79 | 25.46 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 5.32 | 15.63 | 25.82 | 3.00 | 89.0 | 82.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 5.21 | 15.56 | 26.00 | 1.00 | 55.8 | 45.0 |
| XI | XI | Gakpo | MID | 12 | 7.5 | 4.84 | 13.19 | 21.18 | 1.00 | 81.1 | 45.0 |
| Bench 3 | Autosub In | O.Dango | MID | 5 | 6.0 | 3.90 | 11.91 | 19.00 | 2.00 | 78.3 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Muñoz
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 57.79
- Actual score: 56.00
- Transfer: O.Dango -> Minteh (projected gain 1.91, hit 0)
- Autosub outfielders: Van de Ven, Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.08 | 11.98 | 19.02 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 9.76 | 15.27 | 3.00 | 91.0 | 90.0 |
| Vice Captain | Bench | Muñoz | DEF | 8 | 6.0 | 5.17 | 15.01 | 23.82 | 0.00 | 92.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.74 | 13.92 | 22.03 | 8.00 | 94.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.38 | 13.45 | 22.05 | 3.00 | 68.8 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 5.0 | 3.39 | 10.98 | 20.75 | 8.00 | 61.5 | 61.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.45 | 10.29 | 17.69 | 6.00 | 33.7 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.76 | 14.06 | 22.81 | 2.00 | 76.5 | 65.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 4.60 | 13.64 | 22.18 | 2.00 | 75.1 | 90.0 |
| Bench 3 | Autosub In | Calvert-Lewin | FWD | 11 | 5.5 | 3.44 | 9.19 | 14.38 | 6.00 | 74.1 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 5.61 | 15.61 | 25.13 | 8.00 | 85.1 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.1 | 4.96 | 15.09 | 25.15 | 0.00 | 61.5 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 4.78 | 14.91 | 24.96 | 6.00 | 85.4 | 90.0 |
| XI | XI | Gakpo | MID | 12 | 7.5 | 4.42 | 13.06 | 20.94 | 2.00 | 71.0 | 82.0 |
| XI | XI | Minteh | MID | 6 | 6.2 | 4.66 | 12.98 | 20.74 | 3.00 | 81.5 | 71.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 5.30
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Mbeumo
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 59.41
- Actual score: 43.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: M.Salah -> B.Fernandes (projected gain 6.53, hit 0)
- Autosub outfielders: Minteh, Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.38 | 11.73 | 18.19 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.90 | 10.35 | 16.04 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 4.86 | 14.31 | 22.65 | 1.00 | 92.8 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.1 | 4.33 | 13.85 | 23.11 | 0.00 | 63.6 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.85 | 13.63 | 21.35 | 2.00 | 87.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 4.09 | 11.75 | 19.44 | 1.00 | 57.3 | 90.0 |
| Bench 3 | Autosub In | Senesi | DEF | 4 | 5.0 | 3.76 | 11.54 | 19.54 | 1.00 | 67.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 4.88 | 14.77 | 23.81 | 2.00 | 79.8 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 4.72 | 14.24 | 23.47 | 2.00 | 66.6 | 62.0 |
| Bench 4 | Bench | Calvert-Lewin | FWD | 11 | 5.5 | 3.47 | 9.75 | 15.32 | 9.00 | 70.1 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 14 | 9.0 | 6.25 | 17.72 | 28.42 | 13.00 | 96.0 | 90.0 |
| Vice Captain | XI | Mbeumo | MID | 14 | 8.5 | 5.41 | 15.34 | 25.16 | 2.00 | 87.2 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 5.04 | 14.26 | 23.59 | 2.00 | 84.7 | 90.0 |
| XI | Bench | Gakpo | MID | 12 | 7.5 | 4.34 | 12.35 | 19.80 | 0.00 | 66.7 | 0.0 |
| Bench 2 | Autosub In | Minteh | MID | 6 | 6.3 | 4.05 | 12.07 | 19.20 | 2.00 | 76.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 5.30 -> 4.00
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.64
- Actual score: 54.00
- Transfer: Gakpo -> Foden (projected gain 9.16, hit 0)
- Autosub outfielders: Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.54 | 18.21 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.48 | 14.91 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.80 | 14.08 | 22.27 | 1.00 | 89.1 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.23 | 12.96 | 21.41 | 6.00 | 79.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 4.04 | 11.45 | 19.52 | 4.00 | 78.7 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.97 | 11.24 | 18.60 | 0.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.0 | 1.06 | 4.30 | 8.98 | 0.00 | 13.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.16 | 16.33 | 26.03 | 2.00 | 65.8 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.9 | 3.56 | 12.98 | 24.08 | 2.00 | 57.7 | 76.0 |
| Bench 2 | Autosub In | Calvert-Lewin | FWD | 11 | 5.6 | 3.91 | 10.44 | 16.02 | 13.00 | 78.3 | 86.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 6.43 | 19.17 | 29.89 | 3.00 | 86.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.2 | 6.19 | 18.69 | 30.33 | 1.00 | 92.2 | 45.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 4.48 | 14.23 | 24.95 | 0.00 | 78.8 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.62 | 14.09 | 23.80 | 11.00 | 82.5 | 90.0 |
| XI | XI | Minteh | MID | 6 | 6.2 | 4.31 | 12.27 | 20.05 | 3.00 | 73.3 | 70.0 |

## GW18

- Train rows: 173897
- Bank: 4.00 -> 4.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.43
- Actual score: 51.00
- Transfer: Mbeumo -> Semenyo (projected gain 4.34, hit 0)
- Autosub outfielders: Minteh.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.43 | 17.97 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.54 | 9.68 | 15.04 | 11.00 | 89.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.87 | 13.66 | 21.69 | 2.00 | 90.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.14 | 12.83 | 20.64 | 2.00 | 88.9 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 3.41 | 10.00 | 16.11 | 11.00 | 83.3 | 90.0 |
| Bench 3 | Bench | J.Timber | DEF | 1 | 6.5 | 3.36 | 9.41 | 14.89 | 0.00 | 65.5 | 0.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 0.97 | 3.45 | 6.99 | 0.00 | 10.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.59 | 13.50 | 21.70 | 5.00 | 83.3 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.8 | 4.01 | 12.14 | 20.12 | 2.00 | 70.5 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 11 | 5.7 | 3.96 | 11.19 | 17.39 | 8.00 | 79.6 | 84.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.12 | 18.40 | 29.36 | 2.00 | 66.1 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 5.94 | 17.83 | 29.38 | 0.00 | 79.0 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 5.28 | 15.57 | 25.11 | 9.00 | 89.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.92 | 14.59 | 23.58 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Minteh | MID | 6 | 6.1 | 3.46 | 11.26 | 18.88 | 1.00 | 73.9 | 45.0 |

## GW19

- Train rows: 174672
- Bank: 4.60 -> 3.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 56.50
- Actual score: 42.00
- Transfer: Mateta -> Ekitiké (projected gain 3.93, hit 0)
- Autosub outfielders: Minteh, Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.05 | 17.50 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.72 | 10.25 | 15.97 | 2.00 | 92.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.73 | 13.11 | 20.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 4.05 | 12.55 | 19.86 | 3.00 | 92.4 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.5 | 4.07 | 11.98 | 20.16 | 9.00 | 29.3 | 82.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.6 | 3.48 | 10.54 | 16.74 | 6.00 | 87.0 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.12 | 3.39 | 6.30 | 0.00 | 10.5 | 0.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.0 | 5.16 | 15.24 | 24.04 | 2.00 | 75.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.52 | 13.31 | 22.52 | 2.00 | 80.3 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 11 | 5.8 | 4.03 | 11.99 | 19.30 | 1.00 | 67.5 | 20.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 5.91 | 17.79 | 28.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.85 | 25.14 | 5.00 | 94.2 | 90.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.83 | 14.52 | 23.66 | 0.00 | 84.9 | 0.0 |
| XI | Bench | B.Fernandes | MID | 14 | 9.2 | 3.93 | 14.49 | 28.51 | 0.00 | 17.3 | 0.0 |
| Bench 2 | Autosub In | Minteh | MID | 6 | 6.1 | 3.82 | 10.81 | 17.53 | 4.00 | 72.4 | 57.0 |

## GW20

- Train rows: 175452
- Bank: 3.30 -> 2.60
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.56
- Actual score: 59.00
- Transfer: Minteh -> Cherki (projected gain 4.61, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 10.72 | 17.03 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.50 | 9.86 | 15.46 | 1.00 | 91.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.63 | 13.74 | 21.91 | 2.00 | 94.3 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.26 | 12.51 | 21.09 | 3.00 | 72.9 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.9 | 3.97 | 12.00 | 19.83 | 1.00 | 65.8 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 4.20 | 11.60 | 17.92 | 7.00 | 65.8 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.8 | 1.07 | 4.14 | 7.84 | 0.00 | 16.0 | 0.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 5.13 | 14.94 | 23.55 | 0.00 | 74.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.29 | 12.32 | 20.30 | 17.00 | 81.4 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 11 | 5.8 | 4.15 | 11.92 | 19.75 | 2.00 | 37.7 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 6.14 | 17.75 | 28.80 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.51 | 16.02 | 25.33 | 1.00 | 92.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 5.31 | 15.54 | 24.56 | 4.00 | 83.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 4.07 | 13.22 | 23.23 | 17.00 | 61.2 | 90.0 |
| Bench 3 | Bench | B.Fernandes | MID | 14 | 9.1 | 3.01 | 11.41 | 22.21 | 0.00 | 13.7 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 2.60 -> 4.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 58.69
- Actual score: 53.00
- Transfer: B.Fernandes -> Rogers (projected gain 4.19, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.73 | 10.65 | 17.15 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.70 | 15.28 | 3.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 4.69 | 13.30 | 21.52 | 6.00 | 92.8 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.33 | 12.72 | 20.55 | 6.00 | 78.1 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.98 | 11.76 | 18.21 | 0.00 | 90.5 | 90.0 |
| Bench 2 | Autosub In | Senesi | DEF | 4 | 4.8 | 3.78 | 10.73 | 18.61 | 6.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.8 | 0.92 | 3.06 | 5.74 | 0.00 | 12.5 | 0.0 |
| XI | Bench | Ekitiké | FWD | 12 | 9.1 | 4.41 | 14.70 | 24.44 | 0.00 | 27.6 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 5.24 | 13.97 | 22.15 | 12.00 | 91.8 | 81.0 |
| Bench 3 | Bench | Calvert-Lewin | FWD | 11 | 5.9 | 3.66 | 11.39 | 18.35 | 8.00 | 76.0 | 86.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 6.03 | 17.10 | 27.99 | 2.00 | 85.6 | 72.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 5.46 | 15.39 | 24.69 | 6.00 | 91.6 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.26 | 15.27 | 23.71 | 1.00 | 87.3 | 17.0 |
| XI | XI | Rogers | MID | 2 | 7.5 | 4.85 | 14.77 | 23.68 | 3.00 | 81.8 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 4.68 | 13.88 | 23.78 | 3.00 | 79.6 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 4.20 -> 4.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 57.38
- Actual score: 33.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Muñoz -> Tarkowski (projected gain 2.10, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.10 | 17.58 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.26 | 9.57 | 15.20 | 5.00 | 92.3 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 4.66 | 13.56 | 21.91 | 0.00 | 94.3 | 0.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.59 | 13.35 | 20.93 | 5.00 | 84.4 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.38 | 13.19 | 21.33 | 8.00 | 90.2 | 90.0 |
| Bench 4 | Bench | Senesi | DEF | 4 | 4.8 | 4.11 | 11.96 | 19.61 | 3.00 | 86.6 | 90.0 |
| Bench 3 | Autosub In | Van de Ven | DEF | 18 | 4.5 | 4.15 | 11.23 | 17.79 | 0.00 | 85.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.96 | 14.05 | 22.08 | 2.00 | 88.0 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 11 | 5.9 | 4.49 | 12.88 | 20.35 | 2.00 | 75.0 | 90.0 |
| Bench 2 | Bench | Ekitiké | FWD | 12 | 9.0 | 4.22 | 12.87 | 23.17 | 2.00 | 17.8 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.8 | 5.26 | 15.77 | 26.08 | 1.00 | 74.5 | 45.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 5.22 | 15.63 | 25.25 | 2.00 | 90.5 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.93 | 15.11 | 24.50 | 1.00 | 59.9 | 45.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.10 | 14.44 | 23.40 | 2.00 | 80.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.2 | 4.68 | 14.01 | 23.63 | 3.00 | 76.7 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 4.30 -> 3.60
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Thiago
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 60.36
- Actual score: 42.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Senesi -> Chalobah (projected gain 0.25, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.19 | 11.83 | 18.54 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.53 | 9.91 | 15.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.76 | 13.65 | 21.26 | 1.00 | 85.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 4.75 | 13.27 | 21.66 | 4.00 | 87.1 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.5 | 4.28 | 12.50 | 19.52 | 4.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 4.06 | 11.79 | 20.03 | 6.00 | 41.8 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.81 | 10.73 | 17.69 | 7.00 | 87.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.14 | 15.66 | 26.45 | 1.00 | 33.9 | 31.0 |
| Vice Captain | XI | Thiago | FWD | 5 | 7.1 | 5.56 | 14.88 | 23.34 | 2.00 | 91.7 | 90.0 |
| Bench 2 | Bench | Calvert-Lewin | FWD | 11 | 6.0 | 4.34 | 12.44 | 19.66 | 2.00 | 81.5 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 5.57 | 15.93 | 25.71 | 8.00 | 87.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 5.37 | 15.57 | 24.54 | 1.00 | 89.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.22 | 14.77 | 23.80 | 8.00 | 84.8 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 5.19 | 14.48 | 24.35 | 3.00 | 59.7 | 72.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 4.75 | 14.25 | 24.75 | 1.00 | 54.6 | 29.0 |

## GW24

- Train rows: 178639
- Bank: 3.60 -> 0.80
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 59.01
- Actual score: 61.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Calvert-Lewin -> Watkins (projected gain 1.12, hit 0)
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 11.50 | 17.98 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.44 | 10.12 | 16.18 | 1.00 | 96.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.37 | 12.65 | 20.10 | 5.00 | 81.2 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 4.29 | 12.58 | 20.74 | 2.00 | 86.4 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.6 | 4.48 | 12.57 | 19.84 | 3.00 | 89.6 | 90.0 |
| Bench 2 | Autosub In | Guéhi | DEF | 8 | 5.2 | 4.19 | 12.23 | 20.23 | 3.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.6 | 3.88 | 11.28 | 18.40 | 0.00 | 90.5 | 0.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.11 | 14.93 | 24.81 | 13.00 | 61.1 | 83.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.73 | 14.33 | 22.68 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Watkins | FWD | 2 | 8.8 | 4.67 | 13.31 | 21.62 | 0.00 | 78.7 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 5.86 | 16.62 | 26.55 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 5.70 | 15.98 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.4 | 5.12 | 14.98 | 23.65 | 3.00 | 88.7 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 4.73 | 13.57 | 23.05 | 8.00 | 69.3 | 68.0 |
| Bench 3 | Bench | Foden | MID | 13 | 8.6 | 4.02 | 13.47 | 23.53 | 1.00 | 62.1 | 2.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rice
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 57.74
- Actual score: 47.00
- Transfer: Tarkowski -> Virgil (projected gain 0.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.50 | 12.21 | 18.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.63 | 9.99 | 15.84 | 1.00 | 93.9 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.47 | 13.07 | 20.59 | 0.00 | 91.6 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 4.71 | 12.83 | 20.44 | 6.00 | 79.5 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.34 | 12.46 | 20.07 | 4.00 | 87.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.20 | 12.37 | 20.17 | 3.00 | 57.0 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.88 | 9.72 | 17.09 | 1.00 | 66.5 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.11 | 13.91 | 23.00 | 5.00 | 62.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.8 | 4.75 | 13.81 | 22.28 | 2.00 | 77.3 | 90.0 |
| Bench 2 | Bench | Watkins | FWD | 2 | 8.8 | 3.31 | 10.79 | 19.58 | 2.00 | 50.6 | 85.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 5.69 | 16.49 | 26.55 | 2.00 | 92.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.47 | 15.77 | 24.98 | 10.00 | 87.2 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.4 | 5.50 | 15.68 | 25.10 | 5.00 | 87.1 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.29 | 13.01 | 21.74 | 1.00 | 72.0 | 29.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.4 | 0.97 | 4.26 | 8.46 | 0.00 | 14.7 | 0.0 |

## GW26

- Train rows: 180267
- Bank: 0.70 -> 1.90
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: J.Timber
- Effective captain: Rice
- Chip used: triple_captain
- Predicted score: 75.16
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.57) beats the best remaining Triple Captain opportunity (7.76).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Watkins -> João Pedro (projected gain 2.63, hit 0)
- Chip used: Triple Captain on Rice. Optimizer chose Triple Captain here because the current estimated captain upside (10.57) beats the best remaining Triple Captain opportunity (7.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 6.24 | 15.56 | 23.63 | 3.00 | 132.4 | 180.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.37 | 9.72 | 15.33 | 1.00 | 92.9 | 90.0 |
| Vice Captain | XI | J.Timber | DEF | 1 | 6.4 | 6.72 | 16.67 | 25.27 | 3.00 | 127.3 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.00 | 13.82 | 21.51 | 7.00 | 92.1 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 12 | 5.9 | 4.19 | 12.64 | 20.13 | 17.00 | 90.5 | 90.0 |
| XI | XI | Chalobah | DEF | 7 | 5.7 | 4.41 | 12.62 | 20.35 | 3.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.81 | 11.02 | 18.07 | 3.00 | 81.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 5.46 | 15.24 | 23.87 | 10.00 | 73.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 4.51 | 14.17 | 23.48 | 2.00 | 86.3 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.57 | 13.11 | 20.79 | 2.00 | 77.0 | 87.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.55 | 19.64 | 30.83 | 14.00 | 94.2 | 180.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 5.88 | 16.23 | 25.83 | 14.00 | 90.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.25 | 15.35 | 24.44 | 2.00 | 91.0 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.6 | 4.48 | 12.42 | 20.65 | 1.00 | 63.2 | 19.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.3 | 2.24 | 7.44 | 14.16 | 5.00 | 15.1 | 70.0 |

## GW27

- Train rows: 181084
- Bank: 1.90 -> 0.30
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 68.52
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Foden -> B.Fernandes (projected gain 3.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 5.19 | 14.35 | 22.00 | 3.00 | 111.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.96 | 8.93 | 14.19 | 2.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 5.82 | 16.20 | 24.87 | 3.00 | 107.5 | 56.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.16 | 14.70 | 23.49 | 11.00 | 94.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 5.03 | 14.35 | 22.37 | 2.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Chalobah | DEF | 7 | 5.8 | 4.58 | 12.57 | 20.27 | 2.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.40 | 10.23 | 16.85 | 0.00 | 82.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 5.87 | 15.82 | 24.55 | 7.00 | 85.6 | 79.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.07 | 14.40 | 23.53 | 2.00 | 85.8 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.88 | 13.47 | 21.12 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.5 | 7.25 | 20.88 | 32.72 | 4.00 | 119.6 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.9 | 6.07 | 16.84 | 26.68 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.61 | 15.97 | 25.90 | 2.00 | 81.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 5.31 | 14.84 | 23.93 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Cherki | MID | 13 | 6.5 | 3.54 | 10.60 | 17.97 | 1.00 | 27.7 | 32.0 |

## GW28

- Train rows: 181902
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 63.75
- Actual score: 80.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Cherki -> Wilson (projected gain 0.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 11.87 | 18.73 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.35 | 9.37 | 14.66 | 0.00 | 89.1 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 5.32 | 14.69 | 23.59 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.52 | 13.34 | 21.16 | 6.00 | 90.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.53 | 12.97 | 20.77 | 8.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.8 | 3.65 | 11.68 | 19.51 | 1.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.5 | 3.73 | 11.04 | 17.37 | 0.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.57 | 16.62 | 26.04 | 2.00 | 62.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 5.44 | 15.10 | 24.18 | 6.00 | 84.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 4.91 | 13.57 | 20.91 | 15.00 | 76.5 | 75.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 6.22 | 18.32 | 29.37 | 5.00 | 102.6 | 75.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 5.99 | 17.41 | 27.59 | 8.00 | 89.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 5.60 | 15.80 | 25.34 | 13.00 | 82.3 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 5.14 | 14.37 | 23.01 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 5.9 | 4.56 | 13.16 | 20.65 | 12.00 | 87.6 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 0.90 -> 0.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: B.Fernandes
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 65.39
- Actual score: 71.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Van de Ven -> O'Reilly (projected gain 0.07, hit 0)
- Autosub outfielders: Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.86 | 18.60 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.30 | 9.34 | 14.71 | 2.00 | 88.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 5.52 | 15.66 | 24.71 | 1.00 | 89.7 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.40 | 13.00 | 91.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.88 | 13.50 | 21.15 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | O'Reilly | DEF | 13 | 5.0 | 4.58 | 12.41 | 19.64 | 0.00 | 74.4 | 0.0 |
| Bench 4 | Bench | Chalobah | DEF | 7 | 5.7 | 3.43 | 10.97 | 18.30 | 2.00 | 83.7 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 5.65 | 16.22 | 25.65 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 5.18 | 14.70 | 23.11 | 2.00 | 86.2 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 8.9 | 5.13 | 14.66 | 22.70 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 6.93 | 19.11 | 29.54 | 7.00 | 100.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 5.55 | 16.78 | 26.40 | 3.00 | 96.1 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 14 | 9.9 | 5.75 | 16.74 | 26.58 | 8.00 | 90.5 | 90.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 5.03 | 13.84 | 21.81 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Autosub In | Rogers | MID | 2 | 7.7 | 4.71 | 13.35 | 21.29 | 1.00 | 84.6 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: bench_boost
- Predicted score: 81.30
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.19) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Wilson -> Anderson (projected gain 0.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 11.62 | 18.12 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 3.40 | 9.35 | 14.52 | 6.00 | 88.7 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 5.18 | 14.78 | 23.11 | 2.00 | 87.2 | 90.0 |
| XI | XI | J.Timber | DEF | 1 | 6.3 | 5.06 | 14.37 | 22.48 | 1.00 | 71.2 | 37.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.51 | 12.41 | 19.27 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench Boost | O'Reilly | DEF | 13 | 5.1 | 4.02 | 11.47 | 18.75 | 2.00 | 57.9 | 90.0 |
| Bench 4 | Bench Boost | Chalobah | DEF | 7 | 5.6 | 3.68 | 10.72 | 17.26 | 2.00 | 83.6 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 6.88 | 18.86 | 29.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Ekitiké | FWD | 12 | 9.1 | 5.48 | 15.83 | 24.72 | 1.00 | 74.3 | 26.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 5.05 | 13.93 | 21.55 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 7.05 | 19.55 | 29.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 6.33 | 18.44 | 28.97 | 10.00 | 77.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 4.74 | 14.13 | 23.44 | 3.00 | 83.0 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 4.64 | 12.78 | 20.10 | 2.00 | 89.1 | 87.0 |
| Bench 2 | Bench Boost | Rogers | MID | 2 | 7.6 | 4.09 | 12.52 | 20.28 | 2.00 | 83.9 | 90.0 |