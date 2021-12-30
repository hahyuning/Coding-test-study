from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    x, *info = map(int, input().split())
    for i in range(0, len(info) - 2, 2):
        graph[x].append((info[i], info[i + 1]))

q = deque()
q.append(1)
dist = [-1] * (v + 1)
dist[1] = 0
max_node = 0
max_dist = 0
while q:
    now = q.popleft()
    for nxt, cost in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + cost
            q.append(nxt)

            if dist[nxt] > max_dist:
                max_dist = dist[nxt]
                max_node = nxt

q = deque()
q.append(max_node)
dist = [-1] * (v + 1)
dist[max_node] = 0
max_dist = 0
while q:
    now = q.popleft()
    for nxt, cost in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + cost
            q.append(nxt)

            if dist[nxt] > max_dist:
                max_dist = dist[nxt]
print(max_dist)