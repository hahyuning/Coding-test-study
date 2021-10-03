def dfs(idx, res):
    global ans

    if idx >= n:
        ans = max(ans, res)
        return

    for i in range(idx, n):
        dfs(i + 2, res + a[i][2])

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

ans = 0
dfs(0, 0)
print(ans)