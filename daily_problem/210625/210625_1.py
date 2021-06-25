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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]

    ans = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            continue

        union(a, b)
        ans += 1
    print(ans)
