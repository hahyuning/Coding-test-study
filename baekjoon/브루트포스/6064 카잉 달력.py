t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)