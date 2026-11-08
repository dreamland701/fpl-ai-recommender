# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 240.73
- Total actual points: 251.00
- Average predicted points: 60.18
- Average actual points: 62.75
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
- Chip used: bench_boost
- Predicted score: 91.84
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.92) beats the best remaining Bench Boost opportunity (15.83).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.92) beats the best remaining Bench Boost opportunity (15.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 3.21 | 11.27 | 18.27 | 2.00 | 85.0 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 7.16 | 10.44 | 15.65 | 4.00 | 172.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.99 | 12.94 | 20.20 | 2.00 | 86.4 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.41 | 12.55 | 19.28 | 5.00 | 157.6 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.96 | 11.83 | 18.48 | 1.00 | 85.6 | 90.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.22 | 10.47 | 17.10 | 2.00 | 86.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.58 | 9.84 | 14.49 | 8.00 | 165.9 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.49 | 19.16 | 30.74 | 2.00 | 85.6 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 8.96 | 17.60 | 26.18 | 8.00 | 155.8 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 6.88 | 12.35 | 19.68 | 4.00 | 147.7 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.76 | 19.03 | 32.05 | 2.00 | 63.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.30 | 18.68 | 29.50 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.80 | 14.63 | 23.50 | 2.00 | 85.0 | 90.0 |
| Bench 2 | Bench Boost | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.27 | 12.73 | 20.79 | 11.00 | 83.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 8.4 | 4.91 | 11.42 | 18.76 | 8.00 | 74.9 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 1.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: James Maddison
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 31.19
- Actual score: 14.00
- Transfer: Marcus Rashford -> James Maddison (projected gain 6.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 0.31 | 9.60 | 16.16 | 0.00 | 2.8 | 0.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.73 | 8.98 | 15.07 | 3.00 | 77.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 3.12 | 16.46 | 24.61 | 1.00 | 84.2 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.14 | 11.29 | 18.78 | 0.00 | 1.4 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 0.14 | 10.19 | 16.83 | 0.00 | 0.7 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.46 | 15.37 | 0.00 | 1.5 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.00 | 8.96 | 15.52 | 0.00 | 1.4 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.63 | 17.81 | 28.91 | 2.00 | 85.3 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 3.78 | 14.68 | 22.05 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.49 | 13.80 | 22.84 | 0.00 | 1.2 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.27 | 18.45 | 31.40 | 0.00 | 1.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.48 | 18.26 | 27.90 | 2.00 | 87.2 | 90.0 |
| Vice Captain | XI | James Maddison | MID | 18 | 8.0 | 4.53 | 17.23 | 25.49 | 2.00 | 78.8 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.25 | 15.40 | 25.24 | 0.00 | 2.6 | 0.0 |
| Bench 4 | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 0.00 | 11.96 | 20.69 | 0.00 | 2.1 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.40 -> 3.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Virgil van Dijk
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 53.58
- Actual score: 58.00
- Transfer: James Maddison -> Cole Palmer (projected gain 5.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.51 | 10.54 | 17.19 | 2.00 | 87.3 | 45.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.75 | 5.71 | 9.86 | 2.00 | 75.7 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 11 | 6.4 | 5.30 | 8.36 | 13.83 | 1.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.14 | 7.74 | 13.21 | 7.00 | 81.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.83 | 6.09 | 10.38 | 6.00 | 71.5 | 90.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.31 | 5.84 | 9.70 | 2.00 | 69.2 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.45 | 4.97 | 10.04 | 2.00 | 42.5 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.24 | 15.59 | 26.38 | 1.00 | 74.6 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.84 | 8.64 | 15.24 | 7.00 | 55.5 | 84.0 |
| Bench 2 | Bench | Carlton Morris | FWD | 12 | 5.1 | 3.15 | 5.94 | 10.99 | 2.00 | 61.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 4.40 | 12.67 | 21.89 | 3.00 | 56.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.22 | 11.63 | 19.35 | 3.00 | 85.0 | 60.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 5.14 | 11.12 | 17.95 | 15.00 | 85.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.57 | 9.32 | 16.03 | 2.00 | 77.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.90 | 7.72 | 14.56 | 10.00 | 66.7 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 3.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Alexander Isak
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 64.12
- Actual score: 108.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Alexander Isak (projected gain 5.11, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.38) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Illia Zabarnyi replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.23 | 7.84 | 12.84 | 7.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 1.76 | 7.73 | 13.33 | 0.00 | 50.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.76 | 10.96 | 17.94 | 7.00 | 80.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.84 | 9.62 | 15.58 | 6.00 | 78.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 4.39 | 9.57 | 15.64 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.87 | 8.42 | 14.32 | 1.00 | 67.4 | 90.0 |
| Bench 2 | Autosub In | Illia Zabarnyi | DEF | 3 | 4.5 | 3.62 | 7.85 | 12.60 | 7.00 | 83.7 | 90.0 |
| Vice Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 5.31 | 12.79 | 19.78 | 8.00 | 80.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 5.26 | 12.65 | 20.14 | 2.00 | 82.3 | 89.0 |
| Bench 3 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.52 | 8.95 | 17.52 | 0.00 | 41.0 | 0.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.38 | 16.34 | 26.71 | 0.00 | 71.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.80 | 13.23 | 22.14 | 5.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.86 | 13.08 | 20.51 | 20.00 | 81.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.62 | 11.95 | 20.09 | 20.00 | 64.6 | 79.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.91 | 11.47 | 19.17 | 8.00 | 78.3 | 90.0 |