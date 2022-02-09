import sys
input = sys.stdin.readline

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

v = int(input())
parent = [i for i in range(v)]
cost_matrix = [list(map(int, input().split())) for _ in range(v)]
edges = []
for i in range(v):
    for j in range(i, v):
        if i == j:
            continue
        edges.append((cost_matrix[i][j], i, j))

# 비용 순으로 정렬
edges.sort()

# 최종 비용
res = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        res += cost

print(res)