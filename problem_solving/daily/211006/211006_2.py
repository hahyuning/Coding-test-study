n = int(input())
if n == 2:
    res = [int(input()) for _ in range(n)]
    print(min(res))
else:
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        x = int(input())
        s[i] = s[i - 1] + x

    ans = 0
    for i in range(1, n):
        lt = i + 1
        rt = n

        while lt <= rt:
            mid = (lt + rt) // 2
            a = s[mid] - s[i - 1]
            b = s[n] - a

            if a < b:
                lt = mid + 1
            else:
                rt = mid - 1
            ans = max(ans, min(a, b))

    print(ans)