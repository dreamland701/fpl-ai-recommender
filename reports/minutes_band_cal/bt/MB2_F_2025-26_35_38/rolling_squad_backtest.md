# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 276.21
- Total actual points: 245.00
- Average predicted points: 69.05
- Average actual points: 61.25
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
- Predicted score: 57.94
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.36 | 9.83 | 16.37 | 6.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.01 | 0.00 | 0.02 | 0.00 | 2.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.76 | 13.29 | 21.01 | 6.00 | 83.5 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.08 | 11.63 | 18.09 | 1.00 | 63.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.67 | 11.03 | 18.81 | 1.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.49 | 10.02 | 15.34 | 0.00 | 78.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.29 | 8.65 | 14.09 | 2.00 | 60.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.58 | 18.71 | 30.57 | 7.00 | 76.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.73 | 13.64 | 22.78 | 6.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.77 | 7.36 | 11.40 | 2.00 | 67.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.03 | 18.00 | 30.58 | 5.00 | 83.5 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.06 | 14.29 | 23.27 | 4.00 | 79.6 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.54 | 12.54 | 19.74 | 1.00 | 82.1 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.29 | 12.29 | 20.20 | 1.00 | 76.8 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.24 | 12.00 | 18.87 | 4.00 | 83.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 93.07
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.05) beats the best remaining Triple Captain opportunity (8.56).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.33, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.05) beats the best remaining Triple Captain opportunity (8.56).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.72 | 10.70 | 17.31 | 9.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.86 | 13.67 | 21.74 | 11.00 | 83.5 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.95 | 12.76 | 19.15 | 5.00 | 150.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.67 | 12.45 | 19.94 | 2.00 | 83.8 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.41 | 10.47 | 15.77 | 4.00 | 156.4 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.85 | 8.43 | 14.15 | 4.00 | 74.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 13.95 | 21.09 | 33.61 | 11.00 | 166.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.88 | 12.23 | 20.79 | 2.00 | 77.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.73 | 8.01 | 11.96 | 2.00 | 73.5 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.77 | 19.63 | 32.28 | 3.00 | 83.5 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.59 | 12.76 | 19.81 | 0.00 | 83.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.51 | 12.63 | 20.56 | 2.00 | 77.9 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.87 | 11.32 | 17.97 | 5.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.47 | 11.28 | 19.58 | 0.00 | 54.3 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.84
- Actual score: 78.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.71 | 12.10 | 19.15 | 6.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.90 | 14.81 | 23.64 | 6.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.97 | 11.35 | 18.69 | 14.00 | 83.2 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.80 | 10.32 | 16.28 | 3.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.63 | 8.40 | 14.53 | 2.00 | 55.1 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.73 | 7.71 | 13.37 | 6.00 | 64.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.31 | 19.29 | 32.54 | 9.00 | 78.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.74 | 13.33 | 21.92 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.58 | 7.29 | 11.25 | 11.00 | 59.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.51 | 19.05 | 31.22 | 9.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.65 | 12.21 | 19.79 | 5.00 | 77.2 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.17 | 10.83 | 17.62 | 2.00 | 80.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.69 | 10.78 | 18.43 | 12.00 | 74.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.90 | 8.81 | 15.22 | 1.00 | 52.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.36
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaydee Canvot -> Marc Guéhi (projected gain 2.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.33 | 11.88 | 18.74 | 0.00 | 81.5 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 13.53 | 21.97 | 1.00 | 81.6 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.71 | 13.04 | 21.00 | 2.00 | 83.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.26 | 11.71 | 18.89 | 0.00 | 83.4 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.64 | 9.94 | 16.17 | 0.00 | 71.9 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.47 | 9.62 | 15.31 | 1.00 | 78.3 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.97 | 20.00 | 33.45 | 0.00 | 83.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.07 | 11.97 | 19.63 | 2.00 | 78.6 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.16 | 8.41 | 13.34 | 2.00 | 70.4 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.39 | 18.99 | 31.57 | 14.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.54 | 12.91 | 20.41 | 0.00 | 79.3 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.98 | 12.41 | 20.25 | 0.00 | 83.9 | 0.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.30 | 9.62 | 16.15 | 2.00 | 74.2 | 83.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.62 | 7.95 | 14.49 | 0.00 | 56.4 | 0.0 |