n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

ans = 0
for i in range(1, n + 1):
    ans += abs(i - a[i - 1])
print(ans)