def count(mid):
    s = 0
    cnt = 1
    for x in a:
        s += x
        if s >= mid:
            cnt += 1
            s = 0
    return cnt

n, k = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = sum(a)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = count(mid)
    if res > k:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(ans)