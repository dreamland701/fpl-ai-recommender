# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW6
- Simulated weeks: GW7-GW8
- Total predicted points: 148.35
- Total actual points: 119.00
- Average predicted points: 74.18
- Average actual points: 59.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW6 are included before the first simulated week.
- League-average scores were not available for this run.

## GW7

- Train rows: 194907
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Haaland
- Vice captain: Cherki
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 75.87
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.26) beats the best remaining Triple Captain opportunity (9.75).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.26) beats the best remaining Triple Captain opportunity (9.75).
- Autosub: van Ewijk replaced Cherki.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 4.03 | 11.85 | 19.45 | 9.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.00 | 0.01 | 0.25 | 0.00 | 3.5 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 5.14 | 13.70 | 21.22 | 6.00 | 83.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.06 | 13.54 | 21.60 | 6.00 | 87.6 | 90.0 |
| XI | XI | Thomas | DEF | 7 | 4.0 | 3.49 | 9.90 | 15.80 | 3.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | van Ewijk | DEF | 7 | 3.9 | 3.04 | 8.34 | 13.96 | 1.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Davis | DEF | 12 | 4.0 | 2.56 | 8.25 | 13.62 | 0.00 | 75.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 8.26 | 22.75 | 37.50 | 13.00 | 85.8 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.8 | 5.97 | 17.13 | 28.45 | 2.00 | 88.0 | 90.0 |
| Bench 4 | Bench | Danns | FWD | 14 | 4.5 | 0.69 | 1.78 | 3.67 | 0.00 | 12.5 | 0.0 |
| XI | XI | Rogers | MID | 6 | 7.9 | 5.67 | 16.77 | 26.19 | 2.00 | 90.2 | 90.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 5.73 | 16.03 | 24.40 | 5.00 | 84.4 | 70.0 |
| XI | XI | Palmer | MID | 6 | 9.7 | 5.28 | 16.01 | 26.38 | 2.00 | 90.7 | 90.0 |
| Vice Captain | Bench | Cherki | MID | 15 | 7.9 | 6.02 | 15.70 | 24.51 | 0.00 | 86.4 | 0.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.69 | 13.16 | 22.04 | 9.00 | 88.7 | 90.0 |

## GW8

- Train rows: 195575
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: João Pedro
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.48
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cherki -> Mbeumo (projected gain 2.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 4.55 | 12.66 | 20.62 | 7.00 | 89.3 | 90.0 |
| Bench 1 | Bench Boost | Matthews | GK | 8 | 4.0 | 0.10 | 0.23 | 0.48 | 0.00 | 4.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.22 | 13.84 | 22.14 | 1.00 | 86.8 | 22.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 4.24 | 12.79 | 20.15 | 1.00 | 81.5 | 90.0 |
| XI | XI | Thomas | DEF | 7 | 4.0 | 3.81 | 10.33 | 16.32 | 1.00 | 85.1 | 59.0 |
| Bench 3 | Bench Boost | Davis | DEF | 12 | 4.0 | 3.06 | 8.59 | 13.75 | 2.00 | 80.7 | 90.0 |
| Bench 2 | Bench Boost | van Ewijk | DEF | 7 | 3.9 | 3.24 | 8.27 | 13.69 | 2.00 | 74.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 7.85 | 23.34 | 38.70 | 8.00 | 85.4 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.8 | 6.00 | 16.39 | 26.18 | 0.00 | 88.0 | 0.0 |
| Bench 4 | Bench Boost | Danns | FWD | 14 | 4.5 | 0.73 | 1.79 | 3.36 | 0.00 | 12.1 | 0.0 |
| XI | XI | Rogers | MID | 6 | 7.9 | 5.92 | 16.84 | 26.05 | 1.00 | 88.3 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.7 | 5.79 | 16.42 | 26.29 | -1.00 | 89.7 | 79.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 4.55 | 14.90 | 23.99 | 0.00 | 79.3 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 7.9 | 4.94 | 13.25 | 21.57 | 2.00 | 87.5 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.64 | 13.06 | 21.92 | 3.00 | 87.5 | 79.0 |