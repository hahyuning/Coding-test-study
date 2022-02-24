n = int(input())
n %= 15 * (10 ** 5)
d = [0] * (n + 1)
if n == 0:
    print(0)
else:
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1000000

    print(d[n])