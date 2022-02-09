import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
for _ in range(n):
    s = input().rstrip()
    t = []
    for x in s:
        if x != " ":
            t.append(x)
    c = Counter(t)
    m = c.most_common(2)
    if len(m) == 1 or m[0][1] > m[1][1]:
        print(m[0][0])
    else:
        print("?")
