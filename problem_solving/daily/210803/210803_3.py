n = int(input())
a = list(map(int, input().split()))
d = [False] * 400001

ans = 0
for i in range(n):
    for j in range(i):
        if d[a[i] - a[j] + 200000]:
            ans += 1
            break

    for j in range(i + 1):
        d[a[i] + a[j] + 200000] = True
print(ans)
