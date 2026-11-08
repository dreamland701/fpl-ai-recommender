# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 258.26
- Total actual points: 270.00
- Average predicted points: 64.57
- Average actual points: 67.50
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
- Predicted score: 56.90
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.31 | 10.08 | 16.74 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.42 | 22.64 | 6.00 | 92.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.00 | 17.15 | 1.00 | 59.7 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.30 | 10.93 | 18.65 | 1.00 | 72.8 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.40 | 10.10 | 15.65 | 0.00 | 79.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.04 | 7.95 | 13.03 | 2.00 | 53.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.42 | 18.45 | 30.16 | 7.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.66 | 13.67 | 23.01 | 6.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.62 | 7.26 | 11.23 | 2.00 | 62.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.14 | 32.23 | 5.00 | 102.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.70 | 13.95 | 22.72 | 4.00 | 70.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.28 | 12.70 | 19.82 | 4.00 | 91.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.39 | 12.44 | 19.76 | 1.00 | 81.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.13 | 12.16 | 19.97 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.56
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.43) beats the best remaining Bench Boost opportunity (9.05).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 10.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.43) beats the best remaining Bench Boost opportunity (9.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 10.94 | 17.84 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.20 | 14.89 | 23.50 | 11.00 | 94.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.35 | 12.65 | 18.94 | 5.00 | 99.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.47 | 12.51 | 20.21 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.22 | 10.46 | 15.73 | 4.00 | 103.2 | 180.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.77 | 8.17 | 13.71 | 4.00 | 70.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 8.90 | 22.42 | 35.50 | 11.00 | 130.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.64 | 12.15 | 20.65 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.93 | 11.81 | 2.00 | 70.4 | 66.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.08 | 20.83 | 34.00 | 3.00 | 104.3 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 6.26 | 14.58 | 22.32 | 5.00 | 103.9 | 70.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.56 | 20.94 | 0.00 | 89.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.31 | 12.50 | 20.34 | 2.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 3.32 | 9.64 | 16.05 | 12.00 | 61.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.21
- Actual score: 85.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 13.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.74 | 12.41 | 19.76 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.17 | 15.96 | 25.28 | 6.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.62 | 13.73 | 22.75 | 2.00 | 111.5 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.18 | 11.73 | 18.33 | 3.00 | 106.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.85 | 11.39 | 18.91 | 14.00 | 83.7 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.64 | 7.60 | 13.15 | 6.00 | 60.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.23 | 19.38 | 32.82 | 9.00 | 81.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.28 | 22.00 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.52 | 6.93 | 10.72 | 11.00 | 57.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.88 | 9.00 | 108.6 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 3.16 | 11.02 | 18.38 | 1.00 | 49.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.40 | 10.42 | 17.69 | 12.00 | 75.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.41 | 10.41 | 17.83 | 12.00 | 67.1 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.73 | 13.59 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.59
- Actual score: 54.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Rayan Cherki -> Dominik Szoboszlai (projected gain 8.65, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mateus Mané replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.30 | 12.10 | 19.20 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.19 | 14.74 | 23.71 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.10 | 14.30 | 22.82 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.01 | 20.76 | 0.00 | 97.5 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.40 | 9.69 | 15.40 | 1.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.22 | 9.37 | 14.86 | 0.00 | 84.4 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.6 | 7.19 | 21.19 | 35.14 | 0.00 | 95.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.87 | 12.01 | 19.83 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.29 | 13.14 | 2.00 | 67.2 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.26 | 33.40 | 14.00 | 106.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.92 | 13.74 | 22.74 | 2.00 | 90.7 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.3 | 3.71 | 12.16 | 20.00 | 0.00 | 80.9 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.06 | 11.88 | 19.70 | 2.00 | 89.7 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.31 | 7.40 | 13.66 | 0.00 | 50.1 | 0.0 |