n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))

ans1 = 1
c = a[:]
c[0] = 1 - c[0]
c[1] = 1 - c[1]
for i in range(1, n):
    if c[i - 1] != b[i - 1]:
        ans1 += 1
        c[i - 1] = 1 - c[i - 1]
        c[i] = 1 - c[i]

        if i != n - 1:
            c[i + 1] = 1 - c[i + 1]

ans2 = 0
d = a[:]
for i in range(1, n):
    if d[i - 1] != b[i - 1]:
        ans2 += 1
        d[i - 1] = 1 - d[i - 1]
        d[i] = 1 - d[i]

        if i != n - 1:
            d[i + 1] = 1 - d[i + 1]

if c == b and d == b:
    print(min(ans1, ans2))
elif c == b:
    print(ans1)
elif d == b:
    print(ans2)
else:
    print(-1)