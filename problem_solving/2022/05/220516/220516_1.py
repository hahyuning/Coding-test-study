import heapq, sys
input = sys.stdin.readline


def dijkstra():
    q = []
    dist = [-1] * (n + 1)

    for x in interview:
        heapq.heappush(q, (0, x))
        dist[x] = 0

    while q:
        cost, now = heapq.heappop(q)

        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost

            if dist[nxt] == -1 or dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    return dist


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[v].append((u, c))

    interview = list(map(int, input().split()))

    dist = dijkstra()
    max_dist = max(dist)
    print(dist.index(max_dist))
    print(max_dist)
