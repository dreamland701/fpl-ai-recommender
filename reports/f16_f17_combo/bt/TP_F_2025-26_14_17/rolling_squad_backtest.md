# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 265.41
- Total actual points: 285.00
- Average predicted points: 66.35
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
- Predicted score: 65.64
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.01 | 11.52 | 18.45 | 6.00 | 88.8 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.18 | 0.50 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.65 | 13.34 | 21.06 | 1.00 | 85.0 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.57 | 12.90 | 20.45 | 14.00 | 86.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.26 | 11.58 | 19.12 | 8.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.73 | 7.82 | 12.37 | 4.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.39 | 6.74 | 11.40 | 0.00 | 74.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.83 | 23.35 | 38.20 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.33 | 14.89 | 23.68 | 2.00 | 87.4 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.85 | 2.75 | 4.79 | 1.00 | 12.2 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.08 | 17.28 | 27.82 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.68 | 16.13 | 26.20 | 2.00 | 89.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 15.59 | 25.54 | 3.00 | 86.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.15 | 14.36 | 23.87 | 4.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.87 | 13.10 | 21.20 | 2.00 | 89.3 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.46
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.67, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.90 | 11.47 | 18.50 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.08 | 0.34 | 0.52 | 0.00 | 5.8 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.06 | 14.70 | 23.41 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.07 | 11.99 | 19.66 | 6.00 | 88.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.03 | 11.82 | 18.87 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.29 | 9.04 | 14.53 | 3.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.18 | 3.89 | 6.96 | 0.00 | 36.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.57 | 24.78 | 40.35 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.96 | 11.93 | 19.97 | 2.00 | 65.8 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.17 | 3.84 | 6.34 | 0.00 | 23.0 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.83 | 16.34 | 26.89 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.20 | 14.38 | 24.01 | 8.00 | 83.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.95 | 13.05 | 23.19 | 6.00 | 69.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.38 | 12.83 | 21.85 | 3.00 | 73.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.95 | 12.10 | 19.71 | 4.00 | 79.1 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.08
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.26) beats the best remaining Bench Boost opportunity (4.94).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.26) beats the best remaining Bench Boost opportunity (4.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.87 | 12.79 | 20.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.06 | 0.27 | 0.53 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.33 | 12.77 | 20.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.55 | 10.49 | 17.46 | 1.00 | 88.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.59 | 9.69 | 15.30 | 1.00 | 79.9 | 90.0 |
| Bench 3 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.24 | 5.05 | 10.47 | 0.00 | 30.1 | 0.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.05 | 3.68 | 6.72 | 1.00 | 30.9 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.41 | 23.08 | 38.27 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.48 | 17.47 | 27.25 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.91 | 5.53 | 8.43 | 0.00 | 40.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.52 | 20.56 | 33.62 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.21 | 14.51 | 24.46 | 2.00 | 80.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.32 | 12.32 | 20.01 | 3.00 | 81.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.07 | 12.10 | 20.60 | 6.00 | 75.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.94 | 11.72 | 21.05 | 2.00 | 63.8 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.23
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 10.48, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.50 | 10.39 | 16.88 | 7.00 | 83.9 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.05 | 11.99 | 19.50 | 1.00 | 89.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.85 | 11.23 | 18.21 | 1.00 | 88.6 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.03 | 8.83 | 14.05 | 0.00 | 76.1 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.32 | 4.51 | 9.91 | 0.00 | 25.7 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.96 | 3.04 | 6.06 | 0.00 | 41.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.66 | 24.34 | 39.78 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.44 | 10.89 | 17.21 | 2.00 | 46.6 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.03 | 3.02 | 4.74 | 0.00 | 19.2 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.29 | 19.39 | 31.47 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.38 | 28.29 | 3.00 | 78.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.14 | 16.02 | 25.22 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.66 | 14.16 | 22.94 | 11.00 | 78.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.97 | 12.02 | 19.24 | 4.00 | 79.9 | 90.0 |