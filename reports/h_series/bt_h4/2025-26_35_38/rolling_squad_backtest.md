# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 268.47
- Total actual points: 267.00
- Average predicted points: 67.12
- Average actual points: 66.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 55.67
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.32 | 10.17 | 17.28 | 6.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.00 | 0.15 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.77 | 13.67 | 21.63 | 6.00 | 86.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.54 | 11.14 | 18.78 | 1.00 | 82.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.64 | 11.05 | 17.55 | 1.00 | 63.4 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.67 | 8.13 | 13.42 | 1.00 | 80.5 | 73.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.80 | 7.94 | 12.85 | 2.00 | 59.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.31 | 19.06 | 30.57 | 7.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.38 | 13.41 | 22.52 | 6.00 | 83.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.82 | 12.70 | 21.71 | 2.00 | 77.5 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.01 | 18.50 | 30.82 | 5.00 | 84.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.86 | 14.71 | 24.04 | 4.00 | 81.0 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.40 | 12.58 | 20.35 | 1.00 | 85.0 | 45.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.30 | 12.42 | 19.08 | 4.00 | 87.4 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.55 | 6.91 | 10.03 | 2.00 | 69.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 94.73
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.52) beats the best remaining Triple Captain opportunity (8.85).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 5.94, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.52) beats the best remaining Triple Captain opportunity (8.85).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 11.47 | 19.08 | 9.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.88 | 14.22 | 22.56 | 11.00 | 87.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.65 | 12.61 | 19.28 | 5.00 | 147.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.33 | 12.47 | 19.80 | 2.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.69 | 8.09 | 13.27 | 2.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.42 | 22.51 | 35.36 | 11.00 | 179.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.76 | 12.46 | 21.60 | 2.00 | 79.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.52 | 11.60 | 19.60 | 2.00 | 77.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.16 | 33.05 | 3.00 | 86.9 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 8.79 | 14.18 | 22.13 | 5.00 | 144.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.66 | 13.40 | 20.26 | 0.00 | 88.6 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.22 | 9.85 | 16.36 | 12.00 | 66.7 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.50 | 7.17 | 10.60 | 0.00 | 70.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.70
- Actual score: 73.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.57 | 12.61 | 20.12 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.90 | 15.57 | 25.01 | 6.00 | 88.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.18 | 13.10 | 21.26 | 2.00 | 87.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.75 | 11.38 | 18.70 | 14.00 | 85.6 | 90.0 |
| Bench 2 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.72 | 8.55 | 13.88 | 0.00 | 79.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 5.81 | 19.21 | 32.70 | 9.00 | 80.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.45 | 13.09 | 21.89 | 2.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.22 | 13.04 | 22.22 | 2.00 | 84.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.50 | 19.91 | 32.19 | 9.00 | 85.9 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 2.81 | 10.76 | 18.27 | 1.00 | 52.5 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.26 | 10.51 | 18.11 | 12.00 | 78.6 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 1.52 | 4.08 | 6.56 | 0.00 | 32.0 | 0.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.37
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.05 | 11.86 | 19.12 | 0.00 | 81.5 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 13.85 | 22.79 | 1.00 | 83.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.58 | 13.54 | 21.66 | 2.00 | 88.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.22 | 12.22 | 19.55 | 0.00 | 86.6 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.21 | 9.19 | 14.88 | 1.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.65 | 7.33 | 12.30 | 6.00 | 70.7 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.86 | 20.71 | 34.53 | 0.00 | 88.4 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.80 | 13.74 | 22.48 | 12.00 | 85.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.67 | 11.70 | 19.07 | 2.00 | 78.1 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.59 | 32.09 | 14.00 | 84.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.28 | 13.07 | 21.69 | 2.00 | 86.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.64 | 11.10 | 18.82 | 2.00 | 84.7 | 64.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |
| Bench 4 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 0.84 | 2.68 | 5.01 | 0.00 | 20.7 | 0.0 |