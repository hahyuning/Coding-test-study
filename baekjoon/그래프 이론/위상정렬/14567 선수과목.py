from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = [0] * (n + 1)
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, 1))

while q:
    now, level = q.popleft()
    res[now] = level

    for nxt in graph[now]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append((nxt, level + 1))

print(*res[1:])