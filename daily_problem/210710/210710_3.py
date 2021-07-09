from collections import deque

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

n, m, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

parent = [i for i in range(n + 1)]

res = -1
cnt = 0
q = deque()
q.append((1, 0))
check = [False] * (n + 1)
check[1] = True

while q:
    now, now_cost = q.popleft()
    if sum(check[1:]) == n:
        if res == -1 or now_cost < res:
            res = now_cost

    edges = graph[now]
    edges.sort()
    for cost, nxt in edges:
        if find(now) != find(nxt):
            union(now, nxt)
            q.append((nxt, now_cost + cost + t * cnt))
            cnt += 1
print(res)