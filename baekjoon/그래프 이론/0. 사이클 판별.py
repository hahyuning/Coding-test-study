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
# 부모를 자기 자신으로 초기화
parent = [i for i in range(v + 1)]

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find(a) == find(b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 유니온 수행
    union(a, b)
