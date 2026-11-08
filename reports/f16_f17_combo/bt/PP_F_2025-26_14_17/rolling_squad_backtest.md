# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 265.54
- Total actual points: 285.00
- Average predicted points: 66.38
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
- Predicted score: 66.35
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.05 | 11.57 | 18.44 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.19 | 0.73 | 1.20 | 0.00 | 5.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.72 | 13.47 | 21.13 | 1.00 | 86.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.62 | 13.00 | 20.48 | 14.00 | 88.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.31 | 11.67 | 19.13 | 8.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.82 | 8.01 | 12.49 | 4.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.45 | 6.86 | 11.43 | 0.00 | 76.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.92 | 23.52 | 38.32 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.39 | 15.01 | 23.72 | 2.00 | 89.0 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.78 | 2.65 | 4.61 | 1.00 | 10.2 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.41 | 27.86 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.72 | 16.23 | 26.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.45 | 15.73 | 25.61 | 3.00 | 88.3 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.15 | 14.36 | 23.80 | 4.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.96 | 13.29 | 21.31 | 2.00 | 90.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.24
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.76, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.37 | 18.40 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.29 | 0.79 | 1.29 | 0.00 | 5.7 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.03 | 14.67 | 23.38 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.03 | 11.93 | 19.60 | 6.00 | 87.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.00 | 11.76 | 18.80 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.28 | 9.05 | 14.54 | 3.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.56 | 4.79 | 8.07 | 0.00 | 44.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.57 | 24.80 | 40.39 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.91 | 11.84 | 19.90 | 2.00 | 64.3 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.01 | 3.57 | 6.04 | 0.00 | 18.5 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.82 | 16.35 | 26.91 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.13 | 14.27 | 23.91 | 8.00 | 82.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.14 | 12.98 | 22.65 | 6.00 | 74.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.29 | 12.67 | 21.69 | 3.00 | 71.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 12.05 | 19.65 | 4.00 | 78.3 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.13
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.17) beats the best remaining Bench Boost opportunity (4.83).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.17) beats the best remaining Bench Boost opportunity (4.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.84 | 12.73 | 20.21 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.19 | 0.61 | 1.21 | 0.00 | 5.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.30 | 12.73 | 20.64 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.50 | 10.42 | 17.39 | 1.00 | 87.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.58 | 9.71 | 15.32 | 1.00 | 79.7 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.08 | 4.77 | 10.19 | 0.00 | 25.7 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.13 | 3.41 | 5.96 | 1.00 | 33.1 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.38 | 23.05 | 38.24 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.49 | 17.50 | 27.32 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.78 | 5.31 | 8.19 | 0.00 | 36.6 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.56 | 20.64 | 33.73 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.40 | 14.43 | 23.92 | 2.00 | 85.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.27 | 19.94 | 3.00 | 80.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.00 | 11.99 | 20.49 | 6.00 | 73.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.07 | 11.53 | 20.40 | 2.00 | 67.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.81
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.39, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.43 | 10.27 | 16.76 | 7.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.25 | 0.62 | 1.19 | 0.00 | 5.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.91 | 19.44 | 1.00 | 88.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.80 | 11.16 | 18.15 | 1.00 | 87.5 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.01 | 8.81 | 14.04 | 0.00 | 75.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.11 | 4.13 | 9.53 | 0.00 | 20.1 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.35 | 3.94 | 7.19 | 0.00 | 49.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.64 | 24.32 | 39.78 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.36 | 10.78 | 17.13 | 2.00 | 44.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.89 | 2.78 | 4.47 | 0.00 | 15.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.29 | 19.41 | 31.52 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.39 | 28.34 | 3.00 | 78.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.11 | 15.96 | 25.17 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.62 | 14.09 | 22.89 | 11.00 | 77.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.94 | 19.17 | 4.00 | 78.6 | 90.0 |