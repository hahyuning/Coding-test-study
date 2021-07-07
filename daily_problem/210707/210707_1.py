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

t = int(input())
for i in range(1, t + 1):
    v = int(input())
    e = int(input())
    parent = [i for i in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        union(a, b)

    print("Scenario " + str(i) + ":")
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()