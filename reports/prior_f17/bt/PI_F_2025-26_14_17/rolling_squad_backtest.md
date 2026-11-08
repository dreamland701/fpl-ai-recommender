# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.01
- Total actual points: 285.00
- Average predicted points: 66.00
- Average actual points: 71.25
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
- Predicted score: 66.08
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.02 | 11.45 | 18.18 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.69 | 13.40 | 21.02 | 1.00 | 86.1 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.60 | 12.87 | 20.20 | 14.00 | 84.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.28 | 11.49 | 18.76 | 8.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.88 | 8.16 | 12.71 | 4.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.45 | 6.89 | 11.53 | 0.00 | 75.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.77 | 23.15 | 37.73 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.43 | 15.15 | 23.94 | 2.00 | 87.6 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.77 | 2.66 | 4.68 | 1.00 | 11.6 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.20 | 17.55 | 28.06 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.75 | 16.20 | 26.11 | 2.00 | 86.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.50 | 15.86 | 25.83 | 3.00 | 87.7 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.13 | 14.30 | 23.69 | 4.00 | 81.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.94 | 13.19 | 21.10 | 2.00 | 89.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.95
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.78, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 11.25 | 18.14 | 2.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.1 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.01 | 14.58 | 23.19 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.01 | 11.84 | 19.41 | 6.00 | 85.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.98 | 11.66 | 18.57 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.35 | 9.26 | 14.89 | 3.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.56 | 4.83 | 8.16 | 0.00 | 43.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.43 | 24.48 | 39.91 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.93 | 11.89 | 19.96 | 2.00 | 62.4 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.00 | 3.61 | 6.17 | 0.00 | 20.3 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.86 | 16.45 | 27.05 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.15 | 14.27 | 23.84 | 8.00 | 78.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.17 | 13.05 | 22.75 | 6.00 | 72.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.24 | 12.45 | 21.28 | 3.00 | 68.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.97 | 19.48 | 4.00 | 75.4 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.65
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.92) beats the best remaining Bench Boost opportunity (4.53).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.92) beats the best remaining Bench Boost opportunity (4.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.81 | 12.53 | 19.81 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.02 | 0.00 | 0.07 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.29 | 12.66 | 20.51 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.47 | 10.25 | 17.03 | 1.00 | 83.6 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.66 | 9.94 | 15.73 | 1.00 | 83.7 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.01 | 4.56 | 9.81 | 0.00 | 22.1 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.12 | 3.42 | 5.99 | 1.00 | 31.5 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.28 | 22.85 | 37.96 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.25 | 16.92 | 26.52 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.77 | 5.36 | 8.33 | 0.00 | 38.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.62 | 20.80 | 33.98 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 14.53 | 24.05 | 2.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.26 | 12.17 | 19.72 | 3.00 | 78.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.95 | 11.77 | 20.08 | 6.00 | 69.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.09 | 11.54 | 20.35 | 2.00 | 64.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.34
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.48, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.40 | 10.09 | 16.39 | 7.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.99 | 11.86 | 19.31 | 1.00 | 86.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.77 | 10.96 | 17.73 | 1.00 | 83.5 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.08 | 9.00 | 14.36 | 0.00 | 79.1 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.07 | 4.06 | 9.43 | 0.00 | 17.1 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.33 | 3.91 | 7.16 | 0.00 | 48.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.54 | 24.13 | 39.53 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.15 | 10.33 | 16.56 | 2.00 | 48.5 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.82 | 4.60 | 0.00 | 16.2 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.36 | 19.62 | 31.85 | 1.00 | 90.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.47 | 28.52 | 3.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.08 | 15.82 | 24.89 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.66 | 14.19 | 23.02 | 11.00 | 75.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.85 | 18.96 | 4.00 | 75.8 | 90.0 |