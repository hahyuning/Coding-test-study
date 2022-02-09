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
    edges = []
    parent = [i for i in range(r * c)]
    for i in range(r):
        tmp = list(map(int, input().split()))
        for j in range(c - 1):
            edges.append((tmp[j], i * c + j, i * c + j + 1))
    for i in range(r - 1):
        tmp = list(map(int, input().split()))
        for j in range(c):
            edges.append((tmp[j], i * c + j, (i + 1) * c + j))
    edges.sort()

    res = 0
    for c, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            res += c
    print(res)