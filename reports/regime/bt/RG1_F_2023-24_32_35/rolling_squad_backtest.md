# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 281.88
- Total actual points: 306.00
- Average predicted points: 70.47
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.54
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.12 | 8.74 | 14.20 | 3.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.75 | 4.89 | 7.26 | 1.00 | 48.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.00 | 11.19 | 18.31 | 5.00 | 84.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.64 | 10.74 | 17.25 | 5.00 | 78.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.46 | 9.83 | 15.98 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.45 | 6.77 | 10.82 | 2.00 | 67.2 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.99 | 6.30 | 10.43 | 1.00 | 73.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.98 | 17.60 | 30.68 | 8.00 | 68.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.39 | 13.42 | 20.16 | 2.00 | 72.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.47 | 11.96 | 19.93 | 2.00 | 72.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.10 | 17.55 | 27.02 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.58 | 16.51 | 26.86 | 5.00 | 87.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.66 | 16.23 | 26.64 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.04 | 14.28 | 23.50 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.88 | 8.36 | 14.04 | 2.00 | 79.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.77
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.49, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.92 | 8.55 | 13.83 | 9.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.00 | 5.34 | 7.99 | 0.00 | 55.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.53 | 12.13 | 19.37 | 1.00 | 89.2 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.11 | 11.36 | 17.99 | 5.00 | 81.1 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.24 | 11.31 | 17.61 | 0.00 | 83.7 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.60 | 7.14 | 11.38 | 2.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.54 | 6.98 | 10.96 | 1.00 | 67.9 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.57 | 20.89 | 34.51 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.22 | 13.06 | 19.84 | 12.00 | 73.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.96 | 11.29 | 18.52 | 7.00 | 70.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.72 | 15.96 | 24.52 | 26.00 | 84.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.89 | 15.11 | 24.96 | 1.00 | 81.0 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.28 | 14.65 | 22.99 | 2.00 | 83.6 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.74 | 10.87 | 18.51 | 0.00 | 48.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.22 | 7.83 | 13.11 | 7.00 | 77.6 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.40
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (10.53).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.55) beats the best remaining Bench Boost opportunity (10.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.99 | 8.88 | 14.70 | 2.00 | 83.9 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.68 | 2.49 | 4.01 | 0.00 | 25.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.58 | 13.04 | 20.32 | 14.00 | 177.5 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.96 | 12.44 | 19.34 | 26.00 | 158.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.06 | 12.34 | 18.74 | 12.00 | 169.9 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.16 | 6.70 | 10.82 | 0.00 | 78.5 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.28 | 6.58 | 10.65 | 2.00 | 60.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.43 | 18.71 | 30.78 | 0.00 | 78.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.06 | 14.67 | 23.14 | 2.00 | 84.5 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.54 | 14.45 | 22.67 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 15.82 | 24.89 | 0.00 | 86.9 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.41 | 14.57 | 23.54 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.89 | 13.88 | 21.13 | 3.00 | 132.7 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.30 | 23.08 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.02 | 8.27 | 13.26 | 2.00 | 81.4 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.16
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.54) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.13, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.54) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.74 | 10.63 | 17.08 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.57 | 1.72 | 3.13 | 1.00 | 16.3 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.16 | 14.78 | 23.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.85 | 13.68 | 21.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.60 | 13.01 | 20.29 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.64 | 10.67 | 0.00 | 77.4 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.08 | 6.27 | 10.28 | 0.00 | 67.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.99 | 17.21 | 27.28 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.02 | 15.38 | 26.16 | 5.00 | 40.8 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.93 | 13.52 | 21.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.88 | 17.54 | 28.26 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.34 | 15.07 | 24.31 | 8.00 | 115.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.68 | 13.15 | 20.71 | 5.00 | 78.4 | 78.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.30 | 13.09 | 21.64 | 9.00 | 113.9 | 180.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.80 | 7.89 | 12.93 | 2.00 | 83.2 | 77.0 |