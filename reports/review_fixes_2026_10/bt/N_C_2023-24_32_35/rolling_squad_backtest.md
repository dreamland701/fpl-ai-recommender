# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 249.14
- Total actual points: 322.00
- Average predicted points: 62.29
- Average actual points: 80.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.27
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Bruno Borges Fernandes replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.91 | 8.42 | 13.86 | 3.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.56 | 8.10 | 13.66 | 1.00 | 88.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.16 | 11.82 | 19.30 | 5.00 | 85.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.70 | 10.80 | 17.31 | 5.00 | 76.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.62 | 10.29 | 16.71 | 6.00 | 79.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.64 | 9.66 | 15.21 | 11.00 | 76.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.08 | 9.39 | 15.51 | 1.00 | 70.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.63 | 12.98 | 19.72 | 2.00 | 73.6 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.1 | 3.99 | 11.90 | 19.33 | 1.00 | 84.2 | 9.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.33 | 9.49 | 15.08 | 2.00 | 60.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.40 | 17.07 | 26.46 | 5.00 | 92.4 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.99 | 16.66 | 27.44 | 0.00 | 95.6 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.73 | 16.45 | 26.81 | 5.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.06 | 14.37 | 23.76 | 1.00 | 97.2 | 53.0 |
| Bench 2 | Autosub In | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.61 | 11.32 | 19.42 | 9.00 | 73.4 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Luis Díaz
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 53.82
- Actual score: 99.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 4.26, hit 0)
- Autosub: Pedro Porro replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.83 | 8.44 | 13.80 | 9.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.72 | 7.84 | 13.07 | 7.00 | 80.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.46 | 12.22 | 19.63 | 1.00 | 90.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.20 | 11.24 | 17.55 | 0.00 | 84.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.96 | 11.16 | 17.73 | 5.00 | 81.0 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.86 | 10.49 | 16.79 | 2.00 | 81.6 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro | DEF | 18 | 5.9 | 3.04 | 9.28 | 14.96 | 0.00 | 72.8 | 48.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.55 | 13.21 | 20.03 | 12.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Ivan Toney | FWD | 4 | 8.1 | 3.42 | 10.07 | 16.71 | 0.00 | 55.0 | 0.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.74 | 8.22 | 13.62 | 2.00 | 54.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.04 | 16.52 | 25.13 | 26.00 | 87.7 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.76 | 14.90 | 24.67 | 1.00 | 77.5 | 57.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.32 | 14.32 | 22.55 | 2.00 | 86.4 | 65.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.34 | 12.60 | 20.95 | 15.00 | 85.7 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.48 | 11.03 | 18.81 | 0.00 | 64.9 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.50 -> 1.30
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 71.08
- Actual score: 102.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.07) beats the best remaining Bench Boost opportunity (16.62).
- Transfer: Ivan Toney -> Dominic Solanke (projected gain 6.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.07) beats the best remaining Bench Boost opportunity (16.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.96 | 14.80 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.6 | 2.55 | 7.59 | 12.54 | 2.00 | 77.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.58 | 13.49 | 21.02 | 14.00 | 119.1 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 5.36 | 12.64 | 19.18 | 12.00 | 115.5 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.22 | 12.48 | 19.38 | 26.00 | 108.3 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 5.26 | 12.16 | 18.62 | 2.00 | 115.1 | 180.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 1.89 | 7.17 | 12.54 | 0.00 | 44.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.25 | 14.66 | 23.18 | 2.00 | 85.1 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 5.99 | 14.54 | 22.85 | 8.00 | 121.8 | 176.0 |
| Bench 3 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.34 | 7.51 | 12.37 | 5.00 | 47.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.56 | 16.72 | 26.44 | 0.00 | 86.6 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.95 | 13.90 | 22.43 | 18.00 | 95.5 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.75 | 13.66 | 20.62 | 3.00 | 96.6 | 163.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.05 | 12.95 | 22.50 | 0.00 | 55.3 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.7 | 2.42 | 8.63 | 15.66 | 0.00 | 36.8 | 0.0 |

## GW35

- Train rows: 130234
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Alexander Isak
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.98
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.02) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mark Flekken -> Jordan Pickford (projected gain 2.81, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (10.02) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.99 | 11.32 | 18.08 | 10.00 | 114.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.05 | 8.53 | 14.07 | 3.00 | 82.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.21 | 15.35 | 24.42 | 1.00 | 116.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.00 | 14.55 | 23.05 | 1.00 | 119.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.80 | 13.77 | 21.44 | 1.00 | 115.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.05 | 11.76 | 18.49 | 1.00 | 102.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.78 | 7.14 | 11.75 | 2.00 | 70.0 | 180.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.0 | 6.21 | 16.84 | 26.24 | 13.00 | 97.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.85 | 13.91 | 21.94 | 2.00 | 99.3 | 90.0 |
| Bench 2 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.32 | 8.91 | 13.62 | 6.00 | 57.5 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.47 | 18.25 | 28.96 | 4.00 | 112.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 5.43 | 15.34 | 24.55 | 8.00 | 80.0 | 180.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.81 | 13.04 | 21.58 | 9.00 | 83.7 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.19 | 12.89 | 20.08 | 5.00 | 74.5 | 78.0 |
| Bench 4 | Bench | Jarrod Bowen | MID | 19 | 7.7 | 1.83 | 7.15 | 12.88 | 13.00 | 30.1 | 90.0 |