from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
q.append(1)
dist = [-1] * (n + 1)
dist[1] = 0
max_node = 0
max_dist = 0
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

            if dist[nxt] > max_dist:
                max_dist = dist[nxt]
                max_node = nxt

q = deque()
q.append(max_node)
dist = [-1] * (n + 1)
dist[max_node] = 0
max_dist = 0
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

            if dist[nxt] > max_dist:
                max_dist = dist[nxt]
print((max_dist + 1) // 2)
