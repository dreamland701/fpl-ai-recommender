# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.59
- Total actual points: 257.00
- Average predicted points: 71.15
- Average actual points: 64.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.31
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 10.87 | 17.69 | 6.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.43 | 15.06 | 23.40 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.25 | 11.85 | 18.20 | 6.00 | 79.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.51 | 10.98 | 18.80 | 1.00 | 78.3 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 3.24 | 8.48 | 13.61 | 2.00 | 53.5 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.87 | 8.42 | 14.01 | 1.00 | 81.7 | 73.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.38 | 18.23 | 29.72 | 7.00 | 74.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.93 | 23.22 | 6.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.11 | 11.04 | 2.00 | 65.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.13 | 18.59 | 31.56 | 5.00 | 90.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.40 | 13.05 | 20.31 | 4.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.26 | 12.13 | 20.72 | 4.00 | 81.8 | 20.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.09 | 11.90 | 19.72 | 1.00 | 76.2 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 3.95 | 10.99 | 17.80 | 3.00 | 84.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 98.66
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.44) beats the best remaining Triple Captain opportunity (9.63).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 7.43, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.44) beats the best remaining Triple Captain opportunity (9.63).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 11.34 | 18.34 | 9.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.44 | 15.23 | 23.89 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.52 | 12.34 | 20.03 | 2.00 | 86.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.07 | 11.71 | 18.22 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.54 | 7.63 | 13.14 | 4.00 | 72.5 | 90.0 |
| Bench 4 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.1 | 2.50 | 7.49 | 12.51 | 2.00 | 75.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 15.69 | 24.35 | 36.47 | 11.00 | 176.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.56 | 11.69 | 20.48 | 2.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.51 | 7.43 | 11.28 | 2.00 | 72.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 19.95 | 33.05 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 10.54 | 17.06 | 24.11 | 5.00 | 124.6 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.86 | 13.75 | 21.25 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.59 | 12.81 | 20.66 | 2.00 | 76.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 3.11 | 10.04 | 16.99 | 4.00 | 86.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.93
- Actual score: 80.00
- Transfer: El Hadji Malick Diouf -> Marc Guéhi (projected gain 6.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 5.13 | 13.55 | 21.42 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.53 | 16.86 | 26.40 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.83 | 14.33 | 23.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 5.10 | 13.55 | 20.71 | 8.00 | 81.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.93 | 11.36 | 18.90 | 14.00 | 85.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.63 | 7.45 | 13.00 | 6.00 | 62.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.18 | 18.98 | 32.01 | 9.00 | 80.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.72 | 13.39 | 22.15 | 2.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.34 | 6.54 | 10.32 | 11.00 | 58.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.81 | 20.19 | 32.67 | 9.00 | 90.0 | 90.0 |
| XI | XI | Mathias Jensen | MID | 5 | 4.9 | 4.07 | 11.72 | 18.75 | 2.00 | 85.6 | 62.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.31 | 11.21 | 18.35 | 1.00 | 50.8 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.51 | 10.38 | 17.81 | 12.00 | 70.1 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.70 | 8.60 | 14.68 | 1.00 | 40.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.69
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.18 | 11.58 | 18.58 | 0.00 | 86.4 | 0.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.08 | 14.72 | 23.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.23 | 23.11 | 1.00 | 90.0 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.68 | 13.82 | 21.93 | 0.00 | 90.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.16 | 11.74 | 18.63 | 0.00 | 81.7 | 0.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.21 | 9.17 | 14.80 | 1.00 | 79.9 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.15 | 20.82 | 34.24 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.80 | 11.73 | 19.70 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.01 | 8.03 | 12.98 | 2.00 | 69.6 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.34 | 19.13 | 32.20 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.59 | 11.78 | 19.70 | 0.00 | 84.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 3.92 | 11.74 | 19.55 | 2.00 | 90.0 | 64.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.43 | 10.48 | 16.94 | 1.00 | 49.5 | 32.0 |
| Bench 4 | Bench Boost | Mathias Jensen | MID | 5 | 4.9 | 2.84 | 9.15 | 15.36 | 2.00 | 72.0 | 82.0 |