n = int(input())
k = int(input())

if k == 1:
    print(n % 1000000003)
else:
    # d[i][j]: i 개의 색상환을 j 개의 색으로 채우는 경우의 수
    d = [[0] * (k + 1) for _ in range(n + 1)]


    for i in range(n + 1):
        d[i][1] = i
        d[i][0] = 1

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            # 마지막 색깔
            if i == n:
                d[i][j] = (d[i - 1][j] + d[i - 3][j - 1]) % 1000000003
            else:
                # j 번째 색을 사용하지 않는 경우 + j 번째 색을 사용하는 경우
                d[i][j] = (d[i - 1][j] + d[i - 2][j - 1]) % 1000000003

    print(d[n][k])