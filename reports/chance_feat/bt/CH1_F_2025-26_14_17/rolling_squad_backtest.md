# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.09
- Total actual points: 285.00
- Average predicted points: 66.02
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
- Predicted score: 65.98
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.37 | 18.07 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.15 | 0.37 | 0.00 | 2.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.70 | 13.45 | 21.11 | 1.00 | 86.1 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.56 | 12.78 | 20.08 | 14.00 | 84.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.39 | 18.65 | 8.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.90 | 8.25 | 12.88 | 4.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.41 | 6.76 | 11.31 | 0.00 | 75.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.93 | 23.56 | 38.35 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.37 | 14.97 | 23.66 | 2.00 | 87.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.79 | 2.73 | 4.79 | 1.00 | 11.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.36 | 27.78 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 15.95 | 25.71 | 2.00 | 86.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.72 | 25.62 | 3.00 | 88.0 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.25 | 23.64 | 4.00 | 81.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.91 | 13.11 | 21.01 | 2.00 | 89.5 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.79
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.70, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.15 | 18.01 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.14 | 0.28 | 0.00 | 2.5 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.53 | 23.12 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.99 | 11.79 | 19.34 | 6.00 | 85.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.94 | 11.56 | 18.43 | 2.00 | 88.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.32 | 15.02 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.51 | 4.62 | 7.76 | 0.00 | 43.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.59 | 24.88 | 40.50 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.87 | 11.68 | 19.61 | 2.00 | 62.6 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.03 | 3.68 | 6.28 | 0.00 | 20.1 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.26 | 26.73 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.07 | 14.01 | 23.40 | 8.00 | 79.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.11 | 12.86 | 22.44 | 6.00 | 73.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.22 | 12.36 | 21.11 | 3.00 | 68.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.83 | 19.24 | 4.00 | 75.8 | 90.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.86) beats the best remaining Bench Boost opportunity (4.45).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.86) beats the best remaining Bench Boost opportunity (4.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.78 | 12.47 | 19.75 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.00 | 0.06 | 0.29 | 0.00 | 1.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.62 | 20.44 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.44 | 10.19 | 16.98 | 1.00 | 84.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.67 | 10.00 | 15.85 | 1.00 | 84.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.98 | 4.38 | 9.45 | 0.00 | 21.9 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.08 | 3.24 | 5.66 | 1.00 | 31.2 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.42 | 23.22 | 38.52 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.55 | 17.78 | 27.87 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.80 | 5.44 | 8.47 | 0.00 | 38.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.56 | 20.69 | 33.80 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 14.37 | 23.80 | 2.00 | 84.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.23 | 12.07 | 19.55 | 3.00 | 78.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.92 | 11.63 | 19.82 | 6.00 | 69.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.00 | 11.23 | 19.81 | 2.00 | 64.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.67
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.69) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.82, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.69) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.36 | 9.94 | 16.15 | 7.00 | 78.6 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.06 | 0.14 | 0.00 | 0.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.77 | 19.17 | 1.00 | 86.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.74 | 10.90 | 17.65 | 1.00 | 84.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.09 | 9.04 | 14.45 | 0.00 | 79.3 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.04 | 3.91 | 9.15 | 0.00 | 17.2 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.82 | 6.99 | 0.00 | 48.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.69 | 24.51 | 40.08 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.37 | 10.87 | 17.33 | 2.00 | 46.7 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.89 | 2.85 | 4.65 | 0.00 | 16.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.26 | 19.35 | 31.41 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.32 | 18.41 | 28.41 | 3.00 | 79.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.04 | 15.72 | 24.74 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.59 | 13.97 | 22.65 | 11.00 | 75.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.75 | 18.78 | 4.00 | 76.2 | 90.0 |