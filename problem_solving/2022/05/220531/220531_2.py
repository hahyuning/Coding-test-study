from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(m):
    k, v = map(int, input().split())

    q = deque()
    visited = [False] * (n + 1)
    visited[v] = True
    for x, c in graph[v]:
        visited[x] = True
        q.append((x, c))

    ans = 0
    while q:
        now, c = q.popleft()

        if c >= k:
            ans += 1
            for nxt, nc in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, nc))
    print(ans)
