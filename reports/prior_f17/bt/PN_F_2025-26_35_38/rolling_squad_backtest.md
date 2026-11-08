# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.39
- Total actual points: 253.00
- Average predicted points: 71.10
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
- Predicted score: 58.86
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.36 | 9.86 | 16.41 | 6.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.31 | 0.51 | 1.09 | 0.00 | 7.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.47 | 22.74 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.93 | 11.19 | 17.45 | 1.00 | 59.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.66 | 11.03 | 18.79 | 1.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.41 | 9.86 | 15.25 | 0.00 | 78.6 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.13 | 8.21 | 13.45 | 2.00 | 57.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.56 | 18.73 | 30.65 | 7.00 | 76.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.72 | 13.70 | 23.08 | 6.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.64 | 6.92 | 10.63 | 2.00 | 61.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.15 | 32.26 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.05 | 14.29 | 23.22 | 4.00 | 79.4 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.64 | 13.21 | 20.64 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.51 | 12.57 | 19.97 | 1.00 | 84.2 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.29 | 12.32 | 20.23 | 1.00 | 76.9 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.41
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.85) beats the best remaining Triple Captain opportunity (9.05).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.56, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.85) beats the best remaining Triple Captain opportunity (9.05).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.70 | 10.75 | 17.56 | 9.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.20 | 0.77 | 0.00 | 7.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.85 | 23.44 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.88 | 12.65 | 18.93 | 5.00 | 146.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.64 | 12.47 | 20.15 | 2.00 | 85.7 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.31 | 10.29 | 15.41 | 4.00 | 152.8 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.80 | 8.30 | 13.92 | 4.00 | 72.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.75 | 22.30 | 35.36 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.88 | 12.25 | 20.81 | 2.00 | 77.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.60 | 7.58 | 11.19 | 2.00 | 67.8 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.15 | 20.78 | 33.93 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.99 | 13.98 | 21.58 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.50 | 12.64 | 20.56 | 2.00 | 77.8 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.86 | 11.38 | 18.24 | 5.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.31 | 10.78 | 18.81 | 0.00 | 50.3 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.94
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.69 | 12.15 | 19.38 | 6.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.13 | 0.23 | 0.00 | 2.8 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.29 | 16.00 | 25.35 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.58 | 13.36 | 22.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.95 | 11.39 | 18.91 | 14.00 | 85.2 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.14 | 11.30 | 17.62 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.68 | 7.57 | 13.11 | 6.00 | 61.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.27 | 19.35 | 32.82 | 9.00 | 80.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.72 | 13.41 | 22.21 | 2.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.37 | 6.61 | 10.15 | 11.00 | 53.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.19 | 32.85 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.16 | 10.92 | 17.91 | 2.00 | 82.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.62 | 10.61 | 18.13 | 12.00 | 71.3 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.18 | 8.49 | 15.46 | 7.00 | 36.9 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.75 | 8.42 | 14.67 | 1.00 | 49.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.17
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.54) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.54) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.31 | 11.94 | 18.97 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.07 | 0.00 | 2.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.33 | 14.70 | 23.67 | 1.00 | 88.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.18 | 22.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 12.86 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.48 | 9.66 | 15.35 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.21 | 9.21 | 14.56 | 0.00 | 83.2 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.34 | 21.16 | 35.17 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.05 | 12.04 | 19.89 | 2.00 | 80.9 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.02 | 7.98 | 12.58 | 2.00 | 64.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.77 | 20.12 | 33.18 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.22 | 12.57 | 21.17 | 9.00 | 77.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.96 | 12.46 | 20.45 | 0.00 | 85.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.09 | 11.96 | 19.82 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.30 | 9.67 | 16.22 | 2.00 | 74.6 | 83.0 |