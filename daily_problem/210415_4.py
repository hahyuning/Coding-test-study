ans = 0
now = 0
for _ in range(10):
    a, b = map(int, input().split())
    now = now - a + b
    ans = max(ans, now)

print(ans)