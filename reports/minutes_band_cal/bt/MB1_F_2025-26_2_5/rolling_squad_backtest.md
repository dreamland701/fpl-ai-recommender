# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 242.92
- Total actual points: 242.00
- Average predicted points: 60.73
- Average actual points: 60.50
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
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.37
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Maxime Estève replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.40 | 8.72 | 14.61 | 0.00 | 82.7 | 0.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.63 | 15.47 | 24.96 | 1.00 | 82.7 | 8.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.13 | 10.41 | 16.71 | 1.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.71 | 9.19 | 15.74 | -1.00 | 80.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.48 | 8.63 | 14.20 | 3.00 | 80.7 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 2.96 | 7.12 | 11.38 | 6.00 | 84.9 | 82.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.27 | 18.95 | 31.51 | 2.00 | 80.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.93 | 16.33 | 27.56 | 9.00 | 82.7 | 79.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.82 | 7.48 | 12.22 | 2.00 | 70.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.95 | 20.82 | 35.63 | 5.00 | 82.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.18 | 18.09 | 28.72 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 5.98 | 15.55 | 26.33 | 0.00 | 82.7 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.30 | 14.37 | 22.70 | 6.00 | 82.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.18 | 10.93 | 18.91 | 2.00 | 82.7 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 52.92
- Actual score: 44.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.37 | 4.45 | 7.68 | 0.00 | 37.4 | 90.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.64 | 13.92 | 1.00 | 75.3 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.81 | 8.35 | 13.52 | 2.00 | 76.6 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 4.0 | 2.48 | 8.00 | 13.10 | 1.00 | 74.4 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.39 | 7.26 | 12.03 | 9.00 | 71.5 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.85 | 5.70 | 10.16 | 0.00 | 10.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.77 | 20.72 | 33.68 | 9.00 | 82.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.48 | 15.77 | 25.78 | 2.00 | 76.5 | 78.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.36 | 7.44 | 12.21 | 6.00 | 67.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.50 | 20.71 | 35.22 | 3.00 | 82.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.64 | 15.69 | 24.14 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.92 | 15.68 | 25.50 | 10.00 | 84.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.56 | 19.46 | 2.00 | 73.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.08 | 10.50 | 17.14 | 3.00 | 78.1 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.50
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.57) beats the best remaining Triple Captain opportunity (9.29).
- Transfer: Daniel Ballard -> Marc Cucurella Saseta (projected gain 4.79, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.57) beats the best remaining Triple Captain opportunity (9.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 2.17 | 6.87 | 10.43 | 0.00 | 70.1 | 0.0 |
| Bench 1 | Bench | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.00 | 0.17 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.92 | 12.32 | 19.05 | 1.00 | 73.4 | 45.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.68 | 8.33 | 12.84 | 6.00 | 77.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.89 | 8.14 | 12.51 | 6.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.65 | 7.61 | 11.70 | 4.00 | 75.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.42 | 7.60 | 11.80 | 0.00 | 63.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.70 | 20.48 | 32.90 | 13.00 | 80.9 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.27 | 15.87 | 24.71 | 2.00 | 73.0 | 71.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 8.63 | 13.24 | 2.00 | 74.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.55 | 21.81 | 35.28 | 9.00 | 82.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.62 | 17.13 | 25.03 | 13.00 | 80.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.03 | 14.64 | 23.76 | 2.00 | 77.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 11.67 | 18.17 | 3.00 | 77.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.77 | 10.48 | 16.33 | 1.00 | 78.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.13
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 0.91 | 3.25 | 5.60 | 0.00 | 31.4 | 0.0 |
| Bench 1 | Bench Boost | Odysseas Vlachodimos | GK | 15 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.46 | 10.65 | 17.47 | 0.00 | 63.4 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.42 | 8.89 | 13.59 | -2.00 | 79.8 | 32.0 |
| XI | XI | Maxime Estève | DEF | 3 | 4.0 | 3.54 | 8.77 | 13.30 | 4.00 | 80.8 | 90.0 |
| Bench 3 | Bench Boost | Trai Hume | DEF | 17 | 4.5 | 3.05 | 8.55 | 13.79 | 4.00 | 81.1 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.63 | 7.27 | 11.72 | 4.00 | 69.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.68 | 19.69 | 33.08 | 9.00 | 80.4 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.56 | 12.09 | 20.31 | 8.00 | 52.1 | 66.0 |
| Bench 2 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.09 | 8.41 | 13.38 | 6.00 | 75.2 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.84 | 20.46 | 34.06 | 5.00 | 82.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.88 | 17.85 | 26.98 | 5.00 | 81.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 14.67 | 23.21 | 10.00 | 79.3 | 86.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.34 | 10.64 | 17.64 | 9.00 | 79.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.60 | 9.47 | 15.12 | 15.00 | 77.5 | 90.0 |