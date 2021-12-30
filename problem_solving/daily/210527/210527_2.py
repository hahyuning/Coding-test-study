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

while True:
    v, e = map(int, input().split())
    if v == 0 and e == 0:
        break

    total = 0
    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        total += cost
        edges.append((cost, a, b))
    edges.sort()

    parent = [i for i in range(v)]
    res = 0
    for edge in edges:
        cost, a, b = edge
        if find(a) != find(b):
            union(a, b)
            res += cost

    print(total - res)