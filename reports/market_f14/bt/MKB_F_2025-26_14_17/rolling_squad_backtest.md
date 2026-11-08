# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 265.39
- Total actual points: 289.00
- Average predicted points: 66.35
- Average actual points: 72.25
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
- Predicted score: 65.93
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 11.60 | 18.42 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.79 | 13.58 | 21.24 | 1.00 | 86.4 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.54 | 12.71 | 19.90 | 14.00 | 83.4 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.20 | 11.27 | 18.37 | 8.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.95 | 8.34 | 13.03 | 4.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.41 | 6.72 | 11.23 | 0.00 | 75.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.92 | 23.57 | 38.39 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.39 | 14.93 | 23.56 | 2.00 | 88.0 | 63.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.79 | 2.65 | 4.67 | 1.00 | 10.1 | 13.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.08 | 17.25 | 27.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.64 | 15.92 | 25.63 | 2.00 | 86.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.48 | 15.75 | 25.56 | 3.00 | 87.1 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 5.03 | 13.97 | 23.20 | 4.00 | 81.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.81 | 12.85 | 20.56 | 2.00 | 88.4 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.59
- Actual score: 61.00
- Transfer: Maxence Lacroix -> Marc Guéhi (projected gain 1.76, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.92 | 11.45 | 18.38 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.91 | 14.39 | 22.91 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.62 | 13.17 | 20.54 | 8.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.69 | 11.28 | 18.43 | 3.00 | 67.9 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.39 | 9.35 | 15.05 | 3.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.37 | 4.29 | 7.25 | 0.00 | 40.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.53 | 24.78 | 40.36 | 2.00 | 90.0 | 68.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.77 | 11.47 | 19.30 | 2.00 | 61.7 | 65.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 1.15 | 3.97 | 6.69 | 0.00 | 21.4 | 58.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.65 | 15.94 | 26.23 | 18.00 | 88.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.01 | 13.87 | 23.19 | 8.00 | 78.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.07 | 12.72 | 22.17 | 6.00 | 70.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.12 | 12.17 | 20.85 | 3.00 | 67.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.76 | 11.61 | 18.94 | 4.00 | 74.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.41
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.48) beats the best remaining Bench Boost opportunity (4.03).
- Transfer: Jean-Philippe Mateta -> Igor Thiago Nascimento Rodrigues (projected gain 12.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.48) beats the best remaining Bench Boost opportunity (4.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.98 | 12.89 | 20.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.79 | 13.70 | 21.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.50 | 11.77 | 19.23 | 2.00 | 80.3 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.71 | 10.09 | 15.97 | 1.00 | 84.8 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 0.59 | 3.58 | 8.29 | 0.00 | 14.3 | 0.0 |
| Bench 3 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 0.93 | 2.87 | 5.04 | 1.00 | 27.9 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.34 | 23.07 | 38.27 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.66 | 17.95 | 28.04 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.2 | 1.97 | 5.79 | 8.88 | 0.00 | 39.7 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.45 | 20.43 | 33.42 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.36 | 14.24 | 23.62 | 2.00 | 83.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.10 | 11.77 | 19.15 | 3.00 | 76.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.82 | 11.45 | 19.56 | 6.00 | 67.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.77 | 10.76 | 19.15 | 2.00 | 61.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.46
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.29, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.54 | 10.35 | 16.64 | 7.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.78 | 13.32 | 20.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.81 | 11.03 | 18.16 | 6.00 | 73.4 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.14 | 9.17 | 14.64 | 0.00 | 80.0 | 0.0 |
| Bench 2 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.32 | 3.81 | 6.86 | 0.00 | 47.7 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 0.55 | 2.65 | 7.18 | 0.00 | 5.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.68 | 24.57 | 40.21 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.33 | 10.78 | 17.20 | 2.00 | 45.2 | 90.0 |
| Bench 3 | Bench | Marc Guiu Paz | FWD | 7 | 4.2 | 0.88 | 2.84 | 4.58 | 0.00 | 15.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.16 | 19.11 | 31.09 | 1.00 | 90.0 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.39 | 18.61 | 28.72 | 3.00 | 79.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.99 | 15.54 | 24.44 | 10.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.56 | 13.85 | 22.44 | 11.00 | 73.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.73 | 11.45 | 18.37 | 4.00 | 73.9 | 90.0 |