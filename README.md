# FORGE DSA 🔥

Practice built around **what companies actually test, and how they ask it**.
Not another pile of LeetCode answers.

Members only. Private for now; we review going public after the first month.

## The FORGE words

| Word | Means |
|---|---|
| **The Anvil** | Our weekly DSA slot: Mondays, 30 min after check-in |
| **Strike** | A solved problem + an `APPROACH.md` note |
| **Intel** | An assessment log entry (format, topics, time limit, never the questions) |
| **Disguise** | The story version of a problem, the way assessments ask it |
| **The Heat** | The monthly timed mock |
| **Smiths** | This month's curators |
| **The Radar** | `RADAR.md`: what's being tested right now |

## How the repo is laid out

```
intel/        assessment log entries      -> start with intel/_TEMPLATE.md
patterns/     practice, grouped by pattern
  hashmaps/
    README.md                 the pattern in simple terms, how to spot it
    001-first-unique/
      PROBLEM.md              plain version + disguise
      cases/                  test cases (NN.in / NN.out)
      _reference/             the Smiths' working solution
      solutions/<github>/     YOUR strike goes here
mocks/        the monthly Heat
tools/judge.py   runs every solution against every case
RADAR.md      what's being tested now
```

## Land a strike (solve a problem)

1. Pick a problem in `patterns/`. Read the **Disguise first** and try to spot the pattern yourself.
2. Create `solutions/<your-github-username>/` inside the problem folder.
3. Add **one** of:
   - `solution.py`
   - `Solution.java` (class `Solution` with a `main` method, **no package line**)
4. Your program **reads from standard input and prints to standard output**, exactly like online assessments (HackerRank, Codility style). The input format is in `PROBLEM.md`.
5. Add `APPROACH.md`: your idea, the time and space cost, and the edge cases you thought about. (Template: `patterns/_APPROACH_TEMPLATE.md`.)
6. Test locally:
   ```bash
   python3 tools/judge.py patterns/hashmaps/001-first-unique
   ```
7. Open a pull request. GitHub runs the judge on every case automatically, including the ones you didn't look at.

## The rules

- **Never commit real assessment questions.** Not in intel, not as a problem, not "reworded". Format and topics only.
- **Don't read the `cases/` before you've tried.** They're there so the judge can test you, like hidden test cases.
- **Don't look at other members' solutions until you've landed your own strike.**
- Java or Python, your choice.

## Drop your intel

Sat a company assessment? Copy `intel/_TEMPLATE.md`, fill it in while you remember, open a PR.
That's the most valuable thing you can add to this repo.

See `CONTRIBUTING.md` for Smiths (curators).
