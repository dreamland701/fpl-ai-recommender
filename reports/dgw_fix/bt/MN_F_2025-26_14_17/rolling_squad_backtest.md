# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 263.00
- Total actual points: 285.00
- Average predicted points: 65.75
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
- Predicted score: 66.55
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.15 | 11.53 | 18.38 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.91 | 13.50 | 21.19 | 1.00 | 89.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.51 | 12.65 | 19.86 | 14.00 | 83.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.17 | 18.26 | 8.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.95 | 8.39 | 13.11 | 4.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.44 | 6.75 | 11.26 | 0.00 | 75.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 23.68 | 38.57 | 14.00 | 108.3 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.51 | 14.98 | 23.68 | 2.00 | 90.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.72 | 2.56 | 4.58 | 1.00 | 9.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.21 | 27.48 | 4.00 | 99.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 15.89 | 25.59 | 2.00 | 87.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.52 | 15.66 | 25.48 | 3.00 | 89.3 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.20 | 14.11 | 23.40 | 4.00 | 84.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.93 | 12.98 | 20.76 | 2.00 | 89.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.64
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.56, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.90 | 11.35 | 18.29 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.92 | 14.44 | 22.97 | 0.00 | 94.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.90 | 11.72 | 19.22 | 6.00 | 83.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.81 | 11.44 | 18.24 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.39 | 9.41 | 15.15 | 3.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.40 | 4.32 | 7.30 | 0.00 | 41.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.58 | 24.92 | 40.55 | 2.00 | 113.5 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.70 | 11.59 | 19.46 | 2.00 | 60.2 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.11 | 3.82 | 6.46 | 0.00 | 21.3 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.70 | 15.96 | 26.28 | 18.00 | 89.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.95 | 13.95 | 23.31 | 8.00 | 77.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.91 | 12.59 | 22.02 | 6.00 | 69.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.91 | 12.28 | 20.98 | 3.00 | 64.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.79 | 11.73 | 19.09 | 4.00 | 73.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.00
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.86) beats the best remaining Bench Boost opportunity (3.29).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 12.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.86) beats the best remaining Bench Boost opportunity (3.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.04 | 12.76 | 20.08 | 2.00 | 100.3 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.24 | 12.61 | 20.43 | 6.00 | 91.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.68 | 10.11 | 15.99 | 1.00 | 84.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.34 | 10.04 | 16.73 | 1.00 | 81.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.02 | 3.59 | 8.29 | 0.00 | 3.2 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.93 | 2.87 | 5.02 | 1.00 | 28.2 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.43 | 23.32 | 38.63 | 13.00 | 98.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 7.22 | 18.04 | 28.17 | 2.00 | 109.5 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.90 | 5.61 | 8.65 | 0.00 | 39.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.86 | 20.57 | 33.61 | 13.00 | 119.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.31 | 14.14 | 23.46 | 2.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.08 | 11.86 | 19.27 | 3.00 | 74.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.62 | 11.41 | 19.48 | 6.00 | 65.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.47 | 10.86 | 19.29 | 2.00 | 54.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.82
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.23, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.43 | 10.19 | 16.47 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.90 | 11.72 | 19.10 | 1.00 | 85.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.64 | 10.61 | 17.21 | 1.00 | 82.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.11 | 9.11 | 14.54 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.26 | 3.71 | 6.72 | 0.00 | 47.6 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.37 | 2.57 | 7.06 | 0.00 | 2.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.71 | 24.65 | 40.30 | 16.00 | 114.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.19 | 10.73 | 17.13 | 2.00 | 41.7 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.89 | 2.75 | 4.43 | 0.00 | 15.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.16 | 31.14 | 1.00 | 90.8 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.59 | 18.43 | 28.43 | 3.00 | 82.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.28 | 15.68 | 24.66 | 10.00 | 98.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.54 | 13.73 | 22.31 | 11.00 | 74.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.71 | 11.48 | 18.39 | 4.00 | 73.5 | 90.0 |