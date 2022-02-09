import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

n = int(input())
parent = dict()
for _ in range(n):
    a, b, x, y = map(int, input().split())
    for i in range(min(a, x), max(a, x) + 1):
        if (i, b) not in parent:
            parent[(i, b)] = (i, b)
        if (i, y) not in parent:
            parent[(i, y)] = (i, y)
    for j in range(min(b, y), max(b, y) + 1):
        if (a, j) not in parent:
            parent[(a, j)] = (a, j)
        if (x, j) not in parent:
            parent[(x, j)] = (x, j)

    for i in range(min(a, x), max(a, x) + 1):
        union((a, b), (i, b))
        union((a, b), (i, y))
    for j in range(min(b, y), max(b, y) + 1):
        union((a, b), (a, j))
        union((a, b), (x, j))

ans = []
check = False
for x in parent.keys():
    y = find(x)
    if x == (0, 0) or y == (0, 0):
        check = True

    if y not in ans:
        ans.append(y)

if check:
    print(len(ans) - 1)
else:
    print(len(ans))