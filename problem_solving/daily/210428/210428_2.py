from itertools import permutations

n, m = map(int, input().split())
num = [i for i in range(1, n + 1)]
p_num = permutations(num)

for p in p_num:
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[0][i] = p[i]

    for i in range(1, n):
        for j in range(n - i):
            a[i][j] = a[i - 1][j] + a[i - 1][j + 1]

    if a[n - 1][0] == m:
        print(" ".join(map(str, p)))
        break