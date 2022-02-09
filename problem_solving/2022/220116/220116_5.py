def fractal(len, x, y):
    if len == 1:
        return 0
    bd = len // n

    if bd * (n - k) // 2 <= x < bd * (n + k) // 2 and bd * (n - k) // 2 <= y < bd * (n + k) // 2:
        return 1
    return fractal(bd, x % bd, y % bd)

s, n, k, r1, r2, c1, c2 = map(int, input().split())
len = n ** s

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(fractal(len, i, j), end="")
    print()