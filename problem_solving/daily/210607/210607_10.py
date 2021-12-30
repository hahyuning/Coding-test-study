import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, input().split())
dist = [-1] * (n + 1)
dist[s] = 0
q = []
heapq.heappush(q, (0, s))

while q:
    cost, now = heapq.heappop(q)
    cost = -cost
    if dist[now] != -1 and cost < dist[now]:
        continue

    for nxt, nxt_cost in graph[now]:
        if cost != 0:
            nxt_cost = min(nxt_cost, cost)
        if dist[nxt] == -1 or nxt_cost > dist[nxt]:
            dist[nxt] = nxt_cost
            heapq.heappush(q, (-nxt_cost, nxt))

print(dist[e])