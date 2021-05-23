n = int(input())
if n == 1:
    print(0)
    print(1)
elif n == 2:
    print(1)
    print(str(2) + " " + str(1))
elif n == 3:
    print(1)
    print(str(3) + " " + str(1))
else:
    # d[i]: i를 1로 만들때 필요한 최솟값
    d = [0] * (n + 1)
    v = [0] * (n + 1)
    d[2] = 1
    v[2] = 1
    d[3] = 1
    v[3] = 1

    for i in range(4, n + 1):
        d[i] = d[i - 1] + 1
        v[i] = i - 1
        if i % 3 == 0:
            if d[i] > d[i // 3] + 1:
                d[i] = d[i // 3] + 1
                v[i] = i // 3
        if i % 2 == 0:
            if d[i] > d[i // 2] + 1:
                d[i] = d[i // 2] + 1
                v[i] = i // 2

    print(d[n])
    print(n, end=" ")
    while v[n] > 1:
        print(v[n], end=" ")
        n = v[n]
    print(1)

