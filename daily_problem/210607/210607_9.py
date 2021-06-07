from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = combinations([i for i in range(1, n + 1)], 2)
ans = -1
a, b = 0, 0
for x in p:
    chicken = [x[0], x[1]]

    dist = [-1] * (n + 1)
    dist[0] = 0
    dist[x[0]] = 0
    dist[x[1]] = 0
    q = deque()
    q.append(x[0])
    q.append(x[1])

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    if ans == -1 or ans > sum(dist):
        a = x[0]
        b = x[1]
        ans = sum(dist)
print(a, b, 2 * ans)
