def top_down(n, a, b, c):
    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0

    if a < 0 or b < 0 or c < 0:
        return 0

    if d[n][a][b][c] != -1:
        return d[n][a][b][c]

    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i + j + k == 0:
                    continue

                ans += top_down(n - 1, a - i, b - j, c - k)
    ans %= 1000000007
    d[n][a][b][c] = ans
    return d[n][a][b][c]

n, a, b, c = map(int, input().split())
d = [[[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
print(top_down(n, a, b, c))