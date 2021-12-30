n = int(input())
a = [int(input()) for _ in range(n)]
a.reverse()
ans = 0
for i in range(1, n):
    diff = 0
    if a[i - 1] <= a[i]:
        diff = (a[i] - a[i - 1] + 1)
    a[i] -= diff
    ans += diff

print(ans)