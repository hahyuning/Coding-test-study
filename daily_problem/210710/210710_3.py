import sys
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

n = int(input())
parent = [i for i in range(n + 1)]
a = [input().rstrip() for _ in range(n)]
edges = []
all_cost = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == "0":
            continue

        if a[i][j].isupper():
            cost = ord(a[i][j]) - 38
        else:
            cost = ord(a[i][j]) - ord("a") + 1
        all_cost += cost
        if i != j:
            edges.append((cost, i, j))
edges.sort()

res = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost

for i in range(n - 1):
    if find(i) != find(i + 1):
        print(-1)
        break
else:
    print(all_cost - res)