from collections import deque

n, root = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = deque()
q.append((root, 0))
check = [False] * (n + 1)
check[root] = True
giga_node = 0
giga_len = 0

if len(graph[root]) >= 2:
    giga_len = 0
    giga_node = root
else:
    while q:
        now, c = q.popleft()
        giga_len = c
        giga_node = now
        if len(graph[now]) > 2:
            break

        for nxt, nc in graph[now]:
            if not check[nxt]:
                check[nxt] = True
                q.append((nxt, c + nc))

q = deque()
dist = [-1] * (n + 1)
q.append((giga_node, 0))
dist[giga_node] = 0
while q:
    now, c = q.popleft()
    for nxt, nc in graph[now]:
        if dist[nxt] == -1 and not check[nxt]:
            check[nxt] = True
            dist[nxt] = c + nc
            q.append((nxt, c + nc))
print(giga_len, max(dist))