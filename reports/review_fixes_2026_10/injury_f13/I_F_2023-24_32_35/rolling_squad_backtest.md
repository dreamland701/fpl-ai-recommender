# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 254.54
- Total actual points: 332.00
- Average predicted points: 63.64
- Average actual points: 83.00
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
- Bank: 100.00 -> 1.20
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.21
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.07 | 8.71 | 14.16 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.59 | 8.11 | 13.64 | 1.00 | 86.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.96 | 11.35 | 18.56 | 5.00 | 83.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.50 | 10.49 | 16.86 | 5.00 | 74.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.55 | 9.59 | 15.05 | 11.00 | 74.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.13 | 9.49 | 15.59 | 1.00 | 72.1 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.96 | 8.76 | 14.75 | 2.00 | 71.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.62 | 13.24 | 19.90 | 2.00 | 74.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.42 | 11.79 | 19.71 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.69 | 10.05 | 15.79 | 2.00 | 62.8 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.44 | 17.90 | 27.60 | 5.00 | 96.4 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.45 | 16.22 | 26.34 | 5.00 | 84.9 | 90.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.68 | 16.22 | 26.66 | 0.00 | 92.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.01 | 14.26 | 23.47 | 1.00 | 96.0 | 53.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.07 | 12.39 | 20.69 | 3.00 | 74.8 | 88.0 |

## GW33

- Train rows: 128527
- Bank: 1.20 -> 1.70
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Luis Díaz
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 53.88
- Actual score: 92.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.23, hit 0)
- Autosub: Pedro Porro replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.85 | 8.45 | 13.68 | 9.00 | 82.9 | 90.0 |
| XI | XI | Mark Flekken | GK | 4 | 4.6 | 2.92 | 8.19 | 13.53 | 7.00 | 80.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.52 | 12.25 | 19.56 | 1.00 | 89.2 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.06 | 11.25 | 17.81 | 5.00 | 79.1 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.81 | 10.39 | 16.49 | 2.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | 18 | 5.9 | 2.98 | 9.25 | 14.89 | 0.00 | 71.8 | 48.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.37 | 7.91 | 13.18 | 0.00 | 73.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.41 | 13.06 | 19.89 | 12.00 | 76.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.86 | 11.31 | 18.54 | 7.00 | 68.8 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.79 | 8.38 | 13.73 | 2.00 | 53.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.10 | 16.34 | 25.14 | 26.00 | 89.8 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.67 | 14.80 | 24.40 | 1.00 | 76.4 | 57.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.39 | 14.35 | 22.42 | 2.00 | 85.3 | 65.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.54 | 12.90 | 20.90 | 3.00 | 78.5 | 78.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.51 | 11.10 | 18.67 | 0.00 | 63.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.70 -> 1.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 71.27
- Actual score: 109.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.39) beats the best remaining Bench Boost opportunity (17.06).
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 6.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.39) beats the best remaining Bench Boost opportunity (17.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.90 | 8.79 | 14.57 | 2.00 | 85.3 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.71 | 7.89 | 12.99 | 2.00 | 77.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.51 | 13.27 | 20.67 | 14.00 | 117.3 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.15 | 12.32 | 19.15 | 26.00 | 106.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 5.26 | 12.08 | 18.54 | 2.00 | 115.0 | 180.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.5 | 2.69 | 7.55 | 12.27 | -1.00 | 73.0 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.90 | 7.24 | 12.69 | 0.00 | 43.8 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 6.08 | 14.78 | 23.20 | 8.00 | 123.9 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.10 | 14.57 | 23.02 | 2.00 | 83.9 | 90.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.22 | 7.51 | 12.32 | 5.00 | 45.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 16.03 | 25.26 | 0.00 | 84.2 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.35 | 14.36 | 23.15 | 18.00 | 97.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.70 | 14.25 | 22.47 | 20.00 | 106.5 | 180.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.76 | 13.61 | 20.58 | 3.00 | 96.9 | 163.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.07 | 12.96 | 22.47 | 0.00 | 55.2 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 71.19
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.04) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 2.51, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (11.04) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.73 | 10.81 | 17.35 | 10.00 | 112.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.01 | 8.32 | 13.79 | 3.00 | 81.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.09 | 14.92 | 23.76 | 1.00 | 111.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 14.09 | 22.31 | 1.00 | 115.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.04 | 11.59 | 18.28 | 1.00 | 101.8 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.47 | 7.10 | 11.71 | 1.00 | 73.6 | 87.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.46 | 6.65 | 11.06 | 2.00 | 65.6 | 180.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 7.49 | 17.25 | 27.30 | 13.00 | 105.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.72 | 13.65 | 21.40 | 2.00 | 94.7 | 90.0 |
| Bench 2 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.19 | 8.83 | 13.55 | 6.00 | 55.5 | 84.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.03 | 17.55 | 28.08 | 2.00 | 112.8 | 88.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.15 | 17.43 | 28.03 | 4.00 | 111.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.26 | 14.98 | 24.20 | 8.00 | 79.4 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.51 | 12.86 | 20.10 | 5.00 | 74.8 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.32 | 12.56 | 20.73 | 9.00 | 77.8 | 180.0 |