# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.91
- Total actual points: 225.00
- Average predicted points: 65.73
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
- Predicted score: 65.80
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 10.81 | 17.57 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.46 | 0.61 | 0.84 | 0.00 | 7.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.94 | 13.72 | 19.72 | 8.00 | 78.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.53 | 12.70 | 20.38 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.32 | 12.68 | 19.97 | 8.00 | 87.8 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.18 | 10.99 | 17.41 | 0.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.39 | 9.33 | 14.32 | 0.00 | 84.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.31 | 24.29 | 39.49 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.56 | 15.08 | 23.75 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.04 | 12.48 | 19.63 | 2.00 | 77.1 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.68 | 15.85 | 25.17 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.42 | 15.77 | 25.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.01 | 14.49 | 24.01 | 2.00 | 84.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.06 | 14.25 | 23.64 | 3.00 | 79.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.93 | 13.93 | 22.41 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.03
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.58, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 10.79 | 17.58 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.10 | 0.44 | 0.00 | 6.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.53 | 13.20 | 19.89 | 1.00 | 77.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.83 | 13.20 | 21.49 | 4.00 | 87.8 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.19 | 11.65 | 17.86 | 11.00 | 86.4 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.63 | 10.12 | 16.74 | 7.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.85 | 5.63 | 9.25 | 0.00 | 44.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 22.80 | 37.62 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.68 | 15.47 | 24.69 | 2.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.51 | 10.83 | 17.27 | 2.00 | 70.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.63 | 15.65 | 24.98 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.35 | 15.57 | 24.33 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.65 | 13.54 | 22.33 | 0.00 | 77.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.66 | 13.37 | 21.94 | 8.00 | 77.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.15 | 11.86 | 19.81 | 10.00 | 73.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.08
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 10.96 | 17.65 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.18 | 0.37 | 0.50 | 0.00 | 7.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.01 | 14.25 | 22.48 | 8.00 | 87.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 12.00 | 19.62 | 2.00 | 83.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.82 | 11.26 | 17.87 | 0.00 | 88.5 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.08 | 9.83 | 16.86 | 0.00 | 44.7 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.70 | 2.83 | 6.19 | 0.00 | 0.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.81 | 20.22 | 34.23 | 5.00 | 81.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.41 | 13.55 | 21.93 | 2.00 | 81.0 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.50 | 10.24 | 16.70 | 2.00 | 73.1 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.91 | 16.72 | 26.72 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.54 | 16.23 | 25.55 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.53 | 15.42 | 24.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.15 | 14.12 | 22.50 | 8.00 | 82.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.33 | 12.86 | 21.00 | 2.00 | 87.0 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.00
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.63) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.63) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.19 | 11.48 | 18.22 | 7.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.18 | 0.20 | 0.00 | 4.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.54 | 15.20 | 23.96 | 6.00 | 89.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.35 | 12.19 | 19.05 | 4.00 | 85.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.11 | 11.81 | 19.35 | 2.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.44 | 5.24 | 9.44 | 1.00 | 41.5 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.19 | 0.82 | 3.28 | 0.00 | 4.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.74 | 20.53 | 34.63 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.91 | 12.56 | 20.69 | 5.00 | 73.7 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.00 | 9.18 | 15.55 | 7.00 | 63.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.86 | 16.54 | 26.43 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.38 | 15.81 | 25.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.66 | 13.91 | 22.19 | 2.00 | 77.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.76 | 13.79 | 22.17 | 10.00 | 81.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.11 | 11.95 | 19.06 | 2.00 | 80.8 | 90.0 |