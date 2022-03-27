def solution(n, edges):

    def dfs(now, x):
        cnt[now] = x

        for nxt in graph[now]:
            if cnt[nxt] == -1:
                dfs(nxt, x + 1)


    ans = 0
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        cnt = [-1] * n
        dfs(i, 0)
        ans += sum(cnt) - (n - 1)

    return ans
