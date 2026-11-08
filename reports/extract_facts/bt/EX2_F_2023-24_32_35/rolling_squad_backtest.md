# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 305.36
- Total actual points: 306.00
- Average predicted points: 76.34
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
- Predicted score: 61.35
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.18 | 8.88 | 14.38 | 3.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.94 | 6.59 | 9.65 | 1.00 | 68.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.12 | 11.49 | 18.69 | 5.00 | 84.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.70 | 10.82 | 17.26 | 5.00 | 79.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.57 | 10.08 | 16.28 | 6.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.51 | 6.83 | 10.79 | 2.00 | 68.8 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.07 | 6.47 | 10.59 | 1.00 | 75.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 7.06 | 19.20 | 32.83 | 8.00 | 77.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.41 | 13.46 | 20.11 | 2.00 | 73.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.57 | 12.16 | 20.16 | 2.00 | 75.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.15 | 17.70 | 27.09 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.59 | 16.46 | 26.65 | 5.00 | 87.3 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.75 | 16.40 | 26.86 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.11 | 14.48 | 23.76 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 3.03 | 8.72 | 14.54 | 2.00 | 82.7 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.47
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 6.84, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.99 | 8.70 | 14.01 | 9.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.02 | 5.35 | 7.95 | 0.00 | 58.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.61 | 12.35 | 19.67 | 1.00 | 89.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.31 | 11.96 | 19.43 | 0.00 | 82.2 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.15 | 11.42 | 17.98 | 5.00 | 81.1 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.64 | 7.23 | 11.46 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.61 | 7.03 | 10.90 | 1.00 | 69.5 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.35 | 20.56 | 34.05 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.26 | 13.17 | 19.92 | 12.00 | 74.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.07 | 11.56 | 18.87 | 7.00 | 73.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.74 | 16.03 | 24.55 | 26.00 | 83.8 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.96 | 15.20 | 24.94 | 1.00 | 82.2 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.97 | 14.07 | 22.15 | 2.00 | 74.6 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.72 | 11.35 | 19.65 | 0.00 | 46.8 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.36 | 8.17 | 13.59 | 7.00 | 80.7 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Eberechi Eze
- Vice captain: Dominic Solanke
- Effective captain: Eberechi Eze
- Chip used: triple_captain
- Predicted score: 106.49
- Actual score: 113.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.55) beats the best remaining Triple Captain opportunity (14.36).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Eberechi Eze (projected gain 8.67, hit 0)
- Chip used: Triple Captain on Eberechi Eze. Optimizer chose Triple Captain here because the current estimated captain upside (16.55) beats the best remaining Triple Captain opportunity (14.36).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Jan Paul van Hecke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.09 | 9.09 | 14.97 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.76 | 2.57 | 4.03 | 0.00 | 30.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.75 | 13.25 | 20.59 | 14.00 | 177.6 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.01 | 12.47 | 19.30 | 26.00 | 158.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.15 | 12.43 | 18.78 | 12.00 | 169.7 | 180.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.66 | 10.64 | 2.00 | 63.0 | 90.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.10 | 6.64 | 10.81 | 0.00 | 76.3 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.31 | 18.96 | 31.53 | 0.00 | 75.0 | 0.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 11.59 | 15.46 | 27.17 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.99 | 14.61 | 23.15 | 2.00 | 82.9 | 90.0 |
| Captain | Captain | Eberechi Eze | MID | 8 | 6.1 | 12.36 | 17.45 | 24.30 | 14.00 | 180.0 | 162.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.92 | 16.11 | 25.31 | 0.00 | 87.8 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 10.58 | 14.85 | 23.14 | 3.00 | 163.1 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.14 | 22.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.03 | 8.41 | 13.61 | 2.00 | 80.9 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 79.05
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Phil Foden (projected gain 4.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.17 | 8.66 | 14.27 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.67 | 1.84 | 3.22 | 1.00 | 22.6 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.18 | 14.88 | 23.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.92 | 13.95 | 22.11 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.65 | 13.18 | 20.53 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.43 | 6.74 | 10.77 | 0.00 | 77.7 | 0.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.37 | 10.34 | 0.00 | 69.7 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.92 | 17.06 | 27.01 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.95 | 15.71 | 26.97 | 5.00 | 37.9 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.01 | 13.81 | 21.68 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.49 | 16.04 | 27.46 | 8.00 | 134.7 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 4.98 | 14.48 | 23.44 | 0.00 | 74.1 | 0.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.43 | 13.14 | 21.56 | 9.00 | 117.2 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.65 | 12.97 | 20.32 | 5.00 | 78.3 | 78.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.6 | 2.93 | 8.23 | 13.45 | 2.00 | 85.7 | 77.0 |