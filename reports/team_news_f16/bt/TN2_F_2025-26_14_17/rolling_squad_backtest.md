# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 262.96
- Total actual points: 277.00
- Average predicted points: 65.74
- Average actual points: 69.25
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
- Predicted score: 65.21
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.95 | 11.31 | 18.10 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.21 | 0.74 | 1.28 | 0.00 | 6.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.64 | 13.32 | 21.05 | 1.00 | 84.4 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.67 | 20.05 | 14.00 | 83.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.18 | 11.31 | 18.68 | 8.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.82 | 8.10 | 12.81 | 4.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.35 | 6.63 | 11.27 | 0.00 | 73.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.85 | 23.43 | 38.33 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.30 | 14.85 | 23.63 | 2.00 | 86.3 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.86 | 2.86 | 5.01 | 1.00 | 13.6 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.07 | 17.25 | 27.76 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.61 | 15.86 | 25.71 | 2.00 | 85.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.37 | 15.59 | 25.58 | 3.00 | 86.2 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.09 | 14.19 | 23.63 | 4.00 | 81.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.81 | 12.91 | 20.88 | 2.00 | 86.9 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.51
- Actual score: 59.00
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 4.31, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 11.27 | 18.14 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.09 | 0.45 | 0.85 | 0.00 | 0.4 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.00 | 14.55 | 23.14 | 0.00 | 90.0 | 0.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.97 | 11.62 | 18.51 | 2.00 | 88.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.71 | 11.28 | 18.42 | 3.00 | 70.4 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.40 | 9.37 | 15.07 | 3.00 | 85.9 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.03 | 2.60 | 5.59 | 0.00 | 1.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.60 | 24.91 | 40.56 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.92 | 11.81 | 19.79 | 2.00 | 63.9 | 65.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.20 | 3.98 | 6.61 | 0.00 | 24.7 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.71 | 16.10 | 26.65 | 18.00 | 89.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.05 | 13.98 | 23.50 | 8.00 | 78.5 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.8 | 4.95 | 13.54 | 22.01 | 10.00 | 79.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.30 | 12.53 | 21.32 | 3.00 | 70.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.90 | 19.38 | 4.00 | 76.5 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.24
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.66) beats the best remaining Bench Boost opportunity (4.27).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 12.38, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.66) beats the best remaining Bench Boost opportunity (4.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.79 | 12.51 | 19.76 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.02 | 0.30 | 0.78 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.47 | 11.74 | 19.19 | 2.00 | 81.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.47 | 10.23 | 17.01 | 1.00 | 84.8 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.70 | 10.05 | 15.93 | 1.00 | 84.6 | 90.0 |
| Bench 3 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.16 | 4.80 | 10.06 | 0.00 | 26.3 | 0.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.55 | 3.03 | 5.95 | 1.00 | 16.1 | 76.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.46 | 23.31 | 38.65 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.54 | 17.69 | 27.67 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.93 | 5.67 | 8.71 | 0.00 | 42.0 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.44 | 20.40 | 33.52 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.9 | 4.98 | 14.40 | 22.75 | 1.00 | 85.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.27 | 12.14 | 19.68 | 3.00 | 79.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.99 | 11.80 | 20.04 | 6.00 | 71.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.02 | 11.33 | 20.10 | 2.00 | 64.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.99
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.73, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.41 | 10.10 | 16.36 | 7.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.07 | 0.31 | 0.77 | 0.00 | 0.2 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.82 | 11.11 | 18.33 | 6.00 | 76.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.76 | 10.94 | 17.68 | 1.00 | 84.7 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 9.13 | 14.57 | 0.00 | 80.3 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.24 | 4.33 | 9.66 | 0.00 | 22.3 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.03 | 1.99 | 4.75 | 0.00 | 1.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.72 | 24.59 | 40.21 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.48 | 11.11 | 17.67 | 2.00 | 49.4 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.12 | 4.95 | 0.00 | 20.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.18 | 19.19 | 31.33 | 1.00 | 89.4 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.47 | 28.49 | 3.00 | 79.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.06 | 15.74 | 24.73 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 6.9 | 3.75 | 11.95 | 19.49 | 2.00 | 69.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.83 | 18.89 | 4.00 | 77.2 | 90.0 |