while True:
    n = int(input())
    if n == 0:
        break

    a = [int(input()) for _ in range(n)]
    for i in range(1, n):
        a[i] = max(a[i], a[i - 1] + a[i])
    print(max(a))