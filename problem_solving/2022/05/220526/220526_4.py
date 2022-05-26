def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n, s = map(int, input().split())
a = list(map(int, input().split()))
diff = []
for x in a:
    diff.append(abs(x - s))

ans = diff[0]
for i in range(n):
    ans = gcd(ans, diff[i])
print(ans)