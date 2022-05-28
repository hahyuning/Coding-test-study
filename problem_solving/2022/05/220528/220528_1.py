def check(mid):
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5

    return h1 * h2 / (h1 + h2)


x, y, c = map(float, input().split())
lt = 0
rt = min(x, y)

ans = 0
while rt - lt > 10 ** (-6):
    mid = (lt + rt) / 2
    if check(mid) >= c:
        ans = mid
        lt = mid
    else:
        rt = mid

print(ans)