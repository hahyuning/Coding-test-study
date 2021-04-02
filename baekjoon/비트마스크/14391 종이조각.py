n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

ans = 0
# 비트마스크 값이 0이면 행, 1이면 열
for s in range(1 << (n * m)):
    sum = 0
    # 행에 대해 검사
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i * m + j
            if (s & (1 << k)) == 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        # 마지막이 행으로 끝난 경우
        sum += cur

    # 열에 대해 검사
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i * m + j
            if (s & (1 << k)) != 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        # 마지막이 열로 끝난 경우
        sum += cur
    # 최대값 갱신
    ans = max(ans, sum)

print(ans)
