INF = 1e9

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
            continue

        if a[i][0] <= a[j][1] <= a[i][1] or a[i][0] <= a[j][0] <= a[i][1] or a[j][0] <= a[i][1] <= a[j][1] or a[j][0] <= a[i][0] <= a[j][1]:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] == INF:
        print(-1)
    else:
        print(dist[a][b])