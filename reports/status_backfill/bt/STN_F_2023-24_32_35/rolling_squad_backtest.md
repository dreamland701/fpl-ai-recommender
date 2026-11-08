# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 259.72
- Total actual points: 316.00
- Average predicted points: 64.93
- Average actual points: 79.00
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
- Predicted score: 59.91
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 8.77 | 14.30 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.81 | 4.81 | 7.13 | 1.00 | 53.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.95 | 11.35 | 18.59 | 5.00 | 82.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.60 | 10.70 | 17.16 | 5.00 | 77.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.45 | 9.95 | 16.18 | 6.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.49 | 6.70 | 10.69 | 2.00 | 67.1 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.92 | 6.33 | 10.48 | 1.00 | 71.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.71 | 17.57 | 30.62 | 8.00 | 66.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.70 | 13.44 | 20.20 | 2.00 | 76.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.50 | 12.04 | 20.10 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.35 | 17.69 | 27.27 | 5.00 | 94.4 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.49 | 16.37 | 26.58 | 5.00 | 86.1 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.70 | 16.32 | 26.80 | 0.00 | 92.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.04 | 14.40 | 23.72 | 1.00 | 97.2 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.90 | 8.56 | 14.40 | 2.00 | 78.8 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.78
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.24, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.87 | 8.57 | 13.90 | 9.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.06 | 5.27 | 7.89 | 0.00 | 59.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.51 | 12.27 | 19.63 | 1.00 | 89.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.29 | 11.34 | 17.66 | 0.00 | 84.3 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.33 | 17.93 | 5.00 | 80.6 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.57 | 7.17 | 11.42 | 2.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.54 | 6.89 | 10.79 | 1.00 | 67.2 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.44 | 20.88 | 34.47 | 10.00 | 100.7 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.44 | 13.13 | 19.98 | 12.00 | 76.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.87 | 11.40 | 18.73 | 7.00 | 69.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 6.00 | 16.08 | 24.73 | 26.00 | 87.5 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.74 | 15.03 | 24.78 | 1.00 | 78.4 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.42 | 14.49 | 22.69 | 2.00 | 86.7 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.65 | 11.01 | 18.76 | 0.00 | 46.9 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.23 | 8.01 | 13.44 | 7.00 | 77.4 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Dominic Solanke
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 70.40
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.66) beats the best remaining Bench Boost opportunity (13.99).
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 6.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.66) beats the best remaining Bench Boost opportunity (13.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.93 | 14.83 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.71 | 2.41 | 3.88 | 0.00 | 28.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.45 | 13.17 | 20.54 | 14.00 | 115.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.19 | 12.42 | 19.29 | 26.00 | 107.5 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.26 | 12.37 | 18.78 | 12.00 | 112.9 | 180.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.15 | 6.71 | 10.85 | 0.00 | 78.0 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.32 | 6.50 | 10.50 | 2.00 | 61.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.2 | 6.04 | 18.65 | 30.66 | 0.00 | 74.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.17 | 14.73 | 23.27 | 2.00 | 85.1 | 90.0 |
| Vice Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 6.01 | 14.68 | 23.09 | 8.00 | 122.9 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 16.02 | 25.25 | 0.00 | 84.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.41 | 14.54 | 23.48 | 18.00 | 99.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.75 | 13.66 | 20.72 | 3.00 | 97.3 | 163.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.14 | 13.18 | 22.85 | 0.00 | 57.3 | 0.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.7 | 3.05 | 8.46 | 13.62 | 2.00 | 81.3 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 70.63
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.16, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (10.68) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.65 | 10.68 | 17.19 | 10.00 | 110.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.57 | 1.64 | 3.02 | 1.00 | 18.4 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.06 | 14.84 | 23.66 | 1.00 | 111.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.76 | 13.89 | 22.05 | 1.00 | 112.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.59 | 13.15 | 20.52 | 1.00 | 109.5 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.40 | 6.66 | 10.70 | 0.00 | 76.8 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.08 | 6.24 | 10.21 | 0.00 | 66.7 | 0.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 7.48 | 17.22 | 27.30 | 13.00 | 104.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.94 | 15.31 | 26.02 | 5.00 | 41.0 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.72 | 13.71 | 21.57 | 2.00 | 95.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.14 | 17.47 | 28.13 | 4.00 | 111.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.36 | 15.24 | 24.61 | 8.00 | 81.8 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.47 | 12.97 | 21.39 | 9.00 | 81.6 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.50 | 12.90 | 20.25 | 5.00 | 75.4 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.78 | 8.11 | 13.34 | 2.00 | 81.7 | 77.0 |