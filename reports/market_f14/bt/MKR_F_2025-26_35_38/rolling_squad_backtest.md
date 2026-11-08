# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.76
- Total actual points: 260.00
- Average predicted points: 71.19
- Average actual points: 65.00
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
- Predicted score: 57.09
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 10.87 | 17.68 | 6.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.09 | 0.03 | 0.37 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.47 | 15.06 | 23.39 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.29 | 11.85 | 18.19 | 6.00 | 79.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.54 | 10.98 | 18.79 | 1.00 | 78.4 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.15 | 8.48 | 13.63 | 2.00 | 53.4 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.81 | 8.42 | 14.03 | 1.00 | 81.7 | 73.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.36 | 18.23 | 29.73 | 7.00 | 74.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.62 | 13.93 | 23.25 | 6.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.62 | 7.11 | 11.06 | 2.00 | 65.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.07 | 18.59 | 31.58 | 5.00 | 90.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.38 | 13.05 | 20.32 | 4.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.15 | 12.13 | 20.74 | 4.00 | 81.6 | 20.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.10 | 11.90 | 19.71 | 1.00 | 76.3 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 3.86 | 10.99 | 17.83 | 3.00 | 84.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 99.48
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.57) beats the best remaining Triple Captain opportunity (9.71).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 7.37, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.57) beats the best remaining Triple Captain opportunity (9.71).
- Autosub: El Hadji Malick Diouf replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.02 | 11.34 | 18.33 | 9.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.10 | 0.44 | 0.00 | 4.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.46 | 15.23 | 23.89 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.57 | 12.34 | 20.02 | 2.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.10 | 11.71 | 18.21 | 5.00 | 79.8 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.50 | 7.63 | 13.15 | 4.00 | 72.4 | 90.0 |
| Bench 2 | Autosub In | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.53 | 7.49 | 12.50 | 2.00 | 75.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 15.82 | 24.28 | 36.39 | 11.00 | 177.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.59 | 11.69 | 20.47 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.50 | 7.43 | 11.28 | 2.00 | 72.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.88 | 19.95 | 33.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 10.76 | 17.00 | 24.02 | 5.00 | 125.5 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.90 | 13.74 | 21.24 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.59 | 12.81 | 20.66 | 2.00 | 76.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 3.16 | 10.04 | 16.97 | 4.00 | 86.1 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.96
- Actual score: 80.00
- Transfer: James Justin -> Marc Guéhi (projected gain 6.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.04 | 13.55 | 21.45 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.45 | 16.86 | 26.42 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.91 | 14.33 | 23.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 5.01 | 13.55 | 20.74 | 8.00 | 81.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.03 | 11.36 | 18.87 | 14.00 | 85.6 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.65 | 8.15 | 13.49 | 0.00 | 78.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.21 | 18.98 | 32.00 | 9.00 | 80.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.80 | 13.39 | 22.13 | 2.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.37 | 6.54 | 10.31 | 11.00 | 58.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.75 | 20.19 | 32.68 | 9.00 | 90.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 4.15 | 11.72 | 18.72 | 2.00 | 85.7 | 62.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.39 | 11.21 | 18.33 | 1.00 | 50.9 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.48 | 10.38 | 17.82 | 12.00 | 70.0 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.71 | 8.60 | 14.68 | 1.00 | 40.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.23
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 3.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.20 | 11.58 | 18.57 | 0.00 | 86.5 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.11 | 14.72 | 23.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.17 | 14.23 | 23.10 | 1.00 | 90.0 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.68 | 13.82 | 21.93 | 0.00 | 90.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.19 | 11.73 | 18.62 | 0.00 | 81.7 | 0.0 |
| Bench 4 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.79 | 8.13 | 13.32 | 6.00 | 70.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.12 | 20.82 | 34.25 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.82 | 11.73 | 19.70 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.97 | 8.03 | 12.99 | 2.00 | 69.5 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.29 | 19.13 | 32.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.61 | 11.78 | 19.69 | 0.00 | 84.9 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 3.85 | 11.74 | 19.58 | 2.00 | 90.0 | 64.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.42 | 10.48 | 16.94 | 1.00 | 49.5 | 32.0 |
| Bench 3 | Bench Boost | Mathias Jensen | MID | 5 | 4.9 | 2.88 | 9.15 | 15.34 | 2.00 | 72.1 | 82.0 |