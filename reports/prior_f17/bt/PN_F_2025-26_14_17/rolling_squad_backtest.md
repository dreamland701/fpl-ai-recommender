# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.56
- Total actual points: 285.00
- Average predicted points: 66.14
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
- Predicted score: 66.04
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.39 | 18.10 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.13 | 0.10 | 0.06 | 0.00 | 2.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.71 | 13.46 | 21.10 | 1.00 | 86.3 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.57 | 12.79 | 20.08 | 14.00 | 85.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.40 | 18.64 | 8.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.86 | 8.12 | 12.68 | 4.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.45 | 6.88 | 11.50 | 0.00 | 76.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.93 | 23.61 | 38.50 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.37 | 14.98 | 23.67 | 2.00 | 87.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.83 | 2.87 | 5.01 | 1.00 | 12.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.40 | 27.86 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.67 | 16.02 | 25.83 | 2.00 | 87.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.72 | 25.61 | 3.00 | 88.0 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.26 | 23.63 | 4.00 | 81.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.93 | 13.19 | 21.14 | 2.00 | 90.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.91
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.67, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.19 | 18.07 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.07 | 0.00 | 4.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.99 | 14.52 | 23.09 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.83 | 19.41 | 6.00 | 86.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.94 | 11.55 | 18.40 | 2.00 | 87.8 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.33 | 9.20 | 14.82 | 3.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.56 | 4.82 | 8.14 | 0.00 | 44.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.59 | 24.94 | 40.66 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.88 | 11.76 | 19.76 | 2.00 | 62.8 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.06 | 3.81 | 6.50 | 0.00 | 21.3 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.80 | 16.30 | 26.82 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.08 | 14.09 | 23.57 | 8.00 | 79.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.12 | 12.93 | 22.57 | 6.00 | 73.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.24 | 12.50 | 21.37 | 3.00 | 68.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.95 | 19.47 | 4.00 | 76.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.82
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.98) beats the best remaining Bench Boost opportunity (4.59).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.08, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.98) beats the best remaining Bench Boost opportunity (4.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.78 | 12.50 | 19.79 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.28 | 12.64 | 20.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.44 | 10.16 | 16.91 | 1.00 | 83.8 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.63 | 9.88 | 15.65 | 1.00 | 82.6 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.02 | 4.59 | 9.85 | 0.00 | 22.8 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.12 | 3.40 | 5.95 | 1.00 | 32.6 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.41 | 23.25 | 38.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.56 | 17.79 | 27.87 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.83 | 5.55 | 8.64 | 0.00 | 39.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.55 | 20.64 | 33.72 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.39 | 14.40 | 23.87 | 2.00 | 84.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.26 | 12.18 | 19.78 | 3.00 | 79.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.96 | 11.80 | 20.14 | 6.00 | 70.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.03 | 11.38 | 20.11 | 2.00 | 65.2 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.79
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.71, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.37 | 10.05 | 16.33 | 7.00 | 79.0 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 11.83 | 19.29 | 1.00 | 87.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.74 | 10.88 | 17.62 | 1.00 | 83.9 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.06 | 8.94 | 14.29 | 0.00 | 78.1 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.07 | 4.01 | 9.31 | 0.00 | 17.9 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.33 | 3.90 | 7.13 | 0.00 | 49.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.68 | 24.55 | 40.23 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.43 | 11.09 | 17.72 | 2.00 | 48.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.93 | 3.00 | 4.90 | 0.00 | 17.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.38 | 31.47 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.35 | 18.51 | 28.56 | 3.00 | 80.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.06 | 15.78 | 24.84 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.60 | 14.03 | 22.77 | 11.00 | 76.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.85 | 18.98 | 4.00 | 77.0 | 90.0 |