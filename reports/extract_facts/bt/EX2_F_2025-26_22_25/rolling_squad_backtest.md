# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.28
- Total actual points: 237.00
- Average predicted points: 66.07
- Average actual points: 59.25
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
- Predicted score: 65.91
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 10.83 | 17.59 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.45 | 0.59 | 0.81 | 0.00 | 6.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.88 | 13.60 | 19.49 | 8.00 | 77.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.72 | 20.38 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.32 | 12.69 | 19.94 | 8.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.39 | 9.31 | 14.27 | 0.00 | 84.5 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.60 | 7.42 | 12.14 | 6.00 | 77.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.28 | 39.41 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.53 | 15.03 | 23.58 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.99 | 8.24 | 12.37 | 2.00 | 70.4 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.64 | 15.77 | 24.99 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.41 | 15.77 | 25.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.24 | 14.58 | 23.55 | 10.00 | 78.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.00 | 14.51 | 23.97 | 2.00 | 83.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.03 | 14.20 | 23.47 | 3.00 | 78.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.35
- Actual score: 42.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.84, hit 0)
- Autosub: Mateus Mané replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 10.84 | 17.64 | 1.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.10 | 0.44 | 0.00 | 6.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.53 | 13.22 | 19.86 | 1.00 | 77.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.83 | 13.22 | 21.48 | 4.00 | 87.8 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.19 | 11.66 | 17.84 | 11.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.55 | 7.44 | 12.14 | 0.00 | 76.2 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.86 | 5.65 | 9.26 | 0.00 | 44.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 22.83 | 37.59 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.66 | 15.48 | 24.60 | 2.00 | 86.8 | 90.0 |
| Bench 3 | Autosub In | Mateus Mané | FWD | 20 | 4.5 | 2.54 | 7.92 | 12.78 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 6.25 | 17.69 | 27.78 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.35 | 15.57 | 24.27 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.18 | 14.83 | 24.37 | 2.00 | 79.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.69 | 13.46 | 22.02 | 8.00 | 77.3 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.30 | 12.72 | 21.74 | 0.00 | 72.7 | 0.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Erling Haaland
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 64.62
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.12) beats the best remaining Bench Boost opportunity (6.27).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 6.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.12) beats the best remaining Bench Boost opportunity (6.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 10.98 | 17.65 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.18 | 0.36 | 0.48 | 0.00 | 7.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.20 | 22.36 | 8.00 | 86.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 12.03 | 19.64 | 2.00 | 83.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.83 | 11.27 | 17.85 | 0.00 | 88.5 | 45.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.18 | 4.39 | 8.04 | -1.00 | 38.3 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.77 | 2.98 | 6.40 | 0.00 | 21.2 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 5.68 | 19.07 | 32.17 | 5.00 | 75.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.44 | 13.66 | 22.02 | 2.00 | 81.1 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.01 | 8.10 | 13.34 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 5.90 | 16.70 | 26.66 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.20 | 25.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.52 | 15.43 | 24.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.39 | 14.44 | 23.24 | 8.00 | 88.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.40 | 13.25 | 22.26 | 12.00 | 72.2 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.40
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 6.34, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.19 | 11.49 | 18.22 | 7.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.16 | 0.17 | 0.00 | 4.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.53 | 15.18 | 23.89 | 6.00 | 89.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.34 | 12.18 | 19.00 | 4.00 | 85.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.13 | 11.86 | 19.38 | 2.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.17 | 5.87 | 9.81 | 2.00 | 62.3 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.22 | 0.86 | 3.34 | 0.00 | 5.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.78 | 20.65 | 34.76 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.98 | 12.76 | 20.93 | 5.00 | 74.6 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.97 | 8.65 | 14.08 | 2.00 | 70.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.86 | 16.56 | 26.39 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.59 | 16.42 | 27.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.05 | 15.24 | 25.22 | 2.00 | 86.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.78 | 13.85 | 22.22 | 10.00 | 82.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.62 | 13.84 | 22.04 | 2.00 | 76.9 | 90.0 |