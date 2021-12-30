n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    a = list(map(int, input().split()))
    cnt = 0
    now = 0
    for i in range(n):
        if now + a[i] <= m:
            now += a[i]
        else:
            cnt += 1
            now = a[i]

    if now > 0:
        cnt += 1
    print(cnt)