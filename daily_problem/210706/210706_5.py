import heapq

n, m = map(int, input().split())
# a: 시작, b: 도착, k: 출발 시간 차이, g: 방문 교차로 개수
a, b, k, g = map(int, input().split())
tmp = list(map(int, input().split()))
godula = dict()

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

s = -k
for i in range(g - 1):
    for j, cost in graph[tmp[i]]:
        if j == tmp[i + 1]:
            godula[(tmp[i], j)] = [s, s + cost]
            s += cost
            break

q = []
dist = [-1] * (n + 1)
dist[a] = 0
heapq.heappush(q, (0, a))

while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for nxt, nxt_cost in graph[now]:
        if (now, nxt) in godula:
            st, et = godula[(now, nxt)]
            if st <= cost < et:
                nxt_cost += et
            else:
                nxt_cost += cost
        elif (nxt, now) in godula:
            st, et = godula[(nxt, now)]
            if st <= cost < et:
                nxt_cost += et
            else:
                nxt_cost += cost
        else:
            nxt_cost += cost
        if nxt_cost < dist[nxt] or dist[nxt] == -1:
            dist[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, nxt))

print(dist[b])