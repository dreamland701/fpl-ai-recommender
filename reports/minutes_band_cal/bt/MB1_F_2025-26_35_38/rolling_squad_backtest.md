# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 276.36
- Total actual points: 246.00
- Average predicted points: 69.09
- Average actual points: 61.50
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
- Predicted score: 57.93
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.39 | 9.86 | 16.33 | 6.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.65 | 13.01 | 20.67 | 6.00 | 83.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.03 | 11.48 | 17.86 | 1.00 | 62.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.70 | 11.06 | 18.78 | 1.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.57 | 10.16 | 15.56 | 0.00 | 79.5 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.24 | 8.50 | 13.86 | 2.00 | 59.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.61 | 18.74 | 30.54 | 7.00 | 78.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.82 | 13.78 | 23.00 | 6.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.79 | 7.39 | 11.45 | 2.00 | 67.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.93 | 17.72 | 30.24 | 5.00 | 83.2 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.09 | 14.32 | 23.23 | 4.00 | 80.7 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.63 | 12.69 | 19.96 | 1.00 | 83.2 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.32 | 12.32 | 20.16 | 1.00 | 77.9 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.14 | 11.72 | 18.53 | 4.00 | 83.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nico O'Reilly
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 92.52
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.84) beats the best remaining Triple Captain opportunity (8.43).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.43, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (16.84) beats the best remaining Triple Captain opportunity (8.43).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 10.84 | 17.51 | 9.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.75 | 13.38 | 21.40 | 11.00 | 83.1 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.99 | 12.80 | 19.21 | 5.00 | 149.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.75 | 12.59 | 20.14 | 2.00 | 84.9 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.47 | 10.49 | 15.73 | 4.00 | 158.6 | 180.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.87 | 8.47 | 14.21 | 4.00 | 74.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 13.74 | 20.80 | 33.27 | 11.00 | 166.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.91 | 12.25 | 20.74 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.75 | 8.05 | 12.02 | 2.00 | 73.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.66 | 19.34 | 31.94 | 3.00 | 83.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.54 | 12.65 | 20.51 | 2.00 | 79.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.48 | 12.48 | 19.47 | 0.00 | 83.1 | 0.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.95 | 11.46 | 18.17 | 5.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.44 | 11.14 | 19.37 | 0.00 | 53.3 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.85
- Actual score: 78.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.25 | 19.37 | 6.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.79 | 14.53 | 23.30 | 6.00 | 83.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.05 | 11.50 | 18.91 | 14.00 | 84.3 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.69 | 10.03 | 15.93 | 3.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 2.59 | 8.26 | 14.32 | 2.00 | 54.2 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.75 | 7.74 | 13.42 | 6.00 | 64.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.39 | 19.45 | 32.76 | 9.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.82 | 13.48 | 22.14 | 2.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.54 | 7.16 | 11.05 | 11.00 | 58.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.40 | 18.76 | 30.88 | 9.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.68 | 12.24 | 19.75 | 5.00 | 78.4 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.25 | 10.99 | 17.84 | 2.00 | 81.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.71 | 10.81 | 18.48 | 12.00 | 74.1 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.86 | 8.68 | 15.01 | 1.00 | 51.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.06
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Enzo Fernández (projected gain 2.11, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.42 | 12.06 | 18.98 | 0.00 | 82.5 | 0.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.84 | 13.24 | 21.61 | 1.00 | 81.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.61 | 12.74 | 20.64 | 2.00 | 83.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.66 | 9.97 | 16.23 | 0.00 | 71.8 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.50 | 9.64 | 15.28 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Jaydee Canvot | DEF | 8 | 4.5 | 3.37 | 9.50 | 14.88 | 0.00 | 83.9 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.87 | 19.70 | 33.09 | 0.00 | 83.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.17 | 12.15 | 19.87 | 2.00 | 79.7 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 3.18 | 8.44 | 13.40 | 2.00 | 70.3 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.29 | 18.69 | 31.20 | 14.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.63 | 13.08 | 20.66 | 0.00 | 80.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.08 | 12.59 | 20.49 | 0.00 | 84.9 | 0.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 4.25 | 11.57 | 18.84 | 1.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.33 | 9.64 | 16.12 | 2.00 | 75.4 | 83.0 |