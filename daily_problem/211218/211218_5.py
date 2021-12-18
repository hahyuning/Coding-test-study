import sys
sys.setrecursionlimit(10 ** 5)

def dfs(now):
    visited[now] = True

    for nxt in tree[now]:
        if not visited[nxt]:
            res[nxt] += res[now]
            dfs(nxt)

n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    parent = a[i - 1]
    tree[parent].append(i)

res = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    res[i] += w

visited = [False] * (n + 1)
dfs(1)
print(*res[1:])