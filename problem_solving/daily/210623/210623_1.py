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

g = int(input())
p = int(input())
airport = []
for _ in range(p):
    x = int(input())
    airport.append(x)

# 부모를 자기 자신으로 초기화
parent = dict()
for i in range(g + 1):
    parent[i] = i

cnt = 0
for i in airport:
    x = find(i)
    if x == 0:
        break
    union(x, x - 1)
    cnt += 1
print(cnt)