w, h = map(int, input().split())

# d[i][j][k][l]
# k: 방향 (0은 북쪽/1은 동쪽), l: 방향 전환 가능 여부 (0은 불가능/1은 가능),
d = [[[[0] * 2 for _ in range(2)] for _ in range(h)] for _ in range(w)]

for i in range(1, h):
    d[0][i][1][1] = 1
for i in range(1, w):
    d[i][0][0][1] = 1

for i in range(1, w):
    for j in range(1, h):
        # 동쪽 방향에서 들어오고, 방향 전환 불가능(직전에 방향 전환)
        d[i][j][0][0] = d[i - 1][j][1][1]
        # 동쪽 방향에서 들어오고, 방향 전환 가능
        d[i][j][0][1] = d[i - 1][j][0][0] + d[i - 1][j][0][1]

        # 북쪽 방향에서 들어오고, 방향 전환 불가능
        d[i][j][1][0] = d[i][j - 1][0][1]
        # 북쪽 방향에서 들어오고, 방향 전환 가능
        d[i][j][1][1] = d[i][j - 1][1][0] + d[i][j - 1][1][1]

ans = sum(d[-1][-1][0]) + sum(d[-1][-1][1])
print(ans % 100000)