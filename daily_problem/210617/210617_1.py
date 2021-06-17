v, e = map(int, input().split())
dist = [[1e9] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for i in range(1, v + 1):
    dist[i][i] = 0

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

ans = 1e9
for i in range(1, v + 1):
    for j in range(i, v + 1):
        if i == j:
            continue
        ans = min(ans, dist[i][j] + dist[j][i])

if ans == 1e9:
    print(-1)
else:
    print(ans)

