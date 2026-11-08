# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 279.61
- Total actual points: 266.00
- Average predicted points: 69.90
- Average actual points: 66.50
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
- Predicted score: 57.84
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 10.49 | 17.32 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.97 | 14.23 | 22.32 | 6.00 | 87.4 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.78 | 11.38 | 17.64 | 1.00 | 60.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.60 | 11.21 | 18.97 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 3.04 | 8.93 | 14.29 | 1.00 | 80.3 | 73.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.05 | 8.33 | 13.47 | 2.00 | 57.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.45 | 19.06 | 30.66 | 7.00 | 76.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.65 | 13.55 | 22.60 | 6.00 | 83.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.97 | 12.72 | 21.39 | 2.00 | 75.9 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.36 | 19.21 | 31.91 | 5.00 | 86.8 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.05 | 14.66 | 23.91 | 4.00 | 79.8 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.59 | 12.93 | 19.38 | 4.00 | 88.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.54 | 12.64 | 19.98 | 1.00 | 83.8 | 45.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.55 | 6.91 | 10.03 | 2.00 | 69.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 97.36
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.02).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 4.84, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.02).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.74 | 11.17 | 18.55 | 9.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.04 | 14.55 | 23.02 | 11.00 | 88.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.73 | 12.56 | 18.75 | 5.00 | 144.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.57 | 12.49 | 20.24 | 2.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.69 | 8.09 | 13.27 | 2.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.69 | 22.71 | 35.36 | 11.00 | 179.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.91 | 12.42 | 21.25 | 2.00 | 78.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.79 | 11.96 | 20.19 | 2.00 | 76.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.18 | 20.73 | 33.73 | 3.00 | 88.7 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 8.99 | 14.43 | 22.06 | 5.00 | 143.2 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.97 | 13.74 | 20.63 | 0.00 | 89.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.36 | 10.02 | 16.67 | 12.00 | 64.3 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.50 | 7.17 | 10.60 | 0.00 | 70.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.66
- Actual score: 72.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.83 | 12.66 | 20.52 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.18 | 15.83 | 25.07 | 6.00 | 89.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.53 | 13.69 | 22.55 | 2.00 | 90.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.85 | 11.42 | 19.21 | 14.00 | 85.5 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.83 | 8.47 | 13.58 | 0.00 | 78.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.20 | 19.57 | 32.94 | 9.00 | 79.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.40 | 22.24 | 2.00 | 84.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.33 | 13.02 | 22.04 | 2.00 | 83.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.85 | 20.19 | 32.98 | 9.00 | 88.3 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.02 | 11.06 | 18.36 | 1.00 | 50.9 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.53 | 10.79 | 18.13 | 12.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 1.52 | 4.08 | 6.56 | 0.00 | 32.0 | 0.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.75
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.34 | 12.34 | 19.73 | 0.00 | 82.2 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.23 | 14.72 | 23.64 | 1.00 | 85.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.95 | 14.11 | 22.46 | 2.00 | 89.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.47 | 12.73 | 20.30 | 0.00 | 87.4 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.27 | 9.61 | 15.19 | 1.00 | 76.2 | 90.0 |
| Bench 2 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.65 | 7.33 | 12.30 | 6.00 | 70.7 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.18 | 21.26 | 35.01 | 0.00 | 87.6 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.06 | 14.37 | 23.27 | 12.00 | 87.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.84 | 11.92 | 19.31 | 2.00 | 76.9 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.67 | 20.07 | 32.92 | 14.00 | 85.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.64 | 13.93 | 22.65 | 2.00 | 88.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.97 | 11.65 | 19.09 | 2.00 | 85.1 | 64.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |
| Bench 4 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 0.84 | 2.68 | 5.01 | 0.00 | 20.7 | 0.0 |