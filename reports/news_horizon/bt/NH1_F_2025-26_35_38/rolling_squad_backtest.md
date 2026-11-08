# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 283.92
- Total actual points: 253.00
- Average predicted points: 70.98
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
- Predicted score: 58.76
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.35 | 9.76 | 16.17 | 6.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.05 | 0.00 | 0.21 | 0.00 | 2.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.14 | 14.41 | 22.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.89 | 11.11 | 17.33 | 1.00 | 59.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.67 | 10.95 | 18.61 | 1.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.47 | 10.03 | 15.50 | 0.00 | 80.7 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.13 | 8.13 | 13.25 | 2.00 | 56.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.57 | 18.63 | 30.35 | 7.00 | 76.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.64 | 22.93 | 6.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.71 | 7.16 | 11.04 | 2.00 | 64.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.40 | 19.13 | 32.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.05 | 14.24 | 23.12 | 4.00 | 79.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.62 | 13.15 | 20.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.51 | 12.55 | 19.94 | 1.00 | 84.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.28 | 12.26 | 20.09 | 1.00 | 76.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.14
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.79) beats the best remaining Triple Captain opportunity (9.01).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.68 | 10.66 | 17.41 | 9.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.24 | 14.82 | 23.39 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.74 | 12.58 | 18.91 | 5.00 | 142.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.67 | 12.46 | 20.05 | 2.00 | 86.3 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.41 | 10.46 | 15.70 | 4.00 | 156.4 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.76 | 8.23 | 13.83 | 4.00 | 71.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.69 | 22.22 | 35.24 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.88 | 12.18 | 20.64 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.67 | 7.83 | 11.60 | 2.00 | 70.6 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.15 | 20.78 | 33.93 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 13.95 | 21.52 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.50 | 12.60 | 20.45 | 2.00 | 77.8 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.83 | 11.35 | 18.21 | 5.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.33 | 10.72 | 18.63 | 0.00 | 50.8 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.86
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.69 | 12.09 | 19.26 | 6.00 | 84.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.10 | 0.00 | 1.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.26 | 15.96 | 25.33 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.54 | 13.38 | 22.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.17 | 11.51 | 18.06 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.95 | 11.37 | 18.85 | 14.00 | 85.3 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.65 | 7.52 | 13.06 | 6.00 | 60.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.27 | 19.27 | 32.61 | 9.00 | 80.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.72 | 13.36 | 22.10 | 2.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.40 | 6.80 | 10.54 | 11.00 | 55.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.90 | 20.21 | 32.87 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.12 | 10.88 | 17.91 | 2.00 | 81.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.63 | 10.58 | 18.02 | 12.00 | 71.5 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.23 | 8.48 | 15.30 | 7.00 | 38.1 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.72 | 8.33 | 14.51 | 1.00 | 48.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.15
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.30 | 11.88 | 18.87 | 0.00 | 83.2 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.31 | 14.66 | 23.61 | 1.00 | 87.7 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.19 | 22.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.63 | 12.85 | 20.54 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.46 | 9.61 | 15.28 | 1.00 | 77.9 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.25 | 9.36 | 14.86 | 0.00 | 84.6 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.35 | 21.08 | 34.94 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.05 | 11.99 | 19.78 | 2.00 | 80.6 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.07 | 8.19 | 12.99 | 2.00 | 66.9 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.77 | 20.13 | 33.22 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.21 | 12.60 | 21.27 | 9.00 | 76.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.98 | 12.44 | 20.35 | 0.00 | 86.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.07 | 11.93 | 19.82 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.27 | 9.63 | 16.19 | 2.00 | 73.6 | 83.0 |