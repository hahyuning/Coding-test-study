n, k = map(int, input().split())
min_val = (k * (k + 1)) // 2
if n < min_val:
    print(-1)
else:
    if (n - min_val) % k == 0:
        print(k - 1)
    else:
        print(k)