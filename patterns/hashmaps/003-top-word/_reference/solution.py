import sys
from collections import Counter

data = sys.stdin.read().split()
n = int(data[0])
counts = Counter(data[1:1 + n])
best = max(counts.values())
print(min(word for word, c in counts.items() if c == best))
