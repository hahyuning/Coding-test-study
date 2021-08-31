import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

res = []
while q:
    now = heapq.heappop(q)
    res.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            heapq.heappush(q, nxt)

print(*res)
