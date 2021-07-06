import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 0:
        dist[u][v] = 0
        dist[v][u] = 1
    else:
        dist[u][v] = 0
        dist[v][u] = 0

for i in range(1, n + 1):
    dist[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][k] + dist[k][b], dist[a][b])

t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    print(dist[s][e])
