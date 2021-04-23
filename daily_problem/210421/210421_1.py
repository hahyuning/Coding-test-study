from collections import deque

def bfs():
    check = [False] * (n + 1)
    q = deque()
    q.append(v)
    check[v] = True

    ans = [v]
    while q:
        now = q.popleft()
        for next in graph[now]:
            if check[next] == False:
                q.append(next)
                check[next] = True
                ans.append(next)
    return ans

def dfs(x):
    global ans, visited
    visited[x] = True
    ans.append(x)

    for y in graph[x]:
        if visited[y] == False:
            dfs(y)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

# dfs 수행
visited = [False] * (n + 1)
ans = []
dfs(v)
print(" ".join(map(str, ans)))

# bfs 수행
ans = bfs()
print(" ".join(map(str, ans)))