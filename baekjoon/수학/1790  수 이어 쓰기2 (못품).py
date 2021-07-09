n, k = map(int, input().split())

num = 0
for i in range(10):
    tmp = (10 ** i) * 9 * (i + 1)
    if k <= tmp:
        if k % (i + 1) == 0:
            num += k // (i + 1)
        else:
            num += (k // (i + 1) + 1)
        str_num = str(num)
        if num <= n:
            idx = k % (i + 1)
            idx += i
            print(str_num[idx % (i + 1)])
            break
        else:
            print(-1)
            break
    else:
        k -= tmp
        num += (10 ** i) * 9