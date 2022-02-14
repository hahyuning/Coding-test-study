n = int(input())
if n == 0:
    print(0)
else:
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = (a[i - 1] + a[i - 2]) % 1000000007

    print(a[n])
