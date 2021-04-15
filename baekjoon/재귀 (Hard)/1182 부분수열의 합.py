def dfs(index, sum):
    global cnt
    if index == n and sum == s:
        cnt += 1
        return

    if index == n and sum != s:
        return

    dfs(index + 1, sum + a[index])
    dfs(index + 1, sum)

n, s = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
dfs(0, 0)

if s == 0:
    cnt -= 1
print(cnt)