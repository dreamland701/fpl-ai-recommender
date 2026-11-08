# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 282.66
- Total actual points: 306.00
- Average predicted points: 70.66
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
- Predicted score: 59.75
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.14 | 8.76 | 14.21 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.69 | 4.82 | 7.23 | 1.00 | 50.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 11.34 | 18.54 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.63 | 10.71 | 17.18 | 5.00 | 77.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.50 | 9.94 | 16.14 | 6.00 | 77.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.70 | 10.68 | 2.00 | 66.6 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.00 | 6.32 | 10.43 | 1.00 | 73.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.03 | 17.52 | 30.35 | 8.00 | 68.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.36 | 13.44 | 20.28 | 2.00 | 71.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.49 | 11.99 | 19.99 | 2.00 | 73.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.10 | 17.68 | 27.37 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.56 | 16.37 | 26.54 | 5.00 | 86.7 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 16.30 | 26.75 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.09 | 14.41 | 23.71 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.96 | 8.54 | 14.27 | 2.00 | 81.1 | 90.0 |

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
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 3.67, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.55 | 13.80 | 9.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.94 | 5.25 | 7.94 | 0.00 | 57.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.24 | 19.57 | 1.00 | 87.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.32 | 17.91 | 5.00 | 79.9 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 11.30 | 17.62 | 0.00 | 82.1 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.61 | 7.17 | 11.40 | 2.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.53 | 6.88 | 10.73 | 1.00 | 67.4 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.59 | 20.85 | 34.34 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.23 | 13.10 | 19.94 | 12.00 | 73.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.00 | 11.35 | 18.55 | 7.00 | 71.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.72 | 16.06 | 24.81 | 26.00 | 83.0 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.88 | 14.99 | 24.66 | 1.00 | 80.5 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.23 | 14.48 | 22.71 | 2.00 | 82.9 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.80 | 10.94 | 18.53 | 0.00 | 48.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.30 | 7.98 | 13.31 | 7.00 | 79.0 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.61
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (10.51).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (10.51).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.01 | 8.89 | 14.69 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.66 | 2.39 | 3.81 | 0.00 | 27.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.65 | 13.13 | 20.46 | 14.00 | 174.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.91 | 12.40 | 19.29 | 26.00 | 155.7 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.06 | 12.34 | 18.73 | 12.00 | 167.3 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.17 | 6.70 | 10.80 | 0.00 | 77.7 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.27 | 6.44 | 10.34 | 2.00 | 60.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.43 | 18.56 | 30.40 | 0.00 | 78.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.06 | 14.69 | 23.19 | 2.00 | 84.4 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.69 | 14.67 | 23.04 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 15.95 | 25.21 | 0.00 | 85.2 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.40 | 14.54 | 23.48 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.72 | 13.65 | 20.77 | 3.00 | 130.2 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.13 | 22.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.08 | 8.44 | 13.54 | 2.00 | 82.2 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.42
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.62) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.16, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.62) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.74 | 10.65 | 17.15 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.55 | 1.65 | 3.01 | 1.00 | 19.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.15 | 14.83 | 23.69 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.89 | 13.85 | 22.01 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.61 | 13.12 | 20.50 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.39 | 6.66 | 10.69 | 0.00 | 76.5 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.08 | 6.22 | 10.14 | 0.00 | 67.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.96 | 17.22 | 27.36 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.12 | 15.87 | 27.08 | 5.00 | 42.1 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.96 | 13.64 | 21.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.84 | 17.49 | 28.22 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.42 | 15.19 | 24.53 | 8.00 | 113.9 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.30 | 12.93 | 21.23 | 9.00 | 113.2 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.60 | 12.87 | 20.19 | 5.00 | 77.6 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.90 | 8.11 | 13.26 | 2.00 | 84.6 | 77.0 |