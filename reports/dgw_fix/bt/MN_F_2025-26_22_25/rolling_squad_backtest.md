# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 265.54
- Total actual points: 225.00
- Average predicted points: 66.39
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
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.97
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 11.10 | 18.06 | 6.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.31 | 0.24 | 0.32 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.21 | 13.88 | 20.00 | 8.00 | 83.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.85 | 20.66 | 0.00 | 95.4 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.19 | 12.56 | 19.85 | 8.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.16 | 11.00 | 17.46 | 0.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.35 | 9.31 | 14.36 | 0.00 | 83.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.32 | 24.48 | 39.81 | 2.00 | 117.4 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.87 | 15.34 | 24.21 | 2.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.11 | 12.54 | 19.75 | 2.00 | 77.3 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.85 | 15.79 | 25.15 | 3.00 | 100.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.41 | 15.77 | 25.40 | 2.00 | 98.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.12 | 14.61 | 24.21 | 2.00 | 86.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.16 | 14.21 | 23.60 | 3.00 | 80.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.17 | 14.11 | 22.72 | 2.00 | 96.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.51
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.58, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.96 | 11.19 | 18.08 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.66 | 13.37 | 20.03 | 1.00 | 80.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.94 | 13.36 | 21.62 | 4.00 | 90.4 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.24 | 11.81 | 17.98 | 11.00 | 87.6 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.64 | 10.28 | 16.91 | 7.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.73 | 5.39 | 8.81 | 0.00 | 42.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.47 | 23.22 | 38.14 | 1.00 | 113.7 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.99 | 15.84 | 25.15 | 2.00 | 93.4 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.64 | 11.05 | 17.50 | 2.00 | 73.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.75 | 15.71 | 25.01 | 8.00 | 94.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.44 | 15.59 | 24.26 | 1.00 | 93.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.71 | 13.47 | 21.99 | 8.00 | 78.7 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.52 | 13.37 | 21.97 | 0.00 | 75.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.37 | 12.10 | 20.08 | 10.00 | 77.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.95
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.29).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.99 | 11.21 | 18.07 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.08 | 14.31 | 22.61 | 8.00 | 89.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 12.04 | 19.74 | 2.00 | 83.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.76 | 11.26 | 17.91 | 0.00 | 86.7 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.08 | 9.68 | 16.24 | 0.00 | 83.0 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.98 | 3.45 | 6.90 | 0.00 | 25.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.67 | 20.32 | 34.46 | 5.00 | 81.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.27 | 13.45 | 21.85 | 2.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.49 | 10.22 | 16.71 | 2.00 | 72.4 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.94 | 16.76 | 26.85 | 7.00 | 101.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.15 | 25.46 | 3.00 | 94.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.53 | 15.41 | 24.60 | 2.00 | 93.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.49 | 14.33 | 22.88 | 8.00 | 87.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.31 | 12.88 | 21.07 | 2.00 | 86.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.11
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 4.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.29 | 11.69 | 18.58 | 7.00 | 88.4 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.57 | 15.20 | 24.03 | 6.00 | 90.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.44 | 12.33 | 19.34 | 4.00 | 87.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.79 | 19.37 | 2.00 | 82.6 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.66 | 6.03 | 10.78 | 1.00 | 45.8 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.54 | 1.73 | 4.65 | 0.00 | 12.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.55 | 20.55 | 34.74 | 11.00 | 92.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.56 | 12.14 | 20.15 | 5.00 | 65.5 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.06 | 9.24 | 15.56 | 7.00 | 63.7 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.83 | 16.32 | 26.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.40 | 15.89 | 25.92 | 2.00 | 95.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.85 | 13.95 | 22.31 | 2.00 | 80.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.66 | 13.74 | 22.18 | 10.00 | 80.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.10 | 11.95 | 19.11 | 2.00 | 80.3 | 90.0 |