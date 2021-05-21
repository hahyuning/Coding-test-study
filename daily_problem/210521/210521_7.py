import heapq
v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (v + 1)
dist[1] = 0

q = []
heapq.heappush(q, (0, 1))
while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for nxt in graph[now]:
        if dist[nxt] == -1 or cost + 1 < dist[nxt]:
            dist[nxt] = cost + 1
            heapq.heappush(q, (cost + 1, nxt))

ans = 0
for x in dist:
    if x != -1 and x <= 2:
        ans += 1
print(ans - 1)