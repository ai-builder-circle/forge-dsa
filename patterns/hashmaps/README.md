# Pattern: Hashmaps (frequency counting)

**In simple terms:** keep a notebook where you write down each thing you've seen and how many times
(or where). Looking something up in the notebook is instant, so you don't have to rescan everything.

**The jargon:** a hash map (`dict` in Python, `HashMap` in Java) gives average O(1) insert and lookup.
It turns many O(n²) "compare every pair" solutions into O(n).

## How to spot it under a disguise
- "How many times...", "first one that only appears once", "most common / trending"
- "Find two things that add up to / match..."
- "Have we seen this before?", "duplicates", "group things that are the same"

## Problems
| # | Problem | Difficulty |
|---|---|---|
| 001 | First unique | easy |
| 002 | Pair to target | easy |
| 003 | Top word | easy |
