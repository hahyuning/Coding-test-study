def check(mid):
    min_sum = 0
    more = 0
    for l, r in a:
        if mid < l:
            return False
        more += min(mid, r) - l
        min_sum += l

    if more >= t - min_sum:
        return True
    return False

n, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
min_val = 0
for l, r in a:
    max_val += r
    min_val += l

if t > max_val or min_val > t:
    print(-1)
else:
    rt = t
    lt = 0
    ans = -1
    while lt <= rt:
        mid = (lt + rt) // 2
        if check(mid):
            ans = mid
            rt = mid - 1
        else:
            lt = mid + 1

    print(ans)