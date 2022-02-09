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

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

cycle = False
ans = 0
for i in range(1, e + 1):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find(a) == find(b):
        cycle = True
        ans = i
        break
    union(a, b)
print(ans)