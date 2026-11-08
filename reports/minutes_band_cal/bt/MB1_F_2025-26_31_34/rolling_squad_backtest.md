# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 264.45
- Total actual points: 227.00
- Average predicted points: 66.11
- Average actual points: 56.75
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
- Predicted score: 61.00
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.36 | 9.09 | 14.49 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.12 | 0.00 | 1.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.14 | 15.04 | 23.95 | 3.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 13.19 | 22.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.88 | 12.49 | 19.13 | 0.00 | 83.1 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.41 | 9.64 | 15.92 | -1.00 | 79.8 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.14 | 8.99 | 14.31 | 1.00 | 80.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.79 | 16.81 | 27.23 | 2.00 | 83.1 | 77.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.2 | 4.77 | 14.96 | 24.62 | 1.00 | 72.9 | 7.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.93 | 13.92 | 23.05 | 2.00 | 83.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.78 | 20.34 | 33.05 | 13.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.20 | 15.81 | 26.17 | 2.00 | 80.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 14.19 | 22.48 | 3.00 | 83.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.26 | 13.85 | 21.37 | 10.00 | 83.1 | 88.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 4.7 | 3.82 | 10.20 | 15.91 | 3.00 | 79.5 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.05
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.82) beats the best remaining Bench Boost opportunity (18.22).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.82) beats the best remaining Bench Boost opportunity (18.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.49 | 7.52 | 12.56 | 0.00 | 80.5 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.23 | 0.26 | 0.37 | 0.00 | 2.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.09 | 11.93 | 20.58 | 4.00 | 65.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.83 | 11.27 | 18.65 | 9.00 | 79.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.04 | 10.53 | 16.14 | 5.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.16 | 9.69 | 15.61 | 3.00 | 83.1 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.34 | 8.71 | 14.21 | 6.00 | 80.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.82 | 15.12 | 25.29 | 2.00 | 79.8 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.65 | 12.62 | 20.88 | 14.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.2 | 3.11 | 10.26 | 18.10 | 0.00 | 36.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.58 | 19.84 | 32.39 | 4.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.65 | 14.20 | 23.87 | 4.00 | 79.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.50 | 13.23 | 21.18 | 5.00 | 81.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.67 | 10.92 | 17.58 | 3.00 | 71.0 | 70.0 |
| Bench 2 | Bench Boost | Anton Stach | MID | 11 | 4.7 | 3.32 | 9.71 | 15.47 | 0.00 | 75.1 | 0.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 4.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 92.76
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.93) beats the best remaining Triple Captain opportunity (6.01).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Hugo Ekitiké -> Dominic Calvert-Lewin (projected gain 7.21, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (15.93) beats the best remaining Triple Captain opportunity (6.01).
- Autosub: El Hadji Malick Diouf replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.89 | 5.64 | 9.62 | 2.00 | 48.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.01 | 0.00 | 2.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.52 | 13.06 | 19.18 | 12.00 | 158.5 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.85 | 12.02 | 18.40 | 5.00 | 168.0 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.74 | 11.42 | 19.90 | 0.00 | 71.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.31 | 19.13 | 8.00 | 81.5 | 90.0 |
| Bench 4 | Autosub In | El Hadji Malick Diouf | DEF | 19 | 4.0 | 2.93 | 8.54 | 14.11 | 5.00 | 80.7 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 9.58 | 15.91 | 25.61 | 0.00 | 160.0 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 8.89 | 13.42 | 19.38 | 8.00 | 160.1 | 180.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.80 | 11.70 | 19.70 | 2.00 | 79.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.12 | 17.59 | 29.83 | 6.00 | 83.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 11.33 | 17.55 | 27.78 | 2.00 | 166.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.56 | 13.26 | 21.26 | 5.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.18 | 10.32 | 17.46 | 0.00 | 65.1 | 0.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 4.7 | 3.73 | 6.86 | 11.21 | 0.00 | 63.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 4.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.63
- Actual score: 51.00
- Transfer: Anton Stach -> Morgan Gibbs-White (projected gain 12.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.57 | 7.52 | 12.26 | 3.00 | 73.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.11 | 0.18 | 0.31 | 0.00 | 3.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.69 | 15.96 | 25.27 | 4.00 | 83.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.23 | 14.01 | 22.89 | 8.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 12.04 | 19.95 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 10.49 | 17.92 | 0.00 | 0.0 | 0.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.43 | 9.39 | 14.87 | 2.00 | 82.1 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 5.80 | 16.07 | 25.56 | 10.00 | 83.2 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.62 | 19.34 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 0.00 | 10.41 | 16.80 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.84 | 19.57 | 32.78 | 5.00 | 83.2 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.21 | 14.93 | 23.99 | 13.00 | 83.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.53 | 12.64 | 20.72 | 1.00 | 83.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 12.39 | 21.74 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.49 | 6.86 | 13.35 | 0.00 | 33.6 | 0.0 |