import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    row_sum = []
    for row in a:
        row_sum.append(sum(row))
    col_sum = []
    for j in range(n):
        s = 0
        for i in range(n):
            s += a[i][j]
        col_sum.append(s)

    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        c = c2 - c1 + 1
        for i in range(r1, r2 + 1):
            row_sum[i] += c * v
        r = r2 - r1 + 1
        for j in range(c1, c2 + 1):
            col_sum[j] += r * v

    print(" ".join(map(str, row_sum)))
    print(" ".join(map(str, col_sum)))
