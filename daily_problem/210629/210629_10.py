def check(x):
    s = 0
    res = 1
    for y in a:
        if s + y <= x:
            s += y
        else:
            res += 1
            s = y
    return res

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

lt = max(a)
rt = sum(a)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res <= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)
