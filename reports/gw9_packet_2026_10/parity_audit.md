# Train/live parity audit: live GW9 (2026-10-31T11:00:00Z) vs GW9 of 2023-24, 2024-25, 2025-26

Live rows 669; historical rows 2146. Subsets: all players, and regulars (minutes_avg_5 > 45).

## all players (live n 669, hist n 2146)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 4.900 | 4.600 | 5.066 | 4.940 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 0.200 | 0.185 | 2.240 | 2.097 | 0.26 | 0.00 | **zero share 0.26 vs 0.00** |
| transfers_in_prev_event | 497.000 | 577.500 | 14498.845 | 20796.597 | 0.16 | 0.20 |  |
| transfers_out_prev_event | 1264.000 | 1539.500 | 14498.845 | 20796.597 | 0.00 | 0.01 |  |
| transfer_balance_prev_event | -137.000 | -255.000 | 0.000 | 0.000 | 0.01 | 0.01 |  |
| home_fixture_count | 1.000 | 1.000 | 0.526 | 0.507 | 0.47 | 0.49 |  |
| away_fixture_count | 0.000 | 0.000 | 0.474 | 0.493 | 0.53 | 0.51 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.033 | 2.990 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.033 | 2.990 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.333 | 1.667 | 1.376 | 1.494 | 0.05 | 0.02 |  |
| team_goals_against_avg_3 | 1.333 | 1.333 | 1.345 | 1.491 | 0.00 | 0.02 |  |
| team_goals_for_avg_5 | 1.200 | 1.400 | 1.393 | 1.430 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.400 | 1.400 | 1.380 | 1.436 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.333 | 1.333 | 1.356 | 1.474 | 0.06 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.333 | 1.333 | 1.355 | 1.483 | 0.00 | 0.02 |  |
| opponent_goals_for_avg_5 | 1.200 | 1.400 | 1.371 | 1.425 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.400 | 1.400 | 1.377 | 1.443 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.017 | -0.083 | 0.005 | -0.004 | 0.00 | 0.00 |  |
| form_x_opp_weakness_3 | 0.000 | 0.000 | -0.007 | -0.041 | 0.23 | 0.28 | **mean ratio 0.17** |
| xgi_x_opp_weakness_3 | 0.000 | 0.000 | -0.004 | -0.005 | 0.50 | 0.55 |  |
| opp_def_weakness_5 | 0.030 | 0.060 | 0.007 | 0.005 | 0.00 | 0.00 |  |
| form_x_opp_weakness_5 | 0.001 | 0.000 | -0.062 | -0.034 | 0.21 | 0.27 |  |
| xgi_x_opp_weakness_5 | 0.000 | 0.000 | -0.004 | -0.003 | 0.45 | 0.51 |  |
| points_avg_1 | 0.789 | 0.677 | 1.582 | 1.360 | 0.33 | 0.35 |  |
| minutes_avg_1 | 0.000 | 0.000 | 29.469 | 27.548 | 0.55 | 0.58 |  |
| appearance_rate_1 | 0.000 | 0.000 | 0.453 | 0.423 | 0.55 | 0.58 |  |
| played_60_rate_1 | 0.000 | 0.000 | 0.314 | 0.288 | 0.69 | 0.71 |  |
| points_avg_3 | 1.000 | 0.667 | 1.556 | 1.381 | 0.23 | 0.28 |  |
| minutes_avg_3 | 8.000 | 1.667 | 29.408 | 27.832 | 0.42 | 0.48 |  |
| appearance_rate_3 | 0.333 | 0.333 | 0.460 | 0.430 | 0.42 | 0.48 |  |
| played_60_rate_3 | 0.000 | 0.000 | 0.307 | 0.289 | 0.57 | 0.63 |  |
| points_avg_5 | 1.057 | 0.843 | 1.593 | 1.383 | 0.21 | 0.27 |  |
| minutes_avg_5 | 11.000 | 6.500 | 29.409 | 27.735 | 0.37 | 0.44 |  |
| appearance_rate_5 | 0.400 | 0.400 | 0.459 | 0.429 | 0.37 | 0.44 |  |
| played_60_rate_5 | 0.000 | 0.000 | 0.306 | 0.288 | 0.53 | 0.57 |  |
| points_avg_8 | 1.167 | 0.951 | 1.600 | 1.393 | 0.19 | 0.25 |  |
| minutes_avg_8 | 14.750 | 11.250 | 29.712 | 27.940 | 0.33 | 0.39 |  |
| appearance_rate_8 | 0.500 | 0.375 | 0.467 | 0.435 | 0.33 | 0.39 |  |
| played_60_rate_8 | 0.125 | 0.000 | 0.311 | 0.291 | 0.48 | 0.51 |  |
| price_change_1 | 0.000 | 0.000 | -0.003 | -0.003 | 0.94 | 0.92 |  |
| selected_change_1 | -0.008 | -0.001 | -0.002 | -0.000 | 0.00 | 0.00 | **mean ratio 4360.84** |
| home_fixture_ratio | 1.000 | 1.000 | 0.526 | 0.507 | 0.47 | 0.49 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.096 | 0.091 | 0.88 | 0.89 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.094 | 0.090 | 0.82 | 0.83 |  |
| bps_avg_3 | 1.667 | 0.333 | 5.478 | 4.896 | 0.42 | 0.48 |  |
| bps_avg_5 | 1.800 | 0.800 | 5.605 | 4.916 | 0.38 | 0.44 |  |
| influence_avg_3 | 1.267 | 0.067 | 6.510 | 6.379 | 0.45 | 0.50 |  |
| influence_avg_5 | 1.960 | 0.840 | 6.629 | 6.356 | 0.39 | 0.45 |  |
| creativity_avg_3 | 0.233 | 0.000 | 4.626 | 4.402 | 0.45 | 0.52 |  |
| creativity_avg_5 | 0.520 | 0.100 | 4.728 | 4.355 | 0.40 | 0.48 |  |
| threat_avg_3 | 0.000 | 0.000 | 4.005 | 4.000 | 0.53 | 0.59 |  |
| threat_avg_5 | 0.400 | 0.000 | 4.027 | 3.979 | 0.47 | 0.54 |  |
| ict_index_avg_3 | 0.467 | 0.067 | 1.511 | 1.477 | 0.43 | 0.49 |  |
| ict_index_avg_5 | 0.600 | 0.290 | 1.536 | 1.468 | 0.38 | 0.45 |  |
| starts_avg_3 | 0.000 | 0.000 | 0.329 | 0.311 | 0.56 | 0.60 |  |
| starts_avg_5 | 0.000 | 0.000 | 0.329 | 0.310 | 0.52 | 0.55 |  |
| expected_goals_avg_3 | 0.000 | 0.000 | 0.040 | 0.042 | 0.61 | 0.65 |  |
| expected_goals_avg_5 | 0.000 | 0.000 | 0.042 | 0.041 | 0.54 | 0.59 |  |
| expected_assists_avg_3 | 0.000 | 0.000 | 0.026 | 0.027 | 0.54 | 0.58 |  |
| expected_assists_avg_5 | 0.002 | 0.000 | 0.027 | 0.027 | 0.48 | 0.53 |  |
| expected_goal_involvements_avg_3 | 0.000 | 0.000 | 0.066 | 0.069 | 0.50 | 0.55 |  |
| expected_goal_involvements_avg_5 | 0.008 | 0.000 | 0.069 | 0.067 | 0.45 | 0.51 |  |
| expected_goals_conceded_avg_3 | 0.103 | 0.018 | 0.439 | 0.460 | 0.43 | 0.49 |  |
| expected_goals_conceded_avg_5 | 0.172 | 0.112 | 0.455 | 0.441 | 0.38 | 0.45 |  |
| defensive_contribution_avg_3 | 0.333 | 0.000 | 2.354 | 0.731 | 0.48 | 0.85 | **zero share 0.48 vs 0.85; mean ratio 3.22** |
| defensive_contribution_avg_5 | 0.600 | 0.000 | 2.319 | 0.723 | 0.43 | 0.83 | **zero share 0.43 vs 0.83; mean ratio 3.21** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.057 | 0.017 | 0.87 | 0.96 | **mean ratio 3.35** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.055 | 0.018 | 0.83 | 0.95 | **mean ratio 3.12** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.348 | 0.00 | 0.65 | **zero share 0.00 vs 0.65; mean ratio 2.88** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.296 | 0.331 | 0.70 | 0.67 |  |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.296 | 0.331 | 0.70 | 0.67 |  |

