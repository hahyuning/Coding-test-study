n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)

ans = 0
for i in range(1, n + 1):
    if a[i - 1] - (i - 1) >= 0:
        ans += a[i - 1] - (i - 1)
print(ans)