# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 270.65
- Total actual points: 248.00
- Average predicted points: 67.66
- Average actual points: 62.00
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 67.22
- Actual score: 27.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.62 | 19.86 | 2.00 | 95.8 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.27 | 11.13 | 18.35 | 2.00 | 98.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.65 | 14.77 | 21.11 | 7.00 | 104.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.30 | 13.48 | 21.75 | 2.00 | 78.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 5.26 | 13.44 | 19.51 | 1.00 | 91.1 | 90.0 |
| Bench 2 | Bench | Riccardo Calafiori | DEF | 1 | 5.7 | 4.03 | 12.11 | 21.00 | 1.00 | 79.0 | 69.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.53 | 11.99 | 19.87 | 2.00 | 83.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.02 | 16.70 | 28.05 | 2.00 | 92.4 | 90.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 3.79 | 10.13 | 17.93 | 2.00 | 62.2 | 68.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 8.64 | 15.34 | 2.00 | 76.9 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.88 | 19.91 | 34.87 | 2.00 | 85.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.33 | 18.33 | 28.73 | 7.00 | 100.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.41 | 17.17 | 28.02 | -1.00 | 95.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.56 | 14.98 | 24.05 | 2.00 | 105.1 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.63 | 14.81 | 24.85 | 2.00 | 89.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.81
- Actual score: 75.00
- Transfer: Riccardo Calafiori -> Marc Guéhi (projected gain 3.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.21 | 11.82 | 19.22 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.92 | 9.19 | 15.05 | 6.00 | 76.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.38 | 15.62 | 20.99 | 2.00 | 91.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.83 | 14.78 | 21.60 | 3.00 | 102.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.02 | 12.72 | 18.93 | 1.00 | 84.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.35 | 11.91 | 17.02 | 5.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.63 | 10.96 | 17.38 | 2.00 | 81.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.70 | 13.11 | 21.70 | 2.00 | 65.4 | 73.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 3.10 | 9.45 | 15.70 | 1.00 | 60.5 | 45.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.76 | 8.51 | 13.45 | 1.00 | 73.7 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.44 | 18.77 | 28.15 | 18.00 | 98.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.88 | 18.74 | 32.12 | 2.00 | 78.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.35 | 15.01 | 23.58 | 3.00 | 71.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.39 | 12.75 | 20.11 | 12.00 | 75.6 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.82 | 11.85 | 17.78 | 3.00 | 69.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 1.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 69.12
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (9.12).
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 6.05, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (9.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.47 | 18.81 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.49 | 10.07 | 16.53 | 6.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.35 | 15.84 | 22.61 | 12.00 | 92.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.57 | 14.93 | 21.14 | 2.00 | 82.1 | 90.0 |
| Bench 2 | Bench | James Tarkowski | DEF | 9 | 5.5 | 3.54 | 12.42 | 17.49 | 3.00 | 84.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.75 | 11.62 | 21.63 | 4.00 | 93.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.60 | 9.87 | 16.76 | 0.00 | 82.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.73 | 13.11 | 23.60 | 2.00 | 55.9 | 90.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.3 | 2.34 | 9.69 | 15.39 | 2.00 | 26.3 | 74.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 3.03 | 7.17 | 14.52 | 0.00 | 67.9 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.41 | 20.46 | 32.91 | 4.00 | 118.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.4 | 5.96 | 18.61 | 31.87 | 2.00 | 79.2 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.70 | 15.97 | 23.92 | 2.00 | 100.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.16 | 15.16 | 22.41 | 8.00 | 71.4 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.13 | 11.15 | 19.34 | 1.00 | 75.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Junior Kroupi
- Vice captain: Antoine Semenyo
- Effective captain: Junior Kroupi
- Chip used: bench_boost
- Predicted score: 75.49
- Actual score: 95.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 6.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.41) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.10 | 11.72 | 19.13 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.18 | 9.86 | 16.37 | 2.00 | 84.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.70 | 16.31 | 24.78 | 9.00 | 95.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.88 | 4.00 | 91.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 3.99 | 11.76 | 18.44 | 1.00 | 86.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.79 | 11.09 | 16.03 | 5.00 | 73.4 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.29 | 9.80 | 15.68 | 23.00 | 79.6 | 90.0 |
| Captain | Captain | Junior Kroupi | FWD | 4 | 4.5 | 7.29 | 16.40 | 23.29 | 12.00 | 96.6 | 136.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.50 | 13.21 | 22.02 | 2.00 | 77.7 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.3 | 3.13 | 9.54 | 14.64 | 2.00 | 66.1 | 65.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.83 | 19.28 | 30.00 | 3.00 | 94.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.44 | 17.17 | 30.93 | 6.00 | 61.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.94 | 14.23 | 22.62 | 4.00 | 84.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.43 | 13.34 | 20.53 | 3.00 | 76.1 | 77.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 3.33 | 10.78 | 17.92 | 1.00 | 60.6 | 75.0 |