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

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

friend = []
ans = 0
for i in range(1, n + 1):
    x = find(i)
    if x not in friend:
        min_cost = 10000
        for j in range(1, n + 1):
            y = find(j)
            if x == y:
                min_cost = min(min_cost, cost[j])
        ans += min_cost
        friend.append(x)

if ans <= k:
    print(ans)
else:
    print("Oh no")