n = int(input())
a = [0] + list(map(int, input().split()))

d = [0] * (n + 1)
for i in range(n + 1):
    d[i] = (i - 1) * (1 + abs(a[i] - a[1]))

for i in range(1, n + 1):
    for j in range(1, i):
        d[i] = min(d[i], max(d[j], (i - j) * (1 + abs(a[i] - a[j]))))

lt = 0
rt = 10 ** 9
ans = -1
while lt <= rt:
    mid = (lt + rt) // 2
    if d[n] <= mid:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)