from collections import deque

def bfs(start):
    check = [-1] * n
    q = deque()
    q.append(start)
    check[start] = 0

    while q:
        now = q.popleft()
        for nxt, cost in graph[now]:
            if check[nxt] == -1:
                check[nxt] = check[now] + cost
                q.append(nxt)
    return max(check)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, k = map(int, input().split())
parent = [i for i in range(n)]

edges = []
for _ in range(k):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

ans = 0
graph = [[] for _ in range(n)]
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
        graph[a].append((b, cost))
        graph[b].append((a, cost))

print(ans)

max_val = 0
for i in range(n):
    res = bfs(i)
    max_val = max(max_val, res)
print(max_val)