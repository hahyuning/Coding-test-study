n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

# LIS
# d[i]: a[i][1] 을 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
# d[i] = max(d[j] + 1), 0 <= j < i & a[j][1] < a[i][1]
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i][1] > a[j][1] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(n - max(d))

