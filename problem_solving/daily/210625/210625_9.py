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

def mst(edges):
    ans = 0
    res = []
    for i, x in edges.items():
        if deleted[i]:
            continue
        a, b = x[0], x[1]
        if find(a) != find(b):
            res.append(i)
            union(a, b)
            ans += i

    res.sort()
    check = True
    for i in range(1, n):
        if find(i) != find(i + 1):
            check = False
            break
    return check, res[0], ans

n, m, k = map(int, input().split())
edges = dict()
for i in range(1, m + 1):
    a, b = map(int, input().split())
    edges[i] = (a, b)

deleted = [False] * (m + 1)
res = 0
while True:
    parent = [i for i in range(n + 1)]
    ch, res, ans = mst(edges)
    deleted[res] = True
    if not ch:
        for _ in range(k):
            print(0, end=" ")
        break

    print(ans, end=" ")
    k -= 1

    if k == 0:
        break