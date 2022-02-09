n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = 0
now = []
ans = 0
for lt in range(n):
    while rt < n and a[rt] not in now:
        now.append(a[rt])
        rt += 1

    ans += len(now)
    now.remove(a[lt])
print(ans)

