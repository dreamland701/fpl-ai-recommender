# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 242.84
- Total actual points: 211.00
- Average predicted points: 60.71
- Average actual points: 52.75
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
- Predicted score: 59.62
- Actual score: 70.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.01 | 10.89 | 17.61 | 6.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.62 | 7.97 | 13.47 | 2.00 | 95.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.10 | 14.09 | 22.05 | 12.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.55 | 13.26 | 21.42 | 10.00 | 95.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.71 | 12.65 | 19.99 | 6.00 | 87.0 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.49 | 10.76 | 17.67 | 5.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 4.05 | 10.63 | 16.85 | 2.00 | 93.8 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.99 | 12.14 | 19.13 | 2.00 | 88.3 | 61.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.20 | 11.60 | 18.11 | 2.00 | 77.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.31 | 11.48 | 17.90 | 6.00 | 81.1 | 81.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.25 | 18.92 | 28.92 | 2.00 | 127.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.25 | 16.15 | 27.82 | 10.00 | 72.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.79 | 15.61 | 25.76 | 2.00 | 100.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.13 | 12.94 | 20.46 | 9.00 | 87.0 | 61.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 4.07 | 11.96 | 19.21 | 3.00 | 64.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.33
- Actual score: 33.00
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 2.19, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.72 | 10.81 | 17.45 | 1.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.88 | 8.24 | 13.69 | 2.00 | 96.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.87 | 15.49 | 24.42 | 1.00 | 95.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 4.77 | 13.52 | 21.17 | 0.00 | 93.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 3.65 | 11.19 | 17.97 | 1.00 | 78.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.84 | 10.16 | 16.37 | 1.00 | 89.5 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.30 | 10.01 | 16.27 | 1.00 | 87.6 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.71 | 11.16 | 17.44 | 1.00 | 73.2 | 27.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.56 | 10.64 | 16.58 | 13.00 | 63.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 3.56 | 10.54 | 16.73 | 2.00 | 67.2 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.2 | 5.33 | 17.09 | 29.03 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.20 | 15.53 | 25.07 | 0.00 | 105.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.19 | 13.62 | 21.01 | 7.00 | 67.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.14 | 12.79 | 19.75 | 2.00 | 95.7 | 90.0 |
| Bench 3 | Bench | Cody Gakpo | MID | 12 | 7.6 | 3.49 | 11.28 | 18.64 | 1.00 | 68.9 | 34.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 63.14
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.40) beats the best remaining Triple Captain opportunity (7.55).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.23, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (6.40) beats the best remaining Triple Captain opportunity (7.55).
- Autosub: Junior Kroupi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.43 | 10.01 | 16.32 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.75 | 7.91 | 13.02 | 2.00 | 93.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.54 | 12.60 | 19.81 | 5.00 | 94.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.93 | 12.60 | 21.20 | 14.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.69 | 12.24 | 19.47 | 3.00 | 102.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.85 | 10.19 | 16.87 | 5.00 | 47.1 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.05 | 9.73 | 15.65 | 0.00 | 92.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 4.49 | 12.77 | 19.94 | 4.00 | 90.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 3.53 | 10.56 | 16.90 | 8.00 | 69.6 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.27 | 9.76 | 16.22 | 2.00 | 40.7 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.08 | 17.61 | 29.43 | 2.00 | 93.0 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 6.40 | 17.21 | 26.85 | 1.00 | 111.9 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.27 | 12.71 | 21.29 | 2.00 | 55.0 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.14 | 11.54 | 17.24 | 0.00 | 79.0 | 0.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 4 | 8.0 | 3.17 | 10.90 | 18.30 | 0.00 | 80.6 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 66.75
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.05 | 9.38 | 15.50 | 3.00 | 79.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.72 | 7.87 | 12.84 | 1.00 | 91.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.77 | 12.62 | 20.68 | 1.00 | 92.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.77 | 11.30 | 18.02 | 2.00 | 80.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.56 | 10.34 | 17.26 | 0.00 | 86.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.69 | 10.31 | 17.20 | 0.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.0 | 3.10 | 9.30 | 16.27 | 6.00 | 67.8 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 6.55 | 16.73 | 24.75 | 13.00 | 99.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.5 | 3.82 | 11.10 | 17.95 | 2.00 | 77.0 | 64.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.56 | 9.93 | 16.60 | 1.00 | 49.6 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.12 | 18.06 | 29.75 | 0.00 | 91.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 6.9 | 5.79 | 14.56 | 22.35 | 3.00 | 105.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.26 | 13.58 | 21.70 | 1.00 | 72.1 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 3.96 | 11.54 | 18.77 | 14.00 | 64.8 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.49 | 8.87 | 14.58 | -2.00 | 35.7 | 37.0 |