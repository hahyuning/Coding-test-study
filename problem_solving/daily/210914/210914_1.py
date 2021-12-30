n, m, h = map(int, input().split())
a = [[]]
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

# d[i][j]: i번째 학생까지 고려했을 때 높이가 j가 되는 경우의 수
d = [[0] * (h + 1) for _ in range(n + 1)]

for i in range(n + 1):
    d[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, h + 1):
        # i번째 학생의 블록을 사용하지 않는 경우
        d[i][j] = d[i - 1][j]

        # i번째 학생의 k번째 블록을 사용하는 경우
        for k in range(len(a[i])):
            if j >= a[i][k]:
                d[i][j] += d[i - 1][j - a[i][k]]
                d[i][j] %= 10007

print(d[n][h])