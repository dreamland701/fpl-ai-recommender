# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 261.36
- Total actual points: 235.00
- Average predicted points: 65.34
- Average actual points: 58.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Daniel Ballard
- Vice captain: Mohamed Salah
- Effective captain: Daniel Ballard
- Chip used: none
- Predicted score: 72.62
- Actual score: 34.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Lyle Foster replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.17 | 10.77 | 17.44 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.26 | 0.72 | 1.32 | 0.00 | 15.0 | 0.0 |
| Captain | Captain | Daniel Ballard | DEF | 17 | 4.6 | 7.75 | 18.41 | 29.27 | 1.00 | 90.0 | 8.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.22 | 10.62 | 17.17 | 1.00 | 86.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.24 | 10.62 | 16.92 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.85 | 9.64 | 16.86 | -1.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.70 | 8.65 | 14.86 | 2.00 | 89.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.87 | 18.68 | 31.05 | 9.00 | 90.0 | 79.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.23 | 18.60 | 31.18 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 2.89 | 7.48 | 12.19 | 2.00 | 69.0 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.58 | 22.68 | 38.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.10 | 20.36 | 32.10 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.58 | 17.26 | 28.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.07 | 15.93 | 24.53 | 6.00 | 90.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.06 | 13.25 | 22.49 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.26
- Actual score: 44.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.44 | 4.61 | 7.99 | 0.00 | 38.5 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.51 | 1.12 | 1.78 | 0.00 | 10.5 | 0.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.66 | 14.07 | 1.00 | 74.6 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.81 | 8.48 | 13.87 | 2.00 | 75.7 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.15 | 7.96 | 13.06 | 7.00 | 76.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.47 | 7.33 | 12.08 | 9.00 | 68.8 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.03 | 6.19 | 11.08 | 0.00 | 14.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.82 | 20.68 | 33.55 | 9.00 | 81.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.71 | 16.22 | 26.64 | 2.00 | 77.7 | 78.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.35 | 7.32 | 12.04 | 6.00 | 64.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.18 | 22.70 | 37.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.81 | 15.93 | 24.73 | 2.00 | 87.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.90 | 15.57 | 25.30 | 10.00 | 84.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.30 | 19.07 | 2.00 | 72.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.18 | 10.82 | 17.80 | 3.00 | 77.6 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.55
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (10.08).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 6.06, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.22) beats the best remaining Triple Captain opportunity (10.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 2.15 | 6.86 | 10.10 | 0.00 | 67.1 | 0.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 4.0 | 0.34 | 1.65 | 1.69 | 0.00 | 9.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.91 | 13.76 | 20.63 | 5.00 | 90.0 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.71 | 8.60 | 13.15 | 6.00 | 76.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.88 | 8.26 | 12.59 | 6.00 | 75.2 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.68 | 7.78 | 11.91 | 4.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.42 | 7.64 | 11.78 | 0.00 | 61.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.71 | 20.55 | 32.76 | 13.00 | 77.6 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.34 | 16.03 | 24.59 | 2.00 | 70.4 | 71.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 8.82 | 13.37 | 2.00 | 73.2 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.19 | 24.07 | 37.78 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.71 | 17.40 | 25.44 | 13.00 | 83.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.01 | 14.51 | 23.41 | 2.00 | 74.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.70 | 11.54 | 17.74 | 3.00 | 77.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.84 | 10.93 | 16.99 | 1.00 | 77.9 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.94
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trai Hume -> Micky van de Ven (projected gain 1.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.06 | 3.53 | 5.85 | 0.00 | 32.1 | 0.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 4.0 | 0.54 | 1.34 | 1.91 | 0.00 | 9.7 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.46 | 12.44 | 18.75 | 2.00 | 76.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.06 | 11.79 | 18.53 | 1.00 | 89.9 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.81 | 9.59 | 14.13 | 2.00 | 79.6 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.31 | 8.84 | 13.63 | -2.00 | 81.3 | 32.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 7.46 | 11.93 | 4.00 | 67.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.36 | 21.64 | 35.70 | 9.00 | 86.7 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.52 | 11.83 | 19.70 | 8.00 | 49.7 | 66.0 |
| Bench 3 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.08 | 8.49 | 13.46 | 6.00 | 73.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.49 | 22.52 | 36.53 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.98 | 17.92 | 27.29 | 5.00 | 85.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.24 | 14.49 | 22.89 | 10.00 | 79.4 | 86.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.6 | 3.28 | 10.26 | 17.04 | 9.00 | 79.5 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.62 | 9.75 | 15.68 | 15.00 | 76.1 | 90.0 |