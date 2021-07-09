def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    # 더 작은 쪽을 루트로 만든다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
w = [int(input()) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n + 1)]
edges = []
for i in range(n):
    edges.append((w[i], i, n))

for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        edges.append((p[i][j], i, j))
edges.sort()

res = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost
print(res)
