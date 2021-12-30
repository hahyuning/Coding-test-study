n, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

occupied = [False] * (n + 1)

for i in range(q):
    ans = 0
    x = a[i]
    while x > 1:
        if occupied[x]:
            ans = x
        x //= 2
    occupied[a[i]] = True
    print(ans)