n, m = map(int, input().split())

dist = [[1e9] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    dist[a][b] = min(dist[a][b], t)

for k in range(1, n + 1):
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

k = int(input())
cities = list(map(int, input().split()))

min_cost = 1e9
ans = []
for i in range(1, n + 1):
    cost = 0
    for c in cities:
        cost = max(cost, dist[c][i] + dist[i][c])

    if cost < min_cost:
        ans = [i]
        min_cost = cost
    elif cost == min_cost:
        ans.append(i)
print(*ans)


