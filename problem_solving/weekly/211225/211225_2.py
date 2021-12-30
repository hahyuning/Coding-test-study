n = int(input())
a = list(map(int, input().split()))

s = [a[0]]
for i in range(1, n):
    s.append(s[i - 1] + a[i])

ans = 0
for i in range(n):
    ans += a[i] * (s[n - 1] - s[i])
print(ans)