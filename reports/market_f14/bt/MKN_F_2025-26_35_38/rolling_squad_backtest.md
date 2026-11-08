# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 271.36
- Total actual points: 260.00
- Average predicted points: 67.84
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
- Predicted score: 57.12
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.98 | 10.87 | 17.69 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.05 | 0.03 | 0.34 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.53 | 15.06 | 23.40 | 6.00 | 98.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.56 | 11.85 | 18.20 | 6.00 | 88.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.26 | 10.98 | 18.80 | 1.00 | 74.3 | 90.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.55 | 8.48 | 13.61 | 2.00 | 59.8 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.67 | 8.42 | 14.01 | 1.00 | 76.2 | 73.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.36 | 18.23 | 29.72 | 7.00 | 75.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.99 | 13.93 | 23.22 | 6.00 | 87.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.53 | 7.11 | 11.04 | 2.00 | 62.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.86 | 18.59 | 31.56 | 5.00 | 99.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.56 | 13.05 | 20.31 | 4.00 | 98.6 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.00 | 12.13 | 20.72 | 4.00 | 53.6 | 20.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.88 | 11.90 | 19.72 | 1.00 | 72.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 4.22 | 10.99 | 17.80 | 3.00 | 89.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 84.99
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.71) beats the best remaining Triple Captain opportunity (7.83).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 7.65, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (14.71) beats the best remaining Triple Captain opportunity (7.83).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.08 | 11.34 | 18.34 | 9.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.10 | 0.46 | 0.00 | 7.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.53 | 15.23 | 23.89 | 11.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.33 | 12.34 | 20.03 | 2.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.26 | 11.71 | 18.22 | 5.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.29 | 7.63 | 13.14 | 4.00 | 66.4 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.20 | 7.49 | 12.51 | 2.00 | 67.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 11.96 | 24.35 | 36.47 | 11.00 | 165.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 2.93 | 11.69 | 20.48 | 2.00 | 68.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.19 | 7.43 | 11.28 | 2.00 | 64.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.22 | 19.95 | 33.05 | 3.00 | 93.9 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.64 | 17.06 | 24.11 | 5.00 | 142.6 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.83 | 13.75 | 21.25 | 0.00 | 91.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.63 | 12.81 | 20.66 | 2.00 | 77.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 2.63 | 10.04 | 16.99 | 4.00 | 75.6 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 62.92
- Actual score: 80.00
- Transfer: James Justin -> Marc Guéhi (projected gain 5.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.53 | 13.55 | 21.42 | 6.00 | 98.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.95 | 16.86 | 26.40 | 6.00 | 104.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.07 | 14.33 | 23.54 | 2.00 | 117.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 5.69 | 13.55 | 20.71 | 8.00 | 96.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.78 | 11.36 | 18.90 | 14.00 | 82.1 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.61 | 8.15 | 13.48 | 0.00 | 76.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.14 | 18.98 | 32.01 | 9.00 | 77.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.76 | 13.39 | 22.15 | 2.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.12 | 6.54 | 10.32 | 11.00 | 53.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.00 | 20.19 | 32.67 | 9.00 | 110.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 4.12 | 11.72 | 18.75 | 2.00 | 86.7 | 62.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.51 | 11.21 | 18.35 | 1.00 | 50.0 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.36 | 10.38 | 17.81 | 12.00 | 67.7 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.15 | 8.60 | 14.68 | 1.00 | 51.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.33
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 3.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.83 | 11.58 | 18.58 | 0.00 | 77.7 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.35 | 14.72 | 23.45 | 2.00 | 106.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.71 | 14.23 | 23.11 | 1.00 | 80.4 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.20 | 13.82 | 21.93 | 0.00 | 111.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.90 | 11.74 | 18.63 | 0.00 | 75.0 | 0.0 |
| Bench 2 | Bench Boost | El Hadji Malick Diouf | DEF | 19 | 4.1 | 3.22 | 8.13 | 13.30 | 6.00 | 78.2 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.28 | 20.82 | 34.24 | 0.00 | 95.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.48 | 11.73 | 19.70 | 2.00 | 76.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.75 | 8.03 | 12.98 | 2.00 | 63.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.73 | 19.13 | 32.20 | 14.00 | 96.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.24 | 11.78 | 19.70 | 0.00 | 77.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 3.95 | 11.74 | 19.55 | 2.00 | 92.1 | 64.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.76 | 10.48 | 16.94 | 1.00 | 53.5 | 32.0 |
| Bench 4 | Bench Boost | Mathias Jensen | MID | 5 | 4.9 | 2.64 | 9.15 | 15.36 | 2.00 | 67.5 | 82.0 |