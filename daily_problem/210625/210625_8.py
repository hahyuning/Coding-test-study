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
s = [0] + input().split()
parent = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    u, b, d = map(int, input().split())
    if s[u] != s[b]:
        edges.append((d, u, b))

edges.sort()
ans = 0
for d, u, b in edges:
    if find(u) != find(b):
        union(u, b)
        ans += d

check = False
for i in range(1, n):
    if find(i) != find(i + 1):
        check = True
        break

if check:
    print(-1)
else:
    print(ans)