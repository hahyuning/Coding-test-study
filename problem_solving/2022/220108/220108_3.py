n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

k = m
lt, rt = 0, -1
while rt < n - 1:
    if a[rt + 1] % 2 == 0:
        rt += 1
    else:
        if k > 0:
            k -= 1
            rt += 1
        else:
            while lt <= rt and a[lt] % 2 == 0:
                lt += 1
            if a[lt] % 2 != 0:
                k += 1
                lt += 1
    ans = max(ans, rt - lt + 1 - (m - k))
print(ans)