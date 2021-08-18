def check(mid):
    s = 0
    cnt = 0
    for v, c in beer:
        if c <= mid:
            s += v
            cnt += 1
        if cnt == n:
            break

    if cnt < n:
        return 0
    return s

n, m, k = map(int, input().split())
beer = []
rt = 0
for _ in range(k):
    v, c = map(int, input().split())
    rt = max(rt, c)
    beer.append((v, c))
beer.sort(reverse=True)

ans = -1
lt = 1

while lt <= rt:
    mid = (lt + rt) // 2
    s = check(mid)

    if s >= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)