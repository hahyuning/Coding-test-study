def check(mid):
    res = 0
    while mid > 0:
        res += mid // 5
        mid //= 5
    return res

n = int(input())
lt = 0
rt = 10 ** 9

ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) < n:
        lt = mid + 1
    else:
        ans = mid
        rt = mid - 1

print(ans if check(ans) == n else -1)
