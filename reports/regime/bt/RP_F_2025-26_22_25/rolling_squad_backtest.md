# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.89
- Total actual points: 232.00
- Average predicted points: 66.22
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
- Predicted score: 65.75
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.71 | 10.76 | 17.53 | 6.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.45 | 0.72 | 1.12 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.98 | 13.87 | 20.03 | 8.00 | 80.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.32 | 12.74 | 20.16 | 8.00 | 87.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.44 | 12.48 | 20.09 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.36 | 9.30 | 14.33 | 0.00 | 84.1 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.57 | 7.39 | 12.18 | 6.00 | 76.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.32 | 24.37 | 39.70 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.48 | 14.87 | 23.43 | 2.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.85 | 7.87 | 11.83 | 2.00 | 67.3 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.64 | 15.76 | 25.08 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.30 | 15.47 | 24.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.29 | 14.80 | 24.08 | 10.00 | 77.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.97 | 14.41 | 23.93 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.98 | 14.08 | 23.40 | 3.00 | 77.0 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.81
- Actual score: 42.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 4.31, hit 0)
- Autosub: Mateus Mané replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.92 | 17.67 | 1.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.39 | 0.85 | 0.00 | 3.3 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.92 | 13.43 | 21.77 | 4.00 | 89.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.62 | 13.42 | 20.14 | 1.00 | 81.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.29 | 11.89 | 18.12 | 11.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.59 | 7.51 | 12.18 | 0.00 | 77.7 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.87 | 5.73 | 9.36 | 0.00 | 45.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.39 | 23.07 | 37.96 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.68 | 15.41 | 24.44 | 2.00 | 88.2 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.5 | 2.47 | 7.68 | 12.26 | 2.00 | 68.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.61 | 15.54 | 24.71 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.37 | 15.51 | 24.06 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.30 | 15.18 | 24.97 | 2.00 | 81.1 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.70 | 13.64 | 22.39 | 0.00 | 78.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.69 | 13.44 | 21.96 | 8.00 | 78.2 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.55
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.36).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 6.46, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.87 | 10.95 | 17.68 | 6.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.18 | 0.51 | 0.85 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.97 | 14.21 | 22.50 | 8.00 | 88.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 12.06 | 19.82 | 2.00 | 82.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.82 | 11.31 | 18.00 | 0.00 | 88.2 | 45.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.24 | 4.06 | 7.26 | -1.00 | 41.3 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.09 | 3.72 | 7.37 | 0.00 | 28.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.76 | 20.19 | 34.32 | 5.00 | 80.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.31 | 13.28 | 21.51 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.90 | 7.78 | 12.84 | 2.00 | 66.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.79 | 16.37 | 26.19 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.45 | 15.97 | 25.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.47 | 15.30 | 24.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.15 | 14.17 | 22.67 | 8.00 | 80.7 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.41 | 13.38 | 22.64 | 12.00 | 71.3 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.78
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 6.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.17 | 11.46 | 18.25 | 7.00 | 82.5 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.30 | 0.52 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.48 | 15.10 | 23.88 | 6.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.30 | 12.09 | 18.97 | 4.00 | 85.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.09 | 11.84 | 19.48 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.19 | 5.91 | 9.83 | 2.00 | 63.7 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.14 | 0.79 | 3.28 | 0.00 | 4.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.69 | 20.47 | 34.66 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.76 | 12.17 | 20.13 | 5.00 | 70.9 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.87 | 8.33 | 13.57 | 2.00 | 67.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.78 | 16.31 | 26.06 | 5.00 | 89.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.22 | 15.38 | 25.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.04 | 15.29 | 25.40 | 2.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.64 | 13.92 | 22.27 | 2.00 | 76.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.71 | 13.72 | 22.14 | 10.00 | 80.3 | 90.0 |