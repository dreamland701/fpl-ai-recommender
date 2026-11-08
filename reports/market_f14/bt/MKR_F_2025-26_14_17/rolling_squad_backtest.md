# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 268.30
- Total actual points: 283.00
- Average predicted points: 67.08
- Average actual points: 70.75
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
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.35 | 11.95 | 18.81 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.98 | 13.81 | 21.47 | 1.00 | 86.3 | 46.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.72 | 13.00 | 20.75 | 4.00 | 87.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.63 | 12.72 | 19.84 | 14.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.00 | 8.25 | 12.83 | 4.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.51 | 6.77 | 11.16 | 0.00 | 74.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.90 | 23.40 | 37.99 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.41 | 14.77 | 23.41 | 2.00 | 89.2 | 63.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.74 | 12.89 | 21.47 | 1.00 | 68.1 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.08 | 17.64 | 27.88 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.65 | 16.28 | 25.93 | 2.00 | 84.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.70 | 16.08 | 25.86 | 3.00 | 86.6 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.73 | 12.45 | 20.17 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.42 | 6.59 | 10.31 | 2.00 | 49.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nick Woltemade
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.78
- Actual score: 54.00
- Transfer: Jean-Philippe Mateta -> Nick Woltemade (projected gain 3.97, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.05 | 11.35 | 18.20 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.77 | 14.01 | 22.51 | 0.00 | 90.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.22 | 11.71 | 19.33 | 2.00 | 86.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.82 | 11.30 | 18.43 | 3.00 | 68.5 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.12 | 8.78 | 14.40 | 3.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.28 | 4.29 | 7.20 | 0.00 | 40.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.46 | 24.81 | 39.66 | 2.00 | 90.0 | 68.0 |
| Vice Captain | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.69 | 15.21 | 23.33 | 2.00 | 90.0 | 73.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.64 | 13.42 | 22.19 | 2.00 | 74.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.68 | 16.05 | 26.34 | 18.00 | 88.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.06 | 14.13 | 23.50 | 8.00 | 78.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.25 | 12.78 | 22.22 | 6.00 | 70.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.68 | 11.35 | 18.70 | 4.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.4 | 3.02 | 7.66 | 11.78 | 1.00 | 53.2 | 27.0 |

## GW16

- Train rows: 172367
- Bank: 0.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.28
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.95) beats the best remaining Bench Boost opportunity (8.04).
- Transfer: Daniel Muñoz Mejía -> Trevoh Chalobah (projected gain 3.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.95) beats the best remaining Bench Boost opportunity (8.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.26 | 13.92 | 21.67 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 4.81 | 13.56 | 21.61 | 9.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.76 | 12.80 | 20.37 | 2.00 | 77.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.22 | 12.19 | 19.61 | 6.00 | 82.9 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.73 | 9.88 | 15.63 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.05 | 3.17 | 5.36 | 1.00 | 26.9 | 76.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.22 | 22.79 | 37.80 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.49 | 17.20 | 27.56 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nick Woltemade | FWD | 15 | 7.5 | 3.60 | 10.71 | 17.49 | 0.00 | 59.1 | 74.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.21 | 19.89 | 32.77 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.61 | 15.24 | 24.66 | 2.00 | 79.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.03 | 11.50 | 18.87 | 3.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.76 | 11.16 | 19.63 | 2.00 | 60.2 | 90.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 2.30 | 6.58 | 10.69 | 2.00 | 44.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.45
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.58) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.29, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.58) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Lewis Miley replaced Maxime Estève.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 10.68 | 16.99 | 7.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Alex Cairns | GK | 11 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.24 | 12.03 | 19.65 | 2.00 | 86.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.04 | 11.41 | 18.53 | 6.00 | 72.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 3.59 | 10.98 | 17.77 | 3.00 | 80.5 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.99 | 8.69 | 14.06 | 0.00 | 81.0 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.49 | 4.07 | 7.13 | 0.00 | 46.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.58 | 24.63 | 39.54 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.38 | 10.85 | 17.48 | 2.00 | 46.0 | 90.0 |
| Bench 3 | Bench | Nick Woltemade | FWD | 15 | 7.3 | 2.31 | 8.33 | 14.74 | 13.00 | 43.5 | 72.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.33 | 18.67 | 28.19 | 3.00 | 76.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.93 | 18.44 | 30.67 | 1.00 | 90.0 | 45.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.78 | 14.15 | 22.71 | 11.00 | 72.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.61 | 11.16 | 18.02 | 4.00 | 74.4 | 90.0 |
| Bench 2 | Autosub In | Lewis Miley | MID | 15 | 4.4 | 2.46 | 7.41 | 11.64 | 4.00 | 56.6 | 90.0 |