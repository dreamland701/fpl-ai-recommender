# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 264.11
- Total actual points: 270.00
- Average predicted points: 66.03
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
- Predicted score: 65.98
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.02 | 11.46 | 18.20 | 6.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.05 | 0.35 | 0.59 | 0.00 | 0.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.71 | 13.49 | 21.21 | 1.00 | 87.4 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.55 | 12.79 | 20.13 | 14.00 | 86.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.52 | 12.79 | 20.47 | 1.00 | 87.9 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.88 | 8.19 | 12.77 | 4.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.40 | 6.72 | 11.25 | 0.00 | 75.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.98 | 23.74 | 38.69 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.31 | 14.74 | 23.26 | 2.00 | 87.6 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.71 | 2.44 | 4.27 | 1.00 | 11.0 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.16 | 17.44 | 27.89 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.65 | 15.95 | 25.71 | 2.00 | 87.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.40 | 15.58 | 25.35 | 3.00 | 86.9 | 82.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.78 | 13.50 | 21.02 | 2.00 | 79.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.91 | 13.06 | 20.87 | 2.00 | 87.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.18
- Actual score: 64.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 1.68, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 11.24 | 18.14 | 2.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.24 | 0.52 | 0.76 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.97 | 14.49 | 23.08 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.52 | 12.86 | 20.03 | 8.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.00 | 11.81 | 19.39 | 6.00 | 86.6 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.35 | 9.27 | 14.91 | 3.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.51 | 4.66 | 7.89 | 0.00 | 44.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.63 | 25.03 | 40.79 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.82 | 11.55 | 19.38 | 2.00 | 62.5 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.96 | 3.42 | 5.81 | 0.00 | 19.4 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.84 | 16.40 | 26.97 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.06 | 14.01 | 23.43 | 8.00 | 79.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.07 | 12.75 | 22.25 | 6.00 | 72.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.86 | 11.83 | 19.23 | 4.00 | 73.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 3.98 | 11.26 | 18.40 | 3.00 | 75.0 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.54
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (4.60).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 10.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.97) beats the best remaining Bench Boost opportunity (4.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.80 | 12.53 | 19.80 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Benjamin Lecomte | GK | 10 | 3.9 | 0.18 | 0.48 | 0.82 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.70 | 13.39 | 21.22 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 12.64 | 20.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.65 | 9.94 | 15.75 | 1.00 | 84.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.99 | 4.52 | 9.78 | 0.00 | 24.3 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.08 | 3.27 | 5.74 | 1.00 | 32.4 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.45 | 23.34 | 38.74 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.51 | 17.59 | 27.51 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.73 | 5.17 | 7.96 | 0.00 | 37.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.60 | 20.76 | 33.92 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.35 | 14.24 | 23.57 | 2.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.21 | 12.00 | 19.42 | 3.00 | 76.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.00 | 11.31 | 19.99 | 2.00 | 65.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.6 | 3.44 | 10.81 | 18.05 | 3.00 | 71.9 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 2.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.42
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.80, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.38 | 10.06 | 16.33 | 7.00 | 76.3 | 90.0 |
| Bench 1 | Bench | Benjamin Lecomte | GK | 10 | 3.9 | 0.16 | 0.38 | 0.59 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.64 | 12.97 | 20.42 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.97 | 11.82 | 19.28 | 1.00 | 87.4 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.08 | 9.03 | 14.43 | 0.00 | 79.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 1.02 | 3.94 | 9.27 | 0.00 | 19.3 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.31 | 3.83 | 7.01 | 0.00 | 49.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.71 | 24.61 | 40.29 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.36 | 10.87 | 17.36 | 2.00 | 46.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.81 | 2.55 | 4.10 | 0.00 | 15.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.32 | 19.54 | 31.76 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.36 | 18.59 | 28.74 | 3.00 | 79.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.57 | 13.93 | 22.57 | 11.00 | 74.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.84 | 11.68 | 18.64 | 4.00 | 74.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 3.76 | 11.66 | 19.29 | 1.00 | 78.2 | 36.0 |