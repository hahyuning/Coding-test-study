import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [[INF] * k for _ in range(n + 1)]
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

heapq.heappush(q, (0, 1))
dist[1][0] = 0
while q:
    cost, now = heapq.heappop(q)
    for nxt, nxt_cost in graph[now]:
        nxt_cost += cost
        if nxt_cost < dist[nxt][-1]:
            dist[nxt][-1] = nxt_cost
            dist[nxt].sort()
            heapq.heappush(q, (nxt_cost, nxt))

for i in range(1, n + 1):
    if dist[i][-1] == INF:
        print(-1)
    else:
        print(dist[i][-1])