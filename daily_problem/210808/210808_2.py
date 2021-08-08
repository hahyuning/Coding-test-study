def check(mid):
    res = 0
    for x in a:
        res += mid // x
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = max(a) * m
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)

    if res >= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)