# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 274.03
- Total actual points: 283.00
- Average predicted points: 68.51
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
- Predicted score: 66.78
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.52 | 11.95 | 18.82 | 6.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.23 | 13.81 | 21.47 | 1.00 | 91.0 | 46.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.19 | 13.00 | 20.75 | 4.00 | 99.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.62 | 12.72 | 19.83 | 14.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.91 | 8.25 | 12.84 | 4.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 2.56 | 6.77 | 11.16 | 0.00 | 75.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 7.90 | 23.40 | 37.98 | 14.00 | 105.6 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 5.35 | 14.77 | 23.39 | 2.00 | 86.6 | 63.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 2.95 | 12.89 | 21.50 | 1.00 | 59.3 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.61 | 17.64 | 27.86 | 4.00 | 105.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 6.11 | 16.28 | 25.92 | 2.00 | 92.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.96 | 16.08 | 25.87 | 3.00 | 91.5 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.45 | 12.45 | 20.16 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.4 | 2.27 | 6.59 | 10.32 | 2.00 | 45.7 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Nick Woltemade
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.40
- Actual score: 54.00
- Transfer: Jean-Philippe Mateta -> Nick Woltemade (projected gain 3.97, hit 0)
- Autosub: Maxime Estève replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.91 | 11.35 | 18.22 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.51 | 14.01 | 22.50 | 0.00 | 89.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.17 | 11.71 | 19.35 | 2.00 | 87.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 3.75 | 11.30 | 18.45 | 3.00 | 67.6 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 3.9 | 2.87 | 8.78 | 14.38 | 3.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.42 | 4.29 | 7.19 | 0.00 | 41.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 9.13 | 24.80 | 39.64 | 2.00 | 115.6 | 68.0 |
| Vice Captain | XI | Nick Woltemade | FWD | 15 | 7.5 | 6.24 | 15.21 | 23.30 | 2.00 | 100.9 | 73.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.12 | 13.42 | 22.20 | 2.00 | 66.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.80 | 16.05 | 26.34 | 18.00 | 91.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.14 | 14.13 | 23.49 | 8.00 | 80.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.06 | 12.78 | 22.24 | 6.00 | 68.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.43 | 11.35 | 18.69 | 4.00 | 69.7 | 90.0 |
| Bench 2 | Bench | Lewis Miley | MID | 15 | 4.4 | 3.30 | 7.66 | 11.76 | 1.00 | 56.8 | 27.0 |

## GW16

- Train rows: 172367
- Bank: 0.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 73.20
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.94) beats the best remaining Bench Boost opportunity (8.02).
- Transfer: Daniel Muñoz Mejía -> Trevoh Chalobah (projected gain 3.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.94) beats the best remaining Bench Boost opportunity (8.02).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.93 | 13.91 | 21.64 | 2.00 | 112.6 | 90.0 |
| Bench 1 | Bench Boost | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 5.14 | 13.56 | 21.61 | 9.00 | 111.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.40 | 12.80 | 20.35 | 2.00 | 91.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.36 | 12.19 | 19.62 | 6.00 | 89.1 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.56 | 9.88 | 15.64 | 1.00 | 81.4 | 90.0 |
| Bench 4 | Bench Boost | Axel Tuanzebe | DEF | 3 | 3.9 | 1.23 | 3.17 | 5.37 | 1.00 | 32.3 | 76.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 7.17 | 22.79 | 37.79 | 13.00 | 95.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 6.21 | 17.20 | 27.55 | 2.00 | 97.9 | 90.0 |
| Bench 2 | Bench Boost | Nick Woltemade | FWD | 15 | 7.5 | 3.43 | 10.71 | 17.50 | 0.00 | 56.7 | 74.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.28 | 19.89 | 32.78 | 13.00 | 114.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 6.41 | 15.23 | 24.64 | 2.00 | 95.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.75 | 11.50 | 18.88 | 3.00 | 71.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.76 | 11.16 | 19.63 | 2.00 | 61.6 | 90.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.4 | 2.28 | 6.58 | 10.70 | 2.00 | 43.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.65
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 11.32, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Lewis Miley replaced Maxime Estève.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.86 | 10.68 | 17.00 | 7.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Mark Gillespie | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.21 | 12.03 | 19.66 | 2.00 | 86.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.25 | 11.41 | 18.54 | 6.00 | 77.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.4 | 3.66 | 10.97 | 17.77 | 3.00 | 81.0 | 90.0 |
| XI | Bench | Maxime Estève | DEF | 3 | 3.9 | 2.70 | 8.69 | 14.08 | 0.00 | 74.9 | 0.0 |
| Bench 4 | Bench | Axel Tuanzebe | DEF | 3 | 3.9 | 1.57 | 4.07 | 7.15 | 0.00 | 51.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 9.29 | 24.63 | 39.52 | 16.00 | 118.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.15 | 10.85 | 17.47 | 2.00 | 41.6 | 90.0 |
| Bench 3 | Bench | Nick Woltemade | FWD | 15 | 7.3 | 2.25 | 8.33 | 14.72 | 13.00 | 42.2 | 72.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 7.17 | 18.67 | 28.19 | 3.00 | 85.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 5.36 | 18.44 | 30.68 | 1.00 | 82.0 | 45.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.97 | 14.15 | 22.71 | 11.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.45 | 11.16 | 18.01 | 4.00 | 70.0 | 90.0 |
| Bench 2 | Autosub In | Lewis Miley | MID | 15 | 4.4 | 2.48 | 7.41 | 11.63 | 4.00 | 56.2 | 90.0 |