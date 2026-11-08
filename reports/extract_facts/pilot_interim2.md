# Extractor pilot: e4b, e4b_v2, 31b, haiku_v2 on 60 prose documents + 30 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| e4b | 90 | 99% | 1 | 8.1 | 14 | 268 | 22.2 |
| e4b_v2 | 90 | 92% | 7 | 5.8 | 18 | 226 | 27.3 |
| 31b | 90 | 100% | 0 | 2.1 | 14 | 92 | 61.9 |
| haiku_v2 | 90 | 100% | 0 | 2.0 | 21 | - | - |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| e4b | 30 | 0.75 | 0.23 | 0.30 | 220 | 75 | 748 | bench->missed 667, out->doubt 69, out->missed 6, doubt->missed 2 |
| e4b_v2 | 30 | 0.89 | 0.53 | 0.60 | 513 | 65 | 455 | bench->missed 359, out->doubt 57, out->missed 29, doubt->bench 5 |
| 31b | 30 | 0.99 | 0.29 | 0.29 | 281 | 2 | 687 | bench->missed 680, out->missed 6, not listed->out 1, out->doubt 1 |
| haiku_v2 | 30 | 0.95 | 0.95 | 1.00 | 918 | 50 | 50 | doubt->bench 45, out->bench 3, out->missed 2, not listed->out 1 |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|
| e4b vs e4b_v2 | 46 | 0.62 | 0.72 |
| e4b vs 31b | 51 | 0.19 | 0.30 |
| e4b vs haiku_v2 | 49 | 0.21 | 0.29 |
| e4b_v2 vs 31b | 48 | 0.25 | 0.38 |
| e4b_v2 vs haiku_v2 | 46 | 0.25 | 0.36 |
| 31b vs haiku_v2 | 47 | 0.49 | 0.60 |

## Outcome validity on prose documents (facts joined to the next gameweek's minutes)

| arm | status | facts | matched to a player | appeared | started |
|---|---|---|---|---|---|
| e4b | xi | 336 | 254 | 87% | 69% |
| e4b | bench | 21 | 13 | 85% | 54% |
| e4b | doubt | 21 | 17 | 59% | 47% |
| e4b | out | 59 | 51 | 29% | 22% |
| e4b | return | 16 | 12 | 83% | 67% |
| e4b | role | 28 | 21 | 81% | 48% |
| e4b | other | 5 | 4 | 75% | 75% |
| e4b_v2 | xi | 227 | 183 | 89% | 70% |
| e4b_v2 | bench | 18 | 11 | 91% | 64% |
| e4b_v2 | doubt | 21 | 14 | 64% | 43% |
| e4b_v2 | out | 50 | 48 | 29% | 19% |
| e4b_v2 | return | 15 | 11 | 82% | 64% |
| e4b_v2 | role | 19 | 13 | 85% | 62% |
| 31b | xi | 26 | 24 | 100% | 88% |
| 31b | bench | 7 | 7 | 57% | 0% |
| 31b | doubt | 24 | 18 | 61% | 39% |
| 31b | out | 40 | 38 | 13% | 5% |
| 31b | return | 16 | 15 | 80% | 60% |
| 31b | role | 12 | 10 | 100% | 60% |
| haiku_v2 | xi | 24 | 21 | 95% | 81% |
| haiku_v2 | bench | 4 | 4 | 50% | 0% |
| haiku_v2 | doubt | 17 | 12 | 58% | 58% |
| haiku_v2 | out | 41 | 34 | 9% | 6% |
| haiku_v2 | return | 19 | 17 | 71% | 53% |
| haiku_v2 | role | 17 | 14 | 100% | 79% |

## Disagreement cases for a hand audit (first 0)

**2022-23 GW31 guardian 134.1h** Aaron Ramsdale saves everything for Arsenal to keep title challenge alive  
- e4b: Aaron Ramsdale [xi] saved everything for Arsenal to keep title challenge alive; Ibrahima Konaté [xi] launched his chest at a cross and seemed certain to score; Mohamed Salah [xi] step inside and leaping claw-away as Mohamed Salah went for the far corner; Darwin Núñez [xi] block from Darwin Núñez, who ran on to the perfect pass from Salah; Gabriel Martinelli [xi] scored the opener, a goal made by a turn from Bukayo Saka; Bukayo Saka [xi] a goal made by a turn from Bukayo Saka; Andy Robertson [xi] fell over trying to follow him; Gabriel Jesus [xi] the header from Gabriel Jesus precise; Trent Alexander-Arnold [xi] stepped into midfield and began to unfurl those 30- to 40-yard passes; Oleksandr Zinchenko [xi] Alexander-Arnold made the difference deep into the second half, nutmegging Oleksandr Zinchenko  
- e4b_v2: Aaron Ramsdale [xi] Ramsdale just kept making saves, blocks, catches, clearances.  
- 31b: (none)  
- haiku_v2: (none)  

