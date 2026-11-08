# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 283.69
- Total actual points: 251.00
- Average predicted points: 70.92
- Average actual points: 62.75
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
- Predicted score: 58.61
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.30 | 9.69 | 16.15 | 6.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.19 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.10 | 14.32 | 22.50 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.65 | 11.08 | 18.82 | 1.00 | 78.4 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.86 | 11.05 | 17.21 | 1.00 | 59.2 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.47 | 10.06 | 15.63 | 0.00 | 80.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.11 | 8.05 | 13.07 | 2.00 | 57.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.53 | 18.62 | 30.40 | 7.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.69 | 13.62 | 22.99 | 6.00 | 83.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.80 | 7.52 | 11.50 | 2.00 | 63.8 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.43 | 19.05 | 32.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.08 | 14.41 | 23.43 | 4.00 | 79.2 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.63 | 13.05 | 20.45 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.55 | 12.69 | 20.16 | 1.00 | 84.1 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.27 | 12.28 | 20.18 | 1.00 | 76.6 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.14
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.46, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Autosub: Mateus Mané replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.55 | 17.28 | 9.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.08 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.20 | 14.69 | 23.21 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.75 | 12.47 | 18.69 | 5.00 | 143.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.64 | 12.46 | 20.14 | 2.00 | 84.9 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.37 | 10.50 | 15.80 | 4.00 | 155.9 | 180.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.70 | 8.00 | 13.43 | 4.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.69 | 22.15 | 35.15 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.89 | 12.30 | 20.84 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 2.70 | 7.99 | 11.91 | 2.00 | 70.5 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.20 | 20.98 | 34.05 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.02 | 14.07 | 21.54 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.55 | 12.77 | 20.67 | 2.00 | 77.5 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.83 | 11.34 | 18.19 | 5.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.34 | 10.87 | 19.04 | 0.00 | 50.2 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.88
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.70 | 12.11 | 19.25 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.30 | 15.98 | 25.21 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.54 | 13.21 | 21.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.19 | 11.49 | 17.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.93 | 11.38 | 18.89 | 14.00 | 84.4 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.59 | 7.27 | 12.66 | 6.00 | 61.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.24 | 19.18 | 32.58 | 9.00 | 80.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.36 | 22.12 | 2.00 | 84.2 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.45 | 6.96 | 10.80 | 11.00 | 56.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.88 | 20.11 | 32.82 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.19 | 11.04 | 17.95 | 2.00 | 81.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.64 | 10.54 | 18.11 | 12.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.19 | 8.65 | 15.69 | 7.00 | 36.8 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.71 | 8.21 | 14.40 | 1.00 | 48.6 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.05
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.73) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.73) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.25 | 11.77 | 18.73 | 0.00 | 83.0 | 0.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.29 | 14.57 | 23.44 | 1.00 | 88.0 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.07 | 14.15 | 22.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.61 | 12.77 | 20.40 | 0.00 | 90.0 | 0.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.28 | 9.44 | 14.94 | 0.00 | 84.5 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.37 | 9.36 | 14.87 | 1.00 | 78.5 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.31 | 21.06 | 34.96 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.06 | 11.99 | 19.86 | 2.00 | 80.2 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.18 | 8.50 | 13.39 | 2.00 | 67.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.77 | 20.11 | 33.20 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.22 | 12.57 | 21.25 | 9.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.97 | 12.51 | 20.52 | 0.00 | 85.7 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.09 | 11.96 | 19.87 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.28 | 9.59 | 16.15 | 2.00 | 74.0 | 83.0 |