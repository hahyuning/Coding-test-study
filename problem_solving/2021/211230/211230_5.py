import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

    if a != b:
        cnt[a] += cnt[b]

n, m, q = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

removed = []
for _ in range(q):
    x = int(input())
    removed.append(x)
removed.reverse()

parent = [i for i in range(n + 1)]
cnt = [1] * (n + 1)
for i, x in enumerate(edges, start=1):
    if i not in removed:
        a, b = x
        union(a, b)

ans = 0
for x in removed:
    a = find(edges[x - 1][0])
    b = find(edges[x - 1][1])

    if a != b:
        ans += cnt[a] * cnt[b]
        cnt[a] += cnt[b]
        parent[b] = a

print(ans)
