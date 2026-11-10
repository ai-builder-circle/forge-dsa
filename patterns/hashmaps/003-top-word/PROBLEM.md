# 003 · Top word

**Pattern:** hashmaps · **Difficulty:** easy · **Seen in intel:** not yet

## Disguise
A social app records every hashtag used today, in order. Product wants the **trending** hashtag:
the one used the most. If several tie, show the one that comes first alphabetically.

## Plain version
Given a list of words, return the most frequent word. Break ties by choosing the
lexicographically smallest.

## Input
Line 1: `n`
Line 2: `n` lowercase words separated by spaces

## Output
One word.

## Example
```
4
ship code ship forge
```
```
ship
```

## Limits
`1 ≤ n ≤ 100 000`.
