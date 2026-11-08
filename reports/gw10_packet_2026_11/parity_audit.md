# Train/live parity audit: live GW10 (2026-11-06T18:30:00Z) vs GW10 of 2023-24, 2024-25, 2025-26

Live rows 670; historical rows 2152. Subsets: all players, and regulars (minutes_avg_5 > 45).

## all players (live n 670, hist n 2152)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 4.900 | 4.600 | 5.061 | 4.933 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 0.200 | 0.186 | 2.238 | 2.091 | 0.26 | 0.00 | **zero share 0.26 vs 0.00** |
| transfers_in_prev_event | 511.000 | 419.500 | 20240.261 | 15259.897 | 0.16 | 0.20 |  |
| transfers_out_prev_event | 1361.000 | 1045.500 | 20240.261 | 15259.897 | 0.00 | 0.01 |  |
| transfer_balance_prev_event | -196.500 | -172.000 | 0.000 | 0.000 | 0.01 | 0.01 |  |
| home_fixture_count | 0.000 | 0.000 | 0.473 | 0.494 | 0.53 | 0.51 |  |
| away_fixture_count | 1.000 | 1.000 | 0.527 | 0.506 | 0.47 | 0.49 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.090 | 3.036 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.090 | 3.036 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.333 | 1.333 | 1.125 | 1.500 | 0.05 | 0.02 |  |
| team_goals_against_avg_3 | 1.000 | 1.333 | 1.118 | 1.481 | 0.09 | 0.02 |  |
| team_goals_for_avg_5 | 1.200 | 1.600 | 1.316 | 1.488 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.200 | 1.400 | 1.295 | 1.480 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.333 | 1.333 | 1.074 | 1.476 | 0.05 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.000 | 1.333 | 1.083 | 1.469 | 0.12 | 0.02 |  |
| opponent_goals_for_avg_5 | 1.200 | 1.600 | 1.253 | 1.484 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.200 | 1.400 | 1.286 | 1.462 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.100 | -0.200 | -0.017 | -0.012 | 0.00 | 0.00 |  |
| form_x_opp_weakness_3 | 0.000 | 0.000 | 0.137 | -0.032 | 0.24 | 0.29 | **mean ratio -4.31** |
| xgi_x_opp_weakness_3 | 0.000 | 0.000 | 0.007 | -0.000 | 0.51 | 0.55 | **mean ratio -35.14** |
| opp_def_weakness_5 | -0.090 | -0.060 | -0.004 | -0.019 | 0.00 | 0.00 | **mean ratio 0.21** |
| form_x_opp_weakness_5 | 0.000 | 0.000 | 0.032 | 0.022 | 0.22 | 0.27 |  |
| xgi_x_opp_weakness_5 | 0.000 | 0.000 | 0.002 | -0.000 | 0.44 | 0.51 | **mean ratio -4.06** |
| points_avg_1 | 0.928 | 0.653 | 1.493 | 1.349 | 0.31 | 0.36 |  |
| minutes_avg_1 | 0.000 | 0.000 | 29.276 | 27.490 | 0.54 | 0.57 |  |
| appearance_rate_1 | 0.000 | 0.000 | 0.463 | 0.428 | 0.54 | 0.57 |  |
| played_60_rate_1 | 0.000 | 0.000 | 0.309 | 0.289 | 0.69 | 0.71 |  |
| points_avg_3 | 0.973 | 0.667 | 1.530 | 1.376 | 0.24 | 0.29 |  |
| minutes_avg_3 | 7.833 | 2.333 | 29.330 | 27.783 | 0.44 | 0.47 |  |
| appearance_rate_3 | 0.333 | 0.333 | 0.457 | 0.431 | 0.44 | 0.47 |  |
| played_60_rate_3 | 0.000 | 0.000 | 0.307 | 0.290 | 0.59 | 0.62 |  |
| points_avg_5 | 1.000 | 0.800 | 1.554 | 1.358 | 0.22 | 0.27 |  |
| minutes_avg_5 | 12.900 | 6.200 | 29.360 | 27.639 | 0.38 | 0.44 |  |
| appearance_rate_5 | 0.400 | 0.400 | 0.459 | 0.428 | 0.38 | 0.44 |  |
| played_60_rate_5 | 0.000 | 0.000 | 0.309 | 0.287 | 0.53 | 0.57 |  |
| points_avg_8 | 1.125 | 0.881 | 1.562 | 1.371 | 0.19 | 0.25 |  |
| minutes_avg_8 | 13.188 | 11.125 | 29.493 | 27.705 | 0.34 | 0.39 |  |
| appearance_rate_8 | 0.500 | 0.375 | 0.463 | 0.431 | 0.34 | 0.39 |  |
| played_60_rate_8 | 0.125 | 0.000 | 0.309 | 0.288 | 0.49 | 0.52 |  |
| price_change_1 | 0.000 | 0.000 | -0.001 | -0.005 | 0.95 | 0.90 | **mean ratio 0.30** |
| selected_change_1 | -0.008 | -0.001 | -0.001 | 0.000 | 0.00 | 0.00 | **mean ratio -413294089471260.44** |
| home_fixture_ratio | 0.000 | 0.000 | 0.473 | 0.494 | 0.53 | 0.51 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.097 | 0.090 | 0.89 | 0.88 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.095 | 0.089 | 0.82 | 0.83 |  |
| bps_avg_3 | 1.333 | 0.333 | 5.500 | 4.990 | 0.44 | 0.48 |  |
| bps_avg_5 | 2.200 | 0.800 | 5.579 | 4.895 | 0.38 | 0.44 |  |
| influence_avg_3 | 1.000 | 0.067 | 6.115 | 6.332 | 0.47 | 0.50 |  |
| influence_avg_5 | 2.080 | 0.840 | 6.511 | 6.374 | 0.40 | 0.45 |  |
| creativity_avg_3 | 0.167 | 0.000 | 4.693 | 4.404 | 0.47 | 0.52 |  |
| creativity_avg_5 | 0.530 | 0.080 | 4.748 | 4.346 | 0.41 | 0.48 |  |
| threat_avg_3 | 0.000 | 0.000 | 3.842 | 3.934 | 0.55 | 0.59 |  |
| threat_avg_5 | 0.600 | 0.000 | 4.010 | 3.970 | 0.47 | 0.54 |  |
| ict_index_avg_3 | 0.333 | 0.067 | 1.460 | 1.466 | 0.45 | 0.49 |  |
| ict_index_avg_5 | 0.620 | 0.260 | 1.523 | 1.468 | 0.39 | 0.45 |  |
| starts_avg_3 | 0.000 | 0.000 | 0.328 | 0.310 | 0.57 | 0.59 |  |
| starts_avg_5 | 0.000 | 0.000 | 0.329 | 0.309 | 0.51 | 0.55 |  |
| expected_goals_avg_3 | 0.000 | 0.000 | 0.039 | 0.042 | 0.63 | 0.66 |  |
| expected_goals_avg_5 | 0.000 | 0.000 | 0.042 | 0.041 | 0.53 | 0.60 |  |
| expected_assists_avg_3 | 0.000 | 0.000 | 0.026 | 0.027 | 0.54 | 0.58 |  |
| expected_assists_avg_5 | 0.002 | 0.000 | 0.026 | 0.026 | 0.47 | 0.53 |  |
| expected_goal_involvements_avg_3 | 0.000 | 0.000 | 0.065 | 0.069 | 0.51 | 0.55 |  |
| expected_goal_involvements_avg_5 | 0.008 | 0.000 | 0.069 | 0.067 | 0.44 | 0.51 |  |
| expected_goals_conceded_avg_3 | 0.102 | 0.023 | 0.421 | 0.455 | 0.45 | 0.49 |  |
| expected_goals_conceded_avg_5 | 0.189 | 0.106 | 0.458 | 0.443 | 0.39 | 0.45 |  |
| defensive_contribution_avg_3 | 0.333 | 0.000 | 2.364 | 0.734 | 0.49 | 0.84 | **zero share 0.49 vs 0.84; mean ratio 3.22** |
| defensive_contribution_avg_5 | 0.600 | 0.000 | 2.355 | 0.734 | 0.44 | 0.83 | **zero share 0.44 vs 0.83; mean ratio 3.21** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.053 | 0.016 | 0.88 | 0.96 | **mean ratio 3.40** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.055 | 0.017 | 0.83 | 0.95 | **mean ratio 3.28** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.347 | 0.00 | 0.65 | **zero share 0.00 vs 0.65; mean ratio 2.88** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.288 | 0.324 | 0.71 | 0.68 |  |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.288 | 0.324 | 0.71 | 0.68 |  |

