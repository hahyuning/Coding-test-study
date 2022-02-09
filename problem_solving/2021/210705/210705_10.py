from collections import deque, defaultdict
import sys
input = sys.stdin.readline

v, k, e = map(int, input().split())
graph = defaultdict(list)
for cnt in range(v + 1, v + e + 1):
    a = list(map(int, input().split()))
    graph[cnt] = a
    for i in range(k):
        graph[a[i]].append(cnt)

dist = [-1] * (e + v + 1)
dist[1] = 1

q = deque()
q.append((1, 0))
while q:
    now, hyper = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            if hyper == 0:
                dist[nxt] = dist[now] + 1
            else:
                dist[nxt] = dist[now]
            q.append((nxt, 1 - hyper))
print(dist[v])