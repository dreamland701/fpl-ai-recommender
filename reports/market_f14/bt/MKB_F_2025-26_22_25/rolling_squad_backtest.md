# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.35
- Total actual points: 225.00
- Average predicted points: 66.09
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
- Predicted score: 65.98
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 11.16 | 18.09 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.02 | 0.19 | 0.00 | 3.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.07 | 13.98 | 20.09 | 8.00 | 79.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.58 | 12.88 | 20.72 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.23 | 12.51 | 19.80 | 8.00 | 86.3 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.14 | 10.94 | 17.37 | 0.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.38 | 9.34 | 14.39 | 0.00 | 83.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.26 | 24.28 | 39.56 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.53 | 15.02 | 23.78 | 2.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.06 | 12.52 | 19.71 | 2.00 | 77.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.41 | 15.86 | 25.56 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.62 | 15.77 | 25.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.10 | 14.70 | 24.30 | 2.00 | 84.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.08 | 14.28 | 23.66 | 3.00 | 77.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.96 | 14.01 | 22.58 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.89
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.58, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 11.22 | 18.11 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.44 | 0.49 | 0.71 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.65 | 13.46 | 20.14 | 1.00 | 79.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.85 | 13.20 | 21.38 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.31 | 11.89 | 18.06 | 11.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.75 | 10.37 | 17.01 | 7.00 | 83.4 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.77 | 5.47 | 8.93 | 0.00 | 41.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.38 | 23.04 | 37.89 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.83 | 15.79 | 25.05 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.63 | 11.05 | 17.49 | 2.00 | 73.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.71 | 15.83 | 25.18 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.38 | 15.62 | 24.28 | 1.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.65 | 13.35 | 21.85 | 8.00 | 78.8 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.54 | 13.27 | 21.85 | 0.00 | 77.0 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.23 | 12.00 | 19.96 | 10.00 | 76.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.09
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.36).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (7.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.05 | 11.36 | 18.24 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.21 | 0.31 | 0.00 | 2.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.10 | 14.50 | 22.83 | 8.00 | 87.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 12.04 | 19.76 | 2.00 | 82.7 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.78 | 11.18 | 17.83 | 0.00 | 88.4 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.18 | 9.59 | 16.14 | 0.00 | 85.8 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.94 | 3.36 | 6.78 | 0.00 | 25.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.76 | 20.22 | 34.32 | 5.00 | 81.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.53 | 21.97 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.40 | 10.02 | 16.45 | 2.00 | 72.7 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.95 | 16.89 | 27.03 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.55 | 16.28 | 25.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.46 | 15.28 | 24.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.23 | 14.34 | 22.88 | 8.00 | 83.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.29 | 12.80 | 20.98 | 2.00 | 87.1 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.40
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 4.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.33 | 11.79 | 18.69 | 7.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.59 | 15.31 | 24.14 | 6.00 | 88.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.40 | 12.36 | 19.37 | 4.00 | 86.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.05 | 11.73 | 19.30 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.73 | 6.06 | 10.84 | 1.00 | 47.0 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.61 | 1.88 | 4.84 | 0.00 | 11.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.62 | 20.33 | 34.47 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.66 | 12.00 | 19.98 | 5.00 | 69.6 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.06 | 9.30 | 15.63 | 7.00 | 64.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.82 | 16.40 | 26.20 | 5.00 | 87.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.36 | 15.86 | 25.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.70 | 14.03 | 22.40 | 2.00 | 77.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.75 | 13.83 | 22.32 | 10.00 | 80.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.10 | 11.96 | 19.12 | 2.00 | 80.0 | 90.0 |