# For Smiths (curators)

Curators rotate monthly. To curate you need access to a pro-tier AI model (Claude Pro, ChatGPT Plus,
Gemini Advanced or similar), which **you pay for yourself**.

## Your month

1. Read new `intel/` entries and update `RADAR.md`.
2. Add problems for the patterns the Radar says matter most.
3. Set the month's Heat in `mocks/`.
4. Hand over to the next Smith with a short note in `mocks/HANDOVER.md`.

## Adding a problem

```
patterns/<pattern>/<NNN-short-name>/
  PROBLEM.md        copy patterns/_PROBLEM_TEMPLATE.md
  cases/01.in 01.out 02.in 02.out ...
  _reference/solution.py   (or Solution.java)
```

Checklist before you merge:
- [ ] `PROBLEM.md` has a **plain** version and a **Disguise**, plus an exact input/output format.
- [ ] At least 6 cases: 2 simple, 3 edge cases (empty, single item, duplicates, negatives...), 1 large.
- [ ] `python3 tools/judge.py <problem-folder>` passes for `_reference/`.
- [ ] Difficulty matches what the intel describes. Not harder.

## AI rules

- **AI drafts, you decide.** Run and check everything before it goes in.
- **Never paste real assessment questions into any AI.** Work from intel: format, topics, style.
- Generate large cases with a script, then check them against the reference solution.
