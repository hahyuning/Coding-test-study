import heapq


def dijkstra(start):
    dist = [-1] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)

        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            if dist[nxt] == -1 or nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    return dist


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    destination = [int(input()) for _ in range(t)]
    destination.sort()

    dist1 = dijkstra(s)
    dist2 = dijkstra(g)
    dist3 = dijkstra(h)

    res = []
    for e in destination:
        if dist1[g] != -1 and dist2[h] != -1 and dist3[e] != -1 and dist1[e] != -1:
            if dist1[g] + dist2[h] + dist3[e] == dist1[e]:
                res.append(e)

        if dist1[h] != -1 and dist3[g] != -1 and dist2[e] != -1 and dist1[e] != -1:
            if dist1[h] + dist3[g] + dist2[e] == dist1[e]:
                if e not in res:
                    res.append(e)
    print(*res)
