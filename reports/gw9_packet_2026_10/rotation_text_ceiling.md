# Rotation risk: numbers vs text (nailed-looking players, 2023-24 to 2026-27 GW8)

15198 player-weeks that looked nailed at the deadline (started the last three with >= 75 min, unflagged). Non-start = under 60 minutes. ± is 2 standard errors.

## 1. This week's Guardian predicted lineup (the best text we have)

| Guardian category | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| XI | 10758 | 0.122 | 0.006 | 80.7 | 3.30 |
| doubtful | 123 | 0.496 | 0.090 | 45.7 | 2.41 |
| no article | 3847 | 0.184 | 0.012 | 74.2 | 3.16 |
| out | 69 | 0.957 | 0.049 | 3.9 | 0.06 |
| sub | 401 | 0.392 | 0.049 | 58.5 | 2.49 |

Of the 2304 surprise non-starts, 1596 (69%) had an article; the article had foreseen 17.8% of those (sub / doubtful / out), and listed 82.2% in the XI.

- defenders: 6177 nailed rows, non-start rate 0.149; 629 non-starts with an article, 19.4% foreseen; article present on 75% of rows.
- 2025-26: 4943 nailed rows, non-start rate 0.158; 518 non-starts with an article, 23.6% foreseen; article present on 72% of rows.
- 2026-27: 996 nailed rows, non-start rate 0.109; 36 non-starts with an article, 5.6% foreseen; article present on 38% of rows.

## 2. Prior-season rotation profile (share of last season's articles listing the player as a sub)

| prior-season sub share | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| sub < 10% | 6883 | 0.128 | 0.008 | 80.0 | 3.50 |
| 10-25% | 1980 | 0.160 | 0.016 | 76.7 | 3.27 |
| 25-50% | 1702 | 0.183 | 0.019 | 75.5 | 3.16 |
| 50%+ | 1343 | 0.172 | 0.021 | 75.2 | 3.12 |

Defenders only:

| prior-season sub share | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| sub < 10% | 2724 | 0.119 | 0.012 | 81.1 | 3.15 |
| 10-25% | 893 | 0.162 | 0.025 | 76.9 | 2.96 |
| 25-50% | 636 | 0.176 | 0.030 | 75.6 | 2.73 |
| 50%+ | 437 | 0.190 | 0.038 | 73.2 | 2.95 |

Weeks 1-10 only:

| prior-season sub share | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| sub < 10% | 2249 | 0.096 | 0.012 | 81.5 | 3.60 |
| 10-25% | 638 | 0.135 | 0.027 | 77.3 | 3.28 |
| 25-50% | 532 | 0.164 | 0.032 | 75.4 | 3.07 |
| 50%+ | 415 | 0.149 | 0.035 | 75.8 | 2.93 |

By prior-season start share:

| prior-season start share | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| < 40% | 2981 | 0.178 | 0.014 | 74.9 | 3.02 |
| 40-60% | 2134 | 0.170 | 0.016 | 76.5 | 3.22 |
| 60-80% | 3009 | 0.156 | 0.013 | 77.9 | 3.50 |
| 80%+ | 3784 | 0.100 | 0.010 | 82.1 | 3.62 |

## 3. Both together

| prior sub share / this week's article | n | non-start rate | ± | minutes | points |
|---|---|---|---|---|---|
| sub < 10% / XI | 4992 | 0.108 | 0.009 | 81.9 | 3.55 |
| sub < 10% / sub | 86 | 0.442 | 0.107 | 55.8 | 2.30 |
| 10-25% / XI | 1424 | 0.117 | 0.017 | 80.6 | 3.41 |
| 10-25% / sub | 61 | 0.443 | 0.127 | 55.8 | 2.75 |
| 25-50% / XI | 1168 | 0.152 | 0.021 | 78.6 | 3.18 |
| 25-50% / sub | 93 | 0.312 | 0.096 | 64.6 | 2.17 |
| 50%+ / XI | 892 | 0.135 | 0.023 | 78.7 | 3.22 |
| 50%+ / sub | 75 | 0.333 | 0.109 | 61.9 | 3.24 |

Calafiori's 2026-27 profile: prior-season sub share 0.38 over 29 articles, prior start share 0.50.

Caveat: these are raw rates, not residuals against the model's forecast; the controlled version (excess vs same-forecast peers) is in minutes_prior_study.md, where the same gradient is about 2-3 minutes and 0.1-0.2 points a week for defenders.
