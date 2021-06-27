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

n, m = map(int, input().split())
edges = []
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    c = 1 - c
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(m + 1)]
min_val = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        min_val += cost

edges.sort(reverse=True)
parent = [i for i in range(m + 1)]
max_val = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        max_val += cost

max_val = max_val ** 2
min_val = min_val ** 2
print(max_val - min_val)