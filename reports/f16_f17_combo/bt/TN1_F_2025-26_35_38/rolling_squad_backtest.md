# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 285.29
- Total actual points: 253.00
- Average predicted points: 71.32
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
- Predicted score: 59.29
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.39 | 9.90 | 16.38 | 6.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.17 | 0.22 | 0.67 | 0.00 | 2.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.49 | 22.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.94 | 11.17 | 17.35 | 1.00 | 60.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.73 | 11.13 | 18.85 | 1.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.49 | 10.09 | 15.59 | 0.00 | 81.1 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.11 | 8.11 | 13.36 | 2.00 | 56.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.60 | 18.73 | 30.51 | 7.00 | 77.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.76 | 13.74 | 23.03 | 6.00 | 84.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.78 | 7.32 | 11.21 | 2.00 | 66.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.44 | 19.19 | 32.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.10 | 14.37 | 23.28 | 4.00 | 80.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.67 | 13.20 | 20.53 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.56 | 12.64 | 20.00 | 1.00 | 85.3 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.31 | 12.34 | 20.19 | 1.00 | 77.4 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.28
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.82) beats the best remaining Triple Captain opportunity (9.03).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.45, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.82) beats the best remaining Triple Captain opportunity (9.03).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.75 | 17.51 | 9.00 | 82.5 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.35 | 0.00 | 2.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.28 | 14.88 | 23.42 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.82 | 12.58 | 18.80 | 5.00 | 144.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.71 | 12.58 | 20.22 | 2.00 | 87.4 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.02 | 10.19 | 15.44 | 4.00 | 143.9 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.82 | 8.31 | 13.86 | 4.00 | 72.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.72 | 22.22 | 35.21 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.94 | 12.32 | 20.84 | 2.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.73 | 7.94 | 11.73 | 2.00 | 72.3 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.18 | 20.83 | 33.95 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.03 | 14.00 | 21.51 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.54 | 12.70 | 20.57 | 2.00 | 78.7 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.88 | 11.41 | 18.22 | 5.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.20 | 11.07 | 19.62 | 0.00 | 47.6 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.99
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.73 | 12.20 | 19.39 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.31 | 16.01 | 25.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.60 | 13.40 | 22.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.16 | 11.46 | 17.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.91 | 11.31 | 18.85 | 14.00 | 84.1 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.74 | 7.66 | 13.17 | 6.00 | 62.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.34 | 19.41 | 32.80 | 9.00 | 81.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.75 | 13.42 | 22.15 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.46 | 6.89 | 10.60 | 11.00 | 57.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.83 | 20.10 | 32.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.18 | 10.91 | 17.85 | 2.00 | 83.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.61 | 10.56 | 18.10 | 12.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.09 | 8.82 | 16.33 | 7.00 | 34.6 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.75 | 8.34 | 14.55 | 1.00 | 48.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.73
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.34 | 11.97 | 18.97 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.37 | 14.74 | 23.65 | 1.00 | 89.2 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.13 | 14.26 | 22.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.66 | 12.88 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.49 | 9.68 | 15.34 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.26 | 9.38 | 14.84 | 0.00 | 84.9 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.38 | 21.17 | 35.08 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.09 | 12.08 | 19.87 | 2.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.27 | 13.04 | 2.00 | 68.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.79 | 20.16 | 33.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.27 | 12.65 | 21.24 | 9.00 | 78.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.02 | 12.57 | 20.53 | 0.00 | 87.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.11 | 11.97 | 19.80 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.33 | 9.70 | 16.19 | 2.00 | 75.2 | 83.0 |