def dfs(now):
    global ans

    cnt = ball[now] - 1
    for nxt in graph[now]:
        cnt += dfs(nxt)
    ans += abs(cnt)
    return cnt

while True:
    n = int(input())
    if n == 0:
        break

    graph = [[] for _ in range(n + 1)]
    ball = [0] * (n + 1)
    indegree = [0] * (n + 1)

    for _ in range(n):
        node, cnt, *child = map(int, input().split())
        ball[node] = cnt

        if child[0] > 0:
            for x in child[1:]:
                graph[node].append(x)
                indegree[x] += 1

    ans = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dfs(i)
    print(ans)