# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 258.36
- Total actual points: 216.00
- Average predicted points: 64.59
- Average actual points: 54.00
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.66
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Omar Alderete replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.71 | 10.75 | 17.52 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.32 | 0.34 | 0.50 | 0.00 | 3.8 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.30 | 12.66 | 20.00 | 8.00 | 86.8 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.45 | 12.52 | 20.15 | 0.00 | 90.0 | 0.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 4.10 | 11.48 | 19.37 | 1.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.36 | 9.29 | 14.31 | 0.00 | 83.6 | 0.0 |
| Bench 4 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.33 | 9.24 | 15.01 | 1.00 | 81.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.14 | 23.85 | 38.86 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.35 | 14.58 | 23.06 | 2.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.04 | 12.52 | 19.73 | 2.00 | 75.8 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.70 | 15.94 | 25.36 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.39 | 15.74 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.28 | 14.71 | 23.89 | 10.00 | 77.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.03 | 14.59 | 24.20 | 2.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.07 | 14.33 | 23.81 | 3.00 | 77.5 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.70
- Actual score: 42.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 3.09, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.90 | 17.64 | 1.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.22 | 0.00 | 5.6 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.35 | 21.62 | 4.00 | 89.4 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.23 | 11.73 | 17.88 | 11.00 | 88.7 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 3.78 | 10.68 | 17.69 | 1.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.99 | 8.65 | 14.66 | 1.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.85 | 5.67 | 9.25 | 0.00 | 44.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.20 | 22.53 | 37.10 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.56 | 15.13 | 24.08 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.63 | 11.08 | 17.54 | 2.00 | 71.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.72 | 15.83 | 25.17 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.47 | 15.82 | 24.58 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.28 | 15.06 | 24.71 | 2.00 | 80.7 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.74 | 13.77 | 22.60 | 0.00 | 79.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.78 | 13.66 | 22.29 | 8.00 | 77.9 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.52
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.57) beats the best remaining Triple Captain opportunity (7.32).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.01, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.57) beats the best remaining Triple Captain opportunity (7.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.86 | 10.91 | 17.61 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.06 | 0.13 | 0.21 | 0.00 | 4.2 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.01 | 11.94 | 19.62 | 2.00 | 81.8 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.77 | 11.18 | 17.82 | 0.00 | 88.1 | 45.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.87 | 9.14 | 15.52 | 1.00 | 79.5 | 30.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.37 | 8.85 | 14.36 | 6.00 | 78.7 | 85.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.09 | 3.74 | 7.39 | 0.00 | 27.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.57 | 19.67 | 33.50 | 5.00 | 79.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.18 | 13.01 | 21.18 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.51 | 10.30 | 16.84 | 2.00 | 71.6 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.93 | 16.77 | 26.84 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.55 | 16.27 | 25.63 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.57 | 15.56 | 24.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.16 | 14.19 | 22.67 | 8.00 | 80.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.41 | 13.32 | 22.48 | 12.00 | 70.8 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.48
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 3.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.17 | 11.46 | 18.23 | 7.00 | 84.6 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.33 | 12.17 | 19.11 | 4.00 | 84.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.07 | 11.76 | 19.33 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.64 | 8.31 | 14.40 | 0.00 | 60.1 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.69 | 8.25 | 13.21 | 1.00 | 77.8 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.14 | 0.76 | 3.21 | 0.00 | 3.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.51 | 19.99 | 33.91 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.68 | 12.02 | 19.97 | 5.00 | 72.3 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 2.94 | 9.02 | 15.24 | 7.00 | 64.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.87 | 16.61 | 26.57 | 5.00 | 89.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.38 | 15.83 | 25.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.10 | 15.41 | 25.55 | 2.00 | 85.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.69 | 14.02 | 22.41 | 2.00 | 76.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.78 | 13.87 | 22.37 | 10.00 | 80.4 | 90.0 |