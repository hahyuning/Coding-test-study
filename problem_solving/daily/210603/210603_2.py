n, k = map(int, input().split())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for _ in range(k):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = []
for i in range(1, n + 1):
    s = 0
    for j in range(1, n + 1):
        s += dist[i][j]
    ans.append((s, i))
ans.sort(key=lambda x:(x[0], x[1]))
print(ans[0][1])

