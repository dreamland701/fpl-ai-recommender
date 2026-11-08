# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 299.08
- Total actual points: 294.00
- Average predicted points: 74.77
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
- Predicted score: 59.82
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.13 | 8.78 | 14.29 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.71 | 4.79 | 7.11 | 1.00 | 51.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 11.33 | 18.54 | 5.00 | 82.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.62 | 10.67 | 17.12 | 5.00 | 77.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.49 | 9.93 | 16.14 | 6.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.69 | 10.66 | 2.00 | 66.6 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.99 | 6.34 | 10.48 | 1.00 | 73.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.24 | 18.24 | 31.61 | 8.00 | 76.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.35 | 13.36 | 20.04 | 2.00 | 71.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.50 | 12.08 | 20.09 | 2.00 | 73.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.11 | 17.63 | 27.09 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.54 | 16.36 | 26.53 | 5.00 | 86.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.26 | 26.68 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.06 | 14.37 | 23.65 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.94 | 8.59 | 14.43 | 2.00 | 80.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.01
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 7.29, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.59 | 13.92 | 9.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.98 | 5.28 | 7.91 | 0.00 | 57.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.57 | 12.27 | 19.59 | 1.00 | 87.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.09 | 11.32 | 17.89 | 5.00 | 79.9 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 10.80 | 18.49 | 0.00 | 78.0 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.60 | 7.16 | 11.40 | 2.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.88 | 10.78 | 1.00 | 67.1 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.16 | 21.99 | 36.33 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.23 | 13.11 | 19.89 | 12.00 | 73.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.01 | 11.48 | 18.79 | 7.00 | 71.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.72 | 15.98 | 24.53 | 26.00 | 83.3 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.89 | 15.09 | 24.83 | 1.00 | 80.8 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.21 | 14.43 | 22.56 | 2.00 | 82.7 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.80 | 11.08 | 18.82 | 0.00 | 48.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.28 | 8.03 | 13.46 | 7.00 | 78.5 | 90.0 |

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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.93) beats the best remaining Triple Captain opportunity (14.20).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Eberechi Eze (projected gain 6.95, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (14.93) beats the best remaining Triple Captain opportunity (14.20).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Jan Paul van Hecke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.01 | 8.97 | 14.86 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.41 | 3.88 | 0.00 | 27.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 9.68 | 14.22 | 22.24 | 14.00 | 180.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.91 | 12.37 | 19.21 | 26.00 | 155.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.05 | 12.35 | 18.72 | 12.00 | 167.1 | 180.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.17 | 6.72 | 10.85 | 0.00 | 77.6 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.26 | 6.50 | 10.50 | 2.00 | 60.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.45 | 18.76 | 30.73 | 0.00 | 78.2 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.74 | 16.84 | 27.28 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.07 | 14.75 | 23.22 | 2.00 | 84.7 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 10.47 | 16.18 | 23.09 | 14.00 | 171.8 | 162.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.84 | 16.02 | 25.18 | 0.00 | 86.6 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 10.15 | 13.98 | 22.98 | 3.00 | 171.7 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.23 | 22.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.08 | 8.48 | 13.64 | 2.00 | 82.1 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 78.30
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Phil Foden (projected gain 4.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 8.55 | 14.17 | 3.00 | 82.5 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.55 | 1.65 | 3.03 | 1.00 | 19.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.16 | 14.81 | 23.59 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.90 | 22.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.63 | 13.14 | 20.50 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.66 | 10.69 | 0.00 | 76.3 | 0.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.07 | 6.25 | 10.22 | 0.00 | 67.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.96 | 17.15 | 27.11 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.06 | 15.46 | 26.16 | 5.00 | 40.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.01 | 13.82 | 21.68 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.42 | 14.83 | 25.86 | 8.00 | 139.2 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 4.88 | 14.29 | 23.21 | 0.00 | 71.2 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.65 | 13.00 | 20.34 | 5.00 | 78.7 | 78.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.23 | 12.98 | 21.38 | 9.00 | 111.9 | 180.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.6 | 2.87 | 8.12 | 13.35 | 2.00 | 83.9 | 77.0 |