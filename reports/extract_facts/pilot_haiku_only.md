# Extractor pilot: haiku on 60 prose documents + 30 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| haiku | 90 | 100% | 0 | 1.8 | 20 | - | - |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| haiku | 30 | 0.95 | 0.67 | 0.70 | 649 | 35 | 319 | bench->missed 284, doubt->bench 31, out->missed 2, out->bench 1 |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|

## Outcome validity on prose documents (facts joined to the next gameweek's minutes)

| arm | status | facts | matched to a player | appeared | started |
|---|---|---|---|---|---|
| haiku | xi | 16 | 14 | 93% | 86% |
| haiku | bench | 5 | 5 | 40% | 0% |
| haiku | doubt | 11 | 9 | 67% | 67% |
| haiku | out | 46 | 39 | 10% | 8% |
| haiku | return | 19 | 17 | 71% | 53% |
| haiku | role | 11 | 8 | 100% | 88% |

## Disagreement cases for a hand audit (first 0)

