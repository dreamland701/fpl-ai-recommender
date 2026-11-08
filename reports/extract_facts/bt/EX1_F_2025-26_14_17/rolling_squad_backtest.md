# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.65
- Total actual points: 285.00
- Average predicted points: 66.16
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
- Predicted score: 65.90
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.37 | 18.07 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.15 | 0.18 | 0.19 | 0.00 | 3.4 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.67 | 13.38 | 20.96 | 1.00 | 85.2 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.55 | 12.78 | 20.05 | 14.00 | 84.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.41 | 18.67 | 8.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.89 | 8.25 | 12.86 | 4.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.40 | 6.71 | 11.24 | 0.00 | 74.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 23.61 | 38.37 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.35 | 14.94 | 23.57 | 2.00 | 87.2 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.81 | 2.79 | 4.87 | 1.00 | 11.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.11 | 17.30 | 27.64 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.67 | 15.99 | 25.73 | 2.00 | 86.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.72 | 25.58 | 3.00 | 87.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.12 | 14.25 | 23.60 | 4.00 | 81.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.88 | 13.05 | 20.88 | 2.00 | 88.7 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.13
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.63, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 11.22 | 18.09 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.05 | 0.20 | 0.00 | 4.7 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.96 | 14.50 | 23.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.81 | 19.35 | 6.00 | 85.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.94 | 11.61 | 18.48 | 2.00 | 88.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.34 | 15.04 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.52 | 4.69 | 7.89 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.86 | 25.51 | 41.63 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.92 | 11.86 | 19.86 | 2.00 | 63.2 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.05 | 3.73 | 6.35 | 0.00 | 20.4 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.26 | 26.68 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.13 | 14.18 | 23.64 | 8.00 | 80.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.30 | 12.59 | 21.45 | 3.00 | 69.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.68 | 12.02 | 22.10 | 6.00 | 66.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.87 | 11.89 | 19.32 | 4.00 | 75.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.98
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.91) beats the best remaining Bench Boost opportunity (3.33).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.91) beats the best remaining Bench Boost opportunity (3.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.76 | 12.43 | 19.64 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.02 | 0.03 | 0.10 | 0.00 | 3.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.59 | 20.38 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.20 | 16.99 | 1.00 | 84.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.68 | 10.01 | 15.87 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.09 | 3.29 | 5.72 | 1.00 | 31.4 | 76.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 1.32 | 4.87 | 0.00 | 1.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.44 | 23.30 | 38.56 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.41 | 17.41 | 27.22 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.80 | 5.44 | 8.44 | 0.00 | 38.1 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.49 | 20.45 | 33.37 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.64 | 16.01 | 25.87 | 2.00 | 79.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.25 | 12.14 | 19.65 | 3.00 | 78.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.05 | 11.97 | 20.32 | 6.00 | 71.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.16 | 11.70 | 20.50 | 2.00 | 67.2 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.64
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.50, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.95) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.40 | 10.11 | 16.39 | 7.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 11.84 | 19.26 | 1.00 | 86.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.75 | 10.92 | 17.66 | 1.00 | 84.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.10 | 9.08 | 14.51 | 0.00 | 79.3 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.26 | 4.48 | 9.98 | 0.00 | 21.2 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.78 | 6.88 | 0.00 | 48.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.95 | 25.10 | 41.10 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 2.99 | 10.39 | 17.41 | 2.00 | 40.9 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.90 | 2.88 | 4.70 | 0.00 | 16.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.25 | 19.32 | 31.29 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.54 | 18.91 | 29.30 | 3.00 | 86.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.28 | 16.18 | 25.58 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.63 | 14.08 | 22.79 | 11.00 | 75.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.82 | 18.88 | 4.00 | 76.5 | 90.0 |