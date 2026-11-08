# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 268.95
- Total actual points: 267.00
- Average predicted points: 67.24
- Average actual points: 66.75
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.93
- Actual score: 41.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.13 | 12.43 | 19.67 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 3.09 | 9.11 | 14.82 | 2.00 | 83.3 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.45 | 16.11 | 24.50 | 6.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.98 | 15.33 | 24.22 | 1.00 | 91.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.07 | 11.82 | 19.20 | -1.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.92 | 11.69 | 18.88 | 1.00 | 83.7 | 45.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.83 | 11.61 | 19.02 | 4.00 | 78.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.97 | 14.93 | 23.40 | 2.00 | 87.0 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.01 | 14.65 | 23.78 | 6.00 | 86.1 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.61 | 10.97 | 19.14 | 8.00 | 33.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.60 | 20.18 | 32.97 | 5.00 | 95.9 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.01 | 15.07 | 24.04 | 4.00 | 85.3 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.69 | 14.02 | 23.11 | 2.00 | 75.6 | 74.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.82 | 13.75 | 21.16 | 4.00 | 96.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.60 | 13.75 | 21.92 | 1.00 | 83.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 79.02
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.63) beats the best remaining Bench Boost opportunity (15.82).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Neco Williams -> Jan Paul van Hecke (projected gain 0.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.63) beats the best remaining Bench Boost opportunity (15.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.25 | 12.22 | 20.29 | 9.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.74 | 8.18 | 13.71 | 2.00 | 83.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.72 | 16.13 | 25.79 | 11.00 | 95.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 6.03 | 14.79 | 23.07 | 15.00 | 141.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.88 | 13.72 | 22.71 | 2.00 | 90.6 | 90.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 6 | 4.6 | 4.41 | 11.65 | 19.23 | 6.00 | 86.9 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.47 | 10.08 | 17.01 | 4.00 | 82.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.64 | 14.47 | 23.94 | 2.00 | 66.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.58 | 13.37 | 22.64 | 2.00 | 85.9 | 90.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.24 | 12.38 | 21.93 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.97 | 20.73 | 34.17 | 3.00 | 82.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.47 | 15.79 | 25.43 | 12.00 | 128.4 | 180.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.67 | 13.87 | 23.49 | 0.00 | 73.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.53 | 13.21 | 21.74 | 2.00 | 84.3 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 12.83 | 20.08 | 0.00 | 91.7 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.00
- Actual score: 67.00
- League average score: 0.00
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 2.90, hit 0)
- Autosub outfielders: Konstantinos Mavropanos.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.59 | 12.56 | 20.34 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.77 | 8.31 | 13.72 | 5.00 | 82.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.00 | 16.32 | 26.24 | 6.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.31 | 15.60 | 25.70 | 2.00 | 109.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.06 | 12.50 | 20.78 | 14.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.66 | 10.69 | 17.50 | 3.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 3.29 | 9.85 | 16.91 | 2.00 | 78.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.51 | 13.59 | 22.89 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.15 | 12.68 | 21.48 | 2.00 | 82.0 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.29 | 12.39 | 20.41 | 0.00 | 79.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.43 | 33.21 | 9.00 | 101.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.92 | 17.55 | 28.38 | 1.00 | 110.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.26 | 13.51 | 22.13 | 1.00 | 75.6 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.06 | 11.87 | 19.83 | 12.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.75 | 8.33 | 14.42 | 1.00 | 62.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.99
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Jan Paul van Hecke -> Marcos Senesi Barón (projected gain 1.48, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.93) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Konstantinos Mavropanos, João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.33 | 12.74 | 20.70 | 0.00 | 88.0 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 3.06 | 8.60 | 13.99 | 7.00 | 84.8 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.38 | 15.37 | 24.73 | 2.00 | 95.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.35 | 15.26 | 24.78 | 1.00 | 92.4 | 45.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 5.02 | 14.36 | 23.15 | 0.00 | 93.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.51 | 13.16 | 21.60 | 2.00 | 90.8 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.00 | 11.05 | 17.70 | 8.00 | 86.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.80 | 14.13 | 23.10 | 2.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.21 | 11.79 | 19.74 | 12.00 | 83.0 | 90.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.03 | 9.00 | 15.11 | 1.00 | 62.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.73 | 34.18 | 14.00 | 102.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.16 | 14.96 | 24.36 | 6.00 | 86.9 | 57.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 4.29 | 13.41 | 21.77 | 0.00 | 89.4 | 0.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.14 | 12.58 | 20.71 | 1.00 | 72.7 | 32.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.9 | 2.67 | 7.85 | 14.19 | 0.00 | 44.9 | 0.0 |