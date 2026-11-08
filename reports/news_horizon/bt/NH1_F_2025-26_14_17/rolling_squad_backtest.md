# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.38
- Total actual points: 285.00
- Average predicted points: 66.10
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
- Predicted score: 66.03
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.00 | 11.38 | 18.06 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.13 | 0.37 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.70 | 13.45 | 21.13 | 1.00 | 86.0 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.55 | 12.79 | 20.10 | 14.00 | 84.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.23 | 11.39 | 18.65 | 8.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.90 | 8.25 | 12.89 | 4.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.40 | 6.74 | 11.33 | 0.00 | 74.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 23.57 | 38.36 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.38 | 14.98 | 23.66 | 2.00 | 88.2 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.81 | 2.74 | 4.78 | 1.00 | 11.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.36 | 27.78 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.66 | 15.96 | 25.73 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.43 | 15.72 | 25.63 | 3.00 | 87.8 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.15 | 14.27 | 23.58 | 4.00 | 82.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.89 | 13.10 | 21.03 | 2.00 | 89.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.84
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.69, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 11.16 | 18.01 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.11 | 0.28 | 0.00 | 2.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.97 | 14.53 | 23.16 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.80 | 19.35 | 6.00 | 85.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.95 | 11.58 | 18.44 | 2.00 | 88.4 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.33 | 15.02 | 3.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.53 | 4.64 | 7.75 | 0.00 | 43.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.59 | 24.89 | 40.51 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.88 | 11.71 | 19.62 | 2.00 | 62.9 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.69 | 6.28 | 0.00 | 20.3 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.26 | 26.75 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.09 | 14.03 | 23.41 | 8.00 | 79.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.09 | 12.85 | 22.46 | 6.00 | 72.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.23 | 12.37 | 21.09 | 3.00 | 68.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.84 | 19.26 | 4.00 | 75.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.73
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.94) beats the best remaining Bench Boost opportunity (4.55).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.03, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.94) beats the best remaining Bench Boost opportunity (4.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.77 | 12.47 | 19.76 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.00 | 0.04 | 0.30 | 0.00 | 0.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 12.62 | 20.45 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.20 | 16.97 | 1.00 | 84.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.68 | 10.01 | 15.85 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.04 | 4.46 | 9.46 | 0.00 | 23.3 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.10 | 3.26 | 5.64 | 1.00 | 31.6 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.44 | 23.23 | 38.50 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.49 | 17.73 | 27.88 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.80 | 5.44 | 8.48 | 0.00 | 38.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.52 | 20.65 | 33.82 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.40 | 14.39 | 23.79 | 2.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.23 | 12.08 | 19.56 | 3.00 | 78.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.97 | 11.67 | 19.79 | 6.00 | 70.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.06 | 11.30 | 19.82 | 2.00 | 65.9 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.78
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.69, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.38 | 9.97 | 16.16 | 7.00 | 79.1 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.04 | 0.15 | 0.00 | 0.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.97 | 11.78 | 19.18 | 1.00 | 86.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.73 | 10.89 | 17.65 | 1.00 | 84.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.10 | 9.05 | 14.45 | 0.00 | 79.5 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.17 | 4.00 | 9.02 | 0.00 | 20.1 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.80 | 6.95 | 0.00 | 47.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.70 | 24.52 | 40.07 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.38 | 10.90 | 17.37 | 2.00 | 46.8 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.91 | 2.87 | 4.66 | 0.00 | 16.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.24 | 19.34 | 31.43 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.32 | 18.42 | 28.44 | 3.00 | 79.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.08 | 15.74 | 24.70 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.61 | 14.00 | 22.65 | 11.00 | 76.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.75 | 18.78 | 4.00 | 76.2 | 90.0 |