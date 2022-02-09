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
parent = [i for i in range(n + 1)]
ans = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v):
        ans += 1
    union(u, v)

root = []
for i in range(1, n + 1):
    x = find(i)
    if x not in root:
        root.append(x)
print(ans + len(root) - 1)