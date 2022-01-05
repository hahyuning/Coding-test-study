a, b, c, m = map(int, input().split())
now = 0
ans = 0
for i in range(24):
    if now + a <= m:
        ans += b
        now += a
    else:
        now = max(0, now - c)
print(ans)