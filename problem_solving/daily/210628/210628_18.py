def check(mid):
    cnt = 1
    max_val = a[0]
    min_val = a[0]

    for i in range(1, n):
        max_val = max(max_val, a[i])
        min_val = min(min_val, a[i])
        if max_val - min_val > mid:
            max_val = a[i]
            min_val = a[i]
            cnt += 1
    return cnt

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 10000
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = check(mid)
    if cnt > m:
        lt = mid + 1
    else:
        ans = mid
        rt = mid - 1
print(ans)