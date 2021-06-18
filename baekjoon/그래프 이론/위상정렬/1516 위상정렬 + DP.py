from collections import deque

v = int(input())
indegree = [0] * v
graph = [[] for _ in range(v)]
outgraph = [[] for _ in range(v)]
cost = [0] * v
dist = [0] * v
for i in range(v):
    c, *tmp = list(map(int, input().split()))
    cost[i] = c
    for x in tmp:
        if x != -1:
            graph[x - 1].append(i)
            outgraph[i].append(x - 1)
            indegree[i] += 1

q = deque()
for i in range(v):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    if not outgraph[now]:
        dist[now] = cost[now]
    else:
        for x in outgraph[now]:
            dist[now] = max(dist[now], dist[x] + cost[now])

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for x in dist:
    print(x)
