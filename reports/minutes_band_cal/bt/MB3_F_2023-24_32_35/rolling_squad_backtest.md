# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 284.51
- Total actual points: 306.00
- Average predicted points: 71.13
- Average actual points: 76.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.95
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.13 | 8.77 | 14.30 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.92 | 5.24 | 7.82 | 1.00 | 56.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 11.35 | 18.59 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.66 | 10.69 | 17.01 | 5.00 | 79.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.53 | 9.93 | 16.02 | 6.00 | 79.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.90 | 11.08 | 2.00 | 70.7 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.35 | 6.43 | 10.51 | 2.00 | 74.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.07 | 17.76 | 31.02 | 8.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.43 | 13.43 | 20.05 | 2.00 | 74.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.52 | 12.03 | 19.94 | 2.00 | 75.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.14 | 17.69 | 27.27 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.54 | 16.37 | 26.58 | 5.00 | 86.3 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 16.32 | 26.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.07 | 14.40 | 23.72 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.93 | 8.56 | 14.40 | 2.00 | 80.3 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.23
- Actual score: 84.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.05, hit 0)
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.92 | 8.57 | 13.90 | 9.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.18 | 5.71 | 8.58 | 0.00 | 62.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.57 | 12.27 | 19.63 | 1.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.25 | 11.34 | 17.66 | 0.00 | 82.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.13 | 11.31 | 17.77 | 5.00 | 81.9 | 66.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.62 | 7.08 | 11.17 | 1.00 | 71.4 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.41 | 5.24 | 8.91 | 0.00 | 66.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.57 | 20.88 | 34.47 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.27 | 13.11 | 19.82 | 12.00 | 75.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.08 | 11.59 | 19.10 | 7.00 | 75.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.76 | 16.08 | 24.73 | 26.00 | 83.9 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.87 | 15.03 | 24.78 | 1.00 | 80.1 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.24 | 14.49 | 22.69 | 2.00 | 83.2 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.99 | 11.45 | 19.45 | 0.00 | 53.2 | 0.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.30 | 7.98 | 13.28 | 7.00 | 80.3 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.23
- Actual score: 98.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.79) beats the best remaining Bench Boost opportunity (9.55).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.79) beats the best remaining Bench Boost opportunity (9.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.00 | 8.93 | 14.83 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.60 | 2.31 | 3.78 | 0.00 | 26.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.66 | 13.17 | 20.54 | 14.00 | 175.2 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.00 | 12.37 | 19.12 | 26.00 | 160.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.08 | 12.37 | 18.78 | 12.00 | 167.6 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.71 | 10.86 | 2.00 | 64.5 | 90.0 |
| Bench 3 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.40 | 4.02 | 6.88 | 1.00 | 42.1 | 34.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.44 | 18.60 | 30.48 | 0.00 | 79.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.07 | 14.73 | 23.27 | 2.00 | 84.7 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.66 | 14.68 | 23.09 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.85 | 16.02 | 25.25 | 0.00 | 86.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.41 | 14.54 | 23.48 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.98 | 13.87 | 21.08 | 3.00 | 140.3 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.18 | 22.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.07 | 8.46 | 13.62 | 2.00 | 82.0 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 80.09
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.05) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.16, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (12.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.75 | 10.68 | 17.19 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.49 | 1.54 | 2.92 | 1.00 | 18.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.17 | 14.84 | 23.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.90 | 13.89 | 22.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.63 | 13.15 | 20.52 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.17 | 6.45 | 10.58 | 0.00 | 71.5 | 0.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.93 | 3.28 | 5.82 | 0.00 | 34.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.99 | 17.22 | 27.30 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.95 | 15.21 | 25.92 | 5.00 | 38.7 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.97 | 13.71 | 21.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.86 | 17.47 | 28.13 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.85 | 15.69 | 25.29 | 8.00 | 124.4 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.65 | 13.42 | 22.07 | 9.00 | 122.1 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.64 | 12.87 | 20.06 | 5.00 | 79.7 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.86 | 8.11 | 13.34 | 2.00 | 83.9 | 77.0 |