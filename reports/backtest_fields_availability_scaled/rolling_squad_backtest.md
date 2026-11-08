# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 279.03
- Total actual points: 257.00
- Average predicted points: 69.76
- Average actual points: 64.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 62.40
- Actual score: 43.00
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.17 | 12.56 | 19.87 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.76 | 8.59 | 14.70 | 2.00 | 76.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.45 | 16.11 | 24.50 | 6.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.98 | 15.33 | 24.22 | 1.00 | 91.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 4.73 | 14.02 | 22.48 | 1.00 | 69.7 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 13 | 5.1 | 4.21 | 12.77 | 20.93 | 4.00 | 78.8 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.30 | 12.50 | 20.31 | -1.00 | 82.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.18 | 15.13 | 24.56 | 6.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.3 | 3.57 | 9.83 | 15.10 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.01 | 9.46 | 16.81 | 6.00 | 31.1 | 69.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.60 | 20.18 | 32.97 | 5.00 | 95.9 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.14 | 16.28 | 26.23 | 0.00 | 72.8 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.25 | 15.70 | 25.87 | 2.00 | 75.6 | 74.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.17 | 15.57 | 24.82 | 4.00 | 85.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.82 | 13.75 | 21.16 | 4.00 | 96.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Nico O'Reilly
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 85.24
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.08) beats the best remaining Bench Boost opportunity (15.53).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- League average score: 0.00
- Transfer: Konstantinos Mavropanos -> Jaydee Canvot (projected gain 0.49, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.08) beats the best remaining Bench Boost opportunity (15.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.25 | 12.22 | 20.29 | 9.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.59 | 15.75 | 0.00 | 91.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 7.10 | 17.42 | 27.16 | 15.00 | 141.7 | 180.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.19 | 17.13 | 25.96 | 5.00 | 123.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.72 | 16.13 | 25.79 | 11.00 | 95.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.88 | 13.72 | 22.71 | 2.00 | 90.6 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 5.28 | 13.22 | 19.87 | 4.00 | 92.9 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.70 | 11.00 | 17.83 | 2.00 | 73.1 | 78.0 |
| Bench 3 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.44 | 10.72 | 17.73 | 2.00 | 66.8 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.3 | 3.26 | 9.48 | 14.40 | 2.00 | 81.2 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.97 | 20.73 | 34.17 | 3.00 | 82.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 7.97 | 19.46 | 31.35 | 12.00 | 128.4 | 180.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.32 | 15.79 | 26.75 | 0.00 | 73.9 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.46 | 13.52 | 24.39 | 0.00 | 46.4 | 0.0 |
| Bench 2 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 12.83 | 20.08 | 0.00 | 91.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 4.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.55
- Actual score: 71.00
- League average score: 0.00
- Transfer: Mohamed Salah -> Bukayo Saka (projected gain 3.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.59 | 12.56 | 20.34 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.98 | 3.66 | 6.62 | 0.00 | 31.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.00 | 16.32 | 26.24 | 6.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.31 | 15.60 | 25.70 | 2.00 | 109.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.11 | 12.63 | 20.99 | 14.00 | 87.5 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.31 | 12.05 | 18.73 | 3.00 | 88.9 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.3 | 3.80 | 11.71 | 19.93 | 2.00 | 72.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.66 | 14.03 | 23.64 | 2.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.18 | 9.69 | 16.17 | 8.00 | 67.1 | 75.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 3.29 | 9.39 | 14.70 | 11.00 | 72.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.43 | 33.21 | 9.00 | 101.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.92 | 17.55 | 28.38 | 1.00 | 110.5 | 55.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.9 | 5.19 | 14.40 | 22.72 | 10.00 | 43.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.82 | 13.57 | 23.86 | 7.00 | 26.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.58 | 10.82 | 18.73 | 1.00 | 62.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 4.10 -> 3.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 69.84
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Carlos Henrique Casimiro -> Dominik Szoboszlai (projected gain 3.24, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.38 | 12.87 | 20.91 | 0.00 | 88.0 | 0.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.12 | 8.53 | 14.58 | 0.00 | 29.7 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.38 | 15.37 | 24.73 | 2.00 | 95.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.35 | 15.26 | 24.78 | 1.00 | 92.4 | 45.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 5.02 | 14.36 | 23.15 | 0.00 | 93.1 | 0.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 4.32 | 12.21 | 20.02 | 0.00 | 82.1 | 0.0 |
| Bench 4 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.38 | 9.67 | 15.32 | 0.00 | 86.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.85 | 14.28 | 23.33 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.71 | 10.67 | 17.39 | 2.00 | 76.9 | 72.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 3.61 | 10.03 | 15.88 | 2.00 | 81.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.73 | 34.18 | 14.00 | 102.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.27 | 15.28 | 24.87 | 6.00 | 86.9 | 57.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 5.15 | 14.86 | 23.22 | 0.00 | 49.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.86 | 13.87 | 23.14 | 2.00 | 87.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.47 | 13.86 | 23.45 | 9.00 | 76.1 | 90.0 |