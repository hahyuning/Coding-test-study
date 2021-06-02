import heapq
import math

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 continue
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if nxt_cost < dist[nxt] or dist[nxt] == -1:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

n, m = map(int, input().split())
l = float(input())
graph = [[] for _ in range(n + 1)]
v = [(-1, -1)]

for _ in range(n):
    a, b = map(int, input().split())
    v.append((a, b))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 0))
    graph[b].append((a, 0))

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i == j:
            continue

        d = math.sqrt((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2)
        if d <= l:
            graph[i].append((j, d))
            graph[j].append((i, d))

dist = [-1] * (n + 1)
dijkstra(1)
print(int(dist[n] * 1000))


while True:
    x = list(map(int, input().split()))
    x.sort()
    a, b, c = x
    if a == 0 and b == 0 and c == 0:
        break
    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")