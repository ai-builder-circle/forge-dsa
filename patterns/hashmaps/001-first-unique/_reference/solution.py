import sys
from collections import Counter

s = sys.stdin.readline().strip()
counts = Counter(s)
answer = -1
for i, ch in enumerate(s):
    if counts[ch] == 1:
        answer = i
        break
print(answer)
