# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 305.11
- Total actual points: 309.00
- Average predicted points: 76.28
- Average actual points: 77.25
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
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.09
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.13 | 8.79 | 14.32 | 3.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.93 | 6.57 | 9.66 | 1.00 | 68.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 11.37 | 18.60 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.63 | 10.70 | 17.17 | 5.00 | 77.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.50 | 9.96 | 16.18 | 6.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.71 | 10.69 | 2.00 | 66.6 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.00 | 6.35 | 10.50 | 1.00 | 73.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.26 | 19.51 | 33.20 | 8.00 | 84.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.37 | 13.42 | 20.10 | 2.00 | 71.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.50 | 12.06 | 20.11 | 2.00 | 73.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 7.09 | 17.64 | 27.09 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.55 | 16.41 | 26.63 | 5.00 | 86.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.68 | 16.31 | 26.79 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.07 | 14.41 | 23.72 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.95 | 8.61 | 14.46 | 2.00 | 80.7 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.88
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 6.33, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.62 | 13.96 | 9.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.99 | 5.30 | 7.94 | 0.00 | 58.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.58 | 12.30 | 19.65 | 1.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.21 | 11.93 | 19.60 | 0.00 | 80.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.35 | 17.95 | 5.00 | 80.1 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.60 | 7.17 | 11.42 | 2.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.90 | 10.80 | 1.00 | 67.2 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.56 | 20.89 | 34.44 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.24 | 13.15 | 19.95 | 12.00 | 73.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.02 | 11.49 | 18.84 | 7.00 | 71.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.72 | 16.02 | 24.58 | 26.00 | 83.3 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.91 | 15.13 | 24.91 | 1.00 | 81.0 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.22 | 14.46 | 22.60 | 2.00 | 82.9 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.82 | 11.12 | 18.90 | 0.00 | 48.9 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.29 | 8.06 | 13.51 | 7.00 | 78.7 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Eberechi Eze
- Vice captain: Dominic Solanke
- Effective captain: Eberechi Eze
- Chip used: triple_captain
- Predicted score: 106.33
- Actual score: 113.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.52) beats the best remaining Triple Captain opportunity (14.31).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Eberechi Eze (projected gain 9.06, hit 0)
- Chip used: Triple Captain on Eberechi Eze. Optimizer chose Triple Captain here because the current estimated captain upside (16.52) beats the best remaining Triple Captain opportunity (14.31).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Jan Paul van Hecke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.02 | 9.00 | 14.91 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.66 | 2.43 | 3.91 | 0.00 | 27.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.66 | 13.18 | 20.55 | 14.00 | 175.3 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.92 | 12.40 | 19.26 | 26.00 | 156.1 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.07 | 12.37 | 18.76 | 12.00 | 167.5 | 180.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.17 | 6.73 | 10.87 | 0.00 | 77.7 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.27 | 6.53 | 10.54 | 2.00 | 60.4 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.47 | 18.78 | 30.80 | 0.00 | 78.5 | 0.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 11.51 | 15.45 | 27.24 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.08 | 14.77 | 23.28 | 2.00 | 85.0 | 90.0 |
| Captain | Captain | Eberechi Eze | MID | 8 | 6.1 | 12.33 | 17.51 | 24.45 | 14.00 | 180.0 | 162.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.89 | 16.10 | 25.33 | 0.00 | 87.0 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 10.63 | 14.89 | 23.20 | 3.00 | 164.7 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.26 | 22.97 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.09 | 8.50 | 13.66 | 2.00 | 82.2 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 78.81
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.31) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Phil Foden (projected gain 4.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.31) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.11 | 8.57 | 14.21 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.55 | 1.66 | 3.05 | 1.00 | 19.1 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.18 | 14.87 | 23.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.92 | 13.94 | 22.12 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.64 | 13.18 | 20.56 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.67 | 10.71 | 0.00 | 76.4 | 0.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.08 | 6.25 | 10.23 | 0.00 | 67.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.91 | 17.06 | 27.06 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.08 | 15.48 | 26.22 | 5.00 | 41.0 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.02 | 13.84 | 21.74 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.63 | 15.82 | 26.75 | 8.00 | 137.3 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 4.89 | 14.33 | 23.29 | 0.00 | 71.4 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.66 | 13.01 | 20.38 | 5.00 | 78.8 | 78.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.26 | 13.00 | 21.44 | 9.00 | 112.3 | 180.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.6 | 2.87 | 8.13 | 13.36 | 2.00 | 84.0 | 77.0 |