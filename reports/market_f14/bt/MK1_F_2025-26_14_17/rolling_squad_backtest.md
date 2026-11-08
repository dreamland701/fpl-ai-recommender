# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 268.81
- Total actual points: 283.00
- Average predicted points: 67.20
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
- Predicted score: 65.99
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.34 | 11.95 | 18.82 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.96 | 13.81 | 21.47 | 1.00 | 86.3 | 46.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.74 | 13.00 | 20.75 | 4.00 | 87.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.66 | 12.72 | 19.83 | 14.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.99 | 8.25 | 12.84 | 4.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.49 | 6.77 | 11.16 | 0.00 | 74.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.94 | 23.40 | 37.98 | 14.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.47 | 14.77 | 23.39 | 2.00 | 89.3 | 63.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.65 | 12.89 | 21.50 | 1.00 | 68.0 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.14 | 17.64 | 27.86 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.70 | 16.28 | 25.92 | 2.00 | 84.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.68 | 16.08 | 25.87 | 3.00 | 86.5 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.77 | 12.45 | 20.16 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.38 | 6.59 | 10.32 | 2.00 | 49.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nick Woltemade
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.87
- Actual score: 54.00
- Transfer: Jean-Philippe Mateta -> Nick Woltemade (projected gain 3.97, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.35 | 18.22 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.80 | 14.01 | 22.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.16 | 11.71 | 19.35 | 2.00 | 86.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.75 | 11.30 | 18.45 | 3.00 | 68.4 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 3.18 | 8.78 | 14.38 | 3.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.33 | 4.29 | 7.19 | 0.00 | 40.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.55 | 24.80 | 39.64 | 2.00 | 90.0 | 68.0 |
| Vice Captain | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.79 | 15.21 | 23.30 | 2.00 | 90.0 | 73.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.61 | 13.42 | 22.20 | 2.00 | 74.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.69 | 16.05 | 26.34 | 18.00 | 88.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.10 | 14.13 | 23.49 | 8.00 | 78.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.18 | 12.78 | 22.24 | 6.00 | 70.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.72 | 11.35 | 18.69 | 4.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.4 | 3.11 | 7.66 | 11.76 | 1.00 | 53.3 | 27.0 |

## GW16

- Train rows: 172367
- Bank: 0.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.50
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (7.93).
- Transfer: Daniel Muñoz Mejía -> Trevoh Chalobah (projected gain 3.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (7.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.35 | 13.91 | 21.64 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 4.77 | 13.56 | 21.61 | 9.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.84 | 12.80 | 20.35 | 2.00 | 77.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.20 | 12.19 | 19.62 | 6.00 | 82.8 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.70 | 9.88 | 15.64 | 1.00 | 85.1 | 90.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.02 | 3.17 | 5.37 | 1.00 | 26.9 | 76.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.29 | 22.79 | 37.79 | 13.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.51 | 17.20 | 27.55 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nick Woltemade | FWD | 15 | 7.5 | 3.58 | 10.71 | 17.50 | 0.00 | 59.1 | 74.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.18 | 19.89 | 32.78 | 13.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.70 | 15.23 | 24.64 | 2.00 | 80.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.02 | 11.50 | 18.88 | 3.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.77 | 11.16 | 19.63 | 2.00 | 60.2 | 90.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 2.27 | 6.58 | 10.70 | 2.00 | 44.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.44
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.29, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Lewis Miley replaced Maxime Estève.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.77 | 10.68 | 17.00 | 7.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.20 | 12.03 | 19.66 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.00 | 11.41 | 18.54 | 6.00 | 72.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 3.59 | 10.97 | 17.77 | 3.00 | 80.5 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.93 | 8.69 | 14.08 | 0.00 | 80.9 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.41 | 4.07 | 7.15 | 0.00 | 46.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 8.64 | 24.63 | 39.52 | 16.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.39 | 10.85 | 17.47 | 2.00 | 46.1 | 90.0 |
| Bench 3 | Bench | Nick Woltemade | FWD | 15 | 7.3 | 2.37 | 8.33 | 14.72 | 13.00 | 43.6 | 72.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.32 | 18.67 | 28.19 | 3.00 | 76.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.92 | 18.44 | 30.68 | 1.00 | 90.0 | 45.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.76 | 14.15 | 22.71 | 11.00 | 72.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.63 | 11.16 | 18.01 | 4.00 | 74.4 | 90.0 |
| Bench 2 | Autosub In | Lewis Miley | MID | 15 | 4.4 | 2.50 | 7.41 | 11.63 | 4.00 | 56.7 | 90.0 |