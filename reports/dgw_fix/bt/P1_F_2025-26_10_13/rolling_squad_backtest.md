# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 261.40
- Total actual points: 183.00
- Average predicted points: 65.35
- Average actual points: 45.75
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
- Vice captain: Jean-Philippe Mateta
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 64.73
- Actual score: 74.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 12.06 | 19.43 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.27 | 9.45 | 15.45 | 2.00 | 86.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 15.56 | 24.45 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.92 | 24.09 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.95 | 13.75 | 21.75 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 12.96 | 21.33 | 3.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.58 | 12.21 | 19.36 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.84 | 16.39 | 25.42 | 9.00 | 90.0 | 89.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.21 | 12.05 | 18.83 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.58 | 11.35 | 17.90 | 2.00 | 86.6 | 61.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.34 | 20.46 | 31.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.53 | 17.65 | 29.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.45 | 16.37 | 28.18 | 10.00 | 73.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.57 | 14.30 | 22.64 | 9.00 | 86.7 | 61.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.5 | 4.32 | 12.10 | 19.12 | 4.00 | 82.4 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.29
- Actual score: 22.00
- Transfer: Bruno Guimarães Rodriguez Moura -> Moisés Caicedo Corozo (projected gain 1.71, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 11.84 | 19.05 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.58 | 8.49 | 14.17 | 2.00 | 81.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.21 | 27.25 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.30 | 15.18 | 23.84 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.94 | 12.18 | 19.55 | 1.00 | 77.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.17 | 11.98 | 19.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.32 | 11.59 | 18.66 | 1.00 | 89.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.48 | 16.35 | 24.97 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.69 | 11.07 | 17.26 | 13.00 | 64.2 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.60 | 16.58 | 1.00 | 71.3 | 27.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.57 | 17.70 | 30.05 | 2.00 | 85.3 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 8.1 | 5.90 | 17.44 | 28.14 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.46 | 14.65 | 22.65 | 7.00 | 67.3 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.38 | 13.87 | 21.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.50 | 12.52 | 20.12 | 3.00 | 77.3 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 68.88
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.99).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 2.35, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.99).
- Autosub: Micky van de Ven replaced Antoine Semenyo.
- Autosub: Marc Guéhi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 10.99 | 17.84 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.90 | 8.63 | 14.25 | 3.00 | 84.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.70 | 13.50 | 21.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.13 | 13.49 | 22.66 | 14.00 | 87.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.79 | 12.51 | 19.79 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.53 | 11.20 | 18.05 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 8 | 5.0 | 3.51 | 9.15 | 15.15 | 5.00 | 47.2 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.17 | 14.89 | 23.78 | 1.00 | 69.9 | 59.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 4.68 | 13.93 | 21.78 | 4.00 | 86.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.66 | 8.18 | 13.75 | 2.00 | 41.3 | 85.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 6.77 | 19.02 | 29.68 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.47 | 18.53 | 30.91 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 5.47 | 14.90 | 24.30 | 0.00 | 85.0 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.47 | 12.63 | 18.97 | 0.00 | 77.9 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.15 | 20.49 | 3.00 | 73.6 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 67.49
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.84) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 4.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.84) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 10.05 | 16.58 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.7 | 2.82 | 8.17 | 13.36 | 1.00 | 81.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.10 | 13.89 | 22.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.92 | 12.08 | 19.27 | 2.00 | 78.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.95 | 11.36 | 18.89 | 0.00 | 87.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.34 | 18.11 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.01 | 11.08 | 18.48 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 6.42 | 17.58 | 26.08 | 13.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.16 | 20.46 | 6.00 | 53.9 | 90.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.42 | 9.26 | 15.54 | 1.00 | 53.0 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.35 | 18.59 | 30.60 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 6.9 | 5.91 | 15.54 | 23.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.71 | 14.72 | 23.51 | 1.00 | 73.2 | 90.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 2.57 | 8.12 | 14.89 | 1.00 | 34.2 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.03 | 7.16 | 11.64 | -2.00 | 36.3 | 37.0 |