import heapq

def dijkstra(start):
    q = []
    dist = [-1] * (v + 3)
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, ncost in graph[now]:
            if nxt in [v + 1, v + 2]:
                continue

            ncost += cost
            if dist[nxt] == -1 or ncost < dist[nxt]:
                dist[nxt] = ncost
                heapq.heappush(q, (ncost, nxt))
    return dist

v, e = map(int, input().split())
graph = [[] for _ in range(v + 3)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

m, x = map(int, input().split())
mac = list(map(int, input().split()))
s, y = map(int, input().split())
star = list(map(int, input().split()))

# v + 1: 맥도날드 본부
# v + 2: 스타벅스 본부
for i in mac:
    graph[i].append((v + 1, 0))
    graph[v + 1].append((i, 0))
for j in star:
    graph[j].append((v + 2, 0))
    graph[v + 2].append((j, 0))

dist1 = dijkstra(v + 1)
dist2 = dijkstra(v + 2)

ans = -1
for i in range(1, v + 1):
    if i not in mac and i not in star:
        if dist1[i] == -1 or dist2[i] == -1:
            continue

        if dist1[i] <= x and dist2[i] <= y:
            tmp = dist1[i] + dist2[i]
            if ans == -1 or tmp < ans:
                ans = tmp
print(ans)