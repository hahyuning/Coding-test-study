def check(x):
    res = 0
    for time in t:
        res += x // time
    return res

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

ans = 0
lt = 0
rt = max(t) * (m // len(t)) + 1
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res < m:
        lt = mid + 1
    else:
        rt = mid - 1
        ans = mid
print(ans)

