n, k, m = map(int, input().split())
item = [0] + list(map(int, input().split()))
dist = [[1e9] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dist[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][c] + dist[c][b], dist[a][b])

ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if dist[i][j] <= k:
            tmp += item[j]
    ans = max(ans, tmp)
print(ans)