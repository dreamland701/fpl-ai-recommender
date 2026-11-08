# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 299.37
- Total actual points: 294.00
- Average predicted points: 74.84
- Average actual points: 73.50
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
- Predicted score: 60.28
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.18 | 8.86 | 14.35 | 3.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.78 | 4.88 | 7.18 | 1.00 | 53.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.11 | 11.46 | 18.64 | 5.00 | 84.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.69 | 10.79 | 17.21 | 5.00 | 79.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.56 | 10.06 | 16.23 | 6.00 | 79.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.51 | 6.81 | 10.76 | 2.00 | 68.8 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.07 | 6.46 | 10.57 | 1.00 | 75.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.05 | 17.97 | 31.27 | 8.00 | 70.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.40 | 13.41 | 20.05 | 2.00 | 72.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.57 | 12.17 | 20.14 | 2.00 | 75.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.16 | 17.69 | 27.09 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.57 | 16.41 | 26.56 | 5.00 | 87.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.72 | 16.36 | 26.76 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.10 | 14.44 | 23.69 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 3.02 | 8.70 | 14.51 | 2.00 | 82.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.54
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 6.84, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.99 | 8.68 | 13.97 | 9.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.01 | 5.32 | 7.92 | 0.00 | 58.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.60 | 12.32 | 19.61 | 1.00 | 88.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.14 | 11.39 | 17.93 | 5.00 | 81.0 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.33 | 10.81 | 18.26 | 0.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.65 | 7.23 | 11.44 | 2.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.60 | 7.01 | 10.88 | 1.00 | 69.4 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.91 | 21.60 | 35.88 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.26 | 13.13 | 19.87 | 12.00 | 74.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.06 | 11.55 | 18.82 | 7.00 | 72.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.74 | 15.99 | 24.49 | 26.00 | 83.8 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.94 | 15.17 | 24.86 | 1.00 | 82.1 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.97 | 14.04 | 22.11 | 2.00 | 74.4 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.70 | 11.36 | 19.61 | 0.00 | 46.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.35 | 8.15 | 13.55 | 7.00 | 80.5 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Eberechi Eze
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 100.95
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.91) beats the best remaining Triple Captain opportunity (14.25).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Eberechi Eze (projected gain 6.68, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (14.91) beats the best remaining Triple Captain opportunity (14.25).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Jan Paul van Hecke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.08 | 9.06 | 14.93 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.75 | 2.55 | 4.00 | 0.00 | 30.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 9.69 | 14.21 | 22.21 | 14.00 | 180.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.99 | 12.44 | 19.25 | 26.00 | 158.0 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.14 | 12.40 | 18.74 | 12.00 | 169.4 | 180.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.63 | 10.60 | 2.00 | 62.9 | 90.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.10 | 6.63 | 10.80 | 0.00 | 76.1 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.30 | 18.98 | 31.51 | 0.00 | 74.8 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.72 | 16.83 | 27.28 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.97 | 14.59 | 23.10 | 2.00 | 82.5 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 10.47 | 16.19 | 23.10 | 14.00 | 172.6 | 162.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.87 | 16.03 | 25.17 | 0.00 | 87.4 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 10.24 | 13.96 | 22.83 | 3.00 | 173.0 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.12 | 22.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.02 | 8.40 | 13.59 | 2.00 | 80.8 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 78.60
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.63) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Phil Foden (projected gain 4.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.63) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.16 | 8.63 | 14.23 | 3.00 | 83.9 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.67 | 1.83 | 3.21 | 1.00 | 22.5 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.17 | 14.82 | 23.59 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.91 | 22.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.64 | 13.15 | 20.48 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.43 | 6.73 | 10.75 | 0.00 | 77.7 | 0.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.37 | 10.32 | 0.00 | 69.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.97 | 17.14 | 27.06 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.95 | 15.73 | 26.96 | 5.00 | 37.5 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.00 | 13.79 | 21.63 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.29 | 15.13 | 26.64 | 8.00 | 136.9 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 4.98 | 14.45 | 23.36 | 0.00 | 73.9 | 0.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.40 | 13.11 | 21.51 | 9.00 | 116.8 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.64 | 12.97 | 20.28 | 5.00 | 78.2 | 78.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.6 | 2.93 | 8.22 | 13.43 | 2.00 | 85.6 | 77.0 |