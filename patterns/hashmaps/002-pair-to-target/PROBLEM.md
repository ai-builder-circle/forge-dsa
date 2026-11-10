# 002 · Pair to target

**Pattern:** hashmaps · **Difficulty:** easy · **Seen in intel:** not yet

## Disguise
A customer has a voucher worth exactly `T` rand and must spend it on **exactly two different items**
from a shop's price list, with nothing left over. Exactly one such pair exists.
Print the positions of the two items on the list.

## Plain version
Given an array and a target, return the indices `i < j` such that `nums[i] + nums[j] = target`.
Exactly one answer exists.

## Input
Line 1: `n T`
Line 2: `n` integers (can be negative or zero)

## Output
Two integers `i j` with `i < j`.

## Example
```
4 9
2 7 11 15
```
```
0 1
```

## Limits
`2 ≤ n ≤ 100 000`. Checking every pair is too slow on the largest case.
