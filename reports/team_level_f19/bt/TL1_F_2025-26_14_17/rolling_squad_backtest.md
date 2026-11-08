# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 263.34
- Total actual points: 285.00
- Average predicted points: 65.83
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
- Predicted score: 65.87
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.94 | 11.22 | 17.88 | 6.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.35 | 0.63 | 0.62 | 0.00 | 2.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.65 | 13.29 | 20.89 | 1.00 | 86.0 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.61 | 12.88 | 20.13 | 14.00 | 85.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.30 | 11.50 | 18.73 | 8.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.80 | 8.04 | 12.49 | 4.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.32 | 6.53 | 10.89 | 0.00 | 75.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.89 | 23.44 | 38.27 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.42 | 15.09 | 23.72 | 2.00 | 88.1 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.83 | 2.80 | 4.77 | 1.00 | 11.1 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.11 | 17.29 | 27.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.91 | 25.76 | 2.00 | 87.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.40 | 15.59 | 25.45 | 3.00 | 87.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.11 | 14.30 | 23.74 | 4.00 | 81.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.92 | 13.17 | 21.24 | 2.00 | 89.3 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.74
- Actual score: 58.00
- Transfer: Jurriën Timber -> Marc Cucurella Saseta (projected gain 0.69, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 11.07 | 17.87 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.04 | 0.34 | 0.51 | 0.00 | 2.8 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.96 | 14.45 | 23.05 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.97 | 11.73 | 19.29 | 6.00 | 85.6 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.92 | 11.51 | 18.42 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.28 | 9.04 | 14.59 | 3.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.43 | 4.36 | 7.44 | 0.00 | 43.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.64 | 25.07 | 40.61 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.85 | 11.68 | 19.69 | 2.00 | 63.1 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.01 | 3.64 | 6.25 | 0.00 | 19.9 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.75 | 16.13 | 26.69 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.04 | 13.95 | 23.49 | 8.00 | 79.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.08 | 12.80 | 22.39 | 6.00 | 73.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.26 | 12.52 | 21.41 | 3.00 | 67.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.91 | 12.05 | 19.66 | 4.00 | 75.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.38
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.82) beats the best remaining Bench Boost opportunity (4.42).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.82) beats the best remaining Bench Boost opportunity (4.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.70 | 12.18 | 19.46 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.06 | 0.14 | 0.30 | 0.00 | 1.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.24 | 12.56 | 20.37 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.22 | 16.98 | 1.00 | 84.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.57 | 9.74 | 15.46 | 1.00 | 84.1 | 90.0 |
| Bench 3 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.01 | 4.60 | 9.83 | 0.00 | 22.6 | 0.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.98 | 2.97 | 5.26 | 1.00 | 31.3 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.39 | 23.16 | 38.47 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.60 | 17.94 | 27.94 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.77 | 5.39 | 8.41 | 0.00 | 38.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.53 | 20.59 | 33.68 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.31 | 14.13 | 23.59 | 2.00 | 84.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.37 | 20.01 | 3.00 | 78.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.94 | 11.83 | 20.16 | 6.00 | 69.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.02 | 11.35 | 20.09 | 2.00 | 65.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.35
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.46, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.32 | 9.90 | 16.12 | 7.00 | 78.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.10 | 0.33 | 0.00 | 1.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.95 | 11.68 | 19.11 | 1.00 | 86.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.79 | 11.02 | 17.74 | 1.00 | 84.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.00 | 8.79 | 14.08 | 0.00 | 79.5 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.10 | 4.13 | 9.44 | 0.00 | 17.6 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.20 | 3.48 | 6.44 | 0.00 | 48.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.61 | 24.34 | 39.93 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.38 | 10.95 | 17.66 | 2.00 | 46.8 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.77 | 4.61 | 0.00 | 15.9 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.27 | 19.40 | 31.52 | 1.00 | 90.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 6.25 | 18.27 | 28.29 | 3.00 | 79.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 6.12 | 15.92 | 24.96 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.55 | 13.91 | 22.60 | 11.00 | 75.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.91 | 19.12 | 4.00 | 76.1 | 90.0 |