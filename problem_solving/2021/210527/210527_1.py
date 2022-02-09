import math

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

def dist(x, y, a, b):
    d = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    return d

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        d = dist(stars[i][0], stars[i][1], stars[j][0], stars[j][1])
        edges.append((d, i, j))
edges.sort()

parent = [i for i in range(n)]
res = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += cost

print(format(res, ".2f"))

