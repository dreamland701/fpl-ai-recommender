# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2021-22 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2027.40
- Total actual points: 1926.00
- Average predicted points: 54.79
- Average actual points: 52.05
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 52897
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Miguel Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Miguel Borges Fernandes
- Chip used: none
- Predicted score: 59.61
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Aaron Cresswell replaced Trevoh Chalobah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.5 | 3.83 | 10.20 | 17.17 | 5.00 | 84.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 3.57 | 9.40 | 14.86 | 6.00 | 84.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.5 | 4.67 | 12.65 | 20.68 | 12.00 | 86.2 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.5 | 4.04 | 10.99 | 18.52 | 4.00 | 80.1 | 90.0 |
| XI | Bench | Trevoh Chalobah | DEF | 6 | 5.0 | 3.67 | 10.64 | 17.51 | 0.00 | 89.1 | 0.0 |
| Bench 2 | Autosub In | Aaron Cresswell | DEF | 19 | 5.5 | 3.63 | 10.50 | 17.18 | 2.00 | 87.1 | 90.0 |
| XI | XI | Ethan Pinnock | DEF | 3 | 4.5 | 3.93 | 10.16 | 16.26 | 6.00 | 87.5 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 16 | 6.0 | 3.39 | 9.71 | 15.27 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 3.28 | 8.79 | 13.62 | 2.00 | 49.5 | 90.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 5.0 | 1.86 | 5.94 | 10.16 | 1.00 | 51.0 | 11.0 |
| Captain | Captain | Bruno Miguel Borges Fernandes | MID | 13 | 12.1 | 7.76 | 22.41 | 36.63 | 1.00 | 122.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.6 | 7.19 | 20.11 | 33.14 | 3.00 | 104.5 | 90.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.6 | 4.84 | 14.35 | 22.49 | 4.00 | 92.8 | 90.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 4.58 | 11.72 | 18.30 | 8.00 | 72.7 | 74.0 |
| XI | XI | Sergi Canós | MID | 3 | 5.5 | 3.96 | 10.30 | 16.71 | 3.00 | 79.3 | 90.0 |

## GW3

