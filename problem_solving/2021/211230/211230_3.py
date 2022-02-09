import sys

def dfs(l):
    if l == 2 * n:
        print(*ans)
        sys.exit(0)

    if ans[l] != -1:
        dfs(l + 1)
        return

    for i in range(n):
        if not visited[i] and l + a[i] + 1 < 2 * n and ans[l + a[i] + 1] == -1:
            visited[i] = True
            ans[l] = a[i]
            ans[l + a[i] + 1] = a[i]
            dfs(l + 1)
            ans[l] = -1
            ans[l + a[i] + 1] = -1
            visited[i] = False

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = [-1] * (2 * n)
visited = [False] * (2 * n)
dfs(0)
print(-1)