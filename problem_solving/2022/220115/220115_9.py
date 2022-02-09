n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
if n % 2 == 0:
    for i in range(n // 2):
        ans = max(ans, a[i] + a[-i - 1])
else:
    ans = max(ans, a.pop())
    for i in range((n - 1) // 2):
        ans = max(ans, a[i] + a[-i - 1])

print(ans)