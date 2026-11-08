# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 260.50
- Total actual points: 272.00
- Average predicted points: 65.12
- Average actual points: 68.00
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
- Predicted score: 65.75
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 11.30 | 17.81 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.23 | 0.34 | 0.00 | 1.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.80 | 13.80 | 21.73 | 1.00 | 87.5 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.64 | 13.10 | 20.64 | 14.00 | 86.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.61 | 13.09 | 20.99 | 1.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.91 | 8.32 | 12.98 | 4.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.45 | 6.89 | 11.54 | 0.00 | 75.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.92 | 23.58 | 38.46 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.24 | 14.57 | 23.00 | 2.00 | 87.9 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.65 | 2.27 | 4.03 | 1.00 | 11.0 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.12 | 17.27 | 27.59 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.62 | 15.83 | 25.48 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.32 | 15.29 | 24.84 | 3.00 | 86.9 | 82.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.75 | 13.39 | 20.81 | 2.00 | 79.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.81 | 12.73 | 20.28 | 2.00 | 87.3 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.37
- Actual score: 59.00
- Transfer: Enzo Fernández -> Yankuba Minteh (projected gain 0.80, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.77 | 11.09 | 17.79 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.02 | 0.21 | 0.26 | 0.00 | 1.6 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.06 | 14.79 | 23.55 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.09 | 12.10 | 19.85 | 6.00 | 87.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.72 | 11.47 | 18.84 | 3.00 | 69.8 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.37 | 9.34 | 15.03 | 3.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.56 | 4.82 | 8.17 | 0.00 | 44.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.56 | 24.88 | 40.55 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.74 | 11.37 | 19.10 | 2.00 | 62.8 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 3.25 | 5.56 | 0.00 | 19.4 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.79 | 16.25 | 26.69 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.03 | 13.90 | 23.24 | 8.00 | 79.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.99 | 12.47 | 21.78 | 6.00 | 72.1 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.3 | 4.29 | 11.95 | 19.00 | 3.00 | 77.5 | 71.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.76 | 11.51 | 18.72 | 4.00 | 73.6 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.17
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.90) beats the best remaining Bench Boost opportunity (4.50).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.90) beats the best remaining Bench Boost opportunity (4.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.76 | 12.36 | 19.46 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.02 | 0.13 | 0.27 | 0.00 | 0.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.37 | 12.93 | 20.94 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.50 | 11.92 | 19.56 | 2.00 | 82.2 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.65 | 9.94 | 15.76 | 1.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.08 | 4.81 | 10.22 | 0.00 | 24.8 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.15 | 3.49 | 6.09 | 1.00 | 32.5 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.38 | 23.17 | 38.49 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.44 | 17.42 | 27.23 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.65 | 4.99 | 7.70 | 0.00 | 37.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.55 | 20.61 | 33.66 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.26 | 13.97 | 23.15 | 2.00 | 83.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.11 | 11.69 | 18.93 | 3.00 | 76.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.97 | 11.21 | 19.82 | 2.00 | 65.4 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 2.73 | 8.54 | 14.44 | 2.00 | 55.9 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.21
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.72, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.35 | 9.91 | 16.01 | 7.00 | 78.3 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.05 | 0.14 | 0.16 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.06 | 12.12 | 19.73 | 1.00 | 87.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.82 | 11.27 | 18.69 | 6.00 | 75.6 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.10 | 9.09 | 14.53 | 0.00 | 79.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.11 | 4.24 | 9.72 | 0.00 | 19.7 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.39 | 4.11 | 7.43 | 0.00 | 49.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.64 | 24.43 | 40.04 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.30 | 10.70 | 17.10 | 2.00 | 46.8 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.74 | 2.36 | 3.84 | 0.00 | 14.9 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.39 | 31.51 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.31 | 18.40 | 28.48 | 3.00 | 79.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.49 | 13.66 | 22.16 | 11.00 | 74.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.77 | 11.41 | 18.22 | 4.00 | 74.3 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.1 | 3.80 | 10.76 | 17.61 | 3.00 | 72.3 | 70.0 |