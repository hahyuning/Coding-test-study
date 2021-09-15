n, m, k = map(int, input().split())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

# d[i][j][k]: i번째 주문까지 고려했을 때
# 남은 햄버거의 개수가 j개, 남은 감자튀김의 개수가 k개일 때
# 처리할 수 있는 최대 주문의 수
d = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n)]

for i in range(n):
    b, f = a[i]

    for j in range(1, m + 1):
        for k in range(1, k + 1):
            d[i][j][k] = d[i - 1][j][k]
            if b <= j and f <= k:
                d[i][j][k] = max(d[i - 1][j - b][k - f] + 1, d[i - 1][j][k])

print(d[n - 1][m][k])