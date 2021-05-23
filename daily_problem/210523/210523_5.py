n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]
d = [0] * (n + 1)
d[0] = 1
d[1] = 1
for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

ans = 1
prev = 0
for x in vip:
    ans *= d[x - prev - 1]
    prev = x
ans *= d[n - prev]
print(ans)