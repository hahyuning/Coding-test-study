import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [-1] * (n + 1)
trace = [[] for _ in range(n + 1)]
start = 1

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

ans = []
for x in trace:
    for i in range(len(x) - 1):
        a, b = x[i], x[i + 1]
        if (a, b) not in ans and (b, a) not in ans:
            ans.append((a, b))
print(len(ans))
for a, b in ans:
    print(a, b)