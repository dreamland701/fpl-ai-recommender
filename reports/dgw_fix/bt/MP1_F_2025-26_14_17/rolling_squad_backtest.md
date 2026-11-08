# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 262.57
- Total actual points: 285.00
- Average predicted points: 65.64
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
- Predicted score: 65.84
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.07 | 11.53 | 18.38 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.74 | 13.50 | 21.19 | 1.00 | 86.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.65 | 19.86 | 14.00 | 83.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.14 | 11.17 | 18.26 | 8.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.96 | 8.39 | 13.11 | 4.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.43 | 6.75 | 11.26 | 0.00 | 75.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.97 | 23.68 | 38.57 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.38 | 14.98 | 23.68 | 2.00 | 88.2 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.74 | 2.56 | 4.58 | 1.00 | 10.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.07 | 17.21 | 27.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.89 | 25.59 | 2.00 | 86.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.42 | 15.66 | 25.48 | 3.00 | 87.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.09 | 14.11 | 23.40 | 4.00 | 81.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.86 | 12.98 | 20.76 | 2.00 | 88.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.34
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.56, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.88 | 11.35 | 18.29 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.13 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.94 | 14.44 | 22.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.72 | 19.22 | 6.00 | 85.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.88 | 11.44 | 18.24 | 2.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.41 | 9.41 | 15.15 | 3.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.37 | 4.32 | 7.30 | 0.00 | 40.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.59 | 24.92 | 40.55 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.82 | 11.59 | 19.46 | 2.00 | 61.6 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.10 | 3.82 | 6.46 | 0.00 | 21.6 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.66 | 15.96 | 26.28 | 18.00 | 88.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.04 | 13.95 | 23.31 | 8.00 | 78.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.00 | 12.59 | 22.02 | 6.00 | 70.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.18 | 12.28 | 20.98 | 3.00 | 67.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.73 | 19.09 | 4.00 | 74.7 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.95
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.95).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 11.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.91 | 12.76 | 20.08 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.61 | 20.43 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.72 | 10.11 | 15.99 | 1.00 | 84.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.38 | 10.04 | 16.73 | 1.00 | 82.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.60 | 3.59 | 8.29 | 0.00 | 14.2 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.93 | 2.87 | 5.02 | 1.00 | 28.1 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.45 | 23.32 | 38.63 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.69 | 18.04 | 28.17 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.89 | 5.61 | 8.65 | 0.00 | 40.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.53 | 20.57 | 33.61 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.29 | 14.14 | 23.46 | 2.00 | 82.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.14 | 11.86 | 19.27 | 3.00 | 76.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.82 | 11.41 | 19.48 | 6.00 | 67.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.82 | 10.86 | 19.29 | 2.00 | 61.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.44
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.05, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.46 | 10.19 | 16.47 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.72 | 19.10 | 1.00 | 86.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.62 | 10.61 | 17.21 | 1.00 | 81.7 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.12 | 9.11 | 14.54 | 0.00 | 79.9 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.29 | 3.71 | 6.72 | 0.00 | 47.7 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.50 | 2.57 | 7.06 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.73 | 24.65 | 40.30 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.30 | 10.73 | 17.13 | 2.00 | 45.3 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.86 | 2.75 | 4.43 | 0.00 | 15.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.19 | 19.16 | 31.14 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.43 | 28.43 | 3.00 | 79.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.05 | 15.68 | 24.66 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.50 | 13.73 | 22.31 | 11.00 | 73.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.48 | 18.39 | 4.00 | 73.9 | 90.0 |