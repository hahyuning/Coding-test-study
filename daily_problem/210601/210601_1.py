import heapq, sys

def dijkstra(fro, to):
    dist = [-1] * (v + 1)
    path = [[] for _ in range(v + 1)]

    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0
    path[1].append(1)

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, new_cost in graph[now]:
            if now == fro and nxt == to:
                continue

            new_cost += cost
            if dist[nxt] == -1 or new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))

                path[nxt] = []
                for p in path[now]:
                    path[nxt].append(p)
                path[nxt].append(nxt)

    return [dist[v], path[v]]

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

d, p = dijkstra(-1, -1)
n = len(p)

ans = []
for i in range(1, n):
    d1, p1 = dijkstra(p[i - 1], p[i])
    if d1 == -1:
        print(-1)
        sys.exit(0)
    else:
        ans.append(d1 - d)

print(max(ans))
