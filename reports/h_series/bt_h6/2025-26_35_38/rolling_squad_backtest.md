# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 277.90
- Total actual points: 273.00
- Average predicted points: 69.47
- Average actual points: 68.25
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
- Predicted score: 57.61
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.61 | 17.59 | 6.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.03 | 0.20 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 14.29 | 22.74 | 6.00 | 88.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.76 | 11.23 | 17.38 | 1.00 | 58.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.58 | 11.18 | 18.85 | 1.00 | 79.5 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.91 | 8.97 | 14.51 | 1.00 | 79.8 | 73.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.06 | 8.12 | 13.12 | 2.00 | 55.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.45 | 18.58 | 30.14 | 7.00 | 73.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.66 | 13.42 | 22.44 | 6.00 | 81.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.82 | 12.46 | 20.93 | 2.00 | 74.0 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.44 | 19.39 | 32.39 | 5.00 | 87.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.03 | 14.52 | 23.93 | 4.00 | 76.8 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.61 | 13.15 | 20.03 | 4.00 | 87.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.42 | 12.81 | 20.31 | 1.00 | 81.4 | 45.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.55 | 6.91 | 10.03 | 2.00 | 69.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 93.22
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.77) beats the best remaining Triple Captain opportunity (9.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 4.48, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.77) beats the best remaining Triple Captain opportunity (9.00).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 10.97 | 18.41 | 9.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.13 | 1.37 | 1.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.43 | 23.01 | 11.00 | 89.5 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.74 | 12.56 | 18.82 | 5.00 | 144.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.53 | 12.37 | 20.12 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.69 | 8.09 | 13.27 | 2.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.67 | 22.43 | 35.56 | 11.00 | 178.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.91 | 12.66 | 21.62 | 2.00 | 77.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.75 | 11.94 | 20.38 | 2.00 | 76.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.14 | 20.93 | 34.05 | 3.00 | 90.1 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.93 | 13.95 | 20.78 | 0.00 | 89.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.80 | 13.88 | 22.25 | 2.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.44 | 9.76 | 16.11 | 12.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.50 | 7.17 | 10.60 | 0.00 | 70.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.19
- Actual score: 81.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.89 | 12.94 | 20.64 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.22 | 15.94 | 25.65 | 6.00 | 88.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.53 | 13.68 | 22.50 | 2.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.86 | 11.31 | 18.72 | 14.00 | 83.3 | 90.0 |
| Bench 2 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.68 | 8.30 | 13.63 | 0.00 | 77.1 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.18 | 19.55 | 32.81 | 9.00 | 78.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.57 | 13.15 | 21.89 | 2.00 | 83.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.19 | 12.86 | 22.05 | 2.00 | 81.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.79 | 20.53 | 32.95 | 9.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.02 | 12.30 | 20.42 | 9.00 | 79.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.41 | 10.70 | 18.17 | 12.00 | 76.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 1.52 | 4.08 | 6.56 | 0.00 | 32.0 | 0.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.87
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Enzo Fernández (projected gain 1.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.37 | 12.41 | 20.15 | 0.00 | 83.2 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.16 | 14.62 | 23.55 | 1.00 | 85.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.84 | 13.91 | 22.67 | 2.00 | 87.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.60 | 13.14 | 20.81 | 0.00 | 87.5 | 0.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.43 | 10.03 | 16.05 | 1.00 | 77.1 | 90.0 |
| Bench 3 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.65 | 7.33 | 12.30 | 6.00 | 70.7 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.21 | 21.27 | 35.13 | 0.00 | 86.7 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.19 | 14.66 | 23.90 | 12.00 | 88.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.86 | 11.87 | 19.43 | 2.00 | 77.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.73 | 20.12 | 33.12 | 14.00 | 86.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.74 | 14.26 | 23.02 | 2.00 | 88.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.07 | 12.01 | 19.85 | 2.00 | 86.3 | 64.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 3.97 | 11.62 | 18.87 | 1.00 | 81.2 | 90.0 |
| Bench 4 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 0.84 | 2.68 | 5.01 | 0.00 | 20.7 | 0.0 |