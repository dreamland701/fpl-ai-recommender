# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW6
- Simulated weeks: GW7-GW8
- Total predicted points: 153.49
- Total actual points: 129.00
- Average predicted points: 76.74
- Average actual points: 64.50
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
- Predicted score: 78.95
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.76) beats the best remaining Triple Captain opportunity (10.34).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.76) beats the best remaining Triple Captain opportunity (10.34).
- Autosub: Thomas replaced Cherki.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 3.99 | 11.92 | 19.87 | 9.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.00 | 0.01 | 0.25 | 0.00 | 3.5 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.19 | 14.50 | 23.09 | 6.00 | 90.2 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 5.17 | 14.03 | 22.20 | 6.00 | 84.4 | 90.0 |
| XI | XI | Van Hecke | DEF | 19 | 4.9 | 3.99 | 10.87 | 17.78 | 4.00 | 89.5 | 90.0 |
| Bench 2 | Autosub In | Thomas | DEF | 7 | 4.0 | 3.45 | 9.77 | 15.80 | 3.00 | 84.9 | 90.0 |
| Bench 3 | Bench | van Ewijk | DEF | 7 | 3.9 | 3.04 | 8.34 | 13.96 | 1.00 | 76.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 8.76 | 23.90 | 39.55 | 13.00 | 88.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.8 | 6.07 | 18.03 | 30.05 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Thomas-Asante | FWD | 7 | 5.0 | 2.88 | 8.09 | 12.47 | 5.00 | 66.7 | 77.0 |
| XI | XI | Rogers | MID | 6 | 7.9 | 5.98 | 17.01 | 27.12 | 2.00 | 92.0 | 90.0 |
| Vice Captain | Bench | Cherki | MID | 15 | 7.9 | 6.33 | 17.01 | 27.22 | 0.00 | 89.9 | 0.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 5.69 | 16.01 | 24.45 | 5.00 | 86.1 | 70.0 |
| XI | XI | Semenyo | MID | 15 | 8.3 | 5.40 | 14.49 | 25.02 | 1.00 | 88.7 | 13.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.84 | 13.83 | 23.29 | 9.00 | 89.3 | 90.0 |

## GW8

- Train rows: 195575
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 74.54
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Semenyo -> Mbeumo (projected gain 3.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 4.63 | 13.30 | 21.26 | 7.00 | 90.3 | 90.0 |
| Bench 1 | Bench Boost | Matthews | GK | 8 | 4.0 | 0.10 | 0.23 | 0.48 | 0.00 | 4.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.38 | 14.88 | 23.71 | 1.00 | 90.0 | 22.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 4.13 | 13.30 | 21.15 | 1.00 | 80.9 | 90.0 |
| XI | XI | Thomas | DEF | 7 | 4.0 | 3.80 | 10.28 | 16.39 | 1.00 | 85.4 | 59.0 |
| Bench 2 | Bench Boost | Van Hecke | DEF | 19 | 4.9 | 3.31 | 10.14 | 16.50 | 7.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | van Ewijk | DEF | 7 | 3.9 | 3.24 | 8.27 | 13.69 | 2.00 | 74.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 8.23 | 24.59 | 40.32 | 8.00 | 86.8 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.8 | 6.08 | 17.06 | 27.39 | 0.00 | 88.8 | 0.0 |
| Bench 3 | Bench Boost | Thomas-Asante | FWD | 7 | 5.0 | 3.28 | 8.78 | 13.31 | 2.00 | 70.4 | 66.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.9 | 6.24 | 17.16 | 26.34 | 1.00 | 90.3 | 90.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 4.50 | 14.78 | 23.92 | 0.00 | 80.5 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 7.9 | 5.07 | 14.06 | 23.11 | 2.00 | 89.4 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.96 | 13.87 | 23.41 | 3.00 | 89.3 | 79.0 |
| XI | XI | Cherki | MID | 15 | 7.9 | 3.37 | 10.82 | 18.08 | 0.00 | 38.8 | 45.0 |