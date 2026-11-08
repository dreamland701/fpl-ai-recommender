# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 254.64
- Total actual points: 358.00
- Average predicted points: 63.66
- Average actual points: 89.50
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.77
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Bruno Borges Fernandes replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 8.76 | 14.28 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.59 | 8.07 | 13.57 | 1.00 | 87.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.96 | 11.38 | 18.63 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.50 | 10.45 | 16.79 | 5.00 | 74.9 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.42 | 9.88 | 16.08 | 6.00 | 76.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.55 | 9.54 | 14.94 | 11.00 | 74.8 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.13 | 9.51 | 15.65 | 1.00 | 72.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.63 | 13.25 | 19.90 | 2.00 | 74.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.41 | 11.79 | 19.75 | 2.00 | 72.3 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.68 | 10.01 | 15.74 | 2.00 | 63.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.44 | 17.89 | 27.58 | 5.00 | 96.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.67 | 16.23 | 26.69 | 0.00 | 92.3 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.43 | 16.22 | 26.36 | 5.00 | 84.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.99 | 14.28 | 23.54 | 1.00 | 96.1 | 53.0 |
| Bench 2 | Autosub In | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.50 | 11.38 | 19.43 | 9.00 | 74.0 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.80 -> 1.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Luis Díaz
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.41
- Actual score: 104.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 6.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.85 | 8.50 | 13.80 | 9.00 | 82.9 | 90.0 |
| XI | XI | Mark Flekken | GK | 4 | 4.6 | 2.92 | 8.16 | 13.46 | 7.00 | 81.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.51 | 12.28 | 19.63 | 1.00 | 89.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.28 | 11.30 | 17.60 | 0.00 | 84.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.06 | 11.21 | 17.75 | 5.00 | 79.6 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.80 | 10.42 | 16.55 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.9 | 2.98 | 9.20 | 14.79 | 0.00 | 72.3 | 48.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.08 | 19.91 | 12.00 | 76.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.84 | 11.30 | 18.58 | 7.00 | 68.9 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.78 | 8.34 | 13.66 | 2.00 | 54.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.10 | 16.33 | 25.13 | 26.00 | 89.7 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.65 | 14.80 | 24.43 | 1.00 | 76.4 | 57.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.37 | 14.34 | 22.46 | 2.00 | 85.4 | 65.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.36 | 12.57 | 20.97 | 15.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.48 | 11.11 | 18.74 | 0.00 | 63.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 71.90
- Actual score: 118.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.69) beats the best remaining Bench Boost opportunity (16.03).
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 1.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.69) beats the best remaining Bench Boost opportunity (16.03).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 4.21 | 9.97 | 15.26 | 18.00 | 115.3 | 180.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 2.89 | 8.84 | 14.68 | 2.00 | 85.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.51 | 13.31 | 20.75 | 14.00 | 117.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.30 | 12.48 | 18.95 | 12.00 | 113.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.14 | 12.29 | 19.11 | 26.00 | 106.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 5.25 | 12.10 | 18.61 | 2.00 | 115.0 | 180.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.90 | 7.18 | 12.57 | 0.00 | 44.3 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 6.05 | 14.79 | 23.27 | 8.00 | 124.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.11 | 14.58 | 23.02 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.21 | 7.47 | 12.25 | 5.00 | 46.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.80 | 16.02 | 25.24 | 0.00 | 84.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 5.33 | 14.36 | 23.18 | 18.00 | 97.4 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.73 | 13.61 | 20.63 | 3.00 | 97.0 | 163.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.05 | 12.94 | 22.47 | 0.00 | 55.3 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.7 | 2.36 | 8.53 | 15.53 | 0.00 | 35.6 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 1.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Bruno Borges Fernandes
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 70.56
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jarrod Bowen -> Phil Foden (projected gain 6.45, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (11.05) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Virgil van Dijk replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.72 | 10.85 | 17.45 | 10.00 | 112.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.00 | 8.37 | 13.91 | 3.00 | 81.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.09 | 14.89 | 23.73 | 1.00 | 111.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.86 | 14.13 | 22.41 | 1.00 | 115.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.67 | 13.35 | 20.83 | 1.00 | 111.5 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.6 | 4.03 | 11.61 | 18.34 | 1.00 | 101.8 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.46 | 6.61 | 10.97 | 2.00 | 66.0 | 180.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 8.0 | 7.50 | 17.26 | 27.30 | 13.00 | 104.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.69 | 13.64 | 21.45 | 2.00 | 94.9 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.18 | 8.76 | 13.42 | 6.00 | 55.9 | 84.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.12 | 17.42 | 28.05 | 4.00 | 111.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.25 | 14.97 | 24.19 | 8.00 | 79.4 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.3 | 4.87 | 14.06 | 22.85 | 0.00 | 70.2 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.48 | 12.85 | 20.13 | 5.00 | 75.0 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.30 | 12.55 | 20.76 | 9.00 | 77.8 | 180.0 |