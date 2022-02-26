n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

# (j - i) * (1 + |ai - aj|)

# d[i]: i번째 돌까지 이동하는데 필요한 힘의 최댓값의 최솟값
# d[i] = min(d[i], max(d[j], (j - i) * (1 + |ai - aj|))) for j st j < i
d = [0] * (n + 1)
for i in range(n + 1):
    d[i] = (i - 1) * (1 + abs(a[i] - a[1]))

for i in range(1, n + 1):
    for j in range(1, i):
        d[i] = min(d[i], max(d[j], (i - j) * (1 + abs(a[i] - a[j]))))

print("YES" if d[n] <= k else "NO")