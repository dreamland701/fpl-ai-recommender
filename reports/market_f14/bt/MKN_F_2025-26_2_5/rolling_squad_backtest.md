# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 253.41
- Total actual points: 231.00
- Average predicted points: 63.35
- Average actual points: 57.75
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
- Captain: Tijjani Reijnders
- Vice captain: Mohamed Salah
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 72.15
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Matty Cash replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 5.07 | 11.98 | 19.09 | 6.00 | 124.0 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.42 | 0.12 | 0.16 | 0.00 | 7.3 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 5.18 | 14.63 | 23.97 | 1.00 | 69.8 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 5.47 | 13.21 | 20.82 | 6.00 | 120.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 5.55 | 13.19 | 20.79 | 6.00 | 125.9 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 4.5 | 3.66 | 9.57 | 15.20 | 2.00 | 100.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.38 | 8.86 | 15.57 | -1.00 | 80.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 6.66 | 18.77 | 30.64 | 9.00 | 112.1 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.62 | 14.10 | 23.28 | 2.00 | 96.8 | 87.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.32 | 8.30 | 14.42 | 1.00 | 47.6 | 32.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.18 | 22.04 | 37.19 | 5.00 | 115.5 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 8.05 | 20.72 | 32.29 | 2.00 | 157.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 5.89 | 16.88 | 28.20 | 0.00 | 88.8 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.43 | 15.57 | 24.93 | 6.00 | 114.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.98 | 13.93 | 23.54 | 3.00 | 93.7 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.92
- Actual score: 38.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 7.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 2.40 | 8.65 | 14.63 | 2.00 | 71.6 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.22 | 0.29 | 0.55 | 0.00 | 5.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 2.89 | 9.32 | 15.60 | 1.00 | 65.6 | 4.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.35 | 9.02 | 15.13 | 2.00 | 63.7 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 3.44 | 8.87 | 14.11 | 0.00 | 77.5 | 73.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.57 | 7.39 | 12.08 | 9.00 | 69.6 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.70 | 6.24 | 11.11 | 0.00 | 10.7 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.10 | 16.12 | 26.23 | 2.00 | 84.9 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.57 | 15.37 | 24.11 | 2.00 | 75.9 | 72.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 2.14 | 6.53 | 10.95 | 2.00 | 39.4 | 69.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.65 | 21.79 | 36.63 | 3.00 | 103.9 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.49 | 16.05 | 25.73 | 10.00 | 92.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.84 | 15.67 | 24.52 | 2.00 | 91.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.87 | 14.59 | 23.26 | 2.00 | 88.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.46 | 11.98 | 18.74 | 2.00 | 66.5 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Hugo Ekitiké
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.83
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (7.08).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (7.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.30 | 12.42 | 18.67 | 6.00 | 95.9 | 90.0 |
| Bench 1 | Bench Boost | Alex Paulsen | GK | 4 | 4.0 | 0.11 | 1.05 | 0.50 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.46 | 12.61 | 18.88 | 9.00 | 90.7 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.87 | 8.82 | 13.23 | 0.00 | 69.1 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 2.97 | 8.61 | 12.81 | 5.00 | 69.2 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.34 | 7.58 | 12.09 | 0.00 | 34.2 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.10 | 4.74 | 7.64 | 0.00 | 16.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.18 | 16.80 | 25.36 | 7.00 | 75.9 | 78.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.51 | 15.89 | 24.05 | 2.00 | 71.8 | 71.0 |
| Bench 3 | Bench Boost | Lukas Nmecha | FWD | 11 | 5.0 | 2.29 | 7.80 | 11.63 | 1.00 | 48.4 | 21.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.89 | 23.45 | 36.97 | 9.00 | 103.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.43 | 16.96 | 24.84 | 13.00 | 83.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.11 | 14.25 | 23.32 | 2.00 | 65.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.64 | 12.40 | 18.89 | 3.00 | 62.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 11.93 | 18.17 | 3.00 | 75.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.50
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.31) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Virgil van Dijk (projected gain 5.68, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.31) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.18 | 10.50 | 16.58 | 2.00 | 78.5 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.14 | 0.60 | 0.62 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.95 | 12.75 | 19.45 | 4.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.88 | 11.50 | 17.91 | 2.00 | 78.7 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.5 | 3.62 | 9.58 | 14.78 | 10.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 7.18 | 11.28 | 4.00 | 63.6 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.02 | 3.76 | 6.05 | 1.00 | 13.7 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.47 | 15.35 | 24.91 | 2.00 | 68.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.61 | 11.80 | 19.34 | 8.00 | 47.9 | 66.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 1.98 | 6.04 | 9.96 | 1.00 | 35.8 | 1.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.28 | 21.95 | 35.65 | 5.00 | 100.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.68 | 17.39 | 26.71 | 5.00 | 83.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.89 | 14.19 | 22.80 | 10.00 | 76.5 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.38 | 11.41 | 18.91 | 7.00 | 68.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 2.99 | 10.38 | 17.28 | 9.00 | 71.2 | 90.0 |