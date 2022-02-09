import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

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
s, e = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort(reverse=True)

parent = [i for i in range(n + 1)]
for x in edges:
    c, a, b = x
    if find(a) == find(b):
        continue
    union(a, b)
    if find(s) == find(e):
        print(c)
        break
else:
    print(0)