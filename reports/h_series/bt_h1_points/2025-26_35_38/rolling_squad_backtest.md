# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 272.35
- Total actual points: 267.00
- Average predicted points: 68.09
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
- Predicted score: 56.05
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.39 | 10.07 | 17.01 | 6.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.78 | 13.83 | 21.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.42 | 11.04 | 18.85 | 1.00 | 79.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.55 | 10.91 | 17.02 | 1.00 | 59.4 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.71 | 8.10 | 13.40 | 1.00 | 80.5 | 73.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.81 | 7.97 | 12.98 | 2.00 | 56.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.24 | 18.51 | 29.95 | 7.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.54 | 13.59 | 22.99 | 6.00 | 83.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.90 | 12.87 | 21.36 | 2.00 | 74.1 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.24 | 19.48 | 32.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.94 | 14.47 | 23.55 | 4.00 | 79.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.52 | 12.86 | 19.99 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.30 | 12.35 | 19.59 | 1.00 | 84.1 | 45.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.55 | 6.91 | 10.03 | 2.00 | 69.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 94.97
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.60) beats the best remaining Triple Captain opportunity (8.90).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 3.99, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.60) beats the best remaining Triple Captain opportunity (8.90).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.97 | 18.09 | 9.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.92 | 14.31 | 22.84 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.40 | 12.35 | 18.48 | 5.00 | 143.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.32 | 12.15 | 19.77 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.69 | 8.09 | 13.27 | 2.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.50 | 22.58 | 35.40 | 11.00 | 180.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.72 | 12.55 | 21.32 | 2.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.72 | 12.02 | 20.61 | 2.00 | 77.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.94 | 20.73 | 33.63 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 8.72 | 14.35 | 21.73 | 5.00 | 142.8 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.80 | 13.64 | 20.71 | 0.00 | 90.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.27 | 9.98 | 16.60 | 12.00 | 64.4 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.50 | 7.17 | 10.60 | 0.00 | 70.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.78
- Actual score: 73.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.72 | 12.25 | 19.78 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.91 | 15.53 | 24.73 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.31 | 13.22 | 21.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.71 | 11.01 | 18.61 | 14.00 | 85.1 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.56 | 7.83 | 13.05 | 0.00 | 77.9 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.03 | 19.35 | 32.61 | 9.00 | 80.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.56 | 13.03 | 21.97 | 2.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.10 | 13.00 | 22.11 | 2.00 | 81.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.68 | 20.06 | 32.84 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 2.92 | 10.79 | 18.01 | 1.00 | 49.5 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.44 | 10.43 | 18.18 | 12.00 | 77.8 | 90.0 |
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
- Predicted score: 65.55
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.32 | 11.75 | 19.22 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.02 | 14.05 | 22.74 | 1.00 | 88.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.78 | 13.48 | 21.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.34 | 12.24 | 19.58 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.21 | 8.86 | 14.66 | 1.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.65 | 7.33 | 12.30 | 6.00 | 70.7 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.07 | 20.84 | 34.52 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.92 | 14.04 | 22.64 | 12.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.82 | 11.63 | 18.98 | 2.00 | 80.5 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.55 | 19.82 | 32.47 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.56 | 13.72 | 22.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.93 | 11.25 | 19.18 | 2.00 | 90.0 | 64.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |
| Bench 4 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 0.84 | 2.68 | 5.01 | 0.00 | 20.7 | 0.0 |