# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 276.72
- Total actual points: 297.00
- Average predicted points: 69.18
- Average actual points: 74.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.37
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.79 | 11.22 | 18.36 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.66 | 1.45 | 2.51 | 0.00 | 5.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.38 | 15.17 | 22.32 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.54 | 14.45 | 22.26 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.63 | 12.33 | 20.03 | 7.00 | 89.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.43 | 10.71 | 15.90 | 6.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.14 | 10.62 | 16.13 | 17.00 | 89.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.02 | 24.37 | 39.89 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.49 | 14.58 | 24.26 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.26 | 2.94 | 5.73 | 12.00 | 16.3 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.15 | 19.77 | 34.27 | 2.00 | 88.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 17.71 | 27.83 | 7.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.22 | 13.80 | 21.71 | 2.00 | 90.0 | 80.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.00 | 13.73 | 22.15 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.20 | 13.55 | 22.74 | 2.00 | 86.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.23
- Actual score: 65.00
- Transfer: Trevoh Chalobah -> Tyrick Mitchell (projected gain 1.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.87 | 11.12 | 17.45 | 6.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.35 | 1.19 | 1.89 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.19 | 15.53 | 21.37 | 2.00 | 87.5 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.63 | 14.89 | 22.04 | 3.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 4.33 | 13.41 | 19.13 | 0.00 | 90.0 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 8 | 5.0 | 3.65 | 11.71 | 18.09 | 1.00 | 85.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.66 | 10.21 | 14.40 | 3.00 | 79.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.91 | 25.37 | 39.22 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.67 | 11.73 | 18.78 | 2.00 | 72.8 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.80 | 5.32 | 8.25 | 0.00 | 32.8 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.24 | 18.53 | 31.16 | 2.00 | 84.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.11 | 18.15 | 27.16 | 18.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.41 | 12.11 | 17.95 | 7.00 | 68.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.07 | 11.53 | 18.14 | 12.00 | 74.2 | 89.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 3.50 | 10.44 | 15.54 | 3.00 | 67.9 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.29
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.57) beats the best remaining Bench Boost opportunity (10.29).
- Transfer: Marc Guéhi -> Dan Burn (projected gain 1.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.57) beats the best remaining Bench Boost opportunity (10.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.77 | 10.94 | 17.55 | 6.00 | 84.6 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.41 | 1.03 | 1.66 | 0.00 | 5.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.49 | 14.62 | 20.86 | 2.00 | 80.6 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.1 | 4.00 | 12.52 | 18.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.96 | 11.88 | 16.12 | 6.00 | 73.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.97 | 11.76 | 15.39 | 17.00 | 77.4 | 90.0 |
| Bench 3 | Bench Boost | Tyrick Mitchell | DEF | 8 | 5.0 | 3.55 | 9.54 | 17.02 | 1.00 | 83.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.20 | 24.77 | 39.28 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.27 | 11.29 | 19.85 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 1.39 | 3.14 | 5.34 | 24.00 | 17.7 | 148.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.95 | 19.52 | 31.49 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.12 | 18.06 | 30.33 | 2.00 | 81.8 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 15.44 | 22.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.25 | 19.57 | 4.00 | 80.8 | 85.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.73 | 9.70 | 16.85 | 1.00 | 72.4 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Erling Haaland
- Effective captain: Junior Kroupi
- Chip used: triple_captain
- Predicted score: 74.84
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Tyrick Mitchell -> Marc Guéhi (projected gain 2.59, hit 0)
- Chip used: Triple Captain on Junior Kroupi. Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.05 | 17.71 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.33 | 0.93 | 1.60 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.04 | 14.78 | 21.34 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 4.24 | 13.52 | 22.04 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.89 | 11.43 | 17.77 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 5.1 | 3.81 | 11.03 | 17.58 | 2.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.01 | 9.26 | 13.99 | 0.00 | 67.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.5 | 7.84 | 24.54 | 40.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.25 | 11.91 | 19.21 | 2.00 | 79.1 | 84.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 8.13 | 11.57 | 15.93 | 12.00 | 157.1 | 136.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.56 | 18.30 | 28.14 | 3.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.48 | 16.22 | 28.69 | 6.00 | 72.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.94 | 14.42 | 21.32 | 2.00 | 82.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.37 | 12.70 | 19.37 | 3.00 | 77.5 | 77.0 |
| Bench 4 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 2.71 | 8.63 | 14.33 | 1.00 | 55.9 | 75.0 |