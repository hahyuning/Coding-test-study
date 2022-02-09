n = int(input())
a = [float(input()) for _ in range(n)]
d = [0] * n
d[0] = a[0]

for i in range(1, n):
    d[i] = max(a[i], d[i - 1] * a[i])

print("%.3f" % max(d))