from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    order_graph = [[] for _ in range(n)]
    indegree = [0] * n

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in order:
        order_graph[a].append(b)
        indegree[b] += 1

    visited = [False] * n
    q = deque()
    q.append(0)
    visited[0] = True

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                order_graph[now].append(nxt)
                indegree[nxt] += 1

    res = []
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)
        for nxt in order_graph[now]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)

    if len(res) < n:
        return False

    return True