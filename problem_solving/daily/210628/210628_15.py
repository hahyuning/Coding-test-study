t = int(input())
for _ in range(t):
    n = int(input())

    lt = 1
    rt = n
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if mid * (mid + 1) // 2 > n:
            rt = mid - 1
        else:
            ans = mid
            lt = mid + 1
    print(ans)
