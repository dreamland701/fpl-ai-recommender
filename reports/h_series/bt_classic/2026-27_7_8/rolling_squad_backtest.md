# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW6
- Simulated weeks: GW7-GW8
- Total predicted points: 156.16
- Total actual points: 129.00
- Average predicted points: 78.08
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
- Predicted score: 80.13
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.84) beats the best remaining Triple Captain opportunity (10.44).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.84) beats the best remaining Triple Captain opportunity (10.44).
- Autosub: Thomas replaced Cherki.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 3.98 | 11.78 | 19.34 | 9.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.00 | 0.01 | 0.25 | 0.00 | 3.5 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.33 | 14.75 | 23.50 | 6.00 | 90.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 5.28 | 14.39 | 22.31 | 6.00 | 83.3 | 90.0 |
| XI | XI | Van Hecke | DEF | 19 | 4.9 | 4.09 | 11.41 | 18.02 | 4.00 | 88.1 | 90.0 |
| Bench 2 | Autosub In | Thomas | DEF | 7 | 4.0 | 3.54 | 10.16 | 15.98 | 3.00 | 84.5 | 90.0 |
| Bench 3 | Bench | van Ewijk | DEF | 7 | 3.9 | 3.04 | 8.34 | 13.96 | 1.00 | 76.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 8.84 | 24.16 | 39.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.8 | 6.28 | 18.32 | 30.21 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Thomas-Asante | FWD | 7 | 5.0 | 2.88 | 8.09 | 12.47 | 5.00 | 66.7 | 77.0 |
| Vice Captain | Bench | Cherki | MID | 15 | 7.9 | 6.45 | 17.31 | 27.39 | 0.00 | 90.0 | 0.0 |
| XI | XI | Rogers | MID | 6 | 7.9 | 5.93 | 16.97 | 27.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 5.76 | 16.26 | 24.79 | 5.00 | 84.5 | 70.0 |
| XI | XI | Semenyo | MID | 15 | 8.3 | 5.55 | 15.20 | 25.66 | 1.00 | 90.0 | 13.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.94 | 14.04 | 23.38 | 9.00 | 90.0 | 90.0 |

## GW8

- Train rows: 195575
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: João Pedro
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 76.04
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Semenyo -> Mbeumo (projected gain 3.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.1 | 4.58 | 13.04 | 21.17 | 7.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Matthews | GK | 8 | 4.0 | 0.10 | 0.23 | 0.48 | 0.00 | 4.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.9 | 5.55 | 15.27 | 24.21 | 1.00 | 90.0 | 22.0 |
| XI | XI | De Cuyper | DEF | 5 | 5.2 | 4.28 | 13.42 | 21.19 | 1.00 | 79.3 | 90.0 |
| XI | XI | Thomas | DEF | 7 | 4.0 | 3.92 | 10.59 | 16.57 | 1.00 | 84.1 | 59.0 |
| Bench 2 | Bench Boost | Van Hecke | DEF | 19 | 4.9 | 3.46 | 10.49 | 16.98 | 7.00 | 83.2 | 90.0 |
| Bench 4 | Bench Boost | van Ewijk | DEF | 7 | 3.9 | 3.24 | 8.27 | 13.69 | 2.00 | 74.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.7 | 8.48 | 25.04 | 41.19 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.8 | 6.25 | 17.56 | 28.11 | 0.00 | 90.0 | 0.0 |
| Bench 3 | Bench Boost | Thomas-Asante | FWD | 7 | 5.0 | 3.28 | 8.78 | 13.31 | 2.00 | 70.4 | 66.0 |
| XI | XI | Rogers | MID | 6 | 7.9 | 6.18 | 17.19 | 26.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | Groß | MID | 5 | 6.1 | 4.55 | 15.19 | 24.37 | 0.00 | 79.5 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 7.9 | 5.17 | 14.34 | 23.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rice | MID | 1 | 7.3 | 4.96 | 14.05 | 23.36 | 3.00 | 90.0 | 79.0 |
| XI | XI | Cherki | MID | 15 | 7.9 | 3.56 | 11.28 | 18.38 | 0.00 | 38.4 | 45.0 |