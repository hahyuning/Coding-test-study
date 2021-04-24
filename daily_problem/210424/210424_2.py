n = int(input())
a = list(map(int, input().split()))
target = a[-1]
a = a[:-1]

# d[i][j]: i번째 수까지 사용했을 때 j를 만들 수 있는 방법의 수
d = [[0] * 21 for _ in range(n - 1)]
d[0][a[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if j - a[i] >= 0:
            d[i][j] += d[i - 1][j - a[i]]
        if j + a[i] <= 20:
            d[i][j] += d[i - 1][j + a[i]]

print(d[n - 2][target])

