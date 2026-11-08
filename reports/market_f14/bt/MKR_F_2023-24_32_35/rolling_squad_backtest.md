# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 277.81
- Total actual points: 304.00
- Average predicted points: 69.45
- Average actual points: 76.00
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
- Predicted score: 57.39
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 2.95 | 9.02 | 14.34 | 4.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.96 | 5.57 | 8.09 | 1.00 | 48.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.02 | 11.29 | 18.53 | 5.00 | 83.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.60 | 10.59 | 16.93 | 5.00 | 75.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.46 | 9.84 | 16.00 | 6.00 | 76.9 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.26 | 10.25 | 2.00 | 69.1 | 83.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.91 | 5.82 | 9.76 | 2.00 | 77.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.44 | 16.15 | 28.50 | 8.00 | 63.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.17 | 12.77 | 19.59 | 2.00 | 73.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.13 | 11.42 | 19.34 | 2.00 | 72.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.87 | 16.39 | 25.34 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.31 | 16.18 | 25.79 | 5.00 | 82.8 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 15.96 | 26.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.88 | 14.01 | 23.24 | 1.00 | 90.0 | 53.0 |
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
- Actual score: 75.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.71, hit 0)
- Autosub: Charlie Taylor replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 2.23 | 7.85 | 13.04 | 0.00 | 77.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.11 | 7.24 | 10.62 | 0.00 | 51.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.68 | 12.81 | 20.38 | 1.00 | 87.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.21 | 11.87 | 18.57 | 5.00 | 77.5 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.39 | 11.80 | 18.12 | 0.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.40 | 10.21 | 1.00 | 69.2 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.54 | 5.44 | 9.26 | 0.00 | 80.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.25 | 20.56 | 33.79 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.84 | 12.63 | 19.24 | 12.00 | 73.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.59 | 10.96 | 18.16 | 7.00 | 70.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.81 | 15.98 | 24.43 | 26.00 | 86.6 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.27 | 14.57 | 21.98 | 2.00 | 78.2 | 65.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.50 | 14.51 | 24.03 | 1.00 | 78.8 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.55 | 10.85 | 18.47 | 0.00 | 69.7 | 0.0 |
| Bench 3 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.16 | 6.73 | 11.00 | 2.00 | 72.3 | 77.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 91.05
- Actual score: 104.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.72) beats the best remaining Bench Boost opportunity (8.93).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Guglielmo Vicario -> Jordan Pickford (projected gain 8.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.72) beats the best remaining Bench Boost opportunity (8.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 6.24 | 10.59 | 15.98 | 18.00 | 169.7 | 180.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.86 | 4.45 | 0.00 | 23.2 | 0.0 |
| Captain | Captain | William Saliba | DEF | 1 | 5.8 | 10.78 | 16.78 | 25.35 | 14.00 | 163.0 | 180.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 10.23 | 15.75 | 22.84 | 12.00 | 152.1 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 9.61 | 15.24 | 22.92 | 26.00 | 141.2 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.14 | 6.44 | 10.50 | 2.00 | 60.4 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.05 | 3.37 | 5.81 | 0.00 | 39.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.09 | 17.69 | 28.86 | 0.00 | 74.5 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.30 | 14.97 | 23.23 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.78 | 14.24 | 22.65 | 2.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.04 | 16.43 | 26.61 | 0.00 | 89.7 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 9.40 | 14.61 | 20.36 | 3.00 | 113.0 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 11.83 | 21.91 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 2.27 | 8.28 | 15.35 | 0.00 | 39.1 | 0.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 2.68 | 7.86 | 12.49 | 5.00 | 65.6 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 72.81
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.42) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 10.04, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (10.42) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.78 | 10.92 | 17.48 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.35 | 1.39 | 2.59 | 1.00 | 13.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.10 | 14.80 | 23.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.83 | 14.00 | 22.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.62 | 13.34 | 20.88 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 1.87 | 5.93 | 9.90 | 0.00 | 68.2 | 0.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.88 | 5.32 | 8.76 | 1.00 | 65.5 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 6.62 | 16.06 | 24.95 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.94 | 15.00 | 25.33 | 5.00 | 44.5 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.56 | 13.42 | 21.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.77 | 17.61 | 27.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.54 | 13.02 | 20.10 | 5.00 | 76.6 | 78.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 7.22 | 12.82 | 19.22 | 8.00 | 100.6 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.39 | 12.22 | 19.82 | 9.00 | 101.5 | 180.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.39 | 7.63 | 12.36 | 3.00 | 66.1 | 64.0 |