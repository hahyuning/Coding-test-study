import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [-1] * (n + 1)
trace = [[] for _ in range(n + 1)]
start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
dist[start] = 0
trace[start].append(start)
while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for nxt, nxt_cost in graph[now]:
        nxt_cost += cost
        if dist[nxt] == -1 or nxt_cost < dist[nxt]:
            dist[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, nxt))
            # 경로 갱신
            trace[nxt] = []
            for p in trace[now]:
                trace[nxt].append(p)
            trace[nxt].append(nxt)

print(dist[end])
print(len(trace[end]))
print(*trace[end])