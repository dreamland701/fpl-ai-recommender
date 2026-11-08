# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.66
- Total actual points: 262.00
- Average predicted points: 71.17
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
- Predicted score: 58.81
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.35 | 9.83 | 16.34 | 6.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.00 | 0.15 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.44 | 22.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.91 | 11.14 | 17.36 | 1.00 | 59.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.66 | 11.02 | 18.78 | 1.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.46 | 10.04 | 15.55 | 0.00 | 80.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.12 | 8.16 | 13.36 | 2.00 | 56.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.57 | 18.70 | 30.54 | 7.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.66 | 22.99 | 6.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.16 | 11.07 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.15 | 32.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.05 | 14.29 | 23.24 | 4.00 | 79.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.63 | 13.15 | 20.53 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.51 | 12.56 | 19.95 | 1.00 | 84.1 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.28 | 12.29 | 20.17 | 1.00 | 76.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 1
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 98.01
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.83) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson, Jaydee Canvot -> Marc Guéhi, Alex Scott (projected gain 3.79, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.83) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.71 | 17.49 | 9.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.83 | 23.40 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.18 | 13.10 | 20.21 | 15.00 | 179.7 | 180.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.81 | 12.57 | 18.83 | 5.00 | 143.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.64 | 12.46 | 20.12 | 2.00 | 85.7 | 90.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.73 | 22.25 | 35.26 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.87 | 12.21 | 20.75 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.66 | 7.83 | 11.64 | 2.00 | 70.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.79 | 33.93 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 13.93 | 21.47 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.49 | 12.62 | 20.52 | 2.00 | 77.5 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 3.75 | 10.96 | 17.58 | 4.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.31 | 10.80 | 18.86 | 0.00 | 50.3 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.00
- Free transfers: 1 -> 1
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.77
- Actual score: 76.00
- Transfer: Nico O'Reilly -> Maxence Lacroix (projected gain 4.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.68 | 12.12 | 19.34 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.02 | 0.00 | 0.01 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 15.97 | 25.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.58 | 13.36 | 22.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.43 | 12.24 | 18.73 | 2.00 | 90.0 | 60.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.94 | 11.37 | 18.88 | 14.00 | 85.1 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.28 | 19.31 | 32.73 | 9.00 | 80.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.35 | 22.11 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.42 | 6.82 | 10.55 | 11.00 | 56.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.87 | 9.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.62 | 10.58 | 18.09 | 12.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.17 | 8.49 | 15.49 | 7.00 | 36.7 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 2.74 | 8.32 | 14.61 | 4.00 | 60.7 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 0.00 -> 0.00
- Free transfers: 1 -> 1
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.07
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.00) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Maxence Lacroix -> Marcos Senesi Barón (projected gain 3.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.00) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.30 | 11.92 | 18.93 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.33 | 14.68 | 23.61 | 1.00 | 88.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.19 | 22.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 12.86 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.34 | 12.67 | 20.55 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.46 | 9.61 | 15.29 | 1.00 | 78.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.35 | 21.14 | 35.09 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 12.01 | 19.82 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.21 | 13.01 | 2.00 | 67.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 20.14 | 33.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.21 | 12.54 | 21.14 | 9.00 | 76.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.95 | 12.45 | 20.44 | 0.00 | 85.7 | 0.0 |
| XI | XI | Alex Scott | MID | 4 | 4.9 | 3.67 | 10.58 | 16.98 | 0.00 | 78.5 | 0.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |