import heapq

def dijkstra(start):
    q = []
    dist = [1e9] * (n + 1)
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
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v, w = map(int, input().split())
d1 = dijkstra(1)
d2 = dijkstra(v)
d3 = dijkstra(w)
ans = min(d1[v] + d2[w] + d3[n], d1[w] + d3[v] + d2[n])

print(ans if ans < 1e9 else -1)