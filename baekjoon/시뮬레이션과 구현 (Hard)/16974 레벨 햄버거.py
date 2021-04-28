n, x = map(int, input().split())

# d[i]: 레벨 i 햄버거의 길이
d = [0] * (n + 1)
d[0] = 1

for i in range(1, n + 1):
    d[i] = 3 + 2 * d[i - 1]

# p[i]: 레벨 i 햄버거의 패티의 개수
p = [0] * (n + 1)
p[0] = 1

for i in range(1, n + 1):
    p[i] = 1 + 2 * p[i - 1]

# 실제로 햄버거 문자열을 만드는 것은 불가능
# 재귀함수 hamburger(n, x): 레벨 n 햄버거의 아래 x장을 먹었을 때 먹은 패티의 수
def hamburger(n, x):
    # 패티만 있는 경우
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1

    # 햄버거 번만 먹는 경우
    elif x == 1:
        return 0

    # x가 햄버거번, 레벨 n - 1 버거까지인 경우
    elif x <= 1 + d[n - 1]:
        return hamburger(n - 1, x - 1)
    # x가 햄버거번, 레벨 n - 1 버거, 패티까지인 경우
    elif x == 2 + d[n - 1]:
        return p[n - 1] + 1
    # x가 햄버거번, 레벨 n - 1 버거, 패티, 레벨 n - 1 버거 까지인 경우
    elif x <= 2 + 2 * d[n - 1]:
        return p[n - 1] + 1 + hamburger(n - 1, x - 2 - d[n - 1])
    # x가 전체인 경우
    else:
        return 1 + 2 * p[n - 1]

print(hamburger(n, x))
