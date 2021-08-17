import sys
sys.setrecursionlimit(10 ** 5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
enemy = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(0)
        break
    else:
        aa = enemy[a]
        bb = enemy[b]

        # a의 적을 b의 동지로 설정
        if aa != 0:
            union(aa, b)
        else:
            enemy[a] = b
        # b의 적을 a의 동지로 설정
        if bb != 0:
            union(a, bb)
        else:
            enemy[b] = a
else:
    print(1)