## regulars (live n 209, hist n 646)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 5.300 | 5.000 | 5.492 | 5.446 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 1.900 | 1.959 | 6.139 | 5.878 | 0.01 | 0.00 |  |
| transfers_in_prev_event | 9978.000 | 13587.000 | 42136.766 | 63197.703 | 0.00 | 0.00 |  |
| transfers_out_prev_event | 10861.000 | 17145.500 | 35460.407 | 51379.661 | 0.00 | 0.00 |  |
| transfer_balance_prev_event | 10.000 | 7.000 | 6676.359 | 11818.042 | 0.00 | 0.00 |  |
| home_fixture_count | 1.000 | 0.000 | 0.502 | 0.498 | 0.50 | 0.50 |  |
| away_fixture_count | 0.000 | 1.000 | 0.498 | 0.502 | 0.50 | 0.50 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.043 | 2.995 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.043 | 2.995 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.333 | 1.667 | 1.346 | 1.498 | 0.05 | 0.01 |  |
| team_goals_against_avg_3 | 1.333 | 1.333 | 1.352 | 1.483 | 0.00 | 0.02 |  |
| team_goals_for_avg_5 | 1.200 | 1.400 | 1.373 | 1.449 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.400 | 1.400 | 1.368 | 1.430 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.333 | 1.667 | 1.352 | 1.503 | 0.05 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.333 | 1.333 | 1.351 | 1.460 | 0.00 | 0.02 |  |
| opponent_goals_for_avg_5 | 1.200 | 1.400 | 1.381 | 1.446 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.400 | 1.400 | 1.373 | 1.420 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.017 | -0.083 | 0.001 | -0.030 | 0.00 | 0.00 | **mean ratio -0.03** |
| form_x_opp_weakness_3 | -0.039 | -0.233 | -0.141 | -0.236 | 0.00 | 0.01 |  |
| xgi_x_opp_weakness_3 | -0.000 | -0.003 | -0.010 | -0.021 | 0.06 | 0.07 | **mean ratio 0.49** |
| opp_def_weakness_5 | 0.030 | 0.060 | 0.003 | -0.020 | 0.00 | 0.00 | **mean ratio -0.16** |
| form_x_opp_weakness_5 | 0.120 | 0.025 | -0.166 | -0.155 | 0.00 | 0.00 |  |
| xgi_x_opp_weakness_5 | 0.003 | 0.000 | -0.009 | -0.011 | 0.05 | 0.06 |  |
| points_avg_1 | 2.000 | 2.000 | 3.189 | 2.967 | 0.16 | 0.10 |  |
| minutes_avg_1 | 90.000 | 90.000 | 68.833 | 72.173 | 0.13 | 0.08 |  |
| appearance_rate_1 | 1.000 | 1.000 | 0.871 | 0.916 | 0.13 | 0.08 |  |
| played_60_rate_1 | 1.000 | 1.000 | 0.761 | 0.799 | 0.24 | 0.20 |  |
| points_avg_3 | 3.000 | 2.667 | 3.321 | 3.134 | 0.00 | 0.01 |  |
| minutes_avg_3 | 82.667 | 84.667 | 74.906 | 77.031 | 0.00 | 0.00 |  |
| appearance_rate_3 | 1.000 | 1.000 | 0.931 | 0.961 | 0.00 | 0.00 |  |
| played_60_rate_3 | 1.000 | 1.000 | 0.831 | 0.856 | 0.00 | 0.02 |  |
| points_avg_5 | 3.200 | 2.800 | 3.499 | 3.120 | 0.00 | 0.00 |  |
| minutes_avg_5 | 78.000 | 78.900 | 75.751 | 75.788 | 0.00 | 0.00 |  |
| appearance_rate_5 | 1.000 | 1.000 | 0.941 | 0.952 | 0.00 | 0.00 |  |
| played_60_rate_5 | 0.800 | 1.000 | 0.841 | 0.840 | 0.00 | 0.00 |  |
| points_avg_8 | 3.250 | 2.875 | 3.387 | 3.036 | 0.00 | 0.00 |  |
| minutes_avg_8 | 76.125 | 76.000 | 72.960 | 71.968 | 0.00 | 0.00 |  |
| appearance_rate_8 | 1.000 | 1.000 | 0.925 | 0.922 | 0.00 | 0.00 |  |
| played_60_rate_8 | 0.875 | 0.875 | 0.811 | 0.794 | 0.00 | 0.00 |  |
| price_change_1 | 0.000 | 0.000 | -0.001 | 0.001 | 0.89 | 0.85 |  |
| selected_change_1 | -0.004 | -0.002 | 0.016 | 0.037 | 0.00 | 0.00 | **mean ratio 0.45** |
| home_fixture_ratio | 1.000 | 0.000 | 0.502 | 0.498 | 0.50 | 0.50 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.258 | 0.270 | 0.67 | 0.67 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.266 | 0.265 | 0.51 | 0.52 |  |
| bps_avg_3 | 13.000 | 12.333 | 13.544 | 13.307 | 0.00 | 0.00 |  |
| bps_avg_5 | 14.000 | 12.800 | 14.299 | 13.292 | 0.00 | 0.00 |  |
| influence_avg_3 | 16.067 | 16.400 | 16.665 | 17.696 | 0.00 | 0.00 |  |
| influence_avg_5 | 16.240 | 16.960 | 17.224 | 17.574 | 0.00 | 0.00 |  |
| creativity_avg_3 | 8.133 | 8.717 | 11.372 | 11.961 | 0.07 | 0.08 |  |
| creativity_avg_5 | 9.120 | 9.560 | 11.834 | 11.650 | 0.06 | 0.07 |  |
| threat_avg_3 | 5.333 | 6.167 | 9.306 | 10.514 | 0.14 | 0.14 |  |
| threat_avg_5 | 6.800 | 7.000 | 9.573 | 10.413 | 0.11 | 0.10 |  |
| ict_index_avg_3 | 3.300 | 3.400 | 3.730 | 4.016 | 0.00 | 0.00 |  |
| ict_index_avg_5 | 3.360 | 3.380 | 3.858 | 3.962 | 0.00 | 0.00 |  |
| starts_avg_3 | 1.000 | 1.000 | 0.876 | 0.892 | 0.00 | 0.01 |  |
| starts_avg_5 | 1.000 | 1.000 | 0.881 | 0.874 | 0.00 | 0.00 |  |
| expected_goals_avg_3 | 0.040 | 0.045 | 0.098 | 0.111 | 0.25 | 0.23 |  |
| expected_goals_avg_5 | 0.052 | 0.053 | 0.104 | 0.107 | 0.18 | 0.16 |  |
| expected_assists_avg_3 | 0.040 | 0.043 | 0.064 | 0.074 | 0.07 | 0.09 |  |
| expected_assists_avg_5 | 0.040 | 0.050 | 0.066 | 0.072 | 0.05 | 0.07 |  |
| expected_goal_involvements_avg_3 | 0.103 | 0.117 | 0.162 | 0.185 | 0.06 | 0.07 |  |
| expected_goal_involvements_avg_5 | 0.110 | 0.132 | 0.170 | 0.179 | 0.05 | 0.06 |  |
| expected_goals_conceded_avg_3 | 1.000 | 1.107 | 1.094 | 1.243 | 0.00 | 0.00 |  |
| expected_goals_conceded_avg_5 | 1.094 | 1.100 | 1.144 | 1.181 | 0.00 | 0.00 |  |
| defensive_contribution_avg_3 | 5.667 | 0.000 | 5.726 | 1.982 | 0.10 | 0.70 | **zero share 0.10 vs 0.70; mean ratio 2.89** |
| defensive_contribution_avg_5 | 5.600 | 0.000 | 5.695 | 1.946 | 0.10 | 0.70 | **zero share 0.10 vs 0.70; mean ratio 2.93** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.158 | 0.052 | 0.67 | 0.89 | **mean ratio 3.03** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.152 | 0.054 | 0.58 | 0.85 | **zero share 0.58 vs 0.85; mean ratio 2.84** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.331 | 0.00 | 0.67 | **zero share 0.00 vs 0.67; mean ratio 3.02** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.110 | 0.115 | 0.89 | 0.89 |  |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.110 | 0.115 | 0.89 | 0.89 |  |

Flags: 17 (a flag is a prompt to look, not a verdict; schedule-driven features legitimately differ by week).
