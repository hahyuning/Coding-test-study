for _ in range(3):
    n = int(input())
    a = []
    total = 0
    for _ in range(n):
        x, y = map(int, input().split())
        total += x * y
        a.append((x, y))

    if total % 2 == 1:
        print(0)
        continue

    d = [0] * 50001
    d[0] = 1
    for i in range(n):
        for j in range(50000, a[i][0] - 1, -1):
            if d[j - a[i][0]]:
                for k in range(a[i][1] + 1):
                    if j + k * a[i][0] <= 50000:
                        d[j + k * a[i][0]] = 1

    print(d[total // 2])





