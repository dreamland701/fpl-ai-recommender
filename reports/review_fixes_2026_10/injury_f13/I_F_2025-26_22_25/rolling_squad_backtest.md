# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 267.42
- Total actual points: 227.00
- Average predicted points: 66.86
- Average actual points: 56.75
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
- Predicted score: 66.10
- Actual score: 46.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 11.06 | 18.00 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.36 | 9.73 | 15.85 | 1.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.15 | 13.75 | 19.83 | 8.00 | 83.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.52 | 12.84 | 20.67 | 0.00 | 95.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.51 | 12.63 | 19.76 | 5.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.23 | 12.60 | 19.85 | 8.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 4.05 | 11.35 | 19.12 | 1.00 | 81.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.10 | 23.93 | 39.07 | 2.00 | 118.5 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.95 | 15.53 | 24.45 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.89 | 8.09 | 12.23 | 2.00 | 67.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.42 | 15.81 | 25.47 | 2.00 | 97.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.81 | 15.70 | 25.04 | 3.00 | 100.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.22 | 14.81 | 24.46 | 2.00 | 85.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.21 | 14.20 | 22.81 | 2.00 | 95.8 | 87.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.32 | 13.05 | 20.81 | 4.00 | 88.3 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.00
- Actual score: 50.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 0.11, hit 0)
- Autosub: Cristian Romero replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.94 | 11.15 | 18.03 | 1.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.09 | 8.98 | 14.83 | 1.00 | 82.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.98 | 13.41 | 21.64 | 4.00 | 90.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.60 | 13.24 | 19.87 | 1.00 | 80.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.32 | 12.34 | 19.39 | 1.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Cristian Romero | DEF | 18 | 5.0 | 4.23 | 11.80 | 17.97 | 11.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 3.75 | 10.62 | 17.57 | 1.00 | 81.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 22.73 | 37.48 | 1.00 | 114.6 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 6.08 | 16.04 | 25.40 | 2.00 | 93.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.94 | 12.73 | 2.00 | 69.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.78 | 15.81 | 25.14 | 8.00 | 93.5 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 5.01 | 13.97 | 21.98 | 2.00 | 90.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.80 | 13.68 | 22.25 | 8.00 | 78.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.49 | 13.31 | 21.90 | 0.00 | 75.9 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.43 | 12.21 | 20.21 | 10.00 | 77.5 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.49
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.08).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.25, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 11.17 | 18.02 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.62 | 8.28 | 13.88 | 10.00 | 80.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.01 | 14.15 | 22.40 | 8.00 | 89.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.09 | 12.09 | 19.77 | 2.00 | 83.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.05 | 11.83 | 19.22 | 5.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Cristian Romero | DEF | 18 | 5.0 | 3.75 | 11.24 | 17.89 | 0.00 | 86.3 | 45.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.80 | 9.09 | 15.41 | 1.00 | 77.8 | 30.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.50 | 19.89 | 33.88 | 5.00 | 82.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.36 | 13.64 | 22.09 | 2.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.03 | 8.05 | 13.28 | 2.00 | 67.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.97 | 16.84 | 26.96 | 7.00 | 100.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.62 | 15.60 | 24.83 | 2.00 | 93.2 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.50 | 14.35 | 22.90 | 8.00 | 87.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.36 | 12.97 | 21.17 | 2.00 | 86.2 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.07 | 12.34 | 20.05 | 4.00 | 81.9 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.83
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Tarkowski -> Trevoh Chalobah (projected gain 0.51, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.28 | 11.66 | 18.55 | 7.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 2.98 | 8.89 | 14.62 | 1.00 | 81.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.51 | 15.04 | 23.81 | 6.00 | 90.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.45 | 12.35 | 19.35 | 4.00 | 87.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.59 | 12.34 | 19.86 | 6.00 | 81.3 | 90.0 |
| Bench 3 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.56 | 8.20 | 14.23 | 0.00 | 58.0 | 0.0 |
| Bench 4 | Bench Boost | Cristian Romero | DEF | 18 | 5.0 | 2.55 | 7.97 | 14.11 | -3.00 | 59.5 | 28.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.41 | 20.22 | 34.27 | 11.00 | 93.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.65 | 12.35 | 20.42 | 5.00 | 65.0 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.99 | 8.63 | 14.07 | 2.00 | 69.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.43 | 15.99 | 26.05 | 2.00 | 95.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.88 | 14.01 | 22.38 | 2.00 | 80.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.76 | 13.93 | 22.42 | 10.00 | 80.0 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.22 | 12.13 | 19.33 | 4.00 | 83.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.16 | 12.05 | 19.22 | 2.00 | 80.1 | 90.0 |