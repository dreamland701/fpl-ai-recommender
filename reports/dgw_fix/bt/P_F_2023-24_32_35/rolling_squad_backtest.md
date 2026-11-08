# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 304.37
- Total actual points: 293.00
- Average predicted points: 76.09
- Average actual points: 73.25
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
- Bank: 100.00 -> 0.90
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.26
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Alexis Mac Allister replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.87 | 10.62 | 15.77 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.53 | 9.87 | 14.88 | 4.00 | 69.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 15.64 | 23.14 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.52 | 13.96 | 20.16 | 5.00 | 75.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.47 | 13.41 | 19.75 | 6.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.15 | 12.91 | 19.18 | 1.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.18 | 11.20 | 15.85 | 4.00 | 67.7 | 54.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.39 | 15.92 | 24.16 | 2.00 | 71.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.1 | 4.08 | 11.80 | 19.28 | 1.00 | 83.9 | 9.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.62 | 9.38 | 14.86 | 2.00 | 64.5 | 85.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.4 | 5.11 | 20.10 | 28.81 | 8.00 | 57.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.24 | 17.21 | 32.15 | 5.00 | 90.0 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.65 | 16.64 | 27.75 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.02 | 14.24 | 23.52 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Alexis Mac Allister | MID | 11 | 5.9 | 3.27 | 13.12 | 20.21 | 2.00 | 69.4 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.90 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.24
- Actual score: 61.00
- Transfer: Ivan Toney -> Alexander Isak (projected gain 2.16, hit 0)
- Autosub: Rodrigo Muniz Carvalho replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.85 | 11.13 | 16.40 | 0.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.71 | 10.68 | 15.89 | 0.00 | 79.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 16.79 | 24.56 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 15.10 | 21.62 | 0.00 | 82.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.05 | 14.80 | 21.36 | 5.00 | 78.8 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.78 | 13.94 | 20.29 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 2.63 | 10.06 | 14.21 | 0.00 | 56.6 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 15.35 | 22.89 | 7.00 | 70.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.22 | 12.44 | 22.79 | 12.00 | 73.2 | 90.0 |
| Bench 3 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.82 | 8.13 | 13.35 | 2.00 | 56.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 6.69 | 24.45 | 34.60 | 2.00 | 81.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.86 | 21.36 | 34.60 | 26.00 | 86.2 | 79.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 3.57 | 13.31 | 19.50 | 2.00 | 73.5 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.79 | 11.29 | 18.96 | 0.00 | 68.6 | 0.0 |
| Bench 2 | Bench | Phil Foden | MID | 13 | 8.2 | 3.50 | 10.80 | 22.37 | 0.00 | 41.9 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.10 -> 2.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Solanke
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 114.19
- Actual score: 124.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.44) beats the best remaining Triple Captain opportunity (13.87).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 7.33, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (19.44) beats the best remaining Triple Captain opportunity (13.87).
- Autosub: Phil Foden replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 6.07 | 11.68 | 17.03 | 18.00 | 172.7 | 180.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 5.53 | 10.90 | 16.34 | 1.00 | 160.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.75 | 16.49 | 24.13 | 14.00 | 177.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.16 | 15.04 | 21.47 | 12.00 | 169.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.83 | 14.66 | 21.47 | 26.00 | 153.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 8.05 | 14.61 | 20.72 | 2.00 | 168.5 | 180.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 2.29 | 6.11 | 9.94 | 2.00 | 62.3 | 105.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.75 | 18.42 | 26.90 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.00 | 14.44 | 27.78 | 2.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.32 | 7.46 | 12.19 | 5.00 | 50.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 13.50 | 25.68 | 36.65 | 3.00 | 176.6 | 106.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.85 | 21.54 | 36.57 | 0.00 | 86.4 | 0.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.1 | 8.99 | 15.86 | 21.93 | 14.00 | 171.2 | 162.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 6.22 | 12.03 | 17.56 | 3.00 | 146.4 | 106.0 |
| Bench 2 | Autosub In | Phil Foden | MID | 13 | 8.2 | 2.58 | 9.02 | 19.60 | 16.00 | 32.5 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 2.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Alexander Isak
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 79.68
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexis Mac Allister -> Bruno Borges Fernandes (projected gain 12.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.84 | 10.71 | 17.06 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Norberto Murara Neto | GK | 3 | 4.7 | 2.49 | 6.91 | 11.14 | 0.00 | 73.4 | 0.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.21 | 14.65 | 23.21 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.02 | 14.09 | 22.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.74 | 13.08 | 20.41 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.17 | 11.57 | 18.05 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.06 | 7.88 | 12.74 | 2.00 | 65.1 | 84.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 7.02 | 22.37 | 33.51 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.95 | 13.70 | 21.39 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.14 | 8.15 | 12.58 | 6.00 | 55.8 | 84.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.20 | 23.57 | 35.96 | 8.00 | 108.9 | 180.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.85 | 22.85 | 34.55 | 4.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.79 | 18.83 | 28.96 | 0.00 | 68.9 | 0.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 5.16 | 15.06 | 24.74 | 1.00 | 58.9 | 11.0 |
| Bench 2 | Bench Boost | Eberechi Eze | MID | 8 | 6.1 | 3.85 | 10.59 | 16.43 | 0.00 | 75.3 | 0.0 |