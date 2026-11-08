# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 263.68
- Total actual points: 285.00
- Average predicted points: 65.92
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
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 11.37 | 18.06 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.14 | 0.18 | 0.21 | 0.00 | 3.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.68 | 13.38 | 20.99 | 1.00 | 85.4 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.56 | 12.79 | 20.07 | 14.00 | 84.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.24 | 11.41 | 18.73 | 8.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.90 | 8.24 | 12.85 | 4.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.40 | 6.72 | 11.29 | 0.00 | 74.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.96 | 23.63 | 38.40 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.36 | 14.95 | 23.61 | 2.00 | 87.5 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.82 | 2.79 | 4.88 | 1.00 | 11.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.11 | 17.30 | 27.69 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.68 | 16.00 | 25.77 | 2.00 | 87.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.44 | 15.72 | 25.62 | 3.00 | 87.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.13 | 14.27 | 23.65 | 4.00 | 81.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.89 | 13.05 | 20.91 | 2.00 | 89.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.80
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.63, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 11.21 | 18.07 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.08 | 0.11 | 0.18 | 0.00 | 2.8 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.97 | 14.50 | 23.05 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.81 | 19.35 | 6.00 | 85.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.95 | 11.60 | 18.48 | 2.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.38 | 9.35 | 15.05 | 3.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.52 | 4.70 | 7.95 | 0.00 | 43.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.62 | 24.98 | 40.56 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.93 | 11.87 | 19.88 | 2.00 | 63.4 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.05 | 3.73 | 6.35 | 0.00 | 20.4 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.80 | 16.27 | 26.70 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.14 | 14.19 | 23.66 | 8.00 | 80.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.31 | 12.59 | 21.43 | 3.00 | 69.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.82 | 12.06 | 22.53 | 6.00 | 67.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.87 | 11.89 | 19.36 | 4.00 | 75.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.70
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.89) beats the best remaining Bench Boost opportunity (3.31).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.89) beats the best remaining Bench Boost opportunity (3.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.75 | 12.43 | 19.65 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.02 | 0.00 | 1.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.25 | 12.59 | 20.39 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.22 | 16.99 | 1.00 | 84.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.68 | 10.02 | 15.88 | 1.00 | 84.1 | 90.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.09 | 3.30 | 5.75 | 1.00 | 31.5 | 76.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 1.63 | 5.55 | 0.00 | 3.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.44 | 23.31 | 38.58 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.44 | 17.46 | 27.32 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.79 | 5.44 | 8.45 | 0.00 | 38.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.48 | 20.46 | 33.41 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.36 | 14.53 | 24.56 | 2.00 | 79.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.25 | 12.15 | 19.68 | 3.00 | 78.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.05 | 11.98 | 20.30 | 6.00 | 71.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.18 | 11.72 | 20.52 | 2.00 | 67.3 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.21
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 10.40, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.72) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.40 | 10.11 | 16.38 | 7.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.05 | 0.00 | 0.08 | 0.00 | 1.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 11.85 | 19.27 | 1.00 | 86.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.75 | 10.93 | 17.69 | 1.00 | 84.2 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.10 | 9.09 | 14.53 | 0.00 | 79.5 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.27 | 4.50 | 10.03 | 0.00 | 21.0 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.30 | 3.79 | 6.90 | 0.00 | 48.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.72 | 24.64 | 40.22 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.10 | 10.27 | 17.58 | 2.00 | 42.5 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.90 | 2.90 | 4.72 | 0.00 | 16.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.92 | 19.81 | 30.59 | 3.00 | 86.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.24 | 19.32 | 31.32 | 1.00 | 90.0 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.04 | 15.72 | 24.72 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.62 | 14.09 | 22.84 | 11.00 | 76.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.88 | 11.83 | 18.92 | 4.00 | 76.6 | 90.0 |