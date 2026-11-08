# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.13
- Total actual points: 232.00
- Average predicted points: 65.78
- Average actual points: 58.00
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.24
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dúbravka replaced Marco Bizot.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.57 | 12.00 | 19.35 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Autosub In | Martin Dúbravka | GK | 3 | 4.0 | 3.72 | 9.47 | 15.31 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.99 | 16.33 | 25.84 | 1.00 | 90.0 | 8.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.64 | 11.30 | 18.82 | 5.00 | 89.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.37 | 16.47 | 3.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 9.00 | 15.48 | -1.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.45 | 7.91 | 13.43 | 2.00 | 86.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.93 | 19.15 | 31.57 | 9.00 | 90.0 | 79.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.23 | 18.90 | 31.50 | 2.00 | 77.9 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.03 | 6.13 | 9.23 | 2.00 | 21.5 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.33 | 21.93 | 36.95 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.78 | 19.79 | 30.97 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.45 | 16.86 | 27.96 | 0.00 | 90.0 | 0.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.77 | 15.15 | 24.89 | 3.00 | 90.0 | 85.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.11 | 13.56 | 22.64 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.20 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.18
- Actual score: 48.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 11.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.33 | 9.73 | 15.68 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.68 | 5.21 | 8.82 | 0.00 | 40.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.77 | 13.60 | 21.51 | 4.00 | 90.0 | 70.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.32 | 8.45 | 13.66 | 1.00 | 75.6 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 2.93 | 7.15 | 11.82 | 7.00 | 74.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.23 | 6.65 | 11.02 | 9.00 | 66.2 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.85 | 5.38 | 9.60 | 0.00 | 11.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.91 | 21.19 | 34.52 | 9.00 | 85.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.79 | 16.65 | 27.25 | 2.00 | 78.5 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.48 | 5.25 | 8.54 | 2.00 | 17.5 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.93 | 21.89 | 36.66 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.93 | 15.61 | 25.51 | 10.00 | 86.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.28 | 15.40 | 24.21 | 2.00 | 89.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.66 | 12.05 | 18.62 | 2.00 | 69.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.39 | 11.09 | 18.10 | 3.00 | 80.7 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.45
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.30) beats the best remaining Triple Captain opportunity (10.10).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 6.42, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.30) beats the best remaining Triple Captain opportunity (10.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.48 | 10.38 | 15.82 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.39 | 7.56 | 11.42 | 0.00 | 69.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.81 | 13.31 | 20.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.93 | 11.00 | 16.92 | 6.00 | 67.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.94 | 8.01 | 12.27 | 6.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.55 | 6.96 | 10.70 | 4.00 | 68.4 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.25 | 6.88 | 10.62 | 0.00 | 59.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.78 | 20.78 | 33.38 | 13.00 | 80.4 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.55 | 16.65 | 25.84 | 2.00 | 73.5 | 71.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 3.21 | 6.84 | 9.71 | 0.00 | 31.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.92 | 22.94 | 36.55 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.22 | 14.74 | 23.88 | 2.00 | 79.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.15 | 12.65 | 19.47 | 3.00 | 70.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.52 | 17.93 | 3.00 | 77.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.05 | 11.07 | 17.22 | 1.00 | 81.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.26
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.59) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Anton Stach -> Moisés Caicedo Corozo (projected gain 2.11, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.59) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.75 | 10.57 | 16.67 | 4.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 1.09 | 3.71 | 6.26 | 0.00 | 33.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.35 | 12.42 | 19.22 | 1.00 | 81.8 | 88.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.38 | 12.24 | 18.37 | 2.00 | 74.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.40 | 8.94 | 13.42 | -2.00 | 82.4 | 32.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.65 | 8.93 | 12.74 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.48 | 6.89 | 10.86 | 4.00 | 64.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.39 | 21.85 | 35.93 | 9.00 | 88.5 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.77 | 12.70 | 21.22 | 8.00 | 52.6 | 66.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 2.23 | 4.78 | 7.01 | 0.00 | 18.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.20 | 21.58 | 35.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.41 | 15.06 | 23.44 | 10.00 | 82.6 | 86.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.6 | 4.70 | 12.07 | 17.53 | 4.00 | 87.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.96 | 11.97 | 19.43 | 7.00 | 75.2 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.6 | 3.29 | 10.55 | 17.35 | 9.00 | 78.9 | 90.0 |