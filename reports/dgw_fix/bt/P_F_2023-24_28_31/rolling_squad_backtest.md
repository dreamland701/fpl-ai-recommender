# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 254.15
- Total actual points: 221.00
- Average predicted points: 63.54
- Average actual points: 55.25
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
- Bank: 100.00 -> 2.80
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 101.81
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.21) beats the best remaining Triple Captain opportunity (8.86).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (16.21) beats the best remaining Triple Captain opportunity (8.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 4.30 | 11.60 | 19.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 6.81 | 9.02 | 14.16 | 4.00 | 173.1 | 180.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.46 | 14.22 | 20.25 | 5.00 | 168.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.83 | 8.69 | 16.54 | 2.00 | 83.0 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.46 | 8.30 | 12.80 | 8.00 | 166.7 | 180.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.44 | 7.78 | 14.81 | 1.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 3.15 | 6.92 | 13.75 | 2.00 | 82.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.02 | 30.97 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.96 | 14.91 | 22.76 | 8.00 | 180.0 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 8.22 | 13.87 | 20.22 | 4.00 | 159.5 | 180.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.26 | 14.36 | 23.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.71 | 12.87 | 26.11 | 2.00 | 66.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 11.98 | 22.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 6.75 | 11.89 | 17.78 | 9.00 | 155.2 | 177.0 |
| Bench 3 | Bench | Son Heung-min | MID | 18 | 9.8 | 3.78 | 11.72 | 18.41 | 17.00 | 58.4 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 2.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Ollie Watkins
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 48.49
- Actual score: 17.00
- Transfer: Illia Zabarnyi -> Pedro Porro (projected gain 5.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 9.14 | 15.55 | 3.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 0.00 | 7.41 | 14.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.67 | 15.14 | 22.88 | 1.00 | 90.0 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.37 | 11.59 | 17.64 | 1.00 | 82.1 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 8.90 | 17.71 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 0.00 | 8.01 | 15.83 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.00 | 7.29 | 14.94 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.33 | 17.66 | 29.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.92 | 13.40 | 20.13 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 9.91 | 19.35 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.9 | 7.15 | 19.84 | 29.86 | 2.00 | 90.0 | 86.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 6.18 | 17.47 | 27.18 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 13.82 | 28.03 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 11.19 | 22.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.85 | 10.48 | 16.78 | 2.00 | 90.0 | 90.0 |

## GW30

- Train rows: 125995
- Bank: 1.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Cole Palmer
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 40.47
- Actual score: 62.00
- Transfer: Ross Barkley -> Cole Palmer (projected gain 3.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.45 | 10.82 | 17.85 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 1.82 | 5.80 | 12.23 | 2.00 | 56.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.80 | 8.73 | 17.59 | 1.00 | 54.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.29 | 8.27 | 17.02 | 7.00 | 48.8 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.66 | 6.46 | 13.34 | 6.00 | 38.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 1.88 | 5.48 | 7.75 | 2.00 | 39.0 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.17 | 4.97 | 9.76 | 2.00 | 43.5 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.19 | 16.24 | 27.60 | 1.00 | 81.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.79 | 9.08 | 19.27 | 7.00 | 37.6 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.55 | 5.80 | 10.66 | 2.00 | 53.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.64 | 13.59 | 28.48 | 3.00 | 39.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.89 | 12.08 | 20.67 | 3.00 | 43.8 | 60.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.01 | 11.32 | 15.19 | 10.00 | 45.7 | 87.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.8 | 4.17 | 11.31 | 18.60 | 15.00 | 63.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.17 | 8.41 | 15.17 | 10.00 | 47.2 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.70 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Son Heung-min
- Effective captain: Son Heung-min
- Chip used: bench_boost
- Predicted score: 63.39
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlton Morris -> Rodrigo Muniz Carvalho (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 2.58 | 8.12 | 13.84 | 0.00 | 66.0 | 0.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.73 | 7.90 | 15.46 | 7.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.26 | 11.40 | 22.28 | 7.00 | 78.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.54 | 9.88 | 19.36 | 2.00 | 70.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.69 | 18.71 | 6.00 | 71.0 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.8 | 3.01 | 8.55 | 13.59 | 2.00 | 67.4 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.7 | 2.45 | 8.21 | 13.75 | 1.00 | 77.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.48 | 12.28 | 23.85 | 2.00 | 74.7 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.32 | 9.94 | 18.88 | 0.00 | 41.8 | 0.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.74 | 9.65 | 14.73 | 2.00 | 65.8 | 90.0 |
| Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.59 | 32.40 | 0.00 | 76.8 | 0.0 |
| Vice Captain | Captain | Son Heung-min | MID | 18 | 9.9 | 5.06 | 15.14 | 24.73 | 2.00 | 76.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.43 | 13.28 | 22.05 | 5.00 | 87.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.51 | 12.89 | 24.50 | 20.00 | 71.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.00 | 12.51 | 21.20 | 20.00 | 59.7 | 79.0 |