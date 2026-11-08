# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 263.86
- Total actual points: 321.00
- Average predicted points: 65.97
- Average actual points: 80.25
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
- Predicted score: 58.27
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.19 | 8.87 | 14.37 | 3.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.78 | 4.90 | 7.21 | 1.00 | 53.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.13 | 11.49 | 18.71 | 5.00 | 85.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.71 | 10.84 | 17.27 | 5.00 | 79.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.58 | 10.09 | 16.29 | 6.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.84 | 10.80 | 2.00 | 68.9 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.08 | 6.47 | 10.59 | 1.00 | 75.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 3.79 | 15.34 | 28.22 | 8.00 | 40.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.44 | 13.49 | 20.21 | 2.00 | 73.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.57 | 12.16 | 20.17 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.20 | 17.75 | 27.26 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.59 | 16.44 | 26.63 | 5.00 | 87.3 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.76 | 16.43 | 26.89 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.12 | 14.48 | 23.77 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 3.01 | 8.69 | 14.50 | 2.00 | 82.5 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 51.54
- Actual score: 101.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 5.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.99 | 8.68 | 13.98 | 9.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.00 | 5.32 | 7.91 | 0.00 | 58.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.61 | 12.34 | 19.66 | 1.00 | 89.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.15 | 11.42 | 17.98 | 5.00 | 81.2 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.29 | 11.39 | 17.67 | 0.00 | 83.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.65 | 7.24 | 11.47 | 2.00 | 81.9 | 90.0 |
| Bench 2 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.61 | 7.03 | 10.91 | 1.00 | 69.6 | 45.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 4.79 | 18.16 | 31.70 | 10.00 | 58.5 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.27 | 13.17 | 19.96 | 12.00 | 74.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.05 | 11.49 | 18.78 | 7.00 | 72.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 5.78 | 16.09 | 24.69 | 26.00 | 84.5 | 79.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.0 | 4.93 | 15.12 | 24.84 | 1.00 | 81.7 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 3.24 | 12.45 | 20.67 | 2.00 | 48.6 | 65.0 |
| Bench 4 | Bench | Phil Foden | MID | 13 | 8.2 | 2.02 | 9.55 | 17.76 | 0.00 | 25.3 | 0.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.35 | 8.14 | 13.55 | 7.00 | 80.5 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 83.32
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.64) beats the best remaining Bench Boost opportunity (10.63).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.11, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.64) beats the best remaining Bench Boost opportunity (10.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.07 | 9.05 | 14.91 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.76 | 2.57 | 4.03 | 0.00 | 30.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.76 | 13.24 | 20.59 | 14.00 | 177.8 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.04 | 12.49 | 19.34 | 26.00 | 158.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.18 | 12.44 | 18.82 | 12.00 | 170.1 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.64 | 10.62 | 2.00 | 62.9 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.09 | 6.61 | 10.78 | 0.00 | 76.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 3.45 | 16.00 | 28.56 | 0.00 | 40.8 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.74 | 14.74 | 23.14 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.98 | 14.57 | 23.12 | 2.00 | 82.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.89 | 16.04 | 25.24 | 0.00 | 87.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.43 | 14.57 | 23.47 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.82 | 13.68 | 20.71 | 3.00 | 132.6 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.08 | 22.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.01 | 8.37 | 13.57 | 2.00 | 80.6 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Alexander Isak
- Effective captain: Son Heung-min
- Chip used: triple_captain
- Predicted score: 70.74
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.63) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.09, hit 0)
- Chip used: Triple Captain on Son Heung-min. Optimizer chose Triple Captain here because the current estimated captain upside (10.63) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.77 | 10.71 | 17.20 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.67 | 1.84 | 3.22 | 1.00 | 22.6 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.18 | 14.86 | 23.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.92 | 13.91 | 22.06 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.65 | 13.16 | 20.51 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.44 | 6.74 | 10.77 | 0.00 | 77.8 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.37 | 10.33 | 0.00 | 69.6 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.01 | 17.22 | 27.25 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.97 | 13.70 | 21.53 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Erling Haaland | FWD | 13 | 14.1 | 2.69 | 13.23 | 24.39 | 5.00 | 20.2 | 28.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.88 | 17.49 | 28.13 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.52 | 13.16 | 23.11 | 8.00 | 60.5 | 180.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.9 | 7.43 | 13.12 | 21.54 | 9.00 | 117.2 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.62 | 12.89 | 20.19 | 5.00 | 77.7 | 78.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.6 | 2.94 | 8.23 | 13.45 | 2.00 | 85.7 | 77.0 |