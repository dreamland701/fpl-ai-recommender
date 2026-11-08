# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 216.78
- Total actual points: 245.00
- Average predicted points: 54.20
- Average actual points: 61.25
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
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.12
- Actual score: 27.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.35 | 9.92 | 17.06 | 2.00 | 95.8 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.47 | 9.83 | 16.75 | 2.00 | 98.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.85 | 13.47 | 18.91 | 7.00 | 104.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.33 | 11.46 | 16.07 | 1.00 | 91.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.08 | 11.41 | 18.02 | 2.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.31 | 11.33 | 18.77 | 13.00 | 96.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.48 | 10.60 | 16.72 | 2.00 | 83.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.02 | 13.80 | 23.85 | 2.00 | 92.4 | 90.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.52 | 6.80 | 12.61 | 2.00 | 62.2 | 68.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.20 | 6.66 | 11.76 | 2.00 | 76.9 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.20 | 17.77 | 31.66 | 2.00 | 85.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.33 | 16.33 | 24.33 | 7.00 | 100.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.91 | 16.17 | 27.02 | -1.00 | 95.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.11 | 13.43 | 20.98 | 2.00 | 99.2 | 80.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.46 | 12.48 | 19.25 | 2.00 | 105.1 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marcos Senesi Barón
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 45.62
- Actual score: 69.00
- Transfer: James Tarkowski -> Marc Guéhi (projected gain 2.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.38 | 9.96 | 16.23 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.48 | 7.23 | 11.51 | 6.00 | 76.1 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.74 | 14.01 | 17.75 | 2.00 | 91.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 3.83 | 12.28 | 20.10 | 3.00 | 102.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.17 | 11.25 | 16.19 | 9.00 | 97.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.33 | 10.85 | 15.93 | 1.00 | 84.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 2.75 | 9.22 | 14.19 | 2.00 | 81.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.50 | 10.91 | 17.30 | 2.00 | 65.4 | 73.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.26 | 6.67 | 10.87 | 1.00 | 73.7 | 68.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.15 | 6.37 | 11.11 | 1.00 | 60.5 | 45.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 4.25 | 15.47 | 25.49 | 2.00 | 78.4 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 4.84 | 14.77 | 22.15 | 18.00 | 98.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.11 | 12.00 | 19.01 | 3.00 | 71.3 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 2.68 | 10.74 | 15.79 | 7.00 | 73.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 2.87 | 10.07 | 15.32 | 3.00 | 69.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 55.65
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.40).
- Transfer: Virgil van Dijk -> Jurriën Timber (projected gain 3.75, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.91 | 8.04 | 13.07 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 2.86 | 7.83 | 13.02 | 6.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.75 | 14.74 | 20.21 | 12.00 | 92.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 13.27 | 18.91 | 2.00 | 82.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.41 | 12.24 | 17.96 | 6.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.16 | 8.76 | 14.08 | 0.00 | 82.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 3.35 | 7.62 | 15.63 | 4.00 | 93.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 3.21 | 10.22 | 21.04 | 2.00 | 55.9 | 90.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.3 | 1.36 | 6.08 | 10.05 | 2.00 | 26.3 | 74.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.31 | 5.55 | 10.74 | 0.00 | 67.9 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 6.01 | 16.66 | 26.91 | 4.00 | 118.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.4 | 5.28 | 15.93 | 28.14 | 2.00 | 79.2 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.19 | 13.00 | 19.99 | 8.00 | 71.4 | 84.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.25 | 11.56 | 18.04 | 4.00 | 82.8 | 85.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.39 | 8.89 | 15.99 | 1.00 | 75.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 59.39
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 3.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.22 | 10.49 | 17.44 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.64 | 8.24 | 14.37 | 2.00 | 84.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.60 | 14.11 | 23.18 | 9.00 | 95.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 3.51 | 11.39 | 17.22 | 6.00 | 76.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 3.27 | 11.01 | 17.48 | 4.00 | 91.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.65 | 10.78 | 15.38 | 5.00 | 73.4 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 2.55 | 8.39 | 13.20 | 23.00 | 79.6 | 90.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 5.21 | 11.88 | 16.98 | 12.00 | 96.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.25 | 10.66 | 17.36 | 2.00 | 77.7 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.3 | 2.32 | 6.67 | 9.94 | 2.00 | 66.1 | 65.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 5.43 | 15.28 | 24.00 | 3.00 | 94.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 3.82 | 13.71 | 25.30 | 6.00 | 61.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.17 | 13.15 | 19.51 | 2.00 | 87.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 3.98 | 12.18 | 19.13 | 4.00 | 84.7 | 90.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 2.34 | 8.21 | 14.20 | 1.00 | 60.6 | 75.0 |