from collections import deque

def bfs(s, e):
    q = deque()
    dist = [-1] * (n + 1)
    q.append(s)
    dist[s] = 0

    while q:
        now = q.popleft()
        if now == e:
            return dist[now]
        for nxt, cost in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + cost
                q.append(nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))