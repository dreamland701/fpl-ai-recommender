# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.23
- Total actual points: 285.00
- Average predicted points: 66.06
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
- Predicted score: 65.97
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.38 | 18.10 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Julian Eyestone | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.69 | 13.37 | 20.95 | 1.00 | 85.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.55 | 12.75 | 20.01 | 14.00 | 84.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.42 | 18.72 | 8.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.89 | 8.24 | 12.83 | 4.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.42 | 6.76 | 11.31 | 0.00 | 75.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.86 | 23.27 | 37.77 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.42 | 15.28 | 24.31 | 2.00 | 88.5 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.79 | 2.72 | 4.76 | 1.00 | 11.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.18 | 17.74 | 28.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.55 | 16.11 | 26.33 | 3.00 | 88.6 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.73 | 25.28 | 2.00 | 86.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.24 | 23.64 | 4.00 | 81.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.88 | 12.90 | 20.58 | 2.00 | 88.8 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.82
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.65, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.18 | 18.06 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Julian Eyestone | GK | 5 | 3.9 | 0.00 | 0.07 | 0.16 | 0.00 | 3.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.48 | 23.02 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 11.73 | 19.22 | 6.00 | 85.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.94 | 11.60 | 18.51 | 2.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.33 | 15.02 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.52 | 4.69 | 7.93 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.51 | 24.56 | 39.85 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.93 | 12.06 | 20.38 | 2.00 | 63.3 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.03 | 3.65 | 6.22 | 0.00 | 20.1 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.82 | 16.58 | 27.29 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.05 | 13.84 | 23.09 | 8.00 | 78.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.22 | 13.31 | 23.29 | 6.00 | 73.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.24 | 12.50 | 21.41 | 3.00 | 68.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.83 | 11.67 | 18.97 | 4.00 | 75.2 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.87
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.02) beats the best remaining Bench Boost opportunity (4.66).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.92, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.02) beats the best remaining Bench Boost opportunity (4.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.77 | 12.46 | 19.71 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Julian Eyestone | GK | 5 | 3.9 | 0.15 | 0.15 | 0.30 | 0.00 | 2.8 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.25 | 12.52 | 20.26 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.21 | 17.02 | 1.00 | 84.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.67 | 10.00 | 15.85 | 1.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.00 | 4.50 | 9.71 | 0.00 | 22.2 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.08 | 3.27 | 5.72 | 1.00 | 31.2 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.35 | 22.90 | 37.89 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.58 | 17.95 | 28.24 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.79 | 5.38 | 8.34 | 0.00 | 38.1 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.57 | 20.85 | 34.09 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.49 | 14.76 | 24.55 | 2.00 | 85.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.21 | 11.95 | 19.35 | 3.00 | 77.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.95 | 11.76 | 20.11 | 6.00 | 69.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.00 | 11.14 | 19.63 | 2.00 | 64.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.57
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.71, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.36 | 9.99 | 16.23 | 7.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Julian Eyestone | GK | 5 | 3.9 | 0.12 | 0.16 | 0.32 | 0.00 | 3.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.95 | 11.69 | 19.03 | 1.00 | 86.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.74 | 10.90 | 17.67 | 1.00 | 84.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.09 | 9.06 | 14.50 | 0.00 | 79.4 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.03 | 3.79 | 8.93 | 0.00 | 16.9 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.77 | 6.89 | 0.00 | 47.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.61 | 24.17 | 39.43 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.43 | 11.21 | 18.05 | 2.00 | 47.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.89 | 2.82 | 4.59 | 0.00 | 16.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.27 | 19.50 | 31.67 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.30 | 18.15 | 27.90 | 3.00 | 78.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.73 | 24.80 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.70 | 14.37 | 23.42 | 11.00 | 76.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.84 | 11.62 | 18.54 | 4.00 | 75.7 | 90.0 |