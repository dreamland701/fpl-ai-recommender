# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 261.59
- Total actual points: 225.00
- Average predicted points: 65.40
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
- Predicted score: 65.41
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.68 | 10.67 | 17.41 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.35 | 0.42 | 0.65 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.94 | 13.66 | 19.61 | 8.00 | 78.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.59 | 20.26 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.28 | 12.58 | 19.85 | 8.00 | 86.8 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.15 | 10.93 | 17.38 | 0.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.36 | 9.31 | 14.34 | 0.00 | 83.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.21 | 23.90 | 38.77 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.59 | 15.35 | 24.37 | 2.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.00 | 12.31 | 19.37 | 2.00 | 75.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.40 | 15.84 | 25.57 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.63 | 15.61 | 24.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.12 | 14.60 | 24.36 | 3.00 | 78.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.96 | 14.27 | 23.64 | 2.00 | 82.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.91 | 13.80 | 22.21 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.62
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.60, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 10.82 | 17.53 | 1.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.08 | 0.37 | 0.00 | 5.8 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.88 | 13.29 | 21.51 | 4.00 | 89.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.59 | 13.26 | 19.81 | 1.00 | 79.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.25 | 11.73 | 17.83 | 11.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.67 | 10.19 | 16.76 | 7.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.85 | 5.67 | 9.25 | 0.00 | 44.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.26 | 22.55 | 36.97 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.79 | 15.90 | 25.38 | 2.00 | 89.6 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.56 | 10.84 | 17.14 | 2.00 | 72.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.54 | 16.11 | 25.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.70 | 15.86 | 25.30 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.66 | 13.39 | 21.89 | 0.00 | 78.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.67 | 13.24 | 21.57 | 8.00 | 77.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.18 | 11.81 | 19.59 | 10.00 | 74.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.36
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.64) beats the best remaining Triple Captain opportunity (7.43).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.10, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.64) beats the best remaining Triple Captain opportunity (7.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.84 | 17.53 | 6.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.20 | 0.35 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.97 | 14.15 | 22.34 | 8.00 | 86.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.88 | 19.50 | 2.00 | 81.7 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.79 | 11.17 | 17.76 | 0.00 | 87.7 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.21 | 9.64 | 16.17 | 0.00 | 85.2 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.07 | 3.69 | 7.31 | 0.00 | 27.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.64 | 19.71 | 33.40 | 5.00 | 78.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.43 | 13.80 | 22.52 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.45 | 10.09 | 16.49 | 2.00 | 71.8 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.91 | 16.82 | 27.04 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.63 | 16.60 | 26.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.47 | 15.18 | 24.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.13 | 14.10 | 22.56 | 8.00 | 81.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.29 | 12.70 | 20.75 | 2.00 | 86.0 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.20
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 11.37 | 18.11 | 7.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.01 | 0.05 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.50 | 15.09 | 23.84 | 6.00 | 88.6 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.31 | 12.10 | 18.98 | 4.00 | 84.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.70 | 19.23 | 2.00 | 81.9 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.31 | 4.98 | 9.15 | 1.00 | 38.4 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.11 | 0.68 | 3.06 | 0.00 | 3.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.56 | 19.96 | 33.67 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.89 | 12.73 | 21.20 | 5.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.01 | 9.11 | 15.32 | 7.00 | 63.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.92 | 16.95 | 27.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.37 | 15.89 | 26.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.68 | 14.10 | 22.67 | 2.00 | 77.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.69 | 13.50 | 21.70 | 10.00 | 80.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.09 | 12.02 | 19.31 | 2.00 | 79.8 | 90.0 |