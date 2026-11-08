# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 273.59
- Total actual points: 305.00
- Average predicted points: 68.40
- Average actual points: 76.25
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
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.52
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 3.00 | 9.00 | 14.30 | 4.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 5.57 | 8.07 | 1.00 | 48.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.98 | 11.30 | 18.56 | 5.00 | 83.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.54 | 10.62 | 16.98 | 5.00 | 75.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.42 | 9.86 | 16.04 | 6.00 | 76.9 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.25 | 6.21 | 10.17 | 2.00 | 69.2 | 83.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.01 | 5.77 | 9.66 | 2.00 | 77.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.52 | 16.11 | 28.44 | 8.00 | 63.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.17 | 12.77 | 19.59 | 2.00 | 73.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.18 | 11.39 | 19.29 | 2.00 | 72.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.85 | 16.38 | 25.34 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.35 | 16.15 | 25.75 | 5.00 | 82.9 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.71 | 15.94 | 25.99 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.95 | 13.98 | 23.18 | 1.00 | 90.0 | 53.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 1.89 | 5.80 | 9.81 | 10.00 | 65.9 | 84.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 56.56
- Actual score: 76.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.73, hit 0)
- Autosub: Kobbie Mainoo replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 2.17 | 7.87 | 13.08 | 0.00 | 77.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.10 | 7.23 | 10.61 | 0.00 | 51.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.62 | 12.83 | 20.42 | 1.00 | 87.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.15 | 11.89 | 18.62 | 5.00 | 77.4 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.32 | 11.83 | 18.17 | 0.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.25 | 6.36 | 10.13 | 1.00 | 69.3 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.56 | 5.43 | 9.24 | 0.00 | 80.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.30 | 20.52 | 33.73 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.89 | 12.60 | 19.19 | 12.00 | 73.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.61 | 10.95 | 18.14 | 7.00 | 70.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.82 | 15.97 | 24.42 | 26.00 | 86.7 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.25 | 14.57 | 21.98 | 2.00 | 78.2 | 65.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.47 | 14.52 | 24.05 | 1.00 | 78.8 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.65 | 10.81 | 18.39 | 0.00 | 69.8 | 0.0 |
| Bench 2 | Autosub In | Kobbie Mainoo | MID | 14 | 4.4 | 2.25 | 6.68 | 10.91 | 2.00 | 72.4 | 77.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 87.05
- Actual score: 104.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.73) beats the best remaining Bench Boost opportunity (8.68).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 6.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.73) beats the best remaining Bench Boost opportunity (8.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Guglielmo Vicario | GK | 18 | 5.3 | 0.00 | 5.07 | 9.57 | 0.00 | 0.0 | 0.0 |
| XI | XI | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.61 | 2.88 | 4.49 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | William Saliba | DEF | 1 | 5.8 | 10.63 | 16.83 | 25.42 | 14.00 | 162.8 | 180.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 10.04 | 15.81 | 22.92 | 12.00 | 151.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 9.45 | 15.29 | 23.00 | 26.00 | 141.0 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.19 | 6.41 | 10.45 | 2.00 | 60.4 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.11 | 3.35 | 5.76 | 0.00 | 39.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.09 | 17.69 | 28.86 | 0.00 | 74.5 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.27 | 14.88 | 23.15 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.87 | 14.20 | 22.58 | 2.00 | 84.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.98 | 16.47 | 26.67 | 0.00 | 89.6 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.31 | 14.76 | 23.33 | 18.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 9.22 | 14.66 | 20.45 | 3.00 | 112.8 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 11.82 | 21.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 2.67 | 7.86 | 12.49 | 5.00 | 65.6 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 72.46
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Guglielmo Vicario -> Jordan Pickford (projected gain 4.78, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (10.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.86 | 10.87 | 17.41 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.39 | 1.37 | 2.56 | 1.00 | 13.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.99 | 14.86 | 23.75 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.74 | 14.05 | 22.45 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.52 | 13.39 | 20.97 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 1.86 | 5.93 | 9.91 | 0.00 | 68.2 | 0.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.91 | 5.30 | 8.73 | 1.00 | 65.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 6.58 | 16.06 | 24.97 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.03 | 14.96 | 25.25 | 5.00 | 44.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.59 | 13.40 | 21.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.80 | 17.58 | 27.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.47 | 13.05 | 20.15 | 5.00 | 76.5 | 78.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 7.17 | 12.82 | 19.23 | 8.00 | 100.5 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.38 | 12.10 | 19.72 | 9.00 | 101.7 | 180.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.42 | 7.61 | 12.33 | 3.00 | 66.1 | 64.0 |