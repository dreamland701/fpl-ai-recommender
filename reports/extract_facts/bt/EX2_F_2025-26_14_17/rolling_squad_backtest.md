# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.25
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
- Predicted score: 65.16
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.94 | 11.29 | 18.06 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.14 | 0.33 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.61 | 13.26 | 20.92 | 1.00 | 83.6 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.49 | 12.67 | 20.01 | 14.00 | 82.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.18 | 11.31 | 18.66 | 8.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.82 | 8.11 | 12.83 | 4.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.35 | 6.61 | 11.25 | 0.00 | 73.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.86 | 23.46 | 38.29 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.29 | 14.82 | 23.54 | 2.00 | 85.6 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.89 | 5.06 | 1.00 | 13.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.05 | 17.19 | 27.62 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.62 | 15.88 | 25.70 | 2.00 | 85.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.37 | 15.59 | 25.54 | 3.00 | 85.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.21 | 23.64 | 4.00 | 81.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.79 | 12.88 | 20.81 | 2.00 | 86.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.07
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.55, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 11.27 | 18.12 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.19 | 0.34 | 0.00 | 6.1 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.52 | 23.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.03 | 11.85 | 19.37 | 6.00 | 86.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.96 | 11.63 | 18.50 | 2.00 | 88.4 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.39 | 9.37 | 15.06 | 3.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.21 | 3.98 | 7.09 | 0.00 | 36.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.83 | 25.45 | 41.55 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.96 | 11.91 | 19.88 | 2.00 | 64.2 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.20 | 4.00 | 6.62 | 0.00 | 24.7 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.72 | 16.11 | 26.61 | 18.00 | 88.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.09 | 14.09 | 23.63 | 8.00 | 79.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.36 | 12.68 | 21.52 | 3.00 | 70.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.59 | 12.19 | 22.66 | 6.00 | 63.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.91 | 19.35 | 4.00 | 76.2 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.21
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.17) beats the best remaining Bench Boost opportunity (3.65).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.17) beats the best remaining Bench Boost opportunity (3.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.77 | 12.45 | 19.65 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 3.9 | 0.22 | 0.36 | 0.47 | 0.00 | 5.8 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 12.62 | 20.40 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.47 | 10.23 | 17.01 | 1.00 | 84.7 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.70 | 10.04 | 15.90 | 1.00 | 84.5 | 90.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.03 | 3.61 | 6.55 | 1.00 | 29.6 | 76.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 1.82 | 5.39 | 0.00 | 8.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.46 | 23.32 | 38.58 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.44 | 17.44 | 27.23 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.92 | 5.65 | 8.67 | 0.00 | 41.8 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.39 | 20.26 | 33.25 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.59 | 16.16 | 26.25 | 2.00 | 77.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.17 | 19.68 | 3.00 | 79.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.08 | 12.02 | 20.34 | 6.00 | 72.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.14 | 11.63 | 20.49 | 2.00 | 66.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.82
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.56, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.94) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.44 | 10.17 | 16.43 | 7.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.08 | 0.23 | 0.38 | 0.00 | 5.7 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.01 | 11.89 | 19.28 | 1.00 | 87.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.77 | 10.95 | 17.67 | 1.00 | 84.7 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 9.13 | 14.55 | 0.00 | 80.2 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.41 | 4.71 | 10.17 | 0.00 | 25.0 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.97 | 3.07 | 6.05 | 0.00 | 41.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.94 | 25.08 | 41.05 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.13 | 10.50 | 17.35 | 2.00 | 44.7 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.11 | 4.93 | 0.00 | 20.1 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.17 | 19.17 | 31.20 | 1.00 | 88.7 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.52 | 18.87 | 29.24 | 3.00 | 85.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.26 | 16.17 | 25.55 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.12 | 22.81 | 11.00 | 76.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.86 | 18.90 | 4.00 | 77.3 | 90.0 |