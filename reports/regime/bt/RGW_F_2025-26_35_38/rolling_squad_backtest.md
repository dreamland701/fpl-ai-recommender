# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 285.25
- Total actual points: 259.00
- Average predicted points: 71.31
- Average actual points: 64.75
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.18
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.27 | 9.82 | 16.11 | 6.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.13 | 0.21 | 0.39 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.02 | 14.61 | 22.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.01 | 11.68 | 17.64 | 0.00 | 81.4 | 45.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.54 | 17.99 | 1.00 | 58.7 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.56 | 10.34 | 16.08 | 0.00 | 81.3 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 3.25 | 9.33 | 15.29 | 1.00 | 82.5 | 73.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.22 | 18.01 | 29.33 | 7.00 | 70.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.57 | 13.16 | 21.89 | 6.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.65 | 6.96 | 10.58 | 2.00 | 65.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.15 | 18.57 | 31.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.87 | 13.80 | 22.31 | 4.00 | 80.2 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.35 | 12.65 | 19.40 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.33 | 12.18 | 19.14 | 1.00 | 82.5 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.19 | 12.02 | 19.51 | 1.00 | 76.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 102.77
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.23) beats the best remaining Triple Captain opportunity (8.85).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 4.82, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.23) beats the best remaining Triple Captain opportunity (8.85).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.77 | 17.34 | 9.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.22 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.21 | 15.09 | 23.81 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.22 | 12.88 | 19.75 | 5.00 | 148.3 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.66 | 10.91 | 16.59 | 4.00 | 156.8 | 180.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 6.51 | 10.47 | 15.81 | 3.00 | 118.0 | 171.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.79 | 8.51 | 14.02 | 2.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.43 | 21.66 | 34.49 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.70 | 11.60 | 19.61 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.65 | 7.62 | 11.34 | 2.00 | 70.7 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.95 | 20.32 | 33.06 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.34 | 14.09 | 22.20 | 5.00 | 146.8 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.79 | 13.42 | 20.48 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.40 | 12.31 | 19.74 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.26 | 9.28 | 15.20 | 12.00 | 62.4 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.26
- Actual score: 77.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.55 | 11.85 | 18.55 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.11 | 0.19 | 0.31 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.07 | 15.75 | 24.74 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.56 | 12.98 | 21.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.44 | 12.03 | 18.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.46 | 12.02 | 18.47 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.97 | 8.84 | 14.53 | 0.00 | 78.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.14 | 18.86 | 31.87 | 9.00 | 80.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.57 | 12.73 | 20.93 | 2.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.34 | 6.50 | 10.15 | 11.00 | 55.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.71 | 19.79 | 32.10 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.16 | 10.50 | 17.71 | 1.00 | 51.3 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.53 | 10.30 | 17.51 | 12.00 | 71.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.35 | 10.09 | 16.98 | 12.00 | 77.5 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.51 | 7.65 | 13.35 | 1.00 | 44.8 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.05
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.04) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Dominik Szoboszlai (projected gain 3.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.04) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.17 | 11.58 | 18.13 | 0.00 | 83.7 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.07 | 0.20 | 0.00 | 0.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.12 | 14.37 | 23.07 | 1.00 | 88.7 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.52 | 12.57 | 19.86 | 0.00 | 90.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.69 | 10.61 | 17.13 | 1.00 | 83.8 | 45.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.41 | 9.76 | 15.53 | 0.00 | 84.9 | 0.0 |
| Bench 4 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.84 | 7.99 | 13.41 | 6.00 | 71.9 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.04 | 20.46 | 33.48 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.86 | 11.60 | 19.08 | 2.00 | 79.1 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.95 | 7.84 | 12.30 | 2.00 | 66.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.62 | 19.69 | 32.46 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.83 | 13.47 | 22.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 11.96 | 19.53 | 0.00 | 86.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.89 | 11.21 | 18.37 | 2.00 | 89.7 | 64.0 |
| Bench 2 | Bench Boost | Rayan Cherki | MID | 13 | 6.5 | 3.25 | 9.80 | 16.07 | 1.00 | 48.9 | 32.0 |