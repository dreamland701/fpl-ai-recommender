# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 280.09
- Total actual points: 306.00
- Average predicted points: 70.02
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.24
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.12 | 8.76 | 14.28 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.69 | 4.71 | 6.98 | 1.00 | 50.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 11.38 | 18.63 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.52 | 10.45 | 16.79 | 5.00 | 75.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.47 | 9.88 | 16.08 | 6.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.46 | 6.75 | 10.76 | 2.00 | 67.3 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.29 | 6.25 | 10.15 | 2.00 | 71.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.73 | 17.05 | 29.85 | 8.00 | 61.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.33 | 13.25 | 19.90 | 2.00 | 70.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.39 | 11.79 | 19.75 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.24 | 17.89 | 27.58 | 5.00 | 90.0 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.23 | 26.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.49 | 16.22 | 26.36 | 5.00 | 85.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.02 | 14.28 | 23.54 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.92 | 8.52 | 14.36 | 2.00 | 80.2 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.53
- Actual score: 84.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.20, hit 0)
- Autosub: Charlie Taylor replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.89 | 8.50 | 13.80 | 9.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.89 | 5.07 | 7.58 | 0.00 | 56.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.28 | 19.63 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 11.30 | 17.60 | 0.00 | 82.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.05 | 11.21 | 17.75 | 5.00 | 78.8 | 66.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.55 | 6.93 | 10.85 | 1.00 | 67.6 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.87 | 6.29 | 10.43 | 0.00 | 74.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.51 | 20.80 | 34.36 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.22 | 13.08 | 19.91 | 12.00 | 73.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 11.30 | 18.58 | 7.00 | 70.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.86 | 16.33 | 25.13 | 26.00 | 86.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.78 | 14.80 | 24.43 | 1.00 | 78.1 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.17 | 14.34 | 22.46 | 2.00 | 81.7 | 65.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.79 | 11.11 | 18.74 | 0.00 | 68.6 | 0.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.25 | 7.94 | 13.35 | 7.00 | 77.9 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: William Saliba
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 84.44
- Actual score: 98.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.45) beats the best remaining Bench Boost opportunity (9.14).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 6.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.45) beats the best remaining Bench Boost opportunity (9.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.96 | 8.84 | 14.68 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.50 | 2.07 | 3.36 | 0.00 | 24.4 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 8.75 | 13.31 | 20.75 | 14.00 | 177.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.16 | 12.48 | 18.95 | 12.00 | 169.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.83 | 12.29 | 19.11 | 26.00 | 153.7 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.25 | 6.48 | 10.46 | 2.00 | 59.9 | 90.0 |
| Bench 3 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.27 | 3.71 | 6.37 | 1.00 | 38.9 | 34.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.28 | 18.37 | 30.24 | 0.00 | 74.5 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.75 | 14.79 | 23.27 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.00 | 14.58 | 23.02 | 2.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.85 | 16.02 | 25.24 | 0.00 | 86.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.32 | 14.36 | 23.18 | 18.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.75 | 13.61 | 20.63 | 3.00 | 130.9 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.94 | 22.47 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.02 | 8.34 | 13.43 | 2.00 | 80.9 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 77.87
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.40) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.84 | 10.85 | 17.45 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.30 | 1.08 | 2.17 | 1.00 | 13.6 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.21 | 14.89 | 23.73 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.02 | 14.13 | 22.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.74 | 13.35 | 20.83 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.06 | 6.22 | 10.17 | 0.00 | 67.0 | 0.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.39 | 4.34 | 7.40 | 0.00 | 44.1 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.02 | 17.26 | 27.30 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.21 | 15.79 | 26.77 | 5.00 | 44.2 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.95 | 13.64 | 21.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.85 | 17.42 | 28.05 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.20 | 14.97 | 24.19 | 8.00 | 108.9 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.62 | 12.85 | 20.13 | 5.00 | 77.9 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.83 | 12.55 | 20.76 | 9.00 | 102.9 | 180.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.84 | 8.05 | 13.26 | 2.00 | 83.3 | 77.0 |