n = int(input())
a = list(map(int, input().split()))

ans = a[-1]
for i in range(n - 2, -1, -1):
    if ans % a[i] == 0:
        ans = (ans // a[i]) * a[i]
    else:
        ans = (ans // a[i] + 1) * a[i]
print(ans)