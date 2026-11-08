# Transfer-gain calibration (projected vs realised)

Candidates = every transfer the engine listed with a positive projected gain (top 5 per week, 3GW squad-score horizon, net of hits);
applied = the one it took. Realised = label points in minus out over the same horizon (lineup effects ignored).

## MP1_F: 53 candidates in 21 windows, 53 applied, 0 hits taken

- 1gw: forecast difference in−out mean +2.45, realised +3.19; slope realised-on-forecast 1.21 ± 0.52
- 3gw: forecast difference in−out mean +5.29, realised +5.15; slope realised-on-forecast 1.22 ± 0.43
- 5gw: forecast difference in−out mean +6.98, realised +7.19; slope realised-on-forecast 0.97 ± 0.39
- engine projected_gain vs realised 3GW difference: slope 1.16 ± 0.49; corr 0.32

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 4 | 4 | +0.32 | +0.20 | -3.25 | +2.75 | -2.25 |
| (1, 2] | 5 | 5 | +1.28 | +3.21 | +2.20 | +2.00 | +0.80 |
| (2, 3] | 7 | 7 | +2.50 | +2.84 | +7.00 | +3.57 | +11.79 |
| (3, 5] | 19 | 19 | +4.21 | +4.67 | +3.21 | +2.95 | +4.97 |
| (5, 8] | 11 | 11 | +6.51 | +7.50 | +8.00 | +3.64 | +10.27 |
| (8, 99] | 7 | 7 | +9.84 | +10.37 | +11.00 | +3.86 | +13.71 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 53 | +4.63 | +5.29 | +5.15 ± 1.44 | +5.15 |
| rank 0 (best option) | 53 | +4.63 | +5.29 | +5.15 ± 1.44 | +5.15 |

## MN_F: 54 candidates in 21 windows, 54 applied, 0 hits taken

- 1gw: forecast difference in−out mean +2.56, realised +2.94; slope realised-on-forecast 0.73 ± 0.49
- 3gw: forecast difference in−out mean +5.25, realised +4.43; slope realised-on-forecast 1.18 ± 0.42
- 5gw: forecast difference in−out mean +6.87, realised +7.31; slope realised-on-forecast 0.94 ± 0.39
- engine projected_gain vs realised 3GW difference: slope 1.00 ± 0.47; corr 0.28

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 4 | 4 | +0.31 | +0.20 | -3.25 | +2.75 | -2.25 |
| (1, 2] | 6 | 6 | +1.35 | +3.24 | +2.17 | +1.67 | +2.17 |
| (2, 3] | 8 | 8 | +2.49 | +2.94 | +7.00 | +4.88 | +12.12 |
| (3, 5] | 18 | 18 | +4.20 | +4.60 | +1.44 | +1.78 | +3.94 |
| (5, 8] | 11 | 11 | +6.41 | +7.65 | +7.27 | +3.64 | +11.55 |
| (8, 99] | 7 | 7 | +10.03 | +10.37 | +11.00 | +3.86 | +13.71 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 54 | +4.55 | +5.25 | +4.43 ± 1.40 | +4.43 |
| rank 0 (best option) | 54 | +4.55 | +5.25 | +4.43 ± 1.40 | +4.43 |

## ST1_F: 49 candidates in 21 windows, 49 applied, 0 hits taken

- 1gw: forecast difference in−out mean +2.41, realised +3.14; slope realised-on-forecast 0.87 ± 0.51
- 3gw: forecast difference in−out mean +5.34, realised +5.69; slope realised-on-forecast 1.06 ± 0.44
- 5gw: forecast difference in−out mean +7.03, realised +5.83; slope realised-on-forecast 0.99 ± 0.48
- engine projected_gain vs realised 3GW difference: slope 0.99 ± 0.45; corr 0.31

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 6 | 6 | +0.48 | +1.15 | +0.00 | +2.50 | +1.33 |
| (1, 2] | 7 | 7 | +1.45 | +2.42 | -0.57 | +2.43 | -3.19 |
| (2, 3] | 2 | 2 | +2.25 | +3.29 | +8.50 | +4.50 | +11.25 |
| (3, 5] | 15 | 15 | +4.06 | +4.90 | +8.53 | +4.13 | +9.47 |
| (5, 8] | 10 | 10 | +6.25 | +7.04 | +6.20 | +3.00 | +5.15 |
| (8, 99] | 9 | 9 | +9.73 | +9.71 | +8.44 | +2.33 | +9.33 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 49 | +4.66 | +5.34 | +5.69 ± 1.44 | +5.69 |
| rank 0 (best option) | 49 | +4.66 | +5.34 | +5.69 ± 1.44 | +5.69 |

## STN_F: 51 candidates in 21 windows, 51 applied, 0 hits taken

