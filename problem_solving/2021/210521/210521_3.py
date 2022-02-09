import heapq
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (v + 1)
dist[1] = 0
max_dist = 0

q = []
heapq.heappush(q, (0, 1))
while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for nxt in graph[now]:
        if dist[nxt] == -1 or cost + 1 < dist[nxt]:
            max_dist = max(max_dist, cost + 1)
            dist[nxt] = cost + 1
            heapq.heappush(q, (cost + 1, nxt))

ans = []
for i, x in enumerate(dist):
    if x == max_dist:
        ans.append(i)

print(ans[0], end=" ")
print(max_dist, end=" ")
print(len(ans))