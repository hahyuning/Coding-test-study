n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
# d[n] : 카드 n개를 갖기위해 지불해야 하는 금액의 최솟값
# d[n] = min(d[n - j] + p[j]), 1 <= j <= n
d = [10000000] * 1001
d[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = min(d[i], d[i - j] + p[j])

print(d[n])