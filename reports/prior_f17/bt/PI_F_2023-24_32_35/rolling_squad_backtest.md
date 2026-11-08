# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 281.46
- Total actual points: 306.00
- Average predicted points: 70.36
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
- Predicted score: 59.40
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.12 | 8.74 | 14.21 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.81 | 5.11 | 7.69 | 1.00 | 52.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.00 | 11.25 | 18.44 | 5.00 | 82.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.66 | 10.76 | 17.23 | 5.00 | 77.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.50 | 9.92 | 16.10 | 6.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.71 | 10.70 | 2.00 | 66.7 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.00 | 6.34 | 10.49 | 1.00 | 73.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.79 | 17.06 | 29.82 | 8.00 | 67.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.34 | 13.34 | 20.08 | 2.00 | 72.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.52 | 12.12 | 20.22 | 2.00 | 73.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.05 | 17.50 | 27.01 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.56 | 16.42 | 26.65 | 5.00 | 86.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.68 | 16.30 | 26.76 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.12 | 14.51 | 23.86 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.91 | 8.50 | 14.32 | 2.00 | 80.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.54
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.27, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.92 | 8.54 | 13.81 | 9.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.05 | 5.54 | 8.40 | 0.00 | 59.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.54 | 12.19 | 19.50 | 1.00 | 87.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.13 | 11.38 | 17.98 | 5.00 | 79.8 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.25 | 11.30 | 17.57 | 0.00 | 82.3 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.61 | 7.17 | 11.41 | 2.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.89 | 10.79 | 1.00 | 67.3 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.43 | 20.49 | 33.86 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.18 | 13.00 | 19.80 | 12.00 | 73.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.01 | 11.46 | 18.82 | 7.00 | 70.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.68 | 15.90 | 24.48 | 26.00 | 83.9 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.88 | 15.08 | 24.86 | 1.00 | 80.2 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.28 | 14.62 | 22.91 | 2.00 | 83.1 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.80 | 11.06 | 18.82 | 0.00 | 48.1 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.25 | 7.96 | 13.38 | 7.00 | 78.6 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.70
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.59) beats the best remaining Bench Boost opportunity (10.59).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.59) beats the best remaining Bench Boost opportunity (10.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.00 | 8.90 | 14.73 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.73 | 2.69 | 4.43 | 0.00 | 28.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.59 | 13.09 | 20.43 | 14.00 | 174.6 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.01 | 12.47 | 19.35 | 26.00 | 155.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.07 | 12.33 | 18.70 | 12.00 | 167.1 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.17 | 6.71 | 10.83 | 0.00 | 77.7 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.26 | 6.50 | 10.51 | 2.00 | 60.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.27 | 18.24 | 30.00 | 0.00 | 77.6 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.73 | 14.76 | 23.22 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.99 | 14.53 | 22.98 | 2.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.77 | 15.81 | 24.92 | 0.00 | 86.2 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.46 | 14.68 | 23.69 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.87 | 13.82 | 21.01 | 3.00 | 131.4 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.25 | 22.96 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.06 | 8.43 | 13.57 | 2.00 | 82.1 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 77.81
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.44) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.17, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.44) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.75 | 10.65 | 17.10 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.63 | 1.94 | 3.59 | 1.00 | 20.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.21 | 14.89 | 23.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.89 | 13.85 | 21.98 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.64 | 13.13 | 20.45 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.65 | 10.68 | 0.00 | 76.3 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.07 | 6.24 | 10.22 | 0.00 | 67.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.91 | 17.04 | 27.03 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.84 | 14.84 | 25.26 | 5.00 | 39.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.01 | 13.80 | 21.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.92 | 17.62 | 28.35 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.24 | 15.00 | 24.25 | 8.00 | 113.8 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.65 | 13.04 | 20.49 | 5.00 | 77.9 | 78.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.27 | 13.01 | 21.45 | 9.00 | 111.9 | 180.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.86 | 8.08 | 13.29 | 2.00 | 83.9 | 77.0 |