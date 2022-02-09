from collections import deque
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
d = {"D":(1, 0), "U":(-1, 0), "R":(0, 1), "L":(0, -1)}
parent = [i for i in range(n * m)]

for i in range(n * m):
    x = i // m
    y = i % m

    nx, ny = x + d[a[x][y]][0], y + d[a[x][y]][1]
    nxt = nx * m + ny
    if 0 <= nxt < n * m:
        union(i, nxt)

ans = set()
for i in range(n * m):
    ans.add(find(i))
print(len(ans))