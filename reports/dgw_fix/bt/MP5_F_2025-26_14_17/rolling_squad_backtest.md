# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 262.85
- Total actual points: 270.00
- Average predicted points: 65.71
- Average actual points: 67.50
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
- Predicted score: 65.79
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.07 | 11.53 | 18.50 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.08 | 0.23 | 0.00 | 1.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.74 | 13.28 | 20.99 | 1.00 | 86.8 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.50 | 12.67 | 19.91 | 14.00 | 83.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.45 | 12.66 | 20.37 | 1.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.96 | 8.45 | 13.17 | 4.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.43 | 6.76 | 11.15 | 0.00 | 75.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.97 | 24.10 | 39.48 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.38 | 14.70 | 23.36 | 2.00 | 88.2 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.74 | 2.49 | 4.40 | 1.00 | 10.5 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.07 | 17.33 | 27.75 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 15.96 | 25.85 | 2.00 | 86.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.42 | 15.50 | 25.38 | 3.00 | 87.6 | 82.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.73 | 13.20 | 20.59 | 2.00 | 79.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.86 | 12.96 | 20.69 | 2.00 | 88.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.83
- Actual score: 64.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 4.37, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.88 | 11.37 | 18.48 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.08 | 0.19 | 0.30 | 0.00 | 1.1 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.94 | 14.57 | 23.20 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.65 | 13.47 | 21.12 | 8.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.96 | 11.92 | 19.45 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.41 | 9.40 | 15.24 | 3.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.37 | 4.42 | 7.51 | 0.00 | 40.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.59 | 25.40 | 41.49 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.82 | 11.71 | 19.69 | 2.00 | 61.6 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.10 | 3.75 | 6.42 | 0.00 | 21.6 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.66 | 16.05 | 26.28 | 18.00 | 88.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.04 | 14.03 | 23.53 | 8.00 | 78.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.00 | 12.68 | 22.15 | 6.00 | 70.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.81 | 11.60 | 18.74 | 4.00 | 74.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 3.90 | 11.14 | 18.01 | 3.00 | 74.3 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.00
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.95).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 21.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.42) beats the best remaining Bench Boost opportunity (3.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.91 | 12.75 | 20.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.11 | 0.25 | 0.00 | 0.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.85 | 13.93 | 22.32 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.26 | 12.77 | 20.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.72 | 10.19 | 16.18 | 1.00 | 84.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.60 | 4.36 | 9.20 | 0.00 | 14.2 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.93 | 2.96 | 5.24 | 1.00 | 28.1 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.45 | 23.66 | 39.55 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.69 | 17.33 | 27.31 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.89 | 5.51 | 8.45 | 0.00 | 40.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.53 | 20.45 | 33.38 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.29 | 14.12 | 23.32 | 2.00 | 82.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.14 | 11.88 | 19.16 | 3.00 | 76.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.82 | 11.24 | 19.64 | 2.00 | 61.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 3.40 | 10.68 | 17.67 | 3.00 | 71.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 2.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.22
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 20.86, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.46 | 10.17 | 16.43 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.07 | 0.11 | 0.23 | 0.00 | 1.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.76 | 13.08 | 20.64 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.76 | 19.17 | 1.00 | 86.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.12 | 9.11 | 14.55 | 0.00 | 79.9 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.29 | 3.70 | 6.77 | 0.00 | 47.7 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.50 | 2.00 | 5.84 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.73 | 25.09 | 41.27 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.30 | 10.21 | 16.24 | 2.00 | 45.3 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.86 | 2.68 | 4.26 | 0.00 | 15.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.19 | 18.64 | 30.40 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 17.46 | 27.09 | 3.00 | 79.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.50 | 13.46 | 21.78 | 11.00 | 73.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.38 | 18.48 | 4.00 | 73.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 3.70 | 11.36 | 18.68 | 1.00 | 77.2 | 36.0 |