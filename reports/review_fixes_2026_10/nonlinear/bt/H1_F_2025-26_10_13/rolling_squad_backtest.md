# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 236.49
- Total actual points: 205.00
- Average predicted points: 59.12
- Average actual points: 51.25
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
- Captain: Jean-Philippe Mateta
- Vice captain: Bryan Mbeumo
- Effective captain: Jean-Philippe Mateta
- Chip used: none
- Predicted score: 54.36
- Actual score: 79.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.14 | 12.06 | 19.43 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.33 | 9.45 | 15.45 | 2.00 | 87.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.46 | 15.56 | 24.45 | 12.00 | 87.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.78 | 14.92 | 24.09 | 10.00 | 86.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.09 | 13.75 | 21.75 | 6.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.30 | 12.96 | 21.33 | 3.00 | 81.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.52 | 12.21 | 19.36 | 2.00 | 85.9 | 90.0 |
| Captain | Captain | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.84 | 16.39 | 25.42 | 9.00 | 81.6 | 89.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.55 | 12.05 | 18.83 | 2.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.91 | 11.35 | 17.90 | 2.00 | 65.7 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.44 | 20.46 | 31.34 | 2.00 | 80.4 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | MID | 4 | 8.1 | 2.92 | 17.65 | 29.08 | 2.00 | 84.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.83 | 16.37 | 28.18 | 10.00 | 82.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.77 | 14.30 | 22.64 | 9.00 | 82.6 | 61.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.5 | 4.10 | 12.05 | 19.12 | 2.00 | 86.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Jean-Philippe Mateta
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 53.21
- Actual score: 41.00
- Transfer: Dominik Szoboszlai -> Moisés Caicedo Corozo (projected gain 2.85, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.81 | 11.84 | 19.05 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.15 | 8.49 | 14.17 | 2.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.27 | 17.21 | 27.25 | 1.00 | 87.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 3.69 | 15.18 | 23.84 | 0.00 | 87.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 3.88 | 12.18 | 19.55 | 1.00 | 83.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.78 | 11.98 | 19.43 | 2.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.13 | 11.59 | 18.66 | 1.00 | 85.6 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.00 | 16.35 | 24.97 | 2.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.59 | 11.07 | 17.26 | 13.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.23 | 10.60 | 16.58 | 1.00 | 56.6 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.10 | 17.70 | 30.05 | 2.00 | 82.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.11 | 17.44 | 28.14 | 0.00 | 90.2 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 5.68 | 14.65 | 22.65 | 7.00 | 81.9 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.86 | 13.87 | 21.48 | 2.00 | 81.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.36 | 12.52 | 20.12 | 3.00 | 73.9 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.76
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.43).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.43).
- Autosub: Junior Kroupi replaced Moisés Caicedo Corozo.
- Autosub: Marc Guéhi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.61 | 10.99 | 17.84 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.39 | 8.63 | 14.25 | 3.00 | 88.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.17 | 13.50 | 21.25 | 5.00 | 84.7 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.04 | 13.49 | 22.66 | 14.00 | 86.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.50 | 12.51 | 19.79 | 3.00 | 86.5 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 2.15 | 11.20 | 18.05 | 0.00 | 87.0 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 8 | 5.0 | 2.79 | 9.15 | 15.15 | 5.00 | 59.1 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.06 | 14.89 | 23.78 | 1.00 | 85.2 | 59.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 3.63 | 13.93 | 21.78 | 4.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.23 | 8.18 | 13.75 | 2.00 | 60.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 5.28 | 19.02 | 29.68 | 1.00 | 84.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.2 | 6.30 | 18.53 | 30.91 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 3.97 | 14.90 | 24.30 | 0.00 | 67.9 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.61 | 12.63 | 18.97 | 0.00 | 84.9 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.98 | 12.15 | 20.49 | 3.00 | 80.1 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Morgan Rogers
- Effective captain: Morgan Rogers
- Chip used: bench_boost
- Predicted score: 67.16
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.19) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Morgan Rogers (projected gain 6.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 2.91 | 10.05 | 16.58 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.7 | 2.88 | 8.17 | 13.36 | 1.00 | 86.3 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.00 | 13.89 | 22.72 | 1.00 | 87.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.60 | 12.08 | 19.27 | 2.00 | 83.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.87 | 11.36 | 18.89 | 0.00 | 88.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.81 | 11.34 | 18.11 | 2.00 | 82.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.93 | 11.08 | 18.48 | 0.00 | 86.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 5.16 | 17.58 | 26.08 | 13.00 | 85.0 | 90.0 |
| Bench 3 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.50 | 12.16 | 20.46 | 6.00 | 54.8 | 90.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 3.55 | 9.26 | 15.54 | 1.00 | 68.5 | 10.0 |
| Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.88 | 18.59 | 30.60 | 0.00 | 86.4 | 0.0 |
| Vice Captain | Captain | Morgan Rogers | MID | 2 | 6.9 | 5.58 | 15.54 | 23.91 | 3.00 | 84.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.31 | 14.72 | 23.51 | 1.00 | 79.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 10.74 | 18.71 | 2.00 | 75.8 | 79.0 |
| Bench 4 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 3.26 | 8.12 | 14.89 | 1.00 | 46.3 | 90.0 |