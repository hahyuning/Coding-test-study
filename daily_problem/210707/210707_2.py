import sys
input = sys.stdin.readline
from collections import defaultdict

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

c, h, k = map(int, input().split())
tmp = defaultdict(list)
for i in range(1, n + 1):
    x = find(i)
    tmp[x].append(i)

tmp = sorted(tmp.items(), key=lambda x:-len(x[1]))
ans = 0
for x, y in tmp:
    if c in y:
        ans += len(y)
    elif h not in y and k > 0:
        ans += len(y)
        k -= 1

print(ans)