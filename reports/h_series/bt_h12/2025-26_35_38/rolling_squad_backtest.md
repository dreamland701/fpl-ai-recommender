# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 280.11
- Total actual points: 253.00
- Average predicted points: 70.03
- Average actual points: 63.25
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
- Predicted score: 57.70
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.23 | 9.79 | 16.11 | 6.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.06 | 14.40 | 22.44 | 6.00 | 90.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.79 | 11.08 | 17.11 | 1.00 | 59.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.59 | 10.98 | 18.61 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.34 | 9.95 | 15.46 | 0.00 | 80.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.01 | 8.14 | 13.26 | 2.00 | 56.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.47 | 18.68 | 30.37 | 7.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.61 | 13.57 | 22.90 | 6.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.16 | 11.07 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.37 | 19.14 | 32.12 | 5.00 | 90.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.96 | 14.34 | 23.09 | 4.00 | 79.4 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.54 | 13.10 | 20.54 | 4.00 | 91.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.39 | 12.54 | 19.78 | 1.00 | 84.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.22 | 12.38 | 20.06 | 1.00 | 76.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 95.33
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.55, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.60 | 10.64 | 17.30 | 9.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.12 | 14.83 | 23.14 | 11.00 | 89.7 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.68 | 12.53 | 18.65 | 5.00 | 143.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.53 | 12.44 | 19.97 | 2.00 | 85.8 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.31 | 10.40 | 15.53 | 4.00 | 156.0 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.69 | 22.18 | 35.16 | 11.00 | 180.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.78 | 12.16 | 20.70 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.66 | 7.83 | 11.64 | 2.00 | 70.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.11 | 20.74 | 33.83 | 3.00 | 90.4 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.87 | 13.85 | 21.36 | 0.00 | 91.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.47 | 12.67 | 20.47 | 2.00 | 78.1 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.79 | 11.36 | 18.08 | 5.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.17 | 10.70 | 18.60 | 0.00 | 50.3 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.09
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.55 | 12.04 | 19.11 | 6.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.22 | 15.97 | 25.11 | 6.00 | 89.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.52 | 13.37 | 22.07 | 2.00 | 90.3 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.14 | 11.44 | 17.78 | 3.00 | 90.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.93 | 11.43 | 18.83 | 14.00 | 85.6 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.21 | 19.16 | 32.59 | 9.00 | 80.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.60 | 13.30 | 22.07 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.42 | 6.82 | 10.55 | 11.00 | 56.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.24 | 32.79 | 9.00 | 90.4 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.01 | 10.73 | 17.59 | 2.00 | 82.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.52 | 10.58 | 18.07 | 12.00 | 71.5 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.17 | 8.49 | 15.49 | 7.00 | 36.7 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.99
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.23 | 11.90 | 18.87 | 0.00 | 83.9 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.24 | 14.70 | 23.55 | 1.00 | 88.5 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.02 | 14.17 | 22.59 | 2.00 | 90.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.55 | 12.81 | 20.33 | 0.00 | 89.8 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.38 | 9.61 | 15.17 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.18 | 9.31 | 14.71 | 0.00 | 84.8 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.25 | 21.08 | 34.93 | 0.00 | 90.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.97 | 11.94 | 19.73 | 2.00 | 81.5 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.21 | 13.01 | 2.00 | 67.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.71 | 20.14 | 33.15 | 14.00 | 90.6 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.11 | 12.52 | 20.97 | 9.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.85 | 12.42 | 20.26 | 0.00 | 86.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 3.98 | 11.83 | 19.56 | 2.00 | 89.9 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.21 | 9.62 | 16.06 | 2.00 | 74.5 | 83.0 |