# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 283.18
- Total actual points: 286.00
- Average predicted points: 70.79
- Average actual points: 71.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.81
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.72 | 11.12 | 18.89 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.87 | 8.92 | 15.33 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.33 | 14.76 | 20.57 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.38 | 13.65 | 20.27 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.51 | 11.62 | 18.26 | 7.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.09 | 9.44 | 12.97 | 6.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.0 | 1.89 | 9.40 | 13.26 | 17.00 | 88.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.90 | 24.68 | 39.84 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.92 | 16.18 | 26.78 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.96 | 4.04 | 7.06 | 12.00 | 20.5 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.20 | 19.75 | 34.01 | 2.00 | 89.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.04 | 18.47 | 28.17 | 7.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.32 | 14.85 | 23.24 | 2.00 | 90.0 | 82.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.33 | 14.23 | 21.80 | 2.00 | 90.0 | 80.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.26 | 13.94 | 22.99 | 2.00 | 87.5 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.96
- Actual score: 69.00
- Transfer: Tijjani Reijnders -> Jaidon Anthony (projected gain 0.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.83 | 10.94 | 17.78 | 6.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.87 | 8.75 | 14.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.03 | 15.17 | 20.34 | 2.00 | 85.2 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.51 | 14.48 | 21.06 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.05 | 12.33 | 16.91 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.38 | 9.17 | 12.43 | 3.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.36 | 8.12 | 12.13 | 0.00 | 46.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 25.33 | 39.32 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.11 | 13.16 | 21.72 | 2.00 | 71.8 | 73.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.96 | 5.80 | 9.13 | 0.00 | 35.7 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.25 | 18.74 | 28.07 | 18.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.21 | 18.51 | 31.49 | 2.00 | 85.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.50 | 12.67 | 18.70 | 7.00 | 68.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.28 | 12.32 | 19.20 | 12.00 | 74.2 | 89.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.7 | 3.87 | 11.69 | 18.06 | 1.00 | 85.5 | 58.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.58
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.17).
- Chip advisory: bench_boost (0.57): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Trevoh Chalobah -> Dan Burn (projected gain 1.05, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.17).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.75 | 10.89 | 17.79 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.46 | 9.31 | 14.94 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.33 | 14.41 | 20.25 | 2.00 | 77.9 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.1 | 3.81 | 11.68 | 17.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.64 | 11.26 | 21.22 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.73 | 10.76 | 13.71 | 17.00 | 78.1 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.59 | 10.72 | 14.14 | 6.00 | 71.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.03 | 24.50 | 39.45 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.56 | 12.38 | 22.36 | 2.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.87 | 3.89 | 6.65 | 24.00 | 20.4 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.16 | 20.30 | 32.71 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.02 | 17.90 | 30.48 | 2.00 | 82.7 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.45 | 15.69 | 23.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.04 | 12.83 | 20.43 | 4.00 | 81.7 | 85.0 |
| Bench 3 | Bench | Jaidon Anthony | MID | 3 | 5.7 | 3.51 | 9.79 | 15.59 | 2.00 | 65.4 | 82.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 81.83
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.19) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaidon Anthony -> Marshall Munetsi (projected gain 0.08, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.89 | 11.25 | 18.22 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.20 | 8.93 | 14.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.00 | 14.55 | 21.12 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.19 | 13.35 | 21.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.74 | 10.71 | 16.21 | 2.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.62 | 10.45 | 16.56 | 2.00 | 75.3 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.0 | 2.72 | 8.42 | 12.32 | 0.00 | 65.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.86 | 24.64 | 40.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.68 | 13.19 | 21.77 | 2.00 | 78.1 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.56 | 12.26 | 17.41 | 12.00 | 154.9 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.78 | 19.07 | 29.72 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.39 | 16.06 | 28.68 | 6.00 | 72.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 5.07 | 14.95 | 22.26 | 2.00 | 83.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.41 | 13.04 | 20.10 | 3.00 | 77.1 | 77.0 |
| Bench 2 | Bench Boost | Marshall Munetsi | MID | 20 | 5.4 | 4.17 | 11.07 | 16.47 | 8.00 | 80.5 | 83.0 |