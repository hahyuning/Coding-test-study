def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

b = []
for i in range(n - 1):
    b.append(a[i + 1] - a[i])
b.sort()

div = b[0]
for i in range(len(b) - 1):
    div = gcd(b[i + 1], div)

ans = 0
for x in b:
    ans += x // div - 1
print(ans)
