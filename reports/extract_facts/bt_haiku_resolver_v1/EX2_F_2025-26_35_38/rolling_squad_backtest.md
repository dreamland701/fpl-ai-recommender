# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 289.57
- Total actual points: 253.00
- Average predicted points: 72.39
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
- Predicted score: 61.07
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.42 | 9.98 | 16.47 | 6.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.08 | 0.00 | 0.23 | 0.00 | 3.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.19 | 14.54 | 22.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.32 | 12.11 | 19.12 | 1.00 | 68.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.80 | 11.33 | 19.09 | 1.00 | 81.8 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.49 | 10.09 | 15.58 | 0.00 | 81.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.12 | 8.14 | 13.38 | 2.00 | 56.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 7.28 | 20.69 | 33.60 | 7.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.78 | 13.80 | 23.07 | 6.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.78 | 7.32 | 11.21 | 2.00 | 66.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.38 | 19.09 | 32.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.13 | 14.47 | 23.39 | 4.00 | 80.8 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.60 | 13.08 | 20.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.57 | 12.67 | 20.02 | 1.00 | 85.3 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.34 | 12.42 | 20.25 | 1.00 | 77.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 97.04
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.73) beats the best remaining Triple Captain opportunity (9.24).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.40, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.73) beats the best remaining Triple Captain opportunity (9.24).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.77 | 17.51 | 9.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.27 | 14.86 | 23.37 | 11.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.73 | 12.65 | 20.30 | 2.00 | 87.7 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.77 | 12.52 | 18.70 | 5.00 | 143.4 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.68 | 10.72 | 16.34 | 4.00 | 165.8 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.83 | 8.35 | 13.90 | 4.00 | 72.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.63 | 22.16 | 35.06 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.98 | 12.45 | 20.99 | 2.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.71 | 7.89 | 11.66 | 2.00 | 72.0 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.53 | 21.81 | 35.65 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 5.03 | 14.01 | 21.51 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.56 | 12.77 | 20.65 | 2.00 | 78.9 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.88 | 11.40 | 18.20 | 5.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.16 | 10.95 | 20.02 | 0.00 | 45.6 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.93
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.72 | 12.20 | 19.37 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.03 | 0.00 | 0.07 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.30 | 16.01 | 25.26 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.59 | 13.40 | 22.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.16 | 11.46 | 17.89 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.92 | 11.36 | 18.91 | 14.00 | 84.2 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.74 | 7.67 | 13.18 | 6.00 | 63.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 7.03 | 21.33 | 35.88 | 9.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.77 | 13.48 | 22.21 | 2.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.45 | 6.87 | 10.57 | 11.00 | 57.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.08 | 32.74 | 9.00 | 90.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.17 | 10.89 | 17.80 | 2.00 | 82.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.65 | 10.68 | 18.24 | 12.00 | 71.3 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.19 | 9.06 | 16.62 | 7.00 | 36.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.77 | 8.40 | 14.62 | 1.00 | 49.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 71.53
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.34 | 11.99 | 18.97 | 0.00 | 83.9 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.37 | 14.76 | 23.64 | 1.00 | 88.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.11 | 14.22 | 22.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.66 | 12.89 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.50 | 9.69 | 15.35 | 1.00 | 79.0 | 90.0 |
| Bench 3 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.26 | 9.38 | 14.83 | 0.00 | 84.9 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.80 | 21.97 | 36.25 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.11 | 12.14 | 19.93 | 2.00 | 81.8 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.12 | 8.28 | 13.04 | 2.00 | 68.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.76 | 20.11 | 33.11 | 14.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.05 | 12.65 | 20.63 | 0.00 | 87.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.25 | 12.62 | 21.20 | 9.00 | 78.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.09 | 11.93 | 19.72 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.33 | 9.71 | 16.18 | 2.00 | 75.1 | 83.0 |