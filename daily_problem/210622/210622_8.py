import heapq

t = int(input())
for _ in range(t):
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))

    dist = [-1] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            if dist[nxt] == -1 or nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    cnt = 0
    max_val = 0
    for i in range(1, n + 1):
        if dist[i] != -1:
            cnt += 1
            max_val = max(max_val, dist[i])

    print(cnt, max_val)