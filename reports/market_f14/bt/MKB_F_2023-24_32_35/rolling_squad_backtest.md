# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 282.53
- Total actual points: 300.00
- Average predicted points: 70.63
- Average actual points: 75.00
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
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.06
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 8.64 | 14.12 | 3.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.82 | 5.04 | 7.43 | 1.00 | 50.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.03 | 11.36 | 18.59 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.55 | 10.53 | 16.89 | 5.00 | 75.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.46 | 9.89 | 16.08 | 6.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.35 | 6.43 | 10.32 | 2.00 | 67.9 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.96 | 6.28 | 10.41 | 1.00 | 71.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.68 | 16.95 | 29.67 | 8.00 | 61.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.32 | 13.24 | 19.90 | 2.00 | 70.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.32 | 11.65 | 19.56 | 2.00 | 71.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.26 | 17.98 | 27.71 | 5.00 | 90.0 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.75 | 16.47 | 27.00 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.45 | 16.18 | 26.30 | 5.00 | 85.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.93 | 14.04 | 23.20 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.85 | 8.30 | 14.06 | 2.00 | 80.7 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.39
- Actual score: 85.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.12, hit 0)
- Autosub: Jan Paul van Hecke replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.88 | 8.50 | 13.80 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.06 | 5.55 | 8.35 | 0.00 | 56.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.60 | 12.40 | 19.79 | 1.00 | 87.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.29 | 11.46 | 17.82 | 0.00 | 82.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.36 | 17.95 | 5.00 | 78.7 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.66 | 7.39 | 11.72 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.39 | 6.54 | 10.28 | 1.00 | 68.7 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.50 | 20.86 | 34.51 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.13 | 12.90 | 19.66 | 12.00 | 74.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.84 | 11.08 | 18.27 | 7.00 | 70.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.86 | 16.32 | 25.10 | 26.00 | 86.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.75 | 14.79 | 24.44 | 1.00 | 78.6 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.27 | 14.60 | 22.84 | 2.00 | 81.9 | 65.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.67 | 10.81 | 18.32 | 0.00 | 69.1 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.34 | 7.99 | 13.32 | 7.00 | 78.2 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.50 -> 2.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: William Saliba
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 90.08
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (10.38).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 5.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (10.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.88 | 8.63 | 14.40 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.57 | 2.31 | 3.71 | 0.00 | 24.6 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 9.25 | 13.99 | 21.71 | 14.00 | 176.1 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.70 | 13.22 | 19.99 | 12.00 | 168.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.31 | 12.96 | 20.05 | 26.00 | 152.6 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.21 | 6.81 | 10.97 | 0.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.22 | 6.40 | 10.36 | 2.00 | 60.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.22 | 18.29 | 30.12 | 0.00 | 75.0 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.56 | 14.62 | 23.05 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.92 | 14.37 | 22.71 | 2.00 | 83.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.86 | 15.96 | 25.14 | 0.00 | 86.2 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 9.14 | 14.26 | 21.55 | 3.00 | 130.7 | 163.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.1 | 8.70 | 13.21 | 19.71 | 14.00 | 172.5 | 162.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.74 | 22.19 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.00 | 8.29 | 13.37 | 2.00 | 81.1 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 75.00
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.25) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Stefan Ortega Moreno -> Jordan Pickford (projected gain 2.54, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.25) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Ross Barkley replaced Eberechi Eze.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.81 | 10.78 | 17.35 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.03 | 8.38 | 13.90 | 3.00 | 80.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.20 | 14.92 | 23.78 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.98 | 14.12 | 22.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.72 | 13.39 | 20.89 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.35 | 6.59 | 10.61 | 0.00 | 76.7 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.05 | 6.17 | 10.11 | 0.00 | 67.4 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.02 | 17.30 | 27.43 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.13 | 15.59 | 26.47 | 5.00 | 44.4 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.87 | 13.47 | 21.23 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.05 | 14.84 | 24.08 | 8.00 | 111.0 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.67 | 13.06 | 20.45 | 5.00 | 78.0 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.65 | 12.40 | 20.62 | 9.00 | 105.4 | 180.0 |
| XI | Bench | Eberechi Eze | MID | 8 | 6.1 | 3.81 | 10.96 | 17.55 | 0.00 | 75.2 | 0.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.6 | 2.83 | 8.04 | 13.25 | 2.00 | 83.5 | 77.0 |