import heapq

def dijkstra(start, graph):
    q = []
    dist = [-1] * (n + 1)
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 continue
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if nxt_cost < dist[nxt] or dist[nxt] == -1:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
    return dist

# --------------------------------------------------------------------------
n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph1[b].append((a, c))
    graph2[a].append((b, c))

d1 = dijkstra(x, graph1)
d2 = dijkstra(x, graph2)
total = []
for x, y in zip(d1, d2):
    total.append(x + y)
print(max(total))