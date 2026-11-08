# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.61
- Total actual points: 225.00
- Average predicted points: 65.65
- Average actual points: 56.25
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
- Predicted score: 65.25
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Yerson Mosquera Valdelamar replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.68 | 10.76 | 21.13 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.34 | 0.39 | 0.54 | 0.00 | 3.9 | 0.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.74 | 20.61 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.66 | 20.04 | 8.00 | 86.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.44 | 12.53 | 23.69 | 5.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.35 | 9.38 | 14.30 | 0.00 | 83.6 | 0.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.42 | 9.28 | 16.77 | 8.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.79 | 40.49 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.53 | 14.33 | 22.81 | 2.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.92 | 8.10 | 14.68 | 2.00 | 68.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.37 | 15.82 | 25.63 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.66 | 15.65 | 24.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.21 | 14.51 | 23.61 | 10.00 | 77.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 14.20 | 23.73 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.01 | 13.96 | 28.04 | 3.00 | 77.8 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.39
- Actual score: 40.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 4.58, hit 0)
- Autosub: Yerson Mosquera Valdelamar replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 10.88 | 21.31 | 1.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.02 | 0.26 | 0.00 | 5.7 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.88 | 13.24 | 21.51 | 4.00 | 89.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.27 | 12.23 | 23.21 | 1.00 | 85.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.26 | 11.91 | 18.10 | 11.00 | 88.3 | 90.0 |
| Bench 2 | Autosub In | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.05 | 9.22 | 17.97 | 0.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.84 | 5.85 | 9.50 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 23.47 | 38.73 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.74 | 15.11 | 24.13 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.93 | 15.10 | 2.00 | 69.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.43 | 15.67 | 29.27 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.67 | 15.43 | 24.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.21 | 14.84 | 24.35 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.70 | 13.79 | 22.44 | 0.00 | 79.3 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.70 | 13.33 | 21.86 | 8.00 | 78.3 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.54
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.33).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 6.96, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 14.53 | 21.37 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.18 | 0.32 | 0.00 | 4.3 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.01 | 15.51 | 22.88 | 5.00 | 79.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.87 | 19.64 | 2.00 | 81.9 | 90.0 |
| Bench 2 | Bench | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 3.17 | 11.54 | 16.63 | 0.00 | 71.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.79 | 11.31 | 17.85 | 0.00 | 87.8 | 45.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.07 | 3.85 | 7.59 | 0.00 | 27.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.73 | 20.54 | 35.20 | 5.00 | 79.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.69 | 22.07 | 2.00 | 79.6 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.96 | 10.59 | 15.57 | 2.00 | 67.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 21.57 | 30.71 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.88 | 16.58 | 26.90 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 15.35 | 24.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.12 | 13.60 | 21.92 | 8.00 | 81.2 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.33 | 13.11 | 22.10 | 12.00 | 71.1 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.42
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.78) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 6.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.78) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 15.09 | 21.91 | 7.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.44 | 15.88 | 23.26 | 6.00 | 78.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.31 | 12.03 | 18.97 | 4.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.73 | 19.42 | 2.00 | 82.0 | 90.0 |
| Bench 3 | Bench Boost | Yerson Mosquera Valdelamar | DEF | 20 | 4.3 | 2.74 | 10.05 | 14.83 | 1.00 | 67.3 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.11 | 0.68 | 3.15 | 0.00 | 3.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.66 | 20.79 | 35.38 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.83 | 12.62 | 20.77 | 5.00 | 71.5 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.92 | 11.21 | 16.37 | 2.00 | 69.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.84 | 21.75 | 31.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.34 | 15.69 | 25.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.01 | 15.12 | 25.06 | 2.00 | 85.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.71 | 13.76 | 22.23 | 10.00 | 80.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.63 | 13.38 | 21.59 | 2.00 | 77.0 | 90.0 |