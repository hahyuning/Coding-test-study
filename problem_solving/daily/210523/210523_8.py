import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    a[0][2] += a[0][1]
    a[1][0] += a[0][1]
    a[1][1] += min(a[0][1], a[0][2], a[1][0])
    a[1][2] += min(a[0][1], a[0][2], a[1][1])

    for i in range(2, n):
        for j in range(3):
            if j == 0:
                a[i][j] += min(a[i - 1][j], a[i - 1][j + 1])
            elif j == 1:
                a[i][j] += min(a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i][j - 1])
            else:
                a[i][j] += min(a[i - 1][j - 1], a[i - 1][j], a[i][j - 1])

    print(str(t) + ".", end=" ")
    print(a[n - 1][1])
    t += 1