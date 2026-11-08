# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 269.48
- Total actual points: 263.00
- Average predicted points: 67.37
- Average actual points: 65.75
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
- Predicted score: 72.87
- Actual score: 36.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Lyle Foster replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.48 | 11.09 | 17.85 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.70 | 0.92 | 1.37 | 0.00 | 13.1 | 0.0 |
| Captain | Captain | Daniel Ballard | DEF | 17 | 4.6 | 8.01 | 19.01 | 30.03 | 1.00 | 90.0 | 8.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.26 | 10.51 | 16.65 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.95 | 9.83 | 17.45 | -1.00 | 88.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.5 | 3.34 | 8.90 | 14.44 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.80 | 8.83 | 15.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.98 | 18.67 | 31.22 | 9.00 | 90.0 | 79.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.11 | 17.96 | 30.26 | 2.00 | 76.4 | 90.0 |
| Bench 2 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 2.99 | 7.63 | 12.43 | 2.00 | 70.1 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.62 | 22.66 | 38.18 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.25 | 20.48 | 32.45 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.59 | 17.11 | 28.17 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.06 | 15.57 | 23.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.16 | 13.37 | 22.93 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.52
- Actual score: 65.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.88 | 8.46 | 13.91 | 8.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.22 | 8.62 | 14.02 | 1.00 | 75.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.5 | 2.60 | 8.39 | 13.92 | 15.00 | 79.0 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.23 | 8.11 | 13.31 | 7.00 | 77.3 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.60 | 7.54 | 12.47 | 9.00 | 69.4 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.02 | 6.47 | 11.63 | 0.00 | 14.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.96 | 20.68 | 33.51 | 9.00 | 79.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.93 | 16.56 | 27.27 | 2.00 | 79.0 | 78.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.39 | 7.38 | 12.22 | 6.00 | 64.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.31 | 22.87 | 37.96 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.02 | 16.20 | 25.24 | 2.00 | 88.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.96 | 15.42 | 24.99 | 10.00 | 84.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.87 | 12.45 | 19.32 | 2.00 | 73.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.23 | 10.92 | 18.01 | 3.00 | 78.6 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 70.62
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.26) beats the best remaining Triple Captain opportunity (10.13).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 5.95, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.26) beats the best remaining Triple Captain opportunity (10.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.04 | 10.11 | 15.75 | 10.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.97 | 13.90 | 20.65 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.5 | 4.42 | 12.88 | 18.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.91 | 8.30 | 12.59 | 6.00 | 76.3 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.74 | 8.02 | 12.20 | 4.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.52 | 7.97 | 12.27 | 0.00 | 63.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.81 | 20.63 | 32.85 | 13.00 | 76.4 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.40 | 16.35 | 24.96 | 2.00 | 70.1 | 71.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.95 | 8.90 | 13.38 | 2.00 | 73.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.23 | 24.53 | 38.00 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.81 | 17.75 | 26.05 | 13.00 | 83.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.04 | 14.28 | 23.01 | 2.00 | 74.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.64 | 11.46 | 17.40 | 3.00 | 79.2 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.88 | 11.12 | 17.26 | 1.00 | 78.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.46
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Anton Stach -> Martín Zubimendi Ibáñez (projected gain 1.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.06) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.24 | 9.90 | 16.25 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alex Paulsen | GK | 4 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.45 | 12.57 | 18.78 | 2.00 | 76.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 3.94 | 11.55 | 17.44 | 7.00 | 78.1 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.83 | 9.90 | 14.53 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 3.28 | 8.78 | 13.47 | -2.00 | 82.2 | 32.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 7.73 | 12.41 | 4.00 | 67.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.47 | 21.83 | 35.90 | 9.00 | 86.1 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.67 | 12.20 | 20.15 | 8.00 | 51.2 | 66.0 |
| Bench 3 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.10 | 8.54 | 13.44 | 6.00 | 73.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.59 | 22.79 | 36.74 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.17 | 18.25 | 27.91 | 5.00 | 86.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.25 | 14.33 | 22.43 | 10.00 | 79.2 | 86.0 |
| XI | XI | Martín Zubimendi Ibáñez | MID | 1 | 5.4 | 3.95 | 11.68 | 18.64 | 2.00 | 85.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.28 | 10.03 | 16.59 | 9.00 | 81.6 | 90.0 |