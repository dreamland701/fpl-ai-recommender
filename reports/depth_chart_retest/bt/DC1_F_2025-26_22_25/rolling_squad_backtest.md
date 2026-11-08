# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.75
- Total actual points: 214.00
- Average predicted points: 65.69
- Average actual points: 53.50
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
- Predicted score: 64.69
- Actual score: 39.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nordi Mukiele replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.02 | 11.65 | 18.98 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.12 | 0.00 | 3.1 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.30 | 12.67 | 20.00 | 8.00 | 86.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.30 | 12.15 | 19.59 | 0.00 | 90.0 | 0.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 3.99 | 11.20 | 18.96 | 1.00 | 82.6 | 90.0 |
| Bench 3 | Autosub In | Nordi Mukiele | DEF | 17 | 4.4 | 3.66 | 9.99 | 16.48 | 6.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.30 | 9.13 | 14.04 | 0.00 | 82.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.42 | 24.61 | 40.02 | 2.00 | 90.0 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.82 | 15.86 | 25.05 | 2.00 | 87.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.01 | 14.86 | 23.19 | 2.00 | 76.8 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.55 | 15.57 | 24.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.10 | 15.00 | 24.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.95 | 14.06 | 23.41 | 3.00 | 77.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.81 | 14.04 | 23.38 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.2 | 4.62 | 13.74 | 21.90 | 4.00 | 90.0 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.83
- Actual score: 51.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.70, hit 0)
- Autosub: Ollie Watkins replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.17 | 11.84 | 19.17 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.44 | 0.47 | 0.73 | 0.00 | 4.5 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.38 | 21.69 | 4.00 | 89.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.31 | 11.94 | 18.19 | 11.00 | 88.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.08 | 11.30 | 18.08 | 4.00 | 84.1 | 82.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 3.63 | 10.29 | 17.11 | 1.00 | 81.7 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.82 | 5.56 | 9.05 | 0.00 | 43.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.53 | 23.42 | 38.47 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.04 | 16.46 | 26.14 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Ollie Watkins | FWD | 2 | 8.8 | 4.50 | 13.95 | 22.61 | 8.00 | 74.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.35 | 15.53 | 24.14 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.41 | 15.09 | 24.04 | 8.00 | 89.4 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 5.28 | 14.75 | 23.20 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.65 | 13.53 | 22.22 | 0.00 | 78.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.58 | 13.20 | 21.61 | 8.00 | 77.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.91
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.96) beats the best remaining Triple Captain opportunity (7.59).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 1.21, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.96) beats the best remaining Triple Captain opportunity (7.59).
- Autosub: James Garner replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.18 | 11.83 | 19.12 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.11 | 0.21 | 0.00 | 3.2 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.95 | 19.65 | 2.00 | 81.6 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.81 | 11.29 | 18.00 | 0.00 | 87.7 | 45.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.17 | 11.20 | 17.96 | 9.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.70 | 8.71 | 14.88 | 1.00 | 78.0 | 30.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.07 | 3.67 | 7.25 | 0.00 | 27.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.96 | 20.73 | 35.13 | 5.00 | 82.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.65 | 14.27 | 23.12 | 2.00 | 82.9 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.8 | 4.67 | 14.05 | 23.56 | 0.00 | 76.5 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.49 | 16.15 | 25.45 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.63 | 16.01 | 25.69 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.37 | 15.11 | 24.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.08 | 14.00 | 22.38 | 8.00 | 80.0 | 90.0 |
| Bench 2 | Autosub In | James Garner | MID | 9 | 5.2 | 4.31 | 13.01 | 21.10 | 4.00 | 85.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.31
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.36) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 4.11, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.36) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.51 | 12.43 | 19.82 | 7.00 | 89.5 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.1 | 0.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.34 | 12.10 | 18.95 | 4.00 | 87.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.09 | 11.76 | 19.31 | 2.00 | 82.9 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 3.68 | 11.33 | 18.63 | 1.00 | 82.9 | 90.0 |
| Bench 2 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.54 | 8.03 | 13.96 | 0.00 | 59.9 | 0.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.11 | 0.68 | 3.06 | 0.00 | 2.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.93 | 21.17 | 35.74 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.12 | 13.23 | 21.85 | 5.00 | 74.9 | 90.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.7 | 1.71 | 6.66 | 12.88 | 2.00 | 19.8 | 85.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 6.02 | 16.87 | 26.89 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.28 | 15.31 | 24.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.81 | 13.89 | 22.37 | 10.00 | 84.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.67 | 13.81 | 22.00 | 2.00 | 79.2 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.55 | 12.94 | 20.58 | 4.00 | 89.1 | 90.0 |