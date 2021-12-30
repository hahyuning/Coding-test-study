def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    edges = dict()
    parent = dict()
    for i in range(r):
        for j in range(c):
            parent[(i, j)] = (i, j)
    for i in range(r):
        tmp = list(map(int, input().split()))
        for j in range(c - 1):
            edges[(i, j, i, j + 1)] = tmp[j]
    for i in range(r - 1):
        tmp = list(map(int, input().split()))
        for j in range(c):
            edges[(i, j, i + 1, j)] = tmp[j]
    sorted_edges = sorted(edges.items(), key=lambda x:x[1])

    res = 0
    for edge, cost in sorted_edges:
        a, b, c, d = edge
        if find((a, b)) != find((c, d)):
            union((a, b), (c, d))
            res += cost
    print(res)