def check(mid):
    res = 0
    for x in interval:
        if x > mid:
            if x % mid == 0:
                res += x // mid - 1
            else:
                res += x // mid
    return res

n, m, l = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(l)
a.sort()
interval = []
for i in range(len(a) - 1):
    interval.append(a[i + 1] - a[i])

lt = 1
rt = l
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res > m:
        lt = mid + 1
    else:
        ans = mid
        rt = mid - 1

print(ans)