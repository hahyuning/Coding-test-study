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

p, w = map(int, input().split())
parent = [i for i in range(p + 1)]
c, v = map(int, input().split())
ans = 1000

edges = []
for _ in range(w):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort(key=lambda x:x[0], reverse=True)

for cost, a, b in edges:
    if find(c) != find(v):
        union(a, b)
        ans = min(ans, cost)
    else:
        break
print(ans)