## regulars (live n 204, hist n 652)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 5.300 | 5.000 | 5.502 | 5.423 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 2.100 | 1.765 | 6.132 | 5.850 | 0.02 | 0.00 |  |
| transfers_in_prev_event | 10246.000 | 10093.000 | 62899.436 | 45482.790 | 0.00 | 0.00 |  |
| transfers_out_prev_event | 14932.500 | 12634.500 | 40935.113 | 39330.900 | 0.00 | 0.00 |  |
| transfer_balance_prev_event | -684.500 | -78.000 | 21964.324 | 6151.890 | 0.00 | 0.00 | **mean ratio 3.57** |
| home_fixture_count | 1.000 | 0.000 | 0.510 | 0.495 | 0.49 | 0.50 |  |
| away_fixture_count | 0.000 | 1.000 | 0.490 | 0.505 | 0.51 | 0.50 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.020 | 3.012 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.020 | 3.012 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.333 | 1.333 | 1.098 | 1.495 | 0.04 | 0.01 |  |
| team_goals_against_avg_3 | 1.000 | 1.333 | 1.085 | 1.466 | 0.10 | 0.02 |  |
| team_goals_for_avg_5 | 1.200 | 1.600 | 1.286 | 1.486 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.200 | 1.400 | 1.275 | 1.475 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.333 | 1.333 | 1.105 | 1.492 | 0.05 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.000 | 1.333 | 1.101 | 1.476 | 0.09 | 0.02 |  |
| opponent_goals_for_avg_5 | 1.200 | 1.600 | 1.305 | 1.495 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.200 | 1.400 | 1.287 | 1.478 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.100 | -0.200 | 0.001 | -0.008 | 0.00 | 0.00 | **mean ratio -0.17** |
| form_x_opp_weakness_3 | -0.383 | -0.400 | 0.296 | -0.038 | 0.00 | 0.01 | **mean ratio -7.70** |
| xgi_x_opp_weakness_3 | -0.002 | -0.005 | 0.021 | -0.002 | 0.06 | 0.08 | **mean ratio -10.11** |
| opp_def_weakness_5 | -0.090 | -0.060 | -0.003 | -0.006 | 0.00 | 0.00 | **mean ratio 0.45** |
| form_x_opp_weakness_5 | -0.207 | -0.252 | 0.050 | 0.071 | 0.00 | 0.00 |  |
| xgi_x_opp_weakness_5 | -0.003 | -0.003 | 0.009 | -0.003 | 0.05 | 0.06 | **mean ratio -3.48** |
| points_avg_1 | 2.000 | 2.000 | 3.219 | 2.904 | 0.09 | 0.11 |  |
| minutes_avg_1 | 90.000 | 90.000 | 73.451 | 71.985 | 0.08 | 0.08 |  |
| appearance_rate_1 | 1.000 | 1.000 | 0.917 | 0.919 | 0.08 | 0.08 |  |
| played_60_rate_1 | 1.000 | 1.000 | 0.833 | 0.798 | 0.17 | 0.20 |  |
| points_avg_3 | 3.000 | 2.667 | 3.372 | 3.096 | 0.00 | 0.01 |  |
| minutes_avg_3 | 85.000 | 83.167 | 76.054 | 75.775 | 0.00 | 0.00 |  |
| appearance_rate_3 | 1.000 | 1.000 | 0.943 | 0.953 | 0.00 | 0.00 |  |
| played_60_rate_3 | 1.000 | 1.000 | 0.850 | 0.843 | 0.00 | 0.02 |  |
| points_avg_5 | 3.200 | 2.800 | 3.409 | 3.072 | 0.00 | 0.00 |  |
| minutes_avg_5 | 78.100 | 78.200 | 75.944 | 75.406 | 0.00 | 0.00 |  |
| appearance_rate_5 | 1.000 | 1.000 | 0.940 | 0.950 | 0.00 | 0.00 |  |
| played_60_rate_5 | 1.000 | 0.800 | 0.847 | 0.835 | 0.00 | 0.00 |  |
| points_avg_8 | 3.250 | 2.875 | 3.358 | 3.006 | 0.00 | 0.00 |  |
| minutes_avg_8 | 77.688 | 75.625 | 73.768 | 71.540 | 0.00 | 0.00 |  |
| appearance_rate_8 | 1.000 | 1.000 | 0.926 | 0.918 | 0.00 | 0.00 |  |
| played_60_rate_8 | 0.875 | 0.875 | 0.824 | 0.788 | 0.00 | 0.00 |  |
| price_change_1 | 0.000 | 0.000 | 0.002 | -0.001 | 0.92 | 0.84 | **mean ratio -2.66** |
| selected_change_1 | -0.015 | -0.004 | 0.036 | 0.042 | 0.00 | 0.00 |  |
| home_fixture_ratio | 1.000 | 0.000 | 0.510 | 0.495 | 0.49 | 0.50 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.270 | 0.261 | 0.69 | 0.67 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.267 | 0.263 | 0.53 | 0.53 |  |
| bps_avg_3 | 12.833 | 12.667 | 14.054 | 13.307 | 0.00 | 0.00 |  |
| bps_avg_5 | 13.800 | 12.400 | 14.155 | 13.186 | 0.00 | 0.00 |  |
| influence_avg_3 | 14.900 | 15.933 | 15.881 | 17.210 | 0.00 | 0.00 |  |
| influence_avg_5 | 16.540 | 16.220 | 16.835 | 17.532 | 0.00 | 0.00 |  |
| creativity_avg_3 | 9.733 | 8.967 | 11.889 | 11.721 | 0.07 | 0.08 |  |
| creativity_avg_5 | 9.590 | 9.370 | 11.893 | 11.607 | 0.06 | 0.07 |  |
| threat_avg_3 | 5.667 | 6.333 | 9.456 | 10.183 | 0.13 | 0.14 |  |
| threat_avg_5 | 6.800 | 7.000 | 9.709 | 10.428 | 0.11 | 0.10 |  |
| ict_index_avg_3 | 3.233 | 3.400 | 3.717 | 3.910 | 0.00 | 0.00 |  |
| ict_index_avg_5 | 3.420 | 3.400 | 3.839 | 3.956 | 0.00 | 0.00 |  |
| starts_avg_3 | 1.000 | 1.000 | 0.881 | 0.878 | 0.00 | 0.01 |  |
| starts_avg_5 | 1.000 | 1.000 | 0.877 | 0.870 | 0.00 | 0.00 |  |
| expected_goals_avg_3 | 0.045 | 0.043 | 0.097 | 0.109 | 0.25 | 0.23 |  |
| expected_goals_avg_5 | 0.051 | 0.057 | 0.105 | 0.108 | 0.15 | 0.15 |  |
| expected_assists_avg_3 | 0.043 | 0.037 | 0.066 | 0.074 | 0.08 | 0.10 |  |
| expected_assists_avg_5 | 0.041 | 0.049 | 0.065 | 0.072 | 0.05 | 0.07 |  |
| expected_goal_involvements_avg_3 | 0.097 | 0.117 | 0.163 | 0.183 | 0.06 | 0.08 |  |
| expected_goal_involvements_avg_5 | 0.111 | 0.126 | 0.170 | 0.180 | 0.05 | 0.06 |  |
| expected_goals_conceded_avg_3 | 0.970 | 1.102 | 1.050 | 1.207 | 0.00 | 0.00 |  |
| expected_goals_conceded_avg_5 | 1.050 | 1.126 | 1.147 | 1.183 | 0.00 | 0.00 |  |
| defensive_contribution_avg_3 | 5.667 | 0.000 | 5.895 | 1.946 | 0.10 | 0.70 | **zero share 0.10 vs 0.70; mean ratio 3.03** |
| defensive_contribution_avg_5 | 5.800 | 0.000 | 5.829 | 1.963 | 0.10 | 0.70 | **zero share 0.10 vs 0.70; mean ratio 2.97** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.147 | 0.048 | 0.68 | 0.89 | **mean ratio 3.09** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.151 | 0.051 | 0.58 | 0.85 | **zero share 0.58 vs 0.85; mean ratio 2.95** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.330 | 0.00 | 0.67 | **zero share 0.00 vs 0.67; mean ratio 3.03** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.059 | 0.077 | 0.94 | 0.92 |  |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.059 | 0.077 | 0.94 | 0.92 |  |

Flags: 24 (a flag is a prompt to look, not a verdict; schedule-driven features legitimately differ by week).
