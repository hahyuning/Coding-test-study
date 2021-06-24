from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
outdegree = [0] * (n + 1)
indegree = [0] * (n + 1)
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    indegree[y] += 1
    outdegree[x] += 1

q = deque()
q.append(n)
res = [0] * (n + 1)
res[n] = 1

while q:
    now = q.popleft()
    for nxt, cost in graph[now]:
        res[nxt] += res[now] * cost
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

ans = []
for i in range(1, n + 1):
    if outdegree[i] == 0:
        print(i, res[i])

