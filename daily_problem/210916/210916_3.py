t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == m:
        if sum(a) < k:
            print(1)
        else:
            print(0)
        continue

    a += a
    s = sum(a[0:m])
    rt = m - 1
    ans = 0
    for lt in range(n):
        if s < k:
            ans += 1

        s -= a[lt]
        rt += 1
        s += a[rt]
    print(ans)