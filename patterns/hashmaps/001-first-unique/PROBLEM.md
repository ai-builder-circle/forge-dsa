# 001 · First unique

**Pattern:** hashmaps · **Difficulty:** easy · **Seen in intel:** not yet

## Disguise
A security gate logs the badge letter of everyone who walks through, in order, as one long string.
Security wants to find the first person whose badge letter appears **only once** in the whole day's log.
Return the position (0-based) of that entry, or `-1` if every letter repeats.

## Plain version
Given a string, return the index of the first character that does not repeat. Return `-1` if none.

## Input
One line: the string `s` (may be empty). Letters only.

## Output
One integer.

## Example
```
swiss
```
```
1
```
(`w` at index 1 is the first character that appears only once.)

## Limits
`0 ≤ len(s) ≤ 200 001`. A nested loop will be too slow on the largest case.
