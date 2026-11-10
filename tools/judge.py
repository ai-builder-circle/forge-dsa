#!/usr/bin/env python3
"""FORGE judge: runs every solution against every case, like an online assessment.

Usage:
    python3 tools/judge.py                      # everything
    python3 tools/judge.py patterns/hashmaps    # one pattern
    python3 tools/judge.py patterns/hashmaps/001-first-unique
"""
import glob, os, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIME_LIMIT = 5  # seconds per case


def problems(target):
    for path in sorted(glob.glob(os.path.join(target, "**", "PROBLEM.md"), recursive=True)):
        if "_TEMPLATE" not in path:
            yield os.path.dirname(path)


def solutions(problem):
    dirs = [os.path.join(problem, "_reference")]
    dirs += sorted(glob.glob(os.path.join(problem, "solutions", "*")))
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for name in ("solution.py", "Solution.java"):
            if os.path.exists(os.path.join(d, name)):
                yield os.path.join(d, name)


def command(sol, build_dir):
    if sol.endswith(".py"):
        return [sys.executable, sol]
    shutil.copy(sol, build_dir)
    res = subprocess.run(["javac", "-d", build_dir, os.path.join(build_dir, "Solution.java")],
                         capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError("compile error:\n" + res.stderr[-1500:])
    return ["java", "-Xss64m", "-cp", build_dir, "Solution"]


def run(problem, sol):
    cases = sorted(glob.glob(os.path.join(problem, "cases", "*.in")))
    with tempfile.TemporaryDirectory() as build:
        try:
            cmd = command(sol, build)
        except RuntimeError as e:
            return 0, len(cases), [str(e)]
        passed, notes = 0, []
        for case in cases:
            name = os.path.basename(case)[:-3]
            expected = open(case[:-3] + ".out").read().split()
            try:
                res = subprocess.run(cmd, stdin=open(case), capture_output=True, text=True, timeout=TIME_LIMIT)
                got = res.stdout.split()
                if res.returncode != 0:
                    notes.append(f"case {name}: crashed ({res.stderr.strip().splitlines()[-1:] or ['?']})")
                elif got == expected:
                    passed += 1
                else:
                    notes.append(f"case {name}: wrong answer")
            except subprocess.TimeoutExpired:
                notes.append(f"case {name}: too slow (> {TIME_LIMIT}s), think about a faster approach")
        return passed, len(cases), notes


def main():
    target = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "patterns")
    failed = 0
    for problem in problems(target):
        print(f"\n🔥 {os.path.relpath(problem, ROOT)}")
        for sol in solutions(problem):
            passed, total, notes = run(problem, sol)
            who = os.path.relpath(sol, problem)
            mark = "✅" if passed == total else "❌"
            print(f"  {mark} {who}: {passed}/{total}")
            for n in notes:
                print(f"       - {n}")
            if passed != total:
                failed += 1
    if failed:
        print(f"\n{failed} solution(s) need work. Keep striking.")
        sys.exit(1)
    print("\nAll strikes landed. 🔨")


if __name__ == "__main__":
    main()
