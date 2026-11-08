# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 286.70
- Total actual points: 307.00
- Average predicted points: 71.68
- Average actual points: 76.75
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
- Predicted score: 60.06
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Enzo Fernández replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.30 | 9.21 | 15.07 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.69 | 4.54 | 6.61 | 1.00 | 49.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.08 | 11.37 | 18.61 | 5.00 | 84.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.73 | 10.82 | 17.33 | 5.00 | 81.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.65 | 10.31 | 16.81 | 6.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.32 | 6.44 | 10.25 | 2.00 | 63.8 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.16 | 6.06 | 9.83 | 2.00 | 68.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.99 | 17.41 | 30.35 | 8.00 | 67.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.45 | 13.55 | 20.36 | 2.00 | 73.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.61 | 12.43 | 20.79 | 2.00 | 77.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.97 | 17.20 | 26.35 | 5.00 | 88.7 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.57 | 16.36 | 26.55 | 5.00 | 87.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.62 | 16.01 | 26.24 | 0.00 | 89.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.11 | 14.37 | 23.64 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 7 | 4.8 | 3.13 | 8.19 | 13.45 | 2.00 | 71.0 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.38
- Actual score: 84.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 3.93, hit 0)
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 9.02 | 14.63 | 9.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.93 | 4.97 | 7.31 | 0.00 | 56.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.63 | 12.36 | 19.75 | 1.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.45 | 11.85 | 18.49 | 0.00 | 88.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.20 | 11.45 | 18.06 | 5.00 | 83.3 | 66.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.41 | 6.59 | 10.30 | 1.00 | 64.4 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.19 | 4.78 | 8.12 | 0.00 | 58.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.60 | 20.78 | 34.24 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.27 | 13.07 | 19.80 | 12.00 | 74.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.10 | 11.72 | 19.26 | 7.00 | 74.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.64 | 15.67 | 23.98 | 26.00 | 80.1 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.89 | 14.98 | 24.67 | 1.00 | 80.7 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.14 | 14.12 | 22.02 | 2.00 | 79.9 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.75 | 10.74 | 18.22 | 0.00 | 47.2 | 0.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 7 | 4.8 | 3.14 | 8.16 | 12.82 | 0.00 | 76.5 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: William Saliba
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 90.98
- Actual score: 106.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.75) beats the best remaining Triple Captain opportunity (14.19).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 6.15, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (13.75) beats the best remaining Triple Captain opportunity (14.19).
- Autosub: Issa Kaboré replaced Cole Palmer.
- Autosub: Enzo Fernández replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.16 | 9.31 | 15.42 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.61 | 2.11 | 3.30 | 0.00 | 25.8 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 8.81 | 13.26 | 20.64 | 14.00 | 179.4 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.48 | 12.84 | 19.51 | 12.00 | 180.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.19 | 12.54 | 19.37 | 26.00 | 164.0 | 180.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 3.9 | 2.14 | 6.13 | 9.89 | 2.00 | 57.2 | 90.0 |
| Bench 2 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 1.35 | 3.85 | 6.56 | 1.00 | 40.7 | 34.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.45 | 18.58 | 30.49 | 0.00 | 78.5 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.91 | 14.89 | 23.36 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.07 | 14.64 | 23.06 | 2.00 | 84.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.69 | 15.43 | 24.18 | 0.00 | 81.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.54 | 14.88 | 23.99 | 18.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.72 | 13.49 | 20.39 | 3.00 | 128.7 | 163.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.18 | 22.86 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Autosub In | Enzo Fernández | MID | 7 | 4.8 | 0.84 | 3.56 | 6.18 | 2.00 | 30.8 | 66.0 |

## GW35

- Train rows: 130234
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 76.28
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.91 | 11.07 | 17.77 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.50 | 1.37 | 2.49 | 1.00 | 17.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.20 | 14.65 | 23.20 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.93 | 13.86 | 21.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.78 | 13.47 | 21.02 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 1.94 | 5.85 | 9.56 | 0.00 | 64.1 | 0.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.87 | 3.04 | 5.38 | 0.00 | 32.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.99 | 17.22 | 27.28 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.03 | 15.23 | 25.82 | 5.00 | 40.5 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.09 | 13.99 | 22.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.96 | 17.76 | 28.59 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.10 | 14.61 | 23.47 | 8.00 | 103.5 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.39 | 13.05 | 21.43 | 9.00 | 116.3 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.52 | 12.59 | 19.71 | 5.00 | 74.8 | 78.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 7 | 4.8 | 2.98 | 6.03 | 9.43 | 0.00 | 88.7 | 0.0 |