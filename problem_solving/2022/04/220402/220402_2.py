
def solution(n, edges, k, a, b):
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    ans = set()
    visited = [False] * n
    a, b = min(a, b), max(a, b)

    def dfs(now, path, dist):
        if now == b:
            if dist <= k:
                for x, y in path:
                    ans.add((x, y))
            return

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                path.append((min(now, nxt), max(now, nxt)))
                dfs(nxt, path, dist + 1)
                path.pop()
                visited[nxt] = False

    visited[a] = True
    dfs(a, [], 0)

    return len(ans)

solution(8, [[0, 1], [1, 2], [2, 3], [4, 0], [5, 1], [6, 1], [7, 2], [7, 3], [4, 5], [5, 6], [6, 7]], 4, 0, 3)