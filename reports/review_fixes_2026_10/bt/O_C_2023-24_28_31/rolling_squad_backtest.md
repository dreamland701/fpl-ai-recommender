# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 244.18
- Total actual points: 219.00
- Average predicted points: 61.04
- Average actual points: 54.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 124319
- Bank: 100.00 -> 3.40
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 80.14
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.23) beats the best remaining Bench Boost opportunity (15.22).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.23) beats the best remaining Bench Boost opportunity (15.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.35 | 12.20 | 19.83 | 2.00 | 103.6 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 3.45 | 9.75 | 15.91 | 1.00 | 89.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.73 | 13.36 | 21.47 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.72 | 12.88 | 20.54 | 1.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Kieran Trippier | DEF | 15 | 6.9 | 3.73 | 11.83 | 19.69 | 0.00 | 75.8 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.91 | 11.50 | 18.32 | 5.00 | 105.4 | 180.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.45 | 10.69 | 17.89 | 2.00 | 86.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 7.30 | 20.65 | 33.30 | 2.00 | 106.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 5.85 | 13.94 | 21.04 | 8.00 | 101.2 | 180.0 |
| Bench 3 | Bench Boost | Julián Álvarez | FWD | 13 | 6.6 | 3.68 | 11.87 | 19.95 | 2.00 | 63.6 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.1 | 6.90 | 20.59 | 32.91 | 2.00 | 107.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.47 | 19.17 | 31.62 | 2.00 | 71.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.67 | 13.70 | 22.64 | 13.00 | 81.0 | 85.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.46 | 13.12 | 20.97 | 2.00 | 75.6 | 90.0 |
| XI | XI | Rodrigo Hernandez | MID | 13 | 5.6 | 4.16 | 12.92 | 21.16 | 1.00 | 100.0 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 3.40 -> 4.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 54.63
- Actual score: 10.00
- Transfer: Julián Álvarez -> Carlton Morris (projected gain 3.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.56 | 10.75 | 17.87 | 3.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.07 | 9.05 | 15.00 | 7.00 | 85.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.90 | 14.00 | 21.97 | 1.00 | 106.3 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.42 | 11.45 | 19.33 | 0.00 | 69.1 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.36 | 11.11 | 18.59 | 0.00 | 65.6 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.31 | 8.63 | 15.09 | 0.00 | 54.9 | 0.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 1.36 | 6.58 | 12.93 | 0.00 | 19.1 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.22 | 18.06 | 29.68 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.74 | 15.09 | 24.29 | 0.00 | 77.5 | 0.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.69 | 13.16 | 20.65 | 2.00 | 96.4 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.42 | 17.72 | 30.25 | 0.00 | 60.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.28 | 16.50 | 27.13 | 0.00 | 74.1 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.7 | 3.91 | 12.57 | 21.39 | 0.00 | 65.6 | 0.0 |
| XI | Bench | Luis Díaz | MID | 11 | 7.5 | 2.92 | 10.20 | 17.84 | 0.00 | 42.1 | 0.0 |
| Bench 2 | Bench | Rodrigo Hernandez | MID | 13 | 5.6 | 2.73 | 9.68 | 16.66 | 0.00 | 66.8 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 4.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 50.05
- Actual score: 53.00
- Transfer: Rodrigo Hernandez -> Son Heung-min (projected gain 7.48, hit 0)
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.32 | 10.38 | 17.69 | 2.00 | 92.4 | 45.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.50 | 10.10 | 16.41 | 1.00 | 89.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 3.59 | 12.23 | 19.00 | 2.00 | 84.9 | 82.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.69 | 9.06 | 15.66 | 7.00 | 55.5 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.8 | 2.74 | 8.07 | 13.97 | 0.00 | 40.6 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.38 | 8.01 | 13.61 | 6.00 | 51.2 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | 11 | 6.4 | 2.50 | 7.58 | 13.09 | 1.00 | 49.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.90 | 17.65 | 29.60 | 1.00 | 89.1 | 45.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.04 | 13.06 | 20.06 | 2.00 | 93.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.85 | 11.30 | 19.27 | 7.00 | 54.6 | 84.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.0 | 5.04 | 16.08 | 23.99 | 10.00 | 73.1 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 4.89 | 15.15 | 25.50 | 3.00 | 54.5 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.26 | 13.90 | 23.51 | 3.00 | 60.7 | 60.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.65 | 10.55 | 18.05 | 15.00 | 57.6 | 90.0 |
| Bench 2 | Bench | Luis Díaz | MID | 11 | 7.5 | 3.06 | 8.99 | 15.54 | 10.00 | 40.9 | 88.0 |

## GW31

- Train rows: 126837
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 59.36
- Actual score: 109.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.43) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Rodrigo Muniz Carvalho (projected gain 0.07, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.43) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Bernd Leno replaced Alphonse Areola.
- Autosub outfielders: Phil Foden, Alfie Doughty.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.28 | 10.13 | 16.61 | 0.00 | 76.9 | 0.0 |
| Bench 1 | Autosub In | Bernd Leno | GK | 10 | 4.8 | 3.13 | 9.15 | 15.22 | 1.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.13 | 11.52 | 19.25 | 7.00 | 79.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.67 | 10.10 | 16.73 | 6.00 | 72.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.36 | 9.40 | 15.26 | 2.00 | 69.5 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.79 | 8.56 | 15.95 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.87 | 5.65 | 10.86 | 0.00 | 23.7 | 0.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 9.0 | 4.55 | 14.88 | 25.78 | 0.00 | 72.4 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.81 | 12.89 | 21.51 | 2.00 | 78.3 | 89.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 4.70 | 12.78 | 20.08 | 2.00 | 78.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.8 | 5.43 | 15.39 | 24.61 | 20.00 | 83.0 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.1 | 5.35 | 15.14 | 25.68 | 0.00 | 65.1 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 4.96 | 14.12 | 24.83 | 2.00 | 74.4 | 90.0 |
| Bench 2 | Autosub In | Phil Foden | MID | 13 | 8.1 | 4.13 | 12.84 | 22.15 | 20.00 | 60.9 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.25 | 11.64 | 18.85 | 6.00 | 69.8 | 90.0 |