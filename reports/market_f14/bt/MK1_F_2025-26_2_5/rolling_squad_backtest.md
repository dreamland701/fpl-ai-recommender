# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 254.97
- Total actual points: 216.00
- Average predicted points: 63.74
- Average actual points: 54.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Tijjani Reijnders
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 71.98
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.40 | 11.98 | 19.09 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.43 | 0.59 | 0.98 | 0.00 | 11.5 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.69 | 14.63 | 23.97 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.98 | 13.21 | 20.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.90 | 13.19 | 20.79 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 8.86 | 15.57 | -1.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.78 | 8.67 | 14.16 | 3.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.88 | 18.77 | 30.64 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.82 | 14.10 | 23.28 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.90 | 8.76 | 14.80 | 2.00 | 74.6 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.04 | 37.19 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.18 | 20.72 | 32.29 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.58 | 16.88 | 28.20 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.07 | 15.57 | 24.93 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.57 | 13.93 | 23.54 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.56
- Actual score: 32.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 2.82 | 8.65 | 14.63 | 2.00 | 82.5 | 90.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.11 | 0.39 | 0.70 | 0.00 | 5.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.29 | 9.32 | 15.60 | 1.00 | 76.1 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.78 | 9.02 | 15.13 | 2.00 | 74.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.05 | 7.92 | 12.95 | 1.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 7.39 | 12.08 | 9.00 | 65.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.20 | 6.24 | 11.11 | 0.00 | 22.7 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.60 | 16.12 | 26.23 | 2.00 | 74.8 | 78.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.20 | 15.37 | 24.11 | 2.00 | 90.0 | 72.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.49 | 7.26 | 12.30 | 2.00 | 50.5 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.86 | 21.79 | 36.63 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.93 | 16.05 | 25.73 | 10.00 | 82.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.60 | 15.67 | 24.52 | 2.00 | 87.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.01 | 14.59 | 23.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.56 | 11.98 | 18.74 | 2.00 | 71.3 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.24
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.18) beats the best remaining Bench Boost opportunity (7.31).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.18) beats the best remaining Bench Boost opportunity (7.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.06 | 12.42 | 18.67 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench Boost | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.34 | 1.18 | 0.68 | 0.00 | 5.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.15 | 12.61 | 18.88 | 9.00 | 83.1 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.85 | 8.82 | 13.23 | 0.00 | 69.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.62 | 7.60 | 11.39 | 6.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.39 | 7.58 | 12.09 | 0.00 | 34.3 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.22 | 4.74 | 7.64 | 0.00 | 18.4 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.52 | 16.80 | 25.36 | 7.00 | 84.3 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.89 | 24.05 | 2.00 | 69.1 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.19 | 7.51 | 11.62 | 0.00 | 52.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.97 | 23.45 | 36.97 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.38 | 16.96 | 24.84 | 13.00 | 85.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.66 | 14.25 | 23.32 | 2.00 | 74.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.96 | 12.40 | 18.89 | 3.00 | 69.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.72 | 11.93 | 18.17 | 3.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.20
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Virgil van Dijk (projected gain 5.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.32 | 10.50 | 16.58 | 2.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.04 | 0.84 | 1.06 | 0.00 | 5.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.62 | 12.75 | 19.45 | 4.00 | 79.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.98 | 11.50 | 17.91 | 2.00 | 81.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.18 | 8.24 | 12.71 | -2.00 | 81.0 | 32.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 7.18 | 11.28 | 4.00 | 64.9 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.16 | 3.76 | 6.05 | 1.00 | 15.0 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.18 | 15.35 | 24.91 | 2.00 | 83.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.42 | 11.80 | 19.34 | 8.00 | 43.7 | 66.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.38 | 4.56 | 7.57 | 1.00 | 26.9 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.31 | 21.95 | 35.65 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.67 | 17.39 | 26.71 | 5.00 | 84.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.99 | 14.19 | 22.80 | 10.00 | 77.4 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.70 | 11.41 | 18.91 | 7.00 | 75.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.21 | 10.38 | 17.28 | 9.00 | 77.2 | 90.0 |