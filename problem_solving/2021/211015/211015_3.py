import math


def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx ** 2 + dy ** 2)

def dfs(now):
    check[now] = True
    for nxt in graph[now]:
        if check[nxt]:
            continue

        check[nxt] = True
        if parent[nxt] == -1 or dfs(parent[nxt]):
            parent[nxt] = now
            return True
    return False

n, m, s, v = map(int, input().split())
mouse = []
for _ in range(n):
    x, y = map(float, input().split())
    mouse.append((x, y))
shelter = []
for _ in range(m):
    x, y = map(float, input().split())
    shelter.append((x, y))

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        d = dist(mouse[i], shelter[j])
        if d <= s * v:
            graph[i].append(j + 100)

ans = n
parent = [-1] * 200
for i in range(n):
    check = [False] * 200
    ans -= dfs(i)
print(ans)