import sys

data = sys.stdin.read().split()
n, target = int(data[0]), int(data[1])
nums = list(map(int, data[2:2 + n]))
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        print(seen[target - x], i)
        break
    seen[x] = i
