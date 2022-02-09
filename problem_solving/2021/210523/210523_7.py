n = int(input())
k = 10 ** 9

sign = False
if n > 0:
    sign = True

n = abs(n)
if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
elif n == 2:
    if sign:
        print(1)
        print(1)
    else:
        print(-1)
        print(1)
else:
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % k

    if sign:
        print(1)
        print(d[n])
    else:
        if n % 2 == 0:
            print(-1)
            print(d[n])
        else:
            print(1)
            print(d[n])