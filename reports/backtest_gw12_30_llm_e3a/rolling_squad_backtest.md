# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 928.05
- Total actual points: 1000.00
- Average predicted points: 48.84
- Average actual points: 52.63
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
- Captain: Semenyo
- Vice captain: Mbeumo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 50.96
- Actual score: 44.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: O'Reilly, Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.51 | 9.52 | 14.46 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.01 | 8.27 | 12.06 | 2.00 | 94.2 | 90.0 |
| XI | Bench | Gabriel | DEF | 1 | 6.6 | 4.25 | 12.26 | 20.18 | 0.00 | 90.1 | 0.0 |
| XI | XI | Muñoz | DEF | 8 | 5.7 | 4.04 | 11.28 | 18.17 | 14.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | O'Reilly | DEF | 13 | 4.9 | 3.34 | 10.99 | 17.26 | 1.00 | 84.4 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.8 | 3.88 | 10.71 | 17.41 | 0.00 | 93.4 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.77 | 10.58 | 17.17 | 3.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 4.30 | 12.24 | 19.01 | 1.00 | 87.7 | 75.0 |
| XI | XI | Thiago | FWD | 5 | 6.2 | 3.55 | 11.33 | 17.41 | 4.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Welbeck | FWD | 6 | 6.5 | 2.67 | 8.40 | 12.90 | 8.00 | 70.3 | 90.0 |
| Captain | Bench | Semenyo | MID | 4 | 8.1 | 5.33 | 14.34 | 22.77 | 0.00 | 76.6 | 0.0 |
| Vice Captain | Captain | Mbeumo | MID | 14 | 8.4 | 4.75 | 13.65 | 20.94 | 1.00 | 91.3 | 90.0 |
| XI | XI | M.Salah | MID | 12 | 14.2 | 4.28 | 12.45 | 20.22 | 2.00 | 81.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 6.8 | 3.97 | 12.24 | 19.55 | 6.00 | 87.1 | 90.0 |
| Bench 3 | Autosub In | Anderson | MID | 16 | 5.3 | 3.30 | 10.34 | 16.28 | 9.00 | 87.5 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.20 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 46.69
- Actual score: 36.00
- Transfer: Gabriel -> Guéhi (projected gain 0.66, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.15 | 9.28 | 14.19 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.81 | 8.03 | 11.68 | 1.00 | 92.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.93 | 12.20 | 19.20 | 2.00 | 92.2 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.94 | 11.78 | 19.37 | 0.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.8 | 3.47 | 11.20 | 17.44 | 0.00 | 86.9 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.0 | 3.81 | 10.81 | 16.24 | 4.00 | 83.1 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.8 | 3.57 | 10.71 | 16.80 | 1.00 | 88.4 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 4.12 | 12.29 | 18.97 | 1.00 | 86.9 | 54.0 |
| XI | XI | Thiago | FWD | 5 | 6.4 | 3.94 | 11.16 | 17.76 | 13.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Welbeck | FWD | 6 | 6.5 | 3.10 | 9.58 | 14.80 | 2.00 | 81.7 | 64.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.16 | 12.80 | 20.00 | 1.00 | 62.9 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 6.9 | 4.15 | 12.10 | 20.27 | 4.00 | 92.2 | 90.0 |
| XI | Bench | M.Salah | MID | 12 | 14.2 | 4.13 | 11.86 | 18.71 | 0.00 | 54.0 | 0.0 |
| Bench 3 | Bench | Semenyo | MID | 4 | 8.0 | 3.42 | 10.36 | 17.11 | 1.00 | 36.8 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.62 | 10.27 | 15.84 | 6.00 | 90.5 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 1.60 -> 5.70
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Rice
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.82
- Actual score: 56.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: M.Salah -> Saka (projected gain 2.41, hit 0)
- Autosub outfielders: Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.21 | 9.23 | 13.96 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.99 | 8.32 | 12.64 | 2.00 | 91.3 | 90.0 |
| XI | Bench | Senesi | DEF | 4 | 5.0 | 3.65 | 10.96 | 17.12 | 0.00 | 92.4 | 0.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.1 | 3.55 | 10.82 | 17.43 | 0.00 | 85.5 | 90.0 |
| XI | XI | Muñoz | DEF | 8 | 5.9 | 3.57 | 10.52 | 15.91 | 14.00 | 85.2 | 90.0 |
| Bench 2 | Bench | Van de Ven | DEF | 18 | 4.8 | 3.31 | 10.43 | 16.53 | 0.00 | 85.8 | 0.0 |
| Bench 3 | Autosub In | Guéhi | DEF | 8 | 5.1 | 3.25 | 9.90 | 15.79 | 14.00 | 82.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.6 | 3.95 | 12.25 | 19.80 | 1.00 | 87.4 | 30.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.71 | 11.36 | 18.66 | 2.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Welbeck | FWD | 6 | 6.6 | 2.93 | 9.30 | 14.32 | 1.00 | 73.4 | 23.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.0 | 4.17 | 12.87 | 21.46 | 3.00 | 87.0 | 82.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.27 | 12.87 | 20.83 | 2.00 | 87.1 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.1 | 4.08 | 12.83 | 20.11 | 6.00 | 83.8 | 29.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 3.78 | 11.22 | 19.56 | 4.00 | 53.8 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.3 | 3.60 | 10.34 | 15.99 | 2.00 | 89.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 5.70 -> 4.20
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Semenyo
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 44.96
- Actual score: 58.00
- Transfer: Welbeck -> Mateta (projected gain 1.62, hit 0)
- Autosub outfielders: Senesi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 8.76 | 13.47 | 3.00 | 91.0 | 90.0 |
| XI | XI | Raya | GK | 1 | 5.9 | 3.00 | 8.33 | 13.23 | 2.00 | 87.7 | 90.0 |
| XI | Bench | Muñoz | DEF | 8 | 6.0 | 4.07 | 12.21 | 19.02 | 0.00 | 92.5 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.74 | 11.12 | 17.13 | 8.00 | 76.1 | 90.0 |
| XI | XI | O'Reilly | DEF | 13 | 5.2 | 3.51 | 9.49 | 14.82 | 6.00 | 81.7 | 90.0 |
| Bench 3 | Autosub In | Senesi | DEF | 4 | 5.0 | 2.35 | 7.46 | 14.01 | 8.00 | 60.5 | 61.0 |
| Bench 4 | Bench | Van de Ven | DEF | 18 | 4.8 | 2.12 | 7.02 | 11.87 | 6.00 | 33.7 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.82 | 11.74 | 19.37 | 2.00 | 76.5 | 65.0 |
| XI | XI | João Pedro | FWD | 7 | 7.4 | 3.92 | 11.49 | 18.08 | 1.00 | 81.7 | 32.0 |
| XI | XI | Thiago | FWD | 5 | 6.7 | 3.40 | 11.07 | 17.79 | 2.00 | 75.1 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.8 | 4.12 | 13.21 | 20.62 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.6 | 4.24 | 12.62 | 20.34 | 8.00 | 85.1 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.0 | 3.33 | 11.83 | 19.97 | 6.00 | 62.4 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.1 | 3.58 | 11.72 | 18.66 | 4.00 | 45.9 | 78.0 |
| Bench 2 | Bench | Anderson | MID | 16 | 5.4 | 3.22 | 10.22 | 16.51 | 4.00 | 83.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 4.20 -> 4.70
- Free transfers: 2 -> 2
- Captain: Mbeumo
- Vice captain: Saka
- Effective captain: Mbeumo
- Chip used: none
- Predicted score: 45.60
- Actual score: 34.00
- Transfer: O'Reilly -> Cash (projected gain 1.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.54 | 9.31 | 14.51 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.20 | 9.15 | 14.24 | 1.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.1 | 3.86 | 12.11 | 19.25 | 1.00 | 92.8 | 90.0 |
| XI | XI | Cash | DEF | 2 | 4.7 | 3.91 | 11.09 | 17.12 | 0.00 | 87.7 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.7 | 3.16 | 10.00 | 16.17 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.1 | 2.86 | 9.43 | 15.11 | 0.00 | 62.6 | 0.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 5.0 | 2.90 | 9.24 | 15.68 | 1.00 | 76.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.8 | 3.65 | 11.38 | 17.91 | 2.00 | 79.8 | 90.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.4 | 3.26 | 10.86 | 18.01 | 2.00 | 71.1 | 80.0 |
| XI | XI | Mateta | FWD | 8 | 8.1 | 3.41 | 10.71 | 17.16 | 2.00 | 55.6 | 62.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.1 | 4.18 | 12.59 | 20.20 | 11.00 | 78.8 | 90.0 |
| Captain | Captain | Mbeumo | MID | 14 | 8.5 | 4.20 | 12.22 | 20.24 | 2.00 | 87.2 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.7 | 3.82 | 11.89 | 19.60 | 6.00 | 85.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.93 | 11.16 | 18.90 | 2.00 | 87.7 | 90.0 |
| XI | XI | Anderson | MID | 16 | 5.4 | 3.73 | 11.11 | 17.08 | 3.00 | 86.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 4.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Saka
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.94
- Actual score: 52.00
- Transfer: Anderson -> Foden (projected gain 7.25, hit 0)
- Autosub outfielders: Van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 10.10 | 15.43 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.84 | 8.18 | 13.46 | 2.00 | 89.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.80 | 11.58 | 17.97 | 1.00 | 89.1 | 90.0 |
| XI | XI | Cash | DEF | 2 | 4.9 | 3.23 | 10.81 | 16.92 | 2.00 | 82.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 5.0 | 3.12 | 9.34 | 15.86 | 4.00 | 78.7 | 90.0 |
| Bench 2 | Autosub In | Van de Ven | DEF | 18 | 4.7 | 3.11 | 9.28 | 15.14 | 0.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 6.0 | 1.65 | 6.68 | 13.95 | 0.00 | 20.2 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.30 | 12.27 | 18.91 | 2.00 | 46.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.12 | 10.78 | 18.01 | 6.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.9 | 2.35 | 8.17 | 14.70 | 2.00 | 56.7 | 76.0 |
| Captain | Captain | Foden | MID | 13 | 8.7 | 5.12 | 15.57 | 24.05 | 3.00 | 86.0 | 90.0 |
| Vice Captain | XI | Saka | MID | 1 | 10.2 | 4.18 | 12.68 | 20.27 | 3.00 | 79.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.27 | 21.46 | 11.00 | 82.5 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.11 | 12.23 | 19.64 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Mbeumo | MID | 14 | 8.3 | 3.72 | 11.29 | 19.47 | 0.00 | 78.8 | 0.0 |

## GW18

- Train rows: 173897
- Bank: 1.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: B.Fernandes
- Effective captain: Foden
- Chip used: none
- Predicted score: 47.69
- Actual score: 47.00
- Transfer: Mbeumo -> B.Fernandes (projected gain 5.86, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.37 | 10.23 | 15.87 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.28 | 12.49 | 11.00 | 88.9 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.87 | 10.96 | 17.59 | 2.00 | 90.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.74 | 10.83 | 17.24 | 2.00 | 89.9 | 90.0 |
| XI | XI | Cash | DEF | 2 | 4.9 | 2.84 | 8.67 | 14.26 | 1.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Van de Ven | DEF | 18 | 4.6 | 2.46 | 7.27 | 12.12 | 11.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.51 | 5.38 | 10.90 | 0.00 | 15.1 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.89 | 11.92 | 18.76 | 5.00 | 83.3 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.40 | 10.28 | 16.31 | 8.00 | 82.0 | 68.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.8 | 2.90 | 8.78 | 14.93 | 2.00 | 70.5 | 90.0 |
| Vice Captain | Bench | B.Fernandes | MID | 14 | 9.3 | 4.38 | 14.57 | 23.91 | 0.00 | 84.0 | 0.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 5.00 | 14.03 | 22.76 | 2.00 | 87.1 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.6 | 4.13 | 12.81 | 20.76 | 9.00 | 87.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 4.16 | 12.30 | 19.13 | 7.00 | 81.3 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.1 | 3.92 | 12.29 | 19.18 | 5.00 | 89.0 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.30 -> 3.70
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 46.20
- Actual score: 44.00
- Transfer: B.Fernandes -> Wilson (projected gain 3.57, hit 0)
- Autosub outfielders: Mateta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.21 | 9.83 | 16.04 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.12 | 8.75 | 13.17 | 2.00 | 92.9 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.35 | 11.35 | 17.06 | 3.00 | 92.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.73 | 10.61 | 15.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.6 | 2.91 | 9.13 | 13.80 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 2.68 | 8.34 | 13.86 | 0.00 | 82.4 | 0.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.9 | 1.66 | 5.05 | 9.38 | 0.00 | 16.5 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.2 | 3.39 | 10.27 | 15.83 | 1.00 | 80.1 | 27.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.42 | 9.82 | 16.11 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Autosub In | Mateta | FWD | 8 | 7.7 | 3.01 | 8.55 | 13.38 | 9.00 | 73.5 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 13.79 | 22.64 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.75 | 19.74 | 5.00 | 94.2 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 4.10 | 12.56 | 20.49 | 6.00 | 81.9 | 82.0 |
| XI | Bench | Rice | MID | 1 | 7.2 | 4.08 | 12.26 | 19.41 | 0.00 | 85.9 | 0.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.95 | 12.07 | 19.32 | 2.00 | 89.1 | 84.0 |

## GW20

- Train rows: 175452
- Bank: 3.70 -> 4.20
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 45.39
- Actual score: 49.00
- Transfer: Rice -> Cherki (projected gain 4.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.10 | 9.31 | 14.46 | 1.00 | 89.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.00 | 8.86 | 14.26 | 1.00 | 91.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.9 | 3.19 | 10.75 | 18.22 | 1.00 | 86.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.33 | 10.34 | 16.71 | 2.00 | 76.3 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.72 | 10.16 | 15.25 | 7.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 1.93 | 5.85 | 10.67 | 5.00 | 38.6 | 89.0 |
| Bench 4 | Bench | Muñoz | DEF | 8 | 5.8 | 1.07 | 4.14 | 7.84 | 0.00 | 16.0 | 0.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.35 | 9.33 | 14.57 | 17.00 | 81.4 | 90.0 |
| XI | XI | Mateta | FWD | 8 | 7.7 | 2.99 | 9.18 | 14.75 | 2.00 | 80.9 | 86.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 2.73 | 8.36 | 13.96 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Foden | MID | 13 | 9.0 | 4.91 | 14.48 | 23.60 | 2.00 | 86.8 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.31 | 13.92 | 21.33 | 1.00 | 73.4 | 90.0 |
| XI | XI | Cherki | MID | 13 | 6.7 | 3.98 | 12.47 | 19.50 | 4.00 | 83.0 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.88 | 11.65 | 18.04 | 4.00 | 79.3 | 23.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.73 | 10.74 | 16.99 | 6.00 | 83.9 | 84.0 |

## GW21

- Train rows: 176242
- Bank: 4.20 -> 4.40
- Free transfers: 2 -> 2
- Captain: Foden
- Vice captain: Semenyo
- Effective captain: Foden
- Chip used: none
- Predicted score: 46.36
- Actual score: 53.00
- Transfer: Muñoz -> Tarkowski (projected gain 3.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.05 | 9.23 | 14.79 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.40 | 12.38 | 3.00 | 90.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.3 | 3.39 | 11.10 | 17.12 | 6.00 | 92.8 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.6 | 3.79 | 10.80 | 16.02 | 4.00 | 90.1 | 90.0 |
| XI | XI | Van de Ven | DEF | 18 | 4.5 | 3.28 | 10.76 | 16.41 | 0.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Senesi | DEF | 4 | 4.8 | 2.67 | 7.64 | 13.17 | 6.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Cash | DEF | 2 | 4.8 | 2.63 | 7.34 | 11.89 | 6.00 | 75.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 6.9 | 4.14 | 11.87 | 18.25 | 12.00 | 91.8 | 81.0 |
| Bench 2 | Bench | João Pedro | FWD | 7 | 7.2 | 2.96 | 9.12 | 14.21 | 1.00 | 71.7 | 15.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 2.98 | 8.56 | 13.72 | 2.00 | 76.9 | 90.0 |
| Captain | Captain | Foden | MID | 13 | 8.9 | 4.84 | 13.56 | 21.71 | 2.00 | 85.6 | 72.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 4.05 | 12.86 | 19.32 | 1.00 | 87.3 | 17.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.7 | 4.26 | 12.49 | 20.29 | 6.00 | 91.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.3 | 3.82 | 11.37 | 18.44 | 3.00 | 66.6 | 77.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.91 | 10.80 | 16.90 | 9.00 | 86.3 | 90.0 |

## GW22

- Train rows: 177037
- Bank: 4.40 -> 2.30
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 44.19
- Actual score: 38.00
- Transfer: Van de Ven -> Gabriel (projected gain 3.53, hit 0)
- Autosub outfielders: Cash.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.23 | 9.59 | 14.80 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.46 | 7.27 | 11.30 | 5.00 | 74.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 6.6 | 4.02 | 12.01 | 17.21 | 8.00 | 77.4 | 90.0 |
| XI | Bench | Guéhi | DEF | 8 | 5.3 | 3.36 | 11.26 | 17.81 | 0.00 | 76.3 | 0.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.62 | 10.71 | 16.70 | 3.00 | 86.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.18 | 9.99 | 15.93 | 8.00 | 90.2 | 90.0 |
| Bench 2 | Autosub In | Cash | DEF | 2 | 4.8 | 2.94 | 7.95 | 12.96 | 2.00 | 79.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.96 | 11.25 | 17.18 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.6 | 2.39 | 7.83 | 13.01 | 2.00 | 51.6 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.2 | 2.03 | 7.32 | 12.00 | 8.00 | 28.9 | 73.0 |
| XI | XI | Foden | MID | 13 | 8.8 | 3.91 | 12.72 | 20.94 | 1.00 | 55.5 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.6 | 4.12 | 12.23 | 20.15 | 2.00 | 90.5 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.47 | 11.42 | 18.60 | 1.00 | 41.7 | 33.0 |
| XI | XI | Cherki | MID | 13 | 6.8 | 3.44 | 10.89 | 16.47 | 1.00 | 59.9 | 45.0 |
| XI | XI | Wilson | MID | 10 | 5.8 | 3.77 | 10.83 | 17.01 | 2.00 | 88.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 2.30 -> 1.90
- Free transfers: 2 -> 2
- Captain: Thiago
- Vice captain: Semenyo
- Effective captain: Thiago
- Chip used: none
- Predicted score: 44.56
- Actual score: 42.00
- Transfer: Cherki -> Bruno G. (projected gain 3.08, hit 0)
- Autosub outfielders: Cash.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.70 | 9.98 | 14.96 | 1.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.21 | 12.60 | 5.00 | 94.6 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.8 | 3.99 | 11.67 | 17.21 | 1.00 | 82.5 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.51 | 11.03 | 17.36 | 3.00 | 88.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.7 | 3.40 | 10.64 | 17.14 | 4.00 | 87.1 | 90.0 |
| Bench 2 | Autosub In | Cash | DEF | 2 | 4.8 | 2.94 | 8.26 | 12.68 | 6.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 8 | 5.3 | 2.49 | 7.95 | 13.73 | 6.00 | 36.8 | 90.0 |
| Captain | Captain | Thiago | FWD | 5 | 7.1 | 4.36 | 11.78 | 17.94 | 2.00 | 91.7 | 90.0 |
| Bench 4 | Bench | João Pedro | FWD | 7 | 7.1 | 2.48 | 8.69 | 13.95 | 12.00 | 60.9 | 84.0 |
| XI | XI | Mateta | FWD | 8 | 7.6 | 3.03 | 8.52 | 13.01 | 2.00 | 78.5 | 84.0 |
| XI | Bench | Bruno G. | MID | 15 | 7.2 | 4.09 | 12.93 | 20.19 | 0.00 | 89.4 | 0.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 7.6 | 4.26 | 12.60 | 20.58 | 8.00 | 87.3 | 90.0 |
| XI | XI | Foden | MID | 13 | 8.7 | 3.22 | 10.77 | 17.85 | 1.00 | 66.6 | 29.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 3.38 | 10.61 | 17.10 | 10.00 | 83.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 10.2 | 3.26 | 10.21 | 16.50 | 2.00 | 31.9 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 1.90 -> 1.50
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Rogers
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 45.82
- Actual score: 59.00
- Transfer: Bruno G. -> Rogers (projected gain 4.08, hit 0)
- Autosub outfielders: Cash.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.24 | 10.04 | 16.21 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.94 | 9.02 | 13.68 | 1.00 | 99.6 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 6.9 | 3.70 | 10.67 | 16.19 | 8.00 | 80.8 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.60 | 10.34 | 15.75 | 8.00 | 91.1 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.40 | 10.12 | 16.30 | 2.00 | 86.4 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.26 | 9.95 | 15.90 | 3.00 | 81.4 | 90.0 |
| Bench 2 | Autosub In | Cash | DEF | 2 | 4.8 | 3.11 | 9.15 | 14.24 | 2.00 | 86.4 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.73 | 12.13 | 18.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.1 | 3.46 | 9.99 | 16.23 | 10.00 | 78.5 | 45.0 |
| Bench 3 | Bench | Mateta | FWD | 8 | 7.5 | 2.85 | 7.97 | 11.35 | 0.00 | 70.2 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.7 | 4.86 | 13.22 | 21.15 | 7.00 | 92.1 | 90.0 |
| Vice Captain | XI | Rogers | MID | 2 | 7.7 | 4.40 | 13.18 | 21.34 | 2.00 | 89.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.0 | 3.70 | 11.11 | 17.36 | 2.00 | 88.7 | 90.0 |
| XI | Bench | Saka | MID | 1 | 10.1 | 3.60 | 10.84 | 17.25 | 0.00 | 48.7 | 0.0 |
| Bench 4 | Bench | Foden | MID | 13 | 8.6 | 2.64 | 9.07 | 15.36 | 1.00 | 61.1 | 2.0 |

## GW25

- Train rows: 179450
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 46.57
- Actual score: 59.00
- Transfer: Foden -> B.Fernandes (projected gain 3.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 3.90 | 10.96 | 16.96 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 3.03 | 8.59 | 13.44 | 1.00 | 93.9 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.0 | 4.30 | 12.73 | 19.80 | 6.00 | 86.3 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.88 | 11.16 | 17.92 | 2.00 | 89.6 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 5.8 | 3.71 | 10.99 | 17.09 | 2.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Cash | DEF | 2 | 4.8 | 3.04 | 9.02 | 14.01 | 2.00 | 81.6 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.27 | 8.99 | 14.85 | 3.00 | 82.0 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.3 | 3.83 | 10.99 | 17.47 | 8.00 | 72.8 | 74.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 3.28 | 10.87 | 17.97 | 5.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Mateta | FWD | 8 | 7.5 | 2.10 | 6.34 | 11.20 | 0.00 | 36.4 | 0.0 |
| Captain | Captain | Semenyo | MID | 4 | 7.8 | 4.39 | 13.49 | 21.15 | 2.00 | 92.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.5 | 3.99 | 12.86 | 19.35 | 10.00 | 79.7 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 4.22 | 12.61 | 20.62 | 10.00 | 87.2 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.42 | 9.69 | 15.33 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Saka | MID | 1 | 10.0 | 2.37 | 7.12 | 12.67 | 0.00 | 22.6 | 0.0 |

## GW26

- Train rows: 180267
- Bank: 0.40 -> 2.80
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: bench_boost
- Predicted score: 62.07
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.71) beats the best remaining Bench Boost opportunity (11.07).
- Transfer: Saka -> Rice (projected gain 3.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.71) beats the best remaining Bench Boost opportunity (11.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.07 | 10.48 | 16.16 | 3.00 | 92.4 | 180.0 |
| Bench 1 | Bench Boost | Dúbravka | GK | 3 | 4.0 | 2.87 | 8.42 | 13.13 | 1.00 | 92.9 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 5.20 | 13.55 | 21.20 | 7.00 | 98.7 | 180.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 4.00 | 11.42 | 17.11 | 7.00 | 74.1 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.39 | 10.35 | 16.32 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Bench Boost | Tarkowski | DEF | 9 | 5.8 | 3.17 | 10.00 | 15.79 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Cash | DEF | 2 | 4.8 | 2.67 | 7.48 | 12.27 | 0.00 | 82.4 | 0.0 |
| XI | XI | João Pedro | FWD | 7 | 7.5 | 3.99 | 11.71 | 18.66 | 10.00 | 54.3 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.92 | 11.47 | 18.89 | 2.00 | 86.3 | 90.0 |
| Bench 4 | Bench Boost | Mateta | FWD | 8 | 7.5 | 1.90 | 5.09 | 9.34 | 0.00 | 23.2 | 0.0 |
| XI | XI | Semenyo | MID | 4 | 7.8 | 4.88 | 13.73 | 21.03 | 14.00 | 90.7 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 5.16 | 13.40 | 21.49 | 14.00 | 94.2 | 180.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.7 | 4.33 | 12.89 | 20.04 | 2.00 | 57.2 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 4.15 | 11.75 | 19.04 | 2.00 | 91.0 | 90.0 |
| XI | XI | Wilson | MID | 10 | 6.1 | 3.19 | 10.26 | 16.07 | 2.00 | 86.7 | 71.0 |

## GW27

- Train rows: 181084
- Bank: 2.80 -> 5.70
- Free transfers: 2 -> 2
- Captain: Gabriel
- Vice captain: Rice
- Effective captain: Gabriel
- Chip used: none
- Predicted score: 55.54
- Actual score: 37.00
- Transfer: Mateta -> Mané (projected gain 2.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 5.9 | 4.09 | 11.45 | 17.10 | 3.00 | 116.2 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.66 | 7.53 | 11.69 | 2.00 | 89.7 | 90.0 |
| Captain | Captain | Gabriel | DEF | 1 | 7.1 | 6.19 | 16.72 | 26.03 | 2.00 | 118.8 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.93 | 11.45 | 18.07 | 2.00 | 95.2 | 90.0 |
| XI | XI | Senesi | DEF | 4 | 4.8 | 3.27 | 9.60 | 15.66 | 5.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Tarkowski | DEF | 9 | 5.8 | 2.68 | 9.03 | 14.86 | 1.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Cash | DEF | 2 | 4.9 | 2.47 | 6.74 | 11.11 | 2.00 | 42.3 | 86.0 |
| XI | XI | João Pedro | FWD | 7 | 7.6 | 4.74 | 12.89 | 19.83 | 7.00 | 85.6 | 79.0 |
| XI | XI | Mané | FWD | 20 | 4.6 | 4.03 | 11.98 | 18.17 | 2.00 | 122.8 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 3.91 | 11.55 | 18.69 | 2.00 | 62.8 | 90.0 |
| Vice Captain | XI | Rice | MID | 1 | 7.5 | 6.15 | 16.88 | 26.72 | 4.00 | 111.6 | 90.0 |
| XI | XI | Semenyo | MID | 4 | 7.9 | 4.97 | 13.74 | 22.58 | 4.00 | 94.0 | 86.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 4.10 | 12.58 | 20.07 | 2.00 | 81.9 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.6 | 3.98 | 11.70 | 18.00 | 2.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Wilson | MID | 10 | 6.0 | 2.88 | 9.20 | 14.79 | 8.00 | 76.6 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 5.70 -> 4.60
- Free transfers: 2 -> 2
- Captain: Rice
- Vice captain: Semenyo
- Effective captain: Rice
- Chip used: none
- Predicted score: 50.98
- Actual score: 78.00
- Transfer: Senesi -> Virgil (projected gain 2.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.48 | 9.47 | 13.93 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.85 | 8.17 | 12.36 | 0.00 | 89.1 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 4.78 | 13.30 | 21.28 | 9.00 | 97.8 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 5.9 | 4.12 | 11.29 | 18.19 | 7.00 | 89.0 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.32 | 10.04 | 16.06 | 6.00 | 90.7 | 90.0 |
| Bench 4 | Bench | Tarkowski | DEF | 9 | 5.7 | 2.65 | 8.01 | 12.65 | 3.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Cash | DEF | 2 | 4.9 | 2.70 | 7.41 | 11.97 | 0.00 | 73.8 | 90.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.20 | 13.59 | 20.92 | 2.00 | 62.6 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.0 | 4.17 | 12.32 | 19.40 | 6.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Mané | FWD | 20 | 4.6 | 3.37 | 9.96 | 14.38 | 2.00 | 96.0 | 90.0 |
| Vice Captain | XI | Semenyo | MID | 4 | 8.0 | 4.99 | 14.81 | 23.19 | 8.00 | 90.4 | 90.0 |
| Captain | Captain | Rice | MID | 1 | 7.6 | 5.12 | 14.32 | 23.37 | 5.00 | 97.6 | 75.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.8 | 4.10 | 11.84 | 18.86 | 13.00 | 82.3 | 90.0 |
| XI | XI | Rogers | MID | 2 | 7.7 | 3.97 | 11.51 | 17.98 | 2.00 | 62.9 | 90.0 |
| XI | XI | Wilson | MID | 10 | 5.9 | 3.62 | 10.92 | 17.14 | 12.00 | 87.6 | 71.0 |

## GW29

- Train rows: 182721
- Bank: 4.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: Gabriel
- Effective captain: Semenyo
- Chip used: none
- Predicted score: 53.33
- Actual score: 90.00
- Transfer: Rogers -> Palmer (projected gain 1.82, hit 0)
- Autosub outfielders: Tarkowski.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.42 | 9.46 | 14.50 | 7.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.47 | 7.04 | 11.26 | 2.00 | 88.3 | 90.0 |
| Vice Captain | XI | Gabriel | DEF | 1 | 7.1 | 4.81 | 14.37 | 22.07 | 11.00 | 104.5 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.0 | 4.32 | 12.26 | 19.31 | 1.00 | 89.7 | 90.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.88 | 11.20 | 16.55 | 1.00 | 90.8 | 90.0 |
| Bench 2 | Autosub In | Tarkowski | DEF | 9 | 5.7 | 3.26 | 9.38 | 14.31 | 15.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Cash | DEF | 2 | 4.9 | 2.59 | 7.12 | 11.94 | -1.00 | 75.9 | 45.0 |
| XI | XI | João Pedro | FWD | 7 | 7.7 | 4.27 | 12.30 | 19.73 | 19.00 | 84.9 | 84.0 |
| XI | XI | Thiago | FWD | 5 | 7.1 | 3.97 | 11.80 | 18.23 | 2.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Mané | FWD | 20 | 4.6 | 3.19 | 9.38 | 14.69 | 2.00 | 92.4 | 69.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.1 | 5.93 | 15.91 | 24.14 | 7.00 | 100.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.6 | 4.35 | 13.38 | 21.00 | 3.00 | 80.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 14 | 9.9 | 4.75 | 13.34 | 21.18 | 8.00 | 90.5 | 90.0 |
| XI | XI | Palmer | MID | 7 | 10.6 | 3.85 | 12.34 | 20.36 | 9.00 | 76.0 | 84.0 |
| XI | Bench | Wilson | MID | 10 | 5.9 | 3.87 | 10.80 | 16.91 | 0.00 | 84.0 | 0.0 |

## GW30

- Train rows: 183541
- Bank: 1.70 -> 2.00
- Free transfers: 2 -> 2
- Captain: Semenyo
- Vice captain: João Pedro
- Effective captain: Semenyo
- Chip used: triple_captain
- Predicted score: 59.36
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Wilson -> Summerville (projected gain 1.36, hit 0)
- Chip used: Triple Captain on Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (5.95) beats the best remaining Triple Captain opportunity (0.00).
- Autosub outfielders: Mané.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.74 | 10.32 | 16.02 | 7.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Dúbravka | GK | 3 | 4.0 | 2.90 | 8.15 | 12.22 | 6.00 | 88.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 7.1 | 4.16 | 12.52 | 19.26 | 9.00 | 96.3 | 90.0 |
| XI | XI | Virgil | DEF | 12 | 6.1 | 4.03 | 12.33 | 18.07 | 2.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Tarkowski | DEF | 9 | 5.7 | 3.04 | 10.03 | 15.26 | 0.00 | 88.8 | 0.0 |
| XI | XI | Guéhi | DEF | 8 | 5.2 | 3.56 | 9.79 | 14.87 | 2.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Cash | DEF | 2 | 4.8 | 2.31 | 7.22 | 11.63 | 0.00 | 62.8 | 0.0 |
| Vice Captain | XI | João Pedro | FWD | 7 | 7.6 | 5.88 | 14.86 | 23.52 | 2.00 | 94.1 | 90.0 |
| XI | XI | Thiago | FWD | 5 | 7.2 | 4.00 | 11.39 | 17.33 | 6.00 | 87.3 | 90.0 |
| Bench 3 | Autosub In | Mané | FWD | 20 | 4.6 | 2.34 | 7.10 | 11.76 | 1.00 | 64.4 | 45.0 |
| Captain | Captain | Semenyo | MID | 4 | 8.2 | 5.95 | 15.55 | 23.96 | 2.00 | 102.0 | 74.0 |
| XI | XI | B.Fernandes | MID | 14 | 10.0 | 5.13 | 14.44 | 22.97 | 10.00 | 94.1 | 90.0 |
| XI | XI | Palmer | MID | 7 | 10.6 | 3.82 | 12.45 | 19.44 | 2.00 | 52.0 | 90.0 |
| XI | Bench | Summerville | MID | 19 | 5.7 | 3.56 | 11.35 | 17.29 | 0.00 | 87.2 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.5 | 3.64 | 11.23 | 18.13 | 3.00 | 83.0 | 90.0 |