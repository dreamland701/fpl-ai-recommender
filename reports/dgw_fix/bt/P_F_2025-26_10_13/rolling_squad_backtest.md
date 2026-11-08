# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 257.46
- Total actual points: 176.00
- Average predicted points: 64.37
- Average actual points: 44.00
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
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Jean-Philippe Mateta
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 64.73
- Actual score: 76.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 11.92 | 19.43 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.04 | 9.27 | 15.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 15.50 | 24.51 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.85 | 23.93 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.95 | 13.43 | 21.51 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 13.17 | 21.55 | 3.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.58 | 12.12 | 19.32 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.84 | 15.52 | 24.25 | 9.00 | 90.0 | 89.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.31 | 11.73 | 18.30 | 6.00 | 78.5 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.58 | 10.96 | 17.13 | 2.00 | 86.6 | 61.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.34 | 19.87 | 30.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.53 | 18.05 | 29.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.45 | 16.21 | 27.79 | 10.00 | 73.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.57 | 14.23 | 22.41 | 9.00 | 86.7 | 61.0 |
| Bench 2 | Bench | Dominik Szoboszlai | MID | 12 | 6.5 | 4.12 | 12.11 | 19.22 | 2.00 | 82.5 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.29
- Actual score: 22.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Dominik Szoboszlai -> Moisés Caicedo Corozo (projected gain 1.80, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 11.64 | 18.89 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.32 | 9.52 | 15.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.15 | 27.15 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.30 | 15.05 | 23.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.17 | 12.18 | 19.66 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.94 | 11.91 | 19.34 | 1.00 | 77.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.32 | 11.59 | 18.69 | 1.00 | 89.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.48 | 15.29 | 23.51 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.4 | 3.63 | 10.50 | 16.62 | 2.00 | 66.3 | 84.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.22 | 15.76 | 1.00 | 71.3 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 8.1 | 5.90 | 17.79 | 28.83 | 0.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.57 | 17.62 | 30.05 | 2.00 | 85.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.46 | 13.92 | 21.33 | 7.00 | 67.3 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.38 | 13.69 | 21.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.50 | 12.47 | 20.07 | 3.00 | 77.3 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 1.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 67.29
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.99).
- Transfer: Danny Welbeck -> Igor Thiago Nascimento Rodrigues (projected gain 3.02, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.99).
- Autosub: Marc Guéhi replaced Antoine Semenyo.
- Autosub: Junior Kroupi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 11.02 | 17.92 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.22 | 9.29 | 15.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.70 | 13.35 | 21.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.79 | 12.54 | 19.95 | 3.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.53 | 11.35 | 18.18 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 8 | 5.0 | 3.51 | 9.40 | 15.71 | 5.00 | 47.2 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.46 | 9.29 | 16.67 | 0.00 | 47.9 | 0.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.17 | 14.50 | 23.20 | 1.00 | 69.9 | 59.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 4.68 | 13.56 | 21.24 | 4.00 | 86.8 | 90.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 2.66 | 7.73 | 12.90 | 2.00 | 41.3 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.47 | 18.82 | 31.40 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 6.77 | 18.73 | 29.30 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 5.47 | 15.47 | 25.21 | 0.00 | 85.0 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.47 | 12.47 | 18.84 | 0.00 | 77.9 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.07 | 20.47 | 3.00 | 73.6 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 65.15
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.67) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Morgan Rogers (projected gain 7.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.67) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 10.17 | 16.81 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.12 | 9.03 | 14.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.92 | 11.81 | 18.97 | 2.00 | 78.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.95 | 11.50 | 19.05 | 0.00 | 87.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.50 | 18.30 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.01 | 11.12 | 18.66 | 0.00 | 75.2 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 0.56 | 4.10 | 8.87 | 0.00 | 16.3 | 0.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.5 | 6.42 | 16.71 | 24.99 | 13.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.16 | 20.35 | 6.00 | 53.9 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.42 | 8.86 | 14.63 | 1.00 | 53.0 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.35 | 18.76 | 30.99 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 6.9 | 5.91 | 15.42 | 23.84 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.71 | 14.67 | 23.30 | 1.00 | 73.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.93 | 10.78 | 18.91 | 2.00 | 66.5 | 79.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 2.57 | 8.48 | 15.43 | 1.00 | 34.2 | 90.0 |