n = int(input())
a = list(map(int, input().split()))
a.sort()

total = sum(a)
ans = 0
for i in range(n):
    total -= a[i]
    ans += total * a[i]
print(ans)
