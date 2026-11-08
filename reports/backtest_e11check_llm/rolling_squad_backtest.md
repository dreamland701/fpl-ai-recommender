# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 215.62
- Total actual points: 277.00
- Average predicted points: 53.90
- Average actual points: 69.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 48.54
- Actual score: 39.00
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.43 | 11.23 | 17.37 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 2.49 | 8.40 | 13.55 | 1.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.88 | 12.73 | 20.12 | 1.00 | 91.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.35 | 12.11 | 18.50 | 6.00 | 93.5 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.37 | 10.52 | 16.90 | -1.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.1 | 3.25 | 10.49 | 16.44 | 1.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.23 | 10.41 | 16.62 | 4.00 | 78.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.01 | 12.35 | 19.98 | 6.00 | 86.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.87 | 12.13 | 19.30 | 2.00 | 87.0 | 87.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.92 | 9.04 | 14.05 | 5.00 | 77.2 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 5.30 | 16.18 | 26.97 | 5.00 | 95.9 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.01 | 12.67 | 20.54 | 4.00 | 85.3 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.79 | 12.62 | 21.01 | 2.00 | 75.6 | 74.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.70 | 12.15 | 18.82 | 1.00 | 83.3 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.1 | 3.53 | 11.59 | 17.59 | 2.00 | 92.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 1.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marc Guéhi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 63.96
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.66) beats the best remaining Bench Boost opportunity (11.96).
- League average score: 0.00
- Transfer: Kiernan Dewsbury-Hall -> Carlos Henrique Casimiro (projected gain 0.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.66) beats the best remaining Bench Boost opportunity (11.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.42 | 17.19 | 9.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 5.6 | 2.63 | 7.73 | 12.98 | 3.00 | 83.8 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.03 | 12.79 | 19.97 | 15.00 | 141.7 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.42 | 12.63 | 20.09 | 11.00 | 95.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.88 | 10.72 | 17.61 | 2.00 | 90.6 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.40 | 10.60 | 16.20 | 5.00 | 123.8 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.97 | 8.68 | 14.71 | 4.00 | 82.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.08 | 12.27 | 20.84 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.34 | 10.87 | 18.04 | 2.00 | 66.8 | 90.0 |
| Bench 4 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.51 | 7.21 | 11.95 | 1.00 | 51.6 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.97 | 16.73 | 28.17 | 3.00 | 82.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 5.27 | 13.09 | 20.93 | 12.00 | 128.4 | 180.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.77 | 12.17 | 20.59 | 0.00 | 73.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.03 | 12.11 | 19.94 | 2.00 | 84.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.93 | 11.73 | 18.48 | 0.00 | 91.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.33
- Actual score: 75.00
- League average score: 0.00
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 1.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.29 | 8.86 | 14.34 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 2.85 | 7.92 | 12.87 | 1.00 | 85.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.90 | 12.72 | 20.54 | 6.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.11 | 12.00 | 20.00 | 2.00 | 109.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.06 | 9.29 | 15.30 | 3.00 | 83.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 2.96 | 8.80 | 14.78 | 14.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 2.78 | 8.60 | 14.69 | 2.00 | 72.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.01 | 11.99 | 20.19 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.45 | 10.38 | 17.48 | 2.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.86 | 8.71 | 14.22 | 2.00 | 76.5 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.93 | 16.83 | 27.41 | 9.00 | 101.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.92 | 13.85 | 22.48 | 1.00 | 110.5 | 55.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.42 | 10.36 | 17.37 | 9.00 | 84.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.36 | 9.47 | 15.73 | 12.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.13 | 12.32 | 1.00 | 62.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.79
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.53) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Carlos Henrique Casimiro -> Ismaïla Sarr (projected gain 0.68, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.53) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Jordan Pickford replaced David Raya Martín.
- Autosub outfielders: Konstantinos Mavropanos, Igor Jesus Maciel da Cruz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.13 | 9.34 | 15.20 | 0.00 | 88.0 | 0.0 |
| Bench 1 | Autosub In | Jordan Pickford | GK | 9 | 5.6 | 2.55 | 7.60 | 12.16 | 2.00 | 84.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 4.15 | 12.26 | 20.28 | 1.00 | 92.4 | 45.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.18 | 11.77 | 19.23 | 2.00 | 95.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.62 | 11.06 | 18.15 | 0.00 | 93.1 | 0.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 3.39 | 9.25 | 15.13 | 0.00 | 82.1 | 0.0 |
| Bench 3 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.90 | 7.85 | 12.50 | 8.00 | 86.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.80 | 10.93 | 17.80 | 2.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.41 | 9.79 | 16.34 | 12.00 | 83.0 | 90.0 |
| Bench 4 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.79 | 7.83 | 12.91 | 2.00 | 77.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.53 | 16.73 | 28.18 | 14.00 | 102.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.06 | 11.86 | 19.36 | 6.00 | 86.9 | 57.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 3.49 | 10.51 | 17.07 | 0.00 | 89.4 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.81 | 10.33 | 17.41 | 2.00 | 87.4 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 8 | 6.4 | 3.54 | 9.83 | 15.49 | 1.00 | 82.8 | 45.0 |