def check(mid):
    cnt = 0
    now = 0

    while now + mid <= n:
        tmp = dict()
        for i in range(now, now + mid):
            if a[i] not in tmp:
                tmp[a[i]] = i
            else:
                now = tmp[a[i]] + 1
                break
        else:
            cnt += 1
            now += mid

    return cnt

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

lt = 1
rt = n // m
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)

    if res >= m:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)