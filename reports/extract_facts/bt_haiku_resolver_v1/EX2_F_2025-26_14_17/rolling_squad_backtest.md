# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 263.24
- Total actual points: 285.00
- Average predicted points: 65.81
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
- Predicted score: 65.20
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.93 | 11.28 | 18.04 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.17 | 0.23 | 0.34 | 0.00 | 4.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.61 | 13.26 | 20.94 | 1.00 | 83.7 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.67 | 20.03 | 14.00 | 83.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.18 | 11.31 | 18.70 | 8.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.83 | 8.11 | 12.81 | 4.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.35 | 6.61 | 11.27 | 0.00 | 73.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.86 | 23.48 | 38.32 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.29 | 14.83 | 23.56 | 2.00 | 85.8 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.89 | 5.06 | 1.00 | 13.8 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.04 | 17.19 | 27.67 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.88 | 25.73 | 2.00 | 85.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 15.58 | 25.56 | 3.00 | 86.1 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.21 | 23.66 | 4.00 | 81.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.80 | 12.88 | 20.83 | 2.00 | 86.6 | 90.0 |

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
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.55, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 11.26 | 18.10 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.18 | 0.29 | 0.36 | 0.00 | 5.8 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.98 | 14.52 | 23.06 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.03 | 11.84 | 19.38 | 6.00 | 86.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.97 | 11.63 | 18.51 | 2.00 | 88.6 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.40 | 9.38 | 15.08 | 3.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.21 | 3.99 | 7.13 | 0.00 | 37.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.60 | 24.97 | 40.52 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.96 | 11.91 | 19.89 | 2.00 | 64.4 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.20 | 3.99 | 6.61 | 0.00 | 24.7 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.72 | 16.11 | 26.62 | 18.00 | 89.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.10 | 14.10 | 23.63 | 8.00 | 79.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.37 | 12.68 | 21.49 | 3.00 | 71.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.74 | 12.11 | 22.85 | 6.00 | 65.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 11.93 | 19.39 | 4.00 | 76.5 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.81
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.98) beats the best remaining Bench Boost opportunity (3.42).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.98) beats the best remaining Bench Boost opportunity (3.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.76 | 12.45 | 19.66 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alex Cairns | GK | 11 | 3.9 | 0.03 | 0.11 | 0.21 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 12.62 | 20.41 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.48 | 10.25 | 17.00 | 1.00 | 84.7 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.70 | 10.06 | 15.92 | 1.00 | 84.7 | 90.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.02 | 3.64 | 6.59 | 1.00 | 29.7 | 76.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.00 | 2.18 | 6.18 | 0.00 | 9.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.46 | 23.34 | 38.61 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.46 | 17.49 | 27.31 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.92 | 5.65 | 8.68 | 0.00 | 41.8 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.38 | 20.27 | 33.27 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.35 | 14.77 | 25.01 | 2.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.18 | 19.72 | 3.00 | 79.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.08 | 12.03 | 20.32 | 6.00 | 72.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.15 | 11.65 | 20.49 | 2.00 | 66.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.44
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 10.36, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.43 | 10.16 | 16.41 | 7.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.15 | 0.18 | 0.26 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.01 | 11.89 | 19.29 | 1.00 | 87.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.77 | 10.96 | 17.70 | 1.00 | 84.8 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 9.14 | 14.58 | 0.00 | 80.3 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.41 | 4.73 | 10.17 | 0.00 | 24.9 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 0.98 | 3.07 | 6.05 | 0.00 | 41.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.73 | 24.65 | 40.21 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.26 | 10.21 | 17.21 | 2.00 | 46.0 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.04 | 3.12 | 4.95 | 0.00 | 20.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.85 | 19.68 | 30.45 | 3.00 | 86.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.16 | 19.17 | 31.22 | 1.00 | 88.9 | 45.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.74 | 24.70 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.65 | 14.13 | 22.85 | 11.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.92 | 11.87 | 18.94 | 4.00 | 77.5 | 90.0 |