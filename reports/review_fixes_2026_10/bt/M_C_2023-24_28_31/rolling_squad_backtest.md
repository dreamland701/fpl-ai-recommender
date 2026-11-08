# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 245.71
- Total actual points: 217.00
- Average predicted points: 61.43
- Average actual points: 54.25
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
- Bank: 100.00 -> 1.20
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 80.30
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.19) beats the best remaining Bench Boost opportunity (15.14).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.19) beats the best remaining Bench Boost opportunity (15.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.37 | 12.31 | 20.16 | 2.00 | 103.6 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.8 | 3.41 | 9.74 | 15.98 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.76 | 13.46 | 21.48 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.75 | 12.99 | 20.73 | 1.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Kieran Trippier | DEF | 15 | 6.9 | 3.75 | 11.93 | 19.97 | 0.00 | 75.7 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.91 | 11.52 | 18.58 | 5.00 | 105.4 | 180.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.44 | 10.74 | 18.13 | 2.00 | 86.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 7.27 | 20.83 | 33.87 | 2.00 | 106.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 5.81 | 14.11 | 21.45 | 8.00 | 101.2 | 180.0 |
| Bench 3 | Bench Boost | Julián Álvarez | FWD | 13 | 6.6 | 3.68 | 11.89 | 19.94 | 2.00 | 63.6 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.1 | 6.89 | 20.74 | 33.18 | 2.00 | 107.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.50 | 19.25 | 32.19 | 2.00 | 71.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.65 | 13.70 | 22.79 | 13.00 | 81.0 | 85.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.44 | 13.30 | 21.45 | 2.00 | 75.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.38 | 12.87 | 21.26 | 2.00 | 85.5 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 1.20 -> 2.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 55.91
- Actual score: 12.00
- Transfer: Julián Álvarez -> Carlton Morris (projected gain 3.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.60 | 10.99 | 18.43 | 3.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 3.03 | 9.10 | 15.16 | 7.00 | 86.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.88 | 14.00 | 22.33 | 1.00 | 106.3 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.7 | 3.42 | 11.59 | 19.47 | 0.00 | 69.1 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.36 | 11.28 | 18.77 | 0.00 | 65.6 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.31 | 8.75 | 15.31 | 0.00 | 54.9 | 0.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 1.36 | 6.64 | 13.12 | 0.00 | 19.1 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 6.18 | 18.27 | 30.34 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.1 | 4.74 | 15.28 | 25.22 | 0.00 | 77.5 | 0.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.66 | 13.29 | 21.29 | 2.00 | 96.4 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.42 | 17.98 | 30.70 | 0.00 | 60.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 5.28 | 16.78 | 27.51 | 0.00 | 74.1 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.27 | 13.16 | 21.67 | 2.00 | 84.7 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.7 | 3.91 | 12.68 | 21.60 | 0.00 | 65.6 | 0.0 |
| Bench 2 | Bench | Luis Díaz | MID | 11 | 7.5 | 2.92 | 10.40 | 18.38 | 0.00 | 42.1 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 2.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 50.60
- Actual score: 48.00
- Transfer: Luis Díaz -> Son Heung-min (projected gain 5.26, hit 0)
- Autosub: Virgil van Dijk replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.30 | 10.55 | 18.03 | 2.00 | 92.4 | 45.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.47 | 10.14 | 16.59 | 1.00 | 89.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.55 | 12.17 | 19.14 | 2.00 | 84.9 | 82.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 2.68 | 9.15 | 15.71 | 7.00 | 55.5 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.8 | 2.70 | 8.17 | 14.12 | 0.00 | 40.6 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.37 | 8.09 | 13.69 | 6.00 | 51.2 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | 11 | 6.4 | 2.52 | 7.76 | 13.35 | 1.00 | 49.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 5.86 | 17.96 | 30.12 | 1.00 | 89.2 | 45.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.01 | 13.01 | 20.31 | 2.00 | 93.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.86 | 11.70 | 19.85 | 7.00 | 54.6 | 84.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.0 | 5.03 | 15.91 | 24.20 | 10.00 | 73.1 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 4.88 | 15.45 | 25.80 | 3.00 | 54.5 | 77.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.39 | 15.09 | 23.42 | 10.00 | 87.3 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.30 | 14.32 | 24.00 | 3.00 | 60.6 | 60.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.67 | 10.71 | 18.30 | 15.00 | 57.6 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bukayo Saka
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 58.89
- Actual score: 109.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.42) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Antoine Semenyo (projected gain 0.06, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.42) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Bernd Leno replaced Alphonse Areola.
- Autosub: Antoine Semenyo replaced Bukayo Saka.
- Autosub: Alfie Doughty replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.25 | 10.19 | 16.88 | 0.00 | 77.0 | 0.0 |
| Bench 1 | Autosub In | Bernd Leno | GK | 10 | 4.8 | 3.10 | 9.13 | 15.26 | 1.00 | 83.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.13 | 11.48 | 19.20 | 7.00 | 79.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.67 | 10.06 | 16.69 | 6.00 | 72.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 3.33 | 9.35 | 15.31 | 2.00 | 69.5 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.83 | 8.54 | 15.90 | 1.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.88 | 5.66 | 10.86 | 0.00 | 23.7 | 0.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.9 | 4.54 | 15.07 | 26.24 | 0.00 | 72.5 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.81 | 12.80 | 21.49 | 2.00 | 78.3 | 89.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 3.59 | 9.72 | 15.69 | 3.00 | 74.9 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.7 | 5.42 | 15.35 | 24.74 | 20.00 | 83.1 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.1 | 5.34 | 15.17 | 25.58 | 0.00 | 65.1 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.92 | 13.85 | 24.57 | 2.00 | 74.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.17 | 13.04 | 22.31 | 20.00 | 60.9 | 79.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.48 | 12.83 | 23.37 | 5.00 | 83.3 | 90.0 |