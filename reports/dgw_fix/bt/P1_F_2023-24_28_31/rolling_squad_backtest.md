# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 240.28
- Total actual points: 225.00
- Average predicted points: 60.07
- Average actual points: 56.25
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
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 99.50
- Actual score: 56.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.86) beats the best remaining Triple Captain opportunity (8.86).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.86) beats the best remaining Triple Captain opportunity (8.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 4.30 | 11.27 | 18.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 6.81 | 10.44 | 15.65 | 4.00 | 173.1 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.83 | 12.94 | 20.20 | 2.00 | 83.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.46 | 12.55 | 19.28 | 5.00 | 168.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.44 | 11.83 | 18.48 | 1.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 3.15 | 10.47 | 17.10 | 2.00 | 82.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.46 | 9.84 | 14.49 | 8.00 | 166.7 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.16 | 30.74 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.96 | 17.60 | 26.18 | 8.00 | 180.0 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 8.22 | 12.35 | 19.68 | 4.00 | 159.5 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.71 | 19.03 | 32.05 | 2.00 | 66.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 18.68 | 29.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.26 | 14.63 | 23.50 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.32 | 12.73 | 20.79 | 11.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Marcus Rashford | MID | 14 | 8.4 | 4.05 | 11.42 | 18.76 | 8.00 | 74.6 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 1.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 38.22
- Actual score: 14.00
- Transfer: Marcus Rashford -> James Maddison (projected gain 7.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 0.00 | 9.60 | 16.16 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 8.98 | 15.07 | 3.00 | 79.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.67 | 16.46 | 24.61 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.29 | 18.78 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 0.00 | 10.19 | 16.83 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.46 | 15.37 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.00 | 8.96 | 15.52 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.33 | 17.81 | 28.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.92 | 14.68 | 22.05 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.80 | 22.84 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 18.45 | 31.40 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 6.18 | 18.26 | 27.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 8.0 | 5.91 | 17.23 | 25.49 | 2.00 | 90.0 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.40 | 25.24 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 0.00 | 11.96 | 20.69 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.40 -> 3.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Cole Palmer
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 39.80
- Actual score: 54.00
- Transfer: James Maddison -> Cole Palmer (projected gain 4.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.45 | 10.54 | 17.19 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 1.82 | 5.71 | 9.86 | 2.00 | 56.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.80 | 8.36 | 13.83 | 1.00 | 54.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.29 | 7.74 | 13.21 | 7.00 | 48.8 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.66 | 6.09 | 10.38 | 6.00 | 38.9 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 1.94 | 5.84 | 9.70 | 2.00 | 51.7 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.17 | 4.97 | 10.04 | 2.00 | 43.5 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.19 | 15.59 | 26.38 | 1.00 | 81.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.79 | 8.64 | 15.24 | 7.00 | 37.6 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.55 | 5.94 | 10.99 | 2.00 | 53.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.64 | 12.67 | 21.89 | 3.00 | 39.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.89 | 11.63 | 19.35 | 3.00 | 43.8 | 60.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.8 | 4.17 | 11.12 | 17.95 | 15.00 | 63.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.28 | 9.32 | 16.03 | 2.00 | 50.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.17 | 7.72 | 14.56 | 10.00 | 47.2 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 3.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Alexander Isak
- Effective captain: Alexander Isak
- Chip used: bench_boost
- Predicted score: 62.75
- Actual score: 101.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.12) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlton Morris -> Alexander Isak (projected gain 4.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.12) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.73 | 7.84 | 12.84 | 7.00 | 80.9 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 2.58 | 7.73 | 13.33 | 0.00 | 66.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.26 | 10.96 | 17.94 | 7.00 | 78.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.62 | 15.58 | 6.00 | 71.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.54 | 9.57 | 15.64 | 2.00 | 70.6 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.7 | 2.45 | 8.42 | 14.32 | 1.00 | 77.9 | 90.0 |
| Bench 2 | Bench Boost | Illia Zabarnyi | DEF | 3 | 4.5 | 2.76 | 7.85 | 12.60 | 7.00 | 75.7 | 90.0 |
| Vice Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 4.64 | 12.79 | 19.78 | 8.00 | 76.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.48 | 12.65 | 20.14 | 2.00 | 74.7 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.32 | 8.95 | 17.52 | 0.00 | 41.8 | 0.0 |
| Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.34 | 26.71 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.43 | 13.23 | 22.14 | 5.00 | 87.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.51 | 13.08 | 20.51 | 20.00 | 71.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.00 | 11.95 | 20.09 | 20.00 | 59.7 | 79.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.78 | 11.47 | 19.17 | 8.00 | 73.0 | 90.0 |