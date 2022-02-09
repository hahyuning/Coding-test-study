n, k = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
s = sum(a[lt:lt + k])
ans = s
if k == 1:
    print(max(a))
else:
    while True:
        s -= a[lt]
        if lt + k >= n:
            break
        s += a[lt + k]
        ans = max(ans, s)
        lt += 1
    print(ans)