- Train rows: 53463
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Miguel Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Miguel Borges Fernandes
- Chip used: none
- Predicted score: 54.86
- Actual score: 47.00
- Transfer: Trevoh Chalobah -> Shane Duffy (projected gain 1.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez | GK | 2 | 5.5 | 3.72 | 10.52 | 17.68 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 3.39 | 9.34 | 14.71 | 3.00 | 85.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.5 | 4.37 | 12.98 | 21.29 | 4.00 | 87.1 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.79 | 10.50 | 16.93 | 5.00 | 82.6 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.5 | 3.72 | 10.46 | 17.86 | 6.00 | 76.6 | 90.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.1 | 3.80 | 10.03 | 14.72 | 1.00 | 82.2 | 90.0 |
| XI | XI | Ethan Pinnock | DEF | 3 | 4.5 | 3.46 | 9.45 | 15.02 | 2.00 | 82.7 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 16 | 6.0 | 3.52 | 9.74 | 15.08 | 5.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 3.07 | 9.08 | 13.97 | 1.00 | 64.3 | 90.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 5.0 | 0.84 | 4.09 | 7.00 | 0.00 | 30.5 | 0.0 |
| Captain | Captain | Bruno Miguel Borges Fernandes | MID | 13 | 12.1 | 6.61 | 19.89 | 32.65 | 2.00 | 98.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.6 | 5.97 | 17.77 | 29.55 | 10.00 | 85.2 | 90.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.6 | 4.76 | 14.28 | 21.65 | 2.00 | 72.4 | 90.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 4.52 | 13.23 | 20.71 | 6.00 | 70.8 | 90.0 |
| Bench 2 | Bench | Sergi Canós | MID | 3 | 5.5 | 3.19 | 9.07 | 14.76 | 2.00 | 75.8 | 90.0 |

## GW4

- Train rows: 54040
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.81
- Actual score: 66.00
- Transfer: Sergi Canós -> Saïd Benrahma (projected gain 5.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 3 | 4.5 | 3.81 | 10.62 | 16.52 | 2.00 | 95.1 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez | GK | 2 | 5.5 | 1.53 | 5.51 | 10.81 | 0.00 | 57.7 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 7.5 | 5.02 | 13.44 | 21.72 | 12.00 | 80.9 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.5 | 3.94 | 10.56 | 17.79 | 5.00 | 73.7 | 90.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.1 | 3.68 | 10.10 | 15.33 | 5.00 | 75.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 5.5 | 3.22 | 9.59 | 15.72 | 8.00 | 75.9 | 90.0 |
| Bench 3 | Bench | Ethan Pinnock | DEF | 3 | 4.5 | 3.05 | 8.43 | 13.50 | 2.00 | 76.8 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.1 | 3.55 | 9.45 | 14.60 | 1.00 | 66.9 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 16 | 6.0 | 3.35 | 9.32 | 14.35 | 2.00 | 70.2 | 73.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 5.0 | 0.98 | 2.84 | 4.60 | 0.00 | 17.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 7.36 | 20.54 | 33.44 | 8.00 | 98.3 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 4.92 | 14.71 | 22.02 | 3.00 | 64.1 | 62.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 12.0 | 4.78 | 13.81 | 24.55 | 8.00 | 62.7 | 84.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 4.47 | 12.80 | 20.33 | 3.00 | 69.8 | 90.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.6 | 4.58 | 12.70 | 20.11 | 9.00 | 70.6 | 90.0 |

## GW5

- Train rows: 54639
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.60
- Actual score: 64.00
- Transfer: Emiliano Martínez -> Robert Sánchez (projected gain 1.89, hit 0)
- Autosub: Ethan Pinnock replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.97 | 11.33 | 17.51 | 1.00 | 82.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 2.99 | 9.50 | 14.78 | 6.00 | 76.4 | 90.0 |
| Vice Captain | Bench | Trent Alexander-Arnold | DEF | 11 | 7.5 | 5.22 | 14.47 | 23.21 | 0.00 | 81.5 | 0.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.5 | 3.89 | 11.52 | 19.42 | 2.00 | 74.6 | 90.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.1 | 3.85 | 10.94 | 16.51 | 5.00 | 73.4 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.13 | 9.32 | 15.29 | 1.00 | 75.3 | 90.0 |
| Bench 2 | Autosub In | Ethan Pinnock | DEF | 3 | 4.5 | 2.87 | 8.58 | 13.51 | 8.00 | 80.9 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.1 | 3.24 | 9.16 | 13.58 | 6.00 | 61.8 | 72.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 16 | 6.0 | 2.41 | 8.14 | 12.84 | 2.00 | 63.1 | 90.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 4.9 | 0.83 | 2.13 | 3.19 | 0.00 | 15.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.5 | 7.26 | 20.86 | 33.17 | 12.00 | 96.5 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 12.0 | 4.46 | 15.48 | 27.62 | 2.00 | 66.2 | 90.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.7 | 4.66 | 14.34 | 22.84 | 2.00 | 87.8 | 72.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 4.50 | 12.73 | 20.55 | 3.00 | 67.3 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 3.17 | 10.63 | 17.23 | 10.00 | 44.5 | 87.0 |

## GW6

- Train rows: 55245
- Bank: 1.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.03
- Actual score: 37.00
- Transfer: Adam Armstrong -> Allan Saint-Maximin (projected gain 3.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.77 | 10.35 | 16.27 | 2.00 | 86.9 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 2.85 | 9.23 | 14.62 | 2.00 | 86.6 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.5 | 4.57 | 12.25 | 19.99 | 0.00 | 83.5 | 33.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.2 | 3.95 | 11.04 | 16.30 | 2.00 | 80.9 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.67 | 9.51 | 15.41 | 2.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 7.5 | 3.04 | 9.36 | 15.38 | 1.00 | 38.9 | 90.0 |
| Bench 3 | Bench | Ethan Pinnock | DEF | 3 | 4.5 | 2.63 | 8.59 | 13.57 | 7.00 | 83.0 | 42.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 4.61 | 13.06 | 20.29 | 8.00 | 86.7 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.2 | 3.32 | 9.16 | 13.78 | 1.00 | 64.1 | 74.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 4.9 | 0.60 | 1.58 | 2.41 | 0.00 | 13.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.6 | 7.72 | 22.40 | 35.92 | 7.00 | 108.5 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.9 | 5.42 | 16.24 | 27.47 | 0.00 | 82.1 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 5.19 | 14.03 | 21.99 | 3.00 | 89.2 | 90.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.7 | 4.20 | 12.75 | 20.14 | 2.00 | 70.2 | 90.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 3.88 | 12.05 | 19.36 | 3.00 | 73.5 | 86.0 |

## GW7

- Train rows: 55856
- Bank: 0.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.14
- Actual score: 54.00
- Transfer: Trent Alexander-Arnold -> Marcos Alonso (projected gain 6.67, hit 0)
- Autosub: Ethan Pinnock replaced Marcos Alonso.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.14 | 9.05 | 14.70 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 2.86 | 8.62 | 13.87 | 3.00 | 85.1 | 90.0 |
| XI | Bench | Marcos Alonso | DEF | 6 | 6.0 | 5.34 | 14.13 | 21.50 | 0.00 | 100.4 | 0.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.2 | 3.53 | 10.23 | 15.83 | 6.00 | 83.8 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.73 | 9.77 | 15.60 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Autosub In | Ethan Pinnock | DEF | 3 | 4.5 | 2.54 | 7.52 | 12.51 | 2.00 | 70.0 | 90.0 |
| Bench 3 | Bench | Luke Shaw | DEF | 13 | 5.4 | 2.17 | 6.51 | 11.90 | 2.00 | 37.9 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 4.13 | 12.25 | 19.21 | 2.00 | 75.6 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.2 | 3.05 | 8.24 | 12.99 | 1.00 | 61.5 | 90.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 4.9 | 0.38 | 1.09 | 2.43 | 0.00 | 10.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.6 | 6.74 | 20.73 | 33.97 | 13.00 | 105.7 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.9 | 5.42 | 15.24 | 25.76 | 5.00 | 80.2 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.5 | 5.03 | 13.92 | 21.75 | 2.00 | 79.8 | 90.0 |
| XI | XI | Jack Grealish | MID | 12 | 8.0 | 4.00 | 12.39 | 19.63 | 2.00 | 79.4 | 65.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.7 | 4.29 | 11.78 | 19.16 | 1.00 | 74.1 | 20.0 |

## GW8

- Train rows: 56469
- Bank: 1.90 -> 1.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.40
- Actual score: 63.00
- Transfer: Marcos Alonso -> João Pedro Cavaco Cancelo (projected gain 4.62, hit 0)
- Autosub: Emmanuel Dennis replaced Jack Grealish.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.60 | 10.09 | 16.17 | 6.00 | 89.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 2.76 | 8.60 | 14.01 | 2.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.2 | 4.82 | 13.03 | 20.25 | 6.00 | 92.3 | 90.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.2 | 4.21 | 11.28 | 17.61 | 5.00 | 92.5 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.4 | 3.33 | 10.56 | 17.57 | 0.00 | 72.2 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.19 | 9.06 | 14.64 | 7.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Ethan Pinnock | DEF | 3 | 4.5 | 2.66 | 8.13 | 13.34 | 2.00 | 78.3 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 4.31 | 11.80 | 18.96 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Autosub In | Emmanuel Dennis | FWD | 18 | 5.1 | 3.03 | 8.46 | 13.69 | 2.00 | 67.7 | 68.0 |
| Bench 4 | Bench | Folarin Balogun | FWD | 1 | 4.8 | 0.34 | 0.80 | 1.98 | 0.00 | 8.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.6 | 8.13 | 23.14 | 37.31 | 13.00 | 119.3 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.8 | 5.31 | 15.73 | 26.11 | 5.00 | 84.8 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.5 | 4.32 | 12.10 | 19.82 | 3.00 | 77.8 | 86.0 |
| XI | Bench | Jack Grealish | MID | 12 | 7.9 | 4.01 | 11.24 | 17.82 | 0.00 | 71.5 | 0.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.6 | 3.05 | 9.35 | 15.79 | 1.00 | 50.4 | 90.0 |

## GW9

- Train rows: 57086
- Bank: 1.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.52
- Actual score: 71.00
- Transfer: Folarin Balogun -> Ivan Toney (projected gain 3.00, hit 0)
- Autosub: Luke Shaw replaced Shane Duffy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.25 | 10.05 | 16.28 | 4.00 | 89.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 3.18 | 8.69 | 13.88 | 2.00 | 83.4 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.2 | 4.22 | 12.60 | 19.99 | 1.00 | 80.7 | 90.0 |
| XI | Bench | Shane Duffy | DEF | 4 | 4.2 | 3.43 | 10.54 | 16.61 | 0.00 | 87.4 | 0.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.45 | 9.45 | 15.23 | 12.00 | 81.0 | 90.0 |
| XI | XI | Ethan Pinnock | DEF | 3 | 4.5 | 3.41 | 9.11 | 14.41 | 1.00 | 78.1 | 45.0 |
| Bench 2 | Autosub In | Luke Shaw | DEF | 13 | 5.3 | 2.86 | 8.84 | 14.44 | -1.00 | 73.7 | 90.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.5 | 4.29 | 11.73 | 18.31 | 2.00 | 86.3 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.89 | 10.82 | 17.27 | 2.00 | 76.8 | 80.0 |
| Bench 3 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 2.69 | 7.33 | 11.84 | 12.00 | 59.9 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 7.99 | 23.66 | 38.01 | 24.00 | 114.3 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.8 | 5.21 | 15.38 | 25.09 | 1.00 | 95.5 | 61.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.5 | 4.24 | 11.77 | 19.15 | 3.00 | 76.3 | 84.0 |
| XI | XI | Paul Pogba | MID | 13 | 7.6 | 3.15 | 9.93 | 16.66 | -2.00 | 66.4 | 15.0 |
| Bench 4 | Bench | Jack Grealish | MID | 12 | 7.9 | 2.37 | 7.23 | 12.40 | 6.00 | 34.5 | 76.0 |

## GW10

- Train rows: 57704
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.31
- Actual score: 43.00
- Transfer: Ethan Pinnock -> Tino Livramento (projected gain 3.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 2.95 | 9.11 | 15.11 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 2.68 | 7.36 | 12.15 | 0.00 | 74.8 | 0.0 |
| Vice Captain | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.3 | 4.46 | 12.03 | 18.96 | 2.00 | 82.7 | 77.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.4 | 4.07 | 11.20 | 17.40 | 6.00 | 88.6 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.85 | 10.81 | 17.42 | 2.00 | 84.6 | 90.0 |
| XI | XI | Luke Shaw | DEF | 13 | 5.3 | 2.71 | 7.99 | 13.09 | 5.00 | 72.9 | 90.0 |
| Bench 3 | Bench | Shane Duffy | DEF | 4 | 4.2 | 1.66 | 5.77 | 9.71 | 0.00 | 46.6 | 90.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.5 | 4.21 | 11.47 | 17.89 | 2.00 | 81.6 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 2.81 | 9.08 | 14.62 | 2.00 | 65.2 | 90.0 |
| Bench 2 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 2.54 | 7.30 | 12.12 | 0.00 | 44.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 8.95 | 25.54 | 41.33 | 5.00 | 124.1 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 3.91 | 12.60 | 21.14 | 6.00 | 69.9 | 75.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 4.04 | 11.25 | 18.17 | 5.00 | 72.4 | 63.0 |
| XI | XI | Jack Grealish | MID | 12 | 7.8 | 3.42 | 9.72 | 16.02 | 2.00 | 57.4 | 77.0 |
| Bench 4 | Bench | Paul Pogba | MID | 13 | 7.5 | 1.28 | 5.32 | 10.21 | 0.00 | 27.0 | 0.0 |

## GW11

- Train rows: 58327
- Bank: 0.20 -> 2.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Emile Smith Rowe
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.31
- Actual score: 47.00
- Transfer: Paul Pogba -> Emile Smith Rowe (projected gain 5.96, hit 0)
- Autosub: Aaron Cresswell replaced Jack Grealish.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.48 | 9.56 | 15.42 | -1.00 | 86.3 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 1.41 | 4.02 | 7.08 | 0.00 | 35.5 | 0.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.4 | 4.28 | 11.45 | 17.94 | 6.00 | 82.2 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.3 | 3.72 | 10.82 | 17.21 | 14.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Luke Shaw | DEF | 13 | 5.2 | 2.76 | 8.70 | 14.00 | 1.00 | 77.1 | 72.0 |
| XI | XI | Shane Duffy | DEF | 4 | 4.2 | 3.16 | 8.44 | 13.50 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Autosub In | Aaron Cresswell | DEF | 19 | 5.5 | 2.81 | 8.24 | 13.78 | 1.00 | 75.5 | 90.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.6 | 4.39 | 11.46 | 17.77 | 1.00 | 77.9 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.44 | 9.64 | 15.54 | 2.00 | 72.2 | 90.0 |
| Bench 4 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 1.39 | 4.80 | 8.19 | 2.00 | 29.4 | 73.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 7.52 | 22.31 | 36.75 | 5.00 | 112.0 | 90.0 |
| Vice Captain | XI | Emile Smith Rowe | MID | 1 | 5.7 | 5.19 | 14.11 | 21.37 | 8.00 | 93.0 | 85.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 4.29 | 14.08 | 23.47 | 2.00 | 80.9 | 90.0 |
| XI | Bench | Jack Grealish | MID | 12 | 7.8 | 3.23 | 9.69 | 16.04 | 0.00 | 56.2 | 0.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 3.08 | 9.29 | 15.38 | 2.00 | 60.9 | 85.0 |

## GW12

- Train rows: 58951
- Bank: 2.00 -> 3.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.99
- Actual score: 58.00
- Transfer: Jack Grealish -> Conor Gallagher (projected gain 5.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 4 | 4.5 | 2.52 | 7.30 | 12.25 | 0.00 | 73.6 | 0.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.5 | 0.82 | 2.85 | 5.28 | 0.00 | 28.7 | 0.0 |
| Vice Captain | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.3 | 5.29 | 13.69 | 21.40 | 12.00 | 92.0 | 90.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.5 | 4.60 | 12.65 | 19.77 | 1.00 | 90.0 | 90.0 |
| XI | XI | Aaron Cresswell | DEF | 19 | 5.5 | 3.01 | 9.07 | 15.04 | 2.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Shane Duffy | DEF | 4 | 4.2 | 2.97 | 8.10 | 12.79 | 1.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Luke Shaw | DEF | 13 | 5.2 | 2.66 | 7.30 | 12.18 | 1.00 | 65.9 | 84.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.67 | 9.81 | 15.94 | 10.00 | 77.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.6 | 3.43 | 9.58 | 15.20 | 6.00 | 68.1 | 90.0 |
| Bench 4 | Bench | Emmanuel Dennis | FWD | 18 | 5.1 | 2.64 | 7.44 | 12.27 | 14.00 | 56.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.55 | 22.77 | 37.51 | 8.00 | 120.5 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 4.90 | 14.33 | 23.77 | 2.00 | 88.7 | 90.0 |
| XI | XI | Conor Gallagher | MID | 7 | 5.9 | 5.06 | 13.66 | 21.06 | 5.00 | 95.4 | 80.0 |
| XI | XI | Emile Smith Rowe | MID | 1 | 5.7 | 3.75 | 11.89 | 18.44 | 2.00 | 76.3 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.4 | 3.65 | 10.41 | 17.08 | 2.00 | 71.9 | 70.0 |

## GW13

- Train rows: 59582
- Bank: 3.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.16
- Actual score: 57.00
- Transfer: Shane Duffy -> Trent Alexander-Arnold (projected gain 7.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 1.72 | 5.34 | 9.09 | 8.00 | 41.9 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.4 | 0.66 | 1.95 | 3.53 | 0.00 | 17.1 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 5.57 | 15.98 | 25.34 | 9.00 | 98.9 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.4 | 5.04 | 14.15 | 21.96 | 1.00 | 86.7 | 90.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.5 | 2.93 | 9.86 | 15.49 | 0.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Aaron Cresswell | DEF | 19 | 5.5 | 2.52 | 9.19 | 14.96 | 2.00 | 79.4 | 60.0 |
| Bench 4 | Bench | Luke Shaw | DEF | 13 | 5.2 | 2.09 | 6.55 | 11.60 | 0.00 | 67.4 | 0.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.6 | 4.10 | 10.90 | 17.27 | 9.00 | 77.8 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.66 | 10.71 | 17.29 | 2.00 | 82.4 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.2 | 3.19 | 9.08 | 14.33 | 10.00 | 70.2 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 8.18 | 24.04 | 37.80 | 6.00 | 117.3 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.94 | 13.40 | 22.98 | 1.00 | 89.1 | 88.0 |
| XI | XI | Emile Smith Rowe | MID | 1 | 5.8 | 4.97 | 13.39 | 20.39 | 3.00 | 92.7 | 90.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 4.68 | 12.73 | 19.52 | 2.00 | 75.1 | 90.0 |
| Bench 2 | Bench | Saïd Benrahma | MID | 19 | 6.3 | 2.54 | 8.82 | 14.87 | 1.00 | 61.8 | 58.0 |

## GW14

- Train rows: 60215
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.80
- Actual score: 63.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 2.78 | 7.92 | 12.68 | 4.00 | 73.9 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.4 | 0.26 | 1.55 | 3.01 | 0.00 | 16.3 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 5.27 | 14.73 | 23.74 | 2.00 | 83.5 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.4 | 4.54 | 12.14 | 19.66 | 2.00 | 79.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.5 | 3.53 | 9.67 | 15.16 | 1.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 5.5 | 2.70 | 7.72 | 12.79 | 0.00 | 64.6 | 0.0 |
| Bench 4 | Bench | Luke Shaw | DEF | 13 | 5.1 | 1.19 | 4.17 | 7.54 | 0.00 | 35.4 | 0.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.6 | 3.75 | 11.04 | 17.99 | 2.00 | 83.5 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.8 | 4.09 | 10.71 | 17.30 | 2.00 | 82.2 | 76.0 |
| Bench 3 | Bench | Emmanuel Dennis | FWD | 18 | 5.2 | 2.52 | 8.78 | 14.13 | 9.00 | 62.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 8.11 | 22.59 | 35.68 | 15.00 | 111.0 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.11 | 13.29 | 22.56 | 9.00 | 89.7 | 89.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 4.04 | 12.30 | 19.05 | 1.00 | 76.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 1 | 5.8 | 3.95 | 11.72 | 17.92 | 7.00 | 77.9 | 69.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.2 | 3.52 | 9.58 | 16.04 | 3.00 | 64.8 | 75.0 |

## GW15

- Train rows: 60851
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.43
- Actual score: 38.00
- Transfer: Aaron Cresswell -> Sergio Reguilón (projected gain 0.71, hit 0)
- Autosub: Tino Livramento replaced Emile Smith Rowe.
- Autosub: Saïd Benrahma replaced Ivan Toney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.15 | 8.67 | 14.08 | 3.00 | 78.0 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.4 | 0.58 | 1.52 | 3.05 | 0.00 | 14.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.91 | 14.66 | 23.88 | 9.00 | 92.8 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 5.04 | 14.13 | 22.41 | 2.00 | 90.7 | 90.0 |
| XI | XI | Sergio Reguilón | DEF | 17 | 5.2 | 3.69 | 9.88 | 15.85 | 0.00 | 77.3 | 21.0 |
| Bench 2 | Autosub In | Tino Livramento | DEF | 16 | 4.4 | 3.39 | 9.32 | 14.58 | 2.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Luke Shaw | DEF | 13 | 5.1 | 1.44 | 4.38 | 7.53 | 0.00 | 31.8 | 0.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.3 | 4.15 | 11.95 | 18.96 | 2.00 | 93.3 | 90.0 |
| XI | Bench | Ivan Toney | FWD | 3 | 6.6 | 4.12 | 11.31 | 18.43 | 0.00 | 85.5 | 0.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.8 | 3.60 | 10.09 | 16.42 | 2.00 | 71.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.74 | 22.01 | 35.95 | 6.00 | 115.4 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 5.07 | 14.92 | 24.64 | 3.00 | 92.1 | 85.0 |
| XI | Bench | Emile Smith Rowe | MID | 1 | 5.9 | 4.55 | 12.91 | 20.15 | 0.00 | 86.2 | 0.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 3.66 | 11.24 | 17.85 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Autosub In | Saïd Benrahma | MID | 19 | 6.1 | 2.79 | 8.89 | 14.88 | 1.00 | 66.4 | 5.0 |

## GW16

- Train rows: 61491
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.05
- Actual score: 65.00
- Transfer: Emile Smith Rowe -> Demarai Gray (projected gain 3.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 4 | 4.5 | 2.32 | 7.39 | 12.80 | 0.00 | 65.4 | 0.0 |
| Bench 1 | Bench | David Raya Martin | GK | 3 | 4.4 | 0.52 | 1.24 | 2.40 | 0.00 | 10.8 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 5.55 | 16.12 | 25.90 | 9.00 | 97.1 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 4.82 | 14.37 | 22.50 | 7.00 | 93.6 | 90.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.4 | 3.05 | 8.84 | 13.91 | 1.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Sergio Reguilón | DEF | 17 | 5.2 | 1.18 | 5.19 | 9.03 | 0.00 | 18.3 | 0.0 |
| Bench 4 | Bench | Luke Shaw | DEF | 13 | 5.1 | 1.12 | 3.36 | 6.28 | 0.00 | 23.3 | 0.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.4 | 5.03 | 13.42 | 19.78 | 9.00 | 85.5 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.43 | 9.78 | 15.89 | 1.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Ivan Toney | FWD | 3 | 6.5 | 1.58 | 4.87 | 9.18 | 0.00 | 22.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 8.12 | 22.90 | 37.27 | 8.00 | 116.2 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.81 | 14.02 | 23.61 | 3.00 | 87.2 | 87.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 3.90 | 10.76 | 17.29 | 15.00 | 78.4 | 90.0 |
| XI | XI | Demarai Gray | MID | 8 | 5.5 | 3.65 | 9.90 | 15.45 | 1.00 | 76.5 | 90.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.0 | 2.26 | 7.26 | 12.48 | 3.00 | 41.6 | 69.0 |

## GW17

- Train rows: 62138
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.78
- Actual score: 37.00
- Transfer: David Raya Martin -> Aaron Ramsdale (projected gain 4.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.0 | 3.38 | 9.93 | 16.03 | 5.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 1.76 | 5.69 | 9.77 | 3.00 | 47.4 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 5.78 | 15.53 | 24.99 | 11.00 | 94.5 | 90.0 |
| XI | Bench | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 3.77 | 10.63 | 17.64 | 0.00 | 67.8 | 0.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.4 | 3.07 | 7.94 | 12.91 | 0.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Sergio Reguilón | DEF | 17 | 5.2 | 1.03 | 4.20 | 7.62 | 0.00 | 15.9 | 0.0 |
| Bench 4 | Bench | Luke Shaw | DEF | 13 | 5.1 | 0.28 | 1.89 | 4.11 | 0.00 | 3.0 | 0.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 2.84 | 9.24 | 15.26 | 2.00 | 71.1 | 78.0 |
| XI | Bench | Emmanuel Dennis | FWD | 18 | 5.4 | 2.49 | 8.86 | 13.90 | 0.00 | 38.9 | 0.0 |
| Bench 3 | Bench | Ivan Toney | FWD | 3 | 6.5 | 1.02 | 4.76 | 9.15 | 0.00 | 12.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 8.64 | 23.33 | 37.95 | 8.00 | 117.4 | 73.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 5.31 | 13.50 | 21.40 | 2.00 | 96.4 | 90.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.03 | 12.79 | 22.03 | 0.00 | 68.5 | 0.0 |
| XI | Bench | Demarai Gray | MID | 8 | 5.5 | 3.07 | 9.28 | 14.86 | 0.00 | 74.8 | 0.0 |
| XI | XI | Saïd Benrahma | MID | 19 | 6.0 | 2.76 | 8.36 | 13.65 | 1.00 | 57.2 | 14.0 |

## GW18

- Train rows: 62794
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 47.26
- Actual score: 35.00
- Transfer: Luke Shaw -> Gabriel Magalhães (projected gain 7.15, hit 0)
- Autosub: Sergio Reguilón replaced Tino Livramento.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.0 | 4.63 | 12.61 | 19.87 | 2.00 | 98.7 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 2.00 | 6.92 | 11.74 | 0.00 | 57.0 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.98 | 14.57 | 24.43 | 7.00 | 94.5 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 4.09 | 10.81 | 16.78 | 2.00 | 82.3 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 3.63 | 10.36 | 17.48 | 18.00 | 56.2 | 90.0 |
| XI | Bench | Tino Livramento | DEF | 16 | 4.4 | 2.30 | 7.02 | 11.76 | 0.00 | 61.7 | 0.0 |
| Bench 4 | Autosub In | Sergio Reguilón | DEF | 17 | 5.2 | 0.29 | 2.13 | 4.83 | 1.00 | 10.8 | 4.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 2.92 | 9.00 | 15.00 | 1.00 | 72.6 | 45.0 |
| XI | Bench | Emmanuel Dennis | FWD | 18 | 5.4 | 1.70 | 6.10 | 10.75 | 0.00 | 25.9 | 0.0 |
| Bench 3 | Bench | Ivan Toney | FWD | 3 | 6.5 | 0.79 | 3.56 | 6.75 | 0.00 | 8.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 7.64 | 22.51 | 36.96 | 2.00 | 111.9 | 90.0 |
| XI | Bench | Conor Gallagher | MID | 7 | 6.0 | 3.29 | 10.14 | 16.85 | 0.00 | 61.4 | 0.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 2.63 | 9.43 | 16.68 | 0.00 | 34.4 | 0.0 |
| XI | Bench | Saïd Benrahma | MID | 19 | 6.0 | 1.83 | 6.15 | 10.52 | 0.00 | 22.9 | 0.0 |
| Bench 2 | Bench | Demarai Gray | MID | 8 | 5.5 | 1.09 | 4.45 | 7.93 | 0.00 | 21.4 | 0.0 |

## GW19

- Train rows: 63455
- Bank: -0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: João Pedro Cavaco Cancelo
- Chip used: none
- Predicted score: 48.49
- Actual score: 44.00
- Transfer: Saïd Benrahma -> Gabriel Teodoro Martinelli Silva (projected gain 9.71, hit 0)
- Autosub: Ivan Toney replaced Trent Alexander-Arnold.
- Autosub: Tino Livramento replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.1 | 3.55 | 10.32 | 16.63 | 6.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 1.66 | 4.72 | 7.87 | 9.00 | 37.3 | 90.0 |
| Vice Captain | Captain | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 5.63 | 14.76 | 23.44 | 4.00 | 90.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.13 | 12.65 | 21.91 | 0.00 | 70.4 | 0.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 3.60 | 9.72 | 15.33 | 6.00 | 78.5 | 90.0 |
| XI | XI | Sergio Reguilón | DEF | 17 | 5.2 | 2.29 | 6.47 | 10.08 | 7.00 | 35.8 | 90.0 |
| Bench 3 | Autosub In | Tino Livramento | DEF | 16 | 4.4 | 1.13 | 3.72 | 6.48 | 1.00 | 36.1 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.6 | 3.03 | 8.56 | 13.89 | 9.00 | 63.0 | 82.0 |
| XI | Bench | Emmanuel Dennis | FWD | 18 | 5.4 | 1.56 | 5.31 | 9.55 | 0.00 | 20.3 | 0.0 |
| Bench 2 | Autosub In | Ivan Toney | FWD | 3 | 6.5 | 1.39 | 3.91 | 6.97 | 1.00 | 18.2 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 12.8 | 7.13 | 21.51 | 35.38 | 0.00 | 96.2 | 0.0 |
| XI | XI | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 5.47 | 14.11 | 21.29 | 3.00 | 99.8 | 81.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.03 | 9.93 | 16.87 | 1.00 | 45.2 | 90.0 |
| XI | XI | Conor Gallagher | MID | 7 | 6.0 | 1.94 | 6.88 | 12.15 | 2.00 | 42.5 | 74.0 |
| Bench 4 | Bench | Demarai Gray | MID | 8 | 5.5 | 0.63 | 3.13 | 5.81 | 0.00 | 11.7 | 0.0 |

## GW20

- Train rows: 64120
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 44.21
- Actual score: 22.00
- Transfer: Demarai Gray -> Jorge Luiz Frello Filho (projected gain 1.59, hit 0)
- Autosub: Robert Sánchez replaced Aaron Ramsdale.
- Autosub: Ivan Toney replaced Tino Livramento.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Aaron Ramsdale | GK | 1 | 5.1 | 2.72 | 9.05 | 15.10 | 0.00 | 67.2 | 0.0 |
| Bench 1 | Autosub In | Robert Sánchez | GK | 4 | 4.5 | 2.56 | 7.68 | 12.67 | 3.00 | 72.4 | 90.0 |
| Vice Captain | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 4.37 | 12.87 | 20.85 | 6.00 | 73.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.64 | 10.72 | 18.77 | 2.00 | 55.1 | 90.0 |
| XI | XI | Sergio Reguilón | DEF | 17 | 5.2 | 2.97 | 8.08 | 12.69 | 0.00 | 53.2 | 45.0 |
| Bench 2 | Bench | Gabriel Magalhães | DEF | 1 | 5.2 | 2.43 | 8.02 | 13.18 | 0.00 | 60.1 | 0.0 |
| XI | Bench | Tino Livramento | DEF | 16 | 4.4 | 2.64 | 7.29 | 11.64 | 0.00 | 71.4 | 0.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.5 | 3.69 | 9.22 | 14.31 | 7.00 | 56.8 | 90.0 |
| XI | Bench | Allan Saint-Maximin | FWD | 14 | 6.6 | 2.51 | 7.73 | 13.06 | 0.00 | 48.7 | 0.0 |
| Bench 4 | Autosub In | Ivan Toney | FWD | 3 | 6.5 | 2.05 | 6.65 | 11.16 | 2.00 | 51.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 5.09 | 15.63 | 26.80 | 0.00 | 55.6 | 90.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.05 | 11.58 | 19.72 | 0.00 | 66.5 | 0.0 |
| XI | Bench | Conor Gallagher | MID | 7 | 6.0 | 3.97 | 11.03 | 17.03 | 0.00 | 76.6 | 0.0 |
| XI | XI | Jorge Luiz Frello Filho | MID | 6 | 5.9 | 3.47 | 9.51 | 14.99 | 2.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 2.26 | 7.71 | 12.79 | 0.00 | 38.0 | 0.0 |

## GW21

- Train rows: 64789
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Saïd Benrahma
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.99
- Actual score: 36.00
- Transfer: Conor Gallagher -> Saïd Benrahma (projected gain 8.96, hit 0)
- Autosub: Gabriel Magalhães replaced Allan Saint-Maximin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.05 | 8.21 | 13.63 | 2.00 | 74.0 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 1.21 | 5.69 | 10.07 | 1.00 | 41.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.43 | 13.68 | 22.45 | 4.00 | 84.9 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.5 | 4.30 | 13.59 | 22.58 | 2.00 | 93.1 | 90.0 |
| XI | XI | Sergio Reguilón | DEF | 17 | 5.3 | 2.95 | 7.72 | 12.57 | 6.00 | 47.4 | 82.0 |
| Bench 3 | Autosub In | Gabriel Magalhães | DEF | 1 | 5.2 | 1.22 | 5.48 | 9.38 | -3.00 | 40.8 | 58.0 |
| Bench 2 | Bench | Tino Livramento | DEF | 16 | 4.4 | 1.23 | 3.37 | 6.07 | 0.00 | 29.5 | 0.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.5 | 4.90 | 10.74 | 16.04 | 2.00 | 101.7 | 180.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 3.61 | 10.09 | 16.39 | 1.00 | 67.2 | 45.0 |
| XI | Bench | Allan Saint-Maximin | FWD | 14 | 6.6 | 1.24 | 4.66 | 8.63 | 0.00 | 19.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.7 | 5.70 | 17.51 | 29.11 | 7.00 | 82.8 | 90.0 |
| Vice Captain | XI | Saïd Benrahma | MID | 19 | 5.9 | 5.33 | 11.84 | 17.61 | 6.00 | 99.5 | 70.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.09 | 9.54 | 16.62 | 1.00 | 42.5 | 30.0 |
| XI | XI | Jorge Luiz Frello Filho | MID | 6 | 5.9 | 2.70 | 8.64 | 14.05 | 1.00 | 68.4 | 20.0 |
| Bench 4 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 0.59 | 3.86 | 7.59 | 2.00 | 22.8 | 90.0 |

## GW22

- Train rows: 65467
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Miguel Borges Fernandes
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bruno Miguel Borges Fernandes
- Chip used: none
- Predicted score: 49.81
- Actual score: 94.00
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jorge Luiz Frello Filho -> Manuel Lanzini (projected gain 5.25, hit 0)
- Autosub: Allan Saint-Maximin replaced Saïd Benrahma.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 4.38 | 10.15 | 15.30 | 4.00 | 108.9 | 180.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 2.22 | 7.08 | 12.13 | 0.00 | 55.6 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.15 | 14.26 | 22.77 | 10.00 | 85.2 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 4.27 | 13.18 | 21.50 | 11.00 | 82.9 | 90.0 |
| XI | XI | Sergio Reguilón | DEF | 17 | 5.3 | 3.46 | 9.40 | 14.79 | 1.00 | 62.8 | 78.0 |
| Bench 2 | Bench | Gabriel Magalhães | DEF | 1 | 5.2 | 1.68 | 5.34 | 9.39 | 0.00 | 41.5 | 0.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 16 | 4.3 | 0.50 | 2.06 | 4.29 | 0.00 | 16.1 | 0.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.5 | 4.65 | 11.05 | 16.72 | 10.00 | 113.3 | 180.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 3.70 | 10.17 | 16.80 | 2.00 | 62.2 | 83.0 |
| Bench 3 | Autosub In | Allan Saint-Maximin | FWD | 14 | 6.6 | 1.60 | 4.34 | 7.73 | 9.00 | 23.9 | 85.0 |
| Captain | Captain | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 5.95 | 14.57 | 23.11 | 23.00 | 96.9 | 178.0 |
| XI | XI | Manuel Lanzini | MID | 19 | 5.8 | 4.92 | 12.80 | 19.77 | 1.00 | 100.9 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.7 | 2.73 | 9.84 | 19.27 | 0.00 | 24.5 | 0.0 |
| XI | Bench | Saïd Benrahma | MID | 19 | 5.9 | 2.74 | 8.03 | 13.30 | 0.00 | 41.7 | 0.0 |
| XI | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 1.91 | 6.51 | 10.49 | 0.00 | 43.0 | 0.0 |

## GW23

- Train rows: 66155
- Bank: 0.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Emmanuel Dennis
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Emmanuel Dennis
- Chip used: none
- Predicted score: 52.89
- Actual score: 30.00
- Transfer: Saïd Benrahma -> Alexis Mac Allister (projected gain 7.06, hit 0)
- Autosub: Gabriel Magalhães replaced Sergio Reguilón.
- Autosub: Gabriel Teodoro Martinelli Silva replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.89 | 11.45 | 18.07 | 4.00 | 110.1 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 2.00 | 5.46 | 8.70 | 8.00 | 35.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.72 | 15.54 | 24.86 | 2.00 | 91.6 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 5.40 | 15.11 | 24.09 | 2.00 | 98.4 | 90.0 |
| XI | Bench | Sergio Reguilón | DEF | 17 | 5.3 | 2.13 | 7.16 | 11.38 | 0.00 | 45.3 | 0.0 |
| Bench 3 | Autosub In | Gabriel Magalhães | DEF | 1 | 5.2 | 1.24 | 3.47 | 5.58 | 6.00 | 22.3 | 90.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 16 | 4.3 | 0.17 | 1.30 | 3.12 | 0.00 | 13.3 | 0.0 |
| Captain | Captain | Emmanuel Dennis | FWD | 18 | 5.6 | 5.86 | 13.33 | 20.22 | -1.00 | 101.6 | 77.0 |
| XI | XI | Ivan Toney | FWD | 3 | 6.5 | 4.34 | 11.79 | 18.31 | 7.00 | 100.5 | 90.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.09 | 7.69 | 12.43 | 1.00 | 58.0 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 5.76 | 16.99 | 27.92 | 3.00 | 102.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.6 | 3.98 | 12.17 | 23.00 | 0.00 | 32.9 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 4 | 5.3 | 4.07 | 11.26 | 17.81 | 2.00 | 92.6 | 90.0 |
| XI | XI | Manuel Lanzini | MID | 19 | 5.8 | 2.81 | 8.88 | 14.36 | 2.00 | 75.0 | 90.0 |
| Bench 2 | Autosub In | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 1.66 | 4.89 | 7.34 | 3.00 | 24.9 | 90.0 |

## GW24

- Train rows: 66852
- Bank: 0.90 -> 0.40
- Free transfers: 2 -> 2
- Captain: João Pedro Cavaco Cancelo
- Vice captain: Trent Alexander-Arnold
- Effective captain: João Pedro Cavaco Cancelo
- Chip used: none
- Predicted score: 48.50
- Actual score: 63.00
- Transfer: Sergio Reguilón -> Aymeric Laporte (projected gain 4.62, hit 0)
- Autosub: Gabriel Magalhães replaced Ivan Toney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.0 | 2.85 | 8.23 | 13.11 | 9.00 | 67.8 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 2.36 | 8.11 | 13.61 | 0.00 | 71.8 | 0.0 |
| Captain | Captain | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 5.61 | 14.78 | 23.29 | 7.00 | 89.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.39 | 14.75 | 23.97 | 6.00 | 91.9 | 90.0 |
| XI | XI | Aymeric Laporte | DEF | 12 | 5.8 | 4.55 | 11.80 | 18.45 | 6.00 | 83.5 | 90.0 |
| Bench 2 | Autosub In | Gabriel Magalhães | DEF | 1 | 5.2 | 2.51 | 7.22 | 11.25 | 14.00 | 61.0 | 90.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 16 | 4.3 | 0.24 | 1.55 | 2.97 | 0.00 | 11.6 | 0.0 |
| XI | Bench | Ivan Toney | FWD | 3 | 6.5 | 3.21 | 9.93 | 15.50 | 0.00 | 79.6 | 0.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.7 | 3.22 | 8.49 | 13.72 | 5.00 | 60.7 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 2.68 | 8.34 | 13.75 | 2.00 | 52.3 | 90.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 5.00 | 15.44 | 25.79 | 2.00 | 82.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.6 | 4.47 | 13.12 | 22.52 | 1.00 | 50.2 | 30.0 |
| XI | XI | Manuel Lanzini | MID | 19 | 5.8 | 3.34 | 8.89 | 14.22 | 4.00 | 77.7 | 30.0 |
| Bench 3 | Bench | Alexis Mac Allister | MID | 4 | 5.3 | 2.26 | 7.31 | 12.61 | 0.00 | 56.8 | 0.0 |
| XI | XI | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 2.57 | 6.80 | 10.61 | 0.00 | 55.3 | 68.0 |

## GW25

- Train rows: 67557
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Miguel Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Miguel Borges Fernandes
- Chip used: none
- Predicted score: 56.53
- Actual score: 51.00
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Aaron Ramsdale -> David de Gea (projected gain 5.89, hit 0)
- Autosub: Tino Livramento replaced João Pedro Cavaco Cancelo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David de Gea | GK | 13 | 5.3 | 5.44 | 12.90 | 19.16 | 10.00 | 123.4 | 180.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.15 | 7.34 | 11.15 | 8.00 | 83.7 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.60 | 15.69 | 25.18 | 6.00 | 94.1 | 90.0 |
| XI | Bench | João Pedro Cavaco Cancelo | DEF | 12 | 6.7 | 5.24 | 14.16 | 22.80 | 0.00 | 92.0 | 0.0 |
| XI | Bench | Aymeric Laporte | DEF | 12 | 5.8 | 3.45 | 9.72 | 15.94 | 0.00 | 79.7 | 0.0 |
| Bench 2 | Bench | Gabriel Magalhães | DEF | 1 | 5.2 | 2.06 | 6.25 | 10.66 | 0.00 | 45.5 | 0.0 |
| Bench 4 | Autosub In | Tino Livramento | DEF | 16 | 4.3 | 0.26 | 1.47 | 2.77 | 1.00 | 11.0 | 19.0 |
| XI | XI | Allan Saint-Maximin | FWD | 14 | 6.8 | 3.96 | 10.22 | 16.46 | 2.00 | 72.6 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 3.71 | 10.20 | 16.33 | 1.00 | 67.9 | 90.0 |
| XI | Bench | Ivan Toney | FWD | 3 | 6.5 | 2.62 | 6.99 | 11.32 | 0.00 | 42.3 | 0.0 |
| Captain | Captain | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 7.77 | 19.60 | 30.64 | 12.00 | 129.4 | 180.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 12.7 | 5.81 | 16.17 | 25.48 | 3.00 | 66.7 | 90.0 |
| XI | XI | Alexis Mac Allister | MID | 4 | 5.3 | 2.93 | 6.82 | 9.84 | 2.00 | 68.5 | 116.0 |
| XI | XI | Manuel Lanzini | MID | 19 | 5.8 | 2.22 | 6.59 | 10.78 | 2.00 | 53.0 | 78.0 |
| Bench 3 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.4 | 1.37 | 4.51 | 7.89 | 0.00 | 30.3 | 0.0 |

## GW26

- Train rows: 68264
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.03
- Actual score: 98.00
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Ivan Toney -> Neal Maupay (projected gain 8.40, hit 0)
- Autosub: Gabriel Teodoro Martinelli Silva replaced Manuel Lanzini.
- Autosub: Aymeric Laporte replaced Allan Saint-Maximin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David de Gea | GK | 13 | 5.3 | 4.59 | 13.00 | 20.54 | 2.00 | 116.5 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 4.35 | 11.35 | 17.89 | 1.00 | 111.1 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 7.67 | 18.64 | 28.37 | 6.00 | 132.5 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.7 | 3.34 | 9.96 | 16.59 | 1.00 | 47.8 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 4.07 | 7.56 | 11.15 | 3.00 | 74.0 | 180.0 |
| Bench 3 | Autosub In | Aymeric Laporte | DEF | 12 | 5.8 | 1.97 | 6.27 | 10.91 | 1.00 | 39.9 | 90.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 16 | 4.3 | 1.10 | 2.90 | 5.01 | 12.00 | 21.3 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 5.34 | 12.00 | 18.09 | 11.00 | 104.5 | 175.0 |
| XI | XI | Neal Maupay | FWD | 4 | 6.6 | 4.33 | 11.66 | 18.20 | 2.00 | 87.1 | 90.0 |
| XI | Bench | Allan Saint-Maximin | FWD | 14 | 6.8 | 3.42 | 9.63 | 15.30 | 0.00 | 67.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.8 | 10.13 | 24.67 | 36.13 | 28.00 | 149.0 | 180.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 5.94 | 17.33 | 27.94 | 12.00 | 98.9 | 90.0 |
| XI | XI | Alexis Mac Allister | MID | 4 | 5.3 | 3.39 | 9.38 | 14.36 | 2.00 | 78.6 | 90.0 |
| XI | Bench | Manuel Lanzini | MID | 19 | 5.8 | 2.67 | 7.96 | 12.73 | 0.00 | 67.9 | 0.0 |
| Bench 2 | Autosub In | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 2.49 | 4.04 | 6.13 | 2.00 | 46.5 | 70.0 |

## GW27

- Train rows: 68975
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Wout Weghorst
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Wout Weghorst
- Chip used: none
- Predicted score: 60.47
- Actual score: 48.00
- Chip advisory: triple_captain (0.61): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Allan Saint-Maximin -> Wout Weghorst (projected gain 10.24, hit 0)
- Autosub: Manuel Lanzini replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David de Gea | GK | 13 | 5.3 | 3.88 | 11.12 | 18.01 | 6.00 | 96.8 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.31 | 9.08 | 14.59 | 1.00 | 85.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.87 | 14.79 | 24.30 | 0.00 | 80.4 | 0.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 5.25 | 14.35 | 22.53 | 9.00 | 89.0 | 90.0 |
| XI | XI | Aymeric Laporte | DEF | 12 | 5.8 | 3.23 | 9.32 | 14.70 | 7.00 | 70.3 | 90.0 |
| Bench 2 | Bench | Gabriel Magalhães | DEF | 1 | 5.2 | 2.89 | 8.75 | 14.52 | 0.00 | 74.2 | 0.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.3 | 2.98 | 7.44 | 11.25 | 8.00 | 59.0 | 90.0 |
| Captain | Captain | Wout Weghorst | FWD | 5 | 6.5 | 7.93 | 17.93 | 26.39 | 3.00 | 167.2 | 180.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 4.03 | 11.71 | 19.28 | 2.00 | 100.4 | 90.0 |
| XI | XI | Neal Maupay | FWD | 4 | 6.6 | 3.58 | 9.86 | 15.92 | 2.00 | 70.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.8 | 6.92 | 21.01 | 33.49 | 0.00 | 81.9 | 0.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 6.98 | 19.46 | 31.29 | 3.00 | 108.7 | 90.0 |
| XI | XI | Alexis Mac Allister | MID | 4 | 5.3 | 2.90 | 7.48 | 11.57 | 2.00 | 65.0 | 90.0 |
| Bench 3 | Autosub In | Manuel Lanzini | MID | 19 | 5.8 | 1.34 | 4.29 | 7.61 | 3.00 | 33.9 | 90.0 |
| Bench 4 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 0.94 | 3.56 | 6.60 | 0.00 | 24.3 | 0.0 |

## GW28

- Train rows: 69689
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Emmanuel Dennis
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 49.23
- Actual score: 35.00
- Transfer: Alexis Mac Allister -> Aaron Lennon (projected gain 3.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David de Gea | GK | 13 | 5.2 | 2.84 | 10.10 | 17.00 | 2.00 | 94.3 | 90.0 |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.18 | 9.51 | 15.47 | 1.00 | 96.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 3.63 | 11.27 | 19.18 | 12.00 | 54.6 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 3.73 | 11.13 | 18.38 | 2.00 | 68.7 | 90.0 |
| XI | XI | Aymeric Laporte | DEF | 12 | 5.8 | 2.87 | 8.92 | 14.40 | 2.00 | 69.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 16 | 4.4 | 3.99 | 8.46 | 12.76 | 1.00 | 83.3 | 180.0 |
| Bench 3 | Bench | Gabriel Magalhães | DEF | 1 | 5.2 | 1.37 | 4.08 | 6.96 | 1.00 | 29.7 | 90.0 |
| Vice Captain | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 5.32 | 12.54 | 19.79 | 4.00 | 122.0 | 180.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.5 | 2.87 | 9.91 | 16.51 | 2.00 | 87.2 | 77.0 |
| XI | XI | Neal Maupay | FWD | 4 | 6.5 | 3.22 | 9.65 | 15.99 | 1.00 | 78.1 | 31.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.29 | 18.17 | 30.27 | 3.00 | 79.8 | 78.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.7 | 3.88 | 13.37 | 23.16 | 2.00 | 73.8 | 90.0 |
| XI | XI | Aaron Lennon | MID | 5 | 4.9 | 3.98 | 11.53 | 18.00 | 2.00 | 118.8 | 90.0 |
| Bench 2 | Bench | Manuel Lanzini | MID | 19 | 5.7 | 2.21 | 7.25 | 11.76 | 2.00 | 68.5 | 90.0 |
| Bench 4 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 1.23 | 3.04 | 5.12 | 7.00 | 19.1 | 72.0 |

## GW29

- Train rows: 70403
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.40
- Actual score: 85.00
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Manuel Lanzini -> Dejan Kulusevski (projected gain 5.77, hit 0)
- Autosub: Wout Weghorst replaced Tino Livramento.
- Autosub: Aymeric Laporte replaced Bruno Miguel Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 4.25 | 10.10 | 15.66 | 5.00 | 114.2 | 180.0 |
| Bench 1 | Bench | David de Gea | GK | 13 | 5.2 | 3.09 | 9.42 | 16.15 | 1.00 | 87.1 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 6.73 | 16.86 | 26.28 | 13.00 | 120.3 | 180.0 |
| XI | Bench | Tino Livramento | DEF | 16 | 4.4 | 4.17 | 10.68 | 16.25 | 0.00 | 89.0 | 0.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 3.49 | 10.46 | 17.89 | 9.00 | 66.4 | 90.0 |
| Bench 3 | Autosub In | Aymeric Laporte | DEF | 12 | 5.8 | 3.21 | 9.02 | 14.73 | 6.00 | 75.3 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 3.77 | 8.89 | 13.05 | 7.00 | 96.7 | 180.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.6 | 4.66 | 12.99 | 21.03 | 2.00 | 111.2 | 86.0 |
| Bench 2 | Autosub In | Wout Weghorst | FWD | 5 | 6.5 | 3.24 | 9.85 | 16.40 | 2.00 | 83.0 | 66.0 |
| XI | XI | Neal Maupay | FWD | 4 | 6.5 | 3.78 | 8.90 | 14.30 | 2.00 | 80.4 | 180.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 8.51 | 21.81 | 33.92 | 10.00 | 118.0 | 98.0 |
| XI | XI | Dejan Kulusevski | MID | 17 | 6.2 | 6.57 | 15.60 | 23.21 | 11.00 | 130.0 | 167.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.55 | 13.67 | 23.12 | 0.00 | 78.6 | 0.0 |
| Bench 4 | Bench | Aaron Lennon | MID | 5 | 4.9 | 3.17 | 8.98 | 14.12 | 2.00 | 89.0 | 90.0 |
| XI | XI | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 3.41 | 7.53 | 11.25 | 8.00 | 77.0 | 167.0 |

## GW30

- Train rows: 71117
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.67
- Actual score: 12.00
- Transfer: Aymeric Laporte -> Matthew Cash (projected gain 7.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.62 | 11.24 | 18.37 | 0.00 | 109.4 | 0.0 |
| Bench 1 | Bench | David de Gea | GK | 13 | 5.2 | 2.51 | 8.66 | 14.79 | 0.00 | 73.3 | 0.0 |
| Vice Captain | Bench | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.75 | 17.10 | 28.20 | 0.00 | 105.1 | 0.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 4.78 | 14.80 | 22.77 | 2.00 | 110.2 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 4.27 | 11.83 | 17.67 | 8.00 | 105.3 | 90.0 |
| XI | Bench | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 3.27 | 10.43 | 18.45 | 0.00 | 63.0 | 0.0 |
| Bench 4 | Bench | Tino Livramento | DEF | 16 | 4.4 | 1.03 | 3.98 | 6.74 | 0.00 | 23.6 | 0.0 |
| XI | Bench | Emmanuel Dennis | FWD | 18 | 5.6 | 3.53 | 10.69 | 17.33 | 0.00 | 72.6 | 0.0 |
| XI | Bench | Neal Maupay | FWD | 4 | 6.5 | 3.58 | 10.67 | 17.06 | 0.00 | 82.6 | 0.0 |
| Bench 3 | Bench | Wout Weghorst | FWD | 5 | 6.5 | 2.13 | 7.56 | 12.91 | 0.00 | 55.9 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 12.9 | 6.39 | 19.52 | 31.23 | 0.00 | 75.4 | 0.0 |
| XI | XI | Dejan Kulusevski | MID | 17 | 6.2 | 5.07 | 15.06 | 22.80 | 2.00 | 97.9 | 90.0 |
| XI | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 3.97 | 11.24 | 16.77 | 0.00 | 89.1 | 0.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.05 | 10.63 | 18.29 | 0.00 | 37.3 | 0.0 |
| Bench 2 | Bench | Aaron Lennon | MID | 5 | 4.9 | 2.22 | 7.25 | 11.81 | 0.00 | 66.2 | 0.0 |

## GW31

- Train rows: 71831
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dejan Kulusevski
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 43.32
- Actual score: 52.00
- Transfer: Tino Livramento -> Matt Doherty (projected gain 4.43, hit 0)
- Autosub: Neal Maupay replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 2.31 | 6.28 | 10.50 | 6.00 | 61.3 | 90.0 |
| Bench 1 | Bench | David de Gea | GK | 13 | 5.1 | 1.97 | 5.55 | 9.50 | 2.00 | 48.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.28 | 10.36 | 18.41 | 0.00 | 40.3 | 0.0 |
| XI | XI | Matt Doherty | DEF | 17 | 4.8 | 3.27 | 10.06 | 15.60 | 14.00 | 72.2 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 3.77 | 10.03 | 15.84 | 6.00 | 58.1 | 90.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 2.37 | 8.98 | 15.90 | 1.00 | 69.7 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 2.88 | 8.27 | 13.46 | 1.00 | 79.0 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.4 | 3.24 | 7.94 | 11.89 | 3.00 | 78.3 | 159.0 |
| Bench 3 | Bench | Emmanuel Dennis | FWD | 18 | 5.5 | 1.98 | 7.45 | 12.17 | 1.00 | 49.9 | 12.0 |
| Bench 2 | Autosub In | Neal Maupay | FWD | 4 | 6.5 | 2.29 | 6.00 | 9.74 | 0.00 | 40.1 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.14 | 17.51 | 27.87 | 3.00 | 57.9 | 68.0 |
| Vice Captain | XI | Dejan Kulusevski | MID | 17 | 6.2 | 4.13 | 12.25 | 18.82 | 6.00 | 74.5 | 75.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.33 | 10.17 | 17.10 | 5.00 | 44.2 | 90.0 |
| XI | XI | Aaron Lennon | MID | 5 | 4.8 | 2.46 | 5.96 | 8.96 | 4.00 | 74.3 | 174.0 |
| Bench 4 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 1.68 | 5.00 | 8.42 | 1.00 | 33.5 | 45.0 |

## GW32

- Train rows: 72551
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 47.69
- Actual score: 40.00
- Transfer: David de Gea -> Nick Pope (projected gain 2.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 5 | 5.4 | 3.80 | 10.15 | 16.34 | 2.00 | 104.0 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 2.73 | 8.13 | 13.67 | 2.00 | 85.7 | 90.0 |
| XI | XI | Matt Doherty | DEF | 17 | 4.8 | 3.79 | 11.07 | 16.61 | 1.00 | 82.4 | 20.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 3.47 | 10.61 | 17.65 | 5.00 | 72.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.00 | 10.22 | 18.47 | 4.00 | 50.6 | 90.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 3.17 | 9.99 | 15.55 | 0.00 | 80.8 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 3.66 | 9.19 | 15.07 | 1.00 | 85.0 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.4 | 3.56 | 9.55 | 15.57 | 1.00 | 81.1 | 55.0 |
| Bench 2 | Bench | Emmanuel Dennis | FWD | 18 | 5.5 | 2.77 | 7.54 | 12.96 | 1.00 | 48.2 | 51.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 6.4 | 2.23 | 6.85 | 11.70 | 0.00 | 54.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 5.56 | 16.73 | 28.37 | 5.00 | 74.7 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.64 | 12.94 | 21.27 | 2.00 | 70.1 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 17 | 6.2 | 3.98 | 11.35 | 17.80 | 12.00 | 73.3 | 83.0 |
| XI | XI | Aaron Lennon | MID | 5 | 4.8 | 3.50 | 8.93 | 14.24 | 2.00 | 94.2 | 63.0 |
| Bench 3 | Bench | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 2.67 | 6.67 | 10.97 | 2.00 | 49.2 | 73.0 |

## GW33

- Train rows: 73273
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.68
- Actual score: 106.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.97) beats the best remaining Bench Boost opportunity (16.08).
- Transfer: Matt Doherty -> Fabian Schär (projected gain 3.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.97) beats the best remaining Bench Boost opportunity (16.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 5 | 5.4 | 4.09 | 9.23 | 14.43 | 10.00 | 110.6 | 180.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 4 | 4.5 | 3.59 | 8.99 | 14.08 | 7.00 | 105.1 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.20 | 12.82 | 20.57 | 6.00 | 71.1 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 4.66 | 12.67 | 20.06 | 6.00 | 81.3 | 90.0 |
| XI | XI | Fabian Schär | DEF | 14 | 4.4 | 5.13 | 11.18 | 16.09 | 9.00 | 114.5 | 180.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.3 | 4.43 | 9.78 | 14.73 | 2.00 | 103.6 | 180.0 |
| Bench 3 | Bench Boost | Matthew Cash | DEF | 2 | 5.2 | 2.50 | 8.47 | 13.61 | 0.00 | 61.4 | 0.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.4 | 3.94 | 8.92 | 14.28 | 10.00 | 89.5 | 167.0 |
| Bench 2 | Bench Boost | Emmanuel Dennis | FWD | 18 | 5.4 | 2.77 | 7.85 | 13.15 | 8.00 | 52.9 | 90.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 6.4 | 2.33 | 5.33 | 8.85 | 1.00 | 50.9 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 5.94 | 17.58 | 29.33 | 19.00 | 77.9 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 5.88 | 15.05 | 24.29 | 3.00 | 112.4 | 180.0 |
| XI | XI | Dejan Kulusevski | MID | 17 | 6.3 | 4.40 | 12.14 | 19.29 | 2.00 | 77.0 | 63.0 |
| XI | XI | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 3.43 | 7.48 | 10.70 | 3.00 | 73.2 | 110.0 |
| XI | XI | Aaron Lennon | MID | 5 | 4.8 | 3.45 | 7.38 | 11.38 | 1.00 | 90.9 | 24.0 |

## GW34

- Train rows: 73999
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.12
- Actual score: 48.00
- Transfer: Dejan Kulusevski -> Bukayo Saka (projected gain 5.24, hit 0)
- Autosub: Aaron Lennon replaced Fabian Schär.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Nick Pope | GK | 5 | 5.4 | 4.29 | 12.57 | 20.34 | 10.00 | 128.6 | 90.0 |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 4.64 | 12.29 | 19.29 | 2.00 | 116.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.04 | 14.16 | 22.74 | 5.00 | 84.5 | 90.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 5.06 | 13.64 | 21.87 | 1.00 | 87.8 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.3 | 3.92 | 10.95 | 17.21 | 2.00 | 105.0 | 90.0 |
| XI | Bench | Fabian Schär | DEF | 14 | 4.4 | 3.65 | 10.06 | 16.30 | 0.00 | 100.9 | 0.0 |
| Bench 3 | Bench | Matthew Cash | DEF | 2 | 5.2 | 1.83 | 4.82 | 7.72 | 6.00 | 38.7 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.4 | 3.93 | 11.32 | 18.53 | 5.00 | 102.3 | 90.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.4 | 2.98 | 9.50 | 16.18 | 5.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 6.3 | 1.60 | 4.84 | 8.74 | 2.00 | 24.9 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.80 | 21.42 | 35.18 | 6.00 | 105.4 | 90.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 6.78 | 17.17 | 27.34 | 1.00 | 133.1 | 173.0 |
| XI | XI | Bukayo Saka | MID | 1 | 6.8 | 5.48 | 14.71 | 23.20 | 13.00 | 102.0 | 73.0 |
| XI | XI | Gabriel Teodoro Martinelli Silva | MID | 1 | 5.3 | 3.04 | 8.34 | 12.66 | 1.00 | 64.4 | 26.0 |
| Bench 2 | Autosub In | Aaron Lennon | MID | 5 | 4.8 | 1.91 | 5.66 | 9.49 | 1.00 | 55.2 | 19.0 |

## GW35

- Train rows: 74727
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Miguel Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.88
- Actual score: 45.00
- Transfer: Gabriel Teodoro Martinelli Silva -> N'Golo Kanté (projected gain 3.63, hit 0)
- Autosub: Aaron Lennon replaced Trent Alexander-Arnold.
- Autosub: Fabian Schär replaced N'Golo Kanté.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 5 | 5.4 | 3.84 | 10.66 | 17.54 | 2.00 | 97.5 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.09 | 9.42 | 15.26 | 6.00 | 92.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.92 | 14.04 | 23.22 | 0.00 | 91.9 | 0.0 |
| XI | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.6 | 4.65 | 13.23 | 21.38 | 5.00 | 89.9 | 90.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 3.73 | 9.06 | 14.17 | 6.00 | 78.7 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.3 | 3.09 | 9.05 | 14.26 | 11.00 | 84.8 | 90.0 |
| Bench 4 | Autosub In | Fabian Schär | DEF | 14 | 4.4 | 1.54 | 5.55 | 9.59 | 2.00 | 53.4 | 60.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.4 | 4.13 | 11.27 | 18.37 | 2.00 | 88.7 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.4 | 4.04 | 10.65 | 17.21 | 1.00 | 80.9 | 59.0 |
| Bench 2 | Bench | Neal Maupay | FWD | 4 | 6.3 | 2.16 | 6.72 | 11.22 | 0.00 | 53.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.73 | 19.93 | 33.54 | 1.00 | 107.6 | 21.0 |
| Vice Captain | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 5.85 | 16.66 | 26.87 | 8.00 | 118.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 6.8 | 4.33 | 12.57 | 20.49 | 4.00 | 74.4 | 86.0 |
| XI | Bench | N'Golo Kanté | MID | 6 | 4.9 | 3.83 | 10.33 | 16.10 | 0.00 | 94.4 | 0.0 |
| Bench 3 | Autosub In | Aaron Lennon | MID | 5 | 4.7 | 1.92 | 5.23 | 8.64 | 2.00 | 41.9 | 88.0 |

## GW36

- Train rows: 75457
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.63
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.13) beats the best remaining Triple Captain opportunity (11.18).
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Neal Maupay -> Teemu Pukki (projected gain 2.66, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (13.13) beats the best remaining Triple Captain opportunity (11.18).
- Autosub: Wout Weghorst replaced N'Golo Kanté.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 4 | 4.5 | 3.66 | 10.38 | 16.47 | 7.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 5 | 5.3 | 3.14 | 9.30 | 15.32 | 2.00 | 90.6 | 90.0 |
| Vice Captain | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.7 | 6.38 | 15.43 | 23.80 | 14.00 | 120.4 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.19 | 12.70 | 20.17 | 4.00 | 89.8 | 180.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.3 | 4.58 | 10.82 | 16.89 | 2.00 | 120.6 | 165.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 4.05 | 9.16 | 13.93 | 3.00 | 95.6 | 180.0 |
| Bench 4 | Bench | Fabian Schär | DEF | 14 | 4.2 | 1.26 | 5.75 | 9.97 | 0.00 | 59.9 | 0.0 |
| XI | XI | Emmanuel Dennis | FWD | 18 | 5.5 | 5.44 | 12.48 | 18.89 | 2.00 | 111.7 | 72.0 |
| XI | XI | Teemu Pukki | FWD | 15 | 6.1 | 4.86 | 11.16 | 16.55 | 4.00 | 103.5 | 180.0 |
| Bench 2 | Autosub In | Wout Weghorst | FWD | 5 | 6.3 | 3.22 | 8.61 | 13.99 | 2.00 | 63.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 7.48 | 20.39 | 33.28 | 3.00 | 116.8 | 108.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 5.32 | 15.70 | 25.22 | 2.00 | 99.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 6.7 | 6.32 | 15.43 | 24.14 | 4.00 | 121.0 | 157.0 |
| XI | Bench | N'Golo Kanté | MID | 6 | 4.9 | 3.37 | 7.05 | 10.44 | 0.00 | 72.9 | 0.0 |
| Bench 3 | Bench | Aaron Lennon | MID | 5 | 4.6 | 2.47 | 6.42 | 9.88 | 2.00 | 56.1 | 65.0 |

## GW37

- Train rows: 76191
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Matthew Cash
- Vice captain: João Pedro Cavaco Cancelo
- Effective captain: Matthew Cash
- Chip used: none
- Predicted score: 59.01
- Actual score: 31.00
- Transfer: Nick Pope -> Kasper Schmeichel (projected gain 4.38, hit 0)
- Autosub: N'Golo Kanté replaced Trent Alexander-Arnold.
- Autosub: Fabian Schär replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.0 | 5.73 | 14.21 | 22.04 | 4.00 | 147.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.64 | 10.07 | 16.02 | 3.00 | 87.1 | 90.0 |
| Vice Captain | XI | João Pedro Cavaco Cancelo | DEF | 12 | 6.7 | 6.02 | 16.97 | 26.68 | 1.00 | 116.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.63 | 15.69 | 25.35 | 0.00 | 109.3 | 0.0 |
| Captain | Captain | Matthew Cash | DEF | 2 | 5.2 | 6.47 | 14.58 | 21.75 | 4.00 | 148.7 | 180.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.3 | 3.60 | 10.48 | 16.93 | 2.00 | 103.2 | 72.0 |
| Bench 4 | Autosub In | Fabian Schär | DEF | 14 | 4.2 | 0.63 | 2.54 | 4.83 | 1.00 | 25.8 | 48.0 |
| XI | XI | Teemu Pukki | FWD | 15 | 6.1 | 3.79 | 10.57 | 16.17 | 8.00 | 91.7 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.3 | 4.33 | 10.37 | 15.60 | 2.00 | 98.4 | 31.0 |
| Bench 2 | Bench | Emmanuel Dennis | FWD | 18 | 5.5 | 2.05 | 6.64 | 11.30 | 0.00 | 43.8 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 12.9 | 5.08 | 16.41 | 28.32 | 0.00 | 65.3 | 0.0 |
| XI | Bench | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 4.40 | 13.83 | 22.96 | 0.00 | 77.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 6.7 | 4.53 | 13.22 | 21.04 | 2.00 | 87.3 | 90.0 |
| XI | XI | Aaron Lennon | MID | 5 | 4.6 | 2.97 | 6.64 | 10.19 | 2.00 | 76.9 | 23.0 |
| Bench 3 | Autosub In | N'Golo Kanté | MID | 6 | 4.9 | 1.81 | 4.56 | 7.30 | 1.00 | 32.5 | 71.0 |

## GW38

- Train rows: 76927
- Bank: 0.80 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Cavaco Cancelo
- Vice captain: Bukayo Saka
- Effective captain: João Pedro Cavaco Cancelo
- Chip used: none
- Predicted score: 46.78
- Actual score: 37.00
- Transfer: Fabian Schär -> Connor Roberts (projected gain 5.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Kasper Schmeichel | GK | 9 | 5.0 | 3.85 | 11.05 | 18.02 | 2.00 | 97.6 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 4 | 4.5 | 3.05 | 8.96 | 14.68 | 2.00 | 82.5 | 90.0 |
| Captain | Captain | João Pedro Cavaco Cancelo | DEF | 12 | 6.7 | 5.64 | 15.29 | 24.18 | 1.00 | 97.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.71 | 10.86 | 17.63 | 2.00 | 54.0 | 90.0 |
| XI | XI | Connor Roberts | DEF | 5 | 4.4 | 3.94 | 10.76 | 16.36 | 1.00 | 102.9 | 45.0 |
| XI | XI | Matthew Cash | DEF | 2 | 5.2 | 2.93 | 10.22 | 16.91 | 7.00 | 97.6 | 90.0 |
| XI | XI | Gabriel Magalhães | DEF | 1 | 5.2 | 2.96 | 8.28 | 13.72 | 8.00 | 77.0 | 90.0 |
| XI | XI | Teemu Pukki | FWD | 15 | 6.1 | 3.16 | 9.29 | 14.93 | 2.00 | 79.8 | 90.0 |
| XI | XI | Wout Weghorst | FWD | 5 | 6.2 | 2.66 | 7.89 | 12.57 | 1.00 | 49.9 | 45.0 |
| Bench 4 | Bench | Emmanuel Dennis | FWD | 18 | 5.4 | 0.85 | 4.01 | 7.90 | 0.00 | 20.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 6.7 | 4.95 | 13.04 | 20.36 | 5.00 | 84.8 | 77.0 |
| XI | XI | Mohamed Salah | MID | 11 | 12.8 | 3.60 | 12.77 | 23.21 | 6.00 | 24.1 | 32.0 |
| XI | XI | Bruno Miguel Borges Fernandes | MID | 13 | 11.6 | 3.75 | 11.29 | 18.95 | 1.00 | 57.2 | 90.0 |
| Bench 2 | Bench | Aaron Lennon | MID | 5 | 4.6 | 1.93 | 5.43 | 8.82 | 1.00 | 38.9 | 17.0 |
| Bench 3 | Bench | N'Golo Kanté | MID | 6 | 4.9 | 1.73 | 4.38 | 7.13 | 2.00 | 38.7 | 90.0 |