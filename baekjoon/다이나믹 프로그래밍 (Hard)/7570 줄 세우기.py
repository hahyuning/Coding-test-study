n = int(input())
a = list(map(int, input().split()))

# 1번 방법
d = [0] * (n + 1)
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

# 2번 방법
d = [0] * (n + 1)
for i in a:
    if d[i - 1] == 0:
        d[i] += 1
    else:
        d[i] = d[i - 1] + 1

print(n - max(d))
