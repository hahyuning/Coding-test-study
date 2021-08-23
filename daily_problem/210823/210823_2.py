a, b, c, x, y = map(int, input().split())

ans = x * a + y * b
for i in range(1, 100001):
    tmp = 2 * i * c + max(0, x - i) * a + max(0, y - i) * b
    ans = min(ans, tmp)
print(ans)