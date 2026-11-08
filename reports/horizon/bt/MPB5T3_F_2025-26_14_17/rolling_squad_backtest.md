# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 266.16
- Total actual points: 281.00
- Average predicted points: 66.54
- Average actual points: 70.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW13 are included before the first simulated week.
- League-average scores were not available for this run.

## GW14

- Train rows: 170850
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.54
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.39 | 18.23 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.04 | 0.11 | 0.00 | 2.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.70 | 13.23 | 20.91 | 1.00 | 86.1 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.56 | 12.82 | 20.18 | 14.00 | 84.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.51 | 12.81 | 20.62 | 1.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.90 | 8.30 | 12.90 | 4.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.41 | 6.75 | 11.18 | 0.00 | 74.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 24.04 | 39.35 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.37 | 14.70 | 23.35 | 2.00 | 87.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.79 | 2.69 | 4.67 | 1.00 | 11.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.50 | 28.10 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 16.05 | 26.02 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.57 | 25.53 | 3.00 | 88.0 | 82.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.7 | 4.38 | 13.11 | 21.27 | 7.00 | 87.0 | 45.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.91 | 13.10 | 20.94 | 2.00 | 89.5 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.15
- Actual score: 71.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 5.38, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.21 | 18.27 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.00 | 0.03 | 0.00 | 3.2 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.68 | 23.39 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.58 | 13.28 | 20.85 | 8.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.99 | 12.02 | 19.61 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.33 | 15.13 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.52 | 4.82 | 8.20 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.60 | 25.44 | 41.56 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.87 | 11.90 | 20.01 | 2.00 | 62.7 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.03 | 3.64 | 6.27 | 0.00 | 20.2 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.37 | 26.79 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.08 | 14.16 | 23.74 | 8.00 | 79.3 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.7 | 4.89 | 13.28 | 21.81 | 10.00 | 78.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.12 | 13.03 | 22.73 | 6.00 | 73.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.75 | 19.02 | 4.00 | 75.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.14
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.01) beats the best remaining Bench Boost opportunity (4.63).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 25.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.01) beats the best remaining Bench Boost opportunity (4.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.78 | 12.46 | 19.82 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 3.9 | 0.12 | 0.17 | 0.24 | 0.00 | 2.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.77 | 13.72 | 22.01 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.78 | 20.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.67 | 10.10 | 16.08 | 1.00 | 84.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.01 | 5.43 | 10.90 | 0.00 | 22.4 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.08 | 3.41 | 6.03 | 1.00 | 31.2 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.43 | 23.64 | 39.56 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.53 | 16.95 | 26.79 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.80 | 5.33 | 8.26 | 0.00 | 38.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.55 | 20.51 | 33.47 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 14.38 | 23.73 | 2.00 | 84.7 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.8 | 4.94 | 13.92 | 22.21 | 1.00 | 84.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.23 | 12.14 | 19.57 | 3.00 | 78.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.02 | 11.77 | 20.48 | 2.00 | 65.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 2.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.34
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 24.26, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.37 | 9.99 | 16.25 | 7.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.06 | 0.17 | 0.00 | 2.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.70 | 12.94 | 20.46 | 1.00 | 89.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.85 | 19.31 | 1.00 | 86.5 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.10 | 9.07 | 14.53 | 0.00 | 79.4 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.78 | 6.98 | 0.00 | 47.9 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.05 | 3.49 | 8.28 | 0.00 | 17.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.70 | 25.02 | 41.19 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.39 | 10.46 | 16.68 | 2.00 | 47.0 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.90 | 2.82 | 4.56 | 0.00 | 16.2 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.27 | 18.85 | 30.73 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 17.48 | 27.18 | 3.00 | 79.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.59 | 13.75 | 22.24 | 11.00 | 75.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.70 | 18.98 | 4.00 | 76.2 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.8 | 3.67 | 11.61 | 18.93 | 2.00 | 67.3 | 90.0 |