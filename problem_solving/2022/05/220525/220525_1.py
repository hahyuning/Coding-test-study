import sys

def dfs(now, friends):
    if now >= n:
        if len(friends) >= k:
            for i in range(k):
                print(friends[i])
            sys.exit(0)
        return

    flag = False
    for j in friends:
        if not graph[now + 1][j]:
            flag = True

    if not flag:
        dfs(now + 1, friends + [now + 1])

    dfs(now + 1, friends)


k, n, f = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(f):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

for i in range(1, n + 1):
    dfs(i, [i])

print(-1)