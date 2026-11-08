# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 244.78
- Total actual points: 259.00
- Average predicted points: 61.20
- Average actual points: 64.75
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
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 55.42
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Morgan Gibbs-White replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.02 | 8.79 | 14.57 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.69 | 8.37 | 14.01 | 1.00 | 89.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.88 | 11.68 | 19.43 | 5.00 | 80.3 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 3.48 | 10.78 | 17.54 | 5.00 | 74.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.34 | 10.14 | 16.80 | 6.00 | 74.6 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 9.13 | 15.05 | 2.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 2.99 | 8.95 | 15.15 | 2.00 | 73.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 4.76 | 15.26 | 27.40 | 8.00 | 47.4 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 4.18 | 11.71 | 18.56 | 2.00 | 73.5 | 85.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.99 | 11.54 | 19.59 | 2.00 | 67.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.94 | 18.52 | 28.94 | 5.00 | 92.3 | 73.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.1 | 5.12 | 15.37 | 25.46 | 5.00 | 79.7 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.97 | 14.90 | 25.27 | 0.00 | 79.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.80 | 14.03 | 23.50 | 1.00 | 93.0 | 53.0 |
| Bench 2 | Autosub In | Morgan Gibbs-White | MID | 16 | 5.7 | 3.50 | 11.00 | 18.27 | 1.00 | 80.0 | 67.0 |

## GW33

- Train rows: 128527
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 56.32
- Actual score: 77.00
- Transfer: Morgan Gibbs-White -> Rodrigo Hernandez (projected gain 0.62, hit 0)
- Autosub: Rodrigo Muniz Carvalho replaced Jarrod Bowen.
- Autosub: Antonee Robinson replaced Phil Foden.
- Autosub: Alfie Doughty replaced Rodrigo Hernandez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.90 | 8.73 | 14.39 | 9.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.76 | 7.91 | 13.24 | 7.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.31 | 12.32 | 20.07 | 1.00 | 86.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.09 | 11.46 | 18.19 | 0.00 | 81.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 4.03 | 11.45 | 18.35 | 5.00 | 81.5 | 66.0 |
| Bench 3 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.09 | 8.86 | 14.49 | 6.00 | 79.0 | 90.0 |
| Bench 4 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.50 | 8.40 | 14.11 | 0.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.65 | 19.11 | 31.91 | 10.00 | 87.5 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.19 | 12.24 | 20.00 | 7.00 | 76.0 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.26 | 9.80 | 16.25 | 2.00 | 62.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.9 | 5.93 | 16.44 | 25.83 | 26.00 | 90.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.07 | 15.54 | 25.58 | 1.00 | 84.0 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.9 | 4.76 | 13.87 | 22.83 | 0.00 | 83.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.04 | 12.10 | 20.49 | 0.00 | 53.2 | 0.0 |
| XI | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 3.72 | 10.46 | 17.19 | 0.00 | 77.9 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.69
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.42) beats the best remaining Bench Boost opportunity (16.50).
- Transfer: Rodrigo Hernandez -> Morgan Gibbs-White (projected gain 1.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.42) beats the best remaining Bench Boost opportunity (16.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 9.45 | 15.61 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.77 | 8.18 | 13.46 | 2.00 | 79.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.30 | 13.03 | 20.62 | 14.00 | 112.5 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.04 | 12.11 | 18.69 | 12.00 | 108.8 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 4.83 | 12.00 | 19.03 | 26.00 | 100.5 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.08 | 9.14 | 14.94 | 1.00 | 79.4 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.89 | 8.03 | 13.07 | -1.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.73 | 19.58 | 31.68 | 0.00 | 85.6 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.99 | 13.03 | 21.07 | 8.00 | 107.1 | 176.0 |
| Bench 2 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.98 | 9.34 | 15.17 | 5.00 | 59.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.89 | 18.03 | 28.71 | 0.00 | 101.7 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.69 | 12.29 | 21.68 | 0.00 | 47.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 5.7 | 3.86 | 11.00 | 18.01 | 2.00 | 78.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 3.05 | 10.10 | 17.85 | 16.00 | 40.7 | 71.0 |
| Bench 4 | Bench Boost | Jarrod Bowen | MID | 19 | 7.8 | 2.79 | 9.75 | 17.39 | 0.00 | 42.0 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Benjamin White
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 65.35
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.09) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 7.24, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (9.09) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Antonee Robinson replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.17 | 9.01 | 14.95 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.74 | 7.81 | 12.78 | 2.00 | 78.1 | 90.0 |
| Vice Captain | XI | Benjamin White | DEF | 1 | 5.9 | 5.79 | 16.70 | 26.43 | 1.00 | 123.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.27 | 15.21 | 24.12 | 1.00 | 121.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.05 | 14.46 | 22.58 | 1.00 | 117.9 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 8.74 | 14.19 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.68 | 7.80 | 12.94 | 1.00 | 77.9 | 87.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 5.89 | 16.57 | 25.33 | 2.00 | 114.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 5.33 | 16.19 | 27.43 | 5.00 | 48.4 | 28.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 3.71 | 10.53 | 16.48 | 6.00 | 64.8 | 84.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.8 | 5.61 | 15.90 | 24.06 | 5.00 | 96.8 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 5.24 | 15.43 | 25.63 | 8.00 | 78.2 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.52 | 12.73 | 21.09 | 9.00 | 80.5 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.00 | 12.70 | 21.60 | 0.00 | 55.4 | 0.0 |
| Bench 3 | Bench | Morgan Gibbs-White | MID | 16 | 5.7 | 2.83 | 9.70 | 15.87 | 2.00 | 75.7 | 90.0 |