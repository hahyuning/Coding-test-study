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

    # 순서 그래프에 꼭 지켜야하는 순서(부모->자식)를 추가해서 최소의 순서 그래프 만들기
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

    # 만들어진 순서 그래프로 위상정렬 수행
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

    # 사이클이 발생하는 경우 모든 노드를 다 탐색하지 못하므로 false
    if len(res) < n:
        return False
    return True

solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])