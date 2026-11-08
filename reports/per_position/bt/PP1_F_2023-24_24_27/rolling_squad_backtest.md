# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 274.88
- Total actual points: 296.00
- Average predicted points: 68.72
- Average actual points: 74.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 57.44
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.5 | 3.19 | 11.88 | 20.02 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.00 | 0.00 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.57 | 13.64 | 21.46 | 4.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.89 | 10.62 | 17.31 | 2.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.45 | 10.43 | 16.49 | 12.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.29 | 6.40 | 10.01 | 3.00 | 64.6 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 1.90 | 6.38 | 9.95 | 1.00 | 74.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.35 | 18.45 | 30.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.58 | 16.33 | 26.33 | 13.00 | 75.2 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 4.11 | 13.42 | 23.19 | 6.00 | 69.7 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.64 | 16.61 | 26.73 | 3.00 | 86.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 4.87 | 15.99 | 26.28 | 15.00 | 73.8 | 66.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 5.01 | 14.25 | 23.42 | 2.00 | 86.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.44 | 13.47 | 21.29 | 10.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Jack Hinshelwood | MID | 5 | 4.5 | 2.50 | 7.11 | 12.14 | 0.00 | 66.8 | 0.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 102.38
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.02) beats the best remaining Triple Captain opportunity (8.24).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jordan Pickford -> James Trafford (projected gain 5.85, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (18.02) beats the best remaining Triple Captain opportunity (8.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | James Trafford | GK | 6 | 4.5 | 3.41 | 10.30 | 16.59 | 0.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 3.29 | 4.91 | 6.51 | 5.00 | 67.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 9.39 | 14.09 | 21.65 | 10.00 | 180.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.52 | 12.60 | 20.49 | 1.00 | 86.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.49 | 12.50 | 19.50 | 6.00 | 90.0 | 90.0 |
| XI | XI | Amari'i Bell | DEF | 12 | 3.9 | 3.29 | 6.63 | 10.40 | 1.00 | 133.3 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.11 | 5.65 | 9.61 | 6.00 | 72.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 13.42 | 19.91 | 31.73 | 10.00 | 175.8 | 180.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 9.81 | 18.80 | 29.34 | 5.00 | 180.0 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.61 | 15.69 | 26.14 | 13.00 | 85.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.36 | 18.34 | 29.58 | 15.00 | 81.6 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 12.19 | 18.04 | 27.38 | 5.00 | 159.0 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.02 | 11.41 | 19.46 | 2.00 | 67.4 | 70.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.61 | 9.41 | 17.48 | 2.00 | 64.5 | 70.0 |
| Bench 4 | Bench | Jack Hinshelwood | MID | 5 | 4.5 | 1.30 | 3.86 | 6.78 | 0.00 | 29.1 | 0.0 |

## GW26

- Train rows: 122659
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Erling Haaland
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 51.17
- Actual score: 48.00
- Transfer: James Trafford -> Mark Flekken (projected gain 3.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.28 | 11.47 | 20.48 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 7.19 | 11.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.65 | 13.43 | 20.65 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 0.00 | 12.35 | 20.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.65 | 12.28 | 19.33 | 0.00 | 90.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.82 | 7.96 | 12.14 | 1.00 | 71.7 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 0.00 | 6.54 | 11.75 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 7.11 | 20.38 | 32.89 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.29 | 18.26 | 29.56 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 0.00 | 12.59 | 21.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.79 | 22.00 | 32.78 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.97 | 18.85 | 29.99 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.97 | 18.93 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.26 | 18.07 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Jack Hinshelwood | MID | 5 | 4.5 | 0.82 | 2.55 | 4.53 | 0.00 | 21.4 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Erling Haaland
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 63.89
- Actual score: 88.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Douglas Luiz Soares de Paulo (projected gain 7.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.44 | 10.48 | 17.64 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.41 | 4.09 | 6.54 | 9.00 | 38.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.34 | 12.38 | 19.13 | 6.00 | 80.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.45 | 11.69 | 19.28 | 1.00 | 90.0 | 51.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.84 | 8.82 | 14.74 | 6.00 | 63.3 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.23 | 7.14 | 11.12 | 1.00 | 66.7 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 0.93 | 2.98 | 5.71 | 1.00 | 47.3 | 5.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 6.15 | 19.44 | 32.01 | 6.00 | 87.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.83 | 16.93 | 28.06 | 13.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 1.95 | 7.16 | 13.68 | 5.00 | 21.3 | 30.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 8.22 | 21.00 | 34.33 | 7.00 | 84.1 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.70 | 17.31 | 28.01 | 15.00 | 86.8 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.70 | 13.47 | 20.53 | 4.00 | 79.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.33 | 9.07 | 15.04 | 5.00 | 47.3 | 90.0 |
| Bench 4 | Bench Boost | Jack Hinshelwood | MID | 5 | 4.5 | 0.15 | 1.14 | 2.58 | 0.00 | 12.4 | 0.0 |