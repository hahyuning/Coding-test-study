import heapq
from collections import deque

def daijkstra():
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] != -1 and cost > dist[now]:
            continue

        for nxt, nxt_cost in graph[now]:
            if (now, nxt) in removed:
                continue

            nxt_cost += cost
            if dist[nxt] == -1 or nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))


def reverse_path():
    q = deque()
    q.append(d)

    while q:
        now = q.popleft()
        if now == s:
            continue

        for prev in range(len(reverse_graph[now])):
            if reverse_graph[now][prev] == -1:
                continue

            if dist[prev] + reverse_graph[now][prev] == dist[now]:
                if (prev, now) not in removed:
                    removed.append((prev, now))
                    q.append(prev)


if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        s, d = map(int, input().split())

        graph = [[] for _ in range(n)]
        reverse_graph = [[-1] * n for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))
            reverse_graph[v][u] = p

        dist = [-1] * n
        removed = []

        daijkstra()
        reverse_path()

        dist = [-1] * n
        daijkstra()
        print(dist[d])