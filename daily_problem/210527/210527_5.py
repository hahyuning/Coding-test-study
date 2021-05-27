import sys
INF = sys.maxsize

n = int(input())
a = [0] + [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue

        if a[i][1] <= a[j][0]:
            dist[i][j] = 1
            print(i, j)

for x in dist:
    print(x)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if dist[a][b] == INF:
        print(-1)
    else:
        print(dist[a][b])