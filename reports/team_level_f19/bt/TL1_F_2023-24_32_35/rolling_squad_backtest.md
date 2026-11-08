# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 283.41
- Total actual points: 313.00
- Average predicted points: 70.85
- Average actual points: 78.25
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
- Predicted score: 60.16
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Kristoffer Ajer replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.24 | 9.00 | 14.61 | 3.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.78 | 4.89 | 7.28 | 1.00 | 52.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.08 | 11.33 | 18.55 | 5.00 | 84.2 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.66 | 10.68 | 17.12 | 5.00 | 78.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.53 | 9.93 | 16.13 | 6.00 | 78.5 | 90.0 |
| Bench 2 | Autosub In | Kristoffer Ajer | DEF | 4 | 4.4 | 2.85 | 8.45 | 13.92 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.32 | 6.41 | 10.17 | 2.00 | 68.0 | 83.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.01 | 17.61 | 30.73 | 8.00 | 68.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.47 | 13.67 | 20.55 | 2.00 | 72.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.56 | 12.09 | 20.05 | 2.00 | 73.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.19 | 17.74 | 27.28 | 5.00 | 90.0 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.71 | 16.35 | 26.93 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.48 | 16.23 | 26.41 | 5.00 | 87.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.03 | 14.40 | 23.67 | 1.00 | 90.0 | 53.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.08 | 6.16 | 10.25 | 10.00 | 67.2 | 84.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.45
- Actual score: 84.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 5.25, hit 0)
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.95 | 8.69 | 14.04 | 9.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.16 | 5.43 | 8.08 | 0.00 | 58.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.59 | 12.26 | 19.51 | 1.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.26 | 11.34 | 17.55 | 0.00 | 83.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.11 | 11.32 | 17.82 | 5.00 | 81.2 | 66.0 |
| Bench 2 | Bench | Kristoffer Ajer | DEF | 4 | 4.4 | 3.54 | 9.10 | 14.83 | 0.00 | 84.4 | 0.0 |
| Bench 3 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.49 | 6.70 | 10.43 | 1.00 | 68.5 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.73 | 21.03 | 34.63 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.34 | 13.42 | 20.34 | 12.00 | 74.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.98 | 11.40 | 18.70 | 7.00 | 71.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.71 | 16.05 | 24.69 | 26.00 | 84.5 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.89 | 15.01 | 24.75 | 1.00 | 80.7 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.19 | 14.33 | 22.44 | 2.00 | 84.2 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.95 | 11.17 | 18.94 | 0.00 | 48.4 | 0.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.37 | 6.49 | 10.72 | 2.00 | 74.6 | 77.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.06
- Actual score: 106.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (9.73).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (9.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 9.21 | 15.08 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.76 | 2.62 | 4.11 | 0.00 | 28.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.62 | 13.09 | 20.38 | 14.00 | 178.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.90 | 12.34 | 19.13 | 26.00 | 159.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.04 | 12.30 | 18.63 | 12.00 | 171.1 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.28 | 6.17 | 10.06 | 2.00 | 61.6 | 90.0 |
| Bench 3 | Bench Boost | Kristoffer Ajer | DEF | 4 | 4.4 | 1.45 | 4.28 | 7.40 | 6.00 | 35.6 | 75.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.50 | 18.81 | 30.85 | 0.00 | 78.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.11 | 14.87 | 23.50 | 2.00 | 85.2 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.71 | 14.75 | 23.10 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.90 | 16.03 | 25.32 | 0.00 | 86.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.55 | 14.68 | 23.74 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.78 | 13.59 | 20.60 | 3.00 | 134.4 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.14 | 22.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 2.64 | 6.64 | 11.02 | 5.00 | 69.5 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.73
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.58) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.09, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.58) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.76 | 10.73 | 17.25 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.57 | 1.69 | 3.15 | 1.00 | 20.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.18 | 14.81 | 23.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.92 | 13.87 | 21.97 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.64 | 13.12 | 20.44 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Kristoffer Ajer | DEF | 4 | 4.4 | 2.32 | 6.76 | 11.04 | 2.00 | 58.9 | 83.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 1.98 | 5.97 | 9.77 | 0.00 | 68.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 7.11 | 17.54 | 27.58 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.01 | 15.33 | 26.09 | 5.00 | 40.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.97 | 13.72 | 21.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.01 | 17.59 | 28.32 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.38 | 15.22 | 24.58 | 8.00 | 113.8 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.42 | 13.14 | 21.50 | 9.00 | 113.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.57 | 12.83 | 20.12 | 5.00 | 78.5 | 78.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.58 | 6.92 | 11.47 | 3.00 | 69.6 | 64.0 |