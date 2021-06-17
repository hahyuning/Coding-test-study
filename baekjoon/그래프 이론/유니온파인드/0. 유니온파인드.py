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

# 유니온 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find(i), end=" ")

print()

# 부모 테이블 내용 출력
for i in range(1, v + 1):
    print(parent[i], end=" ")