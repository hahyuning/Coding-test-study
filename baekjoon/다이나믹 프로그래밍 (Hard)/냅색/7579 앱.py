# n: 활성화 된 앱의 수, m: 필요한 메모리
n, m = map(int, input().split())
# 현재 활성화 된 앱이 사용중인 메모리 리스트
a = [0] + list(map(int, input().split()))
# 앱을 비활성화 했을 경우의 비용
c = [0] + list(map(int, input().split()))

# d[i][j]: i 번째까지 앱에서 j 비용으로 만들 수 있는 최대 메모리
# i번째 앱을 비활성화 하지 않는 경우: d[i - 1][j]
# i번째 앱을 비활성화 하는 경우: d[i - 1][j - c[i]] + a[i]
# d[i][j] = min(d[i - 1][j], d[i - 1][j - c[i]] + a[i])
d = [[0] * (sum(c) + 1) for _ in range(n + 1)]
ans = sum(c)

for i in range(1, n + 1):
    for j in range(1, sum(c) + 1):
        d[i][j] = d[i - 1][j]
        if j - c[i] >= 0:
            d[i][j] = max(d[i][j], d[i - 1][j - c[i]] + a[i])

        if d[i][j] >= m:
            ans = min(ans, j)

print(ans)