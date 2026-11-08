# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 267.26
- Total actual points: 208.00
- Average predicted points: 66.81
- Average actual points: 52.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW9 are included before the first simulated week.
- League-average scores were not available for this run.

## GW10

- Train rows: 167841
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 65.98
- Actual score: 69.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.43 | 12.06 | 19.43 | 6.00 | 93.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.00 | 9.07 | 15.23 | 2.00 | 92.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.58 | 15.56 | 24.45 | 12.00 | 93.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.11 | 14.92 | 24.09 | 10.00 | 94.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.25 | 14.17 | 22.42 | 6.00 | 89.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.62 | 12.21 | 19.36 | 2.00 | 92.8 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.94 | 12.11 | 19.90 | 5.00 | 83.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.66 | 12.90 | 20.15 | 2.00 | 82.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.77 | 12.70 | 19.79 | 6.00 | 86.1 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.79 | 11.56 | 18.23 | 2.00 | 70.3 | 61.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.80 | 20.46 | 31.34 | 2.00 | 127.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.86 | 17.99 | 30.98 | 10.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.47 | 17.65 | 29.08 | 2.00 | 99.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.63 | 14.45 | 22.88 | 9.00 | 88.0 | 61.0 |
| Bench 2 | Bench | Cody Gakpo | MID | 12 | 7.6 | 4.60 | 13.51 | 21.70 | 3.00 | 71.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 59.12
- Actual score: 31.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 2.07, hit 0)
- Autosub: Danny Welbeck replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.08 | 11.84 | 19.05 | 1.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.27 | 9.31 | 15.37 | 2.00 | 93.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.42 | 17.21 | 27.25 | 1.00 | 95.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.36 | 15.18 | 23.84 | 0.00 | 91.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.11 | 12.60 | 20.22 | 1.00 | 81.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.34 | 11.59 | 18.66 | 1.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.71 | 11.28 | 18.40 | 1.00 | 87.6 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.08 | 12.29 | 19.23 | 1.00 | 85.2 | 27.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.02 | 12.01 | 18.73 | 13.00 | 69.3 | 90.0 |
| Bench 2 | Autosub In | Danny Welbeck | FWD | 6 | 6.4 | 4.00 | 11.83 | 18.77 | 2.00 | 66.2 | 84.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.75 | 18.41 | 31.24 | 2.00 | 91.6 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 8.1 | 5.84 | 17.44 | 28.14 | 0.00 | 102.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.77 | 15.43 | 23.85 | 7.00 | 70.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.51 | 13.87 | 21.48 | 2.00 | 97.7 | 90.0 |
| Bench 3 | Bench | Cody Gakpo | MID | 12 | 7.6 | 3.93 | 12.67 | 20.93 | 1.00 | 74.9 | 34.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 69.32
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.04) beats the best remaining Triple Captain opportunity (8.30).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 2.19, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (7.04) beats the best remaining Triple Captain opportunity (8.30).
- Autosub: Junior Kroupi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.90 | 11.35 | 18.43 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.16 | 9.04 | 14.80 | 2.00 | 91.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.28 | 13.55 | 22.77 | 14.00 | 93.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.85 | 13.50 | 21.25 | 5.00 | 97.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 13.30 | 21.22 | 3.00 | 104.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.42 | 11.60 | 19.21 | 5.00 | 28.1 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.54 | 11.20 | 18.05 | 0.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 4.89 | 13.93 | 21.78 | 4.00 | 92.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 3.98 | 11.89 | 19.02 | 8.00 | 68.6 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.79 | 11.45 | 19.25 | 2.00 | 58.7 | 85.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 7.04 | 19.02 | 29.68 | 1.00 | 110.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.41 | 18.53 | 30.91 | 2.00 | 97.0 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.73 | 14.08 | 23.62 | 2.00 | 45.0 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.67 | 13.06 | 19.61 | 0.00 | 82.0 | 0.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 4 | 8.0 | 3.72 | 10.74 | 17.52 | 0.00 | 60.6 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 72.84
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.21) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.21) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.43 | 10.51 | 17.33 | 3.00 | 82.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.06 | 8.85 | 14.39 | 1.00 | 89.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.22 | 13.89 | 22.72 | 1.00 | 93.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.21 | 12.62 | 20.14 | 2.00 | 84.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.15 | 11.62 | 19.37 | 0.00 | 78.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.99 | 11.60 | 19.29 | 0.00 | 87.0 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.0 | 3.52 | 10.56 | 18.41 | 6.00 | 71.8 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 6.86 | 17.58 | 26.08 | 13.00 | 102.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.5 | 4.24 | 12.31 | 19.89 | 2.00 | 82.0 | 64.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.89 | 11.44 | 19.20 | 1.00 | 61.6 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.31 | 18.59 | 30.60 | 0.00 | 97.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 6.9 | 6.15 | 15.54 | 23.91 | 3.00 | 107.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.82 | 15.27 | 24.39 | 1.00 | 75.1 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.40 | 12.82 | 20.87 | 14.00 | 63.8 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.74 | 10.02 | 16.29 | -2.00 | 50.7 | 37.0 |