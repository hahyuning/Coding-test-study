n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

lt = 0
ans = 0
for lt in range(n - 1):
    rt = lt + 1
    if a[lt] >= m:
        break
    while rt < n and a[lt] + a[rt] <= m:
        ans += 1
        rt += 1
print(ans)
