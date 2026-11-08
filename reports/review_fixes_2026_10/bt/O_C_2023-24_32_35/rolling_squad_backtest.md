# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 253.45
- Total actual points: 293.00
- Average predicted points: 63.36
- Average actual points: 73.25
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.87
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Morgan Gibbs-White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.02 | 8.81 | 14.57 | 3.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.72 | 8.51 | 14.22 | 1.00 | 90.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.15 | 12.36 | 20.56 | 5.00 | 83.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.8 | 3.72 | 11.24 | 18.29 | 5.00 | 76.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.61 | 10.79 | 17.84 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.6 | 3.36 | 9.34 | 14.79 | 4.00 | 69.1 | 54.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 9.25 | 15.28 | 2.00 | 82.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 4.47 | 14.42 | 25.82 | 8.00 | 41.9 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 4.43 | 12.48 | 19.97 | 2.00 | 78.9 | 85.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.95 | 11.85 | 19.78 | 2.00 | 66.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.9 | 6.93 | 19.17 | 30.33 | 5.00 | 99.3 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.29 | 15.70 | 25.81 | 5.00 | 78.3 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.1 | 5.36 | 15.69 | 26.35 | 0.00 | 82.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.03 | 14.64 | 24.28 | 1.00 | 94.3 | 53.0 |
| Bench 2 | Autosub In | Morgan Gibbs-White | MID | 16 | 5.7 | 3.83 | 11.80 | 19.47 | 1.00 | 82.8 | 67.0 |

## GW33

- Train rows: 128527
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.21
- Actual score: 85.00
- Transfer: Morgan Gibbs-White -> Rodrigo Hernandez (projected gain 0.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.96 | 8.88 | 14.62 | 9.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.71 | 7.87 | 13.16 | 7.00 | 80.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.39 | 12.61 | 20.62 | 1.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.21 | 11.87 | 18.96 | 0.00 | 85.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.07 | 11.68 | 18.71 | 5.00 | 83.4 | 66.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.31 | 9.43 | 14.83 | 0.00 | 66.3 | 0.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.6 | 3.18 | 9.12 | 14.96 | 6.00 | 80.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.26 | 18.17 | 30.38 | 10.00 | 80.1 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.22 | 12.43 | 20.29 | 7.00 | 76.7 | 90.0 |
| Bench 2 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.66 | 10.94 | 18.24 | 2.00 | 68.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.63 | 18.65 | 29.47 | 26.00 | 95.5 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.09 | 15.55 | 25.63 | 1.00 | 81.7 | 57.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.9 | 4.77 | 13.90 | 23.18 | 0.00 | 84.6 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.10 | 12.39 | 20.88 | 0.00 | 53.2 | 0.0 |
| XI | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 3.88 | 10.93 | 18.01 | 0.00 | 79.7 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 70.81
- Actual score: 109.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.38) beats the best remaining Bench Boost opportunity (15.28).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 4.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.38) beats the best remaining Bench Boost opportunity (15.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.19 | 9.74 | 16.03 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.74 | 8.16 | 13.47 | 2.00 | 80.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 5.39 | 13.25 | 20.97 | 14.00 | 112.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 5.19 | 12.48 | 19.36 | 12.00 | 110.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.00 | 12.40 | 19.66 | 26.00 | 101.7 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.27 | 9.58 | 15.60 | 1.00 | 81.6 | 90.0 |
| Bench 3 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.84 | 7.31 | 11.93 | 2.00 | 68.5 | 105.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.50 | 19.01 | 31.21 | 0.00 | 79.4 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.93 | 12.87 | 20.91 | 8.00 | 106.3 | 176.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.49 | 10.63 | 17.53 | 5.00 | 65.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 7.15 | 21.20 | 34.16 | 0.00 | 110.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 5.03 | 14.22 | 23.31 | 18.00 | 95.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.57 | 12.18 | 21.53 | 0.00 | 46.1 | 0.0 |
| Bench 2 | Bench Boost | Phil Foden | MID | 13 | 8.3 | 3.20 | 10.49 | 18.71 | 16.00 | 41.6 | 71.0 |
| Bench 4 | Bench Boost | Rodrigo Hernandez | MID | 13 | 5.6 | 2.17 | 7.15 | 12.48 | 3.00 | 42.6 | 78.0 |

## GW35

- Train rows: 130234
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Benjamin White
- Vice captain: Dominic Solanke
- Effective captain: Benjamin White
- Chip used: triple_captain
- Predicted score: 68.57
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 3.53, hit 0)
- Chip used: Triple Captain on Benjamin White. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 4.49 | 12.63 | 19.98 | 10.00 | 122.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.19 | 9.12 | 15.12 | 3.00 | 85.6 | 90.0 |
| Captain | Captain | Benjamin White | DEF | 1 | 6.0 | 6.09 | 17.57 | 28.03 | 1.00 | 128.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 5.37 | 15.55 | 24.76 | 1.00 | 123.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 5.23 | 14.97 | 23.54 | 1.00 | 120.4 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.12 | 9.12 | 15.06 | 2.00 | 68.6 | 84.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 3.24 | 8.98 | 14.64 | 2.00 | 79.8 | 90.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 5.92 | 16.56 | 25.80 | 2.00 | 116.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 5.00 | 15.08 | 26.05 | 5.00 | 42.5 | 28.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 4.19 | 11.67 | 18.60 | 6.00 | 72.5 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.84 | 17.23 | 28.12 | 4.00 | 102.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.2 | 5.74 | 16.86 | 28.37 | 8.00 | 84.2 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.06 | 12.73 | 21.96 | 0.00 | 56.1 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.46 | 12.24 | 20.63 | 9.00 | 77.4 | 180.0 |
| Bench 4 | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 2.91 | 8.68 | 14.47 | 3.00 | 58.4 | 90.0 |