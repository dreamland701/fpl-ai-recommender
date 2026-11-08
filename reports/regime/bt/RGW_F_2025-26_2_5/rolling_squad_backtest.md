# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 264.91
- Total actual points: 255.00
- Average predicted points: 66.23
- Average actual points: 63.75
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
- Predicted score: 72.85
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.25 | 11.11 | 18.01 | 1.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.09 | 0.37 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Daniel Ballard | DEF | 17 | 4.6 | 7.92 | 18.11 | 28.78 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.92 | 12.05 | 19.24 | 5.00 | 90.0 | 68.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.46 | 10.52 | 17.00 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 3.17 | 9.82 | 17.18 | -1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.92 | 8.49 | 14.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.42 | 19.49 | 32.76 | 2.00 | 72.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.82 | 18.73 | 31.14 | 9.00 | 90.0 | 79.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.61 | 6.91 | 10.49 | 2.00 | 15.7 | 4.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.52 | 22.84 | 38.48 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.79 | 19.65 | 30.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 15.97 | 24.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.28 | 15.38 | 25.61 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 3.93 | 13.15 | 22.29 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.42
- Actual score: 57.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 8.60 | 14.12 | 8.00 | 75.6 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.00 | 0.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.58 | 13.09 | 20.45 | 6.00 | 80.0 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.01 | 8.50 | 13.92 | 2.00 | 77.9 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.24 | 7.75 | 12.72 | 7.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 7.41 | 12.25 | 9.00 | 71.1 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.25 | 6.38 | 11.44 | 0.00 | 16.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.80 | 21.35 | 34.75 | 9.00 | 78.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.49 | 16.23 | 26.66 | 2.00 | 74.1 | 78.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.58 | 5.84 | 9.64 | 2.00 | 17.6 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.11 | 22.75 | 37.88 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.77 | 16.11 | 25.06 | 2.00 | 87.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.82 | 15.70 | 25.52 | 10.00 | 82.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.59 | 11.84 | 18.26 | 2.00 | 71.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.08 | 10.78 | 17.72 | 3.00 | 75.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.98
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.24) beats the best remaining Bench Boost opportunity (10.89).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 5.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.24) beats the best remaining Bench Boost opportunity (10.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.87 | 9.13 | 15.53 | 10.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.00 | 0.01 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.57 | 13.44 | 18.70 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.93 | 12.81 | 18.25 | 1.00 | 72.9 | 45.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.90 | 9.41 | 13.17 | 6.00 | 77.7 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 8.66 | 12.16 | 0.00 | 63.0 | 90.0 |
| Bench 3 | Bench Boost | Joe Rodon | DEF | 11 | 4.0 | 2.83 | 8.51 | 11.79 | 4.00 | 71.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.78 | 20.85 | 34.13 | 13.00 | 75.5 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.16 | 15.48 | 24.46 | 2.00 | 67.6 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.27 | 6.97 | 10.58 | 0.00 | 31.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.13 | 24.01 | 37.96 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.63 | 17.32 | 25.64 | 13.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.93 | 14.56 | 23.80 | 2.00 | 72.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.47 | 10.89 | 16.90 | 3.00 | 77.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.72 | 10.72 | 16.93 | 1.00 | 76.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.66
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Trai Hume -> Veljko Milosavljevic (projected gain 1.77, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.82) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Tijjani Reijnders replaced Veljko Milosavljevic.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.20 | 9.41 | 16.22 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.00 | 0.30 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.18 | 12.05 | 17.20 | 7.00 | 79.7 | 90.0 |
| XI | Bench | Veljko Milosavljevic | DEF | 4 | 4.5 | 4.45 | 11.14 | 15.08 | 0.00 | 81.9 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.44 | 10.79 | 16.45 | 0.00 | 61.6 | 63.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.93 | 10.04 | 13.82 | 2.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.89 | 8.27 | 12.17 | 4.00 | 68.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.36 | 21.53 | 37.00 | 9.00 | 85.1 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.27 | 10.87 | 19.51 | 8.00 | 47.2 | 66.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.86 | 4.18 | 7.38 | 0.00 | 16.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.44 | 22.39 | 36.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.86 | 17.49 | 27.30 | 5.00 | 85.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.14 | 14.18 | 23.19 | 10.00 | 78.0 | 86.0 |
| Bench 2 | Autosub In | Tijjani Reijnders | MID | 13 | 5.6 | 3.05 | 9.48 | 16.31 | 9.00 | 79.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.50 | 9.34 | 15.63 | 15.00 | 74.8 | 90.0 |