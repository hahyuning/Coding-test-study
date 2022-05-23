n, m = map(int, input().split())
in_graph = [[1e9] * (n + 1) for _ in range(n + 1)]
out_graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    in_graph[i][i] = 0
    out_graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    in_graph[a][b] = 1
    out_graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            in_graph[i][j] = min(in_graph[i][j], in_graph[i][k] + in_graph[k][j])
            out_graph[i][j] = min(out_graph[i][j], out_graph[i][k] + out_graph[k][j])

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if in_graph[i][j] not in [0, 1e9]:
            cnt += 1

    if cnt > (n - 1) // 2:
        ans += 1

    cnt = 0
    for j in range(1, n + 1):
        if out_graph[i][j] not in [0, 1e9]:
            cnt += 1

    if cnt > (n - 1) // 2:
        ans += 1

print(ans)
