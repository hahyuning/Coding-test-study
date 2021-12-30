import heapq

def dijkstr(start, end):
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
    return dist[end]

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

if dijkstr(1, n) == dijkstr(1, k) + dijkstr(k, n):
    print("SAVE HIM")
else:
    print("GOOD BYE")