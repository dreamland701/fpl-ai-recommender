# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 244.78
- Total actual points: 259.00
- Average predicted points: 61.19
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
- Predicted score: 55.48
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Morgan Gibbs-White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.04 | 8.84 | 14.62 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.66 | 8.33 | 13.94 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.86 | 11.68 | 19.48 | 5.00 | 80.4 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 3.45 | 10.75 | 17.54 | 5.00 | 74.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.32 | 10.14 | 16.80 | 6.00 | 74.6 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 9.26 | 15.24 | 2.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 2.96 | 8.86 | 14.86 | 2.00 | 73.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 4.75 | 15.34 | 27.25 | 8.00 | 47.4 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 4.20 | 11.87 | 18.87 | 2.00 | 73.4 | 85.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.99 | 11.61 | 19.54 | 2.00 | 67.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.96 | 18.72 | 29.32 | 5.00 | 92.3 | 73.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.1 | 5.15 | 15.60 | 25.81 | 5.00 | 79.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 4.96 | 15.01 | 25.31 | 0.00 | 79.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.84 | 14.20 | 23.66 | 1.00 | 92.9 | 53.0 |
| Bench 2 | Autosub In | Morgan Gibbs-White | MID | 16 | 5.7 | 3.53 | 11.28 | 18.65 | 1.00 | 79.9 | 67.0 |

## GW33

- Train rows: 128527
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 56.30
- Actual score: 77.00
- Transfer: Morgan Gibbs-White -> Rodrigo Hernandez (projected gain 0.46, hit 0)
- Autosub outfielders: Rodrigo Muniz Carvalho, Antonee Robinson, Alfie Doughty.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.80 | 14.49 | 9.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.78 | 7.96 | 13.27 | 7.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 12.26 | 20.04 | 1.00 | 86.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.06 | 11.42 | 18.21 | 0.00 | 81.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.99 | 11.41 | 18.26 | 5.00 | 81.6 | 66.0 |
| Bench 3 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.12 | 8.97 | 14.70 | 6.00 | 79.0 | 90.0 |
| Bench 4 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.51 | 8.54 | 14.19 | 0.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.66 | 19.17 | 32.06 | 10.00 | 87.5 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.20 | 12.44 | 20.24 | 7.00 | 76.0 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.30 | 10.06 | 16.78 | 2.00 | 62.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.92 | 16.41 | 26.47 | 26.00 | 90.2 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.09 | 15.68 | 25.92 | 1.00 | 83.9 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.9 | 4.75 | 13.99 | 23.20 | 0.00 | 83.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.04 | 12.16 | 20.59 | 0.00 | 53.2 | 0.0 |
| XI | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 3.73 | 10.48 | 17.33 | 0.00 | 77.9 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.60 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.64
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.39) beats the best remaining Bench Boost opportunity (16.53).
- Transfer: Rodrigo Hernandez -> Morgan Gibbs-White (projected gain 1.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.39) beats the best remaining Bench Boost opportunity (16.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 9.50 | 15.65 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.78 | 8.20 | 13.51 | 2.00 | 79.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 5.34 | 13.14 | 20.81 | 14.00 | 112.4 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 5.08 | 12.20 | 18.94 | 12.00 | 108.7 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.87 | 12.11 | 19.22 | 26.00 | 100.4 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.08 | 9.24 | 15.03 | 1.00 | 79.4 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.87 | 8.06 | 13.18 | -1.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.71 | 19.65 | 32.37 | 0.00 | 85.7 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.95 | 13.10 | 21.21 | 8.00 | 107.2 | 176.0 |
| Bench 2 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.99 | 9.56 | 15.79 | 5.00 | 59.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.1 | 5.86 | 18.46 | 30.23 | 0.00 | 101.7 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.68 | 12.46 | 22.00 | 0.00 | 47.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 5.7 | 3.85 | 11.15 | 18.50 | 2.00 | 78.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 3.03 | 10.16 | 18.25 | 16.00 | 40.8 | 71.0 |
| Bench 4 | Bench Boost | Jarrod Bowen | MID | 19 | 7.8 | 2.78 | 9.80 | 17.44 | 0.00 | 42.0 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Benjamin White
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 65.36
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 7.37, hit 0)
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.16 | 9.06 | 15.02 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.7 | 2.73 | 7.84 | 12.89 | 2.00 | 78.2 | 90.0 |
| Vice Captain | XI | Benjamin White | DEF | 1 | 6.0 | 5.82 | 16.88 | 26.92 | 1.00 | 123.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 5.30 | 15.34 | 24.42 | 1.00 | 121.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 5.08 | 14.58 | 22.90 | 1.00 | 117.8 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 8.78 | 14.31 | 2.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.73 | 7.86 | 13.15 | 1.00 | 77.8 | 87.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 5.86 | 16.62 | 25.72 | 2.00 | 114.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 5.35 | 16.33 | 27.84 | 5.00 | 48.3 | 28.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 3.70 | 10.60 | 16.77 | 6.00 | 64.8 | 84.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.8 | 5.65 | 16.07 | 24.64 | 5.00 | 96.8 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.2 | 5.21 | 15.63 | 26.50 | 8.00 | 78.2 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.49 | 12.74 | 21.37 | 9.00 | 80.5 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.03 | 12.72 | 21.91 | 0.00 | 55.4 | 0.0 |
| Bench 3 | Bench | Morgan Gibbs-White | MID | 16 | 5.7 | 2.84 | 9.78 | 16.23 | 2.00 | 75.7 | 90.0 |