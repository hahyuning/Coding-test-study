n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = []
c = []
for x in a:
    if x % 10 == 0:
        b.append(x)
    else:
        c.append(x)

ans = 0
for x in b:
    k = x // 10

    if k == 0:
        continue

    if k - 1 <= m:
        ans += k
        m -= (k - 1)
    else:
        ans += m
        m = 0

for x in c:
    k = x // 10

    if m == 0:
        break

    if k <= m:
        ans += k
        m -= k
    else:
        ans += m
        m = 0

print(ans)


