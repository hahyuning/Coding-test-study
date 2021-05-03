from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    q = deque()
    # d[i]: 건물 i를 건설완료 하는데 드는 최소 시간
    d = [-1] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            d[i] = cost[i]

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            indegree[nxt] -= 1
            d[nxt] = max(d[nxt], d[now] + cost[nxt])

            if indegree[nxt] == 0:
                q.append(nxt)

    print(d[w])