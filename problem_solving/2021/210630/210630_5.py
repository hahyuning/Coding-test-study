n = int(input())
m = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    a.sort()
    lt = 0
    rt = n - 1
    cnt = 0
    while lt < rt:
        tmp = a[lt] + a[rt]
        if tmp < m:
            lt += 1
        elif tmp > m:
            rt -= 1
        else:
            cnt += 1
            lt += 1
            rt -= 1
    print(cnt)