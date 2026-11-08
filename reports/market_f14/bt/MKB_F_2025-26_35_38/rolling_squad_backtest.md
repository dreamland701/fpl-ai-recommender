# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 289.30
- Total actual points: 262.00
- Average predicted points: 72.32
- Average actual points: 65.50
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
- Predicted score: 57.62
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.53 | 10.24 | 16.94 | 6.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.53 | 22.77 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.91 | 11.18 | 17.39 | 1.00 | 57.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.62 | 10.98 | 18.74 | 1.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.47 | 10.08 | 15.64 | 0.00 | 80.9 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.04 | 7.95 | 13.02 | 2.00 | 54.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.41 | 18.38 | 30.03 | 7.00 | 74.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.69 | 13.65 | 22.99 | 6.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.68 | 7.10 | 11.01 | 2.00 | 64.8 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 18.92 | 31.93 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.72 | 13.44 | 21.99 | 4.00 | 77.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.42 | 12.71 | 19.84 | 4.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.18 | 12.06 | 19.83 | 1.00 | 75.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.25 | 11.89 | 18.98 | 1.00 | 83.9 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 102.80
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.36) beats the best remaining Triple Captain opportunity (9.15).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 5.79, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.36) beats the best remaining Triple Captain opportunity (9.15).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.85 | 11.09 | 18.02 | 9.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.31 | 14.99 | 23.62 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.17 | 13.09 | 19.60 | 5.00 | 144.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.60 | 12.37 | 19.99 | 2.00 | 86.4 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.30 | 10.35 | 15.59 | 4.00 | 156.3 | 180.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.68 | 7.99 | 13.48 | 4.00 | 71.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.91 | 22.58 | 35.76 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.83 | 12.11 | 20.60 | 2.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.72 | 7.95 | 11.81 | 2.00 | 71.3 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.10 | 20.65 | 33.73 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.6 | 9.58 | 14.96 | 22.89 | 5.00 | 147.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.86 | 13.66 | 21.06 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.48 | 12.56 | 20.40 | 2.00 | 76.4 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.20 | 9.21 | 15.44 | 12.00 | 63.6 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.20
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 6.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.88 | 12.61 | 20.11 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.34 | 16.15 | 25.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.81 | 13.91 | 23.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.31 | 11.76 | 18.39 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.97 | 11.45 | 18.99 | 14.00 | 85.0 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.64 | 7.44 | 12.94 | 6.00 | 62.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.29 | 19.35 | 32.77 | 9.00 | 80.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.70 | 13.31 | 22.04 | 2.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.45 | 6.89 | 10.68 | 11.00 | 57.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.86 | 20.17 | 32.82 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.31 | 11.18 | 18.60 | 1.00 | 51.6 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.51 | 10.33 | 17.72 | 12.00 | 69.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.36 | 10.17 | 17.35 | 12.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.57 | 8.00 | 13.98 | 1.00 | 42.8 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.67
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.82) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 3.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.82) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.36 | 12.06 | 19.13 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.32 | 14.68 | 23.61 | 1.00 | 88.6 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.13 | 14.34 | 22.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.69 | 13.00 | 20.76 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.29 | 9.48 | 15.04 | 0.00 | 84.8 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.39 | 9.44 | 15.07 | 1.00 | 79.2 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.29 | 21.03 | 34.92 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.02 | 11.98 | 19.82 | 2.00 | 80.8 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.11 | 8.27 | 13.12 | 2.00 | 68.2 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.71 | 20.00 | 33.06 | 14.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.85 | 13.72 | 22.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.85 | 12.16 | 20.01 | 0.00 | 83.5 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.96 | 11.63 | 19.37 | 2.00 | 90.0 | 64.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.42 | 7.43 | 13.73 | 0.00 | 52.0 | 0.0 |