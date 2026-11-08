# Extractor pilot: e4b, haiku, haiku_v2 on 60 prose documents + 30 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| e4b | 90 | 99% | 1 | 8.1 | 14 | 268 | 22.2 |
| haiku | 90 | 100% | 0 | 1.8 | 20 | - | - |
| haiku_v2 | 90 | 100% | 0 | 2.0 | 21 | - | - |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| e4b | 30 | 0.75 | 0.23 | 0.30 | 220 | 75 | 748 | bench->missed 667, out->doubt 69, out->missed 6, doubt->missed 2 |
| haiku | 30 | 0.95 | 0.67 | 0.70 | 649 | 35 | 319 | bench->missed 284, doubt->bench 31, out->missed 2, out->bench 1 |
| haiku_v2 | 30 | 0.95 | 0.95 | 1.00 | 918 | 50 | 50 | doubt->bench 45, out->bench 3, out->missed 2, not listed->out 1 |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|
| e4b vs haiku | 49 | 0.18 | 0.26 |
| e4b vs haiku_v2 | 49 | 0.21 | 0.29 |
| haiku vs haiku_v2 | 42 | 0.74 | 0.78 |

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
| haiku | xi | 16 | 14 | 93% | 86% |
| haiku | bench | 5 | 5 | 40% | 0% |
| haiku | doubt | 11 | 9 | 67% | 67% |
| haiku | out | 46 | 39 | 10% | 8% |
| haiku | return | 19 | 17 | 71% | 53% |
| haiku | role | 11 | 8 | 100% | 88% |
| haiku_v2 | xi | 24 | 21 | 95% | 81% |
| haiku_v2 | bench | 4 | 4 | 50% | 0% |
| haiku_v2 | doubt | 17 | 12 | 58% | 58% |
| haiku_v2 | out | 41 | 34 | 9% | 6% |
| haiku_v2 | return | 19 | 17 | 71% | 53% |
| haiku_v2 | role | 17 | 14 | 100% | 79% |

## Disagreement cases for a hand audit (first 0)

**2022-23 GW31 guardian 134.1h** Aaron Ramsdale saves everything for Arsenal to keep title challenge alive  
- e4b: Aaron Ramsdale [xi] saved everything for Arsenal to keep title challenge alive; Ibrahima Konaté [xi] launched his chest at a cross and seemed certain to score; Mohamed Salah [xi] step inside and leaping claw-away as Mohamed Salah went for the far corner; Darwin Núñez [xi] block from Darwin Núñez, who ran on to the perfect pass from Salah; Gabriel Martinelli [xi] scored the opener, a goal made by a turn from Bukayo Saka; Bukayo Saka [xi] a goal made by a turn from Bukayo Saka; Andy Robertson [xi] fell over trying to follow him; Gabriel Jesus [xi] the header from Gabriel Jesus precise; Trent Alexander-Arnold [xi] stepped into midfield and began to unfurl those 30- to 40-yard passes; Oleksandr Zinchenko [xi] Alexander-Arnold made the difference deep into the second half, nutmegging Oleksandr Zinchenko  
- haiku: (none)  
- haiku_v2: (none)  

