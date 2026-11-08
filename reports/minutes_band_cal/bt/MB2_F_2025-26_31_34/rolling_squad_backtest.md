# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 267.11
- Total actual points: 213.00
- Average predicted points: 66.78
- Average actual points: 53.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.88
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.27 | 8.94 | 14.26 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.24 | 15.31 | 24.30 | 3.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 13.46 | 23.14 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.98 | 12.76 | 19.47 | 0.00 | 83.4 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.51 | 9.91 | 16.27 | -1.00 | 80.1 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.12 | 8.97 | 14.35 | 1.00 | 79.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.89 | 17.07 | 27.57 | 2.00 | 83.4 | 77.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.2 | 4.76 | 14.94 | 24.60 | 1.00 | 72.9 | 7.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.03 | 14.19 | 23.40 | 2.00 | 83.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.87 | 20.61 | 33.39 | 13.00 | 83.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.30 | 16.07 | 26.51 | 2.00 | 80.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.79 | 14.46 | 22.83 | 3.00 | 83.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.36 | 14.12 | 21.71 | 10.00 | 83.4 | 88.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 4.7 | 3.79 | 10.18 | 15.95 | 3.00 | 78.4 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.18
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (18.39).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (18.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.47 | 7.51 | 12.59 | 0.00 | 79.4 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.10 | 0.22 | 0.00 | 3.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.07 | 11.91 | 20.55 | 4.00 | 65.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.25 | 18.68 | 9.00 | 77.9 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.13 | 10.81 | 16.48 | 5.00 | 82.2 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.26 | 9.96 | 15.95 | 3.00 | 83.4 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.31 | 8.70 | 14.24 | 6.00 | 79.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.80 | 15.11 | 25.33 | 2.00 | 78.7 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.74 | 12.90 | 21.22 | 14.00 | 83.4 | 90.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.2 | 3.14 | 10.32 | 18.17 | 0.00 | 36.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.67 | 20.12 | 32.73 | 4.00 | 83.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.74 | 14.48 | 24.21 | 4.00 | 79.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.42 | 13.07 | 20.96 | 5.00 | 79.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.65 | 10.89 | 17.56 | 3.00 | 71.0 | 70.0 |
| Bench 2 | Bench Boost | Anton Stach | MID | 11 | 4.7 | 3.30 | 9.70 | 15.50 | 0.00 | 74.0 | 0.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 92.94
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.12) beats the best remaining Triple Captain opportunity (6.13).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Anton Stach -> Alex Scott (projected gain 6.38, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.12) beats the best remaining Triple Captain opportunity (6.13).
- Autosub: El Hadji Malick Diouf replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.93 | 5.78 | 9.83 | 2.00 | 49.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 1.31 | 1.58 | 0.00 | 5.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.37 | 12.92 | 18.98 | 12.00 | 156.3 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.70 | 11.88 | 18.20 | 5.00 | 165.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.90 | 11.59 | 19.46 | 8.00 | 81.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.72 | 11.38 | 19.86 | 0.00 | 72.0 | 90.0 |
| Bench 3 | Autosub In | El Hadji Malick Diouf | DEF | 19 | 4.0 | 2.90 | 8.52 | 14.14 | 5.00 | 79.6 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 9.77 | 16.18 | 25.94 | 0.00 | 160.6 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.90 | 11.97 | 20.03 | 2.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Hugo Ekitiké | FWD | 12 | 9.2 | 1.18 | 4.93 | 11.02 | 0.00 | 8.8 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.21 | 17.86 | 30.16 | 6.00 | 83.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 11.52 | 17.83 | 28.11 | 2.00 | 166.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.49 | 13.12 | 21.05 | 5.00 | 80.8 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 8.41 | 12.81 | 19.68 | 5.00 | 166.9 | 180.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.16 | 10.28 | 17.41 | 0.00 | 65.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.11
- Actual score: 40.00
- Transfer: Hugo Ekitiké -> Ollie Watkins (projected gain 11.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.55 | 7.50 | 12.29 | 3.00 | 72.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.79 | 16.22 | 25.60 | 4.00 | 83.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 14.28 | 23.22 | 8.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 12.31 | 20.29 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 10.76 | 18.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.34 | 9.25 | 14.67 | 2.00 | 81.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.19 | 16.83 | 25.82 | 2.00 | 83.4 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 5.90 | 16.33 | 25.90 | 10.00 | 83.4 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.58 | 19.29 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.94 | 19.84 | 33.12 | 5.00 | 83.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.63 | 12.91 | 21.06 | 1.00 | 83.4 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 12.66 | 22.08 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 12.44 | 20.37 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.52 | 6.92 | 13.41 | 0.00 | 34.0 | 0.0 |