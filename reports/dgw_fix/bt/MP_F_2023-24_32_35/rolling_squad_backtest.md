# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 303.09
- Total actual points: 290.00
- Average predicted points: 75.77
- Average actual points: 72.50
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
- Predicted score: 56.35
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Antoine Semenyo replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.87 | 10.62 | 15.77 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.69 | 4.41 | 6.47 | 1.00 | 50.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 15.64 | 23.14 | 5.00 | 83.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.47 | 13.41 | 19.75 | 6.00 | 76.6 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.18 | 11.20 | 15.85 | 4.00 | 67.7 | 54.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.46 | 6.41 | 10.09 | 2.00 | 67.3 | 83.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.20 | 5.89 | 9.71 | 2.00 | 77.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.73 | 18.36 | 32.29 | 8.00 | 61.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.39 | 15.92 | 24.16 | 2.00 | 71.2 | 90.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.48 | 8.86 | 13.58 | 2.00 | 46.7 | 68.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.4 | 5.11 | 20.10 | 28.81 | 8.00 | 57.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.24 | 17.21 | 32.15 | 5.00 | 90.0 | 73.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.16 | 16.94 | 25.38 | 3.00 | 75.8 | 88.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.64 | 27.75 | 0.00 | 90.0 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 3.27 | 13.12 | 20.21 | 2.00 | 69.4 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.10
- Actual score: 64.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 8.13, hit 0)
- Autosub: Charlie Taylor replaced Rayan Aït-Nouri.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.85 | 11.13 | 16.40 | 0.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.89 | 4.74 | 8.41 | 0.00 | 56.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 16.79 | 24.56 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 15.10 | 21.62 | 0.00 | 82.0 | 90.0 |
| XI | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 2.63 | 10.06 | 14.21 | 0.00 | 56.6 | 0.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.55 | 6.76 | 10.57 | 1.00 | 67.6 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.77 | 5.94 | 10.02 | 0.00 | 79.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.51 | 21.71 | 43.52 | 10.00 | 90.0 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 15.35 | 22.89 | 7.00 | 70.1 | 90.0 |
| Bench 3 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.53 | 9.70 | 14.39 | 0.00 | 56.2 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.4 | 6.69 | 24.45 | 34.60 | 2.00 | 81.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 5.86 | 21.36 | 34.60 | 26.00 | 86.2 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.17 | 18.66 | 26.64 | 2.00 | 81.7 | 65.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.55 | 17.24 | 25.22 | 3.00 | 77.4 | 78.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 3.57 | 13.31 | 19.50 | 2.00 | 73.5 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Solanke
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 115.02
- Actual score: 110.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.09) beats the best remaining Triple Captain opportunity (13.87).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Rayan Aït-Nouri -> Joachim Andersen (projected gain 6.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (19.09) beats the best remaining Triple Captain opportunity (13.87).
- Autosub: Antoine Semenyo replaced Cole Palmer.
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 6.07 | 11.68 | 17.03 | 18.00 | 172.7 | 180.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.50 | 1.84 | 3.60 | 0.00 | 24.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.75 | 16.49 | 24.13 | 14.00 | 177.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.16 | 15.04 | 21.47 | 12.00 | 169.4 | 180.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 6.66 | 12.08 | 17.29 | 11.00 | 175.2 | 180.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.25 | 6.45 | 10.40 | 2.00 | 59.9 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.16 | 3.45 | 6.06 | 0.00 | 39.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.28 | 19.21 | 38.46 | 0.00 | 74.5 | 0.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.75 | 18.42 | 26.90 | 8.00 | 180.0 | 176.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.77 | 6.04 | 9.88 | 10.00 | 67.2 | 117.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 13.50 | 25.68 | 36.65 | 3.00 | 176.6 | 106.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.85 | 21.54 | 36.57 | 0.00 | 86.4 | 0.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 9.00 | 17.43 | 25.59 | 20.00 | 154.8 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.75 | 16.21 | 22.61 | 3.00 | 130.9 | 163.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 6.22 | 12.03 | 17.56 | 3.00 | 146.4 | 106.0 |

## GW35

- Train rows: 130234
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Martin Ødegaard
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 72.61
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexis Mac Allister -> Anthony Gordon (projected gain 6.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.84 | 10.71 | 17.06 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.30 | 1.32 | 2.20 | 1.00 | 13.6 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.02 | 14.09 | 22.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.74 | 13.08 | 20.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.16 | 11.05 | 17.15 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.06 | 6.19 | 10.21 | 0.00 | 67.0 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.95 | 5.48 | 9.07 | 1.00 | 65.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.21 | 21.41 | 34.25 | 5.00 | 44.2 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.95 | 13.70 | 21.39 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | FWD | 3 | 4.5 | 3.20 | 8.46 | 13.35 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.20 | 23.57 | 35.96 | 8.00 | 108.9 | 180.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.10 | 17.27 | 27.37 | 2.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.2 | 4.91 | 16.59 | 23.77 | 10.00 | 76.7 | 81.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 5.16 | 15.06 | 24.74 | 1.00 | 58.9 | 11.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.62 | 12.54 | 19.47 | 5.00 | 77.9 | 78.0 |