# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 253.55
- Total actual points: 298.00
- Average predicted points: 63.39
- Average actual points: 74.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.80
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Morgan Gibbs-White replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.00 | 8.76 | 14.52 | 3.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.76 | 8.56 | 14.31 | 1.00 | 90.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.17 | 12.37 | 20.53 | 5.00 | 83.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 3.74 | 11.28 | 18.30 | 5.00 | 76.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.63 | 10.80 | 17.86 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 9.12 | 15.09 | 2.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 3.03 | 8.98 | 15.22 | 2.00 | 73.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 4.48 | 14.37 | 25.98 | 8.00 | 41.9 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 4.41 | 12.32 | 19.67 | 2.00 | 78.9 | 85.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 11.76 | 19.84 | 2.00 | 66.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.90 | 18.90 | 29.88 | 5.00 | 99.4 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.1 | 5.37 | 15.64 | 26.39 | 0.00 | 82.5 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.27 | 15.51 | 25.53 | 5.00 | 78.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.99 | 14.49 | 24.16 | 1.00 | 94.3 | 53.0 |
| Bench 2 | Autosub In | Morgan Gibbs-White | MID | 16 | 5.7 | 3.79 | 11.56 | 19.15 | 1.00 | 82.9 | 67.0 |

## GW33

- Train rows: 128527
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.25
- Actual score: 93.00
- Transfer: Morgan Gibbs-White -> Rodrigo Hernandez (projected gain 0.21, hit 0)
- Autosub: Rodrigo Muniz Carvalho replaced Jarrod Bowen.
- Autosub: Antonee Robinson replaced Phil Foden.
- Autosub: Alfie Doughty replaced Rodrigo Hernandez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.81 | 14.52 | 9.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.68 | 7.82 | 13.14 | 7.00 | 80.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.42 | 12.68 | 20.66 | 1.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.24 | 11.92 | 18.95 | 0.00 | 85.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 4.11 | 11.73 | 18.82 | 5.00 | 83.4 | 66.0 |
| Bench 3 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 9.02 | 14.78 | 6.00 | 80.1 | 90.0 |
| Bench 4 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.61 | 8.62 | 14.51 | 0.00 | 78.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.25 | 18.09 | 30.20 | 10.00 | 80.1 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.20 | 12.25 | 20.07 | 7.00 | 76.7 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.63 | 10.72 | 17.79 | 2.00 | 68.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.64 | 18.63 | 28.93 | 26.00 | 95.5 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.08 | 15.43 | 25.35 | 1.00 | 81.7 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.9 | 4.77 | 13.82 | 22.84 | 0.00 | 84.6 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.10 | 12.31 | 20.79 | 0.00 | 53.2 | 0.0 |
| XI | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 3.87 | 10.91 | 17.89 | 0.00 | 79.7 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 70.98
- Actual score: 106.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.11) beats the best remaining Bench Boost opportunity (16.22).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 3.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.11) beats the best remaining Bench Boost opportunity (16.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.19 | 9.70 | 16.01 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.74 | 8.14 | 13.42 | 2.00 | 80.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.35 | 13.14 | 20.79 | 14.00 | 112.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.16 | 12.40 | 19.14 | 12.00 | 110.1 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 4.96 | 12.29 | 19.49 | 26.00 | 101.8 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.27 | 9.49 | 15.54 | 1.00 | 81.6 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.98 | 8.28 | 13.49 | -1.00 | 77.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.52 | 18.98 | 30.64 | 0.00 | 79.4 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.96 | 12.80 | 20.75 | 8.00 | 106.2 | 176.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.49 | 10.45 | 17.01 | 5.00 | 65.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.19 | 20.97 | 33.16 | 0.00 | 110.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 5.00 | 14.05 | 22.74 | 18.00 | 95.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.57 | 12.00 | 21.21 | 0.00 | 46.1 | 0.0 |
| Bench 2 | Bench Boost | Phil Foden | MID | 13 | 8.2 | 3.22 | 10.45 | 18.38 | 16.00 | 41.5 | 71.0 |
| Bench 4 | Bench Boost | Rodrigo Hernandez | MID | 13 | 5.6 | 2.20 | 7.13 | 12.22 | 3.00 | 42.6 | 78.0 |

## GW35

- Train rows: 130234
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Benjamin White
- Vice captain: Dominic Solanke
- Effective captain: Benjamin White
- Chip used: triple_captain
- Predicted score: 68.52
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.25) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 3.57, hit 0)
- Chip used: Triple Captain on Benjamin White. Optimizer chose Triple Captain here because the current estimated captain upside (9.25) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Antonee Robinson replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 4.52 | 12.63 | 19.94 | 10.00 | 122.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.20 | 9.08 | 15.06 | 3.00 | 85.6 | 90.0 |
| Captain | Captain | Benjamin White | DEF | 1 | 5.9 | 6.05 | 17.39 | 27.57 | 1.00 | 128.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.34 | 15.43 | 24.46 | 1.00 | 123.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.20 | 14.85 | 23.23 | 1.00 | 120.4 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.26 | 8.94 | 14.54 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.73 | 7.92 | 13.17 | 1.00 | 78.9 | 87.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 5.95 | 16.47 | 25.35 | 2.00 | 116.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 4.97 | 14.89 | 25.55 | 5.00 | 42.5 | 28.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 4.20 | 11.62 | 18.36 | 6.00 | 72.4 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 5.86 | 17.06 | 27.56 | 4.00 | 102.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 5.78 | 16.74 | 27.66 | 8.00 | 84.1 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.03 | 12.70 | 21.64 | 0.00 | 56.1 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.50 | 12.23 | 20.37 | 9.00 | 77.4 | 180.0 |
| Bench 3 | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 2.89 | 8.64 | 14.22 | 3.00 | 58.4 | 90.0 |