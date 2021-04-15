def dfs(w, sum):
    global ans
    if len(w) == 2:
        ans = max(ans, sum)
        return

    for i in range(1, len(w) - 1):
        dfs(w[:i] + w[i + 1:], sum + w[i - 1] * w[i + 1])

n = int(input())
w = list(map(int, input().split()))

ans = 0
dfs(w, 0)
print(ans)