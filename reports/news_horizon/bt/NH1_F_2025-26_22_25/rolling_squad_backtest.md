# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 261.96
- Total actual points: 225.00
- Average predicted points: 65.49
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
- Predicted score: 65.40
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.71 | 10.68 | 17.35 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.34 | 0.43 | 0.69 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.91 | 13.74 | 19.87 | 8.00 | 77.8 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.61 | 20.29 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.30 | 12.61 | 19.88 | 8.00 | 87.2 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.13 | 10.93 | 17.42 | 0.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.35 | 9.28 | 14.31 | 0.00 | 83.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.30 | 24.24 | 39.41 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.51 | 14.99 | 23.67 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.00 | 12.41 | 19.57 | 2.00 | 76.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.64 | 15.83 | 25.23 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.37 | 15.70 | 25.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.96 | 14.44 | 24.00 | 2.00 | 83.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.99 | 14.20 | 23.66 | 3.00 | 77.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.90 | 13.92 | 22.50 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.65
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.64, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.83 | 10.80 | 17.44 | 1.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.08 | 0.41 | 0.00 | 5.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.57 | 13.30 | 19.96 | 1.00 | 78.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.87 | 13.30 | 21.56 | 4.00 | 89.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.27 | 11.77 | 17.90 | 11.00 | 88.4 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.67 | 10.18 | 16.73 | 7.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.86 | 5.61 | 9.08 | 0.00 | 44.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.36 | 22.91 | 37.63 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.73 | 15.56 | 24.72 | 2.00 | 88.8 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.58 | 10.91 | 17.24 | 2.00 | 72.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.66 | 15.71 | 25.00 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.42 | 15.69 | 24.41 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.69 | 13.61 | 22.32 | 0.00 | 79.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.70 | 13.43 | 21.90 | 8.00 | 78.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.18 | 11.94 | 19.90 | 10.00 | 74.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.46
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.75) beats the best remaining Triple Captain opportunity (7.35).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.02, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.75) beats the best remaining Triple Captain opportunity (7.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.83 | 17.45 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.07 | 0.21 | 0.40 | 0.00 | 4.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.95 | 14.21 | 22.51 | 8.00 | 86.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.99 | 11.89 | 19.53 | 2.00 | 81.7 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.79 | 11.21 | 17.84 | 0.00 | 87.8 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.21 | 9.64 | 16.17 | 0.00 | 85.2 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.08 | 3.66 | 7.22 | 0.00 | 27.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.75 | 20.02 | 33.91 | 5.00 | 79.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.44 | 21.74 | 2.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.47 | 10.15 | 16.59 | 2.00 | 72.2 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.86 | 16.65 | 26.73 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.20 | 25.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.51 | 15.37 | 24.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.09 | 14.08 | 22.58 | 8.00 | 80.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.29 | 12.81 | 20.99 | 2.00 | 85.9 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.45
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 4.95, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.15 | 11.35 | 18.02 | 7.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.02 | 0.10 | 0.00 | 1.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.48 | 15.12 | 23.95 | 6.00 | 88.3 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.32 | 12.09 | 18.92 | 4.00 | 85.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.73 | 19.27 | 2.00 | 82.0 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.41 | 5.63 | 10.47 | 1.00 | 40.0 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.18 | 1.32 | 4.44 | 0.00 | 4.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.70 | 20.35 | 34.32 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.87 | 12.40 | 20.42 | 5.00 | 72.3 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.04 | 9.19 | 15.43 | 7.00 | 64.2 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.82 | 16.53 | 26.50 | 5.00 | 89.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.32 | 15.73 | 25.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.61 | 13.85 | 22.19 | 2.00 | 76.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.73 | 13.69 | 22.03 | 10.00 | 81.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.07 | 11.86 | 18.94 | 2.00 | 79.7 | 90.0 |