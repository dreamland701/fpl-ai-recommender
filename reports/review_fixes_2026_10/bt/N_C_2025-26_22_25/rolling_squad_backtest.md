# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 272.63
- Total actual points: 218.00
- Average predicted points: 68.16
- Average actual points: 54.50
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
- Predicted score: 65.81
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 11.07 | 18.03 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.08 | 9.29 | 15.12 | 5.00 | 95.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.08 | 13.66 | 19.70 | 8.00 | 83.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.66 | 13.13 | 21.03 | 0.00 | 98.3 | 0.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.15 | 12.49 | 19.75 | 8.00 | 85.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.47 | 11.96 | 19.28 | 2.00 | 91.1 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 3.87 | 11.19 | 18.97 | 1.00 | 81.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.45 | 24.79 | 40.25 | 2.00 | 120.7 | 79.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.25 | 12.44 | 19.53 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.81 | 7.99 | 12.08 | 2.00 | 65.6 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.84 | 16.10 | 25.54 | 3.00 | 98.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.49 | 15.95 | 25.63 | 2.00 | 99.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.17 | 14.60 | 24.19 | 2.00 | 86.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.14 | 14.04 | 22.60 | 2.00 | 95.8 | 87.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.02 | 14.04 | 23.39 | 3.00 | 80.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.79
- Actual score: 42.00
- Transfer: Virgil van Dijk -> Trevoh Chalobah (projected gain 2.03, hit 0)
- Autosub: Nathan Collins replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.00 | 11.27 | 18.16 | 1.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.40 | 9.73 | 15.82 | 5.00 | 98.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.76 | 13.46 | 20.07 | 1.00 | 79.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.90 | 13.22 | 21.43 | 4.00 | 89.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.58 | 12.53 | 19.33 | 4.00 | 97.7 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 5.0 | 3.63 | 10.51 | 17.49 | 1.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.91 | 7.96 | 13.71 | 6.00 | 50.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.53 | 23.55 | 38.60 | 1.00 | 115.4 | 17.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.69 | 10.93 | 17.30 | 2.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.58 | 7.99 | 12.78 | 2.00 | 69.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.87 | 15.89 | 25.21 | 8.00 | 95.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 15.66 | 24.29 | 1.00 | 93.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.38 | 13.55 | 22.22 | 0.00 | 74.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.68 | 13.42 | 21.87 | 8.00 | 77.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.35 | 12.24 | 20.26 | 10.00 | 77.0 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.95
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 4.07, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.81) beats the best remaining Triple Captain opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.97 | 11.17 | 18.00 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.37 | 9.85 | 16.17 | 1.00 | 100.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.09 | 14.26 | 22.50 | 8.00 | 89.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.88 | 12.92 | 20.05 | 3.00 | 95.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 12.05 | 19.72 | 2.00 | 83.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.80 | 10.82 | 17.75 | 3.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.90 | 9.34 | 15.80 | 1.00 | 79.2 | 30.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.81 | 20.47 | 34.70 | 5.00 | 85.3 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.49 | 10.26 | 16.78 | 2.00 | 72.3 | 84.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.88 | 7.90 | 13.13 | 2.00 | 66.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.93 | 16.66 | 26.74 | 7.00 | 103.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.57 | 16.12 | 25.39 | 3.00 | 94.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.58 | 15.50 | 24.69 | 2.00 | 94.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.30 | 14.21 | 22.77 | 8.00 | 85.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.32 | 12.81 | 20.96 | 2.00 | 85.9 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 74.08
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nathan Collins -> Virgil van Dijk (projected gain 1.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.31 | 11.71 | 18.67 | 7.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.38 | 9.49 | 15.50 | 1.00 | 94.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.61 | 15.28 | 24.21 | 6.00 | 91.6 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.50 | 12.39 | 19.42 | 4.00 | 88.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.19 | 12.23 | 19.38 | 0.00 | 91.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 11.76 | 19.33 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.2 | 3.59 | 10.47 | 17.31 | 3.00 | 73.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.64 | 20.70 | 35.03 | 11.00 | 95.1 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.12 | 9.33 | 15.67 | 7.00 | 64.3 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.99 | 8.60 | 14.08 | 2.00 | 69.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.81 | 16.34 | 26.20 | 5.00 | 90.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.44 | 15.90 | 25.98 | 2.00 | 97.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.01 | 13.95 | 22.31 | 2.00 | 81.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.65 | 13.91 | 22.42 | 10.00 | 81.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.16 | 12.11 | 19.35 | 2.00 | 80.6 | 90.0 |