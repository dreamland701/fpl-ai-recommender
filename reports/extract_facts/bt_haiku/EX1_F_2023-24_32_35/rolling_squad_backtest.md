# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 299.73
- Total actual points: 294.00
- Average predicted points: 74.93
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
- Predicted score: 59.78
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.13 | 8.78 | 14.30 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.29 | 5.96 | 8.98 | 1.00 | 65.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 11.33 | 18.54 | 5.00 | 82.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.62 | 10.68 | 17.13 | 5.00 | 77.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.49 | 9.93 | 16.14 | 6.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.69 | 10.66 | 2.00 | 66.6 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.00 | 6.34 | 10.48 | 1.00 | 73.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.21 | 18.04 | 31.21 | 8.00 | 76.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.35 | 13.36 | 20.04 | 2.00 | 71.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.50 | 12.07 | 20.08 | 2.00 | 73.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.10 | 17.62 | 27.07 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.54 | 16.35 | 26.53 | 5.00 | 86.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.25 | 26.68 | 0.00 | 90.0 | 0.0 |
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
- Predicted score: 59.95
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 7.29, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.59 | 13.92 | 9.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.98 | 5.28 | 7.90 | 0.00 | 57.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.57 | 12.26 | 19.58 | 1.00 | 87.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.09 | 11.32 | 17.90 | 5.00 | 79.9 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.27 | 11.27 | 19.21 | 0.00 | 79.2 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.60 | 7.16 | 11.40 | 2.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.89 | 10.78 | 1.00 | 67.1 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.12 | 21.89 | 36.09 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.22 | 13.10 | 19.88 | 12.00 | 73.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.01 | 11.47 | 18.78 | 7.00 | 71.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.72 | 15.96 | 24.51 | 26.00 | 83.3 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.88 | 15.08 | 24.82 | 1.00 | 80.7 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.21 | 14.42 | 22.55 | 2.00 | 82.7 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.80 | 11.08 | 18.82 | 0.00 | 48.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.27 | 8.03 | 13.46 | 7.00 | 78.5 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Eberechi Eze
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 101.87
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.21) beats the best remaining Triple Captain opportunity (14.18).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Eberechi Eze (projected gain 7.21, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.21) beats the best remaining Triple Captain opportunity (14.18).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Jan Paul van Hecke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.01 | 8.97 | 14.86 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.41 | 3.89 | 0.00 | 27.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 9.60 | 14.09 | 21.98 | 14.00 | 180.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.91 | 12.37 | 19.21 | 26.00 | 155.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.05 | 12.34 | 18.71 | 12.00 | 167.1 | 180.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.17 | 6.72 | 10.85 | 0.00 | 77.6 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.26 | 6.50 | 10.50 | 2.00 | 60.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.45 | 18.74 | 30.71 | 0.00 | 78.2 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.02 | 17.00 | 27.34 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.06 | 14.74 | 23.21 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 10.77 | 16.44 | 23.30 | 14.00 | 174.5 | 162.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.84 | 16.00 | 25.15 | 0.00 | 86.4 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 10.04 | 14.08 | 23.11 | 3.00 | 169.2 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.23 | 22.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.08 | 8.48 | 13.63 | 2.00 | 82.1 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 78.13
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Phil Foden (projected gain 4.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 8.54 | 14.16 | 3.00 | 82.5 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.55 | 1.65 | 3.04 | 1.00 | 19.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.16 | 14.81 | 23.60 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.90 | 22.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.63 | 13.14 | 20.50 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.66 | 10.69 | 0.00 | 76.3 | 0.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.07 | 6.25 | 10.22 | 0.00 | 67.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.95 | 17.14 | 27.12 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.06 | 15.44 | 26.14 | 5.00 | 40.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.01 | 13.81 | 21.68 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.34 | 14.76 | 25.35 | 8.00 | 136.5 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 4.88 | 14.29 | 23.22 | 0.00 | 71.2 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.65 | 13.00 | 20.34 | 5.00 | 78.6 | 78.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.22 | 12.98 | 21.38 | 9.00 | 111.9 | 180.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.6 | 2.87 | 8.12 | 13.35 | 2.00 | 83.9 | 77.0 |