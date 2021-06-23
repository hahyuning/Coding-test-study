import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]

t = int(input())
for _ in range(t):
    n = int(input())
    parent = dict()
    cnt = dict()
    for _ in range(n):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1

        union(a, b)
        print(cnt[find(a)])
