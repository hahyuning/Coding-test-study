def dfs(now, max_val, sum):
    global ans
    if now == b:
        if ans == -1 or max_val < ans:
            ans = max_val
        return

    for nxt, cost in graph[now]:
        if not check[nxt] and sum + cost <= c:
            tmp = max(max_val, cost)
            check[nxt] = True
            dfs(nxt, tmp, sum + cost)
            check[nxt] = False


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
    graph[e].append((s, cost))

ans = -1
check = [False] * (n + 1)
check[a] = True
dfs(a, 0, 0)
print(ans)