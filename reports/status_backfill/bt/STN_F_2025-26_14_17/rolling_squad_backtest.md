# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.55
- Total actual points: 285.00
- Average predicted points: 66.14
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
- Predicted score: 66.66
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.06 | 11.39 | 18.12 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.12 | 0.19 | 0.22 | 0.00 | 3.2 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.88 | 13.45 | 21.11 | 1.00 | 89.2 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.56 | 12.79 | 20.10 | 14.00 | 84.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.23 | 11.42 | 18.70 | 8.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.88 | 8.25 | 12.87 | 4.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.43 | 6.75 | 11.29 | 0.00 | 75.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.89 | 23.60 | 38.44 | 14.00 | 107.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.50 | 14.98 | 23.68 | 2.00 | 90.7 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.77 | 2.75 | 4.82 | 1.00 | 10.4 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.22 | 17.38 | 27.80 | 4.00 | 100.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.69 | 15.97 | 25.75 | 2.00 | 88.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.54 | 15.73 | 25.63 | 3.00 | 89.7 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.23 | 14.22 | 23.58 | 4.00 | 85.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.98 | 13.11 | 20.99 | 2.00 | 90.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.08
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.64, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 11.19 | 18.09 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.07 | 0.11 | 0.18 | 0.00 | 2.6 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.96 | 14.53 | 23.13 | 0.00 | 95.5 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.93 | 11.80 | 19.36 | 6.00 | 84.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.87 | 11.59 | 18.48 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.36 | 9.34 | 15.05 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.53 | 4.69 | 7.92 | 0.00 | 43.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.58 | 24.93 | 40.60 | 2.00 | 113.3 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.74 | 11.75 | 19.75 | 2.00 | 61.2 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.70 | 6.32 | 0.00 | 19.9 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.82 | 16.26 | 26.75 | 18.00 | 92.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.98 | 14.06 | 23.52 | 8.00 | 78.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.02 | 12.91 | 22.54 | 6.00 | 72.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 3.95 | 12.41 | 21.22 | 3.00 | 64.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.84 | 11.87 | 19.35 | 4.00 | 74.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.68
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.29) beats the best remaining Bench Boost opportunity (3.79).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 12.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.29) beats the best remaining Bench Boost opportunity (3.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.91 | 12.48 | 19.75 | 2.00 | 97.6 | 90.0 |
| Bench 1 | Bench Boost | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.03 | 0.00 | 1.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.24 | 12.61 | 20.44 | 6.00 | 91.2 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.40 | 10.19 | 16.98 | 1.00 | 83.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.64 | 10.02 | 15.90 | 1.00 | 83.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.40 | 4.57 | 9.85 | 0.00 | 10.8 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.07 | 3.27 | 5.73 | 1.00 | 31.1 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.40 | 23.27 | 38.63 | 13.00 | 98.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 7.07 | 17.69 | 27.70 | 2.00 | 106.5 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.82 | 5.44 | 8.47 | 0.00 | 37.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.88 | 20.63 | 33.69 | 13.00 | 120.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.40 | 14.39 | 23.85 | 2.00 | 85.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.17 | 12.11 | 19.65 | 3.00 | 76.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.74 | 11.71 | 19.98 | 6.00 | 67.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.67 | 11.36 | 20.08 | 2.00 | 58.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.13
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.90, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.34 | 10.03 | 16.30 | 7.00 | 78.9 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.05 | 0.00 | 0.08 | 0.00 | 1.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.93 | 11.80 | 19.23 | 1.00 | 85.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.75 | 10.90 | 17.66 | 1.00 | 84.2 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.09 | 9.08 | 14.53 | 0.00 | 79.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.93 | 4.00 | 9.36 | 0.00 | 13.5 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.27 | 3.78 | 6.91 | 0.00 | 47.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.67 | 24.57 | 40.21 | 16.00 | 113.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.29 | 10.99 | 17.57 | 2.00 | 43.6 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.92 | 2.88 | 4.70 | 0.00 | 15.8 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.36 | 19.36 | 31.45 | 1.00 | 92.5 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.61 | 18.47 | 28.53 | 3.00 | 82.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.29 | 15.70 | 24.71 | 10.00 | 98.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.01 | 22.75 | 11.00 | 76.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.82 | 11.78 | 18.86 | 4.00 | 75.7 | 90.0 |