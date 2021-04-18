n, k = map(int, input().split())
w = [0]
v = [0]

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

# d[i][j]: i번째 물건까지 고려했을 때, 배낭에 넣은 무게의 합이 j일 때의 가치의 최대값
# i번째 물건을 넣지 않은 경우 = d[i - 1][j]
# i번째 물건을 넣은 경우 = d[i - 1][j - w[i]] + v[i]
d = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        # 무게 j를 만들때 i번째 물건을 썼냐 안썻냐 비교
        d[i][j] = d[i - 1][j]
        if j - w[i] >= 0:
            d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + v[i])

print(d[n][k])