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

check = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] > 6:
            check = False
            break
    if not check:
        break
print("Small World!" if check else "Big World!")


