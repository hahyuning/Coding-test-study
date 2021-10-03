t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    cnt = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if int((i ** 2 + j ** 2 + m) / (i * j)) == (i ** 2 + j ** 2 + m) / (i * j):
                cnt += 1


    print(cnt)