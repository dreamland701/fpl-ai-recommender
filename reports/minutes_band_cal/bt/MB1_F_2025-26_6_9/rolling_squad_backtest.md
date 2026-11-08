# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 255.70
- Total actual points: 272.00
- Average predicted points: 63.93
- Average actual points: 68.00
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
- Predicted score: 63.46
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.1 | 3.64 | 9.82 | 16.33 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.13 | 0.53 | 1.87 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.62 | 12.77 | 17.81 | 7.00 | 82.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.57 | 11.68 | 18.28 | 7.00 | 84.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.30 | 11.40 | 18.33 | 2.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.36 | 10.23 | 14.05 | 6.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.51 | 8.98 | 13.81 | 7.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.22 | 22.67 | 37.20 | 16.00 | 82.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.35 | 14.50 | 24.49 | 2.00 | 82.7 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.60 | 12.80 | 20.99 | 2.00 | 73.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.62 | 17.94 | 31.60 | 2.00 | 82.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.31 | 16.39 | 25.38 | 7.00 | 82.7 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 5.41 | 13.52 | 22.01 | 2.00 | 80.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.63 | 12.90 | 20.65 | 2.00 | 82.7 | 82.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 4.60 | 11.71 | 18.30 | 2.00 | 84.9 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.16
- Actual score: 61.00
- Transfer: Nordi Mukiele -> Omar Alderete (projected gain 1.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.1 | 2.94 | 9.02 | 15.05 | 3.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.01 | 0.37 | 0.99 | 0.00 | 5.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.10 | 15.15 | 20.14 | 2.00 | 84.2 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.95 | 12.85 | 18.82 | 3.00 | 82.8 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.67 | 11.30 | 15.66 | 0.00 | 82.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.62 | 10.73 | 16.86 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.51 | 9.56 | 13.53 | 1.00 | 79.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.12 | 23.75 | 37.13 | 8.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.12 | 13.15 | 21.61 | 2.00 | 73.9 | 73.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.15 | 10.08 | 16.24 | 1.00 | 57.3 | 16.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.30 | 18.52 | 31.37 | 2.00 | 84.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.64 | 16.93 | 25.51 | 18.00 | 82.8 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 3.83 | 11.98 | 18.97 | 10.00 | 69.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.74 | 11.44 | 17.19 | 3.00 | 69.9 | 75.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.21 | 9.82 | 14.59 | 2.00 | 77.3 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.33
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.21).
- Transfer: Marc Guéhi -> Nordi Mukiele (projected gain 1.91, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (8.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.1 | 2.94 | 8.61 | 14.44 | 1.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.11 | 0.35 | 0.91 | 0.00 | 5.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.36 | 14.35 | 20.15 | 2.00 | 79.5 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 3.88 | 11.61 | 15.63 | 6.00 | 74.6 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.98 | 11.45 | 14.75 | 17.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 4.0 | 3.49 | 10.84 | 13.76 | 1.00 | 79.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.68 | 9.68 | 16.22 | 0.00 | 82.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.51 | 22.88 | 37.23 | 13.00 | 82.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.64 | 12.54 | 22.42 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.48 | 8.01 | 12.78 | 1.00 | 39.2 | 30.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 6.58 | 18.50 | 30.25 | 4.00 | 82.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 6.12 | 17.91 | 30.32 | 2.00 | 82.0 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.02 | 10.65 | 18.58 | 1.00 | 75.1 | 58.0 |
| Bench 3 | Bench | Jack Grealish | MID | 9 | 6.9 | 3.34 | 10.20 | 17.65 | 0.00 | 71.1 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.60 | 9.64 | 14.91 | 2.00 | 73.9 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 0.80 -> -0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.75
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Nick Woltemade (projected gain 5.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.1 | 2.80 | 8.29 | 13.98 | 6.00 | 80.9 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.03 | 0.25 | 0.78 | 0.00 | 5.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.45 | 12.97 | 18.87 | 5.00 | 82.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 3.96 | 11.21 | 17.01 | 2.00 | 81.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.39 | 9.62 | 15.32 | 23.00 | 81.6 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.46 | 9.14 | 13.40 | 13.00 | 75.7 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.95 | 9.13 | 13.61 | 0.00 | 68.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.32 | 23.11 | 38.80 | 2.00 | 82.8 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 5.33 | 15.32 | 22.66 | 2.00 | 80.0 | 85.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.64 | 12.98 | 21.54 | 2.00 | 80.0 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.23 | 17.51 | 27.46 | 3.00 | 82.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.45 | 16.08 | 28.59 | 6.00 | 75.0 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.25 | 10.11 | 16.55 | 1.00 | 59.6 | 75.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.36 | 9.14 | 13.99 | 0.00 | 65.8 | 0.0 |
| Bench 4 | Bench Boost | Jack Grealish | MID | 9 | 6.9 | 2.82 | 8.36 | 14.86 | 1.00 | 42.1 | 90.0 |