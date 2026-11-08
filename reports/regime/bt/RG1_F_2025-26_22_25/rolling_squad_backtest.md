# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.14
- Total actual points: 232.00
- Average predicted points: 66.04
- Average actual points: 58.00
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
- Predicted score: 65.58
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.69 | 10.65 | 17.26 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.43 | 0.61 | 0.85 | 0.00 | 3.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.05 | 14.13 | 20.46 | 8.00 | 80.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.32 | 12.76 | 20.18 | 8.00 | 87.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.68 | 20.42 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.42 | 9.50 | 14.66 | 0.00 | 84.5 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.66 | 7.72 | 12.71 | 6.00 | 77.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 24.24 | 39.49 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.45 | 14.77 | 23.27 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.81 | 7.73 | 11.59 | 2.00 | 67.8 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.61 | 15.67 | 24.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.27 | 15.36 | 24.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.27 | 14.69 | 23.89 | 10.00 | 77.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.93 | 14.30 | 23.74 | 2.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.92 | 13.85 | 23.01 | 3.00 | 76.9 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.64
- Actual score: 42.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 4.16, hit 0)
- Autosub: Mateus Mané replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.82 | 17.43 | 1.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.29 | 0.61 | 0.00 | 5.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.70 | 13.68 | 20.58 | 1.00 | 81.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.93 | 13.44 | 21.80 | 4.00 | 89.8 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.33 | 12.02 | 18.34 | 11.00 | 88.8 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.69 | 7.84 | 12.74 | 0.00 | 78.1 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.93 | 5.92 | 9.70 | 0.00 | 45.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.34 | 22.94 | 37.74 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.65 | 15.33 | 24.29 | 2.00 | 88.7 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.5 | 2.42 | 7.54 | 12.01 | 2.00 | 69.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.58 | 15.44 | 24.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.32 | 15.34 | 23.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.27 | 15.06 | 24.76 | 2.00 | 80.9 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.67 | 13.54 | 22.21 | 0.00 | 79.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.66 | 13.32 | 21.75 | 8.00 | 77.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.25
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.31).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 6.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.86 | 10.86 | 17.44 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.17 | 0.43 | 0.62 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.05 | 14.47 | 22.94 | 8.00 | 88.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 12.07 | 19.84 | 2.00 | 82.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.84 | 11.37 | 18.10 | 0.00 | 88.3 | 45.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.34 | 4.39 | 7.82 | -1.00 | 41.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.14 | 3.91 | 7.71 | 0.00 | 28.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.71 | 20.06 | 34.11 | 5.00 | 80.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.28 | 13.21 | 21.38 | 2.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.85 | 7.65 | 12.61 | 2.00 | 66.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.76 | 16.25 | 25.99 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.40 | 15.81 | 24.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.41 | 15.10 | 24.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.10 | 14.00 | 22.36 | 8.00 | 80.5 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.38 | 13.25 | 22.42 | 12.00 | 71.1 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.68
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.16 | 11.38 | 18.04 | 7.00 | 84.6 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.22 | 0.30 | 0.00 | 1.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.54 | 15.30 | 24.21 | 6.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.30 | 12.09 | 18.97 | 4.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.11 | 11.91 | 19.60 | 2.00 | 82.6 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.27 | 6.22 | 10.35 | 2.00 | 63.9 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.21 | 1.04 | 3.70 | 0.00 | 4.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.65 | 20.35 | 34.48 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.75 | 12.11 | 20.02 | 5.00 | 71.7 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.84 | 8.21 | 13.39 | 2.00 | 68.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.74 | 16.16 | 25.78 | 5.00 | 89.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.19 | 15.27 | 24.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.01 | 15.17 | 25.19 | 2.00 | 85.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.60 | 13.74 | 21.96 | 2.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.66 | 13.53 | 21.82 | 10.00 | 79.9 | 90.0 |