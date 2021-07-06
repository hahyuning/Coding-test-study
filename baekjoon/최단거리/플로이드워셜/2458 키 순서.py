INF = 1e9
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

cnt = 0
for i in range(1, n + 1):
    check = True
    for j in range(1, n + 1):
        if i == j:
            continue
        if graph[i][j] == INF and graph[j][i] == INF:
            check = False
            break
    if check:
        cnt += 1
print(cnt)
