# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 266.11
- Total actual points: 226.00
- Average predicted points: 66.53
- Average actual points: 56.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW21 are included before the first simulated week.
- League-average scores were not available for this run.

## GW22

- Train rows: 177037
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.85
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nordi Mukiele replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.19 | 21.87 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 3.1 | 0.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.57 | 12.97 | 20.95 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.48 | 12.64 | 23.89 | 5.00 | 85.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.25 | 12.59 | 19.92 | 8.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | Nordi Mukiele | DEF | 17 | 4.4 | 3.77 | 10.09 | 16.48 | 6.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.37 | 9.42 | 14.38 | 0.00 | 83.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.37 | 24.99 | 40.81 | 2.00 | 90.0 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.66 | 14.65 | 23.28 | 2.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.90 | 8.08 | 14.65 | 2.00 | 68.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.40 | 15.89 | 25.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.63 | 15.61 | 24.85 | 3.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.19 | 14.43 | 23.49 | 10.00 | 77.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.05 | 14.36 | 23.96 | 2.00 | 84.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.03 | 13.98 | 28.04 | 3.00 | 78.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.63
- Actual score: 34.00
- Transfer: Marc Guéhi -> Pedro Porro Sauceda (projected gain 0.96, hit 0)
- Autosub: Nordi Mukiele replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.96 | 11.24 | 21.95 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.36 | 0.29 | 0.38 | 0.00 | 3.8 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.28 | 21.55 | 4.00 | 89.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.33 | 12.38 | 23.49 | 1.00 | 86.2 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 4.18 | 11.51 | 18.52 | 1.00 | 87.1 | 45.0 |
| Bench 2 | Autosub In | Nordi Mukiele | DEF | 17 | 4.4 | 4.16 | 11.20 | 17.91 | 4.00 | 85.9 | 82.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.73 | 5.57 | 9.06 | 0.00 | 42.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.46 | 23.75 | 39.17 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.83 | 15.36 | 24.50 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.93 | 15.11 | 2.00 | 69.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.37 | 15.53 | 29.06 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.67 | 15.42 | 24.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.18 | 14.75 | 24.19 | 2.00 | 80.1 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.58 | 13.49 | 21.96 | 0.00 | 76.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.71 | 13.34 | 21.88 | 8.00 | 78.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.62
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 9.56, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 15.01 | 22.01 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.07 | 15.73 | 23.14 | 5.00 | 81.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 11.99 | 19.80 | 2.00 | 82.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.28 | 11.32 | 18.13 | 9.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.2 | 2.90 | 9.19 | 15.72 | 0.00 | 63.4 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.98 | 3.59 | 7.15 | 0.00 | 25.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.81 | 20.77 | 35.54 | 5.00 | 80.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.35 | 13.65 | 22.02 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.97 | 10.61 | 15.57 | 2.00 | 67.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.49 | 21.48 | 30.63 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.92 | 16.67 | 27.06 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.51 | 15.39 | 24.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.23 | 13.87 | 22.33 | 8.00 | 83.3 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.31 | 13.03 | 21.95 | 12.00 | 70.5 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.01
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Pedro Porro Sauceda -> Trevoh Chalobah (projected gain 2.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.26 | 15.51 | 22.46 | 7.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.49 | 16.03 | 23.43 | 6.00 | 79.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.40 | 12.26 | 19.31 | 4.00 | 86.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.08 | 11.76 | 19.47 | 2.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 3.60 | 10.87 | 18.07 | 1.00 | 81.1 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.55 | 1.81 | 4.85 | 0.00 | 12.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.73 | 20.96 | 35.64 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.72 | 12.32 | 20.31 | 5.00 | 69.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.94 | 11.26 | 16.42 | 2.00 | 69.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.75 | 21.45 | 30.96 | 5.00 | 88.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.39 | 15.84 | 26.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.98 | 15.01 | 24.88 | 2.00 | 84.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.73 | 13.80 | 22.29 | 10.00 | 81.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.67 | 13.48 | 21.74 | 2.00 | 77.9 | 90.0 |