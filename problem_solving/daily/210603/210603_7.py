import heapq
from collections import defaultdict

n, d = map(int, input().split())
road = defaultdict(list)
for _ in range(n):
    s, e, l = map(int, input().split())
    if e <= d:
        road[s].append((e, l))

dist = [-1] * (d + 1)
dist[0] = 0
q = []
heapq.heappush(q, (0, 0))

while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    if now + 1 <= d:
        if dist[now + 1] == -1 or dist[now + 1] > dist[now] + 1:
            dist[now + 1] = dist[now] + 1
            heapq.heappush(q, (cost + 1, now + 1))

    if now in road:
        for nxt, n_cost in road[now]:
            n_cost += cost
            if dist[nxt] == -1 or dist[nxt] > n_cost:
                dist[nxt] = n_cost
                heapq.heappush(q, (n_cost, nxt))

print(dist[d])

