def check(mid):
    res = 0
    for x in interval:
        if x > mid:
            res += (x - 1) // mid
    return res

n, m, l = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(l - 1)
a.sort()
interval = []
for i in range(len(a) - 1):
    interval.append(a[i + 1] - a[i])

lt = 0
rt = l - 1
min_val = l
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res > m:
        lt = mid + 1
    else:
        min_val = mid
        rt = mid - 1

print(min_val)