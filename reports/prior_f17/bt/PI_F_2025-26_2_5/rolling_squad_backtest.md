# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.98
- Total actual points: 220.00
- Average predicted points: 65.99
- Average actual points: 55.00
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
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 72.00
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.22 | 10.69 | 17.34 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.60 | 0.84 | 1.26 | 0.00 | 10.0 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.28 | 17.27 | 27.31 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.57 | 11.94 | 18.98 | 5.00 | 89.9 | 68.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.46 | 10.84 | 18.09 | 5.00 | 89.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.48 | 16.64 | 3.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 9.14 | 15.74 | -1.00 | 81.8 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.68 | 18.49 | 30.52 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.49 | 14.20 | 23.15 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 3.98 | 6.11 | 9.21 | 2.00 | 28.7 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.85 | 23.41 | 39.28 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.86 | 20.01 | 31.26 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.72 | 17.65 | 29.21 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.96 | 16.28 | 25.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.38 | 15.52 | 25.78 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 3.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.33
- Actual score: 45.00
- Transfer: Cole Palmer -> Mohammed Kudus (projected gain 10.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.78 | 8.08 | 13.24 | 8.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.60 | 13.27 | 20.97 | 4.00 | 90.0 | 70.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.34 | 13.16 | 20.58 | 6.00 | 75.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.61 | 13.90 | 1.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.29 | 6.98 | 11.51 | 9.00 | 67.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.92 | 5.79 | 10.22 | 0.00 | 11.3 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.40 | 16.71 | 25.55 | 2.00 | 83.2 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.58 | 16.15 | 26.45 | 2.00 | 74.0 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.47 | 5.25 | 8.56 | 2.00 | 24.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.42 | 23.40 | 39.02 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.67 | 15.95 | 24.62 | 2.00 | 84.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.94 | 15.91 | 25.95 | 10.00 | 85.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.13 | 15.15 | 23.80 | 2.00 | 87.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.80 | 12.53 | 19.32 | 2.00 | 69.2 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 3.80 -> 3.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.93
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.81) beats the best remaining Bench Boost opportunity (8.30).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.81) beats the best remaining Bench Boost opportunity (8.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.79 | 9.37 | 14.77 | 10.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.88 | 12.22 | 18.82 | 1.00 | 69.7 | 45.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.81 | 10.88 | 16.77 | 6.00 | 66.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.85 | 8.10 | 12.47 | 6.00 | 73.9 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.25 | 7.12 | 11.06 | 0.00 | 59.2 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.94 | 3.88 | 6.69 | 0.00 | 10.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.41 | 16.54 | 25.08 | 7.00 | 80.0 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.33 | 16.08 | 24.97 | 2.00 | 68.8 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.14 | 6.73 | 9.60 | 0.00 | 37.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.47 | 24.55 | 39.13 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.64 | 17.42 | 25.57 | 13.00 | 80.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.07 | 14.86 | 24.18 | 2.00 | 75.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.07 | 12.56 | 19.38 | 3.00 | 68.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 11.74 | 18.32 | 3.00 | 75.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.70 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.71
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.12) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Daniel Muñoz Mejía (projected gain 3.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.12) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.13 | 9.45 | 15.51 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.49 | 12.54 | 19.08 | 2.00 | 75.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.23 | 12.08 | 18.97 | 1.00 | 81.4 | 88.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.31 | 10.26 | 16.90 | 0.00 | 59.6 | 63.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.55 | 7.03 | 11.27 | 4.00 | 66.1 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.89 | 3.04 | 5.11 | 1.00 | 6.6 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.33 | 15.72 | 25.10 | 2.00 | 79.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.54 | 12.04 | 20.29 | 8.00 | 47.8 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.17 | 4.69 | 6.92 | 0.00 | 22.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.74 | 23.16 | 37.93 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.89 | 18.09 | 27.50 | 5.00 | 82.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 14.90 | 23.70 | 10.00 | 79.9 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 3.92 | 11.87 | 19.46 | 7.00 | 74.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.33 | 10.70 | 17.79 | 9.00 | 77.2 | 90.0 |