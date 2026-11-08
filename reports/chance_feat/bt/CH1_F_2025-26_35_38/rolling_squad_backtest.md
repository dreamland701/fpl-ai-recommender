# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.14
- Total actual points: 253.00
- Average predicted points: 71.03
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
- Predicted score: 58.73
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.34 | 9.73 | 16.15 | 6.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.28 | 0.38 | 0.86 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.14 | 14.40 | 22.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.91 | 11.12 | 17.32 | 1.00 | 59.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.65 | 10.93 | 18.59 | 1.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.46 | 10.02 | 15.52 | 0.00 | 80.3 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.11 | 8.10 | 13.25 | 2.00 | 56.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.56 | 18.61 | 30.35 | 7.00 | 76.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.70 | 13.62 | 22.92 | 6.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.69 | 7.15 | 11.05 | 2.00 | 63.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.14 | 32.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.04 | 14.22 | 23.11 | 4.00 | 79.1 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.63 | 13.15 | 20.53 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.51 | 12.55 | 19.93 | 1.00 | 84.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.27 | 12.24 | 20.08 | 1.00 | 76.4 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.27
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.83) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.60, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.83) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.68 | 10.66 | 17.39 | 9.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.09 | 0.58 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.82 | 23.38 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.81 | 12.60 | 18.87 | 5.00 | 143.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.64 | 12.43 | 20.06 | 2.00 | 85.6 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.38 | 10.45 | 15.71 | 4.00 | 155.7 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.81 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.73 | 22.23 | 35.22 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.86 | 12.16 | 20.63 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.66 | 7.82 | 11.61 | 2.00 | 70.3 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.79 | 33.93 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 13.96 | 21.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.49 | 12.58 | 20.45 | 2.00 | 77.5 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.84 | 11.36 | 18.21 | 5.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.29 | 10.67 | 18.61 | 0.00 | 50.0 | 0.0 |

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
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.68 | 12.08 | 19.25 | 6.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.02 | 0.05 | 0.00 | 1.3 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 15.98 | 25.30 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.59 | 13.41 | 22.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.19 | 11.53 | 18.04 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.94 | 11.36 | 18.85 | 14.00 | 85.1 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.53 | 13.06 | 6.00 | 61.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.27 | 19.26 | 32.61 | 9.00 | 80.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.35 | 22.10 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.42 | 6.81 | 10.53 | 11.00 | 55.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.90 | 20.21 | 32.88 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.14 | 10.90 | 17.89 | 2.00 | 82.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.61 | 10.55 | 18.02 | 12.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.16 | 8.42 | 15.35 | 7.00 | 36.6 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.51 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.19
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.30 | 11.88 | 18.85 | 0.00 | 83.2 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.33 | 14.67 | 23.59 | 1.00 | 88.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.19 | 22.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 12.85 | 20.51 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.46 | 9.60 | 15.27 | 1.00 | 77.9 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.25 | 9.36 | 14.84 | 0.00 | 84.7 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.34 | 21.07 | 34.94 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 11.98 | 19.77 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.08 | 8.20 | 12.99 | 2.00 | 67.2 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 20.14 | 33.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.22 | 12.61 | 21.28 | 9.00 | 76.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.95 | 12.41 | 20.36 | 0.00 | 85.6 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.08 | 11.95 | 19.81 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.29 | 9.63 | 16.16 | 2.00 | 73.9 | 83.0 |