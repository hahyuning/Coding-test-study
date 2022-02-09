import heapq

def dijkstra(i, start):
    q = []
    heapq.heappush(q, (0, start))
    dist[i][start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[i][now] != -1 and dist[i][now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost

            if nxt_cost < dist[i][nxt] or dist[i][nxt] == -1:
                dist[i][nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

n = int(input())
friends = list(map(int, input().split()))

m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[-1] * (n + 1) for _ in range(3)]
for i in range(3):
    dijkstra(i, friends[i])

max_val = -1
ans = 0
for i in range(1, n + 1):
    min_val = -1
    for j in range(3):
        if min_val == -1 or dist[j][i] < min_val:
            min_val = dist[j][i]

    if max_val == -1 or min_val > max_val:
        max_val = min_val
        ans = i
print(ans)