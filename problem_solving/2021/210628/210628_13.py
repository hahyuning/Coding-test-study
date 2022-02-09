def check(x):
    res = 0
    for y in l:
        if y < x:
            continue
        res += y // x
    return res

m, n = map(int, input().split())
l = list(map(int, input().split()))

lt = 1
rt = max(l)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res >= m:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(ans)

