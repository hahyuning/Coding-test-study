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
a = [input() for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        if a[i][j] == "Y":
            cost = i * n + j
            edges.append((cost, i, j))
edges.sort()

res = 0
k = len(edges)
cnt = [0] * n
check = [False] * k
for i, edge in enumerate(edges):
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        cnt[a] += 1
        cnt[b] += 1
        check[i] = True
        res += 1

if res > m:
    print(-1)
else:
    for i in range(n - 1):
        if find(i) != find(i + 1):
            print(-1)
            break
    else:
        for i in range(k):
            if res == m:
                break
            if not check[i]:
                cost, a, b = edges[i]
                cnt[a] += 1
                cnt[b] += 1
                check[i] = True
                res += 1
        if res < m:
            print(-1)
        else:
            print(*cnt)
