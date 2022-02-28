import sys
sys.setrecursionlimit(10 ** 5)


def dfs(now):
    global order

    order += 1
    left[now] = order

    for nxt in tree[now]:
        if left[nxt] == 0:
            dfs(nxt)

    order += 1
    right[now] = order


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    v, *edges = map(int, input().split())
    for w in edges:
        if w != -1:
            tree[v].append(w)
    tree[v].sort()

root = int(input())
left = [0] * (n + 1)
right = [0] * (n + 1)
order = 0
dfs(root)

for i in range(1, n + 1):
    print(i, end=" ")
    print(left[i], end=" ")
    print(right[i])