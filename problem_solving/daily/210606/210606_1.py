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

n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]
for i in range(1, n + 1):
    g = list(map(int, input().split()))
    for j in range(1, n + 1):
        if g[j - 1] == 1:
            union(i, j)

order = list(map(int, input().split()))
x = find(order[0])
ans = True
for i in range(1, m):
    if find(order[i]) != x:
        ans = False
        break

print("YES" if ans else "NO")
