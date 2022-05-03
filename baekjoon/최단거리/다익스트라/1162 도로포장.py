import heapq

if __name__ == '__main__':
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # cost[i][j]: i번째 도시로 가는데 포장된 도로를 j번 거쳤을 때의 최솟값
    dist = [[-1] * (k + 1) for _ in range(n + 1)]

    q = []
    heapq.heappush(q, (0, 1, 0))
    dist[1][0] = 0
    while q:
        cost, now, cnt = heapq.heappop(q)
        if dist[now][cnt] != -1 and dist[now][cnt] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            if dist[nxt][cnt] == -1 or nxt_cost < dist[nxt][cnt]:
                dist[nxt][cnt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt, cnt))

            if cnt + 1 <= k:
                if dist[nxt][cnt + 1] == -1 or cost < dist[nxt][cnt + 1]:
                    dist[nxt][cnt + 1] = cost
                    heapq.heappush(q, (cost, nxt, cnt + 1))

    ans = -1
    for i in range(k + 1):
        if dist[n][i] != -1:
            if ans == -1 or dist[n][i] < ans:
                ans = dist[n][i]
    print(ans)
