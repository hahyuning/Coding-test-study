n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())

# d[i][j]: 소형기관차 i 대를 운영할 때 j 번째 객차 까지의 최대 운송 손님 수
# j번째 객차를 선택하지 않는 경우, j번째 객차를 선택하는 경우
d = [[0] * (n + 1) for _ in range(4)]
# s[i]: i번째 객차까지의 손님 수의 누적 합
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]

for i in range(1, 4):
    for j in range(1, n + 1):
        if j - m >= 0:
            d[i][j] = max(d[i][j - 1], d[i - 1][j - m] + s[j] - s[j - m])

print(d[3][n])