- 1gw: forecast difference in−out mean +2.52, realised +2.33; slope realised-on-forecast 0.37 ± 0.47
- 3gw: forecast difference in−out mean +5.16, realised +4.57; slope realised-on-forecast 0.97 ± 0.44
- 5gw: forecast difference in−out mean +6.77, realised +5.37; slope realised-on-forecast 0.72 ± 0.48
- engine projected_gain vs realised 3GW difference: slope 0.71 ± 0.48; corr 0.21

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 5 | 5 | +0.39 | +0.27 | -2.40 | +2.40 | -1.60 |
| (1, 2] | 7 | 7 | +1.51 | +2.42 | -0.57 | +2.43 | -3.19 |
| (2, 3] | 6 | 6 | +2.38 | +3.24 | +7.50 | +3.17 | +13.83 |
| (3, 5] | 16 | 16 | +4.26 | +5.48 | +7.00 | +2.12 | +8.81 |
| (5, 8] | 11 | 11 | +6.51 | +7.25 | +4.73 | +2.82 | +5.09 |
| (8, 99] | 6 | 6 | +10.16 | +9.69 | +6.67 | +1.00 | +4.00 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 51 | +4.46 | +5.16 | +4.57 ± 1.41 | +4.57 |
| rank 0 (best option) | 51 | +4.46 | +5.16 | +4.57 ± 1.41 | +4.57 |

## HT2_F: 92 candidates in 21 windows, 48 applied, 4 hits taken

- 1gw: forecast difference in−out mean +3.26, realised +2.59; slope realised-on-forecast 0.93 ± 0.32
- 3gw: forecast difference in−out mean +7.25, realised +4.89; slope realised-on-forecast 1.47 ± 0.28
- 5gw: forecast difference in−out mean +9.60, realised +7.17; slope realised-on-forecast 1.33 ± 0.27
- engine projected_gain vs realised 3GW difference: slope 1.61 ± 0.32; corr 0.46

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 8 | 4 | +0.33 | +2.42 | -1.50 | -0.38 | -2.62 |
| (1, 2] | 13 | 6 | +1.63 | +4.26 | -0.77 | +0.69 | +2.28 |
| (2, 3] | 7 | 3 | +2.65 | +5.60 | -2.00 | +1.43 | -1.04 |
| (3, 5] | 18 | 9 | +4.08 | +4.43 | +4.92 | +2.28 | +4.37 |
| (5, 8] | 23 | 13 | +6.15 | +6.85 | -0.09 | -0.78 | +2.76 |
| (8, 99] | 23 | 13 | +11.36 | +13.72 | +17.35 | +8.65 | +22.43 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 44 | +5.71 | +6.90 | +5.93 ± 2.08 | +5.93 |
| applied, hit | 4 | +8.10 | +13.83 | +11.75 ± 12.02 | +7.75 |
| not applied, free | 39 | +5.18 | +6.38 | +3.08 ± 2.23 | +3.08 |
| not applied, hit | 5 | +6.54 | +11.81 | +4.30 ± 4.47 | +0.30 |
| rank 0 (best option) | 48 | +5.91 | +7.48 | +6.42 ± 2.11 | +6.08 |
| 2-transfer options | 50 | +7.24 | +9.45 | +8.21 ± 2.26 | +7.49 |

## HT2G_F: 94 candidates in 21 windows, 39 applied, 3 hits taken

- 1gw: forecast difference in−out mean +3.37, realised +3.03; slope realised-on-forecast 1.34 ± 0.28
- 3gw: forecast difference in−out mean +7.26, realised +5.44; slope realised-on-forecast 1.50 ± 0.27
- 5gw: forecast difference in−out mean +9.58, realised +8.21; slope realised-on-forecast 1.32 ± 0.26
- engine projected_gain vs realised 3GW difference: slope 1.54 ± 0.32; corr 0.45

| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |
|---|---|---|---|---|---|---|---|
| (-99, 1] | 11 | 0 | +0.32 | +2.19 | -4.09 | +1.36 | -2.91 |
| (1, 2] | 10 | 0 | +1.73 | +4.18 | +0.20 | -1.20 | +2.47 |
| (2, 3] | 6 | 2 | +2.77 | +5.40 | +7.00 | +1.50 | +8.79 |
| (3, 5] | 17 | 9 | +4.14 | +4.56 | +5.68 | +2.59 | +5.69 |
| (5, 8] | 27 | 15 | +6.10 | +7.08 | +0.63 | +1.11 | +4.20 |
| (8, 99] | 23 | 13 | +11.36 | +13.72 | +17.35 | +8.65 | +22.43 |

| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |
|---|---|---|---|---|---|
| applied, free | 36 | +7.02 | +7.89 | +6.44 ± 2.16 | +6.44 |
| applied, hit | 3 | +9.97 | +15.75 | +23.67 ± 2.19 | +19.67 |
| not applied, free | 50 | +4.37 | +5.84 | +3.74 ± 2.04 | +3.74 |
| not applied, hit | 5 | +6.54 | +11.81 | +4.30 ± 4.47 | +0.30 |
| rank 0 (best option) | 49 | +5.97 | +7.42 | +6.49 ± 2.09 | +6.24 |
| 2-transfer options | 56 | +6.99 | +9.03 | +8.10 ± 2.10 | +7.53 |

