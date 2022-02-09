import sys
input = sys.stdin.readline
print = sys.stdout.write

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

n = int(input())
parent = dict()
cnt = dict()
for _ in range(n):
    order, *num = input().rstrip().split()

    if order == "I":
        a, b = num[0], num[1]
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1
        union(a, b)
    else:
        x = num[0]
        if x not in parent:
            parent[x] = x
            cnt[x] = 1

        print(str(cnt[find(x)]) + "\n")