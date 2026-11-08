# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 271.28
- Total actual points: 299.00
- Average predicted points: 67.82
- Average actual points: 74.75
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
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.15
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Teden Mengi replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.3 | 3.51 | 9.00 | 14.30 | 4.00 | 94.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.39 | 5.57 | 8.07 | 1.00 | 58.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.83 | 11.30 | 18.56 | 5.00 | 81.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.61 | 10.62 | 16.98 | 5.00 | 76.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.38 | 9.86 | 16.04 | 6.00 | 76.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 1.98 | 6.21 | 10.17 | 2.00 | 63.3 | 83.0 |
| Bench 2 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.10 | 5.77 | 9.66 | 2.00 | 79.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.01 | 16.11 | 28.44 | 8.00 | 52.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.86 | 12.77 | 19.59 | 2.00 | 64.1 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.05 | 11.39 | 19.29 | 2.00 | 70.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.63 | 16.38 | 25.34 | 5.00 | 80.0 | 73.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.1 | 6.09 | 16.15 | 25.75 | 5.00 | 95.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.83 | 15.94 | 25.99 | 0.00 | 88.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.70 | 13.98 | 23.18 | 1.00 | 93.1 | 53.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 1.97 | 5.80 | 9.81 | 10.00 | 67.8 | 84.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Luis Díaz
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.62
- Actual score: 76.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.71, hit 0)
- Autosub: Guglielmo Vicario replaced Stefan Ortega Moreno.
- Autosub: Kobbie Mainoo replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | Guglielmo Vicario | GK | 18 | 5.3 | 2.32 | 7.87 | 13.08 | 0.00 | 81.8 | 90.0 |
| XI | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 3.43 | 7.23 | 10.61 | 0.00 | 87.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.82 | 12.83 | 20.42 | 1.00 | 95.4 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.57 | 11.89 | 18.62 | 5.00 | 88.4 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.79 | 11.83 | 18.17 | 0.00 | 91.8 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.09 | 6.36 | 10.13 | 1.00 | 66.7 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.33 | 5.43 | 9.24 | 0.00 | 73.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.55 | 20.52 | 33.73 | 10.00 | 104.4 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.15 | 12.60 | 19.19 | 12.00 | 77.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.56 | 10.95 | 18.14 | 7.00 | 71.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 6.08 | 15.97 | 24.42 | 26.00 | 87.0 | 79.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 6.43 | 14.57 | 21.98 | 2.00 | 97.4 | 65.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.45 | 14.52 | 24.05 | 1.00 | 77.5 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.23 | 10.81 | 18.39 | 0.00 | 62.7 | 0.0 |
| Bench 2 | Autosub In | Kobbie Mainoo | MID | 14 | 4.4 | 2.57 | 6.68 | 10.91 | 2.00 | 79.8 | 77.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Luis Díaz
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Luis Díaz
- Chip used: triple_captain
- Predicted score: 80.55
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.11) beats the best remaining Triple Captain opportunity (13.06).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 8.36, hit 0)
- Chip used: Triple Captain on Luis Díaz. Optimizer chose Triple Captain here because the current estimated captain upside (12.11) beats the best remaining Triple Captain opportunity (13.06).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Guglielmo Vicario | GK | 18 | 5.3 | 0.59 | 5.07 | 9.57 | 0.00 | 39.8 | 0.0 |
| XI | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.09 | 2.88 | 4.49 | 0.00 | 34.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.12 | 16.83 | 25.42 | 14.00 | 155.5 | 180.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.26 | 15.81 | 22.92 | 12.00 | 153.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.43 | 15.29 | 23.00 | 26.00 | 138.6 | 180.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.19 | 6.41 | 10.45 | 2.00 | 60.6 | 90.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.18 | 3.35 | 5.76 | 0.00 | 41.5 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 5.95 | 17.69 | 28.86 | 0.00 | 70.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 6.41 | 14.88 | 23.15 | 8.00 | 135.6 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.75 | 14.20 | 22.58 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.19 | 16.47 | 26.67 | 0.00 | 79.6 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.07 | 14.76 | 23.33 | 18.00 | 108.9 | 90.0 |
| Captain | Captain | Luis Díaz | MID | 11 | 7.7 | 8.27 | 14.66 | 20.45 | 3.00 | 125.9 | 163.0 |
| Bench 3 | Bench | Son Heung-min | MID | 18 | 10.0 | 2.15 | 11.82 | 21.88 | 0.00 | 30.8 | 0.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 3.46 | 7.86 | 12.49 | 5.00 | 85.6 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: bench_boost
- Predicted score: 72.97
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Guglielmo Vicario -> Jordan Pickford (projected gain 4.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.83 | 10.87 | 17.41 | 10.00 | 113.5 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.52 | 1.37 | 2.56 | 1.00 | 15.2 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.96 | 14.86 | 23.75 | 1.00 | 113.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.63 | 14.05 | 22.45 | 1.00 | 116.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.58 | 13.39 | 20.97 | 1.00 | 114.3 | 90.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 1.73 | 5.93 | 9.91 | 0.00 | 64.8 | 0.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.88 | 5.30 | 8.73 | 1.00 | 65.3 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 7.48 | 16.06 | 24.97 | 13.00 | 102.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.00 | 14.96 | 25.25 | 5.00 | 41.0 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.57 | 13.40 | 21.10 | 2.00 | 100.7 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 7.19 | 17.58 | 27.54 | 4.00 | 126.1 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.89 | 13.05 | 20.15 | 5.00 | 83.0 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 6.41 | 12.82 | 19.23 | 8.00 | 85.2 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.65 | 12.10 | 19.72 | 9.00 | 84.2 | 180.0 |
| Bench 2 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 3.16 | 7.61 | 12.33 | 3.00 | 84.7 | 64.0 |