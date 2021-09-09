n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# d[i][j] : i행 j열이 선택 되었을 때의 최대 합
d = [[0] * n for _ in range(n)]
d[0][0] = a[0][0]

for i in range(1, n):
    for j in range(0, i + 1):
        d[i][j] = d[i - 1][j] + a[i][j]
        if j >= 1:
            d[i][j] = max(d[i][j], d[i - 1][j - 1] + a[i][j])

print(max(d[n - 1]))