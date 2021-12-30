import math
# 원소가 속한 집합의 루트 노드 찾기
# 경로 압축 기법: 파인드 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신
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

#----------------------------------------------------------------
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

location = [(-1, -1)]
for _ in range(v):
    a, b = map(int, input().split())
    location.append((a, b))

connected = []
for _ in range(e):
    a, b = map(int, input().split())
    if b < a:
        a, b = b, a
    connected.append((a, b))

edges = []
for i in range(1, v + 1):
    for j in range(i, v + 1):
        if i != j and (i, j) not in connected:
            cost = math.sqrt((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2)
            edges.append((cost, i, j))
        elif (i, j) in connected:
            union(i, j)

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

print("{:.2f}".format(res))