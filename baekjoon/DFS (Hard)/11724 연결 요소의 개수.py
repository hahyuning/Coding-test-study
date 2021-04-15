from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def dfs(x):
    global visited
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

answer = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        answer += 1
print(answer)