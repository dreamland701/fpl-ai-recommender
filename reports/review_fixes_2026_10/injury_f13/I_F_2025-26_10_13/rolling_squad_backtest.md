# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 262.67
- Total actual points: 181.00
- Average predicted points: 65.67
- Average actual points: 45.25
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
- Predicted score: 65.66
- Actual score: 72.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.38 | 11.95 | 19.31 | 6.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 3.27 | 9.45 | 15.48 | 2.00 | 87.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.51 | 15.39 | 24.25 | 12.00 | 92.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.11 | 14.91 | 24.08 | 10.00 | 95.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.07 | 13.73 | 21.73 | 6.00 | 86.7 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.62 | 12.94 | 21.36 | 3.00 | 86.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.63 | 12.26 | 19.44 | 2.00 | 94.1 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 6.33 | 16.23 | 25.23 | 9.00 | 99.9 | 89.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 4.41 | 12.16 | 18.94 | 2.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.74 | 11.36 | 17.89 | 2.00 | 88.4 | 61.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.3 | 7.64 | 20.10 | 30.86 | 2.00 | 129.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.46 | 17.65 | 29.08 | 2.00 | 100.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.92 | 15.34 | 26.77 | 10.00 | 75.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.55 | 14.27 | 22.61 | 9.00 | 86.6 | 61.0 |
| Bench 2 | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.5 | 4.27 | 11.98 | 18.95 | 4.00 | 82.8 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Jean-Philippe Mateta
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.36
- Actual score: 22.00
- Transfer: Bruno Guimarães Rodriguez Moura -> Moisés Caicedo Corozo (projected gain 1.79, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.04 | 11.75 | 18.95 | 1.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.58 | 8.50 | 14.20 | 2.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.35 | 17.06 | 27.08 | 1.00 | 96.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.36 | 15.18 | 23.83 | 0.00 | 92.9 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.96 | 12.18 | 19.55 | 1.00 | 78.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.15 | 11.97 | 19.43 | 2.00 | 93.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.35 | 11.63 | 18.74 | 1.00 | 89.7 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.77 | 16.23 | 24.81 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.2 | 3.77 | 11.19 | 17.38 | 13.00 | 62.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.54 | 10.62 | 16.59 | 1.00 | 73.2 | 27.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 8.1 | 5.83 | 17.44 | 28.14 | 0.00 | 104.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.15 | 16.74 | 28.72 | 2.00 | 89.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.42 | 14.39 | 22.28 | 7.00 | 68.7 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.56 | 13.94 | 21.54 | 2.00 | 95.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.55 | 12.49 | 20.08 | 3.00 | 77.6 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Mohamed Salah
- Effective captain: Bryan Mbeumo
- Chip used: triple_captain
- Predicted score: 69.15
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.89) beats the best remaining Triple Captain opportunity (8.13).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 2.25, hit 0)
- Chip used: Triple Captain on Bryan Mbeumo. Optimizer chose Triple Captain here because the current estimated captain upside (6.89) beats the best remaining Triple Captain opportunity (8.13).
- Autosub: Micky van de Ven replaced Antoine Semenyo.
- Autosub: Marc Guéhi replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.73 | 10.90 | 17.75 | 2.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.91 | 8.63 | 14.27 | 3.00 | 85.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.83 | 13.48 | 21.23 | 5.00 | 93.7 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.20 | 13.39 | 22.56 | 14.00 | 90.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.87 | 12.50 | 19.79 | 3.00 | 95.5 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.55 | 11.23 | 18.11 | 0.00 | 92.3 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 8 | 5.0 | 3.49 | 9.16 | 15.14 | 5.00 | 46.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.24 | 14.77 | 23.61 | 1.00 | 71.8 | 59.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.3 | 4.95 | 14.05 | 21.91 | 4.00 | 89.6 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.73 | 8.21 | 13.75 | 2.00 | 40.7 | 85.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.4 | 6.89 | 18.69 | 29.24 | 1.00 | 113.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 6.02 | 17.60 | 29.65 | 2.00 | 96.1 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 5.16 | 14.90 | 24.30 | 0.00 | 80.1 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.57 | 12.72 | 19.05 | 0.00 | 78.6 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.89 | 12.12 | 20.47 | 3.00 | 73.1 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Morgan Rogers
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 67.49
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 4.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.24 | 9.96 | 16.48 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.7 | 2.79 | 8.18 | 13.38 | 1.00 | 81.3 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.19 | 13.81 | 22.64 | 1.00 | 93.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.02 | 12.09 | 19.28 | 2.00 | 79.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.91 | 11.39 | 18.96 | 0.00 | 86.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.72 | 11.34 | 18.12 | 2.00 | 83.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.98 | 11.11 | 18.48 | 0.00 | 73.7 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 6.94 | 17.74 | 26.28 | 13.00 | 99.2 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.49 | 12.03 | 20.28 | 6.00 | 51.8 | 90.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.37 | 9.30 | 15.57 | 1.00 | 49.4 | 10.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.93 | 17.70 | 29.41 | 0.00 | 94.4 | 0.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 6.22 | 15.65 | 24.02 | 3.00 | 104.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.52 | 14.44 | 23.15 | 1.00 | 73.2 | 90.0 |
| Bench 3 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 2.24 | 8.14 | 14.91 | 1.00 | 28.9 | 90.0 |
| Bench 4 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.00 | 7.22 | 11.70 | -2.00 | 35.5 | 37.0 |