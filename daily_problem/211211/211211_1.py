import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
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
parent = [i for i in range(n + 1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

ans = 0
s = 0
for c, a, b in edges:
    s += c
    if find(a) != find(b):
        ans += c
        union(a, b)

tmp = set()
for i in range(1, n + 1):
    tmp.add(find(i))
if len(tmp) != 1:
    print(-1)
else:
    print(s - ans)