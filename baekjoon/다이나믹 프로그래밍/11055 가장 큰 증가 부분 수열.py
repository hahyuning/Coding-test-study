n = int(input())
a = list(map(int, input().split()))
# d[i] : a[i]를 마지막으로 하는 가장 큰 증가하는 부분 수열
# d[i] = max(d[j] + a[i]), 0 <= j <= i - 1, a[j] < a[i]
# 정답 = max(d)
d = [0] * n

for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + a[i])

print(max(d))