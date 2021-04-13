n = int(input())
a = list(map(int, input().split()))
# d[i] : a[i]로 시작하는 가장 긴 감소하는 부분 수열의 길이
# d[i] = max(d[j]) + 1, i < j <= n - 1, a[i] > a[j]
d = [1] * n

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))