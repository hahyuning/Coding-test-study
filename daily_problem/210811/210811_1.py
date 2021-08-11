n = int(input())
a = [0] + [int(input()) for _ in range(n)]
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + a[i]:
            d[i] = d[j] + a[i]

print(max(d))