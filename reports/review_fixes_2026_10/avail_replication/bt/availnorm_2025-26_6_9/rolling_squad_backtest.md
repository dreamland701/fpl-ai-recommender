# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 237.54
- Total actual points: 236.00
- Average predicted points: 59.38
- Average actual points: 59.00
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
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.83
- Actual score: 27.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.03 | 10.48 | 17.33 | 2.00 | 94.5 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.53 | 10.37 | 17.88 | 2.00 | 94.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.34 | 13.91 | 19.69 | 7.00 | 99.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.77 | 12.17 | 17.57 | 1.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.67 | 11.88 | 19.05 | 2.00 | 72.8 | 90.0 |
| Bench 2 | Bench | Riccardo Calafiori | DEF | 1 | 5.7 | 3.51 | 10.52 | 18.36 | 1.00 | 73.0 | 69.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.95 | 10.35 | 17.27 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.28 | 14.51 | 24.65 | 2.00 | 94.4 | 90.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.17 | 8.86 | 15.23 | 2.00 | 60.7 | 84.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.57 | 7.51 | 13.51 | 2.00 | 77.9 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.07 | 17.50 | 30.85 | 2.00 | 82.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.71 | 16.34 | 25.69 | 7.00 | 98.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.08 | 16.21 | 26.40 | -1.00 | 90.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.92 | 13.20 | 21.30 | 2.00 | 105.1 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.93 | 12.93 | 21.81 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 51.50
- Actual score: 78.00
- Transfer: Micky van de Ven -> Marc Guéhi (projected gain 2.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.68 | 10.34 | 16.86 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.54 | 7.99 | 13.10 | 6.00 | 70.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.90 | 14.17 | 18.76 | 2.00 | 87.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.21 | 12.97 | 18.76 | 3.00 | 102.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.53 | 11.19 | 16.40 | 1.00 | 82.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.84 | 10.44 | 14.76 | 5.00 | 77.3 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 3.62 | 10.18 | 16.53 | 6.00 | 58.6 | 74.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.01 | 11.03 | 18.31 | 2.00 | 66.4 | 73.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 2.79 | 7.89 | 12.48 | 1.00 | 58.1 | 58.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.40 | 7.40 | 11.69 | 1.00 | 65.7 | 68.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.11 | 16.33 | 28.07 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 5.59 | 16.27 | 24.19 | 18.00 | 98.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.66 | 13.04 | 20.42 | 3.00 | 64.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.75 | 10.91 | 17.16 | 12.00 | 72.6 | 89.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.7 | 3.26 | 10.08 | 15.03 | 3.00 | 64.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 59.99
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.49) beats the best remaining Triple Captain opportunity (7.95).
- Transfer: Virgil van Dijk -> Jurriën Timber (projected gain 4.00, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.49) beats the best remaining Triple Captain opportunity (7.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.40 | 9.88 | 16.28 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.04 | 8.77 | 14.46 | 6.00 | 81.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.96 | 12.96 | 18.06 | 2.00 | 78.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.50 | 12.28 | 18.11 | 6.00 | 83.4 | 90.0 |
| Bench 2 | Bench | James Tarkowski | DEF | 9 | 5.5 | 3.09 | 10.92 | 15.08 | 3.00 | 81.0 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 3.39 | 9.61 | 15.66 | 6.00 | 63.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.07 | 9.61 | 18.45 | 4.00 | 94.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.06 | 11.15 | 20.25 | 2.00 | 75.9 | 90.0 |
| Bench 3 | Bench | Wilson Isidor | FWD | 17 | 5.5 | 3.06 | 7.77 | 12.70 | 2.00 | 53.5 | 75.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.62 | 6.24 | 12.53 | 0.00 | 56.9 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 6.46 | 17.67 | 28.46 | 4.00 | 119.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.4 | 5.15 | 16.15 | 27.71 | 2.00 | 73.2 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.98 | 13.94 | 20.68 | 2.00 | 101.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.56 | 13.17 | 19.25 | 8.00 | 66.4 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.52 | 9.43 | 16.49 | 1.00 | 71.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Antoine Semenyo
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 65.23
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 3.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.60 | 10.30 | 16.89 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.80 | 8.71 | 14.53 | 2.00 | 80.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 3.70 | 11.73 | 18.99 | 4.00 | 93.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.11 | 11.52 | 17.84 | 6.00 | 72.8 | 90.0 |
| Bench 2 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.37 | 10.78 | 15.38 | 5.00 | 93.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.54 | 10.45 | 16.28 | 1.00 | 83.5 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 3.75 | 10.41 | 16.61 | 6.00 | 73.5 | 81.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 6.12 | 13.81 | 19.67 | 12.00 | 106.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.85 | 11.34 | 18.97 | 2.00 | 76.7 | 84.0 |
| Bench 4 | Bench Boost | Wilson Isidor | FWD | 17 | 5.5 | 2.45 | 7.25 | 12.26 | 7.00 | 51.7 | 74.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 5.99 | 16.87 | 26.14 | 3.00 | 97.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.77 | 15.05 | 27.13 | 6.00 | 62.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.41 | 12.70 | 20.12 | 4.00 | 80.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.82 | 11.53 | 17.65 | 3.00 | 74.1 | 77.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 2.84 | 9.20 | 15.29 | 1.00 | 53.6 | 75.0 |