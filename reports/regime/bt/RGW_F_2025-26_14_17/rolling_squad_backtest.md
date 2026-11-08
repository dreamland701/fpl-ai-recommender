# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 257.71
- Total actual points: 272.00
- Average predicted points: 64.43
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
- Predicted score: 65.35
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.00 | 11.44 | 17.95 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.00 | 0.18 | 0.31 | 0.00 | 1.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.87 | 13.92 | 21.97 | 1.00 | 88.4 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.67 | 13.10 | 20.65 | 14.00 | 86.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.57 | 13.01 | 20.86 | 1.00 | 88.1 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.89 | 8.21 | 12.68 | 4.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.49 | 6.88 | 11.42 | 0.00 | 75.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.75 | 23.65 | 38.54 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.22 | 14.47 | 22.91 | 2.00 | 87.3 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.66 | 2.18 | 3.80 | 1.00 | 12.2 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.08 | 17.25 | 27.38 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.58 | 15.71 | 25.21 | 2.00 | 86.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.34 | 15.29 | 24.85 | 3.00 | 87.6 | 82.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.76 | 13.32 | 20.69 | 2.00 | 79.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.75 | 12.54 | 20.06 | 2.00 | 87.1 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.56
- Actual score: 59.00
- Transfer: Enzo Fernández -> Yankuba Minteh (projected gain 1.07, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 11.09 | 17.79 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.02 | 0.16 | 0.16 | 0.00 | 1.4 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.02 | 14.84 | 23.64 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.04 | 12.16 | 19.93 | 6.00 | 86.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.69 | 11.44 | 18.87 | 3.00 | 69.8 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.34 | 9.19 | 14.67 | 3.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.56 | 4.81 | 8.14 | 0.00 | 42.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.34 | 24.77 | 40.14 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.70 | 11.32 | 19.14 | 2.00 | 61.9 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.91 | 3.17 | 5.31 | 0.00 | 21.0 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.76 | 16.05 | 26.39 | 18.00 | 89.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 4.93 | 13.77 | 23.07 | 8.00 | 78.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.92 | 12.30 | 21.61 | 6.00 | 72.5 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.3 | 4.34 | 12.03 | 19.14 | 3.00 | 78.2 | 71.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.72 | 11.33 | 18.56 | 4.00 | 75.0 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.34
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (4.27).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 9.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.71) beats the best remaining Bench Boost opportunity (4.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.70 | 12.27 | 19.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | James Wright | GK | 2 | 3.9 | 0.02 | 0.09 | 0.23 | 0.00 | 0.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.32 | 13.03 | 21.07 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.40 | 11.82 | 19.19 | 2.00 | 81.8 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.59 | 9.74 | 15.37 | 1.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.95 | 4.80 | 10.21 | 0.00 | 23.9 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.12 | 3.50 | 6.12 | 1.00 | 31.6 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.32 | 23.21 | 38.31 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.55 | 17.15 | 26.67 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.62 | 4.91 | 7.48 | 0.00 | 38.4 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.52 | 20.36 | 33.20 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.17 | 13.84 | 22.72 | 2.00 | 84.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.05 | 11.62 | 18.79 | 3.00 | 76.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.76 | 10.96 | 19.36 | 2.00 | 65.1 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.2 | 2.75 | 8.69 | 14.77 | 2.00 | 56.4 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.46
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.37, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.28 | 9.64 | 15.50 | 7.00 | 79.0 | 90.0 |
| Bench 1 | Bench | James Wright | GK | 2 | 3.9 | 0.04 | 0.07 | 0.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.99 | 12.05 | 19.45 | 1.00 | 87.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.85 | 10.90 | 17.86 | 6.00 | 76.9 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.08 | 8.86 | 14.13 | 0.00 | 79.5 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.42 | 4.07 | 7.31 | 0.00 | 49.7 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.14 | 3.63 | 8.42 | 0.00 | 21.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.40 | 24.03 | 38.84 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.30 | 10.34 | 16.39 | 2.00 | 49.2 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.76 | 2.19 | 3.68 | 0.00 | 15.7 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.25 | 18.72 | 30.82 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.42 | 17.75 | 27.44 | 3.00 | 81.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.48 | 13.45 | 21.80 | 11.00 | 75.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.77 | 11.55 | 18.36 | 4.00 | 75.0 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 6 | 6.1 | 3.83 | 10.78 | 17.67 | 3.00 | 73.8 | 70.0 |