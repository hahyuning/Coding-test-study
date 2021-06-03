n = int(input())
x, y = map(int, input().split())
m = int(input())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist[x][y] if dist[x][y] != 1e9 else -1)
