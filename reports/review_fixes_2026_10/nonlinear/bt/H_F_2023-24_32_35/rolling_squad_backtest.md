# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 286.68
- Total actual points: 277.00
- Average predicted points: 71.67
- Average actual points: 69.25
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
- Captain: Son Heung-min
- Vice captain: Mohamed Salah
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 61.52
- Actual score: 55.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.1 | 3.65 | 12.80 | 19.79 | 6.00 | 78.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 2.80 | 10.12 | 19.05 | 2.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.80 | 12.42 | 20.69 | 5.00 | 82.1 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.6 | 3.64 | 11.92 | 18.63 | 1.00 | 82.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.22 | 11.73 | 19.45 | 5.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Manuel Akanji | DEF | 13 | 4.9 | 3.58 | 9.88 | 16.31 | 1.00 | 78.7 | 45.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.71 | 9.61 | 15.95 | 4.00 | 80.6 | 54.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.69 | 15.96 | 23.02 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Chris Wood | FWD | 16 | 4.8 | 2.23 | 10.49 | 16.35 | 6.00 | 77.9 | 67.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 4.84 | 9.57 | 16.16 | 2.00 | 79.7 | 85.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 10.1 | 6.71 | 20.58 | 30.37 | 5.00 | 81.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.4 | 6.28 | 18.54 | 27.42 | 8.00 | 76.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 5.43 | 15.65 | 19.34 | 5.00 | 83.7 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.42 | 13.92 | 23.91 | 0.00 | 76.0 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.6 | 4.05 | 11.85 | 22.21 | 7.00 | 79.3 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.74
- Actual score: 53.00
- Transfer: Phil Foden -> Mohammed Kudus (projected gain 2.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.1 | 3.81 | 12.70 | 18.83 | 1.00 | 85.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.56 | 10.16 | 18.37 | 2.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.70 | 14.37 | 20.81 | 2.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.23 | 13.39 | 21.24 | 1.00 | 87.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.79 | 11.49 | 17.62 | 5.00 | 82.2 | 66.0 |
| XI | XI | Manuel Akanji | DEF | 13 | 4.9 | 3.39 | 10.15 | 15.54 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.28 | 9.29 | 14.55 | 0.00 | 71.5 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.86 | 13.16 | 19.96 | 7.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 4.8 | 3.26 | 8.92 | 16.10 | 2.00 | 69.5 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.11 | 8.24 | 13.91 | 2.00 | 66.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 7.43 | 20.27 | 24.85 | 2.00 | 81.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.27 | 17.04 | 29.50 | 1.00 | 78.1 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.6 | 5.49 | 15.49 | 23.00 | 2.00 | 84.1 | 65.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.76 | 13.37 | 20.91 | 26.00 | 78.7 | 79.0 |
| XI | XI | Mohammed Kudus | MID | 19 | 6.8 | 4.58 | 12.53 | 20.11 | 2.00 | 82.8 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 1.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Luis Díaz
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 98.11
- Actual score: 113.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.85) beats the best remaining Triple Captain opportunity (13.50).
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Rodrigo Muniz Carvalho -> Jean-Philippe Mateta (projected gain 5.75, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (15.85) beats the best remaining Triple Captain opportunity (13.50).
- Autosub: Chris Wood replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.1 | 7.55 | 15.16 | 24.08 | 16.00 | 166.5 | 180.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.9 | 3.69 | 11.45 | 19.06 | 1.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 7.83 | 15.54 | 22.15 | 14.00 | 158.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 6.87 | 15.10 | 21.33 | 2.00 | 156.6 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.30 | 14.51 | 20.25 | 26.00 | 132.3 | 180.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.7 | 4.00 | 7.94 | 8.46 | 2.00 | 95.5 | 105.0 |
| Bench 3 | Bench | Manuel Akanji | DEF | 13 | 4.9 | 1.98 | 7.28 | 9.07 | 6.00 | 63.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 8.11 | 18.67 | 24.52 | 8.00 | 161.1 | 176.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 5.0 | 6.42 | 14.81 | 18.99 | 29.00 | 157.5 | 157.0 |
| Bench 2 | Autosub In | Chris Wood | FWD | 16 | 4.8 | 3.37 | 9.23 | 15.76 | 2.00 | 64.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 10.61 | 19.37 | 29.86 | 3.00 | 138.0 | 106.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 9.51 | 15.40 | 24.11 | 3.00 | 129.9 | 163.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.54 | 12.09 | 17.52 | 0.00 | 68.6 | 0.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.69 | 11.51 | 21.07 | 0.00 | 0.7 | 0.0 |
| XI | XI | Mohammed Kudus | MID | 19 | 6.8 | 4.17 | 9.91 | 17.59 | 2.00 | 79.4 | 84.0 |

## GW35

- Train rows: 130234
- Bank: 1.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 68.31
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.27) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Mohammed Kudus -> Leon Bailey (projected gain 4.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.27) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.1 | 3.31 | 13.48 | 22.57 | 1.00 | 79.6 | 90.0 |
| XI | XI | André Onana | GK | 14 | 4.9 | 4.21 | 11.28 | 17.04 | 4.00 | 87.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.85 | 14.52 | 18.57 | 1.00 | 76.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.40 | 11.88 | 15.80 | 1.00 | 76.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.23 | 8.77 | 17.42 | 1.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.12 | 8.44 | 13.03 | 2.00 | 57.4 | 84.0 |
| XI | XI | Manuel Akanji | DEF | 13 | 4.9 | 3.24 | 7.25 | 11.24 | 8.00 | 71.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.38 | 13.97 | 22.99 | 2.00 | 66.6 | 90.0 |
| Bench 3 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 5.0 | 2.92 | 9.69 | 15.41 | 2.00 | 69.3 | 68.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 4.8 | 2.48 | 9.11 | 14.07 | 2.00 | 61.6 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.10 | 18.91 | 31.88 | 9.00 | 111.9 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 5.34 | 14.15 | 24.22 | 1.00 | 56.0 | 11.0 |
| XI | XI | Leon Bailey | MID | 2 | 5.5 | 3.91 | 13.25 | 21.02 | 1.00 | 76.9 | 74.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 7.13 | 12.82 | 18.16 | 8.00 | 131.2 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 3.55 | 12.23 | 21.51 | 5.00 | 66.5 | 78.0 |