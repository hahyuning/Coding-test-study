def check(x):
    res = 0
    for y in a:
        if y % x == 0:
            res += y // x
        else:
            res += y // x + 1
    return res

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

lt = 0
rt = max(a)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res <= n:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)

