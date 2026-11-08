# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 191.70
- Total actual points: 260.00
- Average predicted points: 47.92
- Average actual points: 65.00
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Ollie Watkins
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 66.87
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.21) beats the best remaining Bench Boost opportunity (10.67).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.21) beats the best remaining Bench Boost opportunity (10.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.07 | 8.27 | 12.47 | 2.00 | 97.0 | 90.0 |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.8 | 2.66 | 7.67 | 11.86 | 11.00 | 86.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.01 | 8.95 | 14.18 | 5.00 | 95.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.51 | 8.94 | 14.20 | 2.00 | 84.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.16 | 8.93 | 14.38 | 1.00 | 77.4 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 2.68 | 8.57 | 14.00 | 2.00 | 85.6 | 90.0 |
| Bench 4 | Bench Boost | Fabian Schär | DEF | 15 | 5.4 | 2.62 | 7.98 | 12.30 | 1.00 | 82.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.13 | 18.16 | 28.84 | 2.00 | 98.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 6.50 | 15.60 | 23.18 | 8.00 | 111.7 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 3.93 | 8.85 | 13.88 | 4.00 | 95.3 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.08 | 16.13 | 27.95 | 2.00 | 69.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.51 | 14.68 | 23.50 | 2.00 | 87.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.83 | 12.73 | 20.40 | 2.00 | 96.2 | 90.0 |
| Bench 2 | Bench Boost | Kevin De Bruyne | MID | 13 | 10.6 | 2.89 | 10.94 | 18.34 | 6.00 | 35.4 | 68.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.80 | 9.74 | 15.71 | 13.00 | 73.8 | 85.0 |

## GW29

- Train rows: 125157
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 47.31
- Actual score: 13.00
- Transfer: Virgil van Dijk -> Pedro Porro (projected gain 3.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.25 | 7.08 | 11.97 | 3.00 | 76.5 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 1.46 | 5.68 | 9.91 | 0.00 | 48.7 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.41 | 12.46 | 18.61 | 1.00 | 103.5 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.66 | 10.86 | 15.36 | 1.00 | 103.4 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 2.38 | 7.79 | 13.68 | 0.00 | 51.5 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.04 | 7.19 | 11.83 | 0.00 | 44.3 | 0.0 |
| Bench 4 | Bench | Fabian Schär | DEF | 15 | 5.4 | 1.53 | 6.46 | 10.87 | 0.00 | 44.2 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.33 | 15.21 | 25.01 | 2.00 | 96.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.01 | 11.88 | 18.05 | 2.00 | 85.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 2.56 | 9.80 | 16.84 | 0.00 | 47.9 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 5.90 | 16.96 | 25.90 | 2.00 | 123.6 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 3.95 | 14.45 | 25.40 | 0.00 | 52.3 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.20 | 11.40 | 19.24 | 0.00 | 47.3 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 2.76 | 9.32 | 16.82 | 0.00 | 37.8 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 2.05 | 6.88 | 12.26 | 0.00 | 39.9 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Rodrigo Muniz Carvalho
- Vice captain: Cole Palmer
- Effective captain: Rodrigo Muniz Carvalho
- Chip used: none
- Predicted score: 29.25
- Actual score: 60.00
- Transfer: Carlton Morris -> Rodrigo Muniz Carvalho (projected gain 5.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 9.04 | 14.29 | 2.00 | 91.7 | 45.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 1.63 | 4.77 | 8.22 | 3.00 | 64.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 1.58 | 6.44 | 11.21 | 7.00 | 29.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.46 | 5.09 | 7.98 | 6.00 | 51.1 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.4 | 1.61 | 4.79 | 8.28 | 1.00 | 61.0 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.12 | 3.66 | 6.68 | 2.00 | 42.1 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.18 | 3.57 | 8.04 | 2.00 | 37.2 | 82.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 3.52 | 13.29 | 23.28 | 1.00 | 77.1 | 45.0 |
| Captain | Captain | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 3.84 | 9.10 | 13.88 | 6.00 | 70.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 1.93 | 7.34 | 12.94 | 7.00 | 20.9 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 1.90 | 10.57 | 18.39 | 3.00 | 14.6 | 77.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.7 | 3.75 | 10.32 | 16.55 | 15.00 | 79.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 1.81 | 10.13 | 16.35 | 3.00 | 20.7 | 60.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 0.63 | 6.72 | 13.16 | 10.00 | 36.2 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 1.13 | 6.01 | 11.42 | 3.00 | 15.7 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 1.40 -> 2.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 48.26
- Actual score: 116.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 1.29, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (4.99) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Fabian Schär replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.31 | 6.57 | 11.31 | 2.00 | 79.4 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 1.64 | 6.33 | 10.83 | 0.00 | 44.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.35 | 9.46 | 14.94 | 7.00 | 80.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.16 | 7.82 | 12.48 | 6.00 | 75.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 2.23 | 7.06 | 10.76 | 2.00 | 74.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 2.00 | 6.62 | 11.12 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Autosub In | Fabian Schär | DEF | 15 | 5.4 | 2.04 | 5.95 | 9.45 | 2.00 | 45.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.7 | 4.18 | 10.99 | 17.18 | 8.00 | 88.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.55 | 10.95 | 17.84 | 2.00 | 79.4 | 89.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 3.80 | 9.43 | 14.00 | 2.00 | 72.8 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 4.99 | 13.74 | 22.91 | 0.00 | 56.7 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | 7 | 5.8 | 4.39 | 11.98 | 18.41 | 20.00 | 71.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.32 | 10.73 | 19.14 | 5.00 | 85.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.00 | 10.45 | 16.89 | 20.00 | 42.4 | 79.0 |
| Bench 2 | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 2.89 | 9.89 | 16.50 | 0.00 | 41.1 | 0.0 |