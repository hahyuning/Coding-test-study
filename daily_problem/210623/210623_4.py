from itertools import combinations
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

v = int(input())
parent = [i for i in range(v + 1)]
for _ in range(v - 2):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
c = combinations([i for i in range(1, v + 1)], 2)
for a, b in c:
    if find(a) == find(b):
        continue

    print(a, b)
    break