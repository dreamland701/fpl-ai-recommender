# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 263.14
- Total actual points: 285.00
- Average predicted points: 65.78
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
- Predicted score: 65.19
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.93 | 11.28 | 18.04 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.17 | 0.23 | 0.33 | 0.00 | 4.4 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.61 | 13.26 | 20.94 | 1.00 | 83.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.67 | 20.03 | 14.00 | 83.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.18 | 11.31 | 18.71 | 8.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.82 | 8.11 | 12.81 | 4.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.35 | 6.62 | 11.28 | 0.00 | 73.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.87 | 23.47 | 38.32 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.29 | 14.83 | 23.57 | 2.00 | 85.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.90 | 5.06 | 1.00 | 13.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.04 | 17.18 | 27.66 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.62 | 15.89 | 25.74 | 2.00 | 85.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.37 | 15.58 | 25.58 | 3.00 | 86.1 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.22 | 23.68 | 4.00 | 81.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.79 | 12.88 | 20.83 | 2.00 | 86.5 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.77
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.55, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 11.27 | 18.11 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.52 | 23.06 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.03 | 11.85 | 19.38 | 6.00 | 86.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.97 | 11.63 | 18.51 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.40 | 9.37 | 15.07 | 3.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.21 | 3.98 | 7.13 | 0.00 | 37.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.61 | 24.96 | 40.52 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.96 | 11.92 | 19.91 | 2.00 | 64.4 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.20 | 4.00 | 6.61 | 0.00 | 24.7 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.72 | 16.11 | 26.62 | 18.00 | 89.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.10 | 14.10 | 23.64 | 8.00 | 79.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.37 | 12.68 | 21.51 | 3.00 | 70.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.71 | 12.20 | 23.04 | 6.00 | 64.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.91 | 19.38 | 4.00 | 76.5 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.71
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.95) beats the best remaining Bench Boost opportunity (3.39).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.03, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.95) beats the best remaining Bench Boost opportunity (3.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.77 | 12.45 | 19.66 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 12.62 | 20.41 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.48 | 10.25 | 17.01 | 1.00 | 84.7 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.70 | 10.05 | 15.91 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.03 | 3.63 | 6.59 | 1.00 | 29.7 | 76.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 2.13 | 6.07 | 0.00 | 10.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.46 | 23.33 | 38.60 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.45 | 17.49 | 27.33 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.92 | 5.65 | 8.68 | 0.00 | 41.8 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.38 | 20.26 | 33.27 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.29 | 14.70 | 25.02 | 2.00 | 77.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.18 | 19.72 | 3.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.08 | 12.02 | 20.33 | 6.00 | 72.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.15 | 11.65 | 20.50 | 2.00 | 66.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.47
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 10.48, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.43 | 10.16 | 16.42 | 7.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.01 | 11.89 | 19.30 | 1.00 | 87.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.77 | 10.96 | 17.70 | 1.00 | 84.8 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 9.14 | 14.57 | 0.00 | 80.3 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.41 | 4.73 | 10.22 | 0.00 | 24.9 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.97 | 3.07 | 6.06 | 0.00 | 41.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.73 | 24.64 | 40.20 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.23 | 10.35 | 17.49 | 2.00 | 46.1 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.13 | 4.96 | 0.00 | 20.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.92 | 19.80 | 30.56 | 3.00 | 86.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.16 | 19.16 | 31.23 | 1.00 | 88.9 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.74 | 24.71 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.13 | 22.85 | 11.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.87 | 18.94 | 4.00 | 77.5 | 90.0 |