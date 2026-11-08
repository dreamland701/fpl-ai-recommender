# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 282.39
- Total actual points: 308.00
- Average predicted points: 70.60
- Average actual points: 77.00
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
- Predicted score: 59.83
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Sander Berge replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.51 | 9.89 | 16.09 | 3.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.31 | 6.45 | 9.77 | 1.00 | 56.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.87 | 10.93 | 17.95 | 5.00 | 80.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.57 | 10.61 | 17.04 | 5.00 | 76.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.40 | 9.76 | 15.89 | 6.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Malo Gusto | DEF | 7 | 4.3 | 2.80 | 7.60 | 12.28 | 0.00 | 57.4 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.71 | 10.70 | 2.00 | 66.6 | 83.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.86 | 17.31 | 30.18 | 8.00 | 66.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.86 | 14.81 | 22.41 | 2.00 | 76.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.56 | 12.30 | 20.53 | 2.00 | 73.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.13 | 17.73 | 27.38 | 5.00 | 90.0 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.56 | 16.07 | 26.44 | 0.00 | 89.9 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.38 | 15.94 | 25.90 | 5.00 | 84.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.98 | 14.18 | 23.38 | 1.00 | 90.0 | 53.0 |
| Bench 3 | Autosub In | Sander Berge | MID | 6 | 4.6 | 2.76 | 7.66 | 12.50 | 1.00 | 79.8 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.15
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.46, hit 0)
- Autosub: Sander Berge replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.30 | 9.67 | 15.67 | 9.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.45 | 6.63 | 10.08 | 0.00 | 61.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.32 | 11.62 | 18.61 | 1.00 | 85.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.99 | 11.07 | 17.54 | 5.00 | 78.2 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.07 | 10.87 | 16.94 | 0.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.59 | 6.93 | 10.81 | 1.00 | 69.1 | 45.0 |
| Bench 4 | Bench | Malo Gusto | DEF | 7 | 4.3 | 2.06 | 5.29 | 8.45 | 6.00 | 35.2 | 87.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.34 | 20.32 | 33.59 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.62 | 14.24 | 21.75 | 12.00 | 77.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.00 | 11.47 | 18.86 | 7.00 | 70.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.70 | 15.96 | 24.58 | 26.00 | 84.5 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.23 | 14.50 | 22.74 | 2.00 | 83.2 | 65.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.65 | 14.50 | 23.99 | 1.00 | 77.4 | 57.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.60 | 10.56 | 18.06 | 0.00 | 46.5 | 0.0 |
| Bench 2 | Autosub In | Sander Berge | MID | 6 | 4.6 | 2.76 | 7.43 | 11.88 | 2.00 | 78.4 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 89.56
- Actual score: 105.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.73) beats the best remaining Triple Captain opportunity (14.47).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.50, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (13.73) beats the best remaining Triple Captain opportunity (14.47).
- Autosub: Charlie Taylor replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.35 | 9.96 | 16.47 | 2.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.95 | 3.23 | 5.19 | 0.00 | 30.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.14 | 12.51 | 19.51 | 14.00 | 169.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.72 | 12.14 | 18.87 | 26.00 | 152.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 7.68 | 11.87 | 18.01 | 12.00 | 162.6 | 180.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.30 | 6.52 | 10.52 | 2.00 | 61.3 | 90.0 |
| Bench 3 | Bench | Malo Gusto | DEF | 7 | 4.3 | 1.99 | 6.34 | 10.21 | 0.00 | 54.8 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.11 | 17.85 | 29.41 | 0.00 | 74.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.43 | 15.77 | 24.96 | 2.00 | 88.2 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.89 | 14.98 | 23.55 | 8.00 | 180.0 | 176.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.81 | 15.80 | 24.91 | 0.00 | 88.6 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.29 | 14.18 | 22.91 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.70 | 13.64 | 20.73 | 3.00 | 129.9 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.87 | 22.39 | 0.00 | 0.0 | 0.0 |
| XI | XI | Sander Berge | MID | 6 | 4.6 | 2.65 | 7.39 | 12.05 | 2.00 | 77.4 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 74.86
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.96) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 1.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.96) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.94 | 11.29 | 18.18 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.60 | 1.81 | 3.29 | 1.00 | 18.7 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.96 | 14.29 | 22.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.52 | 12.90 | 20.52 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.31 | 12.31 | 19.24 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.04 | 6.15 | 10.08 | 0.00 | 66.9 | 0.0 |
| Bench 4 | Bench Boost | Malo Gusto | DEF | 7 | 4.3 | 1.18 | 3.93 | 6.41 | 0.00 | 27.5 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.22 | 17.95 | 28.52 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.71 | 14.52 | 24.77 | 5.00 | 36.1 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.93 | 13.66 | 21.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.82 | 17.34 | 27.94 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.39 | 15.04 | 24.30 | 8.00 | 119.4 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 7.06 | 12.80 | 21.15 | 9.00 | 109.7 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.53 | 12.71 | 19.99 | 5.00 | 76.8 | 78.0 |
| Bench 2 | Bench Boost | Sander Berge | MID | 6 | 4.6 | 2.25 | 6.98 | 11.55 | 2.00 | 75.4 | 90.0 |