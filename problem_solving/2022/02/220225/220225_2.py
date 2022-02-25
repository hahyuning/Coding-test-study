import heapq, sys
input = sys.stdin.readline


def dijkstra(mid):
    q = []
    heapq.heappush(q, (0, a))
    dist = [-1] * (n + 1)
    dist[a] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            if nxt_cost > mid:
                continue

            nxt_cost += cost
            if nxt_cost < dist[nxt] or dist[nxt] == -1:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    if dist[b] != -1 and dist[b] <= c:
        return True
    return False


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))


lt = 0
rt = 20
ans = -1
while lt <= rt:
    mid = (lt + rt) // 2
    if dijkstra(mid):